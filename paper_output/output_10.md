# Event-Triggered Boundary Control Of Mixed-Autonomy Traffic

Yihuai Zhang, Huan Yu∗

  Abstract— Control problems of mixed-autonomy traffic sys-
tem consisting of both Human-driven Vehicles (HV) and Au-
tonomous Vehicles (AV) have gained increasing attention. This
paper is focused on suppressing traffic oscillations of the mixed-
autonomy traffic system using boundary control design. The
mixed traffic dynamics are described by a 4 × 4 hyperbolic
partial differential equations (PDE) which governs propagation
of four properties in traffic including density of HV, density
of AV, friction between two classes of vehicles from driving
interactions, and averaged velocity. We propose event-triggered
boundary control design since control signal of traffic light
on ramp or varying speed limit cannot be updated in a
continuous time fashion. We apply event-triggered mechanism
for a PDE backstepping controller and obtain dynamic trig-
gering condition. Lyapunov analysis is conducted to prove the
exponential stability of the closed loop system with the event-
triggered controller. Numerical simulation demonstrates how
car-following spacing of AV affects event-triggering mechanism
of control input in mixed-autonomy traffic.

I. INTRODUCTION
Various boundary control designs have been studied for suppression of freeway traffic congestion [15]. The practical implementation of boundary control signal is via traffic light on ramp and varying speed limit (VSL). With the fast development of autonomous driving technology, the penetration of autonomous vehicles (AV) in traffic has increased over the past years, leading to a mixed-autonomy traffic system consisting of both human-driving vehicles (HV) and AV. Traffic oscillations could be induced due to car-following and lane-changing interactions between AV and HV. The design of boundary control strategies for mixed autonomy traffic remains an open question.

Event-based control is a computer control strategy which aims to improve efficiency of a system by updating the controller aperiodically. It needs to define a triggering condition for the system to determine the time instant that the controller need to be updated. The triggering condition can be both static and dynamic [16], [6]. Event-triggered control for hyperbolic PDEs was first developed by Espitia [4]. A continuous control input that can stabilize the system is first developed with an event-triggered mechanism embedded in the system. The event-triggered mechanism is executed based on the system states and the state describing the dynamics of the mechanism. Then the event-triggered control input that can also stabilize the system is obtained through the mechanism. With applications in traffic, Yu [18] first got the

results for stabilizing the traffic oscillations using backstep-
ping method with both theoretical guarantee and application
possibility. The author in [3] developed the event-triggered
output-feedback controller for cascaded roads. The event-
triggered boundary controller created a more realistic setting
to implement for traffic management system. Event-triggered
control has gain a lot of interests due to its efficient way to
use communication and computational resources by updating
the control value aperiodically.
  The traffic dynamics for pure HV traffic are described by
hyperbolic PDEs such as first-order Lighthill and Whitham
and Richard (LWR) model [11], [14], and the second-order
Aw-Rascle-Zhang (ARZ) model [1], [19]. They are both
continuous traffic models. Backstepping boundary control
has been developed for the ARZ model [18], [17], [3].
Besides backstepping control method, feedback control [10],
[20], optimal control [7], [8] can be also applied for boundary
stabilization of traffic PDE models. Boundary control input
is implemented by manipulating red-green phase of traffic
lights on ramp and velocity display of VSL. The continuous
control input is needed to update periodically at each time
step which makes it hard to implement. Some work built
on emulation of ramp metering controllers for discrete-time
traffic system and designed discrete control law. The au-
thor in [13] proposed a hierarchical centralized/decentralized
event-triggered control method for multi-class traffic net-
works modeled by METANET to reduce the computation
and communication load. Ferrara [5] introduced the event-
triggered model predictive schemes of discrete model for
freeway traffic control.The event-triggered MPC triggering
condition is a simple logic rule and is only for the discretized
model. However, previous results for mitigating traffic con-
gestion are mainly focused on traffic consisiting only HV. For
the mixed-autonomy traffic, interactive driving behaviors of
AV and HV on the road can make boundary control problem
more challenging. Mohan [12] proposed a two-class traffic
PDE model by introducing the concept of area occupancy to
capture interactions between different classes. Burkhardt [2]
adopted the two-class traffic PDE model and developed an
output-feedback boundary controller using the backstepping
method to get exponential stable results in L2-sense. In this
paper, we proposed the event-triggered control method for
the mixed-autonomy traffic system.
  The main contributions of this paper lie in two parts: On
the one hand, we first propose the event-triggered controller
for the mixed-autonomy traffic system modeled by an ex-
tended ARZ model and provide the theoretical guarantee
using Lyapunov analysis. On the application side, the results
can be applied to traffic management systems to reduce

computational resources and improve the efficiency of the
traffic system. It paves the way for traffic management.
  The paper is organized as follows. Section 2 introduces
the mixed-autonomy traffic system using the extened-ARZ
model. In Section 3, the boundary control model is derived
and the backstepping controller with a continuous version
is proposed. In Sections 4, the dynamic event-triggered
condition is given and thus the event-triggered boundary con-
troller is developed then the Lyapunov analysis is conducted
to analyze the stability of the closed-loop system. Section
5 provides the numerical simulation results to verify the
theoretical results. Section 6 goes to the conclusion.

## Ii. Mixed-Autonomy Traffic Pde Model

Motivated by the two-class extended ARZ PDE model [2], the mixed-autonomy traffic consisting of HV and AV is proposed as

$$\partial_{t}\rho_{\rm h}+\partial_{x}\left(\rho_{\rm h}v_{\rm h}\right)=0,\tag{1}$$

$$\partial_{t}\left(v_{\rm h}-V_{e,\rm h}\right)+v_{\rm h}\partial_{x}\left(v_{\rm h}-V_{e,\rm h}\right)=\frac{V_{e,\rm h}-v_{\rm h}}{\tau_{\rm h}},\tag{2}$$

$$\partial_{t}\rho_{\rm a}+\partial_{x}\left(\rho_{\rm a}v_{\rm a}\right)=0,\tag{3}$$

$$\partial_{t}\left(v_{\rm a}-V_{e,\rm a}\right)+v_{\rm a}\partial_{x}\left(v_{\rm a}-V_{e,\rm a}\right)=\frac{V_{e,\rm a}-v_{\rm a}}{\tau_{\rm a}},\tag{4}$$
ρh(*x, t*) and ρa(*x, t*) are the traffic densities of HV and AV, vh(x, t), va(*x, t*) are the traffic velocities of HV and AV. The boundary conditions are set as

$$\rho_{\rm h}(0,t)=\rho_{\rm h}^{\star},\tag{5}$$ $$\rho_{\rm a}(0,t)=\rho_{\rm a}^{\star},$$ (6) $$\rho_{\rm h}(0,t)v_{\rm h}(0,t)+\rho_{\rm a}(0,t)v_{\rm a}(0,t)=\rho_{\rm h}^{\star}v_{\rm h}^{\star}+\rho_{\rm a}^{\star}v_{\rm a}^{\star},$$ (7) $$\rho_{\rm h}(L,t)v_{\rm h}(L,t)+\rho_{\rm a}(L,t)v_{\rm a}(L,t)=q_{\rm h}^{\star}+q_{\rm a}^{\star}+U(t),\tag{8}$$

where the spatial and time domain is defined as (x, t) ∈
[0, L] × R+, ρ⋆
             h, ρ⋆
                 a are the equilibrium densities, and v⋆
                                                     h,
v⋆
 a are the equilibrium speed. We will design event-triggered
boundary controller boundary control signal of ramp meter-
ing or VSL. We define the area occupancy AO to describe the
interaction between the two-class vehicles on the road [2],
[12]

$$AO(\rho_{\rm h},\rho_{\rm a})=\frac{a_{\rm h}\rho_{\rm h}+a_{\rm a}\rho_{\rm a}}{W},\tag{9}$$
where W is the road width. The impact area for HV ah and AV aa can be described as:

$a_{\rm h}=d\times(l+s_{\rm h})$ (10) $a_{\rm a}=d\times(l+s_{\rm a})$ (11)
where d is the vehicle width, l is the vehicle length. We assume that the vehicle width and length are the same. sh is the car-following gap of HV, sa is the car-following gap of AV. The fundamental diagram based on the area occupancy is introduced for velocity-density equilibrium relation as:

$$\mathrm{c}_{\mathrm{t}}^{\mathrm{o}}=V_{\mathrm{o,i}}(\rho_{\mathrm{m},\mathrm{p},\mathrm{i}})=V_{\mathrm{b}}\left(1-\left(\frac{\Delta Q}{\Delta Q_{\mathrm{i}}}\right)^{\mathrm{o}}\right)\tag{13}$$
where Vh, Va are the maximum speed, AOh, AOa are the maximum area occupancy, γh, γa are the traffic pressure exponent.

Compared with HV, AV tends to have a larger spacing due to the conservative driving strategies they equipped. A larger spacing leads to a larger impact area, inducing the "creeping effect" on the road that HV can take over AV in congested regimes.

## Iii. Backstepping Control Design A. Boundary Control Model

  Linearizing the system at its equilibrium point ρ⋆
                                                   h, ρ⋆
                                                       a, v⋆
                                                           h,
v⋆
 a and defining a small deviation ˜ρh(x, t) = ρh(x, t) − ρ⋆
                                                           h,
˜vh(x, t) = vh(x, t) − v⋆
                      h, ˜ρa(x, t) = ρa(x, t) − ρ⋆
                                                a, ˜va(x, t) =
va(x, t) − v⋆
             a. Writing the system in a augmented ex-
pression z(x, t) =
                   �˜ρh(x, t)
                              ˜vh(x, t)
                                        ˜ρa(x, t)
                                                  ˜va(x, t)�T

Defining the matrix V
                        =
                           {ˆvij}1≤i,j≤4 such that the
coefficient matrix can be diagonalized as V−1JλV =
Diag{λ1, λ2, λ3, λ4}, with positive eigenvalues in ascending
order. We also define the source term matrix as ˆJ =
V−1JV = { ˆJij}1≤i,j≤4. The transformation matrix T is
given as

0 e − ˆ J22 v∗a x 0 0   0 0 e− ˆ J33 λ3 x 0 T =   e − ˆ J11 v∗ h x 0 0 0 T− 0 0 0 e− ˆ J44 λ4 x  =  T+   V−1 (14)

where T+ ∈ R3×4 and T− ∈ R1×4. The change of
coordinates is
            �w1
                  w2
                      w3
                           w4
                             �T = Tz.
                                              (15)

Then we perform Riemann transformation of the linarized
system, thus we get

w+ t (*x, t*) + Λ+w+ x (*x, t*) =Σ++(x)w+(*x, t*) + Σ+−(x)w−(x, t), (16) w− t (x, t) − Λ−w− x (*x, t*) =Σ−+(x)w+(x, t), (17) w+(0, t) = Qw−(0, t), (18) w−(*L, t*) = Rw+(*L, t*) + ¯U(t), (19)

where w+ = [w1, w2, w3]T, w− = w4. The coefficient
matrices are given as Λ+ = Diag{λ1, λ2, λ3}, Λ− = −λ4,
Σ++(x), Σ+−(x), Σ−+(x), Q, and R are coefficients which
can be obtained through Riemann transformation. The details
of the coefficients can be found in [2]. Also, ¯U(t) =

e−
   ˆ
  J44
   λ4 L 1

      κ4 U(t), κj = v∗
                    hˆv1j + ρ∗
                            hˆv2j + v∗
                                    aˆv3j + ρ∗
                                            aˆv4j, j =
1, 2, 3, 4.

## B. Free/Congestion Analysis

It was shown that the eigenvalues satisfying the following condition [21]

$$\lambda_{4}\leq\min\{\lambda_{1},\lambda_{3}\}\leq\lambda_{2}\leq\max\{\lambda_{1},\lambda_{3}\}.\tag{20}$$

The traffic system can be divided into free and congested regime based on the propagation direction of traffic waves.

- Free regime: the four eigenvalues λ1 > 0, λ2 > 0, λ3 >
0, λ4 > 0. Traffic oscillations transport downstream at
corresponding speed λ1, λ2, λ3, λ4. Vehicles can run
at their maximum speeds.
- Congested regime: λ1 > 0, λ2 > 0, λ3 > 0, λ4 < 0. In
the congested regime, the traffic information propagates from downstream to upstream, the efficiency of the traffic system becomes low.

## C. Backstepping Transformation And Controller Design

We consider the stabilization of the close-loop system (16)-(19) with continuous control input at each time step. Defining the backstepping transformation:

$$\mathcal{K}\mathbf{w}=\begin{pmatrix}\mathbf{w}^{+}\\ \mathbf{w}^{-}-\int_{0}^{x}\mathbf{K}(x,\xi)\mathbf{w}^{+}(\xi,t)+M(x,\xi)\mathbf{w}^{-}(\xi,t)d\xi\end{pmatrix}\tag{21}$$

where $\mathbf{w}=[\mathbf{w}^{+},\mathbf{w}^{-}]$ and the backstepping control kernel $\mathbf{K}(x,\xi)\in\mathbb{R}^{3}$, $M(x,\xi)\in\mathbb{R}^{1}$ are defined as

$$\mathbf{K}(x,\xi)=\left[\begin{array}{cc}k_{1}(x,\xi)&k_{2}(x,\xi)&k_{3}(x,\xi)\end{array}\right]\tag{22}$$

Both kernels are defined on the triangular domain $\mathcal{T}=\{0\leq\xi\leq x\leq L\}$. And the target perturbed system is

$$\alpha_{t}(x,t)+\Lambda^{+}\alpha_{x}(x,t)=\Sigma^{++}(x)\alpha(x,t)+\Sigma^{+-}(x)\beta(x,t)$$ $$+\int_{0}^{x}\mathbf{C}^{+}(x,\xi)\alpha(\xi,t)d\xi+\int_{0}^{x}\mathbf{C}^{-}(x,\xi)\beta(\xi,t)d\xi,\tag{23}$$ $$\beta_{t}\left(x,t\right)-\Lambda^{-}\beta_{x}(x,t)=0,$$ (24) $$\alpha(0,t)=Q\beta(0,t)$$ (25) $$\beta(L,t)=0\tag{26}$$
where α = [α1, α2, α3]T The coefficients C+(*x, ξ*) ∈ R3×3

and C−(x, ξ) ∈ R3×1 are defined on the same triangular
domain T . The kernel equations are stated in [2] and the
well-posedness of the target system and kernel equations are
proved in [9], [22]. The control input is given as

$$\bar{U}(t)=\int_{0}^{L}\left({\bf K}(L,\xi){\bf w}^{+}(\xi,t)+M(L,\xi){\bf w}^{-}(\xi,t)\right)d\xi.$$ $$\qquad-R{\bf w}^{+}(L,t)\tag{27}$$

## D. Inverse Transformation

The transformation (21) is invertible such that the target system share the same properties with the original system. The inverse transformation turn the target system (23)-(26) into the original system (16)-(19):

$$\mathcal{L}\vartheta=\begin{pmatrix}\alpha\\ \beta-\int_{0}^{x}(\mathbf{L}(x,\xi)\alpha(\xi,t)+N(x,\xi)\beta(\xi,t))d\xi\end{pmatrix}\tag{28}$$
where ϑ = [α1, α2, α3, β]T and L(x, ξ) ∈ R3, N(*x, ξ*) ∈ R1
are definied as

$${\bf L}(x,\xi)=\left[\ell_{1}(x,\xi)\quad\ell_{2}(x,\xi)\quad\ell_{3}(x,\xi)\right]\tag{29}$$

The inverse kernels are also defined on the same triangular domain ${\cal T}$. The inverse kernel equations can be easily got in [9]. The states ${\bf w}$ and $\vartheta$ have equivalent $L_{2}$ norms, i.e. there exist two constants $p_{1}>0$ and $p_{2}>0$ such that

$$p_{1}\|{\bf w}\|_{L^{2}}^{2}\leq\|\vartheta\|_{L^{2}}^{2}\leq p_{2}\|{\bf w}\|_{L^{2}}^{2}.\tag{30}$$
where ϑ = (α1, α2, α3, β). The continuous-time control input ¯U(t) can be calculated using states (*α, β*) of target system:

$$\bar{U}(t)=\int_{0}^{L}({\bf L}(L,\xi)\alpha(\xi,t)+N(L,\xi)\beta(\xi,t))d\xi\tag{31}$$ $$-R{\bf w}^{+}(L,t)$$

## Iv. Event-Triggered Boundary Control

  In this section, we introduce event-triggered conditions
for the traffic system which gives the time instant that the
controller should update and then ensure the exponential
stability of the close-loop system.
  First, we consider the stabilization of the closed-loop sys-
tem on events while sampling the continuous-time controller
¯U(t) at certain sequence of time instants and it is updated
when the triggering conditions are verified. Then we redefine
the boundary control input in (19),

$$\mathbf{w}^{-}(L,t)=R\mathbf{w}^{+}(L,t)+\bar{U}_{d}(t)\tag{32}$$

where $\bar{U}_{d}(t)=\bar{U}(t)+d(t)$, $\forall t\in[t_{k},t_{k+1}),k>0$. And the $d(t)$ is the deviation of the theoretical control input and the event-triggered control input. And we can get the sampled control law as

$$\bar{U}_{d}(t)=\int_{0}^{L}(\mathbf{L}(L,\xi)\alpha(\xi,t_{k})+N(L,\xi)\beta(\xi,t_{k}))d\xi$$ $$\quad-R\mathbf{w}^{+}(L,t_{k})\tag{33}$$
thus we get the actuation deviation d(t)

$$d(t)=-\,R({\bf w}^{+}(L,t_{k})-{\bf w}^{+}(L,t))$$ $$+\int_{0}^{L}\bigg{(}{\bf L}(L,\xi)(\alpha(\xi,t_{k})-\alpha(\xi,t))$$ $$+\,N(L,\xi)(\beta(\xi,t_{k})-\beta(\xi,t)\bigg{)}d\xi\tag{34}$$
Applying the sampled control law ¯Ud(t) to the system (16)
- (19), we get the pertubed target system

$$\alpha_{t}(x,t)+\Lambda^{+}\alpha_{x}(x,t)=\Sigma^{++}(x)\alpha(x,t)+\Sigma^{+-}(x)\beta(x,t)$$ $$+\int_{0}^{x}{\bf C}^{+}(x,\xi)\alpha(\xi,t)d\xi+\int_{0}^{x}{\bf C}^{-}(x,\xi)\beta(\xi,t)d\xi,\tag{35}$$ $$\beta_{t}\left(x,t\right)-\Lambda^{-}\beta_{x}(x,t)=0,$$ (36) $$\alpha(0,t)=Q\beta(0,t),$$ (37) $$\beta(L,t)=d(t).\tag{38}$$
Using the comparison principle, we have We consider a triggering condition relies on the evolution of d(t) and the following Lyapunov function,

$m(t)\leq0,\forall t\geq0,$ (45)
this finishes the proof of Lemma 2.

$$V(t)=\int_{0}^{L}\sum_{i=1}^{3}\frac{A_{i}}{\lambda_{i}}\mathrm{e}^{-\frac{\mu x}{\lambda_{i}}}\alpha_{i}^{2}(x,t)+\frac{B}{\Lambda^{-}}\mathrm{e}^{\frac{\mu x}{\Lambda^{-}}}\beta^{2}(x,t)dx\tag{39}$$
We also have the following lemma for the boundness of the actuation deviation d(t).

**Lemma 3**.: _There exists $\epsilon_{i}>0,i\in\{1,2,3\}$, $\phi_{1}$ and $\phi_{2}>0$, for the $d(t)$ introduced in (34) with $t\in(t_{k},t_{k+1})$, such that_
where the constant coefficients A1, A2, A3, B and µ are positive. The Lyapunov candidate is equivalent to the L2
norm of the state ϑ, therefore, there exist two constants p3 > 0 and p4 > 0 such that

$$d^{2}(t)\leq\sum_{i=1}^{3}\epsilon_{i}\alpha_{i}^{2}(L,t)+\phi_{1}d^{2}(t)+\phi_{2}V(t).\tag{46}$$

## A. Dynamic Triggering Condition

Proof. Taking time derivative of d(t), we have

$$\dot{d}(t)=-\int_{0}^{L}{\bf L}(L,\xi)\alpha_{t}(\xi,t)+N(L,\xi)\beta_{t}(\xi,t)d\xi.\tag{47}$$
We define the event-triggered mechanism (ETM) using the dynamic triggering condition which can be derived by the evolution of the controller deviation (34) and another dynamic variable m(t).

Using the dynamics of the perturbed target system in (35) - (38) and integrating by parts, we get

$\begin{array}{l}\dot{d}(t)=\mathbf{L}(L,L)\Lambda^+\alpha(L,t)-N(L,L)\Lambda^-\beta(L,t)\\ \quad+\left(N(L,0)\Lambda^--\mathbf{L}(L,0)\Lambda^+Q\right)\beta(0,t)\\ \quad-\int_{-L}^L\mathbf{L}_\xi(L,\xi)\Lambda^+\alpha(\xi,t)d\xi+\int_{-L}^L N_\xi(\end{array}$

Definition 1. Let the Lyapunov candidate V (t) be given
by (39). The event-triggered controller is defined in (33)
with a dynamic event-triggered mechanism. The time of the
execution tk ≥ 0 from t0 = 0 in a finite number set of times.
The set is determined by:

$$-\int_{0}^{L}{\bf L}_{\xi}(L,\xi)\Lambda^{+}\alpha(\xi,t)d\xi+\int_{0}^{L}N_{\xi}(L,\xi)\Lambda^{-}\beta(\xi,t)d\xi$$
- if {*t > t*k ∧ ζBe
µL
Λ− d2(t) ≥ ζµσV (t) − m(t)} = ∅,
then the set of the times of the events is { t0, . . . , tk}.
$$-\int_{0}^{L}\mathbf{L}(L,\xi)\Sigma^{++}(\xi)\mathbf{w}^{+}(\xi,t)d\xi$$
- if {*t > t*k ∧ ζBe
$$-\int_{0}^{L}{\bf L}(L,\xi)\Sigma^{+-}(\xi){\bf w}^{-}(\xi,t)d\xi.\tag{48}$$
µL
Λ− d2(t) ≥ ζµσV (t) − m(t)} ̸= ∅,
then the next execution time is determined by: tk+1 =
inf{*t > t*k ∧ Be
µL
Λ− d2(t) ≥ ζµσV (t) − m(t)}, where m(t) satisfies the ordinary differential equation,

$$\dot{m}(t)=-\eta m(t)+B\mathrm{e}^{\frac{\eta\,k}{\hbar}}\dot{a}^{2}(t)-\sigma\mu V(t)$$ $$-\sum_{i=1}^{3}\varsigma_{i}\alpha_{i}^{2}(L,t)-\varsigma_{i}\beta^{2}(0,t),\tag{41}$$

where $\varsigma>0$, $\mu>0$, $\sigma>0$, $\varsigma_{i}>0$, $i\in\{1,2,3,4\}$, $\eta>0$ and $m(0)=m^{0}$.

Taking the square of $\dot{a}(t)$, combining Young's inequality, we have

$$\dot{a}^{2}(t)\leq2(\mathbf{L}(L,L)\Lambda^{+}\alpha(L,t)-N(L,L)\Lambda^{-}\beta(L,t))^{2}$$ $$+2\left(-\int_{0}^{L}\mathbf{L}(\xi,t)\Lambda^{+}\alpha(\xi,t)-N_{\xi}(L,\xi)\Lambda^{-}\beta(\xi,t)d\xi\right.$$ $$-\int_{0}^{L}\mathbf{L}(\xi,\xi)\Sigma^{++}(\xi)\mathbf{w}^{+}(\xi,t)d\xi$$
Based on the definition 1, we have the following result for m(t).

$$-\int_{0}^{L}{\bf L}(L,\xi)\Sigma^{+-}(\xi){\bf w}^{-}(\xi,t)d\xi\Bigg{)}^{2}.\tag{49}$$
Using Cauchy-Schwarz inequality, we get Lemma 2. Under the ETM in Definition 1, it holds that
ζBe
µL
Λ− d2(t) − *ζµσV* (t) + m(t) ≤ 0 *with* m(t) ≤ 0

$$\dot{d}^{2}(t)\leq8\sum_{i=1}\ell_{i}^{2}(L,L)\lambda_{i}^{2}\alpha_{i}^{2}(L,t)$$
Proof. We already know the ETM in Definition 1. It holds that the system in the simulation period always guarantee the following condition,

$$\sum_{t=1}^{3}$$ $$+8N^{2}(L,L)(\Lambda^{-})^{2}\beta^{2}(L,t)+\frac{8}{p_{3}}c_{1}V(t)+\frac{8}{p_{1}p_{3}}c_{2}V(t)$$
We have the result

$$\leq8\sum_{t=1}^{3}\ell_{t}^{2}(L,L)\lambda_{t}^{2}\sigma_{t}^{2}(L,t)+8N^{2}(L,L)(\Lambda^{-})^{2}d^{2}(t)$$ $$+\frac{8}{p_{3}}\left(c_{1}+\frac{c_{2}}{p_{1}}\right)V(t),\tag{50}$$
using (41), we get

˙m(t) *≤ −*ηm − 1 ζ m(t) − i=1 ςiα2 i (L, t) − ς4β2(0, t). (44) 3 �

where
        c1
             =
                  max{
                       � L
                        0
                             (Lξ(L, ξ)Λ+)2dξ,
                                               � L
                                                0
(Nξ(L, ξ)Λ−)2dξ}
                 c2
                     =
                        max{
                             � L
                              0 (L(L, ξ)Σ++(ξ))2dξ,
� L
0 (L(L, ξ)Σ+−(ξ))2dξ}.
                        And
                              thus
                                    we
                                         get
                                               that

ϵi = 8ℓ2
        i (L, L)λi, i ∈ {1, 2, 3}, ϕ1 = 8N 2(L, L)(Λ−)2,
ϕ2 =
       8
       p3

p1

             �
              . This concludes the proof of Lemma
3.

�
 c1 + c2

## B. Avoidance Of Zeno Phenomenon

  Under the dynamic event triggering condition, the Zeno
phenomenon should be avoided. In this section, we prove
the dynamic event triggering condition for the system (16)
- (19) avoids the Zeno phenomenon. We have the following
theorem.

Theorem 4. There exists a minimal dwell-time τ ⋆ > 0 be-
tween two adjacent triggering times, tk+1 − tk ≥ τ ⋆, k ≥ 0,
under the dynamic triggering condition in Definition 1 with
parameters ζ, µ, σ, ςi, i ∈ {1, 2, 3, 4}, η, ϵi, i ∈ {1, 2, 3}.
And the parameters satisfying:

$$\varsigma_{i}\geq\max\{\zeta Be^{\frac{\mu L}{\Lambda}}\epsilon_{i},\zeta\mu\epsilon_{i},i\in\{1,2,3\}\}\tag{51}$$

$$\varsigma_{4}\geq\max\{0,-2\zeta\mu(\sum A_{i}q_{i}^{2}-B),i\in\{1,2,3\}\tag{52}$$
Proof. We know from the Definition 1 that for all time t ≥ 0, all events are executed to guarantee

$$\zeta_{B}\frac{\mu^{L}}{\Lambda}\,d^{2}(t)\leq\zeta_{\mu\sigma}V(t)-m(t).\tag{53}$$
Then we define the following function

$$\Psi(t)=\frac{\zeta Be^{\frac{\mu L}{\Lambda}}d^{2}(t)+\frac{1}{2}m(t)}{\zeta\mu\sigma V-\frac{1}{2}m(t)}.\tag{54}$$
The function d(t) and V (t) are continuous on time interval
[tk, tk+1], so that the function Ψ(t) is also a continuous function at [tk, tk+1]. We can derive that there exists t′
k > tk such that ∀t ∈ [t′
k, tk+1], Ψ(t) ∈ [0, 1] using the intermediate value theorem. Taking time derivative to the function Ψ(t), we get

$$\dot{\Psi}(t)=\frac{2\zeta Be^{\frac{\mu L}{\Lambda^{-}}}d\dot{d}+\frac{1}{2}\dot{m}}{\zeta\mu\sigma V-\frac{1}{2}m}-\frac{\zeta\sigma\mu\sigma\dot{V}-\frac{1}{2}\dot{m}}{\zeta\mu\sigma V-\frac{1}{2}m}\Psi.\tag{55}$$
Using Young inequality, we have

$$\dot{\Psi}(t)\leq\frac{\zeta Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}}{\zeta\mu\sigma V-\frac{1}{2}m}+\frac{\zeta Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}}{\zeta\mu\sigma V-\frac{1}{2}m}$$ $$+\frac{\frac{1}{2}\left(-\eta m+Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}-\sigma\mu V\right)}{\zeta\sigma\mu V-\frac{1}{2}m}$$ $$+\frac{\frac{1}{2}\left(-\sum_{i=1}^{3}\varsigma_{i}\alpha_{i}^{2}(L,t)-\varsigma_{4}\beta^{2}(0,t)\right)}{\zeta\mu\sigma V-\frac{1}{2}m}-\frac{\zeta\mu\dot{V}\Psi}{\zeta\mu\sigma V-\frac{1}{2}m}$$ $$+\frac{\frac{1}{2}\left(-\eta m+Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}-\sigma\mu V\right)}{\zeta\mu\sigma V-\frac{1}{2}m}\Psi$$ $$+\frac{\frac{1}{2}\left(-\sum_{i=1}^{3}\varsigma_{i}\alpha_{i}^{2}(L,t)-\varsigma_{4}\beta^{2}(0,t)\right)}{\zeta\mu\sigma V-\frac{1}{2}m}\Psi.\tag{56}$$
As defined in (39), the time derivative of V (t) can be gotten by integrating by parts and using boundary conditions of perturbed target system. Thus the ˙V is given as

λi α2 i (*L, t*) + ( ˙V ≤ − i=1 Aie− µL i=1 Aiq2 i − B)β2(0, t) 3 � 3 � + Be µL Λ− d2(t) − (µ − γ)V, (57) where γ = 2A p3 min{λi}(maxx∈[0,L] ∥Σ++(x)∥ +(1 + 1 p1 ) maxx∈[0,L] ∥Σ+−(x)∥). ˙V ≤ − µL Λ− d2(t) − (µ − γ)V, i=1 α2 i (*L, t*) + β2(0, t) + Be 3 � (58)
Replacing ˙V and using (3), we have

2ς4)β2(0, t) 2m Ψ ˙Ψ(t) *≤ −*(ζµ(� Aiq2 i − B) + 1 ζµσV − 1 1 2ηm − 2m Ψ 2mΨ + �(ζµϵi − ςi)α2 i (*L, t*) ζµσV − 1 ζµσV − 1 2) 2µσ)V µL Λ− d2(−ζµσ + 1 + Be 2m Ψ + (ζµσ(µ − γ) − 1 2m Ψ ζµσV − 1 ζµσV − 1 µL Λ− (1 + ϕ1 + 1 2ζ )d2 + ζBe µL Λ− ϵi − ςi)α2 i (*L, t*) 2m 2m + �(ζBe ζµσV − 1 ζµσV − 1 2µσ)V 1 2ηm + (ζBe µL Λ− ϕ2 − 1 2m − ζµσV − 1 ζµσV − 1 2m − 1 2ς4β2(0, t) ζµσV − 1 2m (59)

## Choosing Σi ≥ Ζbe

Choosing $\varsigma_{i}\geq\zeta Be^{\frac{\mu L}{\Lambda^{-}}}\epsilon_{i}$ and $\varsigma_{i}\geq\zeta\mu\epsilon_{i}$, $i\in\{1,2,3\}$, $\varsigma_{4}>0$ and $\varsigma_{4}+2\zeta\mu(\sum A_{i}q_{i}^{2}-B)>0$, we get the following equation after simplification

$$\dot{\Psi}(t)\leq\frac{\zeta Be^{\frac{\mu L}{\Lambda^{-}}}(1+\phi_{1}+\frac{1}{2\zeta})d^{2}}{\zeta\mu\sigma V-\frac{1}{2}m}+\frac{(\zeta Be^{\frac{\mu L}{\Lambda^{-}}}\phi_{2}-\frac{1}{2}\mu\sigma)}{\zeta\mu\sigma}+\eta$$ $$+\frac{Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}(-\zeta\mu\sigma+\frac{1}{2})}{\zeta\mu\sigma V-\frac{1}{2}m}\Psi+\eta\Psi+\frac{(\zeta\mu\sigma(\mu-\gamma)-\frac{1}{2}\mu\sigma)}{\zeta\mu\sigma}\Psi\tag{60}$$
Rewriting the equation, thus it can be deduced that

$$\dot{\Psi}(t)\leq\frac{(\zeta Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}+\frac{1}{2}m-\frac{1}{2}m)(1+\phi_{1}+\frac{1}{2\zeta})}{\zeta\mu\sigma V-\frac{1}{2}m}$$ $$+\eta+\frac{(\zeta Be^{\frac{\mu L}{\Lambda^{-}}}d^{2}+\frac{1}{2}m-\frac{1}{2}m)(-\zeta\mu+\frac{1}{2})}{\zeta(\zeta\mu\sigma V-\frac{1}{2}m)}\Psi+\eta\Psi$$ $$+\frac{(\zeta\mu(\mu-\gamma)-\frac{1}{2}\mu\sigma)}{\zeta\mu\sigma}\Psi+\frac{(\zeta Be^{\frac{\mu L}{\Lambda^{-}}}\phi_{2}-\frac{1}{2}\mu)}{\zeta\mu\sigma}.\tag{61}$$

Rearranging the above equation, thus we have

$$\dot{\Psi}(t)\leq\left(\frac{-\zeta\mu+\frac{1}{2}}{\zeta}\right)\Psi^{2}+\left(1+\phi_{1}+\frac{1}{2\zeta}\right.$$ $$+\left.\frac{-\zeta\mu\sigma+\frac{1}{2}}{\zeta}+\eta+\frac{\zeta\mu\sigma(\mu-\gamma)-\frac{1}{2}\mu\sigma}{\zeta\mu\sigma}\right)\Psi$$ $$+\left(\frac{(\zeta Be^{\frac{\mu L}{\Lambda}}\phi_{2}-\frac{1}{2}\mu\sigma)}{\zeta\mu\sigma}+\eta+1+\phi_{1}+\frac{1}{2\zeta}\right).\tag{62}$$
Thus the Ψ(t) has the form

$\Psi(t)\leq\varphi_{1}\Psi^{2}(t)+\varphi_{2}\Psi(t)+\varphi_{3}$ (63)

where φ1 =
           1
           2ζ − µσ, φ = 1 + ϕ1 +
                                 1
                                2ζ (1 − σ)µ − γ + η,

$\varphi_{3}=\frac{B\,\mathrm{e}^{\frac{\mu L}{\Lambda}}\,\phi_{2}}{\mu\sigma}+1+\eta+\phi_{1}.$ Using the comparison principle, we get the time from $\Psi(t^{\prime}_{k})=0$ to $\Psi(t_{k+1})=1$ is at least

$$\tau^{\star}=\int_{0}^{L}\frac{1}{\varphi_{1}s^{2}+\varphi_{2}s+\varphi_{3}}ds.\tag{64}$$

Then, $t_{k+1}-t_{k}\geq t_{k+1}-t_{t^{\prime}_{k}}=\tau^{\star}.$ This finishes the proof of Theorem 4.

  Now that have proved that there exists a minimal dwell
time between two adjacent events. The Zeno phenomenon
is avoided. Based on the previous results, the exponential
stability of the system (16) - (19) with the event-triggered
controller (33) was obtained, as stated in Theorem 5.

**Theorem 5**.: _Let $A_{i}>0,i\in\{1,2,3\}$, $B>0$, $\zeta>0$, $\eta\in(0,1)$, $\varsigma_{i},i\in\{1,2,3,4\}\in(0,1)$ such that_

$$\varsigma_{i}-A_{i}{\rm e}^{-\frac{\mu L}{\lambda_{i}}}\leq0,i\in\{1,2,3\}\tag{65}$$ $$\varsigma_{4}+\sum_{i=1}^{3}A_{i}q_{i}^{2}-B\leq0,i\in\{1,2,3\}\tag{66}$$

_$V$ is given by (39) and $d$ is given by (34). The system (16)-(19) with the event-triggered controller (33) is exponential stable under the ETM in Definition 1._
Proof. We consider the following Lyapunov candidate for perturbed target system (35) - (38),

$$V_{d}(t,m)=V(t)-m(t)\tag{67}$$

Taking time derivative of the Lyapunov candidate, we get

$$\dot{V}_{d}(t,m)\leq Be^{\frac{\mu L}{\Lambda}}d^{2}(t)-(\mu-\gamma)V-\dot{m}(t)$$ $$\qquad-\sum_{i=1}^{3}A_{i}\mathrm{e}^{-\frac{\mu L}{\lambda_{i}}}\,\alpha_{i}^{2}(L,t)+(\sum_{i=1}^{3}A_{i}q_{i}^{2}-B)\beta^{2}(0,t),\tag{68}$$
taking into the expression of ˙m(t), we get

$$\dot{V}_{d}\leq-\,(\mu-\gamma)V+B\mathrm{e}^{\frac{\mu L}{\Lambda^{-}}}d^{2}(t)+\eta m+\mu\sigma V$$ $$\quad-B\mathrm{e}^{\frac{\mu L}{\Lambda^{-}}}d^{2}(t)+\sum_{i=1}^{3}(\varsigma_{i}-A_{i}\mathrm{e}^{-\frac{\mu L}{\lambda_{i}}})\alpha_{i}^{2}(L,t)$$ $$\quad+(\varsigma_{4}+\sum_{i=1}^{3}A_{i}q_{i}^{2}-B)\beta^{2}(0,t).\tag{69}$$

Simplifying the equation, thus 
˙Vd *≤ −*(µ(1 − σ) − γ)Vd + (η − (µ(1 − σ) − γ))m. (70)

$$\eta-(\rho(1-\sigma)-\gamma)\geq0,\ \text{we get}$$ $$\tilde{V}_{d}\leq-\rho((1-\sigma)-\gamma)V_{d}.\tag{71}$$
Using comparison principle again and m(0) = 0, thus

$$\dot{V}(t)\leq\mathrm{e}^{(-(\mu(1-\sigma)-\gamma)t)}V(0)\tag{72}$$

This concludes the proof of Theorem 5.

           V. NUMERICAL SIMULATION
 In this section, we provide the numerical simulation for the
closed-loop system with event-triggered controller. Taking
the equilibrium density as ρ⋆
                    h = 150veh/km, ρ⋆
                                  a = 75veh/km,
such that v⋆
         h = 29.16km/h, v⋆
                        a = 13.32veh/km can be
calculated by the fundamental diagram. The relaxation time
is set as τh = 30s, τa = 60s. The pressure exponent value
is selected as γh = 2.5, γa = 2. The car-following gap are
sh = 5m, sa = 16m. The maximum area occupancy AOh =
0.9, AOa = 0.85 In addition, we choose ζ = 8 × 10−3,
σ = 1 × 10−4, η = 0.9, A1 = 2 × 10−2, A2 = 3 × 10−3,
A3 = 4 × 10−3, B = 9 × 10−3, and we also choose
ϱ1 = 2×10−10, ϱ2 = 2×10−9, ϱ3 = 1.2×10−12, ς4 = 0.01,
µ = 5 × 10−4. We run the simulation on a L = 1000m long
road whose width is 6m and the simulation time is 450s.
 The closed-loop results of the mixed traffic system under
the event-triggered controller is shown in Fig. 1. Fig. 1a
represents the density and velocity of the HV while Fig.
1b denotes AV. It can be observed that the event-triggered
controller can stabilize the mixed-autonomy traffic system.
We also provide the comparison between the continuous
controller using backstepping method and the event-triggered
controller in Fig. 2a. The traffic management system do not
need to update the control input at each time-step by using
the event-triggered controller, therefore, the computational
burden has been reduced. The triggered times and the release
time interval are plotted in Fig. 2b. The maximum release
time interval is 22 seconds meaning that we do not need to
recompute the control input and just use the previous control
input. The triggered times in the whole simulation period is
165.
 We then test the different spacing settings of AV, we
run the simulation with spacing of AV sa = 20m. The

comparison between the continuous controller and eventtriggered controller is shown in Fig. 3a. The triggered times and the release time interval are plotted in Fig. 3b. The maximum release time interval is 27s and the triggered times is 244. Results show the traffic system tends to become more congested with a larger spacing of AV. The event triggered controller must need to execute more times to make the system stable.

## Vi. Conclusions

  The event-triggered control of mixed-autonomy traffic
system consisting both HV and AV is investigated. The traffic
dynamics of mixed-autonomy traffic system is represented
by an extend-ARZ model. The backstepping controller is
designed to stabilize the system and then the dynamic
ETM is defined. The event-triggered boudary controller
is derived through the dynamic ETM. And the Lyapunov
analysis is applied to derive the stability results of the
mixed-autonomy system with event-triggered controller. A
numerical simulation is conducted to illustrate the effect of
event-triggered controller. The future work will focus on
developing the observer-based event-triggered controller for
the mixed-autonomy traffic system.

## References

[1] A. Aw and M. Rascle. Resurrection of "second order" models of traffic
flow. *SIAM journal on applied mathematics*, 60(3):916–938, 2000.
[2] M. Burkhardt, H. Yu, and M. Krstic. Stop-and-go suppression in twoclass congested traffic. *Automatica*, 125:109381, 2021.
[3] N. Espitia, J. Auriol, H. Yu, and M. Krstic.
Traffic flow control
on cascaded roads by event-triggered output feedback. International
Journal of Robust and Nonlinear Control, 32(10):5919–5949, 2022.
[4] N. Espitia, A. Girard, N. Marchand, and C. Prieur.
Event-based
control of linear hyperbolic systems of conservation laws. *Automatica*,
70:275–287, 2016.
[5] A. Ferrara, S. Sacone, and S. Siri. Event-triggered model predictive
schemes for freeway traffic control. Transportation Research Part C:
Emerging Technologies, 58:554–567, 2015.
[6] A. Girard. Dynamic triggering mechanisms for event-triggered control.
IEEE Transactions on Automatic Control, 60(7):1992–1997, 2014.
[7] P. Goatin, S. G¨ottlich, and O. Kolb. Speed limit and ramp meter control
for traffic flow networks. *Engineering Optimization*, 48(7):1121–1144, 2016.
[8] G. Gomes and R. Horowitz. Optimal freeway ramp metering using the
asymmetric cell transmission model. Transportation Research Part C: Emerging Technologies, 14(4):244–262, 2006.
[9] L. Hu, F. Di Meglio, R. Vazquez, and M. Krstic.
Control of homodirectional and general heterodirectional linear coupled hyperbolic PDEs. *IEEE Transactions on Automatic Control*, 61(11):3301–3314, 2016.
[10] I. Karafyllis and M. Papageorgiou.
Feedback control of scalar
conservation laws with application to density control in freeways by means of variable speed limits. *Automatica*, 105:228–236, 2019.
[11] M. J. Lighthill and G. B. Whitham. On kinematic waves ii. a theory
of traffic flow on long crowded roads.
Proceedings of the Royal
Society of London. Series A. Mathematical and Physical Sciences,
229(1178):317–345, 1955.
[12] R. Mohan and G. Ramadurai. Heterogeneous traffic flow modelling
using second-order macroscopic continuum model. *Physics Letters A*, 381(3):115–123, 2017.
[13] C. Pasquale, S. Sacone, S. Siri, and A. Ferrara.
Hierarchical
centralized/decentralized event-triggered control of multiclass traf-
fic networks.

IEEE Transactions on Control Systems Technology,
29(4):1549–1564, 2020.

[14] P. I. Richards. Shock waves on the highway. *Operations research*,
4(1):42–51, 1956.
[15] S. Siri, C. Pasquale, S. Sacone, and A. Ferrara. Freeway traffic control:
A survey. *Automatica*, 130:109655, 2021.
[16] P. Tabuada. Event-triggered real-time scheduling of stabilizing control
tasks.
IEEE Transactions on Automatic control, 52(9):1680–1685,
2007.
[17] H. Yu, J. Auriol, and M. Krstic.
Simultaneous downstream and
upstream output-feedback stabilization of cascaded freeway traffic. Automatica, 136:110044, 2022.
[18] H. Yu and M. Krstic. Traffic congestion control for Aw–Rascle–Zhang
model. *Automatica*, 100:38–51, 2019.
[19] H. M. Zhang.
A non-equilibrium traffic model devoid of gas-like
behavior. *Transportation Research Part B: Methodological*, 36(3):275–
290, 2002.
[20] L. Zhang and C. Prieur. Stochastic stability of markov jump hyperbolic
systems with application to traffic flow control. *Automatica*, 86:29–37, 2017.
[21] P. Zhang, R.-X. Liu, S. Wong, and S.-Q. Dai.
Hyperbolicity and
kinematic waves of a class of multi-population partial differential equations. *European Journal of Applied Mathematics*, 17(2):171–200,
2006.
[22] Y. Zhang, H. Yu, J. Auriol, and M. Pereira. Mean-square exponential
stabilization of mixed-autonomy traffic PDE system. arXiv preprint arXiv:2310.15547, 2023.