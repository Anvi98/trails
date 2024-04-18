# Synthesizing Controller For Safe Navigation Using Control Density Function

Joseph Moyalan, Sriram S.K.S Narayanan, Andrew Zheng, and Umesh Vaidya Abstract— We consider the problem of navigating a nonlinear dynamical system from some initial set to some target set while avoiding collision with an unsafe set. We extend the concept of density function to control density function (CDF) for solving navigation problems with safety constraints. The occupancybased interpretation of the measure associated with the density function is instrumental in imposing the safety constraints. The navigation problem with safety constraints is formulated as a quadratic program (QP) using CDF. The existing approach using the control barrier function (CBF) also formulates the navigation problem with safety constraints as QP. One of the main advantages of the proposed QP using CDF compared to QP formulated using CBF is that both the convergence/stability and safety can be combined and imposed using the CDF. Simulation results involving the Duffing oscillator and safe navigation of Dubin car models are provided to verify the main findings of the paper.

## I. Introduction

Most control system applications in robotics and automotive engineering include driving the nonlinear system dynamics from an initial set to a target set while avoiding certain unsafe sets. Safe navigation is a well-known problem in the robotics community, with applications extending to aerospace, unmanned ground vehicles, manufacturing, power systems, etc. Existing literature on the safe navigation problem involves jointly solving the safety and stability problem using artificial potential methods [1]. However, using attractive and repulsive potentials often leads to local minima, which is a well-known problem [2], [3]. Another approach includes [4], which makes use of the control Lyapunov function (CLF) and control barrier function (CBF) to design a feedback law to achieve simultaneously both convergence to a target set and avoidance of an unsafe set. However, the control design is problem-specific and less intuitive, and if the safety and convergence objectives conflict, then such a feedback law can't be designed. Another approach uses the combination of the CLF and CBF to construct a quadratic program (QP) to solve for the desired safe control [5], [6]. However, finding CLF and CBF to formulate the QP is not trivial. The solution to the navigation problem is also achieved in the dual-density space. The density function was first introduced in [7] as a dual to Lyapunov function for stability analysis. This density function was later used as a safety certificate of Engineering, Clemson University, Clemson, SC;
{jmoyala,sriramk,azheng,uvaidya}@clemson.edu.

using the sum of squares optimization method for the analysis and safety of the nonlinear system [8]. In [9], the authors utilized navigation measures for designing safe controllers using a convex formulation. In [10], the authors formulate the safety problem as a co-design problem of finding the density function and optimal safe controller. However, the iterative approach of estimating the density function from the optimal control can be computationally expensive, depending upon the complexity of the problem. In contrast, we design a controller for a given known density function, which is constructed based on the occupancy-based interpretation of the density. Similarly, the use of linear operators such as Koopman and Perron-Frobenius (P-F) operators for convex data-driven approaches for optimal control and control with safety constraints have been explored in [11]–[14]. The convex data-driven approaches heavily rely on observable functions to lift the dynamics to the space of functions. The number of observables required to lift the dynamics to function space increases with an increase in the dimension or complexity of the underlying nonlinear system, which makes it computationally expensive. As such, these approaches suffer the curse of dimensionality. In [15], to avoid the curse of dimensionality, the authors provide an analytical expression for the density-based feedback controller for the navigation of single integrator dynamics, which can be viewed as a dual construction of the navigation functions from [3]. The control design in [15] is only applicable to single integrator dynamics or systems, which can be reformulated as a single integrator using a change of coordinates and inverse dynamics approach. This paper extends the densitybased controller introduced in [15] to nonlinear systems with drift. Therefore, unlike [15], our approach can be applied to any general nonlinear system that contains drift. In this paper, we introduce the notion of control density function (CDF). The CDF is an extension of the density function, just like CLF is the extension of the Lyapunov function for control systems. The construction of CDF is provided based on [15], which is then utilized to formulate the problem statement as a QP with CDF-based constraints. The CDF-based constraint ensures a nonlinear control system's simultaneous convergence and safety. This contrasts with the approaches given in [5], [6] where one needs to augment CLF constraints with CBF to ensure convergence. Another difference includes almost everywhere convergence of the system dynamics, which is a weaker notion of convergence than control Lyapunov functions. As a result, the control law obtained from CDF constraints ensures convergence for almost all initial conditions. The set of all initial conditions not converging to the target set will have a zero Lebesgue measure [16]. We also provide an example of an underactuated system in the form of the Dubin car model, where obstacles are only present in the subspace of the system dynamics. Finally, unlike [15], we also show that the density-based safe controller can be combined with a nominal controller for optimal performance by modifying the cost function to include the norm of the difference between the desired safe control and the nominal control. The rest of the paper is organized as follows. Section II contains the problem statement and some preliminaries, and Section III consists of the paper's main results. Section IV discusses the computational framework for the prescribed QP. In Section V, we provide some simulation results followed by some conclusions.

## Ii. Preliminaries And Problem Statement

Consider the dynamical system of the form

$$\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})+\mathbf{g}(\mathbf{x})\mathbf{u}\tag{1}$$

where $\mathbf{x}\in D\subseteq\mathbb{R}^{n}$ and $\mathbf{u}\in U\subseteq\mathbb{R}^{m}$ are the states and the control inputs respectively. We also assume that $\mathbf{f},\mathbf{g}\in\mathcal{C}^{1}(D,\mathbb{R}^{n})$ are continuously differentiable functions on $D$. The unsafe sets are represented by $\mathcal{U}\subset D$. Next, $\mathbf{X}_{0},\mathbf{X}_{T}\subset D$ represents the initial set and target set, respectively. In this paper, we assume the target is located at the origin, i.e., $\mathbf{X}_{T}=0$. We represent $s_{t}(\mathbf{x})$ to be the solution of (1) with respect to some control $\mathbf{u}$ at time $t$ starting from the initial condition $\mathbf{x}$. We also denote $\mathcal{B}(D)$ to be the Borel $\sigma$-algebra on $D$ and $\mathcal{M}(D)$ as the vector space of real-valued measures on $\mathcal{B}(D)$ and $m(\cdot)$ denotes Lebesgue measure. Also, we represent $\bar{D}:=D\setminus\mathcal{N}_{\eta}$ where $\mathcal{N}_{\eta}$ represents a small neighborhood of $\eta$ radius around $\mathbf{X}_{T}$. The notation $\nabla_{\mathbf{x}}$ denotes $[\frac{\partial}{\partial x_{1}},\ldots,\frac{\partial}{\partial x_{n}}]^{\top}$ where $\mathbf{x}\in\mathbb{R}^{n}$. Also, $tr(A)$ represents the trace of the matrix $A$.

Problem 1. (Almost everywhere (a.e.) safe navigation) The
primary objective of this paper is to design a control u
to drive the trajectories of the system given by (1) from
almost all initial conditions (w.r.t. Lebesgue measure) from
the initial set X0 to a target set XT while avoiding the
unsafe set U.

A. Density function for safe navigation

  The construction of the density-based safe control for the
dynamics given in (1) is inspired by [15]. We define the
unsafe set U. Let there be K number of obstacles. We define
a continuous scalar-valued function ck(x) for k = 1, . . . , K.
Now, each obstacle set can be defined as follows:

$C_{k}:=\{\mathbf{x}\in D:c_{k}(\mathbf{x})\leq0\}$ (2)
Therefore, the set defining the total unsafe region is given by U := �K
k=1 Ck. Similarly, we will define another continuous scalar-valued function bk(x) to define the sensing region for each obstacle set as follows:

$B_{k}:=\{\mathbf{x}\in D:b_{k}(\mathbf{x})\leq0\}\setminus C_{k}$ (3)
Now, we use the functions ck(x) and bk(x) to formulate a smooth inverse bump function. First, we start by constructing the following functions,

mk = ck(x) ck(x) − bk(x), mk ) ψk(x) = exp( −1 exp( −1 mk ) + exp( −1 1−mk ).
Using the functions mk(x) and ψk(x), we define a piecewise smooth inverse bump function Ψk(x) as follows:

Ψk(x) = 0, x ∈ Ck ψk(x), x ∈ Bk 1, otherwise . (4)     
Note that �K
k=1 Ψk(x) encodes the unsafe set U. To encode information about the target set XT , we use V (x) which acts as a distance function from the current state x to the target state XT . The V (x) can be modified to adjust to the geometry of the underlying configuration space. In the Euclidean space with x ∈ Rn, we use V (x) = (x − XT )⊤P(x − XT )
for some *P >* 0. Finally, the density function ρ(x) for the safe control is given as follows:

ρ(x) = �K k=1 Ψk(x) V (x)α (5)
for some *α >* 0.

It can be observed that the density function ρ(x) given in (5) is a smooth function for all x ∈ D. Fig. 1a shows an environment with one obstacle set U and target XT . Fig.

1b shows the corresponding density function representation. Note that the density function ρ(x) takes minimum value for x *∈ U* and max value for x ∈ XT .

Assumption 1. We assume that system dynamics given by
(1) is locally linearizable inside the region Nη containing
XT = 0. We also assume that the linearized dynamics at
the origin are stabilizable. Therefore the local stability of
XT = 0 can be achieved by designing a local linear feedback
controller.

  The construction of density function in (5) was proposed
in [15] and used for solving the safe navigation problem with

simple integrator dynamics of the form ˙x = u. The feedback
controller u for the safe navigation was shown to be of the
form

$$\mathbf{u}(\mathbf{x})={\frac{\partial\rho}{\partial\mathbf{x}}}\qquad\qquad\qquad(6)$$
This paper's main contribution is introducing the CDF for solving the navigation problem as stated in Problem 1 for nonlinear system (1) with drift.

## Iii. Control Density Function (Cdf)

The density functions can be utilized to check the stability of any nonlinear system [14], [17]. However, such density functions cannot be used to design a safe control. By drawing inspiration from how Lyapunov functions were extended to CLF [18], [19], and how barrier functions were extended to CBF [6], [20], we propose in this section an extension of the density function and call it as the CDF. Let us again consider the nonlinear system as follows:

$\bf x=f(x)+g(x)u$

where u = [u1, . . . , um]⊤ and g(x) = [g1(x), . . . , gm(x)].
All the vector fields are assumed to belong to C1( ¯D, Rn).
  The following theorem provides the main result for the
safe navigation control for a nonlinear system using CDF.

**Theorem 1**.: _Under Assumption 1, given system dynamics in (1) and density function given by (5), the system trajectories can be driven from almost all initial conditions to a target set $\mathbf{X}_{T}$ while avoiding unsafe $\mathcal{U}$ if there exists a control $\mathbf{u}\in U$ and $\lambda>0$ such that_

$$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho+\mathbf{g}(\mathbf{x})\mathbf{u}\rho)\geq0,\ \ a.e.\ \mathbf{x}\in\bar{D}$$ $$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho+\mathbf{g}(\mathbf{x})\mathbf{u}\rho)\geq\lambda>0,\ \ \forall\ \mathbf{x}\in\mathbf{X}_{0}\tag{8}$$

_The proof is provided in the Appendix._
Based on the result of Theorem 1, we see that solving for the desired safe control u is an infinite-dimensional feasibility problem. However, if we assume that f(x), g(x)
and ρ(x) are known to us, then we can solve for u point-wise along the system trajectory by formulating it as QP utilizing the CDF constraints given in (8). The QP-CDF formulation is given below:

$$\min_{\mathbf{u}}\|\mathbf{u}\|^{2}$$ s.t. $$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho+\mathbf{g}(\mathbf{x})\mathbf{u}\rho)\geq0,\ \ a.e.\ \mathbf{x}\in\bar{D}$$ $$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho+\mathbf{g}(\mathbf{x})\mathbf{u}\rho)\geq\lambda>0,\ \ \forall\ \mathbf{x}\in\mathbf{X}_{0}\tag{9}$$

**Remark 1**.: _If there exists a nominal control, $\mathbf{u}_{0}$, for the system given by (7), we can reformulate (9) to enforce $\mathbf{u}_{0}$ in the absence of unsafe sets by introducing a cost function which minimizes $\|\mathbf{u}-\mathbf{u}_{0}\|^{2}$._

## Iv. Computational Framework

The inequality in (8) can be expanded as follows:

$$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho)+\nabla_{\mathbf{x}}^{\top}\left[\mathbf{g}(\mathbf{x})\rho\right]\mathbf{u}+tr\left((\nabla_{\mathbf{x}}\mathbf{u}^{\top})^{\top}\mathbf{g}\rho\right)>0\tag{10}$$

We observe that while trying to solve for $\mathbf{u}$ point-wise along the system trajectory, the term $\nabla u_{i}$ is a spatial operator and 
requires information on points in the neighborhood of the system trajectory. Therefore, to calculate ∇ui, we perturb the point on the trajectory by ϵ along the directional basis to obtain points [z1*, . . . , z*n] where zi ∈ Rn. Here, zi = x+ϵ ei where ei is a column vector consisting of all zeros except at ith position where the value is 1. These points around the trajectory will be used to calculate the ∇ui.

To make things easier, we can split the inequality given in (10) as follows:

$$\nabla\cdot(\mathbf{f}\rho)+\nabla_{\mathbf{x}}^{\top}\left[\mathbf{g}(\mathbf{x})\rho\right]\mathbf{u}\geq\beta\rho$$ $$\left|tr\left((\nabla_{\mathbf{x}}\mathbf{u}^{\top})^{\top}\mathbf{g}\right)\right|<\beta\tag{11}$$

Now we can write $\nabla u_{i}$ as follows:

$$\nabla u_{i}=\left[\frac{u_{i}^{1}-u_{i}}{\epsilon},\ldots,\frac{u_{i}^{n}-u_{i}}{\epsilon}\right]^{\top}\tag{12}$$
where uj = [uj
1, . . . , uj m]⊤ represents the control satisfying
(11) at point zj. This can be written in matrix form for all the m control values as follows:

$$(\nabla_{\mathbf{x}}\mathbf{u}^{\top})^{\top}=\left[\begin{array}{ccc}\frac{u_{1}^{1}-u_{1}}{\epsilon}&\ldots&\frac{u_{1}^{n}-u_{1}}{\epsilon}\\ \vdots&&\\ \frac{u_{m}^{1}-u_{m}}{\epsilon}&\ldots&\frac{u_{m}^{n}-u_{m}}{\epsilon}\end{array}\right]\tag{13}$$

Therefore, we can rewrite (11) as follows:

$$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho(\mathbf{x}))+\nabla_{\mathbf{x}}^{\top}\left[\mathbf{g}(\mathbf{x})\rho(\mathbf{x})\right]\mathbf{u}\geq\beta\rho(\mathbf{x})$$ $$\nabla\cdot(\mathbf{f}(z_{1})\rho(z_{1}))+\nabla_{\mathbf{x}}^{\top}\left[\mathbf{g}(z_{1})\rho(z_{1})\right]\mathbf{u}^{1}\geq\beta\rho(z_{1})$$ $$\vdots$$ $$\nabla\cdot(\mathbf{f}(z_{n})\rho(z_{n}))+\nabla_{\mathbf{x}}^{\top}\left[\mathbf{g}(z_{n})\rho(z_{n})\right]\mathbf{u}^{n}\geq\beta\rho(z_{n})$$ $$\left|tr((\nabla_{\mathbf{x}}\mathbf{u}^{\top})^{\top}\ \mathbf{g}(\mathbf{x}))\right|<\beta\tag{14}$$

Here, the number of decision variables to solve the above linear inequalities will be $m(n+1)$. The algorithm 1 summarizes the steps to solve for safe navigation control using QP-CDF as given in (9).

Remark 2. The value of α determines the rate of conver-
gence towards the target set. This stems from the fact that
α appears in the distance function V (x) which contains
information on the target set. It can be inferred that the
convergence rate can be increased by increasing the value
of α and vice-versa. Similarly, increasing the sensing region
around the obstacle will lead to smoother avoidance control,
and decreasing the sensing region will lead to more aggres-
sive avoidance control near the obstacle.

## V. Simulation Results

In this section, we provide some navigation results for different types of system dynamics starting with the Duffing oscillator.

## Algorithm 1: Qp-Cdf

Input: f, g, ρ, x0, β, N
for k = 1 : N do

zj = xk−1 + ej ∀ j = 1*, . . . , n*. Solve for uk, u1 k, . . . , un k do min ∥uk∥2+∥u1 k∥2+ · · · + ∥un k∥2 s.t. ∇ · (f(xk−1)ρ(xk−1))+ ∇⊤ x [g(xk−1)ρ(xk−1)] uk *> βρ*(xk−1), ∇ · (f(z1)ρ(z1) + ∇⊤ x [g(z1)ρ(z1)] u1 k > βρ(z1), ... xk = xk−1 + ∆t(f(xk−1) + g(xk−1)uk) ∇ · (f(zn)ρ(zn) + ∇⊤ x [g(zn)ρ(zn)] un k > βρ(zn), ��tr((∇xu⊤ k )⊤ g(xk−1)) �� < β

## A. Duffing Oscillator

Let us consider the Duffing oscillator dynamics:

$$\dot{x}_{1}=x_{2}$$ $$\dot{x}_{2}=x_{1}-x_{1}^{3}-0.1x_{2}+u\tag{15}$$
Fig. 2 provides a safe navigation control trajectory for the Duffing oscillator by solving QP-CDF. The density function is constructed based on equations (4) and (5). The functions used to describe the obstacle set are given by c(x) :=
∥x − o∥2−r2
1 where o and r1 are the center and radius of the circular obstacle respectively. Similarly, the function used to define sensing region is given by b(x) := ∥x − o∥2−r2
2
where r2 is the radius of the sensing region of the circular obstacle. Here, the obstacle radius is 0.5 units and the sensing radius is 0.7 units with its center located at [0, 0]. The matrix P used to construct the function V (x) is obtained by linearizing the dynamics around the target point and solving the algebraic Riccati equation with the identity matrix as the state and control gain matrix. Here, the control bounds are
±2. It can be observed that the control action obtained from the QP-CDF is minimally invasive. The system trajectories follow along the vector field of the Duffing oscillator when it is away from the obstacle. The control from the QP-CDF is mainly active near the obstacles by making the system trajectories drive away from the obstacles while trying to converge to the target set.

## B. Dubin Car Model

Let us consider the Dubin car model as follows:

$\dot{x}_{1}=v\cos(\theta)$ (16a) $\dot{x}_{2}=v\sin(\theta)$ (16b) $\dot{\theta}=\omega$ (16c)
where u and ω are the control inputs. We assume that the obstacles to be avoided are only present in the x1−x2 space.

In this example, we first reformulate (16a)-(16b) in the form of single integrator dynamics as given in (17) and solve for u1 and u2 using the QP-CDF given in (9). These control values will be then utilized in the design of v and ω. The single integrator dynamics in the x1−x2 space is as follows:

$$\dot{x}_{1}=u_{1}\tag{17a}$$ $$\dot{x}_{2}=u_{2}\tag{17b}$$

The safe control for (17) is obtained by solving the QP-CDF given in (9). Here, $c_{k}({\bf x}):=\|{\bf x}-o_{k}\|^{2}-r_{1k}^{2}$ and $b_{k}({\bf x}):=\|{\bf x}-o_{k}\|^{2}-r_{2k}^{2}$ where $o_{k}$, $r_{1k}$ and $r_{2k}$ are the center, radius and sensing radius of the $k^{th}$ circular obstacle. The control obtained as the solution of the QP-CDF can be used to calculate $u$ and $\tilde{\theta}$ as follows:

$$v=\sqrt{u_{1}^{2}+u_{2}^{2}},\quad\tilde{\theta}=\tan^{-1}\left(\frac{u_{2}}{u_{1}}\right)\tag{18}$$

Now, the control $\omega$ needs to be designed such that $\theta-\tilde{\theta}$ tends to zero. Therefore, we consider the Lyapunov function given by $0.5(\theta-\tilde{\theta})^{2}$ which gives us the following control law for $\omega$:

$$\omega=\dot{\tilde{\theta}}-k(\theta-\tilde{\theta})\tag{19}$$
for some *k >* 0. Fig. 3 provides a safe navigation trajectory for the unicycle model in x1−x2 space. The obstacle radius is
2 units and the sensing radius is 2.5 units with the center for the two obstacles located at [3, 1] and [7.5, −1] respectively.

The value of gain k is chosen to be 10. The control action mainly drives the system trajectories away from the obstacle set while converging on the target set.

## Vi. Conclusion

The problem of safe navigation of nonlinear dynamical systems is considered. We introduce the notion of CDF as an extension to the density-based controllers. The CDF- based safety constraints are inspired by the occupancy-based interpretation of the measure associated with the density function. We then formulate the navigation problem with safety constraints as a QP using CDF. The existing approach for navigation problems includes CBF-based QP. The advantage of CDF-based QP over CBF-based QP is that both the convergence and safety constraints can be imposed using CDF. Finally, we provide simulation results for safe navigation of the Dubin car model and Duffing oscillator to showcase the validity of CDF-based QP.

## Vii. Appendix

The proof of Theorem 1 relies on the following Lemma.

**Lemma 1**.: _If_

$$\int_{0}^{\infty}\int_{{\bf X}_{0}}1_{{\cal U}}(s_{t}({\bf x}))d{\bf x}\;dt=0\tag{20}$$

_then_

$$\int_{{\bf X}_{0}}1_{{\cal U}}(s_{t}({\bf x}))d{\bf x}=0\;\;\;\forall t\geq0\tag{21}$$

_i.e., the amount of time system trajectories spend in set ${\cal U}$ starting from the positive measure set ${\bf X}_{0}$ is equal to zero._

**Proof:** The proof is done by the method of contradiction. Let us assume (21) is not true. Then there exists a time $\bar{t}$ such that

$$\int_{{\bf X}_{0}}1_{{\cal U}}(s_{\bar{t}}({\bf x}))d{\bf x}>0.$$

Now, from the continuity of the solution of the differential equation, there exists a $\Delta$ such that

$$\int_{\bar{t}}^{\bar{t}+\Delta}\int_{{\bf X}_{0}}1_{{\cal U}}({\bf s}_{t}({\bf x}))d{\bf x}\;dt>0$$
Therefore,

$$\begin{array}{l}{{0<\int_{\bar{t}}^{\bar{t}+\Delta}\int_{{\bf X}_{0}}1_{{\cal U}}({\bf s}_{t}({\bf x}))d{\bf x}\;d t}}\\ {{\leq\int_{0}^{\infty}\int_{{\bf X}_{0}}^{\bar{t}}1_{{\cal U}}(s_{t}({\bf x}))d{\bf x}\;d t=0.}}\end{array}$$
Hence, we arrive at a contradiction.

Proof of Theorem 1: Let us consider the following:

$$\nabla\cdot(\mathbf{f}(\mathbf{x})\rho+\mathbf{g}(\mathbf{x})\mathbf{u}\rho)=h(\mathbf{x})\tag{22}$$

where $h(\mathbf{x})\geq0$ and $h(\mathbf{x})\geq\lambda>0$ for $\mathbf{x}\in\mathbf{X}_{0}$. Now, through the method of characteristics, the function $\rho(\mathbf{x})$ can be written as follows:

$$\rho(\mathbf{x})=\int_{0}^{\infty}h(s_{-t}(\mathbf{x}))\left|\frac{\partial s_{-t}(\mathbf{x})}{\partial\mathbf{x}}\right|dt,\tag{23}$$

where $|\cdot|$ represents the determinant. This can be easily verified by simple substitution of (23) in (22) and using the fact that

$$\lim_{t\rightarrow\infty}h(s_{-t}(\mathbf{x}))\left|\frac{\partial s_{-t}(\mathbf{x})}{\partial\mathbf{x}}\right|=0.\tag{24}$$

The limit in (24) is the consequence of $\rho(\mathbf{x})$ being bounded in $\bar{D}$ and using Barbalat's Lemma. The term inside the integral in (23) can be written using the linear Perron-Frobenius (P-F) operator as follows:

$$\partial\mathbf{x}$$
Therefore,

[Pth](x) = h(s−t(x)) ���� ∂s−t(x) ���� . (25) 0 [Pth](x)dt. (26) ρ(x) = � ∞
Now, utilizing (24), we can write

lim t→∞[Pth](x) = 0 =⇒ lim t→∞[Pt1X0](x) = 0 (27) ¯ D [Pt1X0](x)1A(x)dx
which follows because h(x) ≥ *λ >* 0 ∀x ∈ X0 and using dominated convergence theorem. Here, 1X0 represents the indicator function for X0. Now, for any A ⊆ ¯D, we have
�

A [Pt1X0](x)dx = � ¯ D 1X0(x)1A(st(x))dx (28) = �

This can be observed by using the definition of P-F operator
in (25) and doing the change of variables in integration such
as y = s−t(x) and dy =
                          ��� ∂s−t(x)

A [Pt1X0](x)dx = m{x ∈ X0 : st(x) ∈ A}.
∂x
��� dx and relabelling. The right hand side of (28) can be seen as follows:
�
Therefore, using (27), we observe that

A [ lim t→∞ Pt1X0](x)dx = m{x ∈ X0 : lim t→∞ st(x) ∈ A}. 0 = �
The above statement can be generalized for any measurable Lebesgue set A ⊆ ¯D. Therefore,

m{x ∈ X0 : lim t→∞ st(x) ̸= 0} = 0. U ρ(x)dx = 0. (29) U 0 [Pt1X0](x)dtdx ≤ �
Now, from the construction of the density function, we know that ρ(x) = 0 ∀ x *∈ U*. Therefore,
�

� ∞ 0 [Pt1X0](x)dtdx = 0. (30) U
Utilizing the Markov property of the P-F operator and the fact that indicator functions are non-negative functions, we can rewrite (29) as follows:
�

� ∞
Now, doing the change of variables in integration such as y = s−t(x) and dy =
��� ∂s−t(x)

¯ D 0 [Pt1X0](x)1U(x)dtdx U
∂x
��� dx and relabelling, the lefthand side of the (30) can be written as follows:
�

� ∞ 0 [Pt1X0](x)dtdx = � � ∞ 0 ¯ D 1X0(x)1U(st(x))dx dt = � ∞ � 0 X0 1U(st(x))dx dt = 0. (31) = � ∞ � X0 1U(st(x))dx = 0 ∀t ≥ 0
Now, from (31) and using Lemma 1, we can conclude the following:
�

## References

[1] O. Khatib, "Real-time obstacle avoidance for manipulators and mobile
robots," *The international journal of robotics research*, vol. 5, no. 1,
pp. 90–98, 1986.
[2] B. Krogh, "A generalized potential field approach to obstacle avoidance control," in Proc. SME Conf. on Robotics Research: The Next Five Years and Beyond, Bethlehem, PA, 1984, 1984, pp. 11–22.
[3] E. Rimon, *Exact robot navigation using artificial potential functions*.
Yale University, 1990.
[4] M. Z. Romdlony and B. Jayawardhana, "Uniting control lyapunov and
control barrier functions," in 53rd IEEE Conference on Decision and
Control.
IEEE, 2014, pp. 2293–2298.
[5] A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, "Control barrier
function based quadratic programs for safety critical systems," IEEE
Transactions on Automatic Control, vol. 62, no. 8, pp. 3861–3876,
2016.
[6] A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath,
and P. Tabuada, "Control barrier functions: Theory and applications," in *2019 18th European control conference (ECC)*.
IEEE, 2019, pp.
3420–3431.
[7] A. Rantzer, "A dual to lyapunov's stability theorem," Systems &
Control Letters, vol. 42, no. 3, pp. 161–168, 2001.
[8] A. Rantzer and S. Prajna, "On analysis and synthesis of safe control
laws," in 42nd Allerton Conference on Communication, Control, and Computing.
University of Illinois, 2004, pp. 1468–1476.
[9] U. Vaidya, "Optimal motion planning using navigation measure,"
International Journal of Control, vol. 91, no. 5, pp. 989–998, 2018.
[10] Y. Chen, M. Ahmadi, and A. D. Ames, "Optimal safe controller
synthesis: A density function approach," in 2020 American Control
Conference (ACC).
IEEE, 2020, pp. 5407–5412.
[11] X. Ma, B. Huang, and U. Vaidya, "Optimal quadratic regulation of
nonlinear system using koopman operator," in 2019 American Control Conference (ACC).
IEEE, 2019, pp. 4911–4916.
[12] B. Huang and U. Vaidya, "A convex approach to data-driven optimal
control via perron-frobenius and koopman operators," IEEE Transactions on Automatic Control, 2022.
[13] H. Yu, J. Moyalan, U. Vaidya, and Y. Chen, "Data-driven optimal
control of nonlinear dynamics under safety constraints," IEEE Control
Systems Letters, vol. 6, pp. 2240–2245, 2022.
[14] J. Moyalan, H. Choi, Y. Chen, and U. Vaidya, "Data-driven optimal
control via linear transfer operators: A convex approach," *Automatica*,
vol. 150, p. 110841, 2023.
[15] A. Zheng, S. S. Narayanan, and U. Vaidya, "Safe navigation using
density functions," *IEEE Robotics and Automation Letters*, 2023.
[16] J. Moyalan, H. Choi, Y. Chen, and U. Vaidya, "Sum of squares
based convex approach for optimal control synthesis," in 2021 29th Mediterranean Conference on Control and Automation (MED). IEEE,
2021, pp. 1270–1275.
[17] R. Rajaram, U. Vaidya, M. Fardad, and B. Ganapathysubramanian,
"Stability in the almost everywhere sense: A linear transfer operator approach," *Journal of Mathematical analysis and applications*, vol.
368, no. 1, pp. 144–156, 2010.
[18] Z. Artstein, "Stabilization with relaxed controls," Nonlinear Analysis:
Theory, Methods & Applications, vol. 7, no. 11, pp. 1163–1173, 1983.
[19] E. D. Sontag, "A lyapunov-like characterization of asymptotic controllability," *SIAM journal on control and optimization*, vol. 21, no. 3,
pp. 462–471, 1983.
[20] P. Wieland and F. Allgöwer, "Constructive safety using control barrier
functions," *IFAC Proceedings Volumes*, vol. 40, no. 12, pp. 462–467, 2007.