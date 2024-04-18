Shokichi Takakura 1 2 **Taiji Suzuki** 1 2

## Abstract

In this paper, we study the feature learning ability
of two-layer neural networks in the mean-field
regime through the lens of kernel methods. To
focus on the dynamics of the kernel induced by
the first layer, we utilize a two-timescale limit,
where the second layer moves much faster than
the first layer. In this limit, the learning prob-
lem is reduced to the minimization problem over
the intrinsic kernel. Then, we show the global
convergence of the mean-field Langevin dynam-
ics and derive time and particle discretization er-
ror. We also demonstrate that two-layer neural
networks can learn a union of multiple reproduc-
ing kernel Hilbert spaces more efficiently than
any kernel methods, and neural networks aquire
data-dependent kernel which aligns with the tar-
get function. In addition, we develop a label noise
procedure, which converges to the global opti-
mum and show that the degrees of freedom ap-
pears as an implicit regularization.

## 1. Introduction

Although deep learning has achieved great success in var-
ious fields, the theoretical understanding is still limited.
Several works studied the relation between deep learning
and kernel medhods, which are well-studied in the machine
learning community. A line of work has shown that the
training dynamics of infinite-width neural networks can be
approximated by linearized dynamics and the corresponding
kernel is called neural tangent kernel (NTK) (Jacot et al.,
2018; Arora et al., 2019b). Furthermore, generalizability of
neural networks is shown to be characterized by the spec-
tral properties of the NTK (Arora et al., 2019a; Nitanda &
Suzuki, 2020). However, the NTK regime is reffered as a
lazy regime and cannot explain the feature learning ability
to adapt the intrinsic structure of the data since neural net-

    1Department of Mathematical Informatics, the University of
Tokyo, Tokyo, Japan 2Center for Advanced Intelligence Project,
RIKEN, Tokyo, Japan. Correspondence to: Shokichi Takakura
<masayoshi361@g.ecc.u-tokyo.ac.jp>.

works behave as a static kernel machine in the NTK regime.
On the other hand, several works have shown the superiority
of the neural networks to the kernel methods in terms of
the sample complexity (Barron, 1993; Yehudai & Shamir,
2019; Hayakawa & Suzuki, 2020). Thus, as shown in sev-
eral empirical studies (Atanasov et al., 2021; Baratin et al.,
2021), neural networks must acquire the data-dependent
kernel by gradient descent. However, it is challenging to
establish a beyond NTK results on the feature learning of
neural networks with gradient-based algorithm due to the
non-convexity of the optimization landscape.

One promising approach is the mean-field analysis (Mei
et al., 2018; Hu et al., 2020), which is an infinite-width
limit of the neural networks in a different scaling than the
NTK regime. In the mean-field regime, the optimization
of 2-layer neural networks, which is non-convex in general,
is reduced to the convex optimization problem over the
distribution on the parameters. Exploiting the convexity
of the problem, several works (Nitanda & Suzuki, 2017;
Mei et al., 2018; Chizat & Bach, 2018) have shown the
convergence to the global optimum. Recently, quantitative
optimiztion guarantees has been established for the mean-
field Langevin dynamics (MFLD) which can be regarded as
a continuous limit of a noisy gradient descent (Chizat, 2022;
Nitanda et al., 2022). Moreover, very recently, uniform-in-
time results on the particle discretization error have been
obtained (Chen et al., 2023; Suzuki et al., 2022; 2023a).
This allows us to extend results effectively from infinite-
width neural networks to finite-width neural networks.

Although the mean-field limit allows us to analyze the fea-
ture learning in neural networks, the connection between
mean-field neural networks and its corresponding kernel is
still unclear. To establish the connection to the previous
works (Jacot et al., 2018; Suzuki, 2018; Ma & Wu, 2022) on
the relationship between neural networks and kernel meth-
ods, we address the following question:
Is it possible to learn the optimal kernel through the MFLD?
Futhermore, can this kernel align with the target function
by excluding the effect of noise?

To analyze the dynamics of the kernel inside the neural net-
works, we adopt a two-timescale limit (Marion & Berthier,
2023), which separates the dynamics of the first layer and
the second layer. Then, we establish the connection between

neural networks training and kernel learning (Bach et al.,
2004), which involves selecting the optimal kernel for the
data. We provide the global convergence gurantee of the
MFLD by showing the convexity of the objective functional
and derive the time and particle discretization error. Then,
we prove that neural networks can aquire data-dependent
kernel and achieve better sample complexity than any linear
estimators including kernel methods for a union of multiple
RKHSs. We also investigate the alignment with the target
function and the degrees of freedom of the acquired kernel,
which measures the complexity of the kernel, and develop
the label noise procedure which provably reduces the de-
grees of freedom by just adding the label noise. Finally, we
verify our theoretical findings by numerical experiments.
Our contribution can be summarized as follows:

- We prove the convexity of the objective functional with
respect to the first layer distribution and the global convergence of the MFLD in two-timescale limit in spite of the complex dependency of the second layer on the distribution of the first layer. We also derive the time and particle discretization error of the MFLD.
- We show that neural networks can adapt the intrinsic
structure of the target function and achieve a better sample complexity than kernel methods for a variant of Baron space (Ma & Wu, 2022), which is a union of multiple RKHS.
- We study the training dynamics of the kernel induced
by the first layer and show that the alignment is increased during the training and achieve Ω(1) alignment while the kernel alignment at the initialization is O(1/
√
d) for a single-index model, where d is the
input dimension. We also show that the presence of the intrinsic noise induces a bias towards the large degrees of freedom. To alleviate this issue, we propose the label noise procedure to reduce the degrees of freedom and prove the linear convergence to the global optimum.

## 1.1. Related Works

Relation between Neural Networks and Kernel Methods
Suzuki (2018) derived the generalization error bound for
deep learning models using the notion of the degrees of
freedom in the kernel literature. Ma & Wu (2022) charac-
terized the function class, which two-layer neural networks
can approximate, by a union of multiple RKHSs. However,
they did not give any optimization gurantee. Atanasov et al.
(2021) pointed out the connection between training of neural
networks and kernel learning, but their analysis is limited to
linear neural networks with whitened data.

Mean-field Analysis
                     Chen et al. (2020) conducted NTK-
type analysis using mean-field limit. However, their anal-
ysis relies on the closeness of the first-layer distribution

to the initial distribution. Several works have shown that
the superiority of the mean-field neural networks to kernel
methods including NTK with global optimization guaran-
tee. For example, Suzuki et al. (2023b) derived a linear
sample complexity with respect to the input dimension d
for k-sparse parity problems while kernel methods require
Ω(dk) samples. In addition, Mahankali et al. (2023) showed
the superiority of the mean-field neural networks to the ker-
nel methods for even quartic polymonial. However, these
works fix the second layer during the training to ensure the
boundedness of each neuron. Unlike these studies, we con-
sider trainable second layer, and focus on the relationship
between neural networks and kernel machines and its impli-
cation to the feature learning ability of neural networks.

Two-timescale Limit
                     Two-timescale limit is introduced
to the analysis for training of neural networks in Marion
& Berthier (2023). They provided the global convegence
gurantee for simplified neural networks but their analysis
is limited to the single input setting and the relation to the
kernel learning was not discussed. Bietti et al. (2023) lever-
aged the two-timescale limit to analyze the training of neural
networks with a multi-index model and show the saddle-
to-saddle dynamics. However, they used non-parametric
model for the second layer, which is different from practical
settings.

Feature Learning in Two-layer Neural Networks
                                               Aside
from the mean-field analysis, there exists a line of work
which studies the feature learning in (finite-width) two-layer
neural networks (Damian et al., 2022; Mousavi-Hosseini
et al., 2022). For instance, Damian et al. (2022) show that
the random feature model with the first layer parameter up-
dated by one-step gradient descent can learn p-degree poly-
nomial with O(d) samples while kernel methods require
Ω(dp) samples. However, most of these works consider
two-stage optimization procedure, where the first layer is
trained before proceeding to train the second layer.

Implicit Bias of Label Noise
                              Implicit bias of label noise
has been intensively studied recently (Damian et al., 2021;
Li et al., 2021; Vivien et al., 2022). For example, Li et al.
(2021) developed a theoretical framework to analyze the im-
plicit bias of noise in small noise and learning rate limit and
prove that the label noise induces bias towards flat minima.
On the other hand, we elucidate the implicit regularization
of label noise on the kernel inside the neural networks.

## 1.2. Notations

We write the expectation with respect to X ∼ µ by EX∼µ[·]
or Eµ[·].

KL denotes the Kullback-Leibler divergence negative entropy Ent(µ) = Eµ[log µ]. N(v, Σ) denotes the

KL(ν | µ) =
          �
            log
              �
               µ(w)
               ν(w)
                  �
                   dµ(w) and Ent denotes the

Gaussian distribution with mean v and covariance Σ and
υ(S) for S ⊂ Rd denotes the uniform distribution on S. P
denotes the set of probability measures on Rd′ with finite second moment. For a matrix A, ∥A∥op denotes the operator norm with respect to *∥·∥*2 and ∥A∥F denotes the Frobenius norm. For an operator A : L2(µ) → L2(µ), ∥A∥op denotes the operator norm with respect to *∥·∥*L2(µ). For l : R2 → R,
∂1l denotes the partial derivative with respect to the first argument. For a symmetric matrix A, λmin(A) denotes the minimum eigenvalue of A. With a slight abuse of notation, we use f(X) for f : Rd → R and X = [x(1), . . . , x(n)]⊤ ∈
Rn×d to denote [f(x(1))*, . . . , f*(x(n))]⊤.

## 2. Problem Settings 2.1. Mean-Field And Two-Timescale Limit In Two-Layer Neural Networks

Given input x ∈ Rd, let us consider the following two-layer neural network model:

$$f(x;a,\{w_{i}\}_{i=1}^{N})=\frac{1}{N}\sum_{i=1}^{N}a_{i}h(x;w_{i}),$$

where $a_{i}\in\mathbb{R}$, $w_{i}\in\mathbb{R}^{d^{\prime}}$ and $h(x;w_{i})$ is the activation function with parameter $w_{i}$.

Mean-field limit of the above model is defined as an integral over neurons:

$$f(x;P):=\int ah(x;w)P(\mathrm{d}a,\mathrm{d}w),\tag{1}$$

where P is a probability distribution over the parameters of
the first and second layers. However, in this formulation,
the first and the second layer are entangled, and thus it is
difficult to characterize the feature learning, which takes
place in the first layer. To alleviate this issue, we consider
the following formulation:

$$f(x;a,\mu):=\int a(w)h(x;w)\mathrm{d}\mu(w),$$

where $a(w)=\int aP(\mathrm{d}a\mid w)$ and $\mu(w)=\int P(a,w)\mathrm{d}a$ is the marginal distribution of $w$. Similar formulation can be found in Fang et al. (2019). This formulation explicitly separates the first and the second layer, which allows us to focus on the feature learning dynamics in the first layer. More generally, we consider the multi-task learning settings. That is, $f(x;a,\mu):\mathbb{R}^{d}\to\mathbb{R}^{T}$ is defined by

$$f_{i}(x;a,\mu):=\int a^{(i)}(w)h(x;w)\mathrm{d}\mu(w),$$

where $a:\mathbb{R}^{d^{\prime}}\to\mathbb{R}^{T}$ is the second layer and $a^{(i)}$ is the $i$-th component of $a$. Note that the first layer $\mu(w)$ is shared among tasks.

Let ρ be the true or empirical distribution of the pair of input and output (*x, y*) ∈ Rd+T , and ρX be the marginal distribution of x. Then, for *λ >* 0, the (regularized) risk is defined by

$$\begin{array}{l}{{L(a,\mu)=\frac{1}{T}\sum_{i=1}^{T}\mathbb{E}_{\rho}[l_{i}(f_{i}(x;a,\mu),y)],}}\\ {{F(a,\mu)=L(a,\mu)+\lambda\mathbb{E}_{\mu}[r(a(w),w)],}}\end{array}$$
where li is the loss function for the i-th task, and r is the regularization term. In this paper, we consider l2-regularization r(*a, w*) = λa
2T
�T
i=1 a(i)2 + λw
2 ∥w∥2
2, where a = (a(i))T
i=1
and λa, λw > 0. We define ¯λa = λλa, ¯λw = λλw, and
ν = N(0*, I/λ*w) for notational simplicity.

To separate the dynamics of the first and second layer, we
introduce the two-timescale limit (Marion & Berthier, 2023),
where the second layer moves much faster than the first layer.
In this limit, the first layer a(i) converges instantaneously to
the unique optimal solution of mina Eρ[l(f(x; a, µ), y)] +
¯λa
 2 ∥a∥2
      L2(µ) since F(a, µ) is strongly convex with respect

to a, As shown in the next section, ∥a∥2
                                        L2(µ) corresponds
to the RKHS norm for the kernel induced by the first layer.
Since the optimal second layer is a functional of the first
layer distribution µ, we write aµ for the optimal solution.
Then, the learning problem is reduced to the minimization
of the limiting functional G(µ) = F(aµ, µ). We also define
U(µ) by U(µ) := L(aµ, µ) +
                               ¯λ
                               2T Eµ[∥aµ(w)∥2
                                              2]

Throughout the paper, we assume that h(x; wi) satisfies
Assumption 2.1. For example, tanh(u · x + b)(w = (u, b))
satisfies the assumption if EρX[∥x∥2
                               2], EρX[∥x∥4
                                          2] are finite.

Assumption 2.1. h(x; w) is twice differentiable with re-
spect to w and there exist constants cR, cL > 0 such
that supw |h(x; w)| ≤ 1, EρX[supw ∥∇wh(x; w)∥2
                                             2] ≤
c2
R, EρX[supw
            ��∇2
               wh(x; w)
                       ��2
                        op] ≤ c2
                               L.

## 2.2. Kernel Induced By The First Layer

Let us define the kernel induced by the first layer as follows:

$$k_{\mu}(x,x^{\prime})=\int h(x;w)h(x^{\prime};w)\mathrm{d}\mu(w).$$

Obviously, this is a symmetric positive definite kernel. It is well-known that there exists a unique RKHS $\mathcal{H}_{\mu}$ corresponding the kernel $k_{\mu}$. Furthermore, the RKHS norm $\|f\|_{\mathcal{H}_{\mu}}$ is equal to the minimum of $\|a\|_{L^{2}(\mu)}$ over all $a$ such that $f(x;a,\mu)=\int a(w)h(x;w)\mathrm{d}\mu(w)$(Bach, 2017). Thus, the learning problem of the second layer is equivalent to the following optimization problem:

$$\min_{f_{i}\in\mathcal{H}_{\mu}}\sum_{i=1}^{T}\mathbb{E}_{\rho}[l_{i}(f_{i}(x),y)]+\sum_{i=1}^{T}\frac{\bar{\lambda}_{a}}{2}\|f_{i}\|_{\mathcal{H}_{\mu}}^{2}.\tag{2}$$
Thus, learning first layer is equivalent to kernel learning (Bach et al., 2004), which choosing suitable RKHS
Hµ.

## 2.3. Mean-Field Langevin Dynamics

We optimize the limiting functional G(µ) by the mean-field Langevin dynamics (MFLD):

$$\mathrm{d}w_{t}=-\mathbf{\nabla}_{w}{\frac{\delta G(\mu)}{\delta\mu}}\mathrm{d}t+{\sqrt{2\lambda}}\mathrm{d}B_{t},$$
where w0 ∼ µ0 := ν, (Bt)t≥0 is the d′-dimensional Brownian motion, and δG(µ)
δµ
is the first variation of G(µ). The Fokker-Planck equation of the above SDE is given by

$$\partial_{t}\mu_{t}=\lambda\Delta\mu_{t}+\mathbf{\nabla}\cdot\left[\mu_{t}\mathbf{\nabla}{\frac{\delta G(\mu)}{\delta\mu}}\right],$$
where µt is the distribution of wt. It is known that the MFLD is a Wasserstein gradient flow which minimizes the entropy-regularized functional: G(µ) := G(µ) + λ Ent(µ).

To implement the MFLD, we need time and particle dis-
cretization (Chen et al., 2023; Suzuki et al., 2022; 2023a).
For a set of N particles W = {wi}N
                              i=1, we define the empir-
ical distribution µW = 1

              N
                �N
                  i=1 δwi. Let Wk = {w(k)
                                i
                                  }N
                                  i=1
be a set of N particles at the k-th iteration, and µ(N)
                               k
                                  be a
distribution of Wk on Rd′×N. Then, at each step, we update
the particles as follows:

$$w_{i}^{(k+1)}=w_{i}^{(k)}-\eta\mathbf{\nabla}\frac{\delta G(\mu w_{k})}{\delta\mu}(w_{i}^{(k)})+\sqrt{2\eta\lambda}\xi_{i}^{(k)},$$
where *η >* 0 is the step size and ξ(k)
i
∼ N(0, I) are i.i.d.

Gaussian noise. This can be regarded as a noisy gradient descent.

## 3. Convergence Analysis

λ
δG(µ)

As shown in Nitanda et al. (2022); Chizat (2022), the con-
vergence of the MFLD depends on the convexity of the
functional and the properties of the proximal Gibbs distri-
bution, which is defined as pµ(w) ∝ exp
                                    �
                                     − 1

                                            δµ (w)
                                                   �
                                                     .
In the training of neural networks, the convexity is usually
ensured by the linearity of f with respect to distribution as
in Eq. (1). On the other hand, in the two-timescale limit,
f(x; µ) := f(x; aµ, µ) is not linear with respect to µ be-
cause the second layers aµ depend on µ in a non-linear way.
However, we can prove that the functional G(µ) is convex
and its first variation can be written in a simple form if
{li}T
   i=1 are convex.

Theorem 3.1. Assume that the losses {li}T
i=1 are convex.

Then, the limiting functional G(µ) is convex. That is, it holds that

$$G(\mu_{1})+\int\frac{\delta G(\mu_{1})}{\delta\mu}(w)(\mu_{2}(w)-\mu_{1}(w))\mathrm{d}w\leq G(\mu_{2})$$
for any µ1, µ2 ∈ P*. In addition, the first variation of* G(µ)
is given by

$$\delta G\over\delta\mu}(\mu)(w)=\lambda\biggl{(}-{\lambda_{a}\over2T}||a_{\mu}(w)||_{2}^{2}+{\lambda_{w}\over2}||w||_{2}^{2}\biggr{)}.\tag{3}$$
See Appendix B.1 for the proof. We remark that the convexity holds for general regularization term r which is strongly convex with respect to a.

The convergence rate of the MFLD depends on the constant in the log-Sobolev inequality for the proximal distribution pµ.

Definition 3.2. We say a probability distribution µ satisfies log-Sobolev inequality with constant *α >* 0 if for all smooth function g : Rd → R with Eµ[g2] < ∞,

$$\mathbb{E}_{\mu}[g^{2}\log g^{2}]-\mathbb{E}_{\mu}[g^{2}]\log\mathbb{E}_{\mu}[g^{2}]\leq{\frac{2}{\alpha}}\mathbb{E}_{\mu}[\left\|\nabla g\right\|^{2}].$$
To derive the LSI constant α, we assume either of the following conditions on the loss functions:

Assumption 3.3. li is squared loss. That is, li(z, y) =
1
2(z − y)2. In addition, |yi| ≤ cl a.s. for some constant
cl > 0.

Assumption 3.4. li is convex and twice differentiable
with respect to the first argument and |∂1li(z, y)|
                                               ≤
cl,
  ��∂2
    1li(z, y)
           �� ≤ 1 for any z, y ∈ R.

The latter assumption is satisfied by several loss functions
such as logistic loss.
                        Then, using the formula for the
first variation, we can derive the LSI constant applying
the Holley-Stroock argument (Holley & Stroock, 1987) for
bounded perturbation.

Lemma 3.5. Assume that each li satisfies Assumption 3.3
or 3.4. Then, the proximal distribution pµ for any µ ∈ P

satisfies LSI with constant α = λw exp
                                        �
                                         −2 λac2
                                                l
                                              ¯λ2a

�
 .

The proof can be found in Appendix B.2.
Remark 3.6. In the standard formulation (1), the first varia-
tion of F(P) = Eρ[l(f(x; P), y)] + λEP [r(a, w)] is given
by δF

   δP = Eρ[∂1l(f(x; P), y)ah(x; w)] + λr(a, w). Then,
Eρ[∂1l(f(x; P), y)ah(x; w)] is not bounded nor Lipschitz
continuous with respect to (a, w), even if ∂1l and h is
bounded. Therefore, without two-timescale limit, it is diffi-
cult to obtain a LSI constant even for the single output set-
ting. Indeed, previous works fix the second layer or clip the
output using some bounded function (Chizat, 2022; Nitanda
et al., 2022; Suzuki et al., 2023a) to ensure the boundedness
or Lipschitz continuity of the output of neurons.

Combining above results, we can show the linear conver-
gence of the MFLD.
Theorem 3.7. Let µ∗ be the minimizer of G(µ) and
GN(µ(N)
     k
        ) = NEW ∼µ(N)
                     k
                        [G(µW )] + λ Ent(µ(N)
                                           k
                                               ). Then,
for the constant α in Lemma 3.5, µt satisfies

G(µt) − G(µ∗) ≤ exp(−2αλt)(G(µ0) − G(µ∗))

for any 0
            ≤
                t.
                     Furthermore,
                                  for any η
                                              <
min {1/4, 1/(4λα)}, µ(N)
                   k
                      satisfies

1
N GN(µ(N)
      k
         ) − G(µ∗)

≤ exp(−αληk/2)(GN(µ(N)
             0
              ) − G(µ∗)) + ¯δη,N,

where ¯δη,N = O( 1

N + η).

See Appendix B.3 for the proof and the concrete expres-
sion of discretization error ¯δη,N. The proof is based on the
framework in Suzuki et al. (2023a). To obtain discretization
error, we need to prove some additional conditions on the
smoothness of the objective functional. This is far from triv-
ial due to the non-linear dependency of aµ on µ. Note that
we cannot apply the arguments in Chizat (2022); Nitanda
et al. (2022); Suzuki et al. (2023a) without two-timescale
limit since they assume the boundedness or Lipschitz con-
tinuity of each neuron. See also Remark 3.6 for detailed
discussion.

Furthermore, the convergence of the loss function in the
discretized setting can be transferred to the convergence of
the function value of the neural networks as shown in the
following proposition.
Proposition 3.8. Assume that h(x; w) is cR-Lipschitz con-
tinuous with respect to w for any x ∈ S, where S is some
subset of Rd. Let ∆ = c2
                      R

λα(GN(µ(N)
       k
          )−NG(µ∗))+ c2
                       RG(µ0)

subset of $\mathbb{R}^{d}$. Let $\Delta=\frac{c_{R}^{r}}{\lambda\alpha}(\mathcal{G}^{N}(\mu_{k}^{(N)})-N\mathcal{G}(\mu^{*}))+\frac{c_{R}^{r}\mathcal{G}(\mu_{0})}{\lambda_{w}}$. Then, we have_

$$\mathbb{E}_{W_{k}\sim\mu_{k}^{(N)}}\left[\sup_{\begin{subarray}{c}(x,y)\\ \in S\times S\end{subarray}}\left|k_{\mu_{W_{k}}}(x,y)-k_{\mu^{*}}(x,y)\right|^{2}\right]=O\bigg{(}\frac{\Delta}{N}\bigg{)}.$$

_In addition, if $l_{i}$ satisfies Assumption 3.3, then we have_

$$\mathbb{E}_{W_{k}\sim\mu_{k}^{(N)}}\left[\sup_{x\in S}(f_{i}(x;\mu_{W_{k}})-f_{i}(x;\mu^{*}))^{2}\right]$$ $$=O\bigg{(}\frac{c_{0}^{2}(\bar{\lambda}_{a}^{2}+1)}{\bar{\lambda}_{a}^{4}}\cdot\frac{\Delta}{N}\bigg{)}.$$

See Appendix B.4 for the proof. Note that this result is not
covered by Lemma 2 in Suzuki et al. (2023b) since their
analysis relies on the Lipschitz continuity of each neuron.
In the following sections, we consider infinite-width neural
networks trained by the MFLD for simplicity, but the results
can be transferred via this proposition to the finite-width
neural networks trained by the discretized MFLD.

## 4. Generalization Error For Barron Spaces And Superiority To Kernel Methods

In this section, we provide the separation of the general-
ization error between neural networks and kernel methods
which cannot adapt the intrinsic structure of the target func-
tion.

Let D =
        �
          (x(i), y(i))
                   �n
                    i=1 be training data sampled from
the true distribution in an i.i.d. manner. We define X =
�
x(1), . . . , x(n)�⊤ ∈ Rn×d, Yi = [y(1)
                                i
                                   , . . . , y(n)
                                         i
                                           ]⊤ ∈ Rn

and ˆΣµ = Eµ[h(X; w)h(X; w)⊤]. In the following, we
write the true distribution by ρ and the empirical distribu-
tion by ˆρ. In addition, to distinguish the empirical risk
and population risk, we write Uρ(µ), Gρ(µ) for the (regu-
larized) population risk and Uˆρ(µ), Gˆρ(µ) for the empirical
risk. Then, we assume the following.

Assumption 4.1. the output yi for each task is generated by
yi = f ◦
     i (x) + εi, where f ◦
                      i : Rd → R is the target function
and εi is the noise, which follows υ([−σ, σ]) independently
for some σ ≥ 0.

To see the benefit of the feature learning or kernel learning,
we consider the following function class.

Definition 4.2 (KL-restricted Barron space). Let PM =
{µ ∈ P | KL(ν | µ) ≤ M} for some M > 0. Then, we
define the KL-restricted Barron space as

$$\mathcal{B}_{M}=\big{\{}f(x;a,\mu)\mid\mu\in\mathcal{P}_{M},a\in L^{2}(\mu)\big{\}},$$

and the corresponding norm as

$$\|g\|_{\mathcal{B}_{M}}=\inf_{\mu\in\mathcal{P}_{M},a\in L^{2}(\mu)}\Big{\{}\|a\|_{L^{2}(\mu)}\mid g(x)=f(x;a,\mu)\Big{\}}.$$

This can be seen as a variant of Barron space in E et al.
(2019); Ma & Wu (2022). Similar function classes are
also considered in Bach (2017) but they consider Frank-
Wolfe type optimization algorithm, which is different from
usual gradient descent. We remark that Barron space can
be regarded as a union of RKHS: BM = �

                                    µ∈PM Hµ and
the norm ∥f∥BM is equal to the minimum of ∥f∥Hµ over
all µ ∈ PM (Ma & Wu, 2022).

To obtain the generalization guarantee, we utilize the Rademacher complexity. The Rademacher complexity of a function class $\mathcal{F}$ of functions $f:\mathbb{R}^{d}\rightarrow\mathbb{R}^{T}$ is defined by

$$\mathfrak{R}(\mathcal{F}):=\mathbb{E}_{\sigma}\left[\sup_{f\in\mathcal{F}}\frac{1}{nT}\sum_{i=1}^{n}\sum_{t=1}^{T}\sigma_{it}f_{t}(x_{i})\right],$$
where σit is an i.i.d. Rademacher random variable (P(σit =
1) = P(σit = −1) = 1/2). Then, we have the following bound for the mean-field neural networks.

Lemma 4.3. Assume that h(x; w) satisfies Assumption 2.1.

Define a class of the mean-field neural networks by

$$\mathcal{F}_{R,M}=\Big{\{}f(x;a,\mu)\mid\operatorname{KL}(\nu\mid\mu)\leq M,\|a\|_{L^{2}(\mu)}^{2}\leq R\Big{\}}.$$

_Then, the Rademacher complexity of $\mathcal{F}_{R,M}$ is bounded by_

$$\mathfrak{R}(\mathcal{F}_{R,M})\leq\sqrt{R(4M\ \overline{+2T\log2)}\over nT}=O\bigg{(}\frac{R(M+T)}{nT}\bigg{)}.$$
This is a generalization of the result in Chen et al. (2020).

See Appendix C.2 for the proof.

Then, we can derive the generalization error bound for the
empirical risk minimizer ˆµ = argmin
                                 µ
                                     Gˆρ(µ). Note that the

empirical risk minimizer ˆµ can be obtained by the MFLD
as shown in Theorem 3.7.

Theorem 4.4. Assume that Assumption 2.1 and 4.1 holds
with σ = 0, T = 1, and f ◦
                     1 ∈ BM, ∥f ◦
                               1 ∥BM ≤ R for given
M, R > 0. In addition, let λ = 1/√n, and λa = 2M/R.
Then, with probability at least 1 − δ over the choice of
training examples, it holds that

$$\left\|f(\cdot;\hat{\mu})-f^{\circ}\right\|_{L^{2}(\rho_{X})}^{2}=O\Biggl((R+1)\sqrt{\begin{matrix}M+1+\log1/\delta\\ n\end{matrix}}\Biggr).$$
See Appendix C.3 for the proof. Therefore, if R = O(1), the mean-field neural networks can learn the Barron space with n = O(M) samples.

Next, we show the lower bound of the estimation error for
kernel methods. For a given kernel k, a kernel method
returns a function of the form f(x) = �n
                                       i=1 αik(x, xi) for
αi ∈ R. This type of estimator is called linear estimator.
The following theorem gives the lower bound of the sample
complexity for any linear estimators.

Theorem 4.5. Fix m ∈ N and let d ≥ max{2, m} and ρX
be the uniform distribution on {−1, 1}d and h(x; w) =
tanh(u · x + b), where w = (u, b) ∈ Rd+1.
                                           In addi-
tion, let Hn ⊂ L2(ρX) be a set of functions of the form
�n
  i=1 αihi(x) and d(f, Hn) = inf ˆ
                               f∈Hn ∥f − ˆf∥L2(ρX).
Then, there exist constants c1, c2 > 0 which is independent
of d, such that, for every choice of fixed basis functions
h1(x), . . . , hn(x), it holds that

$$\sup_{f\in\mathcal{B}_{M},\|f\|_{\mathcal{B}_{M}}^{2}\leq R}d(f,H_{n})\geq\frac{1}{4}$$

_if $n\leq N/2$ and $M=c_{1}d\log d,R=c_{2}$ where $N=\binom{d}{m}=\Omega(d^{m})$._
The proof can be found in Appendix C.4. This theorem implies that any kernel estimator with n = o(dm) cannot learn the Barron space with M = Ω(d log d). This is in contrast to the mean-field neural networks which can learn the Barron space with n = O(d log d) samples as shown in Theorem 4.4. This is because the kernel methods cannot adapt the underlying RKHS under the target function.

Therefore, feature learning or kernel learning is essential to obtain good generalization results.

## 5. Properties Of The Kernel Induced By The First Layer

In the previous section, we proved that feature learning is
essential to obtain good generalization results and two-layer
neural networks trained by the MFLD can excel over kernel
methods. In this section, we study the properties of the
kernel trained via the MFLD. We show that in regression
problem, the kernel induced by the first layer moves to in-
crease kernel and parameter alignment. We also proved that
the presence of the noise ε induces bias towards the large
degrees of freedom. To overcome this issue, we provide
the label noise procedure, which provably converges to the
global minima of the objective functional with the degrees
of freedom regularization.

## 5.1. Kernel And Parameter Alignment

For simplicity, we consider the single output setting T = 1
and define f ◦ = f ◦
1 . In addition, we consider tanh activation h(x; w) = tanh(u · x + b) (w = (*u, b*)) and assume that ρX = N(0, I). To measure the adaptation of the kernel to the target function, we define the kernel alignment Cristianini et al. (2001). which is commonly used to measure the similarity between kernel and labels.

Definition 5.1. For µ *∈ P*, the empirical and population kernel alignment is defined by

$$\hat{A}(\mu)=\frac{f^{\circ}(X)^{\top}\hat{\Sigma}_{\mu}f^{\circ}(X)}{\|f^{\circ}(X)\|_{2}^{2}\Big{\|}\hat{\Sigma}_{\mu}\Big{\|}_{\mathrm{F}}},$$ $$A(\mu)=\frac{\mathbb{E}_{x\sim\rho_{X},x^{\prime}\sim\rho_{X}}\left[f^{\circ}(x)k_{\mu}(x,x^{\prime})f^{\circ}(x^{\prime})\right]}{\mathbb{E}_{\rho_{X}}\left[f^{\circ}(x)^{2}\right]\sqrt{\mathbb{E}_{x\sim\rho_{X},x^{\prime}\sim\rho_{X}}\left[k(x,x^{\prime})^{2}\right]}}.$$
Note that ˆA(µ) and A(µ) satisfy 0 ≤ ˆA(µ), A(µ) ≤ 1 and larger A(µ) means that the kernel is aligned with the target function. In this section, we consider the regression problem with squared loss. if σ = 0, the limiting functional Uˆρ(µ) has the following explicit formula.

$$U_{\hat{\rho}}(\mu)=\frac{\bar{\lambda}_{a}}{2}f^{\circ}(X)^{\top}(\hat{\Sigma}_{\mu}+n\bar{\lambda}_{a}I)^{-1}f^{\circ}(X).$$
From Jensen's inequality, we have

$$\hat{A}(\mu)\geq\frac{\bar{\lambda}_{a}\|f^{\circ}(X)\|_{2}^{2}}{2U_{\hat{\rho}}(\mu)n}-\bar{\lambda}_{a}.$$
See Lemma D.2 for the detailed derivation. Therefore, the minimization of Uˆρ(µ) is equivalent to the maximization of the lower bound of the kernel alignment.

To derive a concrete expression of the kernel alignment, we
assume that the target function f ◦ is a single-index model
, which is a common structural assumption on the target
function (Bietti et al., 2022).

Assumption 5.2. There exist ˜f
                              :
                                R
                                    →
                                       R, u◦
                                              ∈
Rd (∥u◦∥2 = 1) such that ˜f is differentiable, ∥ ˜f ′∥∞,
∥ ˜f∥∞ ≤ 1, Ez∼N(0,1)[ ˜f(z)] = 0, and f ◦(x) = ˜f(u◦ · x).

We also define the parameter alignment, which measures the similarity between the first layer parameters and the intrinsic direction of the target function.

Definition 5.3. For µ *∈ P*, the parameter alignment is defined as

$$P(\mu)=\mathbb{E}_{(u,b)\sim\mu}\left[\frac{(u^\top u^\diamond)^2}{\left\|u\right\|^2}\right].$$

Here, we define $\frac{(u^\top u^\diamond)^2}{\left\|u\right\|^2}=0$ for $u=0$.

This is the expected cosine similarity between parameters and the target direction, and thus 0 ≤ P(µ) ≤ 1. Note that larger P(µ) means that the first layer parameters are aligned with the intrinsic direction of the target function.

Then, we have the following result on the kernel for empirical risk minimizer ˆµ.

Theorem 5.4. Assume that Assumption 5.2 holds. Then, there exists universal constants c3, c4, c5 satisfying the following: Let ˆµ be the minimizer of Gˆρ(µ) with n ≥
c3(d log d+log 1/δ), λ = c4/(d log d)*, and* λa = c5d log d for 0 < δ < 1 and d ≥ 2. Then, the kernel and parameter alignment for the initial distribution µ0 and the empirical risk minimizer ˆµ satisfies

$A(\mu_{0})=0(1/\sqrt{d})$, $A(\hat{\mu})=0(1)$, $P(\mu_{0})=0(1/d)$, $P(\hat{\mu})=0(1)$,
with probability at least 1 − δ over the choice of samples.

See Appendix D.2 for the proof. In high-dimensional setting d ≫ 1, A(ˆµ), P(ˆµ) = Ω(1) is a significant improvement over P(µ0) = O(1/d), A(µ0) = O(1/
√

                                d) at the initial-
ization. For the parameter alignment, similar results are
shown in Mousavi-Hosseini et al. (2022), but they train only
the first layer and use the norm of the irrelevant directions as
a measure of the alignment. On the other hand, we consider

the joint learning of the first and second layers and use the cosine similarity as a measure of the alignment. In addition, Atanasov et al. (2021) studied the kernel alignment of NTK, but their analysis is limited to linear neural networks.

## 5.2. Degrees Of Freedom And Label Noise

To measure the complexity of the acquired kernel, we define the (empirical) degrees of freedom by

$$d_{\lambda}(\mu)=\mbox{tr}\Big{[}\hat{\Sigma}_{\mu}(\hat{\Sigma}_{\mu}+n\lambda I)^{-1}\Big{]}$$

for $\lambda>0$. This quantity is the effective dimension of the kernel $k_{\mu}$ and plays a crucial role in the analysis of kernel regression (Caponente to & De Vito, 2007). In addition, it is known that the degrees of freedom is related to the compressibility of neural networks (Suzuki et al., 2020).

Under Assumption 4.1, each label Yi can be decom-
posed as Yi = f ◦
              i (X) + εi, where εi is the observation
noise.
      Then, taking the expectation of Uˆρ(µ) with re-
spect to ε yields Eε[Uˆρ(µ)] = B − V + const., where
B =
      ¯λa
      2T
        �T
          i=1 Eε[f ◦
                 i (X)⊤(ˆΣµ + n¯λaI)−1f ◦
                                     i (X)] and
V =
    ¯λaσ2

      6n d¯λa(µ). See Lemma D.3 for the derivation. Here,
B is the bias term, which corresponds to the alignment with
the target function as shown in the previous section, and V is
the variance term, which corresponds to the degrees of free-
dom. Since −V appears in Eε[Uˆρ(µ)], minimizing Uˆρ(µ)
leads to the larger variance and the degrees of freedom. We
verify this phenomenon in Section 6.

To obtain good prediction performance, we need to mini-
mize B+V and control the bias-variance tradeoff. Here, we
consider the following objective functional with the degrees
of freedom regularization:

$${\mathcal{L}}(\mu):={\mathcal{G}}_{\tilde{\rho}}(\mu)+\frac{\bar{\lambda}_{a}\tilde{\sigma}^{2}}{6m}d_{\bar{\lambda}_{a}}(\mu).$$

Here, ˜σ ≥ 0 controls the strength of the regularization.
Since this regularization is proportional to the variance V ,
minimizing L(µ) would lead to smaller variance and better
generalization. To obtain the minimizer of the above func-
tional L(µ), we provide the label noise procedure, where
we add independent label noise to the training data for im-
plicit regularization. In the discretized MFLD update, we
add independent label noise ˜εi ∼ υ([−˜σ, ˜σ]n) to Yi at each
time step. We use the noisy label ˜Yi := Yi + ˜εi to train
the second layer and obtain ˜a(i)
                         µ := argmin
                                       1
                                      nT
                                         �T
                                            i=1 ∥ ˜Yi−
f(X; a, µ)∥2
          2+
              ¯λa
              2 Eµ[a(w)2]. Here, the noisy limiting func-
tional G˜ε(µ) is defined as

$$G_{\tilde{\varepsilon}}(\mu):=\frac{1}{nT}\sum_{i=1}^{T}\|Y_{i}-f(X;\tilde{a}_{\mu},\mu)\|_{2}^{2}$$ $$+\frac{\bar{\lambda}_{a}}{2}\mathbb{E}_{\mu}\Big{[}\|\tilde{a}_{\mu}(w)\|_{2}^{2}\Big{]}+\frac{\bar{\lambda}_{w}}{2}\mathbb{E}_{\mu}[\|w\|_{2}^{2}].$$
Note that we use the clean label Yi to define G˜ε(µ) instead of ˜Yi. Then, we update the first layer by the following discretized MFLD.

$$w_{i}^{(k+1)}=w_{i}^{(k)}-\eta\mathbf{\nabla}\frac{\delta G_{\bar{\varepsilon}^{(k)}}(\mu w_{k})}{\delta\mu}(w_{i}^{(k)})+\sqrt{2\eta\lambda}\xi_{i}^{(k)},$$

where $\bar{\varepsilon}^{(k)}$ is an independent noise at the $k$-th iteration. In fact, the expectation of $G_{\bar{\varepsilon}}(\mu)+\lambda\operatorname{Ent}(\mu)$ with respect to $\bar{\varepsilon}$ is equal to $\mathcal{L}(\mu)$ and the above procedure can be seen as the stochastic MFLD for minimizing $\mathcal{L}(\mu)$. Indeed, the following theorem holds.

Theorem
        5.5.
            Let
                µ∗
                    =
                        argmin
                          µ
                              L(µ).
                                     Then,

_for $\eta<\min(1/4,1/(4\alpha\lambda))$ and $0\leq\tilde{\sigma}^{2}/3\leq\lambda_{\min}\Big{(}\frac{1}{T}\sum_{i=1}^{T}Y_{i}Y_{i}^{\top}\Big{)}$, we have_

$$\frac{1}{N}\mathbb{E}[\mathcal{L}^{N}(\mu_{k}^{N})]-\mathcal{L}(\mu^{*})$$ $$\leq\exp(-\alpha\lambda\eta k/2)(\mathbb{E}[\mathcal{L}^{N}(\mu_{0}^{N})]-\mathcal{L}(\mu^{*}))+\tilde{\delta}^{\prime}_{\eta,N},$$
where ¯δ′
η,N = O(η + 1
N ). Here, the expectation is taken with respect to the randomness of the label noise.

See Appendix D.3 for the proof. Intuitively, the degrees of
freedom represents a metric for quantifying the adaptability
to noise and the first layer performs the robust feature learn-
ing where the second layer is difficult to fit the label noise.
Suzuki & Suzuki (2023) has shown the Bayes optimality
of two-layer linear neural networks which minimizes the
empirical risk with the degrees of freedom regularization.
However, they ignore the optimization aspect and directly
assume that the optimal solution can be obtained. Note that
the condition on ˜σ2 is needed to ensure the convexity of the
objective and the multi-learning setting is necessary to set
˜σ > 0 since 1

          T
            �T
              i=1 YiYi
                     ⊤ must be full rank. However, as
shown in Section 6, the label noise procedure is effective
even for the single output setting.

## 6. Numerical Experiments

To validate our theoretical results, we conduct numerical
experiments with synthetic data.
                                   Specifically, we con-
sider f ◦(x) = x1x2 for d = 15.
                                      Then, the samples
�
 (x(i), y(i))
           �n
             i=1 are independently generated so that x(i)

follows N(0, I) and y(i) = f ◦(x(i)) + ε(i), where ε(i) ∼
υ([σ, σ]). We consider a finite width neural network with the
width m = 2000. We trained the network via noisy gradient
descent with η = 0.2, λ = 0.004, λw = 0.25, λa = 0.25
until T = 10000. The results are averaged over 5 different
random seeds.

First, we investigated the training dynamics of the kernel by
changing the intrinsic noise σ. As shown in Figure 1, kernel
moves to increase the kernel alignment and the degrees

of freedom. In addition, the intrinsic noise increases the degrees of freedom, which is consistent with our arguments in Section 5.2.

Next, we demonstrated the effectiveness of the label noise
procedure. Fig. 2 shows the evolution of the degrees of
freedom and the test loss during the training for different ˜σ.
As expected, the label noise procedure reduces the degrees
of freedom. Moreover, the test loss is also improved, which
implies that the degrees of freedom is a good regularization
for the generalization error.

## 7. Conclusion

In this paper, we studied the feature learning ability of two-
layer neural networks in the mean-field regime via kernel
learning formulation. For that purpose, we proposed to
use the two-timescale limit to analyze the training dynam-
ics of the mean-field neural networks. Then, we provided
the linear convergence guarantee to the global optimum by
showing the convexity of the limiting functional and derive
the discretization error. We also studied the generalization
ability of the empirical risk minimizer and proved that the
feature learning is essential to obtain good generalization
results for a union of multiple RKHSs. Then, we showed
that the kernel induced by the first layer moves to increase
kernel and parameter alignment and the intrinsic noise in
labels induces bias towards the large degrees of freedom.
Finally, we proposed the label noise procedure to reduce the
degrees of freedom and provided the global convergence
guarantee.

ST was partially supported by JST CREST (JPMJCR2015).

TS was partially supported by JSPS KAKENHI (20H00576)
and JST CREST (JPMJCR2115).

## References

Arora, S., Du, S., Hu, W., Li, Z., and Wang, R. Fine-
Grained Analysis of Optimization and Generalization for Overparameterized Two-Layer Neural Networks. In
Proceedings of the 36th International Conference on
Machine Learning, pp. 322–332. PMLR, May 2019a.
URL https://proceedings.mlr.press/v97/ arora19a.html. ISSN: 2640-3498.
Arora, S., Du, S. S., Hu, W., Li, Z., Salakhutdinov, R. R.,
and Wang, R. On Exact Computation with an Infinitely
Wide Neural Net. In Advances in Neural Information
Processing Systems, volume 32. Curran Associates,
Inc., 2019b.
URL https://papers.neurips.
cc/paper_files/paper/2019/hash/ dbc4d84bfcfe2284ba11beffb853a8c4-Abstract.
html.
Atanasov, A., Bordelon, B., and Pehlevan, C. Neural Networks as Kernel Learners: The Silent Alignment Effect.
In *International Conference on Learning Representations*, October 2021. URL https://openreview.net/ forum?id=1NvflqAdoom.
Bach, F. On the Equivalence between Kernel Quadrature
Rules and Random Feature Expansions. Journal of Machine Learning Research, 18(21):1–38, 2017. ISSN 1533-
7928.
URL http://jmlr.org/papers/v18/
15-178.html.
Bach, F. R., Lanckriet, G. R. G., and Jordan, M. I. Multiple kernel learning, conic duality, and the SMO algorithm.
In Twenty-first international conference on
Machine learning - ICML '04, pp.
6, Banff, Alberta, Canada, 2004. ACM Press.
doi:
10.1145/
1015330.1015424.
URL http://portal.acm.
org/citation.cfm?doid=1015330.1015424.
Bakry, D. and ´Emery, M. Diffusions hypercontractives.
S´eminaire de probabilit´*es de Strasbourg*, 19:177–206,
1985.
URL https://eudml.org/doc/113511.
Publisher: Springer - Lecture Notes in Mathematics.
Baratin, A., George, T., Laurent, C., Hjelm, R. D., Lajoie,
G., Vincent, P., and Lacoste-Julien, S. Implicit Regularization via Neural Feature Alignment. In Proceedings
of The 24th International Conference on Artificial Intelligence and Statistics, pp. 2269–2277. PMLR, March 2021. URL https://proceedings.mlr.press/
v130/baratin21a.html. ISSN: 2640-3498.
Barron, A.
Universal approximation bounds for superpositions of a sigmoidal function.
IEEE Transactions on Information Theory, 39(3):930–945, May
1993. ISSN 0018-9448, 1557-9654. doi: 10.1109/18.
256500. URL https://ieeexplore.ieee.org/
document/256500/.
Bartlett, P. L. and Mendelson, S. Rademacher and Gaussian Complexities: Risk Bounds and Structural Results. In Goos, G., Hartmanis, J., Van Leeuwen, J., Helmbold, D., and Williamson, B. (eds.), Computational
Learning Theory, volume 2111, pp. 224–240. Springer
Berlin Heidelberg, Berlin, Heidelberg, 2001.
ISBN
978-3-540-42343-0 978-3-540-44581-4. doi: 10.1007/ 3-540-44581-1 15. URL http://link.springer.
com/10.1007/3-540-44581-1_15. Series Title: Lecture Notes in Computer Science.
Bietti, A., Bruna, J., Sanford, C., and Song, M. J. Learning
single-index models with shallow neural networks. In
Advances in Neural Information Processing Systems, May
2022. URL https://openreview.net/forum?
id=wt7cd9m2cz2.
Bietti, A., Bruna, J., and Pillaud-Vivien, L.
On Learning Gaussian Multi-index Models with Gradient Flow, November 2023. URL http://arxiv.org/abs/
2310.19793. arXiv:2310.19793 [cs, math, stat].
Caponnetto, A. and De Vito, E.
Optimal Rates for
the Regularized Least-Squares Algorithm.
Foundations
of
Computational
Mathematics,
7(3):
331–368,
July 2007.
ISSN 1615-3375,
1615-
3383.
doi:
10.1007/s10208-006-0196-8.
URL
http://link.springer.com/10.1007/
s10208-006-0196-8.
Chen, F., Ren, Z., and Wang, S. Uniform-in-time propagation of chaos for mean field Langevin dynamics, November 2023.
URL http://arxiv.org/abs/2212.
03050. arXiv:2212.03050 [math, stat].
Chen, Z., Cao, Y., Gu, Q., and Zhang, T. A Generalized
Neural Tangent Kernel Analysis for Two-layer Neural Networks. In Advances in Neural Information Processing
Systems, volume 33, pp. 13363–13373. Curran Associates, Inc., 2020.
URL https://proceedings.
neurips.cc/paper/2020/hash/ 9afe487de556e59e6db6c862adfe25a4-Abstract.
html.
Chizat, L. Mean-Field Langevin Dynamics : Exponential Convergence and Annealing. Transactions on Machine Learning Research, May 2022.
ISSN 2835-
8856. URL https://openreview.net/forum?
id=BDqzLH1gEm.
Chizat, L. and Bach, F.
On the global convergence
of gradient descent for over-parameterized models using optimal transport.
Advances in neural information processing systems, 31, 2018.
URL https:
//proceedings-neurips-cc.utokyo.idm.
oclc.org/paper_files/paper/2018/hash/ a1afc58c6ca9540d057299ec3016d726-Abstract.
html.
Cristianini, N., Shawe-Taylor, J., Elisseeff, A., and Kandola,
J. On Kernel-Target Alignment. In Advances in Neural
Information Processing Systems, volume 14. MIT Press,
2001.
URL https://proceedings.neurips.
cc/paper_files/paper/2001/hash/
1f71e393b3809197ed66df836fe833e5-Abstract.
html.
Damian, A., Ma, T., and Lee, J. D. Label noise sgd provably
prefers flat global minimizers.
Advances in Neural
Information Processing Systems, 34:27449–27461, 2021.
URL
https://proceedings-neurips-cc.
utokyo.idm.oclc.org/paper/2021/hash/ e6af401c28c1790eaef7d55c92ab6ab6-Abstract.
html.
Damian, A., Lee, J., and Soltanolkotabi, M.
Neural Networks can Learn Representations with Gradient Descent.
In Proceedings of Thirty Fifth Conference on Learning Theory, pp. 5413–5452. PMLR, June 2022. URL https://proceedings.mlr.press/
v178/damian22a.html. ISSN: 2640-3498.
E, W., Ma, C., and Wu, L.
A priori estimates
of the population risk for two-layer neural networks.
Communications
in
Mathematical
Sciences, 17(5):1407–1425, 2019.
ISSN 15396746,
19450796.
doi:
10.4310/CMS.2019.v17.n5.a11.
URL
https://www.intlpress.com/site/
pub/pages/journals/items/cms/content/
vols/0017/0005/a011/.
Fang, C., Dong, H., and Zhang, T. Over Parameterized Twolevel Neural Networks Can Learn Near Optimal Feature Representations, October 2019. URL http://arxiv. org/abs/1910.11508. arXiv:1910.11508 [cs, math, stat].
Hayakawa, S. and Suzuki, T. On the minimax optimality and
superiority of deep neural network learning over sparse parameter spaces. *Neural Networks*, 123:343–361, March 2020. ISSN 0893-6080. doi: 10.1016/j.neunet.2019.12. 014. URL https://www.sciencedirect.com/ science/article/pii/S089360801930406X.
Holley, R. and Stroock, D. Logarithmic Sobolev inequalities and stochastic Ising models.
Journal of Statistical Physics, 46(5):1159–1194, March 1987.
ISSN
1572-9613. doi: 10.1007/BF01011161. URL https:
//doi.org/10.1007/BF01011161.

Hsu, D. Dimension lower bounds for linear approaches to
function approximation. *Daniel Hsu's homepage*, 2021.
Hu, K., Ren, Z., Siska, D., and Szpruch, L. Mean-Field
Langevin Dynamics and Energy Landscape of Neural Networks, December 2020. URL http://arxiv.org/
abs/1905.07769. arXiv:1905.07769 [math, stat].
Jacot, A., Gabriel, F., and Hongler, C. Neural Tangent
Kernel:
Convergence and Generalization in Neural
Networks.
In Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.
URL https://proceedings.neurips.
cc/paper_files/paper/2018/hash/
5a4be1fa34e62bb8a6ec6b91d2462f5a-Abstract.
html.
Li, Z., Wang, T., and Arora, S. What Happens after SGD
Reaches Zero Loss? –A Mathematical Framework. In
International Conference on Learning Representations,
October 2021. URL https://openreview.net/ forum?id=siCt4xZn5Ve.
Ma, C. and Wu, L.
The Barron space and the flowinduced function spaces for neural network models.
Constructive Approximation, 55(1):369–406, 2022. URL
https://link.springer.com/article/10.
1007/s00365-021-09549-y. Publisher: Springer.
Mahankali, A. V., HaoChen, J. Z., Dong, K., Glasgow, M.,
and Ma, T. Beyond NTK with Vanilla Gradient Descent:
A Mean-Field Analysis of Neural Networks with Polynomial Width, Samples, and Time. In Thirty-seventh
Conference on Neural Information Processing Systems,
2023. URL https://openreview-net.utokyo. idm.oclc.org/forum?id=Y2hnMZvVDm.
Marion, P. and Berthier, R. Leveraging the two timescale
regime to demonstrate convergence of neural networks, October 2023.
URL http://arxiv.org/abs/
2304.09576. arXiv:2304.09576 [cs, math, stat].
Maurer, A. A Vector-Contraction Inequality for Rademacher
Complexities. In Ortner, R., Simon, H. U., and Zilles, S. (eds.), *Algorithmic Learning Theory*, Lecture Notes in Computer Science, pp. 3–17, Cham, 2016. Springer International Publishing. ISBN 978-3-319-46379-7. doi:
10.1007/978-3-319-46379-7 1.
Mei, S., Montanari, A., and Nguyen, P.-M.
A mean
field view of the landscape of two-layer neural networks. *Proceedings of the National Academy of Sciences*,
115(33), August 2018.
ISSN 0027-8424, 1091-6490.
doi: 10.1073/pnas.1806579115. URL https://pnas.
org/doi/full/10.1073/pnas.1806579115.
Mousavi-Hosseini, A., Park, S., Girotti, M., Mitliagkas,
I., and Erdogdu, M. A.
Neural Networks Efficiently
Learn
Low-Dimensional
Representations
with SGD.
In The Eleventh International Conference on Learning Representations,
2022.
URL
https://openreview-net.utokyo.idm.
oclc.org/forum?id=6taykzqcPD.
Nitanda,
A. and Suzuki,
T.
Stochastic Particle
Gradient Descent for Infinite Ensembles,
December 2017.
URL http://arxiv.org/abs/1712.
05438. arXiv:1712.05438 [cs, math, stat].
Nitanda, A. and Suzuki, T.
Optimal Rates for Averaged Stochastic Gradient Descent under Neural
Tangent Kernel Regime.
In International Conference on Learning Representations,
2020.
URL
https://openreview-net.utokyo.idm.
oclc.org/forum?id=PULSD5qI2N1.
Nitanda, A., Wu, D., and Suzuki, T. Convex Analysis of
the Mean Field Langevin Dynamics. In Proceedings
of The 25th International Conference on Artificial Intelligence and Statistics, pp. 9741–9757. PMLR, May 2022. URL https://proceedings.mlr.press/
v151/nitanda22a.html. ISSN: 2640-3498.
Suzuki, K. and Suzuki, T. Optimal criterion for feature
learning of two-layer linear neural network in high dimensional interpolation regime. In The Twelfth International Conference on Learning Representations, October 2023. URL https://openreview.net/forum? id=Jc0FssXh2R.
Suzuki, T. Fast generalization error bound of deep learning from a kernel perspective. In Proceedings of the
Twenty-First International Conference on Artificial Intelligence and Statistics, pp. 1397–1406. PMLR, March 2018. URL https://proceedings.mlr.press/
v84/suzuki18a.html. ISSN: 2640-3498.
Suzuki, T., Abe, H., Murata, T., Horiuchi, S., Ito, K., Wachi,
T., Hirai, S., Yukishima, M., and Nishimura, T. Spectral Pruning: Compressing Deep Neural Networks via Spectral Analysis and its Generalization Error. In Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, pp. 2839–2846, Yokohama,
Japan, July 2020. International Joint Conferences on Artificial Intelligence Organization. ISBN 978-0-9992411-6- 5. doi: 10.24963/ijcai.2020/393. URL https://www. ijcai.org/proceedings/2020/393.
Suzuki, T., Nitanda, A., and Wu, D.
Uniform-intime propagation of chaos for the mean-field gradient Langevin dynamics.
In The Eleventh International
Conference on Learning Representations, September
2022. URL https://openreview.net/forum?

id=_JScUk9TBUn.

Suzuki, T., Wu, D., and Nitanda, A.
Convergence of
mean-field Langevin dynamics: time-space discretization, stochastic gradient, and variance reduction.
In
Thirty-seventh Conference on Neural Information Processing Systems, November 2023a. URL https:// openreview.net/forum?id=9STYRIVx6u.
Suzuki, T., Wu, D., Oko, K., and Nitanda, A. Feature
learning via mean-field Langevin dynamics: classifying sparse parities and beyond. In Thirty-seventh Conference on Neural Information Processing Systems, November 2023b. URL https://https://openreview. net/forum?id=tj86aGVNb3.
Vivien,
L.
P.,
Reygner,
J.,
and
Flammarion,
N.
Label
noise
(stochastic)
gradient
descent
implicitly
solves
the
Lasso
for
quadratic
parametrisation.
In Proceedings of Thirty Fifth Conference
on Learning Theory, pp. 2127–2159. PMLR, June 2022. URL https://proceedings.mlr.press/
v178/vivien22a.html. ISSN: 2640-3498.
Wainwright, M. J.
High-dimensional statistics: A nonasymptotic viewpoint, volume 48. Cambridge university press, 2019.
Yehudai, G. and Shamir, O. On the Power and Limitations of Random Features for Understanding Neural Networks.
In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019.
URL https://proceedings.neurips.
cc/paper_files/paper/2019/hash/ 5481b2f34a74e427a2818014b8e103b0-Abstract.
html.

## A. Auxiliary Lemmas

Lemma A.1 (Holley & Stroock (1987)). Assume that a probability distribution p(w) satisfies the LSI with a constant α > 0.

For a bounded perturbation B(w) : Rd′ → R*, define* p′(w) = p(w) exp(B(w))/Ep[exp(B(w))]. Then, p′ satisfies the LSI
with a constant
α
exp(4∥B∥∞).

Lemma A.2. The optimal i*-th second layer* a(i)
µ satisfies

$$a_{\mu}^{(i)}(w)=-\frac{1}{\bar{\lambda}_{a}}\mathbb{E}_{\rho}[\partial_{1}l_{i}(f_{i}(x;a_{\mu},\mu),y_{i})h(x;w)].$$
for any w ∈ Rd′.

Proof. From the optimality condition on a(i)
µ , it holds that

$$\frac{\partial L}{\partial a_{\mu}^{(i)}}(a^{(i)},\mu)(w)+\lambda\partial_{u},r(a_{\mu}(w),w)\mu(w)=\mathbb{E}[\partial_{t}l_{t}(f_{i}(x;a_{\mu}^{(i)},\mu),y_{i})h(x;w)]\mu(w)+\bar{\lambda}_{u}a_{\mu}^{(i)}(w)\mu(w)=0.$$
Thus, we have

$$a_{\mu}^{(i)}(w)=-\frac{1}{\bar{\lambda}_{a}}\mathbb{E}_{\rho}[\partial_{1}l_{i}(f_{i}(x;a_{\mu},\mu),y)h(x;w)],$$
which completes the proof.

Lemma A.3. Define T : L2(µ) → L2(ρX) by

$$T(a)=\int a(w)h(x;w)\mathrm{d}\mu(w)$$
and its adjoint operator T ∗ : L2(ρX) → L2(µ) by

$$T^{*}(f)=\int f(x)h(x;w)\mathrm{d}\rho(x).$$
For l2-loss, the optimal i*-th second layer* a(i)
µ has the following explicit formula.

$$a_{\mu}^{(i)}(w)=(T^{i}T+\bar{\lambda}_{\mu}\mathbf{I}_{\mu})^{-1}T^{i}f_{i}^{2}$$ $$=T^{*}(T^{*}+\bar{\lambda}_{\mu}\mathbf{I}_{\mu})^{-1}f_{i}^{2},$$

_where $f_{i}^{2}(x^{\prime}):=\mathbb{E}_{\mu}[y_{i}]\mid x=x^{\prime}]$ is the conditional expectation of $y$, given $x$. In addition, if $p_{X}$ is the empirical distribution, $\frac{1}{n}\sum_{j=1}^{n}\delta_{x_{j}}$, then, $a_{\mu}^{(i)}$ is written by_

$$a_{\mu}^{(i)}(w)=h(X;w)^{\top}(\bar{\lambda}_{\mu}+n\bar{\lambda}_{\mu}T)^{-1}Y_{i}.$$
Proof. For l2-loss, the optimality condition on a is given by

$$\mathbb{E}_{\rho}[(T(a_{\mu}^{(i)})-y)h(x;w)]+\bar{\lambda}_{a}a_{\mu}^{(i)}(w)=0.$$
Using Eρ[yih(x; w)] = EρX[f ◦
i (x)h(x; w)] = T ∗f ◦
i , we have

$$T^{*}T(a_{\mu}^{(i)})+\bar{\lambda}_{a}a_{\mu}^{(i)}=T^{*}f_{i}^{\circ}.$$
Since ¯λa > 0 and (T ∗T + ¯λa Id) is invertible, we arrive at

$$a_{\mu}^{(i)}=(T^{*}T+\bar{\lambda}_{a}\,\mathrm{Id})^{-1}T^{*}f_{i}^{\circ}.$$
Since (T ∗T + ¯λa Id)T ∗ = T ∗(TT ∗ + ¯λa Id), we have T ∗(TT ∗ + ¯λa Id)−1 = (T ∗T + ¯λa Id)−1T ∗, and thus a(i)
µ
=
T ∗(TT ∗ + ¯λa Id)−1f ◦
i .

Proof. Let ¯l′′
i (x′) := Eρ[∂2
1li(f(x), yi) | x = x′]. Define Λ, Λ1/2 : L2(ρ) → L2(ρ) by

$$\begin{array}{c}{{\Lambda_{i}(f)(x)=f(x)\overline{{{l}}}_{i}^{\prime\prime}(x),}}\\ {{{\Lambda_{i}^{1/2}}(f)(x)=f(x)\overline{{{l}}}_{i}^{\prime\prime}(x)^{1/2},}}\end{array}$$
and A(i)(w) ∈ L2(ρ) by

$$A^{(i)}(w)(x)=a_{\mu}^{(i)}(w)h(x;w)\bar{l}^{\prime\prime}(x)^{1/2}$$
for a given w ∈ Rd′. Note that Λ, Λ1/2.A are well-defined since ¯l′′
i (x) ≥ 0 from the convexity of li with respect to the first argument.

The second variation of U(µ) is given by

$$\frac{\delta}{\delta\mu}\frac{\delta U(\mu)}{\delta\mu}(w,w^{\prime})=-\frac{\bar{\lambda}_{a}}{T}\sum_{i=1}^{T}a_{\mu}^{(i)}(w)\frac{\delta a_{\mu}^{(i)}(w)}{\delta\mu}(w^{\prime}).$$
Taking the first variation of the both sides of the optimality condition on a(i)
µ (w) for a given w, we have

$$\mathbb{E}_{\mu}[l_{i}^{\prime\prime}(f(x;a_{\mu},\mu),y)\Bigg{(}a_{\mu}^{(i)}(w^{\prime})h(x;w^{\prime})+\int\frac{\delta a_{0}^{(i)}(w^{\prime\prime})}{\delta\mu}(w^{\prime})h(x;w^{\prime\prime})\mathrm{d}\mu(w^{\prime\prime})\Bigg{)}h(x;w)]+\tilde{\lambda}_{a}\frac{\delta a_{0}^{(i)}(w)}{\delta\mu}(w^{\prime})$$ $$=\Bigg{[}(T^{*}\Lambda_{i}T+\tilde{\lambda}_{a}\,\mathrm{Id})\frac{\delta a_{0}^{(i)}(\cdot)}{\delta\mu}(w^{\prime})\Bigg{]}(w)+\Big{[}T^{*}\Lambda_{i}^{1/2}A^{(i)}(w^{\prime})\Big{]}(w)$$ $$=0.$$
Thus, we obtain

δ δµ δU(µ) δµ = − ¯λa T i=1 a(i) µ (w)δa(i) µ (w) δµ (w′) T � = − ¯λa T i=1 a(i) µ (w)(T ∗ΛiT + ¯λa Id)−1� T ∗Λ1/2 i A(i)(w′) � (w) T � = − ¯λa T i=1 a(i) µ (w) � T ∗Λ1/2 i (Λ1/2TT ∗Λ1/2 i + ¯λa Id)−1A(i)(w′) � (w) T � = − ¯λa T i=1 a(i) µ (w) � � (Λ1/2 i TT ∗Λ1/2 i + ¯λa Id)−1A(i)(w′) � (x)h(x; w)¯l′′(x)1/2dρ(x) T � = − ¯λa T i=1 � � (Λ1/2 i TT ∗Λ1/2 i + ¯λa Id)−1A(w′) � (x)A(w)(x)dρ(x) T � = − ¯λa T i=1 ⟨A(i)(w), (Λ1/2 i TT ∗Λ1/2 i + ¯λa Id)−1A(i)(w′)⟩ T �
The second equality follows from the equality A(A∗A + Id)−1 = (AA∗ + Id)−1A for any operator A such that (A∗A +
Id), (AA∗ + Id) are invertible.

In addition, the first variations of L w.r.t. µ and a are given by

$$\partial L(a_{\mu},\mu)=\frac{1}{T}\sum_{i=1}^{T}\mathbb{E}_{\rho}[\partial_{1}l_{i}(f_{i}(x;a,\mu),y)h(x;w)]a_{\mu}^{(i)}(w),$$ $$\partial L(a_{\mu},\mu)=\frac{1}{T}\mathbb{E}_{\rho}[\partial_{1}l_{i}(f_{i}(x;a,\mu),y)h(x;w)]\mu(w),$$
respectively. Therefore, we have

$$\partial L(\frac{a_{\mu},\mu)}{\partial\mu}(w)=\sum_{i=1}^{T}\frac{a_{\mu}^{(i)}(w)}{\mu(w)}\frac{\partial L(a_{\mu},\mu)}{\partial a^{(i)}}(w).$$
The first-order optimality condition on aµ yields

$$\frac{\partial L(a_{\mu},\mu)}{\partial a^{(i)}}(w)=-\lambda\frac{\partial r(a_{\mu}(w),w)}{\partial a^{(i)}}\mu(w),\tag{4}$$
which implies

$$\partial L(a_{\mu},\mu)\over\partial\mu}(w)=-\lambda\sum_{i=1}^{T}\partial r(a_{\mu}(w),w)\over\partial a^{(i)}a_{\mu}^{(i)}(w)$$ $$=-\lambda\langle\mathbf{\nabla}_{a}r(a_{\mu}(w),w),a_{\mu}(w)\rangle.$$
Combining above arguments, we arrive at

$$\delta G(\mu)\over\delta\mu}(w)=-\lambda\langle\mathbf{\nabla}_{a}r(a_{\mu}(w),w),a_{\mu}(w)\rangle+\lambda r(a_{\mu}(w),w)\tag{5}$$ $$=\lambda\biggl{(}-{\lambda_{a}\over2T}\|a_{\mu}(w)\|_{2}^{2}+{\lambda_{w}\over2}\|w\|_{2}^{2}\biggr{)}.$$
Next, we prove the convexity of G(µ). From the convexity of L(*a, µ*) w.r.t. a, we have

$$L(a_{\mu_{1}},\mu_{1})+\int\sum_{i=1}^{T}\frac{\partial L(a_{\mu_{1}},\mu_{1})}{\partial a^{(i)}}(w)\bigg{(}\frac{\mu_{2}(w)}{\mu_{1}(w)}a_{\mu_{2}}^{(i)}(w)-a_{\mu_{1}}^{(i)}(w)\bigg{)}\mathrm{d}w\leq L\bigg{(}\frac{\mu_{2}(w)}{\mu_{1}(w)}a_{\mu_{2}},\mu_{1}\bigg{)}=L(a_{\mu_{2}},\mu_{2}),$$

for any $\mu_{1},\mu_{2}\in\mathcal{P}$. Therefore, it holds that

$$G(\mu_{1})+\int\sum_{i=1}^{T}\frac{\partial L(a_{\mu_{1}},\mu_{1})}{\partial a^{(i)}}(w)\bigg{(}\frac{\mu_{2}(w)}{\mu_{1}(w)}a_{\mu_{2}}^{(i)}(w)-a_{\mu_{1}}^{(i)}(w)\bigg{)}\mathrm{d}w$$ $$+\lambda r(a_{\mu_{1}}(w),w)\mu_{2}(w)-\lambda r(a_{\mu_{1}}(w),w)\mu_{1}(w)\mathrm{d}w$$ $$\leq G(\mu_{2}).$$
Thus, it is sufficient to show that

$$\delta\frac{G(\mu_{1})}{\delta\mu}(w)(\mu_{2}(w)-\mu_{1}(w))\leq\sum_{i=1}^{T}\,\partial L\frac{(a_{\mu_{1}},\mu_{1})}{\partial a^{(i)}}(w)\bigg{(}\frac{\mu_{2}(w)}{\mu_{1}(w)}a_{\mu}^{(i)}(w)-a_{\mu_{1}}^{(i)}(w)\bigg{)}\mathrm{d}w$$ $$+\lambda r(a_{\mu_{2}}(w),w)\mu_{2}(w)-\lambda r(a_{\mu_{1}}(w),w)\mu_{1}(w)$$
for any w. To simplify the notation, we denote the LHS by ρ1(w) and the RHS by ρ2(w). Substituting Eq. (5) to ρ1(w), we have

$\rho_{1}(w)=\lambda[-\langle\mathbf{\nabla}_{a}r(a_{\mu_{1}}(w),w),a_{\mu_{1}}(w)\rangle+r(a_{\mu_{1}}(w),w)]\left(\mu_{2}(w)-\mu_{1}(w)\right)$.

which yields

$$\|(\Sigma_{\mu_{W}}-\Sigma_{\mu^{*}})(f)\|_{L^{2}(\rho_{X})}^{2}\leq\|f\|_{L^{2}(\rho_{X})}^{2}\int(k_{\mu_{W}}(x,x^{\prime})-k_{\mu^{*}}(x,x^{\prime}))^{2}\mathrm{d}\rho_{X}(x^{\prime})\mathrm{d}\rho_{X}(x).$$
This implies ∥ΣµW − Σµ∗∥2
op ≤ Ex,x′[(kµW (x, x′) − kµ∗(*x, x*′))2] ≤ ∆/N.

Since fi(x; µ) is the optimal sofor any invertible operator *A, A*′, we have

lution of $\min_{f\in I_{N}}\mathbb{E}_{\mu}[l_{i}(f(x);y)]+\frac{\lambda}{2\mu}\|f\|_{\mu_{i}}$, where $l_{i}$ is the squared loss, $f_{i}(x;\mu)=\Sigma_{\mu}(\Sigma_{\mu}+\lambda_{\mu}\operatorname{Id})^{-1}\tilde{y}=\int k(x,x^{\prime})\alpha(x^{\prime})d\rho_{\mu}(x^{\prime})$, where $\alpha_{\mu}(x)=(\Sigma_{\mu}+\tilde{\lambda}_{\mu}\operatorname{Id})^{-1}\tilde{y}$. From the identity $A^{-1}-A^{\prime-1}=-A^{-1}(A-A^{\prime})A^{\prime-1}$ for any invertible operator $A,A^{\prime}$, we have

$$\|\alpha_{\mu\nu}-\alpha_{\mu}{}^{2}\|_{\nu_{\mu}}^{2}=\|(\Sigma_{\mu\nu}+\tilde{\lambda}_{\mu}\operatorname{Id})^{-1}(\Sigma_{\mu\nu}-\Sigma_{\mu^{\prime}})(\Sigma_{\mu^{\prime}}+\tilde{\lambda}_{\mu}\operatorname{Id})^{-1}\tilde{y}\|_{L^{1}(\rho,\kappa)}^{2}$$ $$\leq\frac{\sigma_{\mu}^{2}\|\Sigma_{\mu\nu}-\Sigma_{\mu}{}^{2}\|_{\rho_{\mu}}^{2}}{\tilde{\lambda}_{\mu}^{4}}.$$
Thus, for any x ∈ S, we have

$$(f_{t}(x;\mu_{W})-f_{t}(x;\mu^{*}))^{2}\leq2\bigg{(}\int k_{\mu^{*}_{W}}(x,x^{\prime})\alpha_{\mu_{W}}(x^{\prime})-k_{\mu^{*}}(x,x^{\prime})\alpha_{\mu_{W}}(x^{\prime})\mathrm{d}\rho_{X}(x^{\prime})\bigg{)}^{2}$$ $$+2\bigg{(}\int k_{\mu^{*}}(x,x^{\prime})\alpha_{\mu_{W}}(x^{\prime})-k_{\mu^{*}}(x,x^{\prime})\alpha_{\mu^{*}}(x^{\prime})\mathrm{d}\rho_{X}(x^{\prime})\bigg{)}^{2}$$ $$\leq2\sup_{x,x^{\prime}\in S_{N}}(k_{\mu_{W}}(x,x^{\prime})-k_{\mu^{*}}(x,x^{\prime}))^{2}\|\alpha_{\mu_{W}}\|_{L^{2}(\rho_{X})}^{2}$$ $$+2\|\alpha_{\mu_{W}-\rho_{\mu^{*}}}\|_{\rho_{X}}^{2}$$ $$\leq\frac{2c_{0}^{2}\sup_{x,x^{\prime}\in S_{N}S}(k_{\mu_{W}}(x,x^{\prime})-k_{\mu^{*}}(x,x^{\prime}))^{2}}{\lambda_{a}^{2}}+\frac{2c_{0}^{2}\|\Sigma_{\mu_{W}}-\Sigma_{\mu^{*}}\|_{\mathrm{op}}^{2}}{\lambda_{a}^{4}}.$$
By taking the supremum over x and expectation over W, we obtain the result.

## C. Proofs For Section 4 C.1. Lemmas For Section 4

Lemma C.1. For a given δ, τ > 0, we have

$$|\operatorname{tanh}(\tau z)-(1[z\geq0]-1[z<0])|\leq2e^{-2\tau|z|}$$
for any z ∈ R.

Proof.: From the definition of $\tanh$, we have, for any $z\geq0$,

$$|\tanh(\tau z)-(1[z\geq0]-1[z<0])|=1-\frac{e^{\tau z}-e^{-\tau z}}{e^{\tau z}+e^{-\tau z}}$$ $$=\frac{2e^{-\tau z}}{e^{\tau z}+e^{-\tau z}}$$ $$\leq2e^{-2\tau z}.$$
Similarly, for *z <* 0, we have

$$\tanh(\tau z)-(1[z\geq0]-1[z<0])|=1+\frac{e^{\tau z}-e^{-\tau z}}{e^{\tau z}+e^{-\tau z}}$$ $$=\frac{2e^{\tau z}}{e^{\tau z}+e^{-\tau z}}$$ $$\leq2e^{2\tau z}.$$
Combining above arguments, we obtain the result.

Lemma C.2. Let ρX be the uniform distribution on [0, 1]d and S :=
�
sin(2πw · x) | w ∈ {0, 1}d, ∥w∥1 = k
�
be a subset

of L2(ρX). Furthermore, for any fixed basis functions {hj}n
                                                             j=1 ⊂ L2(ρX), let Hn be a span of {hj}n
                                                                                                       j=1. Then, for any
ε ∈ [0, 1], we have

$$\operatorname*{sup}_{\psi\in S}d(\psi,H_{n})\geq\varepsilon$$
if n ≤ N(1 − ε), where N = *|S|* =
�d k
�
.

Proof. Assume that d(ψ, Hn) *< ε* for any ψ *∈ S*. From Theorem 1 in Hsu (2021), we have *n > N*(1 − ε) since S is an orthonormal system in L2(ρX) and *|S|* = N. This contradicts n ≤ N(1 − ε), which completes the proof.

Lemma C.3. For ε, r, rx > 0*, let* λw = 1, h(x; w) = tanh(x · u + b) (w = (u, b)). Then, for any u◦ ∈ Rd and
˜f : R → R which is 1-Lipschitz continuous and differentiable almost everywhere, there exists µ, a *such that* KL(ν | µ) =

O
 �
 r2
 ε2 + d log drrx

d.

_in $\mathbb{R}$ is a $1$-simplex; commutes with an upper measure $u$_

$$\begin{array}{l}\frac{\sigma_{u}}{\tau},\,\big{\|}a\big{\|}_{L^{2}(u)}=r\text{and}\\ \\ \left|\hat{f}\big{(}u^{\circ}\cdot x\big{)}-\left[f(x;u,\mu)+\frac{1}{2}(\hat{f}(r)+\hat{f}(-r))\right]\right|\leq\varepsilon\end{array}$$

_for any $x\in\mathbb{R}^{d}$ such that $|u^{\circ}\cdot x|\leq r$ and $\|x\|\leq r\sqrt{d}$._

Proof.: Let $a(u,b)=r\hat{a}(b/r)$ for $\hat{a}(b):\mathbb{R}\to\mathbb{R},\|\hat{a}\|_{\leq}\leq1$ and $\mu(u)=\mu(u,b):=\mu(u)\mu(b)$, where $\mu(u)=N(ru^{\circ},a^{\circ}I),\mu(b)=v([-\tau r,\tau r])$ for $\tau,\sigma>0$. In addition, let $\bar{g}(x)=\mathbb{E}_{b,\mu_{0}}[r\hat{a}(b/r)\tanh(\tau\cdot u^{\circ}+b)]$. Then, we have

$$|g(x)-f(x;a,\mu)|\leq\int|v\hat{a}(b/r)\|\tanh(x\cdot u+b)-\tanh(\tau x\cdot u^{\circ}+b)|d\mu(\bar{u},b)$$ $$\leq\int|v\hat{b}(\sqrt{\|x\|}\,\|x-u\cdot\tau u^{\circ})|d\mu(u)$$ $$\leq r\sqrt{\int\|v\|^{2}(u-\tau u^{\circ})\|^{2}d\mu(u)}$$ $$\leq r\sqrt{\int\|x\|^{2}\|u-\tau u^{\circ}\|^{2}d\mu(u)}$$ \[\leq r\,r_{x}\sqrt{d}\omega.\
it holds that

$$|\tilde{g}(x)-\tilde{g}(x)|\leq\int_{-\tau}^{\tau}\frac{1}{2}|\tilde{a}(b)||\tanh(\tau(x\cdot u^{\circ}+b^{\prime}))-(1[x\cdot u^{\circ}+b^{\prime}\geq0]-1[x\cdot u^{\circ}+b^{\prime}<0])|\mathrm{d}b^{\prime}$$ $$\leq\int_{-\infty}^{\infty}\frac{1}{2}[\tanh(\tau(x\cdot u^{\circ}+b^{\prime}))-(1[x\cdot u^{\circ}+b^{\prime}\geq0]-1[x\cdot u^{\circ}+b^{\prime}<0])|\mathrm{d}b^{\prime}$$ $$\leq\int_{0}^{\infty}e^{-2\tau z}\mathrm{d}z$$ $$=1/(2\tau)$$
For any f =
�
a(w)h(x; w)dµ(w) *∈ F*2R,2M, we have

∥f∥∞ ≤ � |a(w)|dµ(w) ≤ ∥a∥L2(µ) 2R. ≤ √
Thus, for any f
∈
F2R,2M, l(f(x), y)
=
l(f(x), f ◦(x))
≤
4R and |l′(f(x), y)|
≤
2
√
2R.

Let F′
=
{(x, y) �→ l(f(x), y) | f *∈ F*2R,2M}. Utilizing the standard uniform bound (Wainwright, 2019), for any δ ∈ [0, 1], we have

log 2/δ n 2n , ≤ 2R(F′) + 12R Eρ[g(*x, y*)] − 1 � �
�

$$\operatorname*{sup}_{g\in\mathcal{F}^{\prime}}\qquad\qquad\qquad\sum_{i=1}^{n}g(x^{(i)},y^{(i)})$$
2016), we have

with probability at least 1−δ over the choice of n i.i.d. samples
                                                                    �
                                                                     (x(i), y(i))
                                                                                 �n
                                                                                  i=1 ∼ ρ. From the contraction lemma (Maurer,

R(F′) = Eσ � � i=1 σil(f(xi), yi) sup f∈F2R,2M n � ≤ 2 √ 2RR(F2R,2M) (M + 1) = O R , n � � �
2R,
√
2R]. Combining above arguments, we arrive at since l(·, yi) is 2
√
2R-Lipschitz continuous in [−
√

$$\bar{L}(a_{\hat{\mu}},\mu)\leq L(a_{\hat{\mu}},\hat{\mu})+2\Re(\mathcal{F}^{\prime})+12R\sqrt{\log2/\delta}$$ $$=O\Bigg{(}\sqrt{\frac{M}{n}}+R\sqrt{(\frac{M+1}{n})}+R\sqrt{\log1/\delta}\Bigg{)}$$ $$=O\Bigg{(}(R+1)\Bigg{(}\sqrt{(\frac{M+1}{n})}+\sqrt{\log1/\delta}\Bigg{)}\Bigg{)}$$ $$=O\Bigg{(}(R+1)\sqrt{(M+1)}+\log1/\delta\Bigg{)},$$
since we set λ = 1/√n. This completes the proof.

## C.4. Proof Of Theorem 4.5

Let S :=
�
sin(2πu · x) | u ∈ {0, 1}d, ∥u∥1 = k
�
be a subset of L2(ρX). Note that S is an orthonormal system in L2(ρX).

Assume that

$$\operatorname*{sup}_{f\in{\mathcal{B}}_{M},\|f\|_{{\mathcal{B}}_{M}}^{2}\leq R}d(f,H_{n})<1/4.$$
Then, from Lemma C.3, for any ψ = sin(2πu · x) *∈ S* (∥u∥1 = k), there exists *a, µ* such that KL(ν | µ) = O(d log dk +
k2), ∥a∥L2(µ) = k, and
|ψ(x) − f(x)| ≤ 1/4
for any x ∈ [0, 1]d since |u · x*| ≤ ∥*u∥1∥x∥∞ ≤ k and sin(2πk) = sin(−2πk) = 0. Therefore, we have

$d(\psi,H_{n})\leq\|\psi-f\|_{L^{2}(\rho_{X})}+d(f,H_{n})$

$\leq1/4+1/4=1/2$.

This contradicts Lemma C.2. Thus, we obtain the result.

by setting ε to a sufficiently small constant and *r, r*x sufficiently large constants which are independent of d. Thus, there exists M = O(d log d), R = O(1) such that ∥f ◦ − f∥2
L2(ρX), where f ∈ FR,M. By the same argument in the proof of Theorem 4.4, we have

(M + 1) + log 1/δ R n Lˆρ(a, µ) ≤ Lρ(*a, µ*) + O � � �

with probability at least 1 − δ over the choice of training data. Thus, by setting n ≥ c′
                                                                                          3(d log d + log 1/δ) for sufficiently
large c′
       3, we have

$$L_{\hat{\rho}}(a,\mu)\leq L_{\rho}(a,\mu)+\varepsilon^{2}\leq2\varepsilon^{2}$$
From the optimality of ˆµ and ˆa = aˆµ, we have

$$\begin{split}\mathcal{G}_{\hat{\rho}}(\hat{\mu})&=L(\hat{a},\hat{\mu})+\frac{\bar{\lambda}_{a}}{2}\|\hat{a}\|_{L^{2}(\hat{\mu})}^{2}+\lambda\operatorname{KL}(\nu\mid\hat{\mu})\\ &\leq\mathcal{G}(a,\mu)\\ &\leq2\bar{\varepsilon}^{2}+2\lambda M\\ &\leq3\bar{\varepsilon}^{2},\end{split}$$
by setting λ = ¯ϵ2/2M and λa = *M/R*. Thus, it holds that

$$\begin{array}{c}{{\|\hat{a}\|_{L^{2}(\hat{\mu})}^{2}\leq12R,}}\\ {{\mathrm{KL}(\nu\mid\hat{\mu})\leq6M.}}\end{array}$$
Then, by the same reasoning as in the proof of Theorem 4.4, we have

$$U_{\rho}(\hat{\mu})\leq E_{\rho}[l(f(x;\hat{\mu}),y)]+\frac{\bar{\lambda}_{a}}{2}\left\|a_{\hat{\mu}}\right\|_{L^{2}(\mu)}^{2}$$ $$\leq E_{\hat{\mu}}[l(f(x;\hat{\mu}),y)]+\frac{\bar{\lambda}_{a}}{2}\left\|a_{\hat{\mu}}\right\|_{L^{2}(\mu)}^{2}+O\!\left((R+1)\sqrt{M+1+\log1/\delta}\right)$$ $$\leq\mathcal{G}_{\hat{\rho}}(\hat{\mu})+O\!\left((R+1)\sqrt{M+1+\log1/\delta}\right)$$ $$\leq3\bar{\varepsilon}^{2}+O\!\left((R+1)\sqrt{M+1+\log1/\delta}\right)$$ $$\leq4\bar{\varepsilon}^{2}$$
by setting n = c3(d log d + log 1/δ) for a sufficiently large constant c3 ≥ c′
3 with probability at least 1 − δ over the choice of training data. Therefore, it holds that

$$\begin{split}A(\hat{\mu})&\geq A'(\hat{\mu})\geq\frac{\bar{\lambda}_a}{2U(\hat{\mu})}-\bar{\lambda}_a\\ &\geq\frac{\bar{\varepsilon}^2/(2R)}{8\bar{\varepsilon}^2}-\bar{\varepsilon}^2/2R\\ &\geq\frac{1-8\bar{\epsilon}^2}{16R}\\ &=\Omega(1).\end{split}$$
∥w∥2
2 dµ0(w) is equal Let {ui}d i=1 (u1 = u) be an orthonormal basis of Rd. Then, the symmetry of µ0 = ν implies that
� ⟨ui,w⟩2
∥w∥2
2 dµ0(w) = 1/d. In addition let fi(x) = ˜f(ui · x). Then, we
∥w∥2
2 dµ0(w) = 1, we have
� ⟨u,w⟩2
for any i. Since �d i=1
� ⟨ui,w⟩2

•
•
���∇ δU˜ε
δµ (µ)(w)
��� ≤ RUV ,

���∇w
δU˜ε
δµ (µ)(w)
���
2 ≤ RUV ,
•
δµ2 (µ)(*w, w*′)
���
op ≤ LUV .
���∇w∇⊤
w
δU˜ε
δµ (µ)(w)
���
op ≤ LUV ,
���∇w∇⊤
w′ δ2U˜ε
since U˜ε(µ) = U(µ) − V (µ) + const. Combining above arguments, Theorem 3 in Suzuki et al. (2023a) yields
λα
¯L2C1(λη + η2) +
4
λαη
¯Υ + 2Cλ
λαN ,

1
N E[LN(µ(N)
        k
           )] − L(µ∗) ≤ exp(−λαηk)
                                 � 1

N E[LN(µ(N)
     k
       )] − L(µ∗)
            �
             + 2

�
 +
    1
   ¯λw

��
  1
  4 +
      1
     ¯λw

�
 R2
  UV + λd′�
         , ¯L = LUV + ¯λw, C1 = 8[R2
                            UV + ¯λw ¯R2 + d′], Cλ = 2λLUV α +

2λ2L2
    UV ¯R2, and

where ¯R2 = E
            ����w(0)
               i
                  ���
                   2

λ/η)η3R2
       UV .

¯Υ := 4ηδη + [RUV + λw ¯R + (LUV + ¯λw)2](1 +
                                                 �

λ/η)η2R2
       UV + (RUV + ¯λw ¯R)RUV (1 +
                               �

This completes the proof.

