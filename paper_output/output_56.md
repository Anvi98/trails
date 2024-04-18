# Contrastive Learning On Multimodal Analysis Of Electronic Health Records

Tianxi Cai1,2⋆, Feiqing Huang1⋆, Ryumei Nakada3⋆, Linjun Zhang3⋆, Doudou Zhou1⋆
1Department of Biostatistics, Harvard T.H. Chan School of Public Health, Boston, MA
2Department of Biomedical Informatics, Harvard Medical School, Boston, MA
3Department of Statistics, Rutgers University, Piscataway, NJ
⋆alphabetical order

## Abstract

Electronic health record (EHR) systems contain a wealth of multimodal clinical data including structured data like clinical codes and unstructured data such as clinical notes. However, many existing EHR-focused studies has traditionally either concentrated on an individual modality or merged different modalities in a rather rudimentary fashion.

This approach often results in the perception of structured and unstructured data as separate entities, neglecting the inherent synergy between them. Specifically, the two important modalities contain clinically relevant, inextricably linked and complementary health information. A more complete picture of a patient's medical history is captured by the joint analysis of the two modalities of data. Despite the great success of multimodal contrastive learning on vision-language, its potential remains under-explored in the realm of multimodal EHR, particularly in terms of its theoretical understanding. To accommodate the statistical analysis of multimodal EHR data, in this paper, we propose a novel multimodal feature embedding generative model and design a multimodal contrastive loss to obtain the multimodal EHR feature representation. Our theoretical analysis demonstrates the effectiveness of multimodal learning compared to single-modality learning and connects the solution of the loss function to the singular value decomposition of a pointwise mutual information matrix. This connection paves the way for a privacy-preserving algorithm tailored for multimodal EHR feature representation learning. Simulation studies show that the proposed algorithm performs well under a variety of configurations. We further validate the clinical utility of the proposed algorithm in real-world EHR data.

Keywords: Natural language processing, textual data, structured data, representation learning, singular value decomposition.

## 1 Introduction

The growing accessibility of Electronic Health Record (EHR) data presents numerous opportunities for clinical research, ranging from patient profiling (Halpern et al., 2016) to predicting medical events (Choi et al., 2017). However, the complexity increases with the multimodal nature of EHR data, which encompasses diverse clinical data from patient demographics and genetic information to unstructured textual data like clinical notes, and structured data such as diagnostic and procedure codes, medication orders, and lab results.

A key challenge in EHR-focused research lies in effectively merging these different data types and ensuring that their clinical aspects are meaningfully represented. Research has shown the benefits of integrating structured and unstructured data for tasks like automated clinical code assignment (Scheurwegs et al., 2016), managing chronic diseases (Sheikhalishahi et al., 2019), and pharmacovigilance (Stang et al., 2010).

While these different modalities serve as complementary data sources, there is significant overlap and correlation among these data (Qiao et al., 2019). Joint representation of both structured and narrative data into a more manageable low-dimensional space where similar features are grouped closely can significantly improve the utility of both data types. This representation learning technique has gained popularity for its ability to capture and represent the intricate relationships among various EHR features.

Despite the extensive research on EHR feature representation, most existing studies have primarily focused on either structured (Choi et al., 2016a; Kartchner et al., 2017; Hong et al., 2021; Zhou et al., 2022) or unstructured data modalities (De Vine et al., 2014;
Choi et al., 2016b; Beam et al., 2019; Alsentzer et al., 2019; Huang et al., 2020; Lehman and Johnson, 2023). For instance, Alsentzer et al. (2019) adapted the BERT model (Devlin et al., 2019) to the clinical domain by training on the MIMIC-III clinical notes (Johnson et al., 2016). It was extremely time/resource-consuming to train such a black-box model. De Vine et al. (2014) aligned free-text features with the Unified Medical Language System (UMLS)'s common concept unique identifier (CUI) space (McInnes et al., 2007). They then utilized the skip-gram algorithm (Mikolov et al., 2013) on concatenated concept documents to learn the CUI embeddings. Similarly, Choi et al. (2016b) and Beam et al. (2019) employed singular value decomposition (SVD) on a pointwise mutual information (PMI) matrix derived from CUI co-occurrences in unstructured text to generate CUI embeddings.

This approach was also adopted by Hong et al. (2021) for code embeddings. This SVD- PMI algorithm not only ensures scalability but also upholds data privacy through the use of aggregate co-occurrence data, offering a scalable variant of the skip-gram algorithm (Levy and Goldberg, 2014). Its interpretability is further highlighted in the dynamic log-linear topic model developed by Arora et al. (2016).

Recent studies have emerged on leveraging multimodal EHR features for enhanced predictive modeling, as demonstrated by the work of Khadanga et al. (2019); Zhang et al. (2020); Bardak and Tan (2021); Gan et al. (2023). Specifically, Gan et al. (2023) enhanced code and CUI embeddings by employing the SVD-PMI algorithm, facilitating the integration of structured and unstructured data. Despite these advancements, methods relying on straightforward data merging may not fully account for the intricate interactions within multimodal data, potentially leading to biases. This issue will be further examined in our theoretical (Section 3) and numerical analyses (Sections 4 and 5).

Addressing these limitations, Liu et al. (2022) introduced a multimodal pre-trained language model incorporating a cross-attention mechanism to enrich EHR representations across structured and unstructured data domains.

Additionally, the domain has seen progress in multimodal contrastive learning strategies, as evidenced by research from Li and Gao (2022); Yin et al. (2023); Wang et al. (2023). These strategies, drawing inspiration from successful vision-language models like the Contrastive Language-Image Pre-Training (CLIP) by Radford et al. (2021), aim to train unified representations of diverse data modalities. However, these approaches, grounded in deep neural networks, face challenges due to their "black-box" nature, including a lack of theoretical underpinning, computational complexity, and concerns over privacy since they necessitate access to individual patient data. These factors contribute to their limited applicability in the context of EHR data.

While some theoretical analyses of multimodal learning exist, their applicability to EHR
data has been limited. Groundbreaking studies like Huang et al. (2021) have illustrated the benefits of multimodal learning, showing that learning across multiple modalities can reduce population risk compared to single-modality methods. Recently, Deng et al. (2023) theoretically proved the zero-shot transfer ability of CLIP. Furthermore, Nakada et al. (2023) explored multimodal contrastive learning's performance under a spiked covariance model. However, these studies do not directly apply to the unique discrete feature structure of EHR data, leaving an unaddressed theoretical gap in understanding multimodal contrastive learning's application in healthcare.

Bridging this gap is vital, as it lays a solid foundation for multimodal contrastive learning's development and implementation in healthcare, maximizing its potential to improve patient care and drive medical research forward.

To overcome these limitations, we introduce the Contrastive Learning Algorithm for Integrated Multimodal Electronic health records (CLAIME). Our findings confirm that CLAIME is not only an effective tool for deriving multimodal EHR feature representations but also a method that respects privacy by requiring only aggregated data. Additionally, we propose a novel multimodal feature embedding generative model (2.1) in Section 2.1, designed to enhance statistical analysis of multimodal EHR data. This model is notable for its interpretability and accurate portrayal of EHR data generation. It distinguishes itself from earlier word vector generative models (Arora et al., 2016, 2018; Lu et al., 2023; Xu et al., 2022) by (1) enabling the integration of multimodal EHR features, and (2) allowing patient heterogeneity by incorporating error terms specific to patients, thus increasing the model's robustness. Within this generative framework, we validate the consistency of the CLAIME algorithm and clarify the relationship between multimodal feature embeddings and a multimodal PMI matrix. The proposed algorithm is also privacy-preserving since it only requires summary-level data, opening doors for collaboration across multiple institutions. Our research also fills a theoretical void in the analysis of multimodal contrastive learning for EHR data.

The rest of the paper is structured as follows. Section 2 elaborates on the proposed method.

Section 3 presents the theoretical properties of our algorithm.

In Section 4, simulation studies demonstrate the algorithm's effectiveness under various configurations. Section 5 further validates our algorithm's clinical applicability in EHR studies. Finally, Section 6 includes discussions.

## 2 Method 2.1 Notation

For any matrix A, let ∥A∥, ∥A∥max and ∥A∥F be its operator norm, entrywise maximum norm and Frobenius norm, respectively. We define Pp(A) as the top-p right singular vectors of A. When the right singular vectors are not unique, we choose arbitrary singular vectors.

Denote sj(A) as the j-th largest singular value of A. Let Od,p (d ≥ p) denote a set of d × p orthonormal matrices. For two sequences of positive numbers {ak} and {bk}, we write ak ≲ bk or ak = O(bk) or bk ≳ ak or bk = Ω(ak) if there exists some constant *C >* 0 such that ak ≤ Cbk for all k. We denote ak ≪ bk or ak = o(bk) if limk→∞ ak/bk = 0. For any positive integer I, let [I] = {1, 2, · · · *, I*}. We write a ∨ b and a ∧ b to denote max(*a, b*) and min(*a, b*), respectively. We denote by ej the j-th unit vector in Rd where its j-th element is one, and all other elements are zero.

## 2.2 Model Assumptions

Assume that the collections of codes from the structured modality and CUIs from the unstructured modality are denoted by W(1) := [d1] and W(2) := [d] \ [d1] respectively, where d = d1 + d2, with d representing the total number of unique features across both modalities. Suppose that we have n independent patients. For each patient i, the observed

codes and CUIs are denoted as {w(1)
                                i,t }t∈[T (1)
                                      i
                                        ] and {w(2)
                                                i,t }t∈[T (2)
                                                      i
                                                        ], where w(1)
                                                                 i,t
                                                                     ∈ W(1) and

w(2)
 i,t ∈ W(2). The sizes of these sets are given by T (1)
                               i
                                 ≥ 2 and T (2)
                                       i
                                         ≥ 2, respectively. We

model the probability of observing specific codes and CUIs for the i-th patient based on their embeddings v⋆
w ∈ Rp as follows:

$$\mathbb{P}(w^{(1)}_{i,t}=w|\mathbf{c}_{i},\mathbf{\epsilon}^{(1)}_{i})=\frac{\exp(\langle\mathbf{v}^{*}_{w},\mathbf{c}_{i}\rangle+\epsilon_{i,w})}{\sum_{w^{\prime}\in W^{(1)}}\exp(\langle\mathbf{v}^{*}_{w^{\prime}},\mathbf{c}_{i}\rangle+\epsilon_{i,w^{\prime}})},\ \ w\in\mathcal{W}^{(1)},t\in[T^{(1)}_{i}],\ \text{and}\tag{2.1}$$ $$\mathbb{P}(w^{(2)}_{i,t}=w|\mathbf{c}_{i},\mathbf{\epsilon}^{(2)}_{i})=\frac{\exp(\langle\mathbf{v}^{*}_{w},\mathbf{c}_{i}\rangle+\epsilon_{i,w})}{\sum_{w^{\prime}\in W^{(2)}}\exp(\langle\mathbf{v}^{*}_{w^{\prime}},\mathbf{c}_{i}\rangle+\epsilon_{i,w^{\prime}})},\ \ w\in\mathcal{W}^{(2)},t\in[T^{(2)}_{i}].$$

Here $\mathbf{c}_{i}\sim N(\mathbf{0},\mathbf{I}_{p})$ represents a latent vector specific to patient $i$, reflecting their clinical 

state. The error terms, ϵ(1)
                        i
                           = (ϵi,1, . . . , ϵi,d1)⊤ ∼ N(0, Σ1) and ϵ(2)
                                                               i
                                                                  = (ϵi,d1+1, . . . , ϵi,d)⊤ ∼

N(0, Σ2), account for patient-specific variations and address the variability not captured

by the term ⟨v⋆
             w, ci⟩, where Σ1 and Σ2 are some unknown positive semi-definite matrices.

## 2.3 Claime Algorithm

We define code and CUI embedding matrices as V⋆
                                              1 = (v⋆
                                                    1, . . . , v⋆
                                                           d1)⊤ ∈ Rd1×p and V⋆
                                                                             2 =

(v⋆
  d1+1, . . . , v⋆
              d)⊤ ∈ Rd2×p, respectively, and aim to infer V⋆ =
                                                                       �
                                                                        V⋆⊤
                                                                          1 , V⋆⊤
                                                                                2
                                                                                  �⊤ ∈ Rd×p. The

embeddings should reflect clinical semantics, meaning that highly similar (e.g. rheumatoid arthritis and juvenile rheumatoid arthritis) or related (e.g. fasting glucose and type II diabetes) EHR entities should have close embeddings. Before introducing our algorithm,

we first define aggregate co-occurrence matrices C(M,M) and D(M,M′) for M, M ′ ∈ {1, 2}

across different modalities as:

$$\mathbf{C}^{(M,M)}(w,w^{\prime})=\sum_{i=1}^{n}\mathbf{C}_{i,i}^{(M,M)}(w,w^{\prime}),\ \ \mathbf{D}^{(M,M^{\prime})}(w,w^{\prime})=\sum_{i=1}^{n}\mathbf{D}_{i,i}^{(M,M^{\prime})}(w,w^{\prime})$$
where C(M,M)
i,j
(*w, w*′) =
��{(*t, s*) ∈ [T (M)
i
] × [T (M)
j
] : t ̸= *s, w*(M)
i,t
= *w, w*(M′)
j,s
= w′}
�� and D(M,M′)
i,j
(*w, w*′) =
��{(*t, s*) ∈ [T (M)
i
] × [T (M′)
j
] : w(M)
i,t
= *w, w*(M′)
j,s
= w′}
�� for *i, j* ∈ [n] and M *∈ {*1, 2}. Further, we define the marginal co-occurrence of w *∈ W*(M) as:

$$\gamma^{(M)}_{w}={\bf C}^{(M,M)}(w,\cdot)=\sum_{w^{\prime}\in{\cal W}^{(M)}}{\bf C}^{(M,M)}(w,w^{\prime}).\tag{2.2}$$
scaling factors. CLAIME utilizes the multimodal contrastive learning loss defined as:

We introduce S(M)
              q
                 = (n−1 �n
                          i=1(T (M)
                               i
                                  )q)1/q for q ≥ 1 and S(1,2)
                                                      1
                                                           = n−1 �n
                                                                   i=1 T (1)
                                                                       i
                                                                         T (2)
                                                                          i
                                                                             as

$$\begin{split}\mathcal{L}_{\text{CLIAME}}(\mathbf{V}_{1},\mathbf{V}_{2})&=\frac{1}{n(nS_{1}^{(1)}S_{1}^{(2)}-S_{1}^{(1,2)})}\sum_{i\neq j}\sum_{\in[T_{i}^{(1)}]}\sum_{s\in[T_{j}^{(2)}]}\frac{\langle\mathbf{v}_{w_{i}^{(1)}},\mathbf{v}_{w_{j}^{(2)}}\rangle}{\gamma_{w_{i}}^{(1)},\gamma_{w_{j}}^{(2)},}\\ &\quad-\frac{1}{nS_{1}^{(1,2)}}\sum_{i=1}^{n}\sum_{t\in[T_{i}^{(1)}]}\sum_{s\in[T_{i}^{(2)}]}\frac{\langle\mathbf{v}_{w_{i}^{(1)}},\mathbf{v}_{w_{j}^{(2)}}\rangle}{\gamma_{w_{i}}^{(1)},\gamma_{w_{i}}^{(2)},}+\frac{\lambda}{2}\|\mathbf{V}_{1}\mathbf{V}_{2}^{T}\|_{\text{F}}^{2}.\end{split}\tag{2.3}$$
Here V1 = (v1*, . . . ,* vd1)⊤ ∈ Rd1×p and V2 = (vd1+1, . . . , vd)⊤ ∈ Rd2×p, *λ >* 0 serves as a regularization coefficient, γ(M)
w
, M = 1, 2 are weights chosen based on the frequency of w, as defined in (2.2). Our theoretical analysis in Section 3 motivates the choice of γ(M)
w to guide the minimizer towards V⋆. The essence of the multimodal contrastive learning loss in CLAIME is to enhance the representation of similar features across different modalities by bringing them closer together while distancing those that are dissimilar. In the context of EHR data, this translates to aligning the embeddings of codes and CUIs that have clinical correlations and separating those that do not. The aim is to maximize the inner product of embeddings for features that co-occur within the same patient's data. Remark 2.1. Our CLAIME framework can be naturally extended to non-lienar loss functions. Note that our CLAIME loss function (2.3) can be written as

$$\mathcal{L}_{\text{CLIME}}(\mathbf{V}_{1},\mathbf{V}_{2})=-\frac{1}{\sum_{i=1}^{n}T_{i}^{(1)}T_{i}^{(2)}}\sum_{i=1}^{n}\left\{T_{i}^{(1)}T_{i}^{(2)}s_{ii}-\alpha\tau\sum_{j\neq i}^{n}T_{i}^{(1)}T_{j}^{(2)}s_{ij}\right\}+R(\mathbf{V}_{1},\mathbf{V}_{2}),$$

where $R(\mathbf{V}_{1},\mathbf{V}_{2})$ is a smooth regularizer, and

$$\alpha_{T}=\frac{\sum_{i=1}^{n}T_{i}^{(1)}T_{i}^{(2)}}{\sum_{i\neq j}^{n}T_{i}^{(1)}T_{j}^{(2)}},\ \ s_{ij}=\frac{1}{T_{i}^{(1)}T_{j}^{(2)}}\sum_{l\in[T_{i}^{(1)}]}\sum_{s\in[T_{j}^{(2)}]}\frac{\langle\mathbf{V}_{w_{ij}^{(1)},\mathbf{V}_{w_{ji}^{(2)}}\rangle}}{\gamma_{lw_{ij}^{(1)}}\gamma_{lw_{ij}^{(2)}}},\ \ \ \ \ i,j\in[n].$$

One can consider the following non-linear loss function analogous to the CLIP loss function.

(Radford et al., 2021):

$$\mathcal{L}^{\prime}_{\text{CLAME}}(\mathbf{V}_{1},\mathbf{V}_{2})=-\frac{1}{\sum_{i=1}^{n}T_{i}^{(1)}T_{i}^{(2)}}\sum_{i=1}^{n}T_{i}^{(1)}T_{i}^{(2)}\log\frac{\exp(s_{ii}/\tau)}{\sum_{j\neq i}^{n}T_{i}^{(1)}T_{j}^{(2)}\exp(s_{ij}/\tau)}+R(\mathbf{V}_{1},\mathbf{V}_{2}),$$

which becomes equivalent to the loss (2.3) when $\tau\to\infty$.

To obtain �V = ( �V⊤
1 , �V⊤
2 )⊤ = arg min LCLAIME(V1, V2) efficiently in practice, we note that LCLAIME(V1, V2) can be expressed in terms of pair-wise co-occurrences of concepts as:

$$n(nS_{1}^{(1)}S_{1}^{(2)}-S_{1}^{(1,2)})\sum_{w=d_{1}+1}^{d_{1}}\sum_{\gamma^{(1)}_{w}\gamma^{w}_{w^{\prime}}}^{d_{2}}\sum_{i=1}^{n}\sum_{j\neq i}^{n}\sum_{l\in\mathbb{T}^{(l)}_{i}\setminus e\in\mathbb{T}^{(l)}_{j})}\mathbb{I}(w_{i,t}^{(1)}=w)\mathbb{I}(w_{i,s}^{(2)}=w^{\prime})$$ $$-\frac{1}{nS_{1}^{(1,2)}}\sum_{w=1}^{d_{1}}\sum_{w=d_{1}+1}^{d_{2}}\frac{\langle\mathbf{v}_{w},\mathbf{v}_{w^{\prime}}^{*}\rangle}{\gamma^{(1)}_{w}\gamma^{(2)}_{w}}\sum_{i=1}^{n}\sum_{l\in\mathbb{T}^{(l)}_{i}\setminus e\in\mathbb{T}^{(l)}_{i})}\mathbb{I}(w_{i,t}^{(1)}=w)\mathbb{I}(w_{i,s}^{(2)}=w^{\prime})+\frac{\lambda}{2}\|\mathbf{V}_{1}\mathbf{V}_{2}^{\mathsf{T}}\|_{\mathrm{F}}^{2}\,.\tag{2.4}$$
Subsequently, via arguments given in Supplementary S2, we have the following proposition.

2 F + (constant), LCLAIME(V1, V2) = λ ���V1V⊤ 2 − 1 λ � PMICLAIME ��� 2
where �
PMICLAIME = { �
PMICLAIME(*w, w*′)}w∈W(1),w′∈W(2) with

, � � D(1,2)(*w, w*′) C(1,1)(w, ·)C(2,2)(w′, ·) D(1,2)(·, ·) − C(c)(*w, w*′) n(nS(1) 1 S(2) 1 − S(1,2) 1 ) � PMICLAIME(*w, w*′) := C(1,1)(·, ·)C(2,2)(·, ·)

and C(c)(w, w′) = �n
                 i=1
                   �n
                     j̸=i D(1,2)
                          i,j (w, w′).

Proposition 2.1 shows that LCLAIME(V1, V2) can be related to the SVD of an empirical

association matrix, where its element �
                                     PMICLAIME(w, w′) estimates the association between

the features w and w′. We will later demonstrate the convergence of �
                                                                       PMICLAIME to the

population PMI matrix in Section 3. As a result, �
                                                PMICLAIME(w, w′) can be viewed as a

modified estimator of the population PMI matrix. The final embeddings �V1 �V⊤
                                                                          2 are inferred

through a rank-p SVD of �
                        PMICLAIME, preserving data privacy and offering a scalable estimation. To be more specific, let �U1 �Λ �U2 denote the rank-p SVD of �
                                                                      PMICLAIME, where

�U1 ∈ Rd1×p and �U2 ∈ Rd2×p are the matrices of left and right singular vectors, respectively, and �Λ ∈ Rp×p is a diagonal matrix with its diagonal elements being the top p singular

of the regularization parameter λ does not play a crucial role, and for the sake of simplicity,

values. Then, we set �V1 = �U1 �Λ1/2 and �V2 = �U2 �Λ1/2. It is worth noting that the selection we will assign it a value of 1 in our upcoming numerical analyses.

## 2.4 Comparison Between Claime And Simple Concatenation

We next contrast CLAIME with the simple approach of ignoring between-modality differences between different modalities. Dealing with multimodal data often presents difficulties, leading to conventional methods that overlook the differences between various modalities. A basic strategy commonly adopted is to simply merge the two modalities through direct concatenation, after which algorithms initially intended for unimodal data are applied. However, this rudimentary treatment of multimodal data may lead to substantial bias due to the inherent heterogeneity between different modalities. To illustrate, consider the concatenated data for the i-th patient represented as

$\{w_{i,t}\}_{t\in[T_{i}]}=\left(w_{i,1}^{(1)},\ldots,w_{i,T_{i}^{(1)}}^{(1)},w_{i,1}^{(2)},\ldots,w_{i,T_{i}^{(2)}}^{(2)}\right)$, where $T_{i}=T_{i}^{(1)}+T_{i}^{(2)}$.

A popular method to handle such data is the SVD-PMI algorithm, as referenced in (Levy and Goldberg, 2014; Gan et al., 2023). In this context, we establish the co-occurrence matrices for the concatenated dataset as follows:

$$\mathbf{C}=\begin{bmatrix}\mathbf{C}^{(1,1)}&\mathbf{D}^{(1,2)}\\ \\ \mathbf{D}^{(2,1)}&\mathbf{C}^{(2,2)}\end{bmatrix},$$

where $\mathbf{C}^{(M,M)}$ and $\mathbf{D}^{(M,M^{\prime})}$ are defined in Section 2.3. Subsequently, the empirical concatenated PMI matrix, denoted as $\widehat{\mathsf{PMI}}=\{\widehat{\mathsf{PMI}}(w,w^{\prime})\}_{w,w^{\prime}\in[4]}$, is formulated as

$$\widehat{\mathsf{PMI}}(w,w^{\prime})=\log\frac{\mathbf{C}(w,w^{\prime})\mathbf{C}(\cdot,\cdot)}{\mathbf{C}(w,\cdot)\mathbf{C}(w^{\prime},\cdot)},\tag{2.5}$$

where $\mathbf{C}(w,\cdot)=\sum_{w^{\prime}=1}^{d}\mathbf{C}(w,w^{\prime})$ and $\mathbf{C}(\cdot,\cdot)=\sum_{w=1}^{d}\mathbf{C}(w,\cdot)$. Following this, we conduct a rank-$p$ eigen-decomposition of $\widehat{\mathsf{PMI}}$, represented as $\widehat{\mathbf{U}}_{\mathrm{Cou}}\widehat{\mathbf{A}}_{\mathrm{Cou}}\widehat{\mathbf{U}}_{\mathrm{Cou}}$. The estimator of 
rank-p eigen-decomposition of �
PMI, represented as �UCon �ΛCon �UCon. The estimator of V⋆
The second prevalent technique is contrastive learning (CL), applied directly to the is then achieved by setting �VCon = �UCon �Λ1/2
Con. We refer to this method as "Concate".

concatenated dataset. Specifically, we define the contrastive loss for V ∈ Rd×p as follows:

$$\begin{split}\mathcal{L}_{\text{CL}}(\mathbf{V})&=-\frac{1}{\sum_{i=1}^{n}T_{i}(T_{i}-1)}\sum_{i=1}^{n}\sum_{t\in[T_{i}]}\sum_{s\in[T_{i}](t)}\frac{\langle\mathbf{v}_{w_{i,t}},\mathbf{v}_{w_{i,s}}\rangle}{\gamma_{w_{i,t}}\gamma_{w_{i,s}}}\\ &\quad+\frac{1}{\sum_{i=1}^{n}\sum_{j\neq i}T_{i}T_{j}}\sum_{i\neq j}\sum_{t\in[T_{i}]}\sum_{s\in[T_{j}]}\frac{\langle\mathbf{v}_{w_{i,t}},\mathbf{v}_{w_{j,s}}\rangle}{\gamma_{w_{i,t}}\gamma_{w_{i,s}}}+\frac{\lambda}{2}\|\mathbf{V}\mathbf{V}^{\top}\|_{F}^{2},\end{split}\tag{2.6}$$

where $\gamma_{w}=\mathbf{C}(w,\cdot)$. Let $\widehat{\mathbf{V}}_{\text{CL}}=\arg\min\mathcal{L}_{\text{CL}}(\mathbf{V})$. Similar to Proposition 2.1, we have the 
following proposition. Here, we define

D =   i=1 C(c)⊤ C(2) j̸=i C(M,M) i,j (*w, w*′) for w, w′ ∈ W(M). n � n �  C(1) C(c)  with C(M)(*w, w*′) =
Proposition 2.2. We have

2 F + (constant), LCL(V) = λ ���VV⊤ − 1 λ � PMICL ��� 2 where � PMICL = { � PMICL(w, w′)}w,w′∈[d] with . � C(*w, w*′) � C(w, ·)C(w′, ·) C(·, ·) − D(*w, w*′) n(nS(1) 1 S(2) 1 − S(1,2) 1 ) � PMICL(*w, w*′) := C(·, ·)C(·, ·)
Proposition 2.2 reveals that obtaining �VCL by minimizing the loss LCL is essentially found in Supplementary S4.4. This method is referred to as CL. Nevertheless, as we will equivalent to applying PCA on the matrix �
PMICL. The proof for Proposition 2.2 can be demonstrate in Section 3, both �VCon and �VCL are not optimal solutions.

## 3 Theoretical Analysis

In this section, we investigate the theoretical properties of CLAIME and draw comparisons with the Concate and CL methods. First, let us establish some fundamental concepts. For

w ∈ W(M), and t ∈ [T (M)
             i
               ], denote X(M)
                      i,w (t) = I{w(M)
                              i,t
                                = w}. According to the model (2.1),

conditioned on ci and ϵ(M)
i
, the variable X(M)
i,w (t) follows a Bernoulli distribution, with the probability of occurrence given by

$$p_{i,w}^{(M)}=\mathbb{E}[X_{i,w}^{(M)}(t)|\mathbf{c}_{i},\mathbf{c}_{i}^{(M)}]=\frac{\exp(\langle\mathbf{v}_{w}^{*},\mathbf{c}_{i}\rangle+\epsilon_{i,w})}{\sum_{w^{\prime}\in W^{(M)}}\exp(\langle\mathbf{v}_{w^{\prime}}^{*},\mathbf{c}_{i}\rangle+\epsilon_{i,w^{\prime}})}\,.\tag{3.1}$$

Here, the probability $p_{i,w}^{(M)}$ is a function of the discourse vector $\mathbf{c}_{i}$ and the noise term 
ϵ(M)
i
, and is independent of t.

Next, we denote the expected value of p(M)
i,w as p(M)
w
=
E[p(M)
i,w ]. Further, we define the co-occurrence of a feature w *∈ W*(M) at time t for the i-th

patient and feature w′ ∈ W(M′) at time s for the j-th patient as X(M,M′)
                                                                  i,j,w,w′ (t, s) = I{w(M)
                                                                                   i,t
                                                                                       =

w, w(M′)
    j,s
        = w′} for t ̸= s. This variable follows a Bernoulli distribution, with the probability

of occurrence denoted as p(M,M′)
                         i,j,w,w′. Furthermore, we define the expected value for the case of

i = j as p(M,M′)
            w,w′
                    = E[p(M,M′)
                            i,i,w,w′ ]. It is important to note that when i ̸= j, the expected value

E[p(M,M′)
  i,j,w,w′] equals the product p(M)
                    w
                      p(M′)
                       w′
                         . Now, we introduce the population PMI matrix

PMI defined as

$$\mathbb{PMI}:=\begin{pmatrix}\mathbb{PMI}^{(1,1)}&\mathbb{PMI}^{(1,2)}\\ \\ \mathbb{PMI}^{(2,1)}&\mathbb{PMI}^{(2,2)}\end{pmatrix}\text{with}\mathbb{PMI}^{(M,M^{\prime})}(w,w^{\prime})=\log\frac{p_{w,w^{\prime}}^{(M,M^{\prime})}}{p_{w^{\prime}}^{(M^{\prime})}p_{w^{\prime}}^{(M^{\prime})}}\tag{3.2}$$

for $w\in\mathcal{W}^{(M^{\prime})}$, $w^{\prime}\in\mathcal{W}^{(M^{\prime})}$ with $M,M^{\prime}\in\{1,2\}$. Before proceeding with our theoretical 
analysis, let us establish some general assumptions. Based on our data generation model, we can only identify the left singular space and the singular values of V⋆
1 and V⋆
2. Thus, without loss of generality, we can assume that the singular value decomposition of V⋆
M is

V⋆
 M = U⋆
    MΛ⋆
      M for M ∈ {1, 2}, where U⋆
                     M ∈ OdM,p represents the left singular vectors,

and Λ⋆
     M ∈ Rp×p is a diagonal matrix containing the corresponding singular values. The

embedding can only be identified up to a mean shift. For simplicity, we assume V⋆⊤
M 1dM =
0.

p/dM, ∥Λ⋆
M∥/sp(Λ⋆
M) ≲ 1, Assumption 3.1. For M *∈ {*1, 2}, assume that ∥U⋆
M∥2,∞ ≲
�
and ∥Λ⋆
M∥ ≪ 1.

Assumption 3.1 is widely known as the incoherence constant condition in the literature appearing in matrix completion (Cand`es and Recht, 2009), PCA (Zhang et al., 2022), and the analysis of representation learning algorithm (Ji et al., 2021).

We introduce the notation d = min(d1, d2), and Σ = diag(Σ1, Σ2).

Assumption 3.2. Assume that log d ≪ d1 ∧ d2, p log12 d ≪ d1 ∧ d2, p ≪ (log log d)2, n ≫ p2d5 log2 d and p3 log6 d ≪ d3/2/d1/2.

Assumption 3.2 imposes a condition on the dimension of the low-rank representation.

This assumption is technically necessary in bounding the normalizing constant of the loglinear word production model (Lemma S5.2). Although, we can relax the assumption of p ≪ (log log d)2 into p ≪ log2 d, we stick to the current assumption for the sake of clarity.

Assumption 3.3. Assume that ∥diag(ΣM)∥max ≲ *p/d*M for M *∈ {*1, 2} and 1/p ≪ sp(Σ) ≤ ∥Σ1*∥ ∨ ∥*Σ2∥ ≲ 1.

Assumption 3.3 implies that the signal-to-noise ratio is bounded above and below.

Note that the signal, measured by the smallest positive singular value of (1/p)V⋆
MV⋆⊤
M′ for M, M ′ ∈ {1, 2} is of order 1/p from Assumption 3.1.

Theorem 3.1. Under Assumptions 3.1, 3.2 and 3.3, we have

$$\left\|\mathbb{P}\mathbb{M}\mathbb{I}^{(M,M)}-\left(\frac{1}{p}\mathbf{V}_{M}^{\star}\mathbf{V}_{M}^{\star\top}+\mathbf{\Sigma}_{M}\right)\right\|\lesssim\frac{p^{3/2}}{d_{M}}\log^{6}d,\ \ M\in\{1,2\}$$ $$\left\|\mathbb{P}\mathbb{M}\mathbb{I}^{(1,2)}-\frac{1}{p}\mathbf{V}_{1}^{\star}\mathbf{V}_{2}^{\star\top}\right\|\lesssim\frac{p^{3/2}}{d}\log^{6}d,$$
and hence

$$\left\|\mathbb{PMI}-\left(\frac{1}{p}\mathbf{V^{*}V^{*^{\top}}}+\mathbf{\Sigma}\right)\right\|\lesssim\frac{p^{2}}{d}\log^{6}d.$$

The proof of Theorem 3.1 is presented in Supplementary S4.1. This theorem demon
strates that the PMI matrix for each modality can be closely approximated by the embedding space plus the noise covariance matrix ΣM. When the noise level ΣM is substantial, the PMI value PMI(M,M)(*w, w*′) for a single modality may significantly deviate from ⟨v⋆
w, v⋆
w′⟩/p. On the other hand, the cross-modal PMI matrix PMI(1,2) can be directly estimator for PMI(1,2).

approximated by V⋆
                 1V⋆⊤
                    2 /p. The theorem below affirms that �
                                                       PMICLAIME is an effective

Theorem 3.5. *Suppose that* n ≫ d2 log2 d *and* ∥BCon∥ ∨ ∥BCL∥ ≪ 1/p. Under Assumptions 3.1-3.5,

pV⋆V⋆⊤ + Σ + BCon d log6 d, √n log d + p3 �1 ������ F ≲ p3/2d5/2 ����sin Θ � Pp( �V⊤ Con), Pp pV⋆V⋆⊤ + Σ + BCL d d log6 d �1/2p9/2 �1 √n log d + �d ����sin Θ � Pp( �V⊤ CL), Pp ������ F ≲ p3d5/2
holds with probability 1 − exp
�
−Ω(log2 d)
�
.

The proof Theorem 3.5 is given in Supplementary S4.4. It shows that both Concate and CL will yield biased estimators for the embeddings V⋆ due to the inherent bias terms and covariance matrix of the noise. While the bias terms BCon and BCL can be removed, the influence of Σ remains irreducible due to its unobserved nature. Comparing Theorems
3.3 and 3.5, we find that CLAIME achieves a sharper rate than Concate and CL even when BCL, BCon and Σ go to zero. As a result, CLAIME is a better estimator than Concate and CL.

To quantify the effect of BCon and BCL, we define the following empirical moments i∈[n] T (M)q i
)1/q. We also define the empirical cross-moments as of T (M)
i
: S(M)
q
:= ((1/n) �
i∈[n](T (1)
i
)q/2(T (2)
i
)q/2)1/q for q = 2, 4. Note that when the length of patient S(1,2)
q
:= ((1/n) �
data is the same, i.e., T (M)
i
= T (M) for all i ∈ [n] for M = 1, 2, S(M)
q
= T (M) for all q ≥ 1.

Assumption 3.5. For M = 1, 2, assume that 1 ≳ S(1)
                                          1 S(2)
                                             1 /S(1,2)2
                                                 2
                                                     ≫ 1/n, S(M)2
                                                             1
                                                                /S(M)2
                                                                  2
                                                                      ≫

1/n and S(M)2
        2
             ≫ S(M)
                1
                   . Also assume that S(M)
                                      1
                                         ≳ S(M)
                                             2
                                                ≳ S(M)
                                                   4
                                                       and S(1,2)
                                                            2
                                                                ≳ S(1,2)
                                                                   4
                                                                      .

Assumption 3.5 requires that the empirical variance of T (M)
                                                        i
                                                            dominates the mean of

T (M)
i
, and their moments are comparable to each other.

For the same length setting T (M)
i
≡ T (M) for all i ∈ [n], the assumption is satisfied if T (M) → ∞ and n *→ ∞*.

For the bias term BCon and BCL, we have the following lemma. The proof of Lemma 3.1
is given in Supplementary S4.7.

Lemma 3.1. Suppose that Assumption 3.5 holds. If T (1)
                                        i
                                           = T (2)
                                             i
                                               , then,

$$\|\mathbf{B}_{\mathrm{Con}}\|\;\forall\;\|\mathbf{B}_{\mathrm{CL}}\|\lesssim d{\frac{S_{1}^{(1)}}{S_{2}^{(1)2}}}.$$

Furthermore, if T (1)
                 i
                    = T (2)
                       i
                           ≡ T for all i ∈ [n] for some T > 0, then

T .

∥BCon∥ ∨ ∥BCL∥ ≲ d

We then characterize the effect of Σ.
                                       We will show that when Σ satisfies suitable

conditions, the two existing methods Concate and CL will not be an ideal estimator of V⋆.

(2/3)p.

Assumption 3.6. Assume ∥ sin Θ(U⋆
                              1, Pp(Σ1))∥F ∧ ∥ sin Θ(U⋆
                                                 2, Pp(Σ2))∥F ≥
                                                              �

Assumption 3.6 holds if the column space of Pp(Σ1) is nearly orthogonal to the column

space of U⋆
           1 and that of U⋆
                           2 nearly orthogonal to that of Pp(Σ2).
                                                                    Roughly speaking,

this assumption requires that we can well separate the features and noises based on their directions in each modality.

Theorem 3.6. Suppose that Assumptions 3.1-3.6 hold. If ∥BCon∥ ∨ ∥BCL∥ ≪ 1, then,

∥ sin Θ( �UCon, U⋆)∥F ≳ √p
                        and
                             ∥ sin Θ( �UCL, U⋆)∥F ≳ √p

with probability 1 − exp
                        �
                         −Ω(log2 d)
                                     �
                                      .

The formal statement is available in Theorem S4.8.
                                                   Theorem 3.6 shows that there

is a huge deviation from the estimators of Concate and CL to the true parameters as

∥ sin Θ( �UCon, U⋆)∥F and ∥ sin Θ( �UCL, U⋆)∥F are both lower bounded by the order of √p.

Since for any �U, U⋆ ∈ Od,p, ∥ sin Θ( �U, U⋆)∥F can be trivially upper bounded by √p, this

We present an example construction of the error covariance matrix where we expect to

result shows that �UCon and �UCL can hardly capture any signal in U⋆.

see the performance difference among CLAIME, Concate, and CL.

Corollary 3.1. Choose P(1) ∈ Od1,p satisfying [U⋆
                                            1; P(1)] ∈ Od1,2p and ∥[U⋆
                                                                  1; P(1)]∥2
                                                                         2,∞ ≲

p/d1. Similarly choose P(2) ∈ Od2,p such that [U⋆
                                        2; P(2)] ∈ Od2,2p and ∥[U⋆
                                                             2; P(2)]∥2
                                                                   2,∞ ≲ p/d2.

Let Σ1 := P(1)P(1)⊤, Σ2 := (1/2)P(2)P(2)⊤, V⋆
                                              1 = U⋆
                                                     1 and V⋆
                                                             2 = U⋆
                                                                    2. For these noise

covariance matrices, Assumptions 3.1, 3.3 and 3.4 hold. In addition, Assumption 3.6 holds

since P(1)⊤V⋆
             1 = P(2)⊤V⋆
                        2 = Op×p. Under additional assumptions on (T (M)
                                                                        i
                                                                           )i∈[n], d1 and d2

(Assumptions 3.2 and 3.5), we obtain

$$\|\sin\Theta(\widehat{\mathbf{U}}_{\mathrm{Con}},\mathbf{U}^{*})\|_{\mathrm{F}}\gtrsim\sqrt{p},\ \ \|\sin\Theta(\widehat{\mathbf{U}}_{\mathrm{CL}},\mathbf{U}^{*})\|_{\mathrm{F}}\gtrsim\sqrt{p}\quad\text{and}$$

$$\min_{\mathbf{H}\in\mathcal{D}_{\mathrm{Pr}}}\|\sin\Theta(\widehat{\mathbf{U}}_{\mathbf{H}},\mathbf{U}^{*})\|_{\mathrm{F}}\lesssim\frac{p^{3/2}d^{5/2}d}{\sqrt{n}}\log d+\frac{p^{3}}{d}\log^{6}d.$$

Corollary 3.1 directly follows from Theorems 3.3 and 3.6. Note that the factor $1/2$ in 
the definition of Σ2 guarantees the eigengap condition at the p-th largest singular value of the joint noise covariance matrix Σ. The noise covariance in Corollary 3.1 implies that the subspace spanned by the noise is orthogonal to the subspace spanned by the signal, so that the noisy fluctuations in feature frequency distribution occurs simultaneously to many words, in a separable way from the signal. Under this condition, Concate and CL learn the eigenspace corresponding to noise covariance matrix, since those methods are vulnerable to large noise strength. On the other hand, CLAIME can effectively escape from the noise, and learns core representations when n and ¯d are sufficiently large.

## 4 Simulation Studies

In this section, we assess CLAIME's performance and compare it to CL and Concate via simulation studies. When patient-level data is not available, these three methods can be deployed by performing SVD on different aggregated PMI matrices introduced in Section 2. Since patient-level data is also available in the synthesized datasets, we can additionally apply the gradient descent-based multimodal contrastive learning method (CLAIME-GD) with target function at (2.3), and the gradient descent-based contrastive learning method (CL-GD) with target function at (2.6), respectively. The suffix "-GD" is added to distinguish them from their SVD-based counterparts. To enhance training efficiency, only 10 negative samples per patient are stochastically sampled. The penalty parameter λ is set to 1, while the learning rate starts at 10−4 and decays by a factor of 10 every 10 epochs to ensure convergence. Both gradient-based algorithms converge when their loss functions change by less than 10−6.

We generate patient embedding vector ci ∈ Rp for each patient i from a multivariate normal distribution N(0, Ip) independently. We construct the code and CUI embedding matrices V⋆
1 ∈ Rd1×p and V⋆
2 ∈ Rd2×p, respectively, by generating each entry from a standard normal distribution. The row means of V⋆
1 and V⋆
2 are standardized to zero, and their maximum singular values are standardized to 1. Then, we follow the data generation process in (2.1) to generate T (1)
i number of codes and T (2)
i number of CUIs for the i-th patient, where T (1)
i
, T (2)
i follow a Poisson distribution with the mean of 50 and only nonzero values are retained. Two different cases of error covariance structures are considered.

For Case 1, we set Σ(M) = diag(Ip/2, 0)/c ∈ RdM×dM for M = 1 or 2, where *c >* 0 is a constant controlling the signal-to-noise ratio (SNR) of the data generating process. For

Case 2, we generated σw
                        i.i.d.
                        ∼ Unif(0, 1) and set Σ(M)
                                               w,w′ = ρ|w−w′|σwσw′/2 for w, w′ ∈ [dM]

and M *∈ {*1, 2}, where ρ ∈ (0, 1) controls both the structure and the SNR of the data generating process. Specifically, a larger ρ leads to a greater signal-to-noise ratio in the synthesized data.

For both cases, three experiments are separately conducted to compare the performance of CLAIME, CLAIME-GD, CL, CL-GD, and Concate under different sample sizes n, feature sizes d, and SNR. Their performance is evaluated using the metric Err( �V, V⋆) =
true embedding subspaces. We first fix the SNR by setting c = 0.2 for Case 1 and ρ = 0.8

maxM=1,2 ∥ �VM �V⊤
           M − V⋆
                MV⋆⊤
                   M ∥F, which measures the distance between the estimated and

for Case 2. In the first experiment, we vary the sample sizes n in {2 × 104, 4 × 104, 6 ×

104, 8 × 104, 105}, while fixing d = 2d1 = 2d2 = 1000 and p = 4. In the second experiment, we vary d in {200, 400, 600, 800, 1000} and set d1 = d2 = d/2, while fixing n = 105 and p = 4. For the third experiment, we first fix n = 105, d = 2d1 = 2d2 = 1000 and p = 4.

Then, we vary c equally spaced between 0.2 and 1 for Case 1, and we vary ρ equally spaced between 0 and 0.9 for Case 2.

The results for CL and CL-GD, CLAIME and CLAIME-GD are very close to each other, The error metrics Err( �V, V⋆), averaged over 500 repetitions, are presented in Figure 1.

as indicated by the proximity of their lines in Figures 1 (a)–(c). This suggests that employing gradient-based methods on patient-level data (i.e., CL-GD and CLAIME-GD) is comparable to utilizing SVD on summary-level PMI matrices (i.e., CL and CLAIME). This observation aligns with the theoretical findings in Propositions 2.1 and 2.2. On one hand, in Figures 1(a) and (b), the errors for CLAIME and CLAIME-GD decrease with an increase in n or a decrease in d. This behavior is anticipated and can be theoretically inferred from the upper bounds provided in Theorems 3.1 - 3.3. In contrast, the errors for Concate, CL, and CL-GD remain unchanged. This can be theoretically justified by their lower bounds being irrelevant to both n and d, as shown in Theorem 3.6. From the top panel of Figure 1(c), it can be observed that all methods exhibit larger errors when c decreases, or in other words, the SNR decreases. Comparing to the other methods, CLAIME and CLAIME-GD
demonstrate superior performance in the small SNR regions where c ≤ 0.5. Similarly, the bottom panel of Figure 1(c) shows a consistent increase in errors across all methods with higher values of ρ. CLAIME and CLAIME-GD again significantly outperform the other methods when ρ is larger than 0.5. This supports our initial motivation that the proposed method will be more robust in cases when the data is noisier.

## 5 Application To Electronic Health Records Studies

We consider training a joint representation of codified and narrative CUI features using summary EHR data of patients with at least 1 diagnostic code of rhematoid arthritis (RA) at Mass General Brigham (MGB). The MGB RA EHR cohort consist of 53,716 patients whose longitudinal EHR data have been summarized as co-occurrence counts of EHR concepts within a 30-day window. We include all EHR diagnosis, medication, and procedure codes which have been rolled up to higher concept levels: diagnostic codes to PheCodes1, procedure codes to clinical classification system (CCS)2, medication codes to ingredient level RxNorm codes (Liu et al., 2005). We include all EHR codified features along with CUIs that have occurred more than 15 times in the cohort. This results in d = 4, 668
features, including d1 = 3, 477 codified features with 1, 776 PheCodes for diseases, 238 CCS codes for procedures, and 1, 463 RxNorm codes for medications, and d2 = 1, 048 CUI
features.

Based on the summary-level co-occurrence matrix, we can derive estimators for CLAIME, CL, and Concate, respectively. To assess the quality of the obtained embeddings, we utilize a benchmark previously introduced in Gan et al. (2023). Specifically, we conduct an evaluation focusing on the embeddings' capability to identify established relationships among EHR concept pairs. Various categories of known relations, including similarity and relatedness, have been curated from online knowledge sources. Similar pairs of codified concepts were mainly generated based on code hierarchies such as the PheCode hierarchy. Similar pairs of CUIs were extracted from relationships within the online clinical database UMLS. Additionally, we assessed the similarity between mapped code-CUI pairs, leveraging UMLS to map codified concepts to CUIs. For relatedness among CUI-CUI pairs, we extracted information from the UMLS, considering major classes like "may treat or may prevent", "classifies", "differential diagnosis", "method of", and "causative". Furthermore, related code-CUI pairs and code-code pairs were curated by mapping disease CUIs to PheCodes, drugs to RxNorm, and procedures to CCS categories. These mapped code pairs were then utilized to evaluate the system's ability to detect relatedness among codified features or the relatedness between codified and NLP features.

vectors of related pairs and randomly selected pairs. This approach enables the calculation of the Area Under the Curve (AUC) of the cosine similarities, providing a metric for distinguishing known pairs from random pairs. The random pairs selected have the same semantic type as the known pairs. For example, in investigating the relationship "may treat or may prevent," we only consider disease-drug pairs. This evaluation strategy allows us to quantify and compare the performance of the EHR embeddings across various relationship types.

The results are presented in Table 1. It can be observed that CLAIME excels in embedding relationships across two distinct modalities: code and CUIs. In particular, for the similar CUI-RxNorm group, CLAIME achieves about 6% gain in AUC compared to CL and Concate. It is also much better at capturing causative relationships between codes and CUIs, achieving a 4.4% gain in AUC. Moreover, CLAIME is slightly better in representing the parent-child hierarchical relationships between NLP concepts, with a 2% gain in AUC compared to the other two methods.

Since the data comes from the RA cohort, it is of interest for us to further perform case studies for RA-related codified and CUI concepts. We select 7 key concepts for detailed analysis: rheumatoid arthritis, C-reactive proteins, stiffness of joint, Reiter's disease, swollen joint, pneumococcal vaccine, and leflunomide.

For each of the 7 concepts, we calculate its cosine similarity with all remaining concepts using the embeddings generated by CLAIME, Concate, and CL, respectively. Concepts are ranked by similarity, and a subset comprising the top-100 rankings from any one of the three methods is chosen as positive control. Then, we randomly select an equal number of other concepts as negative controls. This process produces an evaluation set for each of the 7 concepts. Concordance between similarity scores (from CLAIME, Concate, CL) and

| Pairs               | Type                |   Group |   CLAIME |        CL |   Concate |
|---------------------|---------------------|---------|----------|-----------|-----------|
| CUI-PheCode         | 0.920               |   0.92  |    0.92  |   345     |           |
| Similar             | CUI-RXNORM          |   0.972 |    0.919 |     0.918 |        49 |
| summary             | 0.915               |   0.91  |    0.909 |   394     |           |
| May Treat (Prevent) | 0.775               |   0.753 |    0.753 |  1302     |           |
| CUI-Code            | Classifies          |   0.905 |    0.895 |     0.895 |       744 |
| Related             | ddx                 |   0.773 |    0.765 |     0.766 |      1169 |
| Causative           | 0.775               |   0.741 |    0.742 |   524     |           |
| summary             | 0.800               |   0.783 |    0.784 |  3739     |           |
| Parent              | 0.848               |   0.855 |    0.856 |   422     |           |
| Similar             | Sibling             |   0.796 |    0.763 |     0.766 |       865 |
| summary             | 0.813               |   0.794 |    0.796 |  1287     |           |
| May Treat (Prevent) | 0.767               |   0.765 |    0.766 |   257     |           |
| CUI-CUI             |                     |         |          |           |           |
| Classifies          | 0.936               |   0.924 |    0.925 |    45     |           |
| Related             | ddx                 |   0.741 |    0.771 |     0.773 |        95 |
| Method of           | 0.809               |   0.796 |    0.8   |    15     |           |
| summary             | 0.756               |   0.752 |    0.752 |   421     |           |
| Similar             | PheCode Hierachy    |   0.914 |    0.909 |     0.909 |      3868 |
| ddx                 | 0.790               |   0.796 |    0.795 |  5819     |           |
| Classifies          | 0.896               |   0.9   |    0.9   |  4525     |           |
| Code-Code           |                     |         |          |           |           |
| Related             | May Treat (Prevent) |   0.734 |    0.727 |     0.725 |      4598 |
| Causative           | 0.754               |   0.756 |    0.754 |  2468     |           |
| summary             | 0.798               |   0.799 |    0.798 | 17410     |           |

relevance scores (from GPT3.5 (OpenAI, 2023), GPT4 (Achiam et al., 2023) ) is assessed using Kendall's tau rank correlation. Relevance scores are obtained by prompting GPT3.5
and GPT4 to rate concept relevance on a scale of 0 to 1 between the given concept and its respective evaluation set.

The results, depicted in Figure 2, reveal that Concate and CL exhibit remarkably similar behavior, with the "CL-GPTx" lines obscured beneath "Concate-GPTx". CLAIME can effectively encode and preserve relations between these medical concepts and their associated features. Notably, negative rank correlations can be observed for CL-GPT3.5/4
and Concate-GPT3.5/4 regarding "leflunomide" and "pneumococcal vaccine" related codes and CUIs. To gain more insights, some detailed examples are provided in Table 2.

| ID                                                  | Desc                                       |   Concate |   CL |   CLAIME |   GPT3.5 |   GPT4 |
|-----------------------------------------------------|--------------------------------------------|-----------|------|----------|----------|--------|
| Relatedness or similarity with Leflunomide          |                                            |           |      |          |          |        |
| PheCode:714.1                                       | Rheumatoid arthritis                       |      0.35 | 0.35 |     0.8  |      0.9 |    0.9 |
| PheCode:714.2                                       | Juvenile rheumatoid arthritis              |      0.36 | 0.37 |     0.78 |      0.9 |    0.8 |
| C0242708                                            | DMARDs                                     |           |      |          |          |        |
| 0.36                                                | 0.36                                       |      0.81 | 0.9  |     1    |          |        |
| RXNORM:5487                                         | Hydrochlorothiazide                        |      0.8  | 0.81 |     0.01 |      0.1 |    0.2 |
| RXNORM:6809                                         | Metformin                                  |      0.79 | 0.79 |     0.01 |      0.2 |    0.2 |
| RXNORM:2556                                         | Citalopram                                 |           |      |          |          |        |
| 0.78                                                | 0.78                                       |      0.05 | 0.1  |     0.1  |          |        |
| Relatedness or similarity with Pneumococcal vaccine |                                            |           |      |          |          |        |
| C0151735                                            | Injection site reaction NOS                |      0.29 | 0.29 |     0.74 |      0.8 |    0.8 |
| CCS:228                                             | Prophylactic vaccinations and inoculations |           |      |          |          |        |
| 0.29                                                | 0.29                                       |      0.64 | 0.9  |     1    |          |        |
| C1445860                                            | Protein antibody                           |      0.04 | 0.04 |     0.61 |      0.6 |    0.7 |
| RXNORM:10689                                        | Tramadol                                   |      0.8  | 0.8  |     0.12 |      0.1 |    0.1 |
| RXNORM:2556                                         | Citalopram                                 |           |      |          |          |        |
| 0.75                                                | 0.75                                       |      0.15 | 0.1  |     0.1  |          |        |
| RXNORM:11248                                        | Cyanocobalamin                             |      0.81 | 0.81 |     0.18 |      0.2 |    0.1 |

More specifically, leflunomide is a type of disease-modifying antirheumatic drugs (DMARDs)
used to treat rheumatoid arthritis by reducing inflammation and permanent damage. Table 2 shows that both Concate and CL fail to capture the close connection between leflunomide, RA, and DMARDs. Additionally, they overestimate similarity with unrelated drugs like hydrochlorothiazide, metformin, and citalopram. In the case of pneumococcal vaccine, it is a vaccine targeting streptococcus pneumoniae infections and can potentially cause injection site reactions. It is related to protein antibodies as they all target the immune system (von Elten et al., 2014). Both Concate and CL struggle to capture this similarity and instead overestimate similarity with unrelated drugs like tramadol, cyanocobalamin, and citalopram, used for pain relief, vitamin B12 deficiency, and depressive disorders respectively.

## 6 Discussion And Conclusion

In this paper, we propose the noisy multimodal log-linear production model for analyzing the multimodal EHR data and present the privacy-preserving algorithm CLAIME to estimate the multimodal feature embeddings with theoretical justification. Our algorithm is readily available for federated learning when multiple healthcare systems want to co-train their model but can not share patient-level data. It is also of great interest to consider a setting where different systems have overlapping but non-identical feature sets, in which case a block-wise matrix completion algorithm may be useful (Zhou et al., 2021).

Although our current analysis focuses on two modalities, it can be extended to more than two modalities. The rich EHR data contains many different modalities such as genetic data and image data. It will be interesting to extend our current framework to accommodate these data. Besides, it will also be interesting to incorporate the patient demographic in the generative model to consider the effects of variables like sex and age.

This paper focuses on a linear loss function, while non-linear loss functions such as mentioned in Remark 2.1 also deserve to be explored.

Another interesting problem is the estimation of the patient embedding ci. The patient embedding is useful for many downstream tasks such as identifying "patients like me".

## References

Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D.,
Altenschmidt, J., Altman, S., Anadkat, S., et al. (2023). GPT-4 technical report. arXiv preprint arXiv:2303.08774.
Alsentzer, E., Murphy, J. R., Boag, W., Weng, W.-H., Jin, D., Naumann, T., and
McDermott, M. (2019).
Publicly available clinical bert embeddings.
arXiv preprint
arXiv:1904.03323.
Arora, S., Li, Y., Liang, Y., Ma, T., and Risteski, A. (2016). A latent variable model
approach to pmi-based word embeddings. Transactions of the Association for Computational Linguistics, 4:385–399.
Arora, S., Li, Y., Liang, Y., Ma, T., and Risteski, A. (2018).
Linear algebraic structure of word senses, with applications to polysemy. Transactions of the Association for
Computational Linguistics, 6:483–495.
Bardak, B. and Tan, M. (2021). Improving clinical outcome predictions using convolution over medical entities with multimodal learning. *Artificial Intelligence in Medicine*,
117:102112.
Beam, A. L., Kompa, B., Schmaltz, A., Fried, I., Weber, G., Palmer, N., Shi, X., Cai,
T., and Kohane, I. S. (2019). Clinical concept embeddings learned from massive sources of multimodal medical data. In *PACIFIC SYMPOSIUM ON BIOCOMPUTING 2020*,
pages 295–306. World Scientific.
Cand`es, E. J. and Recht, B. (2009). Exact matrix completion via convex optimization.
Foundations of Computational mathematics, 9(6):717–772.
Choi, E., Bahadori, M. T., Searles, E., Coffey, C., Thompson, M., Bost, J., Tejedor-Sojo,
J., and Sun, J. (2016a). Multi-layer representation learning for medical concepts. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, pages 1495–1504.
Choi, E., Schuetz, A., Stewart, W. F., and Sun, J. (2017). Using recurrent neural network models for early detection of heart failure onset. Journal of the American Medical
Informatics Association, 24(2):361–370.
Choi, Y., Chiu, C. Y.-I., and Sontag, D. (2016b). Learning low-dimensional representations
of medical concepts. *AMIA Summits on Translational Science Proceedings*, 2016:41–50.
De Vine, L., Zuccon, G., Koopman, B., Sitbon, L., and Bruza, P. (2014). Medical semantic
similarity with a neural language model. In Proceedings of the 23rd ACM International
Conference on Information and Knowledge Management, pages 1819–1822.
Deng, Y., Prasad, K., Fernandez, R., Smolensky, P., Chaudhary, V., and Shieber, S.
(2023). Implicit chain of thought reasoning via knowledge distillation. arXiv preprint
arXiv:2311.01460.
Devlin, J., Chang, M., Lee, K., and Toutanova, K. (2019). BERT: pre-training of deep
bidirectional transformers for language understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, NAACL-HLT, pages 4171–4186.
Gan, Z., Zhou, D., Rush, E., Panickan, V. A., Ho, Y.-L., Ostrouchov, G., Xu, Z., Shen,
S., Xiong, X., Greco, K. F., Hong, C., Bonzel, C.-L., Wen, J., Costa, L., Cai, T., Begoli, E., Xia, Z., Gaziano, J. M., Liao, K. P., Cho, K., Cai, T., and Lu, J. (2023). Arch:
Large-scale knowledge graph via aggregated narrative codified health records analysis. medRxiv.

Halpern, Y., Horng, S., Choi, Y., and Sontag, D. (2016). Electronic medical record phenotyping using the anchor and learn framework. Journal of the American Medical Informatics Association, 23(4):731–740.
Hong, C., Rush, E., Liu, M., Zhou, D., Sun, J., Sonabend, A., Castro, V. M., Schubert,
P., Panickan, V. A., Cai, T., et al. (2021). Clinical knowledge extraction via sparse
embedding regression (KESER) with multi-center large scale electronic health record data. *NPJ digital medicine*, 4(1):1–11.
Huang, K., Singh, A., Chen, S., Moseley, E., Deng, C.-Y., George, N., and Lindvall, C.
(2020). Clinical XLNet: Modeling sequential clinical notes and predicting prolonged mechanical ventilation. In Proceedings of the 3rd Clinical Natural Language Processing
Workshop, pages 94–100, Online. Association for Computational Linguistics.
Huang, Y., Du, C., Xue, Z., Chen, X., Zhao, H., and Huang, L. (2021). What makes multimodal learning better than single (provably). Advances in Neural Information Processing
Systems, 34:10944–10956.
Ji, W., Deng, Z., Nakada, R., Zou, J., and Zhang, L. (2021). The power of contrast for
feature learning: A theoretical analysis. *arXiv preprint arXiv:2110.02473*.
Johnson, A. E., Pollard, T. J., Shen, L., Lehman, L.-w. H., Feng, M., Ghassemi, M.,
Moody, B., Szolovits, P., Anthony Celi, L., and Mark, R. G. (2016). MIMIC-III, a freely accessible critical care database. *Scientific Data*, 3(1):1–9.
Kartchner, D., Christensen, T., Humpherys, J., and Wade, S. (2017). Code2vec: Embed-
ding and clustering medical diagnosis data. In 2017 IEEE International Conference on Healthcare Informatics (ICHI), pages 386–390.

Khadanga, S., Aggarwal, K., Joty, S., and Srivastava, J. (2019). Using clinical notes with
time series data for ICU management. In Inui, K., Jiang, J., Ng, V., and Wan, X., editors, Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 6432–6437, Hong Kong, China. Association for Computational
Linguistics.
Lehman, E. and Johnson, A. (2023). Clinical-t5: Large language models built using mimic
clinical text. *PhysioNet*.
Levy, O. and Goldberg, Y. (2014). Neural word embedding as implicit matrix factorization.
In *Advances in Neural Information Processing Systems*, volume 27.
Li, R. and Gao, J. (2022). Multi-modal contrastive learning for healthcare data analytics.
In *2022 IEEE 10th International Conference on Healthcare Informatics (ICHI)*, pages
120–127. IEEE.
Liu, S., Ma, W., Moore, R., Ganesan, V., and Nelson, S. (2005). RxNorm: prescription for
electronic drug information exchange. *IT professional*, 7(5):17–23.
Liu, S., Wang, X., Hou, Y., Li, G., Wang, H., Xu, H., Xiang, Y., and Tang, B. (2022).
Multimodal data matters: language model pre-training over structured and unstructured electronic health records. *IEEE Journal of Biomedical and Health Informatics*, 27(1):504–
514.
Lu, J., Yin, J., and Cai, T. (2023). Knowledge graph embedding with electronic health
records data via latent graphical block model. *arXiv preprint arXiv:2305.19997*.
McInnes, B. T., Pedersen, T., and Carlis, J. (2007). Using UMLS Concept Unique Identifiers (CUIs) for word sense disambiguation in the biomedical domain. In AMIA Annual
Symposium Proceedings, volume 2007, pages 533–537. American Medical Informatics Association.
Mikolov, T., Chen, K., Corrado, G., and Dean, J. (2013). Efficient estimation of word
representations in vector space. *Proceedings of Workshop at ICLR*, 2013.
Nakada, R., Gulluk, H. I., Deng, Z., Ji, W., Zou, J., and Zhang, L. (2023). Understanding multimodal contrastive learning and incorporating unpaired data. In International
Conference on Artificial Intelligence and Statistics, pages 4348–4380. PMLR.
OpenAI (2023). ChatGPT: Optimizing language models for dialogue. URL: https://openai.
com/blog/chatgpt.
Qiao, Z., Wu, X., Ge, S., and Fan, W. (2019). Mnn: multimodal attentional neural networks
for diagnosis prediction. *Extraction*, 1(2019):A1.
Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell,
A., Mishkin, P., Clark, J., et al. (2021). Learning transferable visual models from natural language supervision. In *International conference on machine learning*, pages 8748–8763.
PMLR.
Scheurwegs, E., Luyckx, K., Luyten, L., Daelemans, W., and Van den Bulcke, T. (2016).
Data integration of structured and unstructured sources for assigning clinical codes to patient stays. *Journal of the American Medical Informatics Association*, 23(e1):e11–e19.
Sheikhalishahi, S., Miotto, R., Dudley, J. T., Lavelli, A., Rinaldi, F., Osmani, V., et al.
(2019). Natural language processing of clinical notes on chronic diseases: systematic review. *JMIR medical informatics*, 7(2):e12239.
Stang, P. E., Ryan, P. B., Racoosin, J. A., Overhage, J. M., Hartzema, A. G., Reich, C.,
Welebob, E., Scarnecchia, T., and Woodcock, J. (2010). Advancing the science for active surveillance: rationale and design for the observational medical outcomes partnership. Annals of Internal Medicine, 153(9):600–606.
von Elten, K. A., Duran, L. L., Banks, T. A., Banks, T. A., Collins, L. C., and Collins,
L. C. (2014). Systemic inflammatory reaction after pneumococcal vaccine: a case series. Human Vaccines & Immunotherapeutics, 10(6):1767–1770.
Wang, X., Luo, J., Wang, J., Yin, Z., Cui, S., Zhong, Y., Wang, Y., and Ma, F.
(2023). Hierarchical pretraining on multimodal electronic health records. arXiv preprint
arXiv:2310.07871.
Xu, Z., Shen, S., Gan, Z., Doudou, Z., Cai, T., and Lu, J. (2022). Codes clinical correlation
test with inference on pmi matrix. Preprint.
Yin, Q., Zhong, L., Song, Y., Bai, L., Wang, Z., Li, C., Xu, Y., and Yang, X. (2023).
A decision support system in precision medicine: contrastive multimodal learning for patient stratification. *Annals of Operations Research*, pages 1–29.
Zhang, A. R., Cai, T. T., and Wu, Y. (2022). Heteroskedastic pca: Algorithm, optimality,
and applications. *The Annals of Statistics*, 50(1):53–80.
Zhang, Z., Liu, J., and Razavian, N. (2020). BERT-XML: Large scale automated ICD coding using BERT pretraining. In Rumshisky, A., Roberts, K., Bethard, S., and Naumann,
T., editors, *Proceedings of the 3rd Clinical Natural Language Processing Workshop*, pages 24–34, Online. Association for Computational Linguistics.

Zhou, D., Cai, T., and Lu, J. (2021). Multi-source learning via completion of block-wise
overlapping noisy matrices. *arXiv preprint arXiv:2105.10360*.
Zhou, D., Gan, Z., Shi, X., Patwari, A., Rush, E., Bonzel, C.-L., Panickan, V. A., Hong,
C., Ho, Y.-L., Cai, T., et al. (2022). Multiview incomplete knowledge graph integration with application to cross-institutional ehr data harmonization. Journal of Biomedical
Informatics, 133:104147.