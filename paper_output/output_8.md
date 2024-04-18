# Model Order Reduction Of Deep Structured State-Space Models: A System-Theoretic Approach

Marco Forgione, Manas Mejari, and Dario Piga IDSIA Dalle Molle Institute for Artificial Intelligence USI-SUPSI, Via la Santa 1, CH-6962 Lugano-Viganello, Switzerland.

March 25, 2024

## Abstract

With a specific emphasis on control design objectives, achieving accurate system modeling with limited complexity is crucial in parametric system identification. The recently introduced deep structured state-space models (SSM), which feature linear dynamical blocks as key constituent components, offer high predictive performance. However, the learned representations often suffer from excessively large model orders, which render them unsuitable for control design purposes. The current paper addresses this challenge by means of system-theoretic model order reduction techniques that target the linear dynamical blocks of SSMs. We introduce two regularization terms which can be incorporated into the training loss for improved model order reduction. In particular, we consider modal ℓ1 and Hankel nuclear norm regularization to promote sparsity, allowing one to retain only the relevant states without sacrificing accuracy. The presented regularizers lead to advantages in terms of parsimonious representations and faster inference resulting from the reduced order models. The effectiveness of the proposed methodology is demonstrated using real-world ground vibration data from an aircraft.

## 1 Introduction

In recent years, deep structured state-space models (SSM) have emerged as powerful and flexible architectures to tackle machine-learning tasks over sequential data such as time series classification, regression, and forecasting [11, 12, 17, 24]. Notably, they exhibit state-of-the-art performance in problems defined over very long sequences, where Transformers struggle due to their computational complexity that grows quadratically with the sequence length [25].

Essentially, SSMs consist in the sequential connection of linear dynamical blocks interleaved with static non-linearities and normalization units, organized in identical repeated layers with skip connections (see Fig. 1). In this sense, they are closely related to the block-oriented modeling framework [23] traditionally employed by the system identification community, and made compatible for training in a deep-learning setting thanks to the *dynoNet* architecture proposed by some of the authors in [8].

Several mathematical and software implementation solutions have been devised to make learning of SSM architectures–in particular of their key constituent linear dynamical block–fast, well-posed, and efficient. For instance, S4 [12] adopts a continuous-time parameterization, an initialization strategy based on continuous-time memorization theory, and a convolution-based implementation in frequency domain based on fast Fourier transform. Conversely, the deep Linear Recurrent Unit architecture [17] adopts a discrete-time parameterization with a diagonal state-transition matrix, an initialization strategy that constrains the eigenvalues of the system in a region of stability, and an efficient implementation in time domain exploiting the parallel scan algorithm [4].

From the Systems and Control perspective, *parsimonious* representations are often sought, *i.e.*, it is desired to obtain a model that describes system's behaviour with as few parameters and states as possible, to simplify downstream tasks such as controller synthesis, state estimation, etc.

The inadequacy of high-dimensional models has driven growing interest in Model Order Reduction (MOR) techniques.

In particular, several contributions focus on reducing the number of states of linear dynamical systems, employing methods that can be broadly categorized into SVD-based and Krylov approximation-based techniques [2].

The former rely on the concept of the Hankel singular values, which characterize the complexity of the reduced-order model and provide an error bound of the approximation [9]. These methods include balanced truncation [1, 15], singular perturbation approximation [14] and Hankel norm approximation [18]. On the other hand, Krylov-based approximation methods are iterative in nature. They are based on *moment matching* of the impulse response rather than computation of singular values, see the recent survey paper [21] for an overview of these approaches.

In this paper, we demonstrate the effective adaptation of these MOR techniques, initially designed for linear dynamical systems, to the task of learning simplified deep SSMs architectures while maintaining their predictive capabilities. In principle, an SSM could first be learned using standard machine-learning algorithms, and then each of the constituent linear dynamical blocks could be reduced employing one of the MOR techniques mentioned above. However, we show that the effectiveness of MOR is significantly increased when the low-order modeling objective is already integrated in the training procedure, by means of a *regularization term* in the loss function which promotes parsimonious representations. In particular, we adopt modal ℓ1 and Hankel nuclear norm regularization approaches that penalize the magnitude of the linear units' eigenvalues and Hankel singular values, respectively. We illustrate our methodology on a well-known system identification benchmark [16] where the aim is to model the oscillations of an aircraft subject to a ground vibration test.

We show that specific combinations of regularizers applied during training, along with MOR techniques applied after training, yield the best results.

All our codes are available in the GitHub repository https://github.com/
forgi86/lru-reduction, allowing full reproducibility of the reported results.

## 2 Problem Setting

We consider a training dataset consisting of a sequence of input-output samples D = {uk, yk}N
k=1, generated from an unknown dynamical system S, where uk ∈
Rnu is the input and yk ∈ Rny is the measured output at time step k. The problem considered in this work is to learn a parametric simulation model M(θ)
with parameters θ ∈ Θ, mapping an input sequence u1:k to the (estimated)
output sequence ˆy1:k, which fits the training dataset D. In particular, the focus is to identify a *parsimonious* model with as few states (in turn, parameters) as possible via regularization and model order reduction techniques.

The parameters θ characterising the model M(θ) are estimated according to the criterion:

$$\hat{\theta}=\arg\min_{\theta\in\Theta}\frac{1}{N}\sum_{k=1}^{N}\mathcal{L}\left(y_{k},\hat{y}_{k}(\theta)\right)+\gamma\mathcal{R}(\theta),\tag{1}$$
where ˆyk(θ) represents the model's output at time k, and L(·) denotes the chosen fitting loss function. The term R(θ) is a regularization cost which aims at enforcing sparsity and reducing the complexity of the model, ultimately facilitating the subsequent MOR step. Different choices for the regularization loss R(θ) will be introduced in the Section 4.2.

In this work, M(θ) is a SSM architecture recently introduced in [17] and known as deep Linear Recurrent Unit.

In the next section, we describe in details the building blocks and parameterizations of this architecture.

## 3 Deep Structured State-Space Model

The deep Linear Recurrent Unit architecture is visualized in Fig. 1. Its core
(shown in gray) is a stack of nlayers Linear Recurrent Units (LRU), which are linear dynamical systems, interleaved with static non-linearities, (*e.g.*, Multi Layer Perceptrons (MLP) or Gated Linear Units (GLU) [5]) and normalization units (typically Layer or Batch Normalization [27]), with *skip connections* included in each repeated layer. In particular, the l-th layer of the network with inputs ul k and output sl k is defined by:

$$\mathcal{M}^{i}:\begin{cases}\tilde{u}_{k}^{i}=\text{Norm}(u_{k}^{i}),\\ y_{k}^{i}=\text{LRU}(\tilde{u}_{1:k}^{i},\theta^{i}),\\ s_{k}^{i}=u_{k}^{i}+f(y_{k}^{i}),\end{cases}\tag{2}$$

where $\text{Norm}(\cdot)$ is the normalization unit; the LRU is a linear time-invariant (LTI) multi-input multi-output (MIMO) dynamical block whose exact structure 
is described in the next sub-section; and f(·) : Rdmodel → Rdmodel is the static non-linearity, applied in an element-wise fashion to all samples of the LRU output sequence. The first and last transformations in the architecture (pink blocks) are static linear projections mapping the input samples uk ∈ Rnu to Uk ∈ Rdmodel, and Yk ∈ Rdmodel to predicted outputs ˆyk ∈ Rny, respectively.

We remark that deep LRU shares a close proximity to the *dynoNet* architecture proposed in [8]. The main difference is that the LRU is a state-space representation of an LTI system, while *dynoNet* employs input-output transfer function descriptions. The architecture is also related to (decoder-only) Transformers [19], with information shared across time steps with an LTI system instead of a causal attention layer.

In the following subsection, we summarize the details of the LRU block. We omit the layer index l when referencing parameters and signals to simplify the notation. Furthermore, we redefine uk/yk as the input/output samples of the LRU to match the standard notation of linear system theory.

## Linear Recurrent Unit

The LRU is a linear, discrete-time, MIMO dynamical system described in statespace form as:

$x_{k}=A_{D}\ x_{k-1}+Bu_{k}$, (3a) $y_{k}=\Re[Cx_{k}]+Du_{k}$, (3b)
where ℜ[·] denotes the real part of its argument, AD ∈ Cnx×nx, B ∈ Cnx×nu and C ∈ Cny×nx are complex-valued matrices, and D ∈ Rny×nu is a real-valued matrix. The matrix AD has a diagonal structure:

$A_{D}=\mbox{diag}(\lambda_{1},\ldots,\lambda_{n_{x}})$, (4)
where λj, j = 1*, . . . , n*x are the complex eigenvalues, or modes, of the system, which is thus represented in a *modal* form. In order to guarantee asymptotic stability of the system, *i.e*, to enforce |λj| < 1, j = 1*, . . . , n*x, each eigenvalue
λj ∈ C is, in turn, parameterized as λj = exp(− exp(νj)+i exp(ϕj)), where νj >
0. Note that since exp(νj) > 0 for νj > 0, this ensures |λj| = exp(− exp(νj)) <
1.

The input matrix B is parameterized as B = diag(γ1*, . . . , γ*nx) ˜B, where
γj =
�
1 − |λj|2, j = 1*, . . . , n*x, is a normalization factor introduced to obtain state signals with the same power as that of the input signal.

Overall, the learnable parameters of a single LRU block are θ := {{νj, ϕj}nx j=1, ˜*B, C, D*}.

Remark 1 *System* (3) has an equivalent complex-conjugate representation:

$$\tilde{x}_{k}=\begin{bmatrix}A_{D}&0\\ 0&A_{D}^{*}\end{bmatrix}\ \tilde{x}_{k-1}+\begin{bmatrix}B\\ B^{*}\end{bmatrix}u_{k},\tag{5a}$$ $$y_{k}=\frac{1}{2}\begin{bmatrix}C&C^{*}\end{bmatrix}\tilde{x}_{k}+Du_{k},\tag{5b}$$

_with $\tilde{x}_{k}\in\mathbb{C}^{2n_{x}}$, which in turn may be transformed in a real Jordan form, with a block-diagonal state-transition matrix containing $n_{x}$ 2x2 blocks, see e.g. Appendix E.3 of [17]. The complex-valued, diagonal representation (3) is preferred for its implementation simplicity and halved state dimension._

## 4 Model Order Reduction And Regularization

In this section, we provide a brief review of the MOR techniques used in this paper. Next, we introduce regularization techniques aimed at promoting the learning of parsimonious LRU representations in terms of state complexity.

## 4.1 Reduction By Truncation And Singular Perturbation

Order reduction techniques based on truncation decrease the dimensionality of a dynamical system by eliminating states that, for various reasons, are considered less important [10]. Consider a state-space model $G$ with realization:

$$\begin{bmatrix}x_{1,k}\\ x_{2,k}\end{bmatrix}=\begin{bmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{bmatrix}\begin{bmatrix}x_{1,k-1}\\ x_{2,k-1}\end{bmatrix}+\begin{bmatrix}B_{1}\\ B_{2}\end{bmatrix}u_{k},\tag{6a}$$ $$y_{k}=\begin{bmatrix}C_{1}&C_{2}\end{bmatrix}\begin{bmatrix}x_{1,k}\\ x_{2,k}\end{bmatrix}+Du_{k},\tag{6b}$$
where the partitioning corresponds to important states to be kept x1 ∈ Rr and unimportant states to be removed x2 ∈ Rnx−r, respectively. The state-space truncation method approximates (6) with a reduced-order system Gr having state-space matrices:

$A_{r}=A_{11},B_{r}=B_{1},C_{r}=C_{1},D_{r}=D$.

Note that state-space truncation does not preserve the steady-state behavior of G and, in general, it may alter its low-frequency response significantly. Alternatively, the removed states x2 may be set to equilibrium by solving for x2,k = x2,k−1 in (6a). This results in the so-called *singular perturbation* approximation, where the reduced-order system Gr is defined by the following state-space matrices:

$$A_{r}=A_{11}+A_{12}(I-A_{22})^{-1}A_{21}$$ (8a) $$B_{r}=B_{1}+A_{12}(I-A_{22})^{-1}B_{2}$$ (8b) $$C_{r}=C_{1}+C_{2}(I-A_{22})^{-1}A_{21}$$ (8c) $$D_{r}=C_{2}(I-A_{22})^{-1}B_{2}+D.$$ (8d)

Singular perturbation preserves the steady-state behavior of (6), and generally provides a better match in the lower frequency range with respect to plain state-space truncation.

In the control literature, state-space truncation and singular perturbation approximations are typically applied to systems described either in modal or imbalanced realization form [10]. The resulting MOR techniques will be denoted here as modal truncation (MT), nodal singular perturbation (MSP), balanced truncation (BT), and bold and angular perturbation (MSP), in the local methods, the states are located according to non-increasing magnitude of the model methods, the eigenstates, so that the fastest dynamics can be guided. This choice is often motivated by physical arguments, when the fast dynamics is are associated to uninteresting second-order effects (e.g., electrical dynamics in mechanical systems). In balanced methods, the states are sorted for non-increasing value of the corresponding Hankel singular values. This choice is supported by the following approximation bound, which holds both for BT and BSP:

$$\|G-G_{r}\|_{\infty}\leq2\sum_{j=r+1}^{n_{r}}\sigma_{j},\tag{9}$$
where *∥·∥*∞ denotes the H∞ norm and σj, j = r + 1*, . . . , n*x are the Hankel singular values corresponding to the eliminated states, see [13, Lemma 3.7].

For the LRU, MT/MSP are directly applicable, being the block already represented in a modal form. Conversely, BT/BSP require a three-step procedure where (i) system (3) is first transformed to a (non-diagonal) balanced form, then (ii) reduced according to either (7) or (8), and finally (iii) re-diagonalized with a state transformation obtained from the eigenvalue decomposition of the state matrix of the system obtained at step (ii) to fit the LRU famework.

## 4.2 Regularized Linear Recurrent Units

In this section, we introduce two regularization approaches that promote learning of LRUs with a reduced state complexity. These methods leverage systemtheoretic MOR methods described in the previous sub-section and exploit the diagonal structure of the LRU's state-transition matrix AD.

## 4.2.1 Modal ℓ1-Regularization

As mentioned in Section 4.1, high-frequency modes often correspond to secondary phenomena that may be eliminated without compromising the salient aspects of the modeled dynamics. For discrete-time LTI systems, fast dynamics are associated to eigenvalues whose modulus |λj| is small. An ℓ1-regularization is therefore introduced to push some of the modes towards zero during training:

$${\cal R}(\theta)=\sum_{l=1}^{n_{\rm layers}}\sum_{j=1}^{n_{x}}|\lambda_{j}^{l}|.\tag{10}$$
Indeed, ℓ1-regularization is known to promote sparsity in the solution [26]. The states corresponding to eigenvalues that are closer to zero will then be eliminated with a MOR method at a second stage after training. Note that modal
ℓ1-regularization of the LRU is computationally cheap, as the eigenvalues are directly available on the diagonal of the state-transition matrix AD.

## 4.2.2 Hankel Nuclear Norm Regularization

It is known that the McMillan degree (minimum realization order) of a discretetime LTI system coincides with the rank of its associated (infinte-dimensional)
Hankel operator H [13]. The (*i, j*)-th block of H is defined as Hij = gi+j−1, where gk = CAk−1
D
B is the impulse response coefficient at time step k. Minimizing the rank of the Hankel operator thus aligns with the objective of obtaining a low-order representation. However, the rank minimization problem is hard to solve and the *nuclear norm* of the Hankel operator ∥H(g)∥∗ := �
j σj, defined as the sum of its singular values σj, is often used as a *convex surrogate* of the rank [6, 18].

Following this rationale, we employ the Hankel nuclear norm of the LRUs as a regularization term in training:

$${\cal R}(\theta)=\sum_{l=1}^{n_{\rm layers}}\sum_{j=1}^{n_{x}}\sigma_{j}^{l},\tag{11}$$
eigj(PQ), where P and Q are the controllability and observability Grammians of the LTI model [13]. In appendix A.1, we show how the where σl j denotes the j-th singular value of the Hankel operator of the LRU in the l-th layer. Note that, as σl j ≥ 0, j = 1*, . . . , n*x, the term �nx j=1 σl j in (11) is the ℓ1-norm of the Hankel singular values, thus, promoting sparsity.

It can be proved that the j-th singular value of the Hankel operator is given by σj(H) =
�
Grammians P and Q, and in turn the Hankel singular values can be computed efficiently for systems in modal form.

Remark 2 (ℓ2-regularization) If the ℓ2-norm of the Hankel singular values
is considered in (11) instead of the ℓ1-norm, the computational burden during
training can be further reduced exploiting the identity �nx
                                         j=1 σ2
                                            j = �nx
                                                 j=1 eigj(PQ) =
trace(PQ).
          Thus, differentiation of the eigenvalues of PQ is not required.
Nonetheless, it is known that ℓ2-norm regularization does not enforce sparsity
in the solution, contrary to the ℓ1 case.

Remark 3 (H∞-error bound) The use of the regularizer (11) is further mo-
tivated by the H∞ error bound (9).
                             This suggests to combine Hankel-norm
regularization during training with MOR based on either BT or BSP.

## 5 Case Study

We test the methodologies of the paper on the ground vibration dataset of an F-16 aircraft introduced in [16].

The input u ∈ R (N) is the force generated by a shaker mounted on the aircraft's right wing, while the outputs y ∈ R3 (m/s2) are the accelerations measured at three test locations on the aircraft. Input and output samples are collected at a constant frequency of 400 Hz. We train deep LRU models with structure as shown in Fig. 1 characterized by: Layer Normalization; MLP nonlinearity; dmodel = 50; nx = 100; and nlayers = 6. The MLP has one hidden layer with 400 hidden units and Gaussian Error Linear Unit (GELU) non-linearities.

Training is repeated three times with identical settings except for the regularization strategy, which is set to: (i) no regularization, (ii) modal ℓ1-regularization, and (iii) Hankel nuclear norm regularization. For both (ii) and (iii), the regularization strength is set to γ = 10−2. We train the models on all the input/output sequences suggested for training in [16] except the one denoted as "Special Odds". To take advantage of parallel computations on more sequences, we split the datasets in (partially overlapping) sub-sequences of length N = 5000 samples each and compute the training loss (1) over batches of 64 sub-sequences simultaneously. In the definition of the loss, the first 200 samples of each subsequence are discarded to cope with the state initialization issue, according to the ZERO initialization scheme described in [7]. We minimize the mean squared error training loss over 10 epochs of AdamW with constant learning rate 10−4, where at each epoch all the 688820 sub-sequences of length N in the training data are processed.

We report the *fit* index [22], the Root Mean Squared Error (RMSE), and the Normalized Root Mean Squared Error (NRMSE) on the three output channels in Table 1. For brevity, we exclusively report the results obtained on the test dataset denoted as "FullMSine Level6 Validation". The three trained models achieve similar performance, which is also in line with existing state-of-the-art. For instance, the average NRMSE over the three channels is about 0.15, which

Regularization
Channel 1
Channel 2
Channel 3
fit
RMSE
NRMSE
fit
RMSE
NRMSE
fit
RMSE
NRMSE
No reg.
86.5
0.180
0.134
90.0
0.167
0.099
76.2
0.368
0.237
Modal ℓ1
85.4
0.195
0.145
89.8
0.171
0.102
74.5
0.395
0.254
Hankel norm
85.8
0.190
0.142
89.0
0.185
0.110
75.5
0.379
0.245

is close to the result reported in [20]. However, we observe that regularization has a strong effect on the properties of the estimated LTI blocks.

The plots in the six columns of Fig. 2, 3 and 4 illustrate this effect, where each column corresponds to LRU in one of the 6 layers. For the model without regularization (Fig. 2), most of the eigenvalues have non-zero magnitude (top panel).

In this sense, the modal reduction methods MT/MSP are not expected to be effective. The Hankel singular values decrease slightly faster towards zero, suggesting that the effectiveness of the balanced reduction methods BT/BSP might be marginally superior. As for the model obtained with modal
ℓ1-regularization (Fig. 3), several eigenvalues have been pushed towards zero
(top panel), suggesting the potential effectiveness of modal reduction methods. Finally, for the model trained with Hankel nucelar norm regularization (Fig. 4), the Hankel singular values decrease very sharply towards zero (bottom panel), while none of the eigenvalues' magnitude is pushed towards zero.

Thus, we expect balanced reduction methods to be effective in this case.

In Table 2, we report the maximum number of eliminated states with the different MOR techniques applied to the three trained models, such that the performance degradation in test (in terms of *fit* index) averaged over the three output channels is less than 1%. The best results are obtained for the combinations of modal ℓ1-regularization followed by MSP and Hankel nuclear norm regularization followed by BSP, which both lead to 91 eliminated states. We also observe that, when regularization is not applied in training, the subsequent MOR is decisively less effective. Fig. 5 further highlights this key experimental results: when training with no regularization, the best reduction approach (BSP) is significantly less effective than the optimal regularizer+MOR combinations: modal ℓ1+MSP and Hankel nuclear norm+BSP.

Truncation Method
Regularization Method
BT
BSP
MT
MSP
No Regularization
28
43
3
35
Modal ℓ1
56
73
0
91
Hankel nuclear norm
89
91
18
76

## 6 Conclusions

We have presented regularization methods and model order reduction approaches that enable substantial simplification of deep structured state-space models. Our experimental results suggest that regularization is a fundamental ingredient of our procedure. Indeed, model order reduction executed as a mere post-hoc step, after a standard training conducted without regularization appears to be significantly less effective. In future works, we will analyze in more depth the effect of the regularization strength γ through more extensive numerical experiments and possibly with analytical tools. Moreover, we aim at decreasing the number of internal input/output channels dmodel and of layers nlayers of the architecture. A possible approach is based on group LASSO regularization, following an approach similar to the one recently introduced in [3] for more classical neural state-space models. Finally, we will extend our techniques to other architectures that feature linear dynamical blocks at their core, such as dynoNet and deep Koopman representations.

## A Appendix A.1 Computation Of Hankel Singular Values

The Hankel singular values of a discrete-time LTI system with complex-valued matrices $(A,B,C,D)$ are given by:

$$\sigma_{j}=\sqrt{\mathfrak{a}\mathfrak{i}\mathfrak{g}_{j}(PQ)},\ \ \forall j\in1,\ldots,n_{x},\tag{12}$$

where $P\in\mathbb{C}^{n_{x}\times n_{x}}$ and $Q\in\mathbb{C}^{n_{x}\times n_{x}}$ are the controllability and observability Gramians, respectively, which are the solutions of the discrete Lyapunov equations [13]:

$$APA^{*}-P+BB^{*}=0\tag{13}$$ $$A^{*}QA-Q+C^{*}C=0,\tag{14}$$

## A.2 Solution To A Diagonal Discrete Lyapunov Equation

We show that discrete Lyapunov equations can be solved efficiently for systems in modal representation where matrix A is diagonal. The direct method to solve the Lyapunov equation with variable X:

$$AXA^{*}-X+Y=0\tag{15}$$
is obtained by exploiting the product property:

$${\rm vec}(AXB)=(B^{\top}\otimes A){\rm vec}(X),\tag{16}$$
where ⊗ is the Kronecker product operator and vec(·) represents the columnwise vectorization operation. Applying this formula to (15), one obtains:

$(I-A^{*}\otimes A){\rm vec}(X)={\rm vec}(Y)$, (17)
which is a linear system in the unknowns vec(X). If A is diagonal, the left-hand side matrix of (17) is also diagonal, and thus its solution is simply obtained through n2
x scalar divisions.

## References

[1] U.M. Al-Saggaf and G. F. Franklin. Model reduction via balanced realizations: an extension and frequency weighting techniques. IEEE Transactions
on Automatic Control, 33(7):687–692, 1988.
[2] A. C. Antoulas. *Approximation of Large-Scale Dynamical Systems*. Society
for Industrial and Applied Mathematics, 2005.
[3] A.
Bemporad.
Linear
and
nonlinear
system
identification
under
ℓ1- and group-Lasso regularization via L-BFGS-B.
arXiv preprint
arXiv:2403.03827, 2024.
[4] G. E. Blelloch. Prefix sums and their applications. 1990. [5] Y. N. Dauphin, A. Fan, M. Auli, and D. Grangier. Language modeling with
gated convolutional networks.
In International Conference on Machine
Learning, pages 933–941. PMLR, 2017.
[6] M. Fazel, H. Hindi, and S.P. Boyd. A rank minimization heuristic with application to minimum order system approximation. In Proc. of the American Control Conf., volume 6, pages 4734–4739, 2001.
[7] M. Forgione, M. Mejari, and D. Piga. Learning neural state-space models:
do we need a state estimator? *arXiv preprint arXiv:2206.12928*, 2022.
[8] M. Forgione and D. Piga.
dynoNet: A neural network architecture for
learning dynamical systems.
International Journal of Adaptive Control
and Signal Processing, 35(4):612–626, 2021.
[9] K. Glover. All optimal hankel-norm approximations of linear multivariable systems and their L∞-error bounds. *International Journal of Control*,
39(6):1115–1193, 1984.
[10] M. Green and D. Limebeer. *Linear Robust Control*. Dover publications,
2012.
[11] A. Gu, K. Goel, A. Gupta, and C. R´e. On the parameterization and initialization of diagonal state space models. Advances in Neural Information
Processing Systems, 35:35971–35983, 2022.
[12] A. Gu, K. Goel, and C. R´e.
Efficiently modeling long sequences with
structured state spaces. The International Conference on Learning Representations (ICLR), 2022.
[13] T. Katayama. *Subspace Methods for System Identification*. Springer London, 2005.
[14] Y. Liu and B. O. D. Anderson. Singular perturbation approximation of
balanced systems. *International Journal of Control*, 50(4):1379–1405, 1989.
[15] B. Moore. Principal component analysis in linear systems: Controllability, observability, and model reduction. IEEE Transactions on Automatic
Control, 26(1):17–32, 1981.
[16] J. P. No¨el and M. Schoukens. F-16 aircraft benchmark based on ground
vibration test data. In 2017 Workshop on Nonlinear System Identification
Benchmarks, pages 19–23, 2017.
[17] A. Orvieto, S. L. Smith, A. Gu, A. Fernando, C. Gulcehre, R. Pascanu, and
S. De. Resurrecting recurrent neural networks for long sequences. arXiv preprint arXiv:2303.06349, 2023.
[18] G. Pillonetto, T. Chen, A. Chiuso, G. De Nicolao, and L. Ljung. Regularized linear system identification using atomic, nuclear and kernel-based norms: The role of the stability constraint. *Automatica*, 69:137–149, 2016.
[19] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, et al.
Language models are unsupervised multitask learners. *OpenAI blog*, 1(8):9,
2019.
[20] M. Revay, R. Wang, and I. R. Manchester. Recurrent equilibrium networks:
Flexible dynamic models with guaranteed stability and robustness. IEEE Transactions on Automatic Control, 2023.
[21] G. Scarciotti and A. Astolfi. Interconnection-based model order reduction
- a survey. *European Journal of Control*, 75:100929, 2024.
[22] J. Schoukens and L. Ljung. Nonlinear system identification: A user-oriented
road map. *IEEE Control Systems Magazine*, 39(6):28–99, 2019.
[23] M. Schoukens and K. Tiels. Identification of block-oriented nonlinear systems starting from linear approximations: A survey. *Automatica*, 85:272–
292, 2017.
[24] J. TH. Smith, A. Warrington, and S. W. Linderman. Simplified state space
layers for sequence modeling. *arXiv preprint arXiv:2208.04933*, 2022.
[25] Y. Tay, M. Dehghani, S. Abnar, D. Shen, Y.and Bahri, P. Pham, J. Rao,
L. Yang, S. Ruder, and D. Metzler. Long range arena: A benchmark for efficient transformers. *arXiv preprint arXiv:2011.04006*, 2020.
[26] R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of
the Royal Statistical Society. Series B, 58(1):267–288, 1996.
[27] Y. Wu and K. He. Group normalization. In Proceedings of the European
conference on computer vision (ECCV), pages 3–19, 2018.