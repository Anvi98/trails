# Near-Field Channel Estimation In Dual-Band Xl-Mimo With Side Information-Assisted Compressed Sensing

Haochen Wu, Liyang Lu, *Member, IEEE*, and Zhaocheng Wang, Fellow, IEEE

  Abstract— Near-field communication comes to be an indispensable
part of the future sixth generation (6G) communications at the
arrival of the forth-coming deployment of extremely large-scale
multiple-input-multiple-output (XL-MIMO) systems. Due to the
substantial number of antennas, the electromagnetic radiation field
is modeled by the spherical waves instead of the conventional
planar waves, leading to severe weak sparsity to angular-domain
near-field channel. Therefore, the channel estimation reminiscent
of the conventional compression sensing (CS) approaches in the
angular domain, judiciously utilized for low pilot overhead, may
result in unprecedented challenges. To this end, this paper proposes
a brand-new near-field channel estimation scheme by exploiting
the naturally occurring useful side information. Specifically, we
formulate the dual-band near-field communication model based
on the fact that high-frequency systems are likely to be deployed
with lower-frequency systems. Representative side information, i.e.,
the structural characteristic information derived by the sparsity
ambiguity and the out-of-band spatial information stemming from
the lower-frequency channel, is explored and tailored to materialize
exceptional near-field channel estimation. Furthermore, in-depth
theoretical analyses are developed to guarantee the minimum es-
timation error, based on which a suite of algorithms leveraging the
elaborating side information are proposed. Numerical simulations
demonstrate that the designed algorithms provide more assured
results than the off-the-shelf approaches in the context of the dual-
band near-field communications in both on- and off-grid scenarios,
where the angle of departures/arrivals are discretely or continuously
distributed, respectively.

  Index Terms— Block sparsity, channel estimation, compressed
sensing, near-field communications, side information.

I. INTRODUCTION
XTREMELY
large-scale multiple-input-multiple-output
(XL-MIMO)
is expected to fulfill the demands for ubiquitous connecting of the sixth generation (6G) mobile networks [1]. Due to the large spatial multiplexing gain offered by the exploitation of large number of antennas, which is much more than that of massive MIMO in the current fifth-generation (5G)
communications, XL-MIMO
can provide a
10-fold increase in spectral efficiency [2]. Additionally, wideband communications are prospective for more available bandwidth owing to rich spectrum resources at high-frequency bands, e.g., This work is supported in part by National Key R&D Program of China under Grant 2018YFB1801501. (Corresponding author: Zhaocheng Wang and Liyang Lu)
H. Wu and L. Lu are with the Department of Electronic Engineering, Tsinghua University, Beijing
100084, China (e-mail:
wuhc23@mails.tsinghua.edu.cn, luliyang@mail.tsinghua.edu.cn).

Z. Wang is with the Department of Electronic Engineering, Tsinghua University, Beijing 100084, China, and also with the Shenzhen International Graduate School, Tsinghua University, Shenzhen 518055, China (email:zcwang@tsinghua.edu.cn).

H. Wu and L. Lu contributed equally to the project and should be considered co-first authors.

millimeter-wave (mmWave) and terahertz (THz) bands [3]. In conjunction with the flexible deployment of high-frequency antennas, wideband XL-MIMO is capable of providing the aforementioned benefits, which is regarded as an essential component in future 6G mobile networks [4].

Due to the extremely large number of antennas and highfrequency bands, the electromagnetic (EM) characteristics of wideband XL-MIMO undergo a fundamental change [5], where the EM radiation field can be partitioned into the far-field and near-field regions. The boundary between these two regions is approximately determined by the Rayleigh distance which is proportional to the product of the square of array aperture and carrier frequency [4], [5]. Outside the Rayleigh distance is the farfield region, where the EM waves can be modeled by the planar waves, e.g., the wave model used in massive MIMO systems [6]. Within the Rayleigh distance, near-field propagation becomes dominant, hence the EM waves need to be accurately modeled by spherical waves [4].

However, huge numbers of antennas cause substantial pilot overhead in channel estimation. To address this issue, the compressed sensing (CS) technique is capable of providing accurate channel estimation while maintaining low pilot overhead by fully exploiting the sparsity of the channel. In the conventional massive MIMO systems considering planar wave model, the number of significant paths is much smaller than the number of antennas, hence the channel exhibits sparsity in the angular domain [7]. Nevertheless, for the near-field region, spherical waves introduce a distance ingredient, causing severe sparsity ambiguity in angular-domain representation, which indicates that one single near-field path component spreads towards multiple angles [2]. Then, the near-field channel in the angular domain exhibits weak sparsity, i.e., the number of nonzero channel-taps becomes relatively large. It precludes accurate channel estimation in the angular domain through the conventional CS, since the ratio of the nonzero channel-taps in the channel vector is greater than the upper bound of sparsity required for accurate estimation [8].

Many research efforts have been devoted to mitigating the aforementioned weak sparsity of the near-field channel [2], [9]–
[11]. For instance, a polar-domain transformation is proposed in
[2] by sampling the angle uniformly and sampling the distance non-uniformly. The near-field channel is then mapped into the polar domain, involving both angular and distance ingredients, which is sparse enough for accurate estimation by the conventional CS. In [9], the authors propose to decompose the nearfield channel into triple parametric variants firstly, and then use the CS algorithm to estimate the triple parameters of the channel. The works [10] and [11] continue to exploit the polardomain transformation [2] for efficient channel estimation in the non-line-of-sight (NLoS) and the mixed line-of-sight (LoS) and NLoS environments, respectively. Despite of these achievements providing sufficiently sparse signals that can be recovered by CS
algorithms, the bottleneck is that the dimensions of the intrinsic signal processing problems are significantly increased. Quantitatively, when the number of antennas at the base station (BS) is
256, the number of the polar-domain channel-taps is about 2200, which is 4 times more than the number of conventional angulardomain channel-taps based on Discrete Fourier Transformation
(DFT) [2]. The excessively high dimensions of signal processing problems cause unacceptable complexity, which precludes these approaches from alleviating weak sparsity in practice.

Actually, useful information stemming from the signal itself or communication environments, called side information [12], can help mitigate the weak sparsity of angular-domain near-field channels without increasing dimensions in the signal processing problems. The side information can provide the emphatic correlation between the nonzero channel-taps and the pilot training matrix, and also the confirmed potential to filter out noise interference, which significantly improves the sparsity bound required for accurate estimation, leading to more desirable performance compared with the traditional methods without side information.

There are two types of key side information for near-field channel estimation in terms of the channel-tap characteristics and the communication system architecture. On one hand, angulardomain sparsity ambiguity offers continuous nonzero channeltaps, which is considered as the structural characteristic information, i.e., block structure [8]. Meanwhile, for multi-carrier communication systems, the positions of nonzero channel-taps are usually the same [2], which indicates that the near-field channel matrix exhibits block sparsity with same sparse patterns among different subcarriers. Current researches have proved that the exploitation of block structure provides more reliable recovery performance than the conventional non-block approaches, since it improves the upper bound of the sparsity level required for reliable recovery [13]. On the other hand, high-frequency systems are likely to be deployed at the same location as lower-frequency systems, giving rise to out-of-band spatial information [14], [15].

A representative example is that millimeter wave (mmWave) systems are typically deployed together with Sub-6GHz systems for providing wide area control signals and multi-band communications [15]. Then, the out-of-band spatial information in lower-frequency Sub-6GHz systems is useful because the spatial characteristics of Sub-6GHz and mmWave channels are similar
[16]. Specifically, this out-of-band spatial information can be formulated as the weights for index selection of nonzero channeltaps in weighted channel estimation [17].

Nevertheless, the investigation of low-complexity near-field channel estimation assisted by side information is still in its infancy. Firstly, to the best of our knowledge, there is no system modeling of near-field communications adopting out-of-band spatial information. As the near-field region of lower-frequency communication systems is smaller than that of high-frequency systems, the user may stay in either the near-field or far-field region of the lower-frequency system, and always in the near-field region of the high-frequency system. In this dual-band communication system, the out-of-band spatial information may come from either

near-field or far-field channels of the lower-frequency system.
The formulation of this hybrid communication model, and the extraction and exploitation of the out-of-band spatial information
remain to be solved. Secondly, the methodology, which employs both out-of-band spatial and structural characteristic information,
needs to be carefully designed. Current works using the side information for weighted sparse recovery, e.g., [15], [17]–[19], do not consider the complex signals in practical communication
scenarios, wherein [15], [17] do not even take block structure into account. It is evident that these existing studies may not be suitable for the out-of-band spatial information- and block structure-assisted near-field channel estimation.
Against the above backgrounds, this paper proposes the scheme
of side information-assisted dual-band near-field channel estimation in the angular domain. The main contributions are summarized as follows.
1) The model of dual-band near-field communication systems is formulated. Specifically, the scenario where lowerfrequency and high-frequency systems are deployed simultaneously at the same location is highlighted, where the various frequencies result in different near-field regions. Hence, two communication scenarios, i.e., near-field
channel estimation aided by far-field and near-field out-ofband spatial information respectively, are further discussed.
The elaborating dual-band model paves the way for the subsequent analysis and estimation procedures.
2) Theoretical analysis of reliable estimation assisted by side
information is developed. We begin with embedding the dedicated side information and the practical complex channel consideration into the iterative mechanism of the orthogonal matching pursuit (OMP) algorithm, leading to a prior factor for correct index selection of nonzero channeltaps. The analysis of minimizing the estimation error corresponding to the prior factor is derived, which involves
judiciously high-dimensional χ2 approximation for tighter
theoretical guarantees.
3) A brand-new near-field channel estimation scheme is proposed, wherein a series of algorithms derived from the OMP leveraging the naturally occurring side information, are developed. Owing to the exploitation of the prior factor derived, the index selections of nonzero channeltaps of the designed algorithms are more accurate, leading to a higher upper bound of the sparsity level required for reliable recovery. This results in more desirable estimation
performance than the approaches without the assistance of side information in both on- and off-grid scenarios, where the angles of arrivals/departures are discretely or continuously distributed correspondingly.
The rest of the paper is organized as follows. Section II
introduces the system model and problem formulation, followed
by some useful definitions. In Section III, we start with the complex logit-weighted OMP (CLW-OMP) and propose our complex simultaneous logit-weighted block OMP (CSLW-BOMP) algorithm. Moreover, the performance guarantees for these algorithms
are derived. In Section IV, the simulation results are presented
and analyzed, and the conclusions are drawn in Section V.
Notation: We briefly summarize the notations used in this
paper. Boldface lowercase letters, e.g., x, denote vectors, and boldface uppercase letters denote matrices, e.g., X. Calligraphic letters, e.g., S, are used for sets, and non-boldface letters e.g., x and X, represent scalars. Moreover, XS represents the submatrix of X composed of the column vectors whose indices are from S. Superscript H denotes the conjunction transpose, and 0 represents the all zero vector or matrix. CN(a, b) denotes a complex Gaussian distribution with mean a and variance b,
χ2(k) denotes a central χ2 distribution with k degrees of freedom, χ′2(k, λ) denotes the non-central χ2 distribution with its degree of freedom being k and noncentrality parameter being λ, and
[CN(a1, b1), CN(a2, b2), · · · , CN(an, bn)] denotes a vector with length n, where the i-th entry follows CN(ai, bi). We use ∥ · ∥F,
| · |, arg(·) to denote the Frobienus norm, modulus and argument of their objective, respectively. The variables from the Sub-6GHz band are underlined, e.g., X, for clarity.

## Ii. System Model And Mathematical Formulation

In this section, we first provide the dual-band XL-MIMO
system model, and then introduce the corresponding mathematical formulation.

## A. System Model

As depicted in Fig. 1, we formulate the system model of dual-band XL-MIMO, where Sub-6GHz and mmWave bands are exemplified as the different frequency band solutions. The antennas on the Sub-6GHz and mmWave bands are co-located, aligned and have similar apertures [15]. Specifically, the BS
and user equippment (UE) are deployed both on Sub-6GHz and mmWave bands with K subcarriers, whose wavelengths are denoted as λ and λ, respectively. On both bands, the BS is composed of N antennas, while each UE has only one antenna.

The antenna spacing of BS is λ/2 on the Sub-6GHz band and
λ/2 on the mmWave band. As the boundary of the far-field and the near-field regions, i.e., the Rayleigh distance Z =
2D2
λ , is proportional to the carrier frequency and array aperture D [5], the Rayleigh distances of both Sub-6GHz and mmWave systems are

(a) Block sparse near-field channels on
 both Sub-6GHz and mmWave bands
                                           (b) Sparse far-field channel on Sub-6GHz band and
                                           block sparse near-field channel on mmWave band

considerably large, leading to different channel models presented as follows.

In conventional far-field scenarios, the electromagnetic radiaition field is modeled by the planar waves. Assume that there exist L significant paths, the far-field channel hfar ∈ CN×1 can be given by [20], [21]

hfar = N L � l=1 gle−jkmrla(θl). (1) L �
Since the number of antennas is much larger than that of the significant paths, the far-field channel exhibits sparsity in the angular domain, i.e., the number of nonzero channel-taps is much smaller than that of the total channel-taps [22]. Nevertheless, due to the large antenna aperture D and the high-frequency carrier in XL-
MIMO systems, the Rayleigh distance is significantly increased [2]. For example, when the carrier frequency is 100GHz and the antenna aperture is 0.5m, the Rayleigh is about 167m, which can cover a whole cell. Consequently, the UE is more likely to fall within the near-field regions where the spherical wave model should be adopted to accurately represent the electromagnetic propagation characteristics. Hence the near-field channel vector hk ∈ CN×1 can be written as [23]

hk = N L � l=1 gle−jkmrlb(θl, rl). (2) L �
Different from the model in (1), the near-field steering vector b(θl, rl) depends not only on the angle θl but also on the radial distance rl. Under such circumstance, b(θl, rl) exhibits nonlinearity with respect to the antenna index l, and hence should be represented by multiple far-field Fourier vectors instead of a single one. Consequently, the nonzero channel-taps will spread towards multiple angles and exhibits weak sparsity, where the ratio of nonzero channel-taps is relatively large and exceeds the upper bound of the reconstructible sparsity required for reliable recovery of the conventional CS algorithms [2]. Fortunately, this weak sparsity in angular-domain near-field channels can be regarded as the block-sparse structure, which can be leveraged to provide more reliable estimation performance. As illustrated in Figs. 1(a) and 1(b), the nonzero channel-taps of near-field channels naturally occur in blocks, which is formulated as xk in the left-hand side of Fig. 2 [24], [25].

Therefore, the different positions of the UE to the BS induce two distinct cases of the dual-band XL-MIMO system, which are presented as follows.

Case I: The UE is located between the Rayleigh distance of the lower sub-6GHz band and the higher mmWave band. Therefore, we should consider the cooperative channel estimation of a sparse far-field Sub-6GHz channel and a block-sparse nearfield mmWave channel.

Case II: The UE is situated within the Rayleigh distance of both the Sub-6GHz and mmWave bands. Hence, the double nearfield cooperative channel estimation should be considered.

## B. Mathematical Formulation

At the k-th subcarrier and the m-th pilot transmission for one UE, the relationship between the received signal yk,m and the parameters, serving as a penalty to introduce out-of-band spatial information to the conventional OMP algorithm. For the optimal v(pi), we provide the following theorem.

Theorem 1. (CLW-OMP): Among all choices of v(pi), the following expression

$$v(p_{i})=D\ln\Bigl{(}\frac{p_{i}}{1-p_{i}}\Bigr{)},i=1,2,\cdots,N,\tag{10}$$

_is optimal in minimizing the error probability of wrongly choosing a nonzero channel-tap over a zero one in $\mathbf{x}$ in each iteration of CLW-OMP. The coefficient $D$ can be calculated as_

$$\sigma_{1}^{2}=\frac{M}{2}((S-1)g^{2}+\sigma^{2}),$$ $$\sigma_{2}^{2}=\frac{M}{2}(Sg^{2}+\sigma^{2}),$$ $$A=\frac{1}{\sigma_{2}^{2}},\tag{11}$$ $$B=\frac{1}{2}e^{-\frac{M^{2}\sigma^{2}\sigma_{2}^{2}}{2\sigma_{1}^{2}(\sigma_{1}^{2}+\sigma_{2}^{2})}}\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{\sigma_{1}^{2}\sigma_{2}^{2}},$$ $$D=\frac{1}{A-B}.$$
Proof: See Appendix A.

In practical scenarios, $g^{2}$ is usually far less than $M$ and $S$, leading to $\sigma_{1}^{2}\approx\sigma_{2}^{2}$, which is denoted as $\sigma_{0}^{2}$. Therefore, the coefficient $D$ will take a much simpler form when applied in practice.

$$D=\frac{\sigma_{0}^{2}}{1-e^{\frac{M^{2}g^{2}}{4\sigma_{0}^{2}}}}\approx\frac{4\sigma_{0}^{4}}{M^{2}g^{2}}.\tag{12}$$
Remark 1: Compared to [17], the coefficient D in (11) is more generalized, since complex signals in practical communication scenarios are considered. In addition, D derived from Theorem
1 is more accurate than that in [15], where the noise variance
σ2 is taken as the coefficient in the prior factor v(pi) without theoretical analysis in the formula of [15].

## B. Multiple Subcarrier Case

In multiple subcarrier cases where K > 1, the system model now follows the form of (5), and X satisfies the BMMV
feature where d > 1. Correspondingly, the correlation term in Section III-A changes from the modulus |aiy|2 to the Frobienus norm ∥AiY∥2
F .

Under this circumstance, the correlation term, which follows the non-central χ2 distribution, will have a higher degree of freedom, leading to an additional complicated factor in the characteristic function, which can not be solved easily by the method leveraged in Theorem 1. Consequently, the Patnaik's second moment approximation, which is suitable for estimating non-central χ2 distributions with high degrees of freedom, is applied [28], and the optimal analytical expression of the prior factor v(pi) can therefore be acquired, which is presented in the following theorem.

Theorem 2. (CSLW-BOMP): Among all choices of v(pi),

$$v(p_{i})=D\ln\biggl{(}\frac{p_{i}}{1-p_{i}}\biggr{)},i=1,2,\cdots,N,\tag{13}$$
minimizes the error probability of wrongly selecting a nonzero channel-tap over a zero one in x in each iteration of CSLW-
BOMP, where the coefficient D follows

$\sigma_{1}^{2}=M(Sdg^{2}+\sigma^{2})$,

$\sigma_{2}^{2}=M[(Sd-1)g^{2}+\sigma^{2}]$,

$\rho=\frac{2dK+\frac{4dKM^{2}g^{2}}{\sigma_{2}^{2}}}{2dK+\frac{2dKM^{2}g^{2}}{\sigma_{2}^{2}}}$,

$\beta_{1}=\frac{1}{\rho\sigma_{2}^{2}}$,

$\beta_{2}=\frac{1}{\sigma_{1}^{2}}$,

$D=\frac{1}{\beta_{2}-\beta_{1}}$.

Proof: See Appendix B.

Similarly, D can be simplified into

$$D=\frac{\rho}{\rho-1}\sigma_{0}^{2}=\frac{\sigma_{0}^{2}+2M^{2}g^{2}}{M^{2}g^{2}}\sigma_{0}^{2},\tag{15}$$
where σ2
0 = M(Sdg2 + σ2). Moreover, when d > 1, the relative difference between σ2
1 and σ2
2 with respect to their specific value becomes smaller with the increase of d, which results in smaller error in the approximation σ2
2 ≈ σ2
1 = σ2
0 and leads to more accurate estimation in (15). The CSLW-BOMP algorithm is summarized in Algorithm 1.

Furthermore, in (15), the coefficient D is inversely proportional to the signal-to-noise ratio (SNR). To be specific, when the SNR
is low, the coefficient D becomes large accordingly, which leads to a larger proportion of the prior factor v(pi) in the index selection mechanism per iteration. In contrast, when the system SNR is high, D tends to approach a small value and v(pi)
is relatively small compared to the correlation term ∥AiY∥2
F , resulting in the CSLW-BOMP algorithm to converge to the conventional BOMP algorithm.

When d = 1, the CSLW-BOMP algorithm becomes the CSLW-
OMP algorithm, which is presented in the following corollary.

Algorithm 1 CSLW-BOMP Algorithm
Input: Y, A, g, σ2, block length d, out-of-band probability
vector p, convergence limit S
Output: Channel estimation ˆX
1: Initialize: i = 1, R = 0, S = ∅
2: repeat
1−pk to obtain the optimal
3: Calculate D with K in (2) replaced by K − i + 1
4: Solve arg max
k /∈S ∥AH
i Y∥2
F + D ln
pk
block index ki for thr i-th iteration
5: Update the support set S = S �{(ki − 1)d + 1, (ki − 1)d +
2, · · · , kid}
6: Update the channel estimation ˆX = arg min
ˆX
∥Y − AS ˆX∥F
to obtain new ˆX
7: Update the residual matrix R = Y − AS ˆX
8: i = i + 1
9: until |S| = S
The CSLW-OMP algorithm can be applied in off-grid scenarios, where the CSLW-BOMP algorithm has difficulties in handling the off-grid structure.

Corollary 1. (CSLW-OMP): Among all v(pi), the optimal choice minimizing the error probability can be expressed as

$$v(p_{i})=D\ln\biggl{(}\frac{p_{i}}{1-p_{i}}\biggr{)},\quad i=1,2,\cdots,N,\tag{16}$$
where the coefficient D *can be calculated by setting* d = 1 in
(2).

The coefficient D can also be simplified by utilizing the fact that σ2
1 ≈ σ2
2 = σ2
0 in practical scenarios, i.e.,

$$D=\frac{\sigma_{0}^{2}+2M^{2}g^{2}}{M^{2}g^{2}}\sigma_{0}^{2}.\tag{17}$$
It is clear that (17) is a special case for (15) when d = 1, and the algorithm design of CSLW-OMP can be acquired by letting d = 1 in Algorithm 1, which is omitted here.

Remark 2: The CLW-BOMP algorithm can also be analyzed based on Theorem 2 by setting K = 1 instead of d, which is similar to the CSLW-OMP algorithm. Since the block structure in the single subcarrier case also involves non-central χ2 distributions with high degrees of freedom, the Patnaik's second moment approximation can be utilized to obtain the optimal v(pi) in the CLW-BOMP algorithm similar to the proof of Theorem 2.

## Iv. Simulation Results

In our simulation, the dual-band XL-MIMO communication system with K = 32 subcarriers is considered, while the number of antennas at the BS side is set to N = 400 in order to meet the near-field requirements in the XL-MIMO systems. For the generation of the out-of-band channel matrix H, each entry in H can be obtained by multiplying the corresponding entry in H
by a specific coefficient Q, whose amplitude and phase depend on the relationship of the central frequencies between the Sub-
6GHz band and the mmWave band, which is denoted as fm and fs, respectively [15].

Specifically, with the assumption that the support set S is the same for X and X, the coefficient Q for nonzero blocks in X
can be calculated as

$$\gamma=\frac{|f_{m}-f_{s}|}{\max(f_{m},f_{s})},$$ $$|Q|=\gamma R_{1}\delta,\tag{18}$$ $$\arg(Q)=2\pi\gamma R_{2}\delta,$$
where R1 and R2 are two independent variables, whose values are ±1 with equal probability, and δ is uniformly distributed between 0 and 1. Moreover, the channel-taps in X in zero rowblock submatrices are set to follow the distribution of CN(0, σ2
n)
to simulate the perturbations on the zero channel-taps in X due to the difference in frequencies between fs and fm, and σ2
n = γ2
C
[15]. C is the variance amplitude ratio for nonzero channel-taps and zero channel-taps in X.

| Parameters             |
|------------------------|
| Support band frequency |
| f                      |
| s                      |
| 3.5GHz                 |
| Support bandwidth      |
| BW                     |
| s                      |
| 150MHz                 |
| Object band frequency  |
| f                      |
| m                      |
| 28GHz                  |
| Object bandwidth       |
| BW                     |
| o                      |
| 850MHz                 |
| Block length           |
| d                      |
| 4                      |
| Amplitude ratio        |
| C                      |
| 3                      |
| Number of iteration    |
| N                      |
| iter                   |
| 1000                   |

Once the Sub-6GHz support channel X is generated, the outof-band probability vector p can then be acquired based on (6).

The function f is selected as

$$p_{i}=f(\underline{x}_{i})=\frac{\underline{x}_{i}-\underline{x}_{min}}{\underline{x}_{max}-\underline{x}_{min}}\,,\tag{19}$$
where xmax and xmin represent the maximum and minimum in {x1, x2, · · · , xN/d}, respectively, and (19) can be leveraged to generate p in both Case I and Case II as illustrated in Section II-A. Meanwhile, we consider the more general Case II scenario, where both Sub-6GHz and mmWave bands are within the near-field region, leading to stronger block structure for both channels. The far-field channel, i.e., the Sub-6GHz system in Case I, is regarded as a special case by setting the block length as 1 or a smaller value compared with the near-field scenario. According to (19), pi of the row-block submatrix with the maximum Frobienus norm in X is normalized to 1 in p, and therefore has the value of infinity under the influence of the prior factor v(pi) = D log(
pi
1−pi ). As a result, the CSLW-BOMP algorithm always chooses the row-block submatrix in X of the mmWave band which corresponds to the strongest row-block submatrix in the support channel X of the Sub-6GHz system, as the starting support information in the first iteration for recovering X, leading to potential performance enhancement of the algorithm. Similarly, the row-block submatrix with the minimum Frobienus norm in X becomes negative infinity due to the existence of v(pi), which improves the overall performance of our proposed algorithm by consistently ignoring this worst-performing submatrix. The detailed simulation parameters are listed in Table I, and the conventional OMP and BOMP algorithms [24] are adopted for comparison.

In Fig. 3, the channel estimation performance in on-grid scenarios is compared, with the number of row-block matrices S
d , number of pilot transmission M fixed to 10 and 50 respectively.

The normalized mean-square error (NMSE) is leveraged as the criterion, which can be expressed as

$$\text{NMSE}=\frac{\|\hat{\mathbf{X}}-\mathbf{X}\|_{F}^{2}}{NK},\tag{20}$$
where X and ˆX represent the angular-domain channel matrix and the estimated angular channel, respectively. Moreover, the optimal bound where the channel-tap selections are set to be correct in each iteration is adopted as the upper bound in on-grid scenarios.

It can be observed that our proposed CSLW-OMP and CSLW-
BOMP algorithms outperform the traditional OMP and BOMP algorithms, while the performance of CSLW-BOMP algorithm is close to that of the optimal bound benchmark, indicating the effectiveness of the application of out-of-band spatial information.

Moreover, the NMSE performance of BOMP and CSLW-BOMP is also superior to that of the OMP and CSLW-OMP algorithms, since the BOMP and the CSLW-BOMP algorithms take the structural characteristic information into consideration and fully utilizes the block structure, which efficiently enhances the robustness of the algorithm, preventing severe nonzero channel-tap selection errors for assured estimation performance. In addition, the exploitation of side information leads to the continuous decrease of the NMSE of the CSLW-BOMP algorithm as the SNR increases, while other algorithms compared tend to reach a plateau at high SNR scenarios.

As illustrated in Fig. 4, when the channel matrix H changes from on-grid to off-grid, the NMSE performance varies drastically. Although the channel grid cannot align with the block structure in off-grid scenarios, leading to inherent defect in handling off-grid block structure, the CSLW-BOMP still performs the best between the two block structure-based algorithms due to the assistance of out-of-band spatial information. Meanwhile, the CSLW-OMP algorithm enjoys more desirable performance than other algorithms, since the OMP algorithms can effectively adapt to the off-grid channel features by taking the off-grid structure where d > 1 as on-grid features where d = 1, and the CSLW-
OMP algorithm can exploit the sophisticated out-of-band spatial information from the Sub-6GHz band to support the mmWave channel estimation.

In Fig. 5, the on-grid recovery performance of all the algorithms is presented as the number of nonzero blocks S
d increases, which is in proportion to the sparsity S
N . We set M = 50 and SNR = 10dB. The probability of accurate estimation, which is defined as the frequencies of the NMSE to be less than a threshold
θ, is utilized to provide their performance, and θ = 10−2.

It can be concluded that all the algorithms achieve accurate channel estimation with probability of accurate estimation as
100% when the sparsity is low. When the sparsity approaches
0.13, the probability of accurate estimation decreases, but the CSLW-BOMP and CSLW-OMP algorithms still outperform other algorithms without out-of-band spatial information. Furthermore, as the sparsity gradually increases, CSLW-BOMP leveraging both types of side information, i.e., structural characteristic information and out-of-band spatial information, enjoys the best recovery performance, being able to accurately recover the channel matrix even if the sparsity is larger than 0.1. Hence, our proposed CSLW-BOMP algorithm can effectively improve the upper bound of the reconstructible sparsity, and therefore acts as a stunning solution to the weak sparsity problem in near-field XL-MIMO systems. Moreover, the proposed CSLW-OMP provides more assured results than those of the OMP algorithm, which even approaches or exceeds the estimation performance of the BOMP assisted by the block structure, and the OMP has the worst estimation performance because of the most restricted upper bound of reconstructible sparsity.

In Fig. 6, the probability of accurate estimation is simulated as a function of the compression rate M
N , which is proportional to the number of required pilot transmissions M. It unveils that the probability of accurate estimation increases with the increase of compression rate, and the CSLW-BOMP still enjoys the highest probability of accurate estimation under the same compression rate among all compared algorithms, which is similar to the conclusions in Fig. 5. Meanwhile, when the probability of accurate estimation is fixed, CSLW-BOMP requires the least pilot transmissions, followed by BOMP, CSLW-OMP and OMP.

For 100% probability of accurate estimation, CSLW-BOMP can reduce the pilot overhead by 25% when compared to the BOMP algorithm, and 30.1% when compared to the OMP algorithm, substantiating the feasibility of the proposed CSLW-BOMP in low-overhead XL-MIMO communications.

## V. Conclusion

In this paper, we concentrate on addressing the weak sparsity challenge of near-field channel estimation resorting to the side information extracted from the spherical wave model and the dualband communication architecture. Specifically, the dual-band near-field communication model is elaborated, where mmWave and Sub-6GHz systems act as co-deployed communication solutions. The structural characteristic information, in conjunction with the out-of-band spatial information stemming from the Sub- 6GHz band, is harnessed for enhancing the channel estimation accuracy, as well as the upper bound of reconstructible sparsity.

A series of variants of the OMP employing side information are proposed, supported by profound analysis revealing the minimum estimation error. Numerical simulations are conducted to substantiate the feasibility of the proposed approaches, indicating fertile advantages in terms of both on- and off-grid estimation accuracy.

Proof: First, we focus on deriving the probability distribution of |aH
i y|2.

Without loss of generality, assume that the first S channel-taps of x are nonzero, i.e., the support set S = {1, 2, · · · , S}. As a result, y can be expressed as

$\mathbf{y}=\sum_{j=1}^{S}\mathbf{a}_{j}x_{j}+\mathbf{n}$, (21)
where ai is the i-th column of A. The correlation term aH
i y can thus be

$$\mathbf{a}_{i}^{\rm H}\mathbf{y}=\mathbf{a}_{i}^{\rm H}\Big{(}\sum_{j=1}^{S}\mathbf{a}_{j}x_{j}+\mathbf{n}\Big{)}=\sum_{i=1}^{S}(\mathbf{a}_{i}^{\rm H}\mathbf{a}_{j})x_{j}+\mathbf{a}_{i}^{\rm H}\mathbf{n}.\tag{22}$$
Suppose that M is sufficiently large, aH
i aj can be approximated to M when i = j according to the law of large numbers, while aH
i aj
∼ CN(0, M) holds for i ̸= j by the central limit theorem. Similarly, we have aH
i n ∼ CN(0, Mσ2) [17].

Consequently, the probability distribution aH
i y can be calculated separately for i ≤ S and i > S.

For i ≤ S, there exists j ∈ {1, 2, · · · , S} such that j = i, and aH
i y can be simplified into

$$\mathbf{a}_{i}^{\rm H}\mathbf{y}=\mathbf{a}_{i}^{\rm H}\mathbf{a}_{i}x_{i}+\sum_{j=1,j\neq i}^{S}(\mathbf{a}_{i}^{\rm H}\mathbf{a}_{j})x_{j}+\mathbf{a}_{i}^{\rm H}\mathbf{n}\tag{23}$$ $$\approx Mx_{i}+\sum_{j=1,j\neq i}^{S}\mathcal{CN}(0,M)x_{j}+\mathcal{CN}(0,M\sigma^{2}).$$
Assume that all nonzero channel-taps xi have the same modulus g [17], the probability distribution of aH
i y satisfies that

$$\mathbf{a}_{i}^{\mathrm{H}}\mathbf{y}\sim\mathcal{CN}(Mx_{i},M\big{(}(S-1)g^{2}+\sigma^{2}\big{)}),\tag{24}$$

dates that the correlation term $\mathbf{a}_{i}^{\mathrm{H}}\mathbf{y}$ follows complex 
can be expressed as

which indicates that the correlation term aH
                                           i y follows complex
Gaussian distribution with mean Mxi and variance M
                                                         �
                                                          (S −
1)g2 + σ2�
           . Denote
                     M
                      2
                        �
                         (S − 1)g2 + σ2�
                                            as σ2
                                                1, then |aH
                                                           i y|2

|aH i y|2 = N(Mℜ(xi), σ2 1)2 + N(Mℑ(xi), σ2 1)2, (25)
which follows the non-central χ2 distribution with degree of freedom k = 2, noncentrality parameter a =
�

                                                                         |aH
                                                                            i y|2 = Mg
and variance σ2
                     1.
   If i > S, for any j ∈ {1, 2, · · · , S}, we have i ̸= j. Therefore,
aH
  i y satisfies that

$$\begin{split}\mathbf{a}_{i}^{\text{H}}\mathbf{y}&=\sum_{i=1}^{S}\mathcal{CN}(0,M)x_{j}+\mathcal{CN}(0,M\sigma^{2})\\ &\sim\mathcal{CN}(0,M(Sg^{2}+\sigma^{2})).\end{split}\tag{26}$$
By letting σ2
2 = M
2 (Kg2 + σ2), the probability distribution of
|aH
i y|2 for i = 1, 2 · · ·N is given by

$$\mathbf{a}_{i}^{\mathrm{H}}\mathbf{y}|^{2}\sim\begin{cases}\sigma_{1}^{2}\chi^{\prime2}(2,Mg)&i\leq S,\\ \sigma_{2}^{2}\chi^{2}(2)&i>S,\end{cases}\tag{27}$$
where χ2 and χ′2 represents the central and non-central distribution respectively.

After that, we move on to solving the optimal v(pi), which is achieved through minimizing the probability of incorrect choices in each iteration of the CLW-OMP algorithm.

Consider that i1 ≤ S and i2 > S, and let v1 = v(pi1), v2 =
v(pi2), T1 = |ai1y|2 and T2 = |ai2y|2. Then the incorrect index i2 is wrongly chosen instead of correct i1 if and only if T1+v1 <
T2 +v2, which is equivalent to T1 −T2 < v2 −v1. We denote the probability of this event as pe(i1, i2), and denote ∆v = v2 − v1
and T = T1 − T2. In order to obtain the analytical expression of v(pi), the following develops the probability distribution function
(PDF) of T as a theoretical foundation.

According to (27), T is the difference between a non-central
χ2 distribution and a central χ2 distribution, and the characteristic function method can be applied to derive the PDF of T . For T1
Combining (35) and (36) yields and T2, their characteristic function φ(ω) = E(ejωT ) are given as follows

jωM2g2 2(σ2 1 +σ2 2) ∆v 2σ2 2 e − M2g2 1−2jωσ2 2 , φ1(ω) = 1 ∂Pe ∂v =pi1(1 − pi2) 1 2(σ2 1 + σ2 2)e 1 − 2jωσ2 1 e σ2 2 ∆v(σ2 1 + σ2 2) φ2(ω) = 1 (37) × Q1 1 − 2jωσ2 2 . (28) σ2 1σ2 2 � � σ2 1 + σ2 2 , � � Mg σ1 2(σ2 1+σ2 2) . −∆v 2σ2 2 e − M2g2 − pi2(1 − pi1) 1
In addition, since T1 and T2 are independent, the characteristic function of T can be expressed as

$\phi(\omega)=\mathbb{E}(e^{j\omega T})=\mathbb{E}(e^{j\omega T_{1}})\mathbb{E}(e^{-j\omega T_{2}})$
Letting ∂Pe
∂v = 0, we have

$$=\frac{1}{(1-2j\omega\sigma_{1}^{2})(1+2j\omega\sigma_{2}^{2})}e^{\frac{j\omega\sigma_{1}^{2}\sigma_{2}^{2}}{(1-2j\omega\sigma_{2}^{2})}}.\tag{29}$$

$$e^{\frac{j\omega}{2j}}Q_{1}\bigg{(}\frac{Mg}{\sigma_{1}}\sqrt{\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}},\sqrt{\frac{\Delta v(\sigma_{1}^{2}+\sigma_{2}^{2})}{\sigma_{1}^{2}\sigma_{2}^{2}}}\bigg{)}=\frac{p_{\rm s_{1}}(1-p_{\rm s_{1}})}{p_{\rm s_{1}}(1-p_{\rm s_{2}})}.$$
After inverse Fourier transformation, the PDF of T can be obtained based on (29) [29], i.e.,
(38)
Since ∆v → 0, we obtain that

t 1 2σ2 2 e − M2g2 2(σ2 1 +σ2 2) t ≥ 0, 2(σ2 1+σ2 2)e 2 − e− a2+b2 2 ), (39) Q1(a, b) ≈ ˜Q1(a, b) = 1 − 1 t 2(e− a2−b2 1 (30) pT (t) = 2σ2 2 e − M2g2 2(σ2 1 +σ2 2) × 2(σ2 1+σ2 2)e       σ2 2 t(σ2 1+σ2 2) σ2 1σ2 2 for lim b→0(Q1(a, b) − ˜Q1(a, b)) = 0. (40) σ2 1+σ2 2 , � � Q1 � Mg σ1 � t < 0,
where Q1 is the first-order Marcum Q-function and given by

    
By substituting (39) into (38), the left-hand side of (38) can be transformed into

$$Q_{1}(a,b)=\int_{b}^{\infty}xe^{-\frac{x^{2}+a^{2}}{2}}I_{0}(ax)dx,\tag{31}$$ $$e^{\frac{\Delta\varphi}{\tau_{1}^{2}}}Q_{1}\Bigg{(}\frac{Mg}{\sigma_{1}}\sqrt{\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}},\sqrt{\frac{\Delta v(\sigma_{1}^{2}+\sigma_{2}^{2})}{\sigma_{1}^{2}\sigma_{2}^{2}}}\Bigg{)}$$
and I0(x) denotes the modified Bessel function of the first kind with zero order. Based on (30), we have

$$p_{e}(i_{1},i_{2})=P(T<\Delta v).\tag{32}$$ $$=e^{\frac{\Delta v}{2}}\Big{(}1-\frac{1}{2}e^{-\frac{\Delta v^{2}\,\tau^{2}\,\tau^{2}}{2\,\tau^{2}\,(1+\tau^{2})}}\Big{(}e^{\frac{\Delta v-\tau^{2}\,\tau^{2}-\tau_{1}^{2}}{2\,\tau^{2}\,\tau^{2}}}-e^{-\frac{\Delta v\,\tau^{2}\,\tau^{2}-\tau_{2}^{2}}{2\,\tau^{2}\,\tau^{2}}}\Big{)}).$$

Due to Taylor expansion and the fact that $\Delta v\to0$, we can 
∆v(σ2
1+σ2
2)
obtain e
∆v
σ2
2 ≈ 1+ ∆v

σ2
 1σ2
   2
      −e
          −
           ∆v(σ2
               1+σ2
                   2)

σ2
 1σ2
   2
       ≈ ∆v(σ2
              1+σ2
                  2)

σ2
2 and e

                                                 σ2
                                                  1σ2
                                                    2
                                                        .
Then,

  The expression of pe(i2, i1), which represents the probability
of i1 being incorrectly chosen over i2, can be similarly calculated
as
                 pe(i2, i1) = P(T < −∆v).
                                                        (33)

∆v(σ2 1+σ2 2) e 2σ2 1σ2 2 − e − ∆v(σ2 1 +σ2 2) 2e − M2g2σ2 2 ∆v σ2 2 � 1 − 1 2σ2 1σ2 2 �� 2σ2 1(σ2 1+σ2 2) � e 2σ2 1(σ2 1+σ2 2) × σ2 1 + σ2 2
The total error probability Pe in one iteration of CLW-OMP
algorithm can be acquired by taking the out-of-band probability pi1 and pi2 into consideration, i.e.,

$$P_{\rm e}=p_{\rm e_{1}}(1-p_{\rm e_{1}})p_{\rm e_{2}}(i_{1},i_{2})+p_{\rm e_{1}}(1-p_{\rm e_{1}})p_{\rm e_{2}}(i_{2},i_{1}).\tag{34}$$ $$=\left(1+\frac{\Delta v}{\sigma_{2}^{2}}\right)\left(1-\frac{1}{2}e^{-\frac{\mu^{2}+\mu^{2}\Delta v^{2}}{2\left[1+\left(1-\frac{\mu^{2}}{\sigma_{1}^{2}}\right)^{2}\right]}}\quad\frac{\frac{2}{3}+\sigma_{1}^{2}}{\sigma_{1}^{2}\sigma_{2}^{2}}\Delta v\right).$$

2e

Then, ∂Pe

Denoting A =
              1
              σ2
              2 and B = 1

                                           σ2
                                            1σ2
                                              2 , we have
A > B. Therefore, the Marcum Q function term in (38) can be
simplified into

∂v = 0 yields the optimal v(pi). However, since pT (t)
is a piecewise function, we need to discuss in cases to further calculate ∂Pe
∂v .

Consider the situation where ∆v > 0. In this case,

$$e^{\frac{M}{\sigma_{1}^{2}}}Q_{1}\left(\frac{Mg}{\sigma_{1}}\sqrt{\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}},\sqrt{\frac{\Delta v(\sigma_{1}^{2}+\sigma_{2}^{2})}{\sigma_{1}^{2}\sigma_{2}^{2}}}\right)\tag{43}$$
= (1 + A∆v)(1 − B∆v) ≈ 1 + (A − B)∆v.

$$C=\int_{-\pi}^{0}$$
is a scalar, and Pe can be written as

$\frac{t}{t}$. 
On the other hand, letting ∆p = pi2 − pi1 → 0 and pi1 = pi, the right-hand side of (38) can be therefore simplified into

$$P_{n}=p_{n_{1}}(1-p_{n_{1}})\Bigg{(}C+\int_{0}^{\Delta_{p}}\frac{1}{2(\sigma_{1}^{2}+\sigma_{2}^{2})}e^{\frac{-\mu^{2}\Delta_{p}}{2(1+\sigma_{2}^{2})}}$$ $$\times Q_{1}\frac{\sigma_{2}^{2}}{\sigma_{1}}\frac{t(\sigma_{1}^{2}+\sigma_{2}^{2})}{\sigma_{1}}\quad dt\tag{36}$$ $$\frac{p_{n_{2}}(1-p_{n_{1}})}{p_{n_{1}}(1-p_{n_{1}})}=1+\frac{\Delta p}{p_{n}(1-p_{n})}.\tag{44}$$
Combining (43) and (44) yields

$$\left(\frac{Mg}{\sigma_{1}}\sqrt{\frac{\gamma}{\sigma_{1}^{2}+\sigma_{2}^{2}}}\sqrt{\frac{\sigma_{1}^{2}\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}}\right)\tag{45}$$ $$+p_{\rm i_{1}}(1-p_{\rm i_{1}})\int_{-\infty}^{-\Delta v}\frac{1}{2(\sigma_{1}^{2}+\sigma_{2}^{2})^{\frac{1}{2}}}e^{-\frac{1}{2\sigma_{1}^{2}(1-p^{2})}}dt.$$ $$\frac{\Delta v}{\Delta p}=\frac{1}{A-B}\frac{1}{p_{\rm i}(1-p_{\rm i})},$$ which is the derivative of $v(p_{i})$ with respect to $p_{i}$. Based on (45), we obtain the optimal expression of the prior factor $v(p_{i})$ as follows

$$v(p_{i})=D\ln\Bigl{(}\frac{p_{i}}{1-p_{i}}\Bigr{)},\tag{46}$$

where the coefficient $D$ is given in (11).

When $\Delta v<0$, the result in (46) can be obtained through a similar derivation, which completes the proof.

## Appendix B Proof Of Theorem 2

Proof: Based on the proof in Appendix A, AH
i Y can be expressed as

$$\mathbf{A}_{i}^{\mathrm{H}}\mathbf{Y}=\sum_{t=1}^{N}\mathbf{A}_{i}^{\mathrm{H}}\mathbf{A}_{t}\mathbf{X}_{t}+\mathbf{A}_{i}^{\mathrm{H}}\mathbf{N}.\tag{47}$$

Using the assumption that $M$ is sufficiently large, we obtain

$$\mathbf{A}_{i}^{\mathrm{H}}\mathbf{A}_{t}\sim\begin{cases}\mathcal{CN}(0,M)_{d\times d},&i\neq t,\\ \mathcal{M}(M,\mathcal{CN}(0,M))_{d\times d},&i=t.\end{cases}\tag{48}$$
CN(0, M)d×d denotes a d × d matrix with all its entries i.i.d.

as CN(0, M), and M(M, CN(0, M))d×d is defined as

M(M, CN(0, M))d×d   = . (49) M CN(0, M) · · · CN(0, M) CN(0, M) M · · · CN(0, M) ... ... ... ... CN(0, M) CN(0, M) · · · M d×d  
Note that the entries in M(M, CN(0, M))d×d are also independent. Since AH
i N = CN(0, Mσ2)d×K, AH
i Y can be calculated for the cases where Xi ̸= 0 and Xi = 0 seperately.

For Xi ̸= 0, there are S nonzero terms in the correlation term in (47), and only one of them satisfies that i = t. With the assumption that all entries in Xi have the same modulus g, AH
i Y
can be calculated as

AH i Y =M(M, CN(0, M))d×dXi + (50) t=1,t̸=i CN(0, M)d×dXt + CN(0, Mσ2)d×K n � =M(M, CN(0, M))d×dXi + CN(0, M(S − 1)dg2 + σ2)d×K.

  Since M(M, CN(0, M))d×dXi
                                  =
                                      MXi + CN(0, (d −
1)Mg2)d×K, the expression of AH
                               i Y can be simplified into

AH
i Y = MXi + CN(0, M
            �
             (Sd − 1)g2 + σ2�
                     )d×K.
                          (51)

Denoting M
           �
            (Sd − 1)g2 + σ2�
                              as σ2
                                  1, ∥AH
                                       i Y∥2
                                            F follows the
non-central χ2 distribution with 2dK degrees of freedom, and its
noncentrality parameter λ can be calculated as 2dKM2g2

σ2
1
, which is similar to the proof in Appendix A. Compared to the previous proof in Appendix A, the difficulty of this theorem lies in the higher degree of freedom of the non-central χ2 distributions.

Actually, when the degree of freedom in non-central χ2 distributions is larger than 2, an additional complicated coefficient will appear in its characteristic function, which can not be solved by the characteristic function method as the proof given in (29)
[29]. As a result, we need to approximate the non-central χ2
distributed ∥AiY∥2
F when Xi ̸= 0 into a more generalized form.

According to [28], the non-central χ2 distribution can be approximated to a central χ2 distribution through Patnaik's second moment approximation, i.e.,

$$\chi^{\prime2}(n,\lambda)\approx\rho\chi(\tau),\tag{52}$$

where

$$\rho=\frac{n+2\lambda}{n+\lambda}=\frac{2dK+\frac{4dKM^{2}g^{2}}{\sigma_{1}^{2}}}{2dK+\frac{2dKM^{2}g^{2}}{\sigma_{1}^{2}}},\tag{53}$$

$$\tau=\frac{(n+\lambda)^{2}}{n+2\lambda}=\frac{\left(\frac{2dK+\frac{2dKM^{2}g^{2}}{\sigma_{1}^{2}}}{2dK+\frac{4dKM^{2}g^{2}}{\sigma_{1}^{2}}}\right)^{2}}{2dK+\frac{4dKM^{2}g^{2}}{\sigma_{1}^{2}}}.$$
Recall that central χ2 distribution is a special case of Gamma distribution, we obtain that

$$\|\mathbf{A}_{i}^{\mathrm{H}}\mathbf{Y}\|_{F}^{2}=\frac{1}{2}\sigma_{1}^{2}\chi^{\prime2}(2dK,\lambda)\tag{54}$$ $$\approx\frac{1}{2}\sigma_{1}^{2}\rho\chi^{2}(\tau)$$ $$=\Gamma\Big{(}\frac{\tau}{2},\frac{1}{\rho\sigma_{1}^{2}}\Big{)}.$$

When $\mathbf{X}_{i}=\mathbf{0}$, we can similarly obtain the distribution of $\mathbf{A}_{i}\mathbf{Y}$ as follows.

$$\mathbf{A}_{i}^{\mathrm{H}}\mathbf{Y}=\sum_{i=1}^{n}\mathcal{CN}(0,M)_{d\times d}\mathbf{X}_{t}+\mathcal{CN}(0,M\sigma^{2})_{d\times K}\tag{55}$$ $$=\sum_{i=1}^{n}\mathcal{CN}(0,dMg^{2})_{d\times K}+\mathcal{CN}(0,M\sigma^{2})_{d\times K}$$ $$=\mathcal{CN}(0,M(Sdg^{2}+\sigma^{2}))_{d\times K}.$$

  Let σ2
       2 = M(Sdg2 + σ2). As a result, the distribution of
∥AH
   i Y∥2
       F can be expressed as a Gamma distribution in the shape-
rate form, i.e.,

$$\|{\bf A}_{i}^{\rm H}{\bf Y}\|_{F}^{2}=\frac{1}{2}\sigma_{2}^{2}\chi^{2}(2dK)=\Gamma\Big{(}dK,\frac{1}{\sigma_{2}^{2}}\Big{)}.\tag{56}$$
After obtaining the probability distribution of ∥AH
i Y∥2
F in different cases, the optimal prior factor v(pi), which minimizes the error probability, is solved similar to that in Appendix A.

Let α1 = τ
2, β1 =
1
ρσ2
1 and α2 = dK, β2 =
1
σ2
2 , then ∥AH
i Y∥2
F
follows the distribution of Γ(α1, β1) and Γ(α2, β2) when Xi = 0
and Xi ̸= 0, respectively. Define v1, v2, T1, T2, ∆v, ∆p, pi as the same in Theorem 1. The PDF of T = T1 − T2 still needs to be derived.

According to [30], the PDF of T , which is the difference between two Gamma distributions, can be written as

$$p_{T}(t)=\begin{cases}\frac{\tilde{c}}{\Gamma(\alpha_{1})}t^{\frac{\alpha_{1}+\alpha_{2}}{2}-1}e^{\frac{\beta_{2}-\beta_{1}}{2}t}\\ \frac{W_{\frac{\alpha_{1}-\alpha_{2}}{2}},1-\alpha_{1}-\alpha_{2}}{\tilde{c}}\left((\beta_{1}+\beta_{2})t\right)\qquad t\geq0,\\ \frac{\tilde{c}}{\Gamma(\alpha_{2})}(-t)^{\frac{\alpha_{1}+\alpha_{2}}{2}-1}e^{\frac{\beta_{2}-\beta_{1}}{2}t}\\ W_{\frac{\alpha_{2}-\alpha_{1}}{2},\frac{1-\alpha_{1}-\alpha_{2}}{2}}\left(-(\beta_{1}+\beta_{2})t\right)\quad t<0,\end{cases}\tag{57}$$

where ˜c =
               βα1
                1
                  βα2
                  2

(β1+β2)(α1+α2)/2 is a scalar, Γ(x) represents the Gamma function, and Wκ,µ(z) is the Whittaker function [31], which is the solution for the following differential equation

$$\frac{d^{2}w}{dz^{2}}+\Big{(}-\frac{1}{4}+\frac{\kappa}{z}+\frac{\frac{1}{4}-\mu^{2}}{z^{2}}\Big{)}w=0.\tag{58}$$

Based on Theorem 1, the derivative of error probability $\frac{\partial P_{\alpha}}{\partial v}$
∂v when ∆v > 0 is given by

β2−β1 α1+α2 2 −1e 2 ∆v× ∂Pe ∂v =pi1(1 − pi2) ˜c Γ(α1)(∆v) W α1−α2 2 , α1+α2−1 (59) α1+α2 2 � (β1 + β2)∆v � 2 −1e− β2−β1 2 ∆v× − pi2(1 − pi1) ˜c Γ(α2)(∆v) W α2−α1 2 , α1+α2−1 2 � (β1 + β2)∆v � .
In (59), we use the property of Wκ,−µ(z) = Wκ,µ(z) for Whittaker functions [31]. From [31], the Whittaker function has a concise estimation, i.e.,

Wκ,µ(z) = Γ(2µ) Γ( 1 2 + µ − κ)z 1 2 −µ, (60)
when ℜ(µ) = α1+α2−1
2
> 1
2 and z = (β1 + β2)∆v → 0, which is naturally satisfied in (59) since α1, α2 > 1 and ∆v → 0. By leveraging (60) and letting ∂Pe

leveraging (60) and letting $\frac{\partial P_{x}}{\partial v}=0$, (59) can be finally expressed by

$$e^{(\beta_{2}-\beta_{1})\Delta v}=\frac{p_{i_{2}}(1-p_{i_{1}})}{p_{i_{1}}(1-p_{i_{2}})},\tag{61}$$
where pi2 (1−pi1 )
pi1 (1−pi2 ) = 1 +
∆p pi(1−pi) since ∆p → 0, which has been demonstrated in Appendix A.

Therefore, since ∆p → 0, ∆v can be expressed as

$$\begin{split}\Lambda v&=\frac{1}{\beta_{2}-\beta_{1}}\ln(1+\frac{\Delta p}{p_{i}(1-p_{i})})\\ &\approx\frac{1}{\beta_{2}-\beta_{1}}\frac{\Delta p}{p_{i}(1-p_{i})}.\end{split}\tag{62}$$
Based on (62), the derivative of v(pi) can be obtained, which finally gives the expression of v(pi), i.e.,

$$v(p_{i})=\frac{1}{\beta_{2}-\beta_{1}}\ln\biggl{(}\frac{p_{i}}{1-p_{i}}\biggr{)}.\tag{63}$$
By denoting
1

By denoting $\frac{1}{\beta_{2}-\beta_{1}}$ as coefficient $D$, the optimal form of $v(p_{i})$ in (2) is therefore acquired.

For the case where $\Delta v<0$, (63) can be obtained by similar deductions. This completes the whole proof.

## References

[1] Z. Wang et al., "A tutorial on extremely large-scale MIMO for 6G:
Fundamentals, signal processing, and applications," IEEE Commun. Surveys Tuts., to appear, 2024.
[2] M. Cui and L. Dai, "Channel estimation for extremely large-scale MIMO:
Far-field or near-field?," *IEEE Trans. Commun.*, vol. 70, no. 4, pp. 2663–
2677, Apr. 2022.
[3] Z. Sha and Z. Wang, "Channel estimation and equalization for terahertz
receiver with RF impairments," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 6,
pp. 1621–1635, Jun. 2021.
[4] M. Cui, Z. Wu, Y. Lu, X. Wei and L. Dai, "Near-field MIMO communications for 6G: Fundamentals, challenges, potentials, and future directions,"
IEEE Commun. Mag., vol. 61, no. 1, pp. 40–46, Jan. 2023.
[5] K. T. Selvan and R. Janaswamy, "Fraunhofer and Fresnel distances: Unified
derivation for aperture antennas," *IEEE Antennas Propag. Mag.*, vol. 59,
no. 4, pp. 12–15, Aug. 2017.
[6] S. Wang et al., "A joint hybrid precoding/combining scheme based on equivalent channel for massive MIMO systems," *IEEE J. Sel. Areas Commun.*,
vol. 40, no. 10, pp. 2882–2893, Oct. 2022.
[7] Z. Wang, P. Zhao, C. Qian and S. Chen, "Location-aware channel estimation
enhanced TDD based massive MIMO," *IEEE Access*, vol. 4, pp. 7828–7840,
Nov. 2016.
[8] L. Lu, W. Xu, Y. Wang, and Z. Tian, "Recovery conditions of sparse
signals using orthogonal least squares-type algorithms," IEEE Trans. Signal
Process., vol. 70, pp. 4727–4741, Oct. 2022.
[9] X. Guo, Y. Chen and Y. Wang, "Compressed channel estimation for nearfield XL-MIMO using triple parametric decomposition," IEEE Trans. Veh. Technol., vol. 72, no. 11, pp. 15040–15045, Nov. 2023.
[10] Y. Lu and L. Dai, "Near-field channel etimation in mixed LoS/NLoS environments for extremely large-scale MIMO systems," *IEEE Trans. Commun.*,
vol. 71, no. 6, pp. 3694–3707, Jun. 2023.
[11] X. Wei and L. Dai, "Channel estimation for extremely large-scale massive
MIMO: Far-field, near-field, or hybrid-field?," *IEEE Commun. Lett.*, vol. 26,
no. 1, pp. 177–181, Jan. 2022.
[12] A. Wyner and J. Ziv, "The rate-distortion function for source coding with
side information at the decoder," *IEEE Trans. Inf. Theory*, vol. 22, no. 1,
pp. 1–10, Jan. 1976.
[13] L. Lu, Z. Wang and S. Chen, "Joint block-sparse recovery using simultaneous BOMP/BOLS," *arXiv:2304.03600*, Apr. 2023.
[14] N. Gonzalez-Prelcic, A. Ali, V. Va and R. W. Heath, "Millimeter-wave communication with out-of-band information," *IEEE Commun. Mag.*, vol. 55,
no. 12, pp. 140–146, Dec. 2017.
[15] A. Ali, N. Gonz´alez-Prelcic and R. W. Heath, "Millimeter wave beamselection using out-of-band spatial information," IEEE Trans. Wireless Commun., vol. 17, no. 2, pp. 1038–1052, Feb. 2018.
[16] M. Peter et al. Measurement campaigns and initial channel models for preferred suitable frequency ranges. Accessed: Mar. 2016. [Online]. Available:
https://bscw.5g-mmmagic.eu/pub/bscw.cgi/d94832/ mmMAGIC D2-1.pdf
[17] J. Scarlett, J. S. Evans and S. Dey, "Compressed sensing with prior
information: Information-theoretic limits and practical decoders," IEEE
Trans. Signal Process., vol. 61, no. 2, pp. 427–439, Jan. 2013.
[18] L. Lu, W. Xu, Y. Cui, M. Dai and J. Long, "Block spectrum sensing
based on prior information in cognitive radio networks," in Proc. IEEE Wireless Communications and Networking Conference (WCNC), Marrakesh,
Morocco, 2019, pp. 1-5.
[19] L. Lu, W. Xu, Y. Cui, Y. Dang, S. Wang, "Gamma-distribution-based
logit weighted block orthogonal matching pursuit for compressed sensing,"
Electron. Lett., vol. 55, no. 17, pp. 959–961, Aug. 2019.
[20] D. Tse and P. Viswanath, "Fundamentals of wireless communication,"
Cambridge, U.K. Cambridge Univ. Press, 2005.
[21] A. M. Sayeed, "Deconstructing multiantenna fading channels," IEEE Trans.
Signal Process., vol. 50, no. 10, pp. 2563–2579, Oct, 2002.
[22] C. Huang, L. Liu, C. Yuen and S. Sun, "Iterative channel estimation using
LSE and sparse message passing for mmWave MIMO systems," IEEE Trans. Signal Process., vol. 67, no. 1, pp. 245–259, Jan., 2019.
[23] J. Sherman, "Properties of focused apertures in the Fresnel region," IRE
Trans. Antennas and Propag., vol. 10, no. 4, pp. 399–408, Jul. 1962.
[24] Y. C. Eldar, P. Kuppinger and H. Bolcskei, "Block-sparse signals: Uncertainty relations and efficient recovery," *IEEE Trans. Signal Process.*, vol. 58,
no. 6, pp. 3042–3054, Jun. 2010.
[25] A. Liu, V. K. N. Lau and W. Dai, "Exploiting burst-sparsity in massive
MIMO with partial channel support information," IEEE Trans. Wireless Commun., vol. 15, no. 11, pp. 7820–7830, Nov. 2016.
[26] Z. Gao, C. Hu, L. Dai and Z. Wang, "Channel estimation for millimeterwave massive MIMO with hybrid precoding over frequency-selective fading
channels," *IEEE Commun. Lett.*, vol. 20, no. 6, pp. 1259–1262, Jun. 2016.
[27] H. Ma, X. Yuan, L. Zhou, B. Li and R. Qin, "Joint block support recovery
for sub-Nyquist sampling cooperative spectrum sensing," IEEE Wireless Commun. Lett., vol. 12, no. 1, pp. 85–88, Jan. 2023.
[28] B. Weston, Approximations to the non central chi-square and noncentral F
distributions. Texas Tech University, 1978.
[29] M. K. Simon, "Probability distributions involving Gaussian random variables: A handbook for engineers and scientists," *Berlin, Germany. Springer*,
2006.
[30] B. Klar, "A note on gamma difference distributions," *J. Stat. Comput. Simul.*,
vol. 85, no. 18, pp. 3708–3715, 2015.
[31] F. Olver, D. Lozier, R. Boisvert and C. Clark, NIST handbook of F
distributions. Cambridge University Press, 2010.