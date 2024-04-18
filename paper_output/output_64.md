# Transformation-Free Fixed-Structure Model Reduction For Lpv Systems

Lennart Heeren1, Adwait Datar1, Antonio Mendez Gonzalez1 and Herbert Werner1
Abstract— In this paper, we propose a model reduction technique for linear parameter varying (LPV) systems based on available tools for fixed-structure controller synthesis. We start by transforming a model reduction problem into an equivalent controller synthesis problem by defining an appropriate generalized plant. The controller synthesis problem is then solved by using gradient-based tools available in the literature. Owing to the flexibility of the gradient-based synthesis tools, we are able to impose a desired structure on the obtained reduced model. Additionally, we obtain a bound on the approximation error as a direct output of the optimization problem. The proposed methods are applied on a benchmark mechanical system of interconnected masses, springs and dampers. To evaluate the effect of the proposed model-reduction approach on controller design, LPV controllers designed using the reduced models (with and without an imposed structure) are compared in closed-loop with the original model.

## I. Introduction

Linear parameter varying (LPV) systems are a generalization of linear time-invariant (LTI) systems where the model matrices have a continuous-dependence on a so-called scheduling variable (see [1], [2]). The LPV framework offers analysis and synthesis tools to systematically design controllers with stability and performance guarantees. However, in some cases the available techniques fail to properly scale with the high complexity of the considered LPV system and can be intractable to apply, specially for very high order systems.

Although the literature on model reduction techniques for LTI systems is vast, it is relatively sparse for LPV systems and thus forms an active area of research. A typical model reduction approach involves an interpolation step wrapping around standard LTI model reduction techniques applied on a grid of of scheduling parameters values. (see [3], [4]). A grid-free approach to LPV model reduction is presented in [5]. Standard model reduction techniques based on balanced truncation involve solving a set of Linear matrix inequalities (LMIs) to obtain the generalised controllability and observability Gramians [6]. From the generalised Gramians a balanced realisation can be constructed, a truncation of which then yields a reduced state-space model. The approximation error is obtained in the form of a sum of the truncated Hankel singular values. Heuristic approaches to minimize this sum of singular values are deployed to obtain a reduced model with the minimum approximation error. In this paper, we bypass this two-step procedure and propose to directly minimize the approximation error bound using fixed-structure controller synthesis techniques. Following up on ideas from [7] and [8], we cast the model reduction problem in the form of a fixed-structure synthesis problem by appropriately defining a generalized plant. This opens the possibility to apply efficient tools developed for addressing the fixed-structure controller synthesis problem [9]–[12]. The optimization problem yields the locally optimal cost which then provides theoretical guarantees in terms of an upper bound on the approximation error. Owing to the flexibility of these gradient-based synthesis tools, we are able to impose a desired structure on the obtained reduced model. For example, it might be desirable to impose a block-diagonal modal structure on the state-matrix with each block of size 2 such that each block defines a particular mode of a system corresponding to a pair of complex-conjugate eigenvalues. Such a block-diagonal structure in the state-matrix has a good physical interpretation and can be used to design different controllers for different frequency regimes. For example, when looking at applications from structural mechanics, one is often interested in modeling and controlling a specific vibration-mode in a system. Another application comes from aeroservoelastic vehicles where a modal structure is desirable for control design (see [3]). This might further open doors for developing model reduction techniques that preserve the typical Lagrangian structure of mechanical systems [13].

Thus, the problem addressed in this paper is to obtain a reduced model with guaranteed error bound when a particular model structure is imposed.

A. Outline The outline of this paper is as follows. We start by discussing the preliminaries in Section II followed by a description of the proposed model reduction procedure in Section III. We next apply the proposed techniques on a benchmark mass-spring-damper example in Section IV and finally conclude the paper in Section V.

**II.** Preliminaries

The linear dynamics of linear parameter varying (LPV) systems depend on a vector of time-varying scheduling parameters

$$\rho(t)=[\rho_{1}(t),...,\rho_{n_{p}}(t)]^{\mathrm{T}}.$$
The values of ρ(t) can be measured online but are not known a priori. The general form of an LPV system is

$$\dot{x}(t)=A(\rho(t))x(t)+B(\rho(t))u(t),\tag{1a}$$ $$y(t)=C(\rho(t))x(t)+D(\rho(t))u(t)\tag{1b}$$
with state, input and output denoted by x(t) ∈ Rnx, u(t) ∈
Rnu and y(t) ∈ Rny, respectively. Here A(ρ), B(ρ), C(ρ) and D(ρ) are matrix-valued continuous functions of ρ and we C(ρ)
D(ρ)
use the notation G =
� A(ρ)
B(ρ)
�
to denote the LPV
system. For the method proposed in this paper, a rational dependence on ρ is assumed that enables the construction of an LPV model in a Linear Fractional Transformation (LFT) form reviewed in the next sub-section. If the dependence is not rational initially, it can be made so by introducing new scheduling parameters (possibly at the expense of some conservatism). All admissible trajectories of the scheduling parameters are assumed to be contained in a compact set,

$$\rho(t)\in{\mathcal{P}}\subset\mathbb{R}^{n_{\rho}},\quad\quad\forall t\geq0.$$
The goal of LPV model order reduction is to find a representation

$$\dot{x}_{\rm red}(t)=A_{\rm red}(\rho(t))x_{\rm red}(t)+B_{\rm red}(\rho(t))u(t),\tag{2a}$$ $$y(t)=C_{\rm red}(\rho(t))x_{\rm red}(t)+\quad D(\rho(t))u(t),\tag{2b}$$
that approximates system (1) in its input-output behavior while the state vector xred(t) ∈ Rn is of a significantly smaller dimension (n ≪ nx). To simplify notation, subscripts are used to indicate parameter dependencies, e.g. Aρ := A(ρ(t)). For a linear parameter varying system G, we denote by ||G||, the induced L2 norm of the system which reduces to the H∞
norm if the system is linear.

## A. Linear Fractional Transformation

For matrices M, ∆ and K of compatible dimensions, an upper LFT denoted by Fu(M,∆) and a lower LFT denoted by Fl(M,K) is defined as

$$\begin{split}\mathscr{F}_{u}\left(\begin{bmatrix}M_{11}&M_{12}\\ M_{21}&M_{22}\end{bmatrix},\Delta\right)=M_{22}+M_{21}\Delta\left(I-M_{11}\Delta\right)^{-1}M_{12},\\ \mathscr{F}_{1}\left(\begin{bmatrix}M_{11}&M_{12}\\ M_{21}&M_{22}\end{bmatrix},K\right)=M_{11}+M_{12}K\left(I-M_{22}K\right)^{-1}M_{21}.\end{split}$$
Assuming that the dependence of the model matrices in (1)
on ρ is rational, the system can be described in LFT form

resarilinear operator.From a closed set, we can write

$$\begin{bmatrix}x_{0}\\ y_{0}^{\prime}\\ y_{0}^{\prime}\end{bmatrix}=\mathcal{R}\left(\begin{bmatrix}D_{0}&C_{0}&D_{0}\\ C_{0}&D_{0}&D_{0}\\ D_{0}&C_{0}&C_{0}\end{bmatrix}\begin{bmatrix}x_{0}\\ y_{0}^{\prime}\\ y_{0}^{\prime}\end{bmatrix}\right),\tag{4}$$

where the dot product is $\mathcal{R}\left(\begin{matrix}D_{0}&C_{0}&D_{0}\\ C_{0}&D_{0}&D_{0}\\ D_{0}&C_{0}&C_{0}\end{matrix}\begin{bmatrix}x_{0}\\ y_{0}^{\prime}\\ y_{0}^{\prime}\end{bmatrix}\right)$.

The vector $\mathbf{v}$ is $\mathbf{v}(t)$ and $\mathbf{v}(t)$ is $\mathcal{R}^{(N)N}$.

The vector $\mathbf{v}$ is $\mathbf{v}(t)$ and $\mathbf{v}(t)$ is $\mathbf{v}(t)$. The vector $\mathbf{v}$ is $\mathbf{v}(t)$ and $\mathbf{v}(t)$ is $\mathbf{v}(t)$.

The vector $\mathbf{v}$ is $\mathbf{v}(t)$ and $\mathbf{v}(t)$ is $\mathbf{v}(t)$ and $\mathbf{v}(t)$ is $\mathbf{v}(t)$.

## Iii. Model Reduction Via Fixed Structure Synthesis

In this section, we present our approach to model reduction in detail. Standard model reduction techniques (see [6]) based on balanced truncation typically involve the following steps.

1) First, the following optimization problem is solved to obtain the generalized Gramians Oρ and Cρ:

min
Cρ,Oρ
      Trace
           �
            CρOρ
                 �

subject to AT
            ρOρ +OρAρ +CT
                             ρCρ < 0
                                         ∀ρ ∈ P,

AρCρ +CρAT
        ρ +BρBT
             ρ < 0
                   ∀ρ ∈ P,

where Trace denotes the trace of a matrix.

2. Next, a transformation matrix $T$ is computed such that $$T^{T}\mathscr{O}_{p}T=T^{-1}\mathscr{C}_{p}T^{-T}=\Sigma=\begin{bmatrix}\sigma_{1},&\\ &\ddots\\ \sigma_{n}\end{bmatrix}.$$ 3. Finally, matrix $T$ is truncated to obtain the reduced model and the model approximation error is available in the form of the sum of the truncated singular values; the number of the truncated model. Following up on ideas from [7] and [8] we propose the strictly minimizes. We correspond by using controller as an optimal controller synthesis problem using a suitable norm. Consider the optimization problem with reduced planner order $n$: $$\min_{G_{\text{opt}}\in\mathscr{G}_{p}}\quad\|G-G_{\text{mix}}\|\,,$$ (6) where $\mathscr{G}_{p}$ is the set of LPV systems of order $n$. This is depicted in the block diagram in Fig. 1 (left). Observe that the block diagram in Fig. 1 (left) can be equivalently transformed to the block diagram in Fig. 1 (left), i.e., $$G-G_{\text{opt}}=\mathscr{F}_{1}\left(\begin{bmatrix}G&I\\ I&0\end{bmatrix},G_{\text{resd}}\right).$$ We can thus convert the reconstruction (model reduction) problem into a controller synthesis problem by defining an appropriate generalized plant $$G_{\text{gp}}=\begin{bmatrix}G&-I\\ I&0\end{bmatrix}$$ and posing the controller synthesis problem as $$\min_{R}\quad\|\mathscr{F}_{1}(G_{\text{gp}},K)\|.$$ (7)
Optimal solution K∗ to this problem thus produces an approximate model Gred = K∗ with an approximation error of ∥G − Gred∥ = ∥Fl(Ggp,K∗)∥. Standard computationally efficient techniques based on linear matrix inequalities (LMI) (see [16]) provide a solution to the controller synthesis problem when there is no restriction on the order of the controller. However, this would lead to a Gred which has the same order as that of G and thus not solve the modelreduction problem. Therefore, we employ fixed-structure synthesis algorithms to solve the above problem that allow us to specify a fixed order of the sought controller Gred which is here the reduced model. Starting points for this are tools developed in [9]–[12]. This avoids computing the tranformation matrices. Furthermore, since the approximation error is the objective function of the optimization problem, we obtain the error estimates as a direct outcome of the optimization. The equivalent controller synthesis problem obtained in the previous section leads to a bi-linear matrix inequality (BMI) and cannot be solved by standard LMI solvers. We use a gradient based optimization algorithm in [12] to solve the BMI problem. The interested reader is pointed to [12] for details on the synthesis algorithm.

Finally, owing to the flexibility of the gradient-based fixedstructure synthesis algorithm, we can easily enforce a desired structure in the model matrices of the reduced plant. This can be done by imposing a suitable structure on the model matrices of the sought reduced model. Letting A ⊂ Rn×n, B ⊂ Rn×nu, C ⊂ Rny×n and D ⊂ Rny×nu denote the sets of model matrices with an appropriate size and a specific sparsity structure, we can pose the optimization problem

$$\begin{array}{c}\min\\ G_{\rm red}\in\delta_{\rm n}^{\rm s}\end{array}\qquad\left|\left|G-G_{\rm red}\right|\right|,\tag{8}$$
where

$${\mathcal{G}}_{n}^{s}=\left\{\left[{\frac{A_{\rho}}{C_{\rho}}}\,{\frac{B_{\rho}}{D_{\rho}}}\,\right]|A_{\rho}\in{\mathcal{A}},B_{\rho}\in{\mathcal{B}},C_{\rho}\in{\mathcal{C}},D_{\rho}\in{\mathcal{D}}\right\}.$$
As briefly discussed earlier, it might be desirable to obtain the state matrix of the reduced plant in a modal form. This can easily be enforced in the proposed approach by setting A ⊂ Rn×n to be the set of block-diagonal matrices with block-size at most 2 and setting B = Rn×nu, C = Rny×n and D = Rny×nu. For the considered example in the next section, we obtain two reduced models, viz., one without imposing any structure and one where we impose a block-diagonal structure on the state-matrix.

## Iv. Numerical Results

We illustrate the applicability of the proposed method on an example of chained multiple mass-spring-damper system with time-varying, scheduled stiffness parameters of individual springs, borrowed from the literature [17] which is slightly modified to add more scheduling parameters (see Fig. 2). The equations of motion for the $N$ blocks are given by

$$m\ddot{x_{i}}=\begin{cases}-F_{1}-F_{1,2},&\text{if}i=1,\\ -F_{i}-F_{i,i-1}-F_{i,i+1},&\text{if}i=2,...,N-1,\\ -F_{N}-F_{N,N-1}+F_{\text{u}},&\text{if}i=N,\end{cases}\tag{9a}$$ $$F_{i}=d\dot{x}_{i}+k_{i}(\rho_{i})x_{i},$$ (9b) $$F_{i,j}=d(\dot{x}_{i}-\dot{x}_{j})+k_{j}(\rho_{j})(x_{i}-x_{j}),$$ (9c) $$y=x_{N}.\tag{9d}$$
where the forces Fi and Fi, j depend on the externally scheduled spring constants, ki(ρi) for i = 1*,...,*N. This system can be easily extended in terms of the number of states by adding more blocks. Also the number of scheduling parameters can be varied by assuming that either the stiffnesses of all springs are equal (nρ = 1), or that ρi = ρi+nρ for i = 1*,...,*N − nρ.

For the numerical results, we let N = 10 to obtain a fullorder model (called the original model) of order 20. The admissible parameter range is taken as P = [−1,1]. We

Approximation error bound
||G−Gred||
0.3056
||G−Gred-modal||
7.6012

apply the proposed model reduction techniques described in Section III to reduce the original model of order 20 (denoted by G) to obtain two reduced-order models of order 4, one without any imposed structure on the state-matrix which we denote by Gred, and one with an imposed blockdiagonal/modal structure (with block-size 2) on the statematrix which we denote by Gred-modal. Table I shows a comparison of the obtained approximation error bounds. We can see that imposing structure on the state-matrix comes at the cost of a larger approximation error. These reduced-order models are next compared with the original model in time and frequency domain in the next sub-section.

## A. Comparison Of Open-Loop Models

We first compare the different models in frequency domain by looking at the sigma plots in Fig. 3. Multiple curves of the same color show the sigma plots of the same LPV
model evaluated at 5 uniformly spaced grid points on P =
[−1,1]. It can be seen that the reduced model without any imposed structure Gred (shown in red) matches well with the original model G (blue curves). Although, the reduced model Gred-modal with an imposed block-diagonal modal structure on the state-matrix does not match well with original model G, the inaccuracy is dominant in the poor approximation of the static-gain. To bring out the comparison clearly, Fig. 4
shows the sigma plots of the error system (G−Gred) (shown in red) and the error system (G−Gred-modal) (shown in green).

It can be observed that the imposing the modal structure in the state-matrix costs us an inaccurate model bringing out the inherent trade-off. Finally, Fig. 5 shows that the step response of Gred matches well with the original model. At the same time, the step response of Gred-modal does not match well with the original model in terms of static gain.

It is apparent in the above plots that the mismatch between the original model and the reduced model Gred-modal is concentrated in the low-frequency (static gain) regime. It is known that a model used for controller design needs to be accurate around the bandwidth and an uncertain static-gain of the open loop can be handled by a well-designed controller. This is evident in the comparison of closed-loop performance discussed in the next sub-section.

## B. Comparison In Closed-Loop

In this section, we use standard LPV synthesis techniques to design a controller for the reduced model and test it on the original model to compare performance in closed-loop. We give only a brief summary of the main ideas behind the synthesis techniques. It is assumed that an LPV model of the corresponding plant is available in LFT form as in (4) where u is the control input and y is the measured signal. Standard LPV synthesis techniques are used to design controllers for the original full-order plant and the reduced plants and we refer the interested reader to [18] for details. The LPV controller has the form described by

$$\begin{array}{c}\left[\dot{x}_{\rm K}(t)\right]\\ v_{\rm K}(t)\end{array}=\left[\begin{array}{cccc}A^{\rm K}&B^{\rm K}_{\rm W}&B^{\rm K}_{\rm V}\\ C^{\rm K}_{\rm V}&D^{\rm K}_{\rm W}&D^{\rm K}_{\rm W}\\ C^{\rm K}_{\rm U}&D^{\rm K}_{\rm W}&D^{\rm K}_{\rm W}\end{array}\right]\left[\begin{array}{c}x_{\rm K}(t)\\ w_{\rm K}(t)\\ e(t)\end{array}\right]\tag{10}$$

$$w_{\rm K}(t)=\Delta_{\rm K}\ v_{\rm K}(t).\tag{11}$$
where e = r − y with the external signal r as the reference command. This controller is interconnected with the plant through the signals u and e along with a performance channel z (typically incorporating S/KS loop shaping) which results

in an LPV closed-loop model in LFT form described by

$$\begin{bmatrix}\hat{x}_{\text{CL}}\\ v_{\text{CL}}\\ z\end{bmatrix}=\begin{bmatrix}\mathcal{A}&\mathcal{B}_{W}&\mathcal{B}_{r}\\ \mathcal{C}_{V}&\mathcal{D}_{W}&\mathcal{D}_{Vr}\\ \mathcal{C}_{z}&\mathcal{D}_{zW}&\mathcal{D}_{yr}\end{bmatrix}\begin{bmatrix}x_{\text{CL}}\\ w_{\text{CL}}\\ r\end{bmatrix}\tag{12}$$ $$w_{\text{CL}}=\Delta_{\text{CL}}\ v_{\text{CL}},\tag{13}$$
where xCL = [x, xK]
T, ∆CL collects in block diagonal fashion the plant and controller block matrices, ∆ and ∆K respectively and the calligraphic system matrices contain the resulting closed-loop interconnection of the LPV plant and controller.

Feasibility of a set of parameterized LMIs (representing the LPV version of the bounded real lemma, see [18] for details) guarantees stability and induced L2 performance, via the existence of the corresponding Lyapunov matrix and multipliers. To reduce the complexity of the controller synthesis, a parameter-independent Lyapunov function is used along with D/G multipliers. The latter guarantees the parameter block of the controller be an exact copy of the one of the plant. We apply the Full-Block S-Procedure (FBSP) and the parameter elimination lemma [18] in the form of a two-step controller synthesis procedure to obtain the controller. In the first step, an LMI optimization problem is solved to obtain Lyapunov matrices and structured multiplier matrices, which guarantee a level of performance. In the second step, the state-space matrices of the LPV controller can be constructed using the obtained matrices from the first step.

We emphasize that the reduced model is used solely for controller design and the obtained controller is then tested in closed-loop with the original plant. Let K, Kred and Kred-modal be the controllers designed using the plants G, Gred and Gred-modal, respectively. These controllers are implemented in closed-loop with the original plant G and compared in the following to evaluate the effect of model reduction on closed-loop performance. We start the assessment of the closed-loop by looking at the sigma plots of the closedloop in Fig. 6. Fig. 6 shows the sigma plots of the closedloop system with controllers K, Kred and Kred-modal. Since all curves are concentrated at 1 at low frequencies, we can conclude that the closed-loop performance is good in this frequency regime with both reduced models. This also agrees with the step-response curves shown in Fig. 7 where all closed-loop models show a zero steady-state error. Furthermore, this illuminates the fact that in spite of the poor open-loop approximation error at low frequencies, the designed controller is able to handle this and achieve a good performance in closed-loop at low-frequencies. The transient responses of the closed-loop with a controllers K
and Kred match well and show good performance whereas the transient response of the closed loop with controller Kred-modal designed using the reduced model Gred-modal shows a performance degradation. Specifically, we get a slightly higher rise-time, a higher overshoot and a higher settling time. Finally, Fig. 8 shows the sigma plots of the obtained controllers. It can be seen that the controllers designed with the different models show very similar frequency responses in general. While the controllers K and Kred are strictly proper, the controller Kred-modal designed with the reduced order model Gred-modal is bi-proper.

## V. Conclusions And Future Work

We propose a novel model reduction technique for LPV
systems by leveraging available tools on fixed-structure synthesis. Owing to the flexibility of the used fixed-structure synthesis tools, we are able to impose a desired structure on the model matrices of the reduced-order model. We demonstrate the applicability of the results on a benchmark example by first analyzing the performance in open-loop. Finally, we evaluate the effect of the model reduction technique on controller design by evaluating the closed-loop performance.

sure that you do not shorten the textheight too much.

## References

[1]
J. S. Shamma, "An overview of lpv systems," Control
of linear parameter varying systems with applications,
pp. 3–26, 2012.
[2]
C. Hoffmann and H. Werner, "A survey of linear
parameter-varying control applications validated by experiments or high-fidelity simulations," IEEE Transactions on Control Systems Technology, vol. 23, no. 2, pp. 416–433, 2014.
[3]
J. Theis, B. Takarics, H. Pfifer, G. J. Balas, and H.
Werner, "Modal matching for lpv model reduction of aeroservoelastic vehicles," in AIAA Atmospheric Flight
Mechanics Conference, 2015, p. 1686.
[4]
D. Amsallem and C. Farhat, "An online method for
interpolating linear parametric reduced-order models," SIAM Journal on Scientific Computing, vol. 33, no. 5, pp. 2169–2198, 2011.
[5]
L. Heeren and H. Werner, "Grid-free constraints for
parameter-dependent generalized gramians via full block s-procedure," in 2022 European Control Conference (ECC), IEEE, 2022, pp. 1073–1078.
[6]
G. D. Wood, "Control of parameter-dependent mechanical systems," Dissertation, St Johns College,
Cambridge, 1995.
[7]
C. L. Beck, Model reduction and minimality for uncertain systems. California Institute of Technology, 1997.
[8]
F. Al-Taie and H. Werner, "Structure-preserving model
reduction for spatially interconnected systems with experimental validation on an actuated beam," International Journal of Control, vol. 89, no. 6, pp. 1248– 1268, 2016.
[9]
S. S. Chughtai and H. Werner, "A hybrid approach
to the synthesis of simply structured robust and
gain-scheduled controllers," *Applied Soft Computing*, vol. 11, no. 6, pp. 4078–4086, 2011.

[10]
S. S. Chughtai and H. Werner, "Simply structured
controllers for parameter varying distributed systems," *Smart materials and structures*, vol. 20, no. 1,
p. 015 006, 2010.
[11]
S. S. Chughtai and H. Werner, "Fixed structure controller design for a class of spatially interconnected systems," *IFAC Proceedings Volumes*, vol. 40, no. 9, pp. 224–229, 2007.
[12]
H. Abbas, S. S. Chughtai, and H. Werner, "A hybrid
gradient-lmi algorithm for solving bmis in control design problems," *IFAC Proceedings Volumes*, vol. 41, no. 2, pp. 14 319–14 323, 2008.
[13]
S. Lall, P. Krysl, and J. E. Marsden, "Structurepreserving model reduction for mechanical systems,"
Physica D: Nonlinear Phenomena, vol. 184, no. 1-4, pp. 304–318, 2003.
[14]
K. Zhou, J. C. Doyle, and K. Glover, Robust and
optimal control. Upper Saddle River, NJ: Prentice Hall, 1996.
[15]
S. Hecker, A. Varga, and J.-F. Magni, "Enhanced lfrtoolbox for matlab," Aerospace Science and Technology, vol. 9, no. 2, pp. 173–180, 2005.
[16]
C. Scherer and S. Weiland, "Lecture notes disc course
on linear matrix inequalities in control," Delft University, 1999.
[17]
J. Theis, P. Seiler, and H. Werner, "LPV model order
reduction by parameter-varying oblique projection," IEEE Trans. Contr. Syst. Technol., vol. 26, no. 3, pp. 773–784, 2018.
[18]
C. W. Scherer, "A full block s-procedure with applications," in Proceedings of the 36th IEEE Conference on Decision and Control, IEEE, vol. 3, 1997, pp. 2602– 2607.