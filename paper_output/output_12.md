# On Moment Relaxations For Linear State Feedback Controller Synthesis With Non-Convex Quadratic Costs And Constraints

Dennis Gramlich, Sheng Gao, Hao Zhang, Carsten W. Scherer and Christian Ebenbauer

  Abstract— We present a simple and effective way to
account for non-convex costs and constraints in state
feedback synthesis, and an interpretation for the vari-
ables in which state feedback synthesis is typically
convex. We achieve this by deriving the controller
design using moment matrices of state and input. It
turns out that this approach allows the consideration
of non-convex constraints by relaxing them as expec-
tation constraints, and that the variables in which
state feedback synthesis is typically convexified can
be identified with blocks of these moment matrices.

          I. INTRODUCTION
 To derive convex controller synthesis conditions sub-
ject to potentially non-convex quadratic constraints we
take a similar approach as [7]. This approach uses mo-
ment matrices and relaxes (non-convex) quadratic con-
straints as expectation constraints (power constraints).
Due to the similarities to [7], we highlight the novelties
of this paper/differences to [7] right at the beginning.

- We show that, as in non-convex quadratic programming [16], the relaxation of non-convex quadratic constraints as expectation constraints yields a deterministic solution, for some problems, and a stochastic solution, for other problems. Deterministic means that the optimal policy of the relaxed problem is deterministic and coincides with an optimal policy of the original problem. Stochastic means that the optimal policy is stochastic and not optimal for the original problem.
- We show how to realize the stochastic optimal policies. - We identify blocks of our moment matrices with the
variables in which state feedback synthesis is usually convexified using the dualization lemma [21].
- We study moment matrices of affine linear systems. - We explain the benefits of linear controller synthesis
with non-convex constraints in compelling examples. Convexification of state feedback synthesis is considered to be a relatively well understood problem in

  Carsten W. Scherer is funded by Deutsche Forschungsgemein-
schaft (DFG, German Research Foundation) under Germany's
Excellence Strategy - EXC 2075 - 390740016. He acknowledges the
support by the Stuttgart Center for Simulation Science (SimTech).
  Dennis Gramlich and Christian Ebenbauer are with the Chair
of Intelligent Control Systems, RWTH Aachen University, 52074
Aachen, Germany {dennis.gramlich,christian.ebenbauer}
@ic.rwth-aachen.de
  Sheng Gao, and Hao Zhang are with the College of Electronic
and Information Engineering, the Department of Control Science
and Engineering, Tongji University, Shanghai, 200092, P. R. China.
2110134@tongji.edu.cn,zhang_hao@tongji.edu.cn.
  Carsten W. Scherer is with the Chair of Mathematical Sys-
tems Theory, University of Stuttgart, 70569 Stuttgart, Germany
carsten.scherer@imng.uni-stuttgart.de

control theory. Lossless convexifications, i.e., transforma-
tions that convert a generally non-convex optimization
problem into a convex optimization problem, exist for the
quadratic stabilization of linear systems [2], H2 and H∞
state feedback synthesis [6], robust state feedback syn-
thesis for systems in linear fractional representation form
[20], and data-based controller synthesis [24].The equiv-
alent convex problems are usually obtained by working
with the dual system [11], or by invoking a dualization
lemma [21]. Throughout, a variable transformation from
the parameters of a quadratic storage function to new
parameters is used, since the controller synthesis is non-
convex in the original parameters for the listed problems.
  All the cited studies consider the new parameters
merely as a useful tool for finding the actual parameters
of interest. In the present work, however, we give the
transformed parameters an interpretation by deriving the
convexification based on moment matrices of state and
input. In the moment matrices, state feedback synthesis
is convex and the blocks of these moment matrices can be
identified with transformed parameters of other works.
  Studying the moment matrices of state and input of
a dynamical system is certainly an established approach
in the research literature. The latter comes from the fact
that occupation measures [17] and Lyapunov measures
[18], [23] offer a dual perspective to value functions and
Lyapunov functions with advantages for the convexifica-
tion of state feedback synthesis. It is therefore proposed,
e.g., in [14], [9], to optimize over the moment matrices of
occupation measures of state and input. The restriction
to linear systems and moments of order two, which we
consider in this paper, is a special case of what is consid-
ered in these studies. On the other hand, linear systems
are generally recognized as an important case and allow
for stronger results than polynomial systems. Controller
synthesis for linear systems via deterministically inter-
preted second-order moment matrices is discussed in
detail in [1]. As shown in [8], it enables the convex com-
putation of the H∞-norm of linear systems. In addition,
state feedback LQG synthesis via second-order moment
matrices is discussed in [12]. In contrast to [1], [12], the
present paper and [7] address control problems with non-
convex quadratic costs and constraints. These are convex
in the moment matrices and always admit the extraction
of a stochastic optimal solution. However, in the presence
of non-convex costs or constraints, the optimal moment
matrices may be realizable only by a stochastic policy
satisfying constraints only in expectation.

  Moment matrices can have various benefits for the
convexification structural controller constraints [19], [5],
or multi-objective control problems [15]. We expand this
list with the design affine linear controllers that avoid
non-convex regions in the state space (Section VI) or
swing up an inverted pendulum (Section VII).

## Ii. Problem Statement We Study A Discrete-Time Linear Time Varying System

$$x_{t+1}=f_{t}+A_{t}x_{t}+B_{t}u_{t}+w_{t}.\tag{1}$$

Here, $x_{t}\in\mathbb{R}^{n}$ is the state, $u_{t}\in\mathbb{R}^{m}$ is the control input and $w_{t}\in\mathbb{R}^{n}$ is a disturbance. Accordingly, $A_{t}\in\mathbb{R}^{n\times n}$ and $B_{t}\in\mathbb{R}^{n\times m}$ are the system matrices at time $t$ and $f_{t}\in\mathbb{R}^{n}$ is a additive element $t$, $w_{t}$ is the observation of the 
is an additional constant term in the dynamics.

For (1) we study the stochastic control problem

$$\begin{array}{ll}\mbox{minimize}&\mathbb{E}\sum_{t=0}^{N}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)^{\top}R_{t}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)\\ \mbox{s.t.}&x_{t+1}=f_{t}+A_{t}x_{t}+B_{t}u_{t}+w_{t},\\ &\mathbb{E}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)^{\top}H_{ti}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)\leq0,\quad i=1,\ldots,s,\\ &u_{t}\sim\mathbb{P}_{u_{t}},\quad w_{t}\sim\mathbb{P}_{w_{t}},\quad x_{0}\sim\mathbb{P}_{x_{0}}.\end{array}\tag{2a}$$
In (2), Px0 denotes the probability distribution of the initial state, Pwt denotes the distribution of the disturbance at time t and Put denotes the distribution of the input at time t. We assume that the first and second moments of x0 are fixed and known and denote them with

$$\overline{\Sigma}_{0}=\begin{pmatrix}\sigma_{0}^{11}&\sigma_{0}^{12}\\ \sigma_{0}^{21}&\Sigma_{0}^{22}\end{pmatrix}=\mathbb{E}\begin{pmatrix}1\\ x_{0}\end{pmatrix}\begin{pmatrix}1\\ x_{0}\end{pmatrix}^{\top}.\tag{3}$$
The initial state x0 and the disturbances wt for t =
0*,... ,N*−1 are assumed to be stochastically independent.

In addition, the control input ut is restricted to be conditionally independent from x0 and wt for t = 0*,... ,N* −1
given the current state xt. The latter restriction makes sure that the closed loop is a Markov process [10] and is satisfied, e.g., if ut = πt(xt,vt), where πt is some measurable function and vt is a random variable independent from x0 and wt for t = 0*,... ,N* −1. The matrices Rt,Hti ∈ R(1+n+m)×(1+n+m) are assumed to be symmetric, but may be indefinite. In (2) we regard the distributions Put of the control inputs ut as the control policy and we minimize over this control policy. Problem (2) could be a relaxation of a deterministic control problem with non-convex quadratic constraints, which is np-hard.

## Iii. Convexification Over Moment Matrices To Approach (2), We Study The Moment Matrices

$$\Sigma_{t}=\begin{pmatrix}\sigma_{t}^{11}&\sigma_{t}^{12}&\sigma_{t}^{13}\\ \sigma_{t}^{21}&\Sigma_{t}^{22}&\Sigma_{t}^{23}\\ \sigma_{t}^{31}&\Sigma_{t}^{32}&\Sigma_{t}^{33}\end{pmatrix}:=\mathbb{E}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}^{\top}\tag{4}$$
of a random trajectory (xt,ut) of (1), where x0 ∼ Px0, wt ∼ Pwt and ut ∼ Put for t = 0*,... ,N*. Obviously, each control policy (Put) gives rise to a sequence of moments (Σt). The advantage of studying the moments
(Σt) lies in the fact that the sequence of moments that can result from a control policy (Put) is characterized by simple linear and semi-definite constraints.

These constraints involve the matrix valued functions
(Σ,Σ+,Σw) ↦ ̃Ft(Σ,Σ+,Σw) defined by ̃Ft(Σ,Σ+,Σw)
equal to

$$\begin{array}{r l r l}{-\sigma^{11}}&{{}-\sigma^{12}}&{{}-\sigma^{13}}\\ {-\sigma^{21}}&{{}-\Sigma^{22}}&{{}-\Sigma^{23}}\\ {-\sigma^{31}}&{{}-\Sigma^{32}}&{{}-\Sigma^{33}}\end{array}$$ ($\bullet$)${}^{\top}$

$-\Sigma^{w}$ $$\left[\begin{array}{c c c}{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}\end{array}\right]\sigma_{+}^{11}\;\;\;\;\sigma_{+}^{12}$$
Theorem 3.1: Let Σt = Σ⊺
t ∈ R(1+n+m)×(1+n+m) be a sequence of matrices satisfying the initial condition (3).

Then there exists a policy (Put) generating the sequence of moments (Σt) satisfying (4) if and only if

$$\Sigma_{t}\geq0,\qquad\qquad\widetilde{F}_{t}(\Sigma_{t},\Sigma_{t+1},\Sigma_{t}^{w})=0\qquad\qquad(5)$$
hold for t = 0*,... ,N*. Moreover, if (5) holds, then there exist controller parameters Kt = (k1
t K2
t ) and Σv t with

$$\left(\sigma_{t}^{31}\quad\Sigma_{t}^{32}\right)=\left(k_{t}^{1}\quad K_{t}^{2}\right)\left(\sigma_{t}^{11}\quad\sigma_{t}^{12}\right)\tag{6}$$

$$\Sigma_{t}^{v}=\Sigma_{t}^{33}-\left(k_{t}^{1}\quad K_{t}^{2}\right)\left(\sigma_{t}^{31}\quad\Sigma_{t}^{32}\right)^{\top}\geq0\tag{7}$$
and the moments (Σt) result from the particular policy

$u_{t}=k_{t}^{1}+K_{t}^{2}x_{t}+v_{t}$, (8)
where vt ∼ Pvt are some random variables independent from x0,wt for t = 0*,... ,N* − 1 with zero mean and variance Σv t .

Proof: Let a policy (Put) be given and let (Σt) be the sequence of moment matrices. We start by showing that (5) must hold. To this end, consider the equation

$$\begin{pmatrix}1&0&0\\ f_{t}&A_{t}&B_{t}\end{pmatrix}\begin{pmatrix}\sigma_{t}^{11}&\sigma_{t}^{12}&\sigma_{t}^{13}\\ \sigma_{t}^{21}&\Sigma_{t}^{22}&\Sigma_{t}^{23}\\ \sigma_{t}^{31}&\Sigma_{t}^{32}&\Sigma_{t}^{33}\end{pmatrix}(\bullet)^{\top}+\begin{pmatrix}0&0\\ 0&\Sigma^{w}\end{pmatrix}$$

$$\begin{pmatrix}\frac{(4)}{=}\mathbb{E}\begin{pmatrix}1&0&0&0\\ f_{t}&A_{t}&B_{t}&I\end{pmatrix}\begin{pmatrix}1\\ x_{t}\\ u_{t}\\ w_{t}\end{pmatrix}\begin{pmatrix}1\\ x_{t}\\ u_{t}\\ w_{t}\end{pmatrix}^{\top}(\bullet)^{\top}\\ \end{pmatrix}$$

$$\begin{pmatrix}1\\ \mathbb{E}\begin{pmatrix}1\\ x_{t+1}\end{pmatrix}\begin{pmatrix}1\\ x_{t+1}\end{pmatrix}^{\top}\stackrel{{(4)}}{{=}}\begin{pmatrix}\sigma_{t+1}^{11}&\sigma_{t+1}^{12}\\ \sigma_{t+1}^{21}&\Sigma_{t+1}^{22}\end{pmatrix},$$
which follows from (4), (1) and the independence of wt from (xt,ut). This equation implies ̃Ft(Σt,Σt+1,Σw t ) = 0.

The constraints Σt ⪰ 0 must obviously hold. Hence, (5)
is satisfied for any control policy (Put).

Next, let a sequence of matrices (Σt) satisfying (5) be given. We show that these matrices equal the moment matrices under the policy (8). To this end, assume that

$$\mathbb{E}\left(\begin{matrix}1\\ x_{t}\end{matrix}\right)\left(\begin{matrix}1\\ x_{t}\end{matrix}\right)^{\top}=\left(\begin{matrix}\sigma_{t}^{11}&\sigma_{t}^{12}\\ \sigma_{t}^{21}&\Sigma_{t}^{22}\end{matrix}\right)\tag{9}$$

and (8) hold at time t. Then, due to Σt ⪰ 0, there exist
controller parameters Kt = (k1
                             t
                                 K2
                                   t ) and Σv
                                            t = Σ33
                                                  t
                                                    −
k1
 t σ13
   t
      − K2
         t Σ23
            t
               ⪰ 0 satisfying (6) and (7) such that a
random variable vt ∼ Pvt with zero mean and variance
Σv
 t can be defined. Next, due to Evt = 0, Evtx⊺
                                             t = 0 and
(8), we can show

$$\mathbb{E}\left(\begin{matrix}1\\ x_{t}\\ u_{t}\end{matrix}\right)u_{t}^{\top}=\left(\begin{matrix}1&0&0\\ 0&I&0\\ k_{t}^{1}&K_{t}^{2}&I\end{matrix}\right)\mathbb{E}\left(\begin{matrix}1\\ x_{t}\\ v_{t}\end{matrix}\right)\left(\begin{matrix}1\\ x_{t}\\ v_{t}\end{matrix}\right)^{\top}\left(\begin{matrix}(k_{t}^{1})^{\top}\\ (K_{t}^{2})^{\top}\\ I\end{matrix}\right)$$ $$=\left(\begin{matrix}1&0&0\\ 0&I&0\\ k_{t}^{1}&K_{t}^{2}&I\end{matrix}\right)\left(\begin{matrix}\sigma_{t}^{11}&\sigma_{t}^{12}&0\\ \sigma_{t}^{21}&\Sigma_{t}^{22}&0\\ 0&0&\Sigma_{t}^{v}\end{matrix}\right)\left(\begin{matrix}(k_{t}^{1})^{\top}\\ (K_{t}^{2})^{\top}\\ I\end{matrix}\right)$$ $$=\left(\begin{matrix}1&0&0\\ 0&I&0\\ k_{t}^{1}&K_{t}^{2}&I\end{matrix}\right)\left(\begin{matrix}\sigma_{t}^{13}\\ \Sigma_{t}^{23}\\ \Sigma_{t}^{23}\\ \Sigma_{t}^{33}\end{matrix}\right)=\left(\begin{matrix}\sigma_{t}^{23}\\ \Sigma_{t}^{23}\\ \Sigma_{t}^{23}\\ \Sigma_{t}^{33}\end{matrix}\right).$$
Combining the above with (9) shows that (4) holds at time t. Next, (4) and ̃Ft(Σt,Σt+1,Σw t ) = 0 together imply
(9) at time t + 1. In this way, we can prove inductively that (Σt) satisfies (4) for all times t.

Due to Theorem 3.1, we can directly optimize over the matrix sequence (Σt) instead of the policy (Put). To this end, notice that the cost (2a) and constraints (2c) can easily be expressed in terms of Σt as

$$\sum_{t=0}^{N}\operatorname{trace}\Sigma_{t}R_{t}\qquad\quad{\mathrm{and}}\qquad\quad\operatorname{trace}\Sigma_{t}H_{t i}\leq0.$$
Hence, we can reformulate (2) as the convex program

$$\begin{array}{ll}\underset{(\Sigma_{t})}{\text{minimize}}&\sum_{t=0}^{N}\text{trace}\,\Sigma_{t}R_{t}\\ \text{s.t.}&\widetilde{F}\big{(}\Sigma_{t},\Sigma_{t+1},\Sigma_{t}^{w}\big{)}=0,&t=0,\ldots,N-1,\\ &\text{trace}\,\Sigma_{t}H_{ti}\leq0,&t=0,\ldots,N,i=1,\ldots,s,\\ &\Sigma_{t}\geq0,&t=0,\ldots,N.\end{array}$$
Remark 3.2: We mention that in the case Σv t = 0 for t = 0*,... ,N*, the optimal policy is deterministic and otherwise it is stochastic. As it is shown in [12], if Rt and Hti are positive semi-definite for all t and i, then the optimal policy will be deterministic.

Remark 3.3: Consider [7] to see how to combine the state feedback synthesis presented in this section with a Kalman filter to obtain optimal output feedback policies.

## Iv. The Time-Invariant Case

We can also study the time-invariant infinite timehorizon version of (2) defined as

$$\begin{array}{ll}\underset{\mathbb{P}_{u}}{\text{minimize}}&\mathbb{E}\lim_{N\to\infty}\frac{1}{N}\sum_{t=0}^{N}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)^{\top}R\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)\\ \text{s.t.}&x_{t+1}=f+Ax_{t}+Bu_{t}+u_{t},\\ &\mathbb{E}\lim_{N\to\infty}\frac{1}{N}\sum_{t=0}^{N}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)^{\top}H_{i}\left(\begin{array}{c}1\\ x_{t}\\ u_{t}\end{array}\right)\leq0,\quad i=1,\ldots,s,\\ &\\ u_{t}\sim\mathbb{P}_{u},\quad w_{t}\sim\mathbb{P}_{w},\quad x_{0}\sim\mathbb{P}_{x_{0}}.\end{array}\tag{11c}$$
In this problem, we minimize the average cost (11a), since the summed cost might often be unbounded, and we impose the average constraints (11c). In addition, we assume that the system data (*f,A,B*), our control policy Pu, and the noise distribution Pw with variance Σw are time-invariant. As in the time-varying case, we study the matrix function ̃F. This time, however, we seach for a time-invariant matrix

$$\Sigma=\begin{pmatrix}\sigma^{11}&\sigma^{12}&\sigma^{13}\\ \sigma^{21}&\Sigma^{22}&\Sigma^{23}\\ \sigma^{31}&\Sigma^{32}&\Sigma^{33}\end{pmatrix}\tag{12}$$
and define a time-invariant control policy according to

$u_{t}=k^{1}+K^{2}x_{t}+v_{t}$ (13)
with controller parameters K = (k1
K2), Σv satisfying

$$\left(\sigma^{31}\quad\Sigma^{32}\right)=\left(k^{1}\quad K^{2}\right)\left(\sigma^{11}\quad\sigma^{12}\right)\tag{14}$$ $$\Sigma^{v}=\Sigma^{33}-\left(k^{1}\quad K^{2}\right)\left(\sigma^{13}\quad\Sigma^{23}\right)^{\top}\tag{15}$$
and vt for t ∈ N0 being identically and independently distributed random variables, independent from x0 and wt for t ∈ N0 with zero mean and variance Σv.

Lemma 4.1: Let Σ ∈ R(1+n+m)×(1+n+m) satisfy the conditions Σ ⪰ 0, ̃F(Σ,Σ,Σw) = 0 and σ11 = 1. Then, if
Σw ≻ 0 holds and ut is chosen according to the policy
(13), the sequence of moment matrices (Σt) generated by the policy (13) converges to Σ.

Proof: Denote the equation ̃F(Σ,Σ,Σw) = 0 as

$$\begin{pmatrix}\sigma^{11}&\sigma^{12}\\ \sigma^{21}&\Sigma^{22}\end{pmatrix}\geq\begin{pmatrix}1&0\\ f^{K}&A^{K}\end{pmatrix}\begin{pmatrix}\sigma^{11}&\sigma^{12}\\ \sigma^{21}&\Sigma^{22}\end{pmatrix}\begin{pmatrix}1&0\\ f^{K}&A^{K}\end{pmatrix}^{\top}$$ $$+\begin{pmatrix}0&0\\ 0&\Sigma^{w}+B\Sigma^{v}B^{\top}\end{pmatrix},$$
where f K ∶= f +Bk1 and AK = A+BK2. This Lyapunov inequality implies that AK is stable. Next consider ̃Σt ∶=
Σ − Σt. For this matrix ˜σ11
t
= 0 holds for all t, since by assumption σ11 = 1 = σ11
t . In addition, this matrix satisfies the Lyapunov equation

$$\begin{pmatrix}\tilde{\sigma}_{t+1}^{11}&\tilde{\sigma}_{t+1}^{12}\\ \tilde{\sigma}_{t+1}^{21}&\tilde{\Sigma}_{t+1}^{22}\end{pmatrix}=\begin{pmatrix}1&0\\ f^{K}&A^{K}\end{pmatrix}\begin{pmatrix}\tilde{\sigma}_{t}^{11}&\tilde{\sigma}_{t}^{12}\\ \tilde{\sigma}_{t}^{21}&\tilde{\Sigma}_{t}^{22}\end{pmatrix}\begin{pmatrix}1&0\\ f^{K}&A^{K}\end{pmatrix}^{\intercal}.$$

The left lower block of this Lyapunov equation reads
˜σ21
 t+1 = AK ˜σ21
          t
             + f K˜σ11
                   t , which, by ˜σ11
                                 t
                                    = 0 for all t and
stability of AK implies ˜σ21
                        t
                           → 0 for t → ∞. Finally,
inspecting the right lower block of this Lyapunov equa-
tion ̃Σ22
     t+1 = f Kσ11
              t (f K)⊺ + AKσ21
                            t (f K)⊺ + f Kσ12
                                          t (AK)⊺ +
AK ̃Σ22
    t (AK)⊺ and recalling AK being stable, ˜σ11
                                            t
                                              being
zero for all t and ˜σ21
                t
                  converging to zero, we conclude that
̃Σ22
 t
    converges to zero. In total, ̃Σt converges to zero.

 Due to Lemma 4.1, the average cost and average
constraints simplify under the control policy (13) to

$$\mathbb{E}\lim_{N\to\infty}{\frac{1}{N}}\sum_{t=0}^{N}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}^{\top}R\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}=\operatorname{trace}\Sigma R,$$
$$\mathbb{E}\lim_{N\to\infty}{\frac{1}{N}}\sum_{t=0}^{N}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}^{\top}H_{i}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}=\operatorname{trace}\Sigma H_{i}.$$
Consequently, the time-invariant control problem (11) can be solved as the convex program

minimize $\mbox{trace}\,\Sigma R$ (16) s.t. $\sigma^{11}=1,\quad\Sigma\geq0,$ $\widetilde{F}(\Sigma,\Sigma,\Sigma^{w})=0,$ $\mbox{trace}\,\Sigma H_{i}\leq0,$ $i=1,\ldots,s.$
Remark 4.2: Since, by Lemma 4.1, Σt converges to the stationary solution Σ, the expectation constraint (2c) is satisfied asymptotically and not just on average.

Moreover, if Σ0 happens to equal Σ, then this constraint is satisfied pointwise in time.

Remark 4.3: Also a mixture of the time-varying and time-invariant control problem can be studied. To this end, we may assume that the covariance matrix sequence becomes stationary, that is, (Σt)
=
(Σ0,Σ1,... ,ΣN−1,ΣN,ΣN,ΣN*,...*). Then, if the problem parameters (ft,At,Rt,Hti) also become stationary for t
≥
N, we could consider the constraints
̃F(Σt,Σt+1,Σw t )
=
0
for t
=
0*,... ,N* − 1, and
̃F(ΣN,ΣN,Σw N) = 0 for the sequence (Σt).

Regarding a suitable cost, we mention that a stationary sequence (Σt) permits, e.g., for a discounted cost

$$\mathbb{E}\sum_{t=0}^{N}\gamma^{t}\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}^{\top}R\begin{pmatrix}1\\ x_{t}\\ u_{t}\end{pmatrix}=\sum_{t=0}^{N-1}\gamma^{t}\operatorname{trace}R\Sigma_{t}+\frac{\gamma^{N}\operatorname{trace}R\Sigma_{N}}{1-\gamma}$$
1−γ R.

with discount factor γ ∈ [0,1[ by choosing Rt = γtR for t = 0*,... ,N* − 1 and RN = γN

## V. The Moment Matrix Perspective And Duality

Next, we explore how the convexification of state feedback synthesis problems given in Section III and IV relates to standard strategies for state feedback synthesis. To this end, we study one of the most basic problems of state feedback synthesis, namely, quadratic stabilization.

Particularly, an affine linear controller K stabilizes (some equilibrium of) the closed loop (f K,AK) ∶= (f +Bk1,A+
BK2) of an affine linear system with K in the sense of Lyapunov if there exists a symmetric matrix P such that the primal matrix inequalities

$$\begin{array}{r l}{-p^{11}}&{{}=p^{12}}\end{array}$$ p21 P 22 1 0 f K AK ⎞ ⎟⎟⎟⎟⎟ ⎠ ⎛ ⎜⎜⎜⎜⎜ ⎝ ⎞ ⎟⎟⎟⎟⎟ ⎠ ⎛ ⎜⎜⎜⎜⎜ ⎝
and P ≻ 0 hold. Equivalently an affine linear controller K stabilizes an affine linear system if there exists a symmetric matrix ̃P such that the dual matrix inequalities

$$\left(\bullet\right)^{\top}\left(\begin{array}{ccc}-\hat{p}^{11}&-\hat{p}^{12}\\ -\hat{p}^{21}&-\hat{P}^{22}\\ \hat{p}^{11}&\hat{p}^{12}\\ \hat{p}^{21}&\hat{P}^{22}\end{array}\right)\left(\begin{array}{ccc}1&(f^{K})^{\top}\\ 0&(A^{K})^{\top}\\ 1&0\\ 0&I\end{array}\right)\geq0\tag{18}$$
and ̃P ≻ 0 hold. The matrices P and ̃P can be linked by

$$P^{-1}=\begin{pmatrix}p^{11}&p^{12}\\ p^{21}&P^{22}\end{pmatrix}^{-1}=\begin{pmatrix}\hat{p}^{11}&\hat{p}^{12}\\ \hat{p}^{21}&\tilde{P}^{22}\end{pmatrix}=\widetilde{P}.$$
The relations between (17) and (18), and P and ̃P can be established by congruence transforms and the Schur complement, or by the following dualization lemma.

Lemma 5.1 (derived from Lemma 10.2, [21]): Let M
be a real, symmetric, non-singular matrix. Then the primal matrix inequalities

$$\left(\begin{array}{l}{{I}}\\ {{W}}\end{array}\right)^{\top}M\left(\begin{array}{l}{{I}}\\ {{W}}\end{array}\right)\leq0,\qquad\quad\left(\begin{array}{l}{{0}}\\ {{I}}\end{array}\right)^{\top}M\left(\begin{array}{l}{{0}}\\ {{I}}\end{array}\right)>0$$
are equivalent to the dual matrix inequalities

$$\begin{pmatrix}W^{\top}\\ -I\end{pmatrix}^{\top}M^{-1}\begin{pmatrix}W^{\top}\\ -I\end{pmatrix}\geq0,\qquad\begin{pmatrix}I\\ 0\end{pmatrix}^{\top}M^{-1}\begin{pmatrix}I\\ 0\end{pmatrix}\prec0.$$

The dual matrix inequality (18) can be convexified by the change of variables from $(P,K)$ to $(\widetilde{P},\widetilde{K})$, where $\widetilde{K}:=KP^{-1}$; we refer to [3] for this convexification.

In $(\widetilde{P},\widetilde{K})$, the dual matrix inequality (18) reads

$$\begin{pmatrix}-\tilde{p}^{11}&-\tilde{p}^{12}&-(\tilde{k}^{1})^{\top}\\ -\tilde{p}^{21}&-\tilde{P}^{22}&-(\widetilde{K}^{2})^{\top}\\ -\tilde{k}^{1}&-\widetilde{K}^{2}&-\widetilde{K}(\widetilde{P})^{-1}\widetilde{K}^{\top}\\ &&\tilde{p}^{11}&\tilde{p}^{12}\\ \tilde{p}^{21}&\widetilde{P}^{22}\end{pmatrix}\begin{pmatrix}1&f^{\top}\\ 0&A^{\top}\\ 0&B^{\top}\\ 1&0\\ 0&I\end{pmatrix}\\ \geq0.\tag{19}$$
Notice that the non-convexity in ̃
K( ̃P)−1 ̃
K⊺ can easily be resolved making use of the Schur complement lemma.

In addition, the representation (19) of the dual matrix inequality (18) reveals how established convexifying variable transforms relate to the one proposed in this article.

Namely, the feasibility of (19) with ̃P ⪰ 0 is equivalent to the feasibility of ̃F(Σ,Σ,0) ⪰ 0 with Σ ⪰ 0. One direction of this statement can be shown by choosing Σ as

$$\begin{pmatrix}\sigma^{11}&\sigma^{12}&\sigma^{13}\\ \sigma^{21}&\Sigma^{22}&\Sigma^{23}\\ \sigma^{31}&\Sigma^{32}&\Sigma^{33}\end{pmatrix}=\begin{pmatrix}-\tilde{p}^{11}&-\tilde{p}^{12}&-(\tilde{k}^{1})^{\intercal}\\ -\tilde{p}^{21}&-\tilde{P}^{22}&-(\tilde{K}^{2})^{\intercal}\\ -\tilde{k}^{1}&-\tilde{K}^{2}&-\tilde{K}(\tilde{P})^{-1}\tilde{K}^{\intercal}\end{pmatrix}.\tag{20}$$
For the reverse direction, we consider any Σ ⪰ 0 with
̃F(Σ,Σ,0) ⪰ 0. Next, perturb Σ33 to project Σ onto the image of the right hand side of (20). One can check that the latter does not lead to a violation of Σ ⪰ 0 or
̃F(Σ,Σ,0) ⪰ 0. This reverses the variable transform (20).

We emphasize that the variables ̃P and ̃
K in which established variable transforms convexify the quadratic stabilization problem equal, by (20), blocks of the moment matrix Σ. This suggests that ̃P and ̃
K should be interpreted as moment matrices. The fact that (18) is related to ̃F(Σ,Σ,0) ⪰ 0 and not to ̃F(Σ,Σ,0) = 0 does not alter the fact that ̃P and ̃
K can be interpreted as moment variables. Indeed, Theorem 3.1 can be proven with ̃F(Σ,Σ,0) ⪰ 0 (or ̃F(Σ,Σ,0) ⪯ 0) in (5) with the difference that, in this case, the sequence Σt is an upper
(lower) bound on the true moment matrices.

We mention that these relations to quadratic stabilization extend to state feedback H2 synthesis. Indeed, it can be shown that solving (11) for R
=
(0
C
0)
⊺
(0
C
0) and Σw = B2(B2)⊺ is equivalent to designing a state feedback controller minimizing the H2-norm from an input with input matrix B2 to an output with output matrix C; consider also [12].

## Vi. Example: Non-Convex Constraints

In this section we examine the possibility of considering non-convex constraints (avoiding non-convex regions in state space) with numerical examples. To this end, we study the stochastic optimal control problem

$$\begin{array}{ll}\mbox{minimize}&\mathbb{E}\sum_{t=0}^{N-1}\left(\left\|x_{t}\right\|^{2}+\left\|u_{t}\right\|^{2}\right)+100\left\|x_{N}\right\|^{2}\\ \mbox{s.t.}&x_{t+1}=x_{t}+u_{t},\\ &\mathbb{E}\|u_{t}\|^{2}\leq0.1,\\ &\mathbb{E}\|x_{t}-\hat{x}_{i}\|^{2}\geq(r_{i}+\varepsilon)^{2},\quad i=1,\ldots,s,\\ &u_{t}\sim\mathbb{P}_{u_{t}},\quad x_{0}\sim\delta_{\bar{x}}.\end{array}\tag{21a}$$
We assume that the states xt and control inputs ut take values in R2. The system dynamics (21b) define a two-dimensional integrator. We might imagine that this integrator is a very simple model for a robot in a plane. In this case, the constraint (21c) restricts the speed of the robot. Moreover, the constraints (21d) model that the robot should maintain a distance of ri from the points
ˆxi for i = 1*,... ,s*. The initial distribution is the dirac distribution Px0 = δ¯x with ¯x = (10
0)
⊺
and the moments

$$\begin{pmatrix}\bar{\sigma}_{0}^{11}&\bar{\sigma}_{0}^{12}\\ \bar{\sigma}_{0}^{21}&\overline{{{\Sigma}}}_{0}^{22}\end{pmatrix}=\begin{pmatrix}1&\bar{x}^{\intercal}\\ \bar{x}&\bar{x}\bar{x}^{\intercal}\end{pmatrix}.$$
The cost reflects that the robot should reach (0
0)
⊺
.

The problem (21) is an instance of (2) for appropriate choices of Rt and Hti for t = 0*,... ,N* and i = 1*,... ,s*.

## A. Test 1

For a first test, we consider two constraints (21d) with

$${\begin{pmatrix}{\hat{x}}_{11}\\ {\hat{x}}_{12}\end{pmatrix}}={\begin{pmatrix}-7.5\\ 0.5\end{pmatrix}},\qquad\qquad{\begin{pmatrix}{\hat{x}}_{21}\\ {\hat{x}}_{22}\end{pmatrix}}={\begin{pmatrix}-2.5\\ -0.5\end{pmatrix}}$$
and r1 = r2 = 1. For these constraints, we map (21)
to the semi-definite program (10) and solve the latter to obtain a control policy (Put). We then simulate the closed loop of this policy with the dynamics (21b). Ten trajectories of this closed loop are depicted in Figure 1. As we can see, the trajectories are almost not distinguishable. Indeed, the solution of this problem is an (almost) deterministic policy. The constraints are then also satisfied deterministically.

Note that we have chosen ε = 0.1 in (21d) to create a visible margin between the areas to be avoided and the trajectory. The code for this example can be accessed via https://github.com/SphinxDG/MomentRelaxationsControllerSyn Assuming that we wish to satisfy the constraints (21d)
deterministically, we can consider this first example as a case where the relaxation works well. Unfortunately, there are also cases, where the controller is not deterministic and constraints are not deterministically satisfied.

## B. Test 2

In a second test, we consider one constraint (21d) with
ˆx1 = (ˆx11
ˆx12) = (−5
0) and r1 = 1, i.e., the area to be avoided is exactly in between the starting position of our system and the desired target.

If we solve the control problem (21) for this constraint, we obtain closed-loop trajectories resembling the ten trajectories depicted in Figure 2. This scenario presents a significantly different case compared to the previous example. The variance in the trajectories highlights that the policy is stochastic, and seven out of ten trajectories pass through the area to be avoided. If (21) results from the relaxation of a problem with hard constraints, then this example yields an inexact relaxation. This behavior is feasible for the control problem (21), since we are optimizing over stochastic policies and impose only expectation constraints. Hence, we see that the solution of (2) can yield a stochastic policy if (2) includes nonconvex costs or constraints. Moreover, in the stochastic case, some or even all of the trajectories sampled from the closed loop can violate the constraints. We mention that the situation of an *obstacle* exactly in between a robot and a target is sometimes considered to be especially challenging since avoiding the obstacle by going to the left or going to the right seems equally preferable; consider, e.g., the elaboration on indecision in [4], where avoidance strategies are examined just for this scenario. Incidentally, the solution to the current example becomes deterministic if perturbing ˆx1 by a tiny amount in the x2
direction.

Of course, this example shows that caution is required when using such a relaxation in practice. For non-convex problems, we cannot rely on obtaining a deterministic solution. For problems with soft constraints, the risk of a stochastic solution may be acceptable if the latter occurs rarely. For problems with hard constraints, as in obstacle avoidance, the risk may not be acceptable. Nevertheless, we believe that the methodology presented here may be useful for the iterative solution of such problems, e.g., for the initialization of solvers.

## Vii. Example: Fixed-Point Escape

A first example of the flexibility of the moment matrix approach to (11) that resembles obstacle avoidance is given in Section VI. As a second example, we now consider the swing up of an inverted pendulum. The dynamics of an inverted pendulum can be described by the system of nonlinear differential equations [13]

$$\begin{pmatrix}\dot{x}_{1}\\ \dot{x}_{2}\\ \dot{x}_{3}\\ \dot{x}_{4}\end{pmatrix}=\begin{array}{c}x_{3}\\ x_{4}\\ \frac{m_{2}lx_{4}^{2}\sin x_{2}-m_{2}g\sin x_{2}\cos x_{2}+u}{m_{1}+(\sin x_{2})^{2}m}\\ \frac{(m_{2}lx_{4}^{2}\cos x_{2}-(m_{1}+m_{2})g)\sin x_{2}-(l\cos x_{2})u}{l(m_{1}+(\sin x_{2})^{2}m_{2})}\end{array}.\tag{22}$$
In this system of equations, g = 9.81 is the gravitational acceleration and m1 = 1 is the mass of a cart on which a pendulum with mass m2 = 10−3 rests. The input u is a force acting on the cart. The state x1 is the position of the cart, x2 is the angle of the pendulum, and x3 and x4
are the respective velocity and angular velocity.

To solve the swing up task, we design a controller that swings the pendulum high enough to reach the region of attraction of a second linear controller that stabilizes the upper pendulum position. The controller that makes the pendulum *escape* from the lower equilibrium is obtained as the solution to the control problem

$$\begin{array}{ll}\mbox{minimize}&\lim_{N\to\infty}\frac{1}{N}\mathbb{E}\sum_{t=0}^{N-1}\left(x_{1t}^{2}+x_{3t}^{2}-10^{4}e(x_{2t},x_{4t})+u_{t}^{2}\right)\\ \mbox{s.t.}&x_{1t+1}=x_{1t}+hx_{3t},\\ &x_{2t+1}=x_{2t}+hx_{4t},\\ &x_{3t+1}=x_{3t}-h\frac{mg}{m_{1}}x_{2t}+h\frac{1}{m_{2}}u,\\ &x_{4t+1}=x_{4t}-h\frac{(m_{1}+m_{2})g}{lm_{2}}x_{2t}+h\frac{l}{m_{1}}u,\\ &\mathbb{E}e(x_{2t},x_{4t})\leq e(2,0),\\ &\mathbb{E}u_{t}^{2}-\mathbb{E}u_{t}x_{t}^{\top}(\mathbb{E}x_{t}x_{t}^{\top})^{-1}\mathbb{E}x_{t}u_{t}\geq10^{4}h,\end{array}\tag{23a}$$
which is (almost) an instance of the infinite-horizon design problem (11). The dynamic constraint of this control problem is obtained from a linearization of (22) in the lower equilibrium and a subsequent Euler discretization. Unlike (11), this problem incorporates the additional constraint (23b), which ensures that the designed control policy excites the pendulum sufficiently. Without this constraint, the optimal solution of the above problem would yield the zero policy. Fortunately, this constraint can be convexified in Σ using the Schur complement.

We also highlight the term e(x2t,x4t) =
1
2*mglx*2
2t +
1
2gl2x2
4t which enters negatively into the cost. This term is a quadratic approximation of the pendulum energy mgl(1 − cos(x2t)) + 1
2gl2x2
4t making sure that the control policy pursues the goal of increasing the energy of the pendulum. Note that once the pendulum is supplied with enough energy, it will eventually reach the upper position. The energy constraint (23a) caps the average pendulum energy to the value of the potential energy of a pendulum at an angle of 2rad ≈ 115○ preventing the pendulum energy from going to infinity.

Two exemplary closed loop trajectories of the proposed control policy with the nonlinear pendulum model (22) are depicted in Figure 3 and Figure 4. First, the policy for the escape from the lower equilibrium is active and supplies the pendulum with energy. Then, the pendulum reaches the region of attraction of a second controller and is stabilized in the upward position. The moment for the switching of control policies is determined based on a Laypunov function for the second controller.

The presented control strategy for the swing up of an inverted pendulum stands out by being composed of two linear controllers. This means that we can take advantage of the extensive possibilities for tuning linear controllers.

For example, we can add additional constraints to the optimal control problem, such as restrictions on the position and speed of the cart. We also have the possibility of including a frequency-dependent cost in the optimization problem [22]. This allows us to put a penalty on high frequency control inputs. Finally, we mention that the controller in the form of two linear controllers requires only minimal online computation.

VIII. Conclusion We present a convexification strategy for linear state feedback synthesis problems with affine, time-varying system dynamics, random initial state, and additive stochastic noise. This convexification is based on moment matrices and permits for non-convex quadratic costs and constraints. Like second-order moment relaxations in non-convex quadratic programming, the case we study always permits for the extraction of a *solution*, which is actually optimal if we relax hard constraints to expectation constraints. In addition, we identify the parameters of known convexification strategies based on the dualization lemma with blocks of our moment matrices. Hence, we interpret the new decision variables after applying the dualization lemma as moment variables.

References
[1] B. Bamieh. Linear-quadratic problems in systems and controls via
covariance representations and linear-conic duality: Finite-horizon
case. *arXiv preprint arXiv:2401.01422*, 2024.
[2] S. Boyd, V. Balakrishnan, E. Feron, and L. ElGhaoui.
Control
system analysis and synthesis via linear matrix inequalities.
In
1993 American Control Conference, pages 2147–2154, 1993.
[3] S. Boyd, L. El Ghaoui, E. Feron, and V. Balakrishnan.
Linear
matrix inequalities in system and control theory. SIAM, 1994.
[4] C. Cathcart, M. Santos, S. Park, and N. E. Leonard. Proactive
opinion-driven robot navigation around human movers, 2023.
[5] V. Causevic, P. U. Abara, and S. Hirche.
Optimal powerconstrained control of distributed systems with information constraints. *Asian Journal of Control*, 24(5):2049–2061, 2022.
[6] P. Gahinet and P. Apkarian. A linear matrix inequality approach to
H∞ control. *International journal of robust and nonlinear control*,
4(4):421–448, 1994.
[7] A. Gattami. Generalized linear quadratic control. IEEE Transactions on Automatic Control, 55(1):131–136, 2009.
[8] A. Gattami and B. Bamieh. Simple covariance approach to H∞-
analysis.
IEEE Transactions on Automatic Control, 61(3):789–
794, 2015.
[9] F. Holtorf and C. Rackauckas. Stochastic optimal control via local
occupation measures. *arXiv preprint arXiv:2211.15652*, 2022.
[10] R. A. Howard. Dynamic Probabilistic Systems, Volume I: Markov
Models, volume 1. Courier Corporation, 2012.
[11] R. Kalman.
On the general theory of control systems.
IFAC
Proceedings Volumes, 1(1):491–502, 1960. 1st International IFAC
Congress on Automatic and Remote Control, Moscow, USSR, 1960.
[12] M. Kamgarpour and T. Summers. On infinite dimensional linear
programming approach to stochastic control. *IFAC-PapersOnLine*,
50(1):6148–6153, 2017.
[13] H. K. Khalil. *Control of nonlinear systems*. Prentice Hall, New
York, NY, 2002.
[14] J. B. Lasserre, D. Henrion, C. Prieur, and E. Trélat. Nonlinear optimal control via occupation measures and lmi-relaxations. SIAM journal on control and optimization, 47(4):1643–1666, 2008.
[15] D. Lee.
Multi-objective lqg design with primal-dual method.
Mathematics, 11(8):1857, 2023.
[16] J.
Park
and
S.
Boyd.
General
heuristics
for
nonconvex
quadratically constrained quadratic programming. arXiv preprint arXiv:1703.07870, 2017.
[17] J. Pitman. Occupation measures for markov chains. Advances in
Applied Probability, 9(1):69–86, 1977.
[18] A. Rantzer. A dual to lyapunov's stability theorem. Systems &
Control Letters, 42(3):161–168, 2001.
[19] A. Rantzer.
Linear quadratic team theory revisited.
In 2006
American Control Conference, pages 5 pp.–, 2006.
[20] C. Scherer and S. Weiland. Linear matrix inequalities in control.
Lecture Notes, Dutch Institute for Systems and Control, Delft, The
Netherlands, 3(2), 2000.
[21] C. W. Scherer. Robust mixed control and linear parameter-varying
control with full block scalings.
In Advances in linear matrix
inequality methods in control, pages 187–207. SIAM, 2000.
[22] G. Stein and M. Athans. The LQG/LTR procedure for multivariable feedback control design.
IEEE Transactions on Automatic
Control, 32(2):105–114, 1987.
[23] U. Vaidya and P. G. Mehta.
Lyapunov measure for almost
everywhere stability. *IEEE Transactions on Automatic Control*,
53(1):307–323, 2008.
[24] H. J. van Waarde, J. Eising, H. L. Trentelman, and M. K. Camlibel.
Data informativity: A new perspective on data-driven analysis and
control. *IEEE Transactions on Automatic Control*, 65(11):4753–
4768, 2020.