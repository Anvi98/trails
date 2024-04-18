# Control Contraction Metrics On Lie Groups

Dongjun Wu1, Bowen Yi2, Ian R. Manchester3

  Abstract— In this paper, we extend the control contraction
metrics (CCM) approach, which was originally proposed for the
universal tracking control of nonlinear systems, to those that
evolves on Lie groups. Our idea is to view the manifold as a
constrained set that is embedded in Euclidean space, and then
propose the sufficient conditions for the existence of a CCM
and the associated controller design. Notably, we demonstrate
that the search for CCM on Lie groups can be reformulated as
convex conditions. The results extend the applicability of the
CCM approach and provide a framework for analyzing the
behavior of control systems with Lie group structures.
  Index Terms— nonlinear systems, contraction analysis, Lie
groups, tracking control

## I. Introduction

  Contraction analysis has gained widespread recognition
both within and beyond the control community since the
seminal paper by Lohmiller and Slotine [1]. It provides
a powerful and flexible tool to analyze the stability and
dynamical behaviour of nonlinear systems by means of linear
systems theory. Over the years, researchers have extensively
applied contraction analysis to various domains, including
observer design [2,3], trajectory tracking [4, 5], machine
learning [6]–[9], and motion planning [10,11]. For a com-
prehensive review of the literature and future perspectives on
this field, the interested reader may refer to the recent survey
paper [12] and the monograph [13].
  One recent development in contraction analysis involves
its utilization as a synthesis tool for constructive nonlinear
control, exemplified by the widely popular control contrac-
tion metric (CCM) method introduced in [14]. It is shown
that by searching for a CCM, the system could be universally
stabilized for any feasible reference trajectories. A salient
feature of this approach is that its design procedure can be
turned into a convex optimization problem. See also [15]
for its robust version for non-affine systems. In the last
few years, the CCM approach has been successfully applied
to many domains, such as the safe control of robots [16],
adaptive control [17], model predictive control (MPC) [18],
and motion planning [10,11].
  The existing results on CCM primarily focus on sys-
tems evolving on Euclidean space. However, a majority of

nonlinear systems reside on manifolds, including robotic
models and rigid body models of vehicles such as aerial or
underwater robots. It is still an open problem to extend the
CCM approach to manifolds. In this paper, we propose some
preliminary results for such an extension to Lie groups. The
main contributions of the paper are twofold:

1. We formulate the CCM on embedded submanifolds and
then specialize it to Lie groups setting. Subsequently, we demonstrate that the search for a CCM on Lie groups
can be characterized by some convex conditions.
2. In the sampled-data version of the "standard" CCM, it
is required to compute the geodesic during the online implementation at every sampling time. We show that computation of geodesics can be avoided by using other types of curves. It provides easier solutions while ensuring guaranteed stability.
Notations: Given a manifold M, T M and T ∗M represent the tangent and co-tangent bundles of M. We use g(·, ·)
and d to denote the Riemannian metric and the associated Riemannian distance, respectively. ∇ stands for the Levi-
Civita connection. Tr(·) is the trace of a square matrix, and ∥ · ∥ is the Euclidean 2-norm. For symmetric matrices A, B ∈ Rn×n, A > B means that the matrix (A − B) is positive definite; for a square matrix X, we define He{X} :=
X + X⊤. Given a vector field f, DfQ stands for the directional derivative of a smooth quantity Q along f, i.e.

DfQ = �
j
∂Q
∂xj fj, particularly LfQ representing the Lie derivative. For m ∈ N+, denote the set ℓm := {1, · · · , m}.

## Ii. Preliminaries

In this section, we review some preliminary results about the control contraction metric (CCM) approach [14].

Consider the nonlinear system

$$\dot{x}=f(x,t)+B(x,t)u\tag{1}$$
with the state x ∈ X ⊆ Rn and the input u ∈ Rm, where the functions f : Rn → Rn and B(x) = col(b1(x), · · · , bm(x))
are assumed continuously differentiable, and B has constant rank m. 1 The paper [14] considers the Euclidean case with X = Rn. We call (x⋆(t), u⋆(t)) ∈ X × Rm a feasible pair, if it satisfies ˙x⋆ = f(x⋆, t) + B(x⋆, t)u⋆ for all t ≥ 0.

Problem set. For the given system (1), we aim to find a feedback law u
= kp(x, x⋆, u⋆, t) that exponentially stabilizes any feasible desired trajectory x⋆.

The first step in contraction analysis is to calculate the variational dynamics of the system (1), that is

$\delta x=A(x,u,t)\delta x+B(x,t)\delta u$ (2)
with A(x, u, t) = ∂f

                ∂x(x, t)+�m
                           i=1
                              ∂bi
                               ∂x ui. The variables δx ∈
T X and δu ∈ T Rm are the differential state and input, which
are the infinitesimal variations in terms of the original system
(1); see [14, 19] for details. A notable feature is that the
variational system (2) is linear time-varying (LTV) if we
regard x and u as exogenous signals.
  In the CCM approach, the design of a tracking controller
is reformulated as the search for a smooth control contraction
metric M : Rn × R → Rn×n
                       >0
                            and a differential controller
δu = kδ(x, δx, u, t) satisfying
C0 The metric M is uniformly bounded, i.e.

$\alpha_{1}I\leq M(x,t)\leq\alpha_{2}I$, $\forall x,t$ (3)
for α1, α2 > 0 and satisfies the contraction condition

$$B^{\top}M\delta x=0\implies$$ $$\delta x^{\top}\left(\frac{\partial M}{\partial t}+D_{f}M+\mbox{He}\{MA\}+2\lambda M\right)\delta x<0\tag{4}$$

for all $x,u,t$ and non-zero $\delta x$, with some $\lambda>0$.

As proven in [14], the following two stronger conditions imply (4):

**C1**: For $\delta x\neq0$, the implication holds

$$\delta x^{\top}\left(\frac{\partial M}{\partial t}+D_{f}M+\mbox{He}\left\{\frac{\partial f^{\top}}{\partial x}\,M\right\}+2\lambda M\right)\delta x<0.\tag{5}$$
**C2**: For each $i\in\ell_{m}$,

$$D_{b_{i}}M+\mbox{He}\left\{\frac{\partial b_{i}}{\partial x}\,M\right\}=0.\tag{6}$$

  When (6) is satisfied, we call bi a Killing vector field under
the metric M(x, t), and in this case, M(x, t) is referred to
as a strong CCM. Otherwise, if only C1 holds, we call it a
weak CCM.
  Remark 1: It should be noted that the (global) existence
of Killing fields on a manifold is related to the topological
properties of the manifold [20], making a relatively strict
condition. It might be easier to find a weak CCM for a
given system on manifolds. However, the challenge can be
circumvented if we consider locally.
  Once a CCM has been found, a controller can be synthe-
sized in the following two steps.
S1 Find a differential feedback δu = kδ(x, δx, u, t) such
    that

δx⊤ ˙Mδx + 2δx⊤M(Aδx + Bkδ) < −2λδx⊤Mδx

holds for all x, u, t and non-zero δx.
S2 Design a feedback law u = kp(·) to ensure that the
closed-loop dynamics conform to the desired differential systems when subjected to the differential feedback
δu that is obtained in S1.
For S2, a feasible construction is that, given a minimizing geodesic γ : [0, 1] → Rn joining x⋆(t0) to x(t0), the feedback kp can be selected as the solution to

$k_{p}(c,u_{\star},t,s)=u_{\star}(t)+\int_{0}^{s}k_{\delta}\left(c(s),c^{\prime}(s),k_{p}(c,u_{\star},t,s),t\right)ds$
where c(t, s) is the solution to the system (1) with initial condition γ(s). Then u
=
kp(c, u⋆, t, 1) exponentially stabilizes the trajectory x⋆(·), i.e., d(x⋆(t), x(t)) ≤
e−λtd(x⋆(0), x(0)),
∀t ≥ 0.

The control strategy described above is open-loop control as there is only onetime measurement of the state. Its performance and robustness can be enhanced by considering the sampled-date controller - recursively applying the openloop control described above at sampled instances [14] - or by adopting the minimal geodesics in real time [21].

## Iii. Control Contraction Metrics On Lie Groups A. General Results

The Lie groups commonly encountered in control systems have a structure characterized as matrix Lie groups multiplied by (in direct product with) a vector space. Many of them, if not all, can be seen as "constrained submanifolds"
within certain Euclidean spaces, e.g., SO(n) = {X ∈
Rn×n : X⊤X = I, det X = 1}. Therefore, it is natural to view these as systems in Euclidean space with constraints

$$\mathcal{M}=\{x\in\mathbb{R}^{n}:h(x)=0\},\tag{7}$$

where the smooth function $h:\mathbb{R}^{n}\rightarrow\mathbb{R}^{q}$ has constant rank.

In this section, we consider the system model in the form (1) with the state space $\mathcal{X}$ being $\mathcal{M}$. To guarantee that the vector fields $f$ and $b_{i}$ ($i\in\ell_{m}$) are tangent to the manifold, it is necessary and sufficient to satisfy the transversality condition

$$L_{f}h(x)=0,\quad L_{b_{i}}h(x)=0.\tag{8}$$

for all x ∈ M and t ≥ 0. We aim to extend the CCM
approach to the systems on manifolds to exponentially track
a feasible desired trajectory x⋆(t) ∈ M.
  Mimicking the conditions C0-C2, we propose the corre-
sponding version on the manifold M as follows. A natural
idea is to equip the manifold with the induced metric within
M × R≥0 that is required to be positive definite on the
tangent bundle T M. These conditions are sufficient to design
a CCM controller on manifolds, which will be introduced in
Proposition 3 below.
A0 There exist two positive constants a1, a2 such that
  ∂h
  ∂xδx = 0 =⇒ a1∥δx∥2 ≤ δx⊤M(x, t)δx ≤ a2∥δx∥2

A1 For some λ > 0 and ∀δx ̸= 0, the following holds

$$B^{\top}M\delta x=0\tag{9}$$ $$\frac{\partial h}{\partial x}\delta x=0$$ $$\delta x^{\top}\left(\frac{\partial M}{\partial t}+\partial_{f}M+\mbox{He}\left\{\frac{\partial f^{\top}}{\partial x}\ M\right\}+2\lambda M\right)\delta x<0$$
A2 Each bi is a Killing field, i.e., for all δx1, δx2
∂h
∂x(x)δx = 0 =⇒

∂x �� δx = 0. (10) δx⊤ � DbiM + He � M ∂bi

  Remark 2: In contrast to the Euclidean case, the new
ingredient in A0-A1 is
                      ∂h
                      ∂xδx = 0, which imposes the
constraint δx ∈ T M. Similarly to C2, the condition A2
is related to the uniform stabilizability of the differential
dynamics for arbitrary u⋆ [14,22]. However, our case only
requires the condition on the set {x ∈ Rn : h(x) = 0}.2

  Once a function M(x, t) satisfying A0-A2 can be found,
we call it a CCM on M. Then, we can proceed to controller
design as follows. Assume that (x⋆(·), u⋆(·)) is a feasible
pair of the system (1) and γ : [0, 1] → M is the minimizing
geodesic under the induced metric from Rn joining x⋆(t0)
to x(t0). We have the following.
  Proposition 3: Let M(x, t) be a CCM on M satisfying
A0 - A3. There exist open-loop and sampled-data exponen-
tially stabilizing controllers of the trajectory x⋆(·).
    Proof: In the proof, we show the existence of the open-
loop and sampled-data controllers that exponentially stabilize
the tracking error system.
  1) Open-loop controller. Let u(t, s), x(t, s) be the solution
to the partial differential system
          ∂x
           ∂t = f(x, t) + B(x, t)u

(11) 2ρ(x, t)B(x, t)⊤M(x, t)∂x ∂s ∂u ∂s = −1
with s ∈ [0, 1], u(t, 0) = u⋆(t), ∀t ≥ t0 and x(t0, s) =
γ(s), ∀s ∈ [0, 1], where the scalar function ρ(x, t) ≥ 0 will be determined later in the proof to guarantee the contraction of the closed loop.

Considering the infinitesimal variable δx(t) := ∂x
∂s (t, s), we calculate the evolution of energy:

$$\frac{d}{dt}\int_{0}^{1}\delta x^{\top}M\delta xds$$ $$=\int_{0}^{1}2\delta x^{\top}M\left(\frac{\partial f}{\partial x}\delta x+\sum_{i=1}^{m}u_{i}\frac{\partial b_{i}}{\partial x}\delta x+\sum_{i=1}^{m}\frac{\partial u_{i}}{\partial s}b_{i}\right)$$ $$\quad+\delta x^{\top}\left(\frac{\partial M}{\partial t}+D_{f}M+\sum_{i=1}^{m}u_{i}D_{b_{i}}M\right)\delta xds$$ $$=\int_{0}^{1}\delta x^{\top}\left(\frac{\partial M}{\partial t}+D_{f}M+\mathrm{He}\left\{M\frac{\partial f}{\partial x}\right\}\right)\delta x$$ $$\quad+\sum_{i=1}^{m}u_{i}\delta x^{\top}\left(D_{b_{i}}M+\mathrm{He}\left\{M\frac{\partial b_{i}}{\partial x}\right\}\right)\delta x$$ $$\quad+2\delta x^{\top}\sum_{i=1}^{m}\frac{\partial u_{i}}{\partial s}Mb_{i}ds.$$
2In fact, the condition (10) coincides with the definition of Killing vector fields i.e. LbM(x, t) = 0, which should not be surprising. Indeed, LbM(δx, δx) =
d dt

�
 ∂φb
  t(x)
  ∂x
    δx
      �⊤
        M(t, φb
            t(x)) ∂φb
                 t (x)
                ∂x
                   δx where

���
  t=0

φb
 t : x �→ φb
        t(x) is the flow of the vector field b. Expanding the above
equation results in (10).

∂x
  �
    − ρMBB⊤M
                 �
                  δxds.

Define a = δx⊤( ∂M

Invoking
         A2,
               the
                   fact
                        that
                              ∂h
                              ∂xvs
                                     =
                                         0
                                             and
                                                  plug-
ging in (11), we immediately get
                                   d
                                   dt
                                     � 1
                                      0 δx⊤Mδxds
                                                     =
� 1
 0 δx⊤ �
        ∂M
         ∂t + DfM + He
                         �
                           M ∂f

∂t +DfM +He
                 �
                   M ∂f

∂x
  �
   −2λM)δ and

a2 + b2)/b otherwise. It follows that

b = δx⊤MBB⊤δx. Invoking A1, we set ρ as 0 if a < 0
and (a +
       √

$$\frac{d}{dt}\int_{0}^{1}\delta x^{\top}M\delta x ds<-2\lambda\frac{d}{dt}\int_{0}^{1}\delta x^{\top}M\delta x ds,$$
showing that u(t, 1) exponentially stabilizes the trajectory x⋆(·), i.e., there exist two constants K, λ > 0 such that dM(x⋆(t), x(t)) ≤ Ke−λ(t−t0)dM(x⋆(t0), x(t0))
(12)
where dM(·, ·) stands for the Riemannian distance on the manifold M under the metric M(x, t). Note that here K
may be larger than 1 since the initial curve γ is the geodesic under the induced metric.

2) *Sampled-data controller.* Choose a sampling time T > 0
satisfying K
�

satisfying $K\sqrt{\frac{a_{2}}{a_{1}}}e^{-\lambda T}=:k<1$, in which the constant $K$ is the same as in (12). At each sampling time instant $t_{i}$, $i=1,2,\cdots$, measure the state $x(t_{i})$, compute a minimizing geodesic $\gamma_{i}$ connecting $x_{\star}(t_{i})$ to $x(t_{i})$ under the _induced metric_ from the ambient space and apply the open-loop control described above with initial condition $x(t_{i},s)=\gamma_{i}(s)$ on the interval $[t_{i},t_{i+1})$. Then, such a sampled-data feedback exponentially stabilizes the trajectory $x_{\star}(\cdot)$. Let $d(\cdot,\cdot)$ be the Riemannian distance corresponding to the induced metric from the ambient space on $\mathcal{M}$ and $d_{M}(\cdot,\cdot)$ the one corresponding to the metric $M$. Invoking (12) and Lemma 8, we have for all $i\in\mathbb{N}_{+}$ and $k\in(0,1)$,

$$d(x(t_{i+1}),x_{\star}(t_{i+1}))\leq\frac{1}{\sqrt{a_{1}}}d_{M}(x(t_{i+1}),x_{\star}(t_{i+1}))$$ $$\leq\frac{1}{\sqrt{a_{1}}}Ke^{-\lambda T}d_{M}(x(t_{i}),x_{\star}(t_{i}))$$ $$\leq\sqrt{\frac{a_{2}}{a_{1}}}Ke^{-\lambda T}d(x(t_{i}),x_{\star}(t_{i}))$$ $$=kd(x(t_{i}),x_{\star}(t_{i})).$$
It is then standard argument to show

$d_{M}(x(t),x_{\star}(t))\leq Ke^{-\tilde{\lambda}(t-t_{0})}d_{M}(x(t_{0}),x_{\star}(t_{0}))$
for some K′, ˜λ > 0 and all t ≥ t0.

It complets the proof.

Remark 4: Note that it is unnecessary to choose the initial curves γ(·) and γi(·) as the geodesics - under the metric M(x, t) - for the open-loop and sampled-data controllers. In fact, thanks to assumption A1, there exist constants c1, c2 >
0 such that c1I ≤ M(x, t) ≤ c2I on T M. Therefore, by Lemma 8 in Appendix, the geodesic distance under the metric M is equivalent to the one induced by the metric of the ambient space. This idea can be also used to design a sampled-data feedback when the geodesic on M under the induced metric, e.g. Euclidean metric, from the ambient space can be easily computed.

  Remark 5: The conditions A0-A2 have two drawbacks
from a numerical implementation perspective. Firstly, these
conditions are non-convex, which require heavy computa-
tional burden. Second, when the dimension of the manifold
M is much smaller than that of the ambient space, numer-
ous unnecessary computations will arise, adding an undue
computational burden. More precisely, one needs to search
for a matrix function taking values in Rn×n, while M only
has the dimension q ≪ n.

## B. Convexified Conditions

In this section, we propose a modified version of conditions to address the aforementioned numerical challenges.
The results are particularly useful on systems evolved on Lie
groups. Toward this end, we make the following assumption.
A3 The
tangent
bundle
of
M
in
(7)
is
spanned
by *independent* vector fields {s1, · · · , sq}. Assume
∥S(S⊤S)−1∥ ≤ cS, ∀x ∈ M with some cS and the
definition S(x) := [s1(x), · · · , sq(x)].
Under the above assumption, we are able to find some
smooth matrix function E : M × R≥0 → Rq×m such that
$B(x,t)=S(x)E(x,t)$, (13)
due to the fact bi ∈ T M. Likewise, δx ∈ T M can be written as δx = S(x)v(x) for some v(x) ∈ Rq. Now, instead of searching for M ∈ Rn×n directly, we may search for another metric M(x, t) in a lower-dimensional space Rq×q, and the previous metric M is parameterized by

$$M(x,t)=P_{S}(x)\mathfrak{M}(x,t)P_{S}^{\top}(x)\tag{14}$$
where PS = S(S⊤S)−1 is the projection operator which is computed before searching for the CCM.

Considering the boundedness of PS, the condition A0 is equivalent to:
A0′ there exist two positive constants a1, a2 such that a1Iq ≤ M(x, t) ≤ a2Iq,
∀x ∈ M, t ≥ 0.

(15)

Meanwhile, writing $\delta x=S(x)v(x)\in T{\cal M}$, and invoking (13) and (14), we have $B^{\top}M\delta x=E^{\top}{\cal M}v$. Then, **A1-A2** can be reformulated as:

${\bf A1^{\prime}}$ For $v\in\mathbb{R}^{q}\backslash\{0\}$, the following implication holds

$$E^{\top}{\cal M}v=0\implies$$ $$v^{\top}\left(\frac{\partial{\cal M}}{\partial t}+D_{f}{\cal M}+{\rm He}\{{\cal M}S_{f}\}+2\lambda{\cal M}\right)v<0\tag{16}$$

where the known matrices $S_{f}:=D_{f}(P_{S}^{\top})S+P_{S}^{\top}\frac{\partial f}{\partial x}S$ and $S_{b_{i}}:=D_{b_{i}}(P_{S}^{\top})S+P_{S}^{\top}\frac{\partial b_{i}}{\partial x}S$ are in $\mathbb{R}^{q\times q}$.

${\bf A2^{\prime}}$ For each $i\in\ell_{m}$:

$$D_{b_{i}}{\cal M}+S_{b_{i}}^{\top}{\cal M}+{\cal M}S_{b_{i}}=0.\tag{17}$$
Following [14], we convexify A0′ - A2′ via the "musical isomorphism" W −1(x, t) = M(x, t). Then, (15) and (17)
are equivalent to

$$\frac{1}{a_{2}}I_{q}\leq W\leq\frac{1}{a_{1}}I_{q},\tag{18}$$
and3

$$-D_{b_{i}}W+WS_{b_{i}}^{\top}+S_{b_{i}}W=0.\tag{19}$$
respectively.

For (16), it is equivalent to the existence of a scalar function ρ(x, t) such that for all x, t:

$$-\frac{\partial W}{\partial t}-D_{f}W+WS_{f}^{\top}+S_{f}W+2\lambda W-\rho EE^{\top}<0.\tag{20}$$

The formulas (18) - (20) is convex w.r.t. to the metric $W$ to be searched for. Once $\rho$ and $W$ has been obtained, we can proceed to controller design with the CCM

$$M=P_{S}W^{-1}P_{S}^{\top}.\tag{21}$$
Remark 6: In Lie groups, the above condition A3 is always guaranteed as the tangent bundle of a Lie group G
is trivial in the sense that T G = G × g, see e.g., [23]. Thus, for example, T G is spanned by left (right)-invariant vector fields. On the other hand, generally even if there exist no global vector fields spanning T M, it is always possible to work locally.

## C. Ccm On Lie Groups

  Most of Lie groups in control applications can be modeled
as G × Rl, where G is a Lie subgroup of GL(µ) = {A ∈
Rµ×µ : A invertible}.4 This class of Lie groups is naturally
embedded in the Euclidean space Rµ2+l.
  We use the space O(2)×R as a case study to illustrate how
to apply the methods proposed in the previous subsection.
  Step 1: We embed the Lie group O(2) × R into R5 via

O(2) × R ∋ (R, x) �→ (r, x) := [R11, R12, R21, R22, x]⊤

where Rij are the elements of R ∈ O(2). The constraint
map h, with q = 3, is then

$$h(r,x)=\begin{bmatrix}r_{1}^{2}+r_{3}^{2}-1\\ r_{2}^{2}+r_{4}^{2}-1\\ r_{1}r_{2}+r_{3}r_{4}\end{bmatrix},$$

which is a reinterpretation of $R^{\top}R=I_{2}.$ From $h,$ we can determine the matrix $S(r,x).$ This is rather straightforward:

$$S(r,x)=\begin{bmatrix}0&0&0&0&1\\ -\frac{r_{3}}{\sqrt{2}}&\frac{r_{3}}{\sqrt{2}}&-\frac{r_{4}}{\sqrt{2}}&\frac{r_{3}}{\sqrt{2}}&0\end{bmatrix}^{\top}.$$

In addition, we have S⊤S = I2, and thus A0 is satisfied. It
yields PS(r, x) = S(r, x).
  Step 2: Write the system dynamics into standard form (1)
and search for W ∈ R2×2 satisfying (18)-(20).
  Step 3: Solve the partial differential equation (11) - the
path integral - to obtain the controller. We need to calculate
the geodesic on O(2) × R under the induced metric from
the ambient space. Since O(2) is compact, the geodesic is
nothing but given by the matrix exponential. That is, given

$R_{1},R_{2}$ in the same component of $O(2)$, the geodesic joining $R_{1}$ to $R_{2}$ is given by $t\mapsto R_{1}\exp(\log(R_{1}^{\top}R_{2})t)$. Thus, the geodesic on $O(2)\times\mathbb{R}$ joining $(R_{1},x_{1})$ to $(R_{2},x_{2})$ is $t\mapsto(R_{1}\exp(\log(R_{1}^{\top}R_{2})t),(1-t)x_{1}+tx_{2})$.

Following the above three steps, we are able to design CCM-based controllers for general control systems evolving on $G\times G_{1}\times\mathbb{R}^{k}$, where $G$ is a compact Lie group in $GL(\mu)$ and $G_{1}$ represents a Lie group embedded in $\mathbb{R}^{p}$.

_Remark 7_: In Step 1, it is unnecessary to compute $S$ from the constraint $h(r,x)$. As we mentioned before, the tangent bundle of a Lie group is trivial and can be simply chosen as the left (or right) invariant vector fields, which is isomorphic to the Lie algebra. For example, the Lie algebra of $O(2)\times\mathbb{R}$ is $\sigma(2)\times\mathbb{R}$ for a basis is

$$E_{1}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}\times\{1\}.\quad E_{2}=\begin{bmatrix}0&\frac{1}{\sqrt{2}}\\ \frac{-1}{\sqrt{2}}&0\end{bmatrix}\times\{0\},$$
The left-invariant vector fields corresponding to E1, E2 are

$S_{1}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}\times\{1\},\ S_{2}=R\begin{bmatrix}0&\frac{-1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}}&0\end{bmatrix}\times\{0\},$
from which one easily recovers S(r, x).

Example 1: Consider the space SE(3):

$$SE(3)=\left\{\begin{bmatrix}R&v\\ 0&1\end{bmatrix}\in\mathbb{R}^{4\times4}:R^{\top}R=I,\det R=1,v\in\mathbb{R}^{3}\right\}.$$

which is isomorphic to $SO(3)\times\mathbb{R}^{3}.$ Embed $SE(3)$ into $\mathbb{R}^{12}$ as in the previous subsection and denote the state variable in $\mathbb{R}^{12}$ as $(r,x).$ Note that $\dim\{SE(3)\}=6,$ we shall search for a CCM $M(x,t)\in\mathbb{R}^{6\times6}.$ Since $\mathfrak{s}(3)=\mathfrak{so}(3)\times\mathbb{R}^{3},$ it is easy to calculate $S(r,v)\in\mathbb{R}^{12\times6}$ as

$$S(r,x)=\begin{bmatrix}0_{9\times3}&S_{r}\\ I_{3}&0_{3\times3}\end{bmatrix}$$
in which

$$S_{r}=\frac{1}{\sqrt{2}}\begin{bmatrix}-r_{2}&-r_{3}&0\\ r_{1}&0&-r_{3}\\ 0&r_{1}&r_{2}\\ -r_{5}&-r_{6}&0\\ r_{4}&0&-r_{6}\\ 0&r_{4}&r_{5}\\ -r_{8}&-r_{9}&0\\ r_{7}&0&-r_{9}\\ 0&r_{7}&r_{8}\end{bmatrix}$$

One can verify that $S^{\top}S=I_{6}$. As a consequence, $P_{S}(r,x)=S(r,x)$.

Consider the system dynamics

$$\dot{R}=R\Omega$$ $$\dot{v}=-kv+Re,$$

in which $e$ is a fixed unit vector in $\mathbb{R}^{3}$ and $\Omega\in\mathfrak{so}(3)$ can be directly controlled. The control objective is to make $v(t)$ exponentially converge to a given desired feasible $v_{\star}(t)$.

The matrices $S_{f}$ and $S_{b_{i}}$ can be easily computed:

$$S_{f}=\begin{bmatrix}-kI_{3}&(I_{3}\otimes e^{\ |\ \ })S_{r}\\ 0_{3\times3}&0_{3\times3}\end{bmatrix},\quad S_{b_{i}}=\begin{bmatrix}0_{3\times3}&0_{3\times3}\\ 0_{3\times3}&F_{i}\end{bmatrix}$$
where

$$F_{1}=\frac{1}{2}\begin{bmatrix}r_{2}-r_{4}&r_{3}&r_{6}\\ 0&-r_{4}&-r_{5}\\ 0&r_{1}&r_{2}\end{bmatrix},$$ $$F_{2}=\frac{1}{2}\begin{bmatrix}-r_{7}&0&r_{9}\\ r_{2}&r_{3}-r_{7}&-r_{8}\\ -r_{1}&0&r_{3}\end{bmatrix},$$ $$F_{3}=\frac{1}{2}\begin{bmatrix}-r_{8}&-r_{9}&0\\ r_{5}&r_{6}&0\\ -r_{4}&-r_{7}&r_{6}-r_{8}\end{bmatrix}.$$

We can then substitute these matrices into (18)-(20) to solve for the matrix function $W$.

## D. More Abstract Manifolds

In this subsection, we provide an intrinsic treatment of CCM on abstract manifolds whose embeddings into Euclidean spaces are not immediately obvious. These results are of theoretical interest and may be viewed as a high level guideline - thanks to their much simpler forms.

Consider a Riemannian manifold M equipped with a metric g0. Let x(t, s) be the solution to the system (1) with initial condition γ(s) at t = 0, with γ : [0, 1] → M a geodesic under the metric g0.

We shall look for a CCM g, such that

$$\frac{1}{2}\frac{d}{dt}g\left(\frac{\partial x(t,s)}{\partial s},\frac{\partial x(t,s)}{\partial s}\right)\leq-\lambda g\left(\frac{\partial x(t,s)}{\partial s},\frac{\partial x(t,s)}{\partial s}\right)\tag{22}$$

for some $\lambda>0$ and all $u,\,t\geq0,\,s\in[0,1].$ Let $\frac{D}{ds}$ be the covariant derivative associated with the metric $g.$ For notational ease, denote $v_{s}:=\frac{\partial x(t,s)}{\partial s},$ then the left hand side 
∂s
, then the left hand side of (22) can be calculated as

$$\frac{1}{2}\frac{dg\left(v_{s},v_{s}\right)}{dt}$$ $$=g\left(\frac{Dv_{s}}{dt},v_{s}\right)+\dot{g}(v_{s},v_{s})$$ $$=g\left(\nabla_{v_{s}}\left(f+\sum_{i=1}^{m}u_{i}b_{i}\right),v_{s}\right)+\dot{g}(v_{s},v_{s})$$ $$=g(\nabla_{v_{s}}f+\sum_{i=1}^{m}u_{i}\nabla_{v_{s}}b_{i}+\sum_{i=1}^{m}\frac{\partial u_{i}}{\partial s}b_{i},v_{s})+\dot{g}(v_{s},v_{s})$$ $$=g(\nabla_{v_{s}}f,v_{s})+\sum_{i=1}^{m}u_{i}g(\nabla_{v_{s}}b_{i},v_{s})+\sum_{i=1}^{m}\frac{\partial u_{i}}{\partial s}g(b_{i},v_{s})$$ $$+\dot{g}(v_{s},v_{s}).$$
If (22) holds for all u, the second term on the last line vanish since it depends linearly on u. In other words,

$$g(\nabla_{v}b_{i},v)=0,\quad\forall v\in T{\cal M},\ i\in\ell_{m}.\tag{23}$$
This is nothing but saying that bis are Killing fields (c.f. C1).

To continue, note that if for v ∈ T M satisfying g(bi, v) =
0 for all i ∈ ℓm, there holds

$$g(\nabla_{v}f,v)+\dot{g}(v,v)+2\lambda g(v,v)<0,\tag{24}$$

then we can simply design a "differential controller" as
∂ui
∂s = −ρg(bi, vs) for some non-negative function ρ(x, t)
as in Proposition 3. We underline that (24) is exactly (9).
  Like in the submanifold case, the search for a CCM on
an abstract manifold can be convexified via the musical
isomorphism: ♭ : T M → T M∗. In words, given v ∈ T M
and the Riemannian metric g, we lift v and g to T M∗:

$ v=v^i\frac{\partial}{\partial x_i}\mapsto v^i g_{ij}dx^j$

$ g=g_{ij}dx^i dx^j\mapsto g^{ij}\frac{\partial}{\partial x_i}\frac{\partial}{\partial x_j}$

where (gij) is the inverse of (gij).
  For implementation, all the expressions will need to be
written in local coordinates, from where one can recover
the assumptions A0-A2. In general, however, one should not
expect to solve the problem globally like on Lie groups.

## Iv. Concluding Remarks

  This paper has presented an extension of the control
contraction metrics approach from Euclidean space to Lie
groups, in which we view the manifolds as constrained sets.
In particular, we show that the search for CCM on matrix
Lie groups (potentially with a direct product with a vector
space) can be formulated as the convex conditions. Future
directions would be to apply the proposed approach to study
the trajectory tracking control of some practical systems on
manifolds.

## Appendix

Lemma 8: Let g1, g2 be two Riemannian metrics on a manifold M satisfying a1g1(v, v) ≤ g2(v, v) ≤ a2g1(v, v),
∀v ∈ T M
(25)
for some positive constants a1, a2. Let d1 and d2 be the induced Riemannian distances of the two metrics respectively.

Then there holds
√a1d1(x, y) ≤ d2(x, y) ≤ √a2d1(x, y),
∀x, y ∈ M (26)
where dg and d¯g are the induced distances on M, whenever they are well defined.

Proof: For a given pair of points x, y ∈ M such that dg(x, y) and d¯g(x, y) are defined, let γg : [0, 1] → M and
γ¯g : [0, 1] → M be the minimizing geodesics joining x to y for dg and d¯g, respectively.

From Assumption A1, we have on one hand,

$$d_{\bar{g}}(x,y)=\int_{0}^{1}\sqrt{\bar{g}}(\gamma^{\prime}_{\bar{g}}(s),\gamma^{\prime}_{\bar{g}}(s))ds$$ $$\leq\int_{0}^{1}\sqrt{\bar{g}}(\gamma^{\prime}_{g}(s),\gamma^{\prime}_{g}(s))ds$$ $$\leq\sqrt{a_{2}}\int_{0}^{1}\sqrt{g}(\gamma^{\prime}_{g}(s),\gamma^{\prime}_{g}(s))ds$$ $$=\sqrt{a_{2}}d_{g}(x,y),$$
with the notation (·)′ = ∂(·)
∂s for scalar functions, and on the other hand, similarly

$$d_{\bar{g}}(x,y)=\int_{0}^{1}\sqrt{\bar{g}(\gamma_{\bar{g}}^{\prime}(s),\gamma_{\bar{g}}^{\prime}(s))}ds\geq\sqrt{a_{1}}d_{g}(x,y).$$

This completes the proof.

## References

[1] W. Lohmiller and J.-J. E. Slotine, "On contraction analysis for nonlinear systems," *Automatica*, vol. 34, no. 6, pp. 683–696, 1998.
[2] B. Yi, R. Wang, and I. R. Manchester, "Reduced-order nonlinear
observers via contraction analysis and convex optimization," IEEE
Trans. Autom. Control, vol. 67, no. 8, pp. 4045–4060, 2021.
[3] N. Aghannan and P. Rouchon, "An intrinsic observer for a class of
Lagrangian systems," *IEEE Trans. Autom. Control*, vol. 48, no. 6, pp.
936–945, 2003.
[4] R. Reyes-B´aez, A. van der Schaft, and B. Jayawardhana, "Tracking control of fully-actuated port-Hamiltonian mechanical systems
via sliding manifolds and contraction analysis," *IFAC-PapersOnLine*,
vol. 50, no. 1, pp. 8256–8261, 2017.
[5] A. Pavlov and L. Marconi, "Incremental passivity and output regulation," *Syst. Control Lett.*, vol. 57, no. 5, pp. 400–409, 2008.
[6] C. Blocher, M. Saveriano, and D. Lee, "Learning stable dynamical
systems using contraction theory," in Int. Conf. Ubiquitous Robot.
Ambient Intell.
IEEE, 2017, pp. 124–129.
[7] S.
Singh,
S.
M.
Richards,
V.
Sindhwani,
J.-J.
E.
Slotine,
and M. Pavone, "Learning stabilizable nonlinear dynamics with
contraction-based regularization," *Int. J. Robot. Res.*, vol. 40, no. 10-
11, pp. 1123–1150, 2021.
[8] M. Revay, R. Wang, and I. R. Manchester, "Recurrent equilibrium
networks: Flexible dynamic models with guaranteed stability and
robustness," *IEEE Trans. Autom. Control*, 2023.
[9] B. Yi and I. R. Manchester, "On the equivalence of contraction and
koopman approaches for nonlinear stability and control," IEEE Trans.
Autom. Control, 2023.
[10] S. Singh, B. Landry, A. Majumdar, J.-J. Slotine, and M. Pavone,
"Robust feedback motion planning via contraction theory," Int. J. Robot. Research, 2019.
[11] H. Tsukamoto and S.-J. Chung, "Learning-based robust motion planning with guaranteed stability: A contraction theory approach," IEEE
Robot. Autom. Lett., vol. 6, no. 4, pp. 6164–6171, 2021.
[12] H. Tsukamoto, S.-J. Chung, and J.-J. E. Slotine, "Contraction theory
for nonlinear stability analysis and learning-based control: A tutorial
overview," *Ann. Rev. Control*, vol. 52, pp. 135–169, 2021.
[13] F. Bullo, *Contraction Theory for Dynamical Systems*, 1.1 ed.
Kindle
Direct Publishing, 2023.
[14] I. R. Manchester and J.-J. E. Slotine, "Control contraction metrics:
Convex and intrinsic criteria for nonlinear feedback design," IEEE
Trans. Autom. Control, vol. 62, no. 6, pp. 3046–3053, 2017.
[15] ——, "Robust control contraction metrics: A convex approach to
nonlinear state-feedback H∞ control," *IEEE Control Syst. Lett.*, vol. 2,
no. 3, pp. 333–338, 2018.
[16] C. Dawson, S. Gao, and C. Fan, "Safe control with learned certificates:
A survey of neural lyapunov, barrier, and contraction methods for
robotics and control," *IEEE Trans. Robot.*, 2023.
[17] B. T. Lopez, J.-J. E. Slotine, and J. P. How, "Robust adaptive control
barrier functions: An adaptive and data-driven approach to safety,"
IEEE Control Syst. Lett., vol. 5, no. 3, pp. 1031–1036, 2020.
[18] A. Sasfi, M. N. Zeilinger, and J. K¨ohler, "Robust adaptive MPC
using control contraction metrics," *Automatica*, vol. 155, 2023, art.
no. 111169.
[19] A. van der Schaft, "On differential passivity," in IFAC Symp. Nonlinear
Control Syst.
IFAC, 2013, pp. 21–25.
[20] K. Nomizu, "On local and global existence of killing vector fields,"
Annals of Mathematics, pp. 105–120, 1960.
[21] R. Wang and I. R. Manchester, "Continuous-time dynamic realization
for nonlinear stabilization via control contraction metrics," in Am.
Control Conf.
IEEE, 2020, pp. 1619–1624.
[22] A. van der Schaft, "On differential passivity." in IFAC Symp. Nonlinear
Control Syst., 2013, pp. 21–25.
[23] J. M. Lee and J. M. Lee, *Smooth manifolds*.
Springer, 2012.