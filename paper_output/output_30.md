# Pursuit-Evasion On A Sphere And When It Can Be Considered Flat

Dejan Milutinovi´c, Alexander Von Moll, Satyanarayana G. Manyam, David W. Casbeer, Isaac E. Weintraub, and Meir Pachter

  Abstract— In classical works on a planar differential pursuit-
evasion game with a faster pursuer, the intercept point resulting
from the equilibrium strategies lies on the Apollonius circle.
This property was exploited for the construction of the equi-
librium strategies for two faster pursuers against one evader.
Extensions for planar multiple-pursuer single-evader scenarios
have been considered. We study a pursuit-evasion game on
a sphere and the relation of the equilibrium intercept point
to the Apollonius domain on the sphere. The domain is a
generalization of the planar Apollonius circle set. We find
a condition resulting in the intercept point belonging to the
Apollonius domain, which is the characteristic of the planar
game solution. Finally, we use this characteristic to discuss
pursuit and evasion strategies in the context of two pursuers
and a single slower evader on the sphere and illustrate it using
numerical simulations.

          I. INTRODUCTION AND BACKGROUND
  The Apollonius circle is a concept that has been used
to address solutions of multiple non-cooperative pursuit-
evasion (P-E) differential games under simple motion in the
plane [1]. It is the set of points that can be reached by
E sooner than P, i.e., it is the dominance region of E. In
the same reference [1], the solution of the two pursuer and
single slower evader differential game is inferred from the
intersection of Apollonius circles. The problem was revisited
and solved in [2] and the Apollonius circle construct was
applied as a building block for the solution of a game with
multiple pursuers [3] in the plane. For P-E differential games
on a sphere with a slower E, the dominance of E is not a
circle [4], therefore, we denote it as the Apollonius domain.

This paper investigates the P-E game of min-max capture time equilibrium strategies on a sphere for a slower E and simple motion of both players, and examines their outcome against the Apollonius domain. In the planar case, the intercept point resulting from equilibrium strategies lies on the Apollonius circle, and here we investigate conditions This paper is based on work performed at the Air Force Research Laboratory (AFRL) *Control Science Center* and is supported by AFOSR LRIR 24RQCOR002. DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited. AFRL-2024-1467; 18 MAR 2024.

D.

Milutinovi´c is with Electrical and Computer Engineering Dept., University of California, Santa Cruz, Santa Cruz, CA, USA
dejan@ucsc.edu A. Von Moll, D. Casbeer, and I. Weintraub are with the Control Science Center, Aerospace Systems Directorate, Air Force Research Laboratory, Dayton, OH 45435, USA alexander.von moll@us.af.mil, david.casbeer@us.af.mil, isaac.weintraub.1@us.af.mil S.

Manyam is with DCS
Corporation, Dayton, OH, USA, smanyam@infoscitex.com M.

Pachter is with Dept.

of Electrical Engineering, Air Force Institute of Technology, Wright-Patterson AFB, OH, USA, meir.pachter@afit.edu for the P-E game on a sphere that result in the intercept point lying on the Apollonius domain. Under these conditions, we discuss P-E strategies for games on a sphere with multiple Ps and a single E in a similar fashion as in [3].

Related works: If two players move in a plane and when both of them apply their equilibrium strategies, the corresponding equilibrium trajectories are straight lines. As pointed out in [5] when a pursuer and an evader have simple motion over a 2D Riemannian manifolds, the same holds when the players are sufficiently close, except that instead of straight lines, the trajectories are along manifold shortest paths, i.e., geodesics. However, when the players are far from each other, there may be multiple geodesics of the same length, which requires an additional analysis. Using this perspective, the authors in [5], [6] analyzed multiple manifolds, but not a sphere. Note that when P and E are on the opposite sides of a sphere and on the same line with the center of the sphere, there are infinitely many geodesics between P and E. The P-E game on a sphere was the topic of [4], but under the condition that P always knows E's velocity. Another related paper is [7] which discusses sufficient conditions for a P-E solution. A P-E on a sphere also appears in popular culture [8] in a graphic novel, in which, on a very small planet, the main character, Goku, must catch a pet monkey, Bubbles, to prove he is worthy to be trained by Master Kai.

Since the P-E solution in this paper results in feedback strategies for P and E, it is worth pointing to other works on feedback control on a sphere. These include the stabilization of collective motion [9], motion coordination in a spatiotemporal flow-field [10], the control of multi agents on a sphere to achieve different spherical patterns [11] and consensus on a sphere [12], the stabilization of bilinear systems [13] and collision-free motion coordination using barrier functions [14].

Paper contributions: We revisit here the problem of P-E
on a sphere, in which P and a slower E have simple motion. Our analysis relies on the Hamilton-Jacobi-Isaacs equation
(HJI), which allows us to derive equilibrium strategies for both players, except for a special game configuration in which there are infinitely many geodesics connecting P and E. The special configuration is the one in which P and E are on the opposite sides of the sphere and on the same line with the center of the sphere. Due to the multiplicity of solutions, the condition of the game is similar to the presence of the dilemma. Therefore, we use the value function and associated rate of loss [15], which allows us to obtain unique equilibrium strategies on the whole sphere surface. With this, we also obtain the corresponding intercept point and using results from [4], we are able to obtain the condition resulting in the intercept point in the Apollonius domain.

The paper is organized as follows. The problem formulation in Section II is followed by the P-E game analysis and equilibrium strategies in Section III. Section IV is about a relation between the intercept point resulting from the equilibrium strategies and the Apollonius domain. Section V shows examples illustrating paper results and Section VI gives conclusions.

## Ii. Problem Description

Consider two agents restricted to motion on a spherical surface, see Fig. 1: a pursuer (P) and a slower evader (E).

Both P and E move on the spherical surface and their positions are defined as the corresponding vectors

$$\vec{P}=R\cos\varphi_{P}\cos\theta_{P}\vec{i}+R\cos\varphi_{P}\sin\theta_{P}\vec{j}+R\sin\varphi_{P}\vec{k},$$ $$\vec{E}=R\cos\varphi_{E}\cos\theta_{E}\vec{i}+R\cos\varphi_{E}\sin\theta_{E}\vec{j}+R\sin\varphi_{E}\vec{k}.\tag{1}$$

Due to their constrained motion on the sphere's surface, the vectors $\vec{E}$ and $\vec{P}$ defining the positions of $E$ and $P$ always have the same magnitudes $|\vec{E}|=|\vec{P}|=R$ (see Fig. 1). The velocities $\vec{v}_{E}$ and $\vec{v}_{P}$ of $E$ and $P$, respectively, are

$$\vec{v}_{E}=v_{E}\vec{e},0\leq v_{E}\leq\mu v_{P}\tag{2}$$ $$\vec{v}_{P}=v_{P}\vec{p},v_{P}=\mbox{const},0<\mu<1,\tag{3}$$
where ⃗e and ⃗p are unit vectors tangential to the sphere representing the agent's direction of travel, and vE and vP
representing the corresponding speed; this implies ⃗vE · ⃗E =
⃗vP · ⃗P = 0.

The control variable of P is only the velocity direction ⃗p, while the control variables of E are both the speed vE and the velocity direction ⃗e. The speed ratio µ ∈ (0, 1) is the ratio of E's maximal speed and P's speed vP ; therefore, P
is faster than E.

P-E game: The two agents are initially at different locations of the sphere and when P *is collocated with* E, we say that P has *captured* E. The capture time τ is the length of time that it takes P and E to move from their initial positions to when P captures E, or formally

$$\tau=\inf\{t\mid\vec{E}=\vec{P}\}.\tag{4}$$
The goal of P is to select its sequence of actions to minimize the capture time, while the goal of E is to select its sequence of actions that will maximize the capture time.

Problem: We analyze here the pursuit evasion problem on the sphere and find the equilibrium (i.e., the saddle point or Nash-equilibrium) strategies {⃗v∗
P ,⃗v∗
E} for P and E, respectively. They are optimal in a sense that if both P
and E commit to them, then the capture time is τ ∗(⃗v∗
P ,⃗v∗
E).

However, if P (E) gives up its equilibrium strategy and applies any other action at any time point, it will extend (shorten) time to capture. This can be expressed as

$$\tau(\vec{v}_{P}^{*},\vec{v}_{E})\leq\tau^{*}(\vec{v}_{P}^{*},\vec{v}_{E}^{*})\leq\tau(\vec{v}_{P},\vec{v}_{E}^{*}).\tag{5}$$

The capture time $\tau^{*}$ is also called the Value of the game. Our goal is to find equilibrium strategies for $P$ and $E$, as well as the Value function. Then we will examine the relative position between the equilibrium intercept point (i.e., the intercept point resulting from both players applying their equilibrium strategies) and the Apollonius domain, which is defined as follows.

_Definition 1: Apollonius domain $\mathcal{A}$_. Let us assume that at the initial time $t=0$, the positions of $P$ and $E$ on a sphere are $P(0)$ and $E(0)$, $P(0)\neq E(0)$. The Apollonius domain, $\mathcal{A}$, is a closed set of points $I$ on the sphere defined as

$$\mathcal{A}=\left\{I\ |\ \widehat{\widehat{E}(0)}\leq\widehat{\widehat{IP}(0)}\over v_{P}}\right\},\tag{6}$$

where $\widehat{IE}(0),\widehat{IP}(0)$ are lengths of arcs from $E(0)$ and $P(0)$ to $I$, respectively, while $\widehat{IE}(0)/\mu v_{P}$ and $\widehat{IP}(0)/v_{P}$ are the corresponding times for $E$ and $P$ to reach $I$ using their maximal speeds.

## Iii. Pursuit-Evasion Equilibrium Strategies

Pre 2 Inverse that: the exact three-point $E$ and $P$ define a $\mu$ parameter:

$$\widetilde{\mu}_{\rm G}\equiv-\frac{1}{16}\,P\,\widetilde{E}\,,\tag{7}$$

The second-point difference, $\alpha$, is the angle between $\widetilde{\alpha}$ and $E$ and $\mu$, the maximum distance $\widetilde{\beta}$. For $\widetilde{\alpha}$ and the right hand side,

$$\widetilde{\alpha}_{\rm G}\equiv-\frac{1}{16}\,P\,\widetilde{E}\,,\tag{8}$$

where $\widetilde{\alpha}$ is a positive real value at equal $E$ and $P$. The $P$-function $\widetilde{\alpha}$ is a positive real value at equal $E$. The $P$-function $\widetilde{\alpha}$ is a positive real value at equal $E$, and the maximum value of $P$ for $\widetilde{\alpha}$. The $P$-function $\widetilde{\alpha}$ is a positive real value at equal $E$. The $P$-function $\widetilde{\alpha}$ is a positive real value at equal $E$, and the $\widetilde{\alpha}$-function is the measure of $\widetilde{\alpha}$ to $E$. The $P$-function $\widetilde{\alpha}$ is a positive real value at equal $E$.

$$\alpha=\begin{cases}\alpha_{0}&E\neq0\\ \alpha_{1}&\beta=-E\end{cases}$$

where $\alpha_{1}$ is the total vector between $E$. One (2) is $\alpha$ and $\beta$. The $\alpha$-function $\widetilde{\alpha}$ is a positive real value at $E$.

$$\widetilde{\alpha}_{\rm G}=\varepsilon_{\rm G}\,v=v\,v\,(\cos\mu v_{\rm G}t+\sin\mu v_{\rm G}t)\tag{9}$$

Using the exact vector $\widetilde{\alpha}_{\rm G}$ and $v$, $\widetilde{\alpha}_{\rm G}$ is the vector $\widetilde{\alpha}_{\rm G}$, $\widetilde{\alpha}_{\rm G}$ is the $\widetilde{\alpha}$-function, $v$ is the $\widetilde{\alpha}$-function. The $P$-function $\widetilde{\alpha}$ is a positive real value at $E$. The $P$-function $v$ is the $\widetilde{\alpha}$-function.

 where $\tau$ is the capture time at which $\alpha(\tau)=0$. The goal of $P$ is to minimize $J$, i.e., time to capture and the goal of $E$ is to maximize it. Theorem 1 defines equilibrium strategies for $P$ and $E$ and their relative angular distance $\alpha\in(0,\pi)$. This is followed by Lemma 1 about the case $\alpha=\pi$ and all the 
results are summarized in Theorem 2 providing equilibrium strategies for P-E relative positions α ∈ (0, π].

Theorem 1. For the P-E game on a sphere with agent
kinematics (8)-(9)*, time to capture cost* (11) and
(a) The relative angular position between P and E is
α ∈ (0, π) *and obeys* (10)
(b) P has constant speed vP , the control variable is heading uP ∈ [0, 2π) and the goal to minimize the time to
capture
(c) The control variables for E are speed vE ∈ [0*, µv*P ]
and heading uE ∈ [0, 2π), and E has the goal to
maximize the time to capture,
the saddle point equilibrium strategies for all α ∈ (0, π) are
defined by
$u_{P}=0$ and $(v_{E},u_{E})=(\mu v_{P},0)$. (12)
Moreover, if both players are at the relative angular position
α ∈ (0, π) and follow their equilibrium strategies, the time to capture is

$$V(\alpha)=R\alpha((1-\mu)v_{P})^{-1}.\tag{13}$$

Proof: The equilibrium strategies satisfy the Hamilton-Jacobi-Isaacs (HJI) equation

$$\min_{u_{P}}\max_{(v_{E},u_{E})}\left\{\left(\frac{v_{E}}{R}\cos u_{E}-\frac{v_{P}}{R}\cos u_{P}\right)\frac{\partial V}{\partial\alpha}+1\right\}=0,\tag{14}$$

where $V(\alpha)$ is the Value of the game (see Remark 1), the minimization is over the variable $u_{P}$ defining the heading of $P$ and the maximization is over the speed $v_{E}$ and variable $u_{E}$ defining the heading of $E$. When the min and max operators are applied, we obtain

$$\max_{(v_{E},u_{E})}\left\{\frac{v_{E}}{R}\cos u_{E}\frac{\partial V}{\partial\alpha}\right\}+\min_{u_{P}}\left\{-\frac{v_{P}}{R}\cos u_{P}\frac{\partial V}{\partial\alpha}\right\}+1=0.\tag{15}$$

The fact that max and min operators are separable reinforces that the strategies in (14) are saddle point strategies. The game is defined over variable $\alpha$ and since $\alpha=0$ corresponds to the capture, we know that $V(0)=0$. Also, we know that for an incrementally larger angular distance $\alpha\in(0,\pi)$, the game lasts incrementally longer, i.e., $\frac{\partial V}{\partial\alpha}>0$. Therefore, we can conclude.

∂α > 0.

Therefore, we can conclude

- min in the second term of (15) is achieved for uP = 0,
which is the equilibrium P strategy for α ∈ (0, π)
* max in the first term of (15) is achieved for $v_{E}=\mu v_{P}$, $u_{E}=0$, which is the equilibrium $E$ strategy for $\alpha\in(0,\pi)$.

_These facts prove the equilibrium actions in (12)_.

When we substitute the equilibrium strategies in (15), we obtain

$$\frac{\mu v_{P}}{R}\,\frac{\partial V}{\partial\alpha}\,-\,\frac{v_{P}}{R}\,\frac{\partial V}{\partial\alpha}+1=0.$$

Re-arranging, we obtain

$$\frac{\partial V}{\partial\alpha}=\frac{R}{(1-\mu)v_{P}}.$$

Finally, since $V(0)=0$, we can conclude that

$$V(\alpha)=\frac{R\alpha}{(1-\mu)v_{P}},$$
which is (13) and that concludes our proof. Remark 1. The cost function resulting from both agents following their equilibrium strategies is also called the Value of the game, hence the symbol V in (13).

In Lemma 1, we discuss the special case when the game starts from the initial position α
=
π. In this case, the great circle is not well defined and there are infinitely many great circles that go through P and E, yet the angular distance α measured along any of them is α = π. Remark 2. The essential problem with α = π is that without a well-defined great circle, there are no reference directions for measuring angles uE and uP .

Lemma 1. For all conditions of Theorem 1, except (a)
which is replaced with (a′): the relative position α = π, the equilibrium actions for P and E are

$$u_{P}=\text{any direction}\tag{16}$$ $$(v_{E},u_{E})=(0,u_{E}),\quad u_{E}\in[0,2\pi),\tag{17}$$

_where $u_{E}$ is measured with respect to a great circle aligned with the direction of motion selected by $P$. The equilibrium action for $E$ corresponds to_

$$\min_{v_{E}}\max_{u_{E}}\mathcal{L}(v_{E},u_{E})=\max_{u_{E}}\min_{v_{E}}\mathcal{L}(v_{E},u_{E})=\tfrac{\mu}{1-\mu},$$ $$\mathcal{L}(v_{E},u_{E})=\frac{\mu-\frac{v_{E}}{v_{P}}\cos u_{E}}{1-\mu},v_{E}\in[0,\mu v_{P}],u_{E}\in[0,2\pi).$$

Proof.: Due to infinitely many great circles that we can consider to measure $\alpha$, we are free to take the one which is aligned with the selected direction of motion by $P$. Because of that, whatever direction is selected by $P$, its $u_{P}=0$ since the adopted great circle is aligned with its motion, but $u_{E}$ has to be also measured with respect to the same great circle. The relative angle on the adopted great circle for $\alpha=\pi$ satisfies

$$\dot{\alpha}=\tfrac{v_{E}}{R}\cos u_{E}-\tfrac{v_{P}}{R}<0,\tag{18}$$

which follows from $v_{E}\leq\mu v_{P}$ and $0<\mu<1\Rightarrow v_{E}<v_{P}$. In other words, on the adopted great circle where $u_{P}=0$ and for $\alpha(0)=\pi$, any action of $E$ results in

$$(v_{E},u_{E})\in\{[0,\mu v_{P}]\times[0,2\pi)\}\Rightarrow\alpha(0^{+})<\pi,\tag{19}$$
and we can conclude that at t = 0+, the great circle is well defined. Consequently, for any *t >* 0+, both P and E
can follow their equilibrium strategies from Theorem 1 since α(t) *< π* for all *t >* 0+.

However, for t = 0 and the adopted great circle (uP = 0)
in (18), we can only state that uE ∈ [0, 2π) which is measured with respect to the adopted great circle. It is because the adopted great circle, i.e., the direction of motion selected by P is unknown to E. Therefore, whatever heading direction is selected by E, the best we can say is that uE ∈ [0, 2π). To find equilibrium actions at t = 0, we will use the rate-of-loss analysis [15] which starts with the following reasoning.

Let us assume that at t = 0, α(0) = π and both P and E commit their control variable selections that hold for a very short (hold time) time h ≈ 0, *h >* 0. As was previously discussed, due to the adopted great circle at t = 0, we always have uP = 0; therefore after h, the value α(h) is

$$\alpha(h)=\pi+{\frac{v_{E}h\cos u_{E}}{R}}-{\frac{v_{P}h}{R}}<\pi-{\frac{v_{P}-v_{E}}{R}}h<\pi.$$
Since α(h) *< π*, Theorem 1 provides strategies for both P
and E, and the resulting time to capture is h + V (α(h)), which depends on where α landed after the initial hold time h. In general, h+V (α(h)) can be different from V (α(0)). To measure that discrepancy as h → 0, we use the instantaneous rate-of-loss

h (20) L = − lim h→0 V (α(h)) − V (α(0)) + h R ) � � R(π + vEh cos uE−vP h = − lim h→0 1 h (1 − µ)vP − Rπ (1 − µ)vP + h = −vE cos uE − vP 1−µ vP cos uE � µ − vE � ≥ 0. (1 − µ)vP − 1 = 1 (21)
This is the rate-of-loss from the prospective of E. Its loss is reflected in the shortening of its time to capture, hence we included the "–" sign in front of the limit of (20) to be able to discuss the rate-of-loss in terms of a non-negative value.

In expression (21), the rate of loss L = L(vE, uE) and for any vE ∈ [0*, µv*P ] the maximum of loss L(vE, uE)
corresponds to uE = −π, i.e.,

1−µ vP � µ + vE � . max uE L(vE, uE) = 1 1−µ (22)
We focus on this max of the rate-of-loss as the worst case scenario since uE does not know the selected direction of movement by P, i..e, the orientation of the adopted great circle. This max increases with vE, so the only way that E
can minimize it is to select vE = 0 and we can conclude that min vE max uE L(vE, uE) =
µ
corresponds to action (0, uE), uE = [0, 2π), which proves the property of the equilibrium action for E in (17).

Alternately, rather than first minimizing over uE, if we initially apply minimization over vE from (21), we obtain

vP cos uE 1−µ , cos uE ≥ 0 vP cos uE l2 = µ− 0 min vE L(vE, uE) =   1−µ , cos uE < 0.  l1 = µ− µvP
Then, when we apply max over uE ∈ [0, 2π), we see that l1 reaches the max value l1 =
µ
1−µ, but only if uE = π/2.

Since E does not know the orientation of the adopted great circle, it cannot use that value. On the other hand, the max value l2 =
µ

           1−µ is reached not only for cos uE < 0, but for
any angle uE ∈ [0, 2π). From this and (22), we can finally
conclude that the equilibrium action for E which is (0, uE),
uE ∈ [0, 2π) corresponds to the saddle point

$$\min_{v_{E}}\max_{u_{E}}\mathcal{L}(v_{E},u_{E})=\max_{u_{E}}\min_{v_{E}}\mathcal{L}(v_{E},u_{E})=\frac{\mu}{1-\mu},\tag{23}$$
which proves (1) and with this, we conclude our proof.

We finish this section with Theorem 2 which summarizes results from Theorem 1 and Lemma 1.

**Theorem 2**.: _For all conditions of Theorem 1 except (a) which is replaced with $(a^{\prime\prime})$: all possible relative positions $\alpha\in(0,\pi]$, the equilibrium actions for $P$ and $E$ are_

$$u_{P}=\begin{cases}0,&\alpha\in(0,\pi)\\ \text{any direction},&\alpha=\pi\end{cases}\tag{24}$$ $$(v_{E},u_{E})=\begin{cases}(\mu v_{P},0),&\alpha\in(0,\pi)\\ (0,\text{any direction}),&\alpha=\pi.\end{cases}\tag{25}$$

_For any initial condition $\alpha\in(0,\pi]$, and $P$ and $E$ following their equilibrium strategies, the time to capture is_

$$\tau\leq V(\alpha)=\frac{R\alpha}{(1-\mu)v_{P}},\quad\text{for}\alpha\neq\pi,\tag{26}$$
and for α = π the difference

$V(\pi)-\tau=\varepsilon>0$, (27)
where ε is an infinitesimally small value, ε → 0.

Proof. The equilibrium actions in (24) and (25) follow directly from Theorem 1 and Lemma 1 covering the cases
α ∈ (0, π) and α = π, respectively. In (17), Lemma 1
states that uE ∈ [0, 2π) and here we restate it as uE = any direction since the range for uE covers all possible angles. Also note that the angle uE is measured with respect to the great circle aligned with the direction of movement selected by P, which can also take any direction. This justifies that instead of referring to a range, Theorem 2 states that uE =
any direction. With this, we conclude the discussion of (24) and (25) in this proof.

With regard to (26), in Theorem 1 we already proved that for α ∈ (0, π) the equality in (26) holds. Therefore, we only need to prove that for α = π the time to capture τ satisfies

$\tau\leq V(\pi)=\frac{R\pi}{(1-\mu)v_{P}}$. (28)
For α = π in (20)–(21) of the Lemma 1 proof, we use the rate-of-loss

$$\mathcal{L}(v_{E},u_{E})=-\lim_{h\to0}\frac{V(\alpha(h))-V(\alpha(0))+h}{h}\tag{29}$$ $$=\frac{1}{1-\mu}\left(\mu-\frac{v_{E}}{v_{P}}\cos u_{E}\right),\tag{30}$$

where $h>0$ is an infinitesimal hold time, $h\to0$. Let us rewrite (29) for $\alpha(0)=\pi$ as

$$V(\pi)-(V(\alpha(h))+h)=h\mathcal{L}(0,u_{E}),h\to0,\tag{31}$$
and recognize that for the equilibrium action of P, α(h) < π which follows from (19). Furthermore, if both P and E follow their equilibrium strategies for all *t > h*, V (α(h)) is the exact time until the capture. Therefore, the time to capture from t = 0 is τ = V (α(h)) + h which we substitute in (31) together with L(0, uE) =
µ
1−µ to obtain
τ = V (π) − h
µ
1−µ, h → 0 ⇒ τ ≤ V (π),
(32)
a set of intercept points Iλ satisfying |⌢
PIλ|/δ(λ) = µ, where δ(λ) and
|⌢
PIλ| are distances from E and P to Iλ, respectively. There is one-to-one correspondence between the angle λ and the distance δ(λ).

which proves (28) and consequently (26). The same expression yields

$$V(\pi)-\tau=\underbrace{h\frac{\mu}{1-\mu}}_{\varepsilon},\ h\to0,\tag{33}$$

where the $\varepsilon$ expression on the right is an infinitesimally small value, which proves (27) and concludes our proof.

## Iv. Apollonius Domain And Intercept Point

Figure 3 depicts P and E at a relative angular position α.

Let us assume that at initial time t = 0, E picks a direction of motion defined by an angle λ and starts moving with its maximal speed vE = µvP . The angle λ is measured with respect to the great circle defined by P and E, and it is known by P at t = 0 as well. Using this information, P
can take the *shortest path* to intercept E at the point Iλ.

The arc length from E to Iλ is δ = |⌢
the arc length from P to Iλ is |⌢ EIλ| = µvP τλ while PIλ| = vP τλ, where τλ
is the time of the intercept. Note that all points on the arc
⌢
EIλ are points that E can reach sooner than P; similarly,
⌢
PIλ are points that P can reach sooner than E. We can sweep the angle λ ∈ [0, 2π) over its full range, and it will produce a closed line of Iλ points. Points inside (outside)
of the line are all points that E (P) can reach sooner. The points inside the line form the Apollonius domain A and the boundary of the domain ∂A is a line which P and E
can reach simultaneously, therefore, it is a set of potential intercept points from the initial configuration.

It is shown in [4] that

$$\cos\left(\frac{\delta}{R\mu}\right)=\cos\frac{\delta}{R}\cos\alpha+\sin\alpha\cos\lambda\sin\frac{\delta}{R},\tag{34}$$

and that this implicit relation describes a one-to-one $\delta(\lambda)$ mapping between $\lambda$ and $\delta$ which is dependent on $\alpha$. It is 
shown in [4] that there is a critical value αc = π(1 − µ) such that for λ ∈ [0, π] and α ≤ αc

$$\delta(0)=\frac{\alpha R\mu}{1+\mu}\leq\delta(\lambda)\leq\frac{\alpha R\mu}{1-\mu}=\delta(\pi),\tag{35}$$

and for $\lambda\in[0,\pi]$ and $\alpha>\alpha_{c}$

$$\delta(0)=\frac{\alpha R\mu}{1+\mu}\leq\delta(\lambda)\leq\frac{R\mu(2\pi-\alpha)}{1-\mu}=\delta(\pi).\tag{36}$$

In both cases, the lower bound corresponds to $\delta(0)=\widehat{EI}_{0}$, which is the arc length between $E$ and $I_{0}$, and the upper bound corresponds to $\delta(\pi)=\widehat{EI}_{\pi}$ which is the arc length between $E$ and $I_{\pi}$. Note that (34) can be rewritten as

$$\cos\lambda=\left(\cos\left(\frac{\delta}{\mu R}\right)-\cos\frac{\delta}{R}\cos\alpha\right)\left(\sin\alpha\sin\frac{\delta}{R}\right)^{-1},\tag{37}$$

and due to this

$$\delta(\lambda)=\delta(-\lambda),\ \mbox{for}\ \lambda\in[-\pi,0].\tag{38}$$
Expressions (34)-(38) are sufficient to define the boundary of Apollonius domain, ∂A, for any initial configuration between P and E.

**Theorem 3**.: _For all conditions of Theorem 2 and if both $P$ and $E$ use their equilibrium strategies, the intercept point $I_{P-E}$ belongs to the boundary of Apollonius domain, $\partial\mathcal{A}$, only if the initial relative distance $\alpha(0)$ between $P$-E satisfies_

$$\alpha(0)\leq\alpha_{c}=\pi(1-\mu).\tag{39}$$

Proof. Since µ < 1, the condition (39) implies that α(0) <
π. Therefore, the equilibrium actions for both E and P are
uE = 0 and uP = 0. With uE = 0, E moves in the direction
λ = π and the intercept point is on the great circle defined
by P and E. The time to capture is (see Theorem 2)

$$\tau=V(\alpha(0))=\frac{R\alpha(0)}{(1-\mu)_{VP}}.\tag{40}$$

Therefore, the arc length traveled by $E$ is

$$\widehat{EI}_{P-E}=\frac{R\mu_{P}\alpha(0)}{(1-\mu)_{VP}}=\frac{R\mu\alpha(0)}{(1-\mu)},\tag{41}$$

which is a value independent of $\alpha_{c}$. Now, for $\alpha(0)<\alpha_{c}$ from (35), we have

$$\widehat{EI}_{\pi}=\delta(\pi)=\frac{R\mu\alpha(0)}{(1-\mu)}=\widehat{EI}_{P-E},\tag{42}$$

and we can conclude that $I_{P-E}=I_{\pi}$. However, for $\alpha(0)>\alpha_{c}$ from (36), we have

$$\widehat{EI}_{\pi}=\delta(\pi)=\frac{R\mu(2\pi-\alpha(0))}{(1+\mu)}.\tag{43}$$

If we assume that $I_{P-E}=I_{\pi}$, then from (41)

$$\widehat{EI}_{\pi}=\frac{R(2\pi-\alpha(0))}{(1+\mu)}=\frac{R\alpha(0)}{(1-\mu)}=\widehat{EI}_{P-E},\tag{44}$$

which yields

$$\alpha(0)=\pi(1-\mu)=\alpha_{c},\tag{45}$$
and contradicts α(0) *> α*c. Therefore, IP −E ̸= Iπ, which concludes the proof of the theorem.

* $v_{E}=0.35$ (b) $v_{E}=0.6$

## V. Results

Figure 4 illustrates the shape of the Apollonius domain for two different evader speeds and for initial geodesic distances below, at, and above the critical αC value from Theorem 3.

In addition, the equilibrium intercept point for the game of min-max capture time is drawn. As expected, the intercept point lies on the associated Apollonius domain when α ≤
αC and lies outside when *α > α*C. Towards the end of this section, we present applications of our results to two differential game problems on the sphere with more than one P.

## A. Two Pursuers

In the spirit of Isaacs [1, Example 6.8.3], we now extend the results for the one-pursuer scenario to the case of two cooperative pursuers by leveraging the geometry of the Apollonius domain. First let us define the evader's dominance region as E = A1∩A2, where A1 and A2 are the Apollonius domains associated with pursuers P1 and P2, respectively.

The set E represents the set of points that the evader can reach before either pursuer. With the evader at the north pole, let α1 and α2 denote the latitude offset for the pursuers, and let λo be the longitudinal offset between the pursuers. The agents' speeds are such that µ1 =
vE
vP1 , µ2 =
vE
vP2 < 1.

Let the point IP1−E be the equilibrium intercept point for the one-on-one game between P1 and E (and let IP2−E be defined similarly for P2).

Proposition 1: _In the two-pursuer scenario with $\alpha_{1}<\pi(1-\mu_{1})$ and $\alpha_{2}<\pi(1-\mu_{2})$ (i.e., the pursuers are sufficiently close to the evader), the intercept point associated with the solution for the game of $\min$-$\max$ capture time is_

$$I^{*}=\begin{cases}I_{P_{1}-E},&I_{P_{1}-E}\in\mathcal{A}_{2}\\ I_{P_{2}-E},&I_{P_{2}-E}\in\mathcal{A}_{1}\\ \max\left\{\widehat{EI}\mid I\in\partial\mathcal{A}_{1}\cap\partial\mathcal{A}_{2}\right\},&\text{otherwise.}\end{cases}\tag{46}$$

In any case, the agents' equilibrium strategy is to take a geodesic path to the equilibrium intercept point $I^{*}$ as described in (46). This is due to the fact that $I^{*}\in\partial\mathcal{A}_{1}\cup\partial\mathcal{A}_{2}$
and all of the points on the boundary of an Apollonius domain are, by definition, points of simultaneous arrival via geodesic paths (i.e., see [4]). Note that the state space for Proposition 1 is restricted such that the geodesic distances from the pursuers to the evader satisfy (39). This is because for *α > α*C the Apollonius domain A does not contain the equilibrium intercept point for the min-max capture time game, and thus E may not necessarily be guaranteed to contain the equilibrium intercept point for the two-pursuer version of the game. A rigorous proof for Proposition 1, as well as the solution for more general two-pursuer initial conditions is left for future work.

## B. Target Guarding

Another primary application for the Apollonius domain is to address target guarding games, in which an evader seeks to reach a target region while avoiding capture by one or more pursuers. The evader wins if it can safely reach a point in the target region while the pursuer(s) wins if capture occurs before the evader can reach the target. Let the target region be a subset of the surface of the sphere denoted as T .

Lemma 2. In the spherical target guarding game with one evader and one or more faster pursuers, the evader wins if A ∩ T ̸= ∅.

Lemma 3. In the spherical target guarding game with one evader and one faster pursuer, the pursuer wins if

$${\cal A}\cap{\cal T}=\varnothing,\quad\alpha\leq\frac{1-\mu}{1+\mu}\pi,\tag{47}$$
by implementing the geodesic parallel strategy (as defined in [4]), wherein the pursuer heads to the point on the Apollonius domain associated with the evader's current heading.

Proof. From [4, Proposition 4.6], under the condition (47) if the pursuer uses the *geodesic parallel strategy*, the Apollonius domain at the initial time is guaranteed to contain the Apollonius domain at all future times until capture for any evader's motion consisting of a polygonal line of geodesic arcs. Thus, if *A ∩ T* = ∅ in the initial configuration, the condition is guaranteed to hold over the playout of the game. Moreover, from [4, Corollary to Proposition 4.7] capture is guaranteed to occur within a time of
α
1−µ. Therefore, the evader's safe reachable set will never intersect the target region, capture is guaranteed in a finite time, and thus the evader will not be able to win.

## Vi. Conclusion

This paper contains the solution to the pursuit-evasion differential game of min-max capture time between one pursuer and one slower evader, all moving with simple motion on a sphere. In the special case where the two agents are on direct opposite ends of the sphere, the agents' equilibrium strategies are not well defined according to the conventional analysis; this configuration lies on a Dispersal Surface. A loss-rate analysis was carried out in this paper to determine a unique equilibrium control input for this configuration which involves the evader standing still for an infinitesimally small amount of time while the pursuer freely chooses any heading. The solution of the game provides a spherical analogue to the Apollonius circle, i.e., the Apollonius domain. It was found that the equilibrium intercept point lies outside the Apollonius domain in a portion of the state space (unlike in the planar case). Consequently, when the initial configuration lies within a specified parameter regime, the Apollonius domain exhibits similar properties to the Apollonius circle, i.e., the sphere can be considered flat. This is due to the geometry of a sphere, which is a closed domain, rather than an open domain of a Cartesian plane. Therefore, some caution must be taken when applying the concept of the Apollonius domain to solve spherical pursuitevasion problems. Some example extensions and applications were discussed, including two cooperative pursuers and target guarding. Future work includes rigorously proving the two-pursuer solution, generalizing it, and obtaining evader reachability sets when the pursuer does not know the evader's heading. Establishing dominance regions for multi-pursuerevader scenarios on spherical geometry remains to be a rich area of research.

## References

[1] R. Isaacs, Differential games: a mathematical theory with applications
to optimization, control and warfare.
New York: Wiley, 1965.
[2] M. Pachter, A. Von Moll, E. Garcia, D. W. Casbeer, and D. Milutinovi´c, "Two-on-one pursuit," Journal of Guidance, Control, and
Dynamics, vol. 42, no. 7, pp. 1638–1644, 2019.
[3] A. Von Moll, M. Pachter, E. Garcia, D. Casbeer, and D. Milutinovi´c,
"Robust policies for a multiple-pursuer single-evader differential game," *Dynamic Games and Applications*, vol. 10, pp. 202–221, 2020.
[4] A. M. Kovshov, "Geodesic parallel pursuit strategy in a simple motion
pursuit game on the sphere," in Advances in Dynamic Games and Applications, J. A. Filar, V. Gaitsgory, and K. Mizukami, Eds. Boston,
MA: Birkh¨auser Boston, 2000, pp. 97–113.
[5] A.
Melikyan,
Geometry
of
Pursuit-Evasion
Games
on
Two-
Dimensional Manifolds.
Boston, MA: Birkh¨auser Boston, 2007, pp.
173–194.
[6] N. Hovakimyan and A. Melikyan, "Geometry of pursuit-evasion on
second order rotation surfaces," *Dynamics and Control*, vol. 10, pp. 297–312, 2000.
[7] A. S. Kuchkarov, "A simple pursuit-evasion problem on a ball of
a riemannian manifold," *Mathematical Notes*, vol. 85, pp. 190–197,
2009.
[8] A. Toriyama, *The Hardest Time of His Death*, 1989, vol. 211, ch. 18,
Do Your Best with Kaio-sama, Dead Son Goku!
[9] D. A. Paley, "Stabilization of collective motion on a sphere," Automatica, vol. 45, no. 1, pp. 212–216, 2009.
[10] S. Hernandez and D. A. Paley, "Three-dimensional motion coordination in a spatiotemporal flowfield," IEEE Transactions on Automatic
Control, vol. 55, no. 12, pp. 2805–2810, 2010.
[11] W. Li and M. W. Spong, "Unified cooperative control of multiple
agents on a sphere for different spherical patterns," IEEE Transactions on Automatic Control, vol. 59, no. 5, pp. 1283–1289, 2014.
[12] J. Markdahl, J. Thunberg, and J. Gonc¸alves, "Almost global consensus
on the n -sphere," *IEEE Transactions on Automatic Control*, vol. 63,
no. 6, pp. 1664–1675, 2018.
[13] V. Muralidharan, A. D. Mahindrakar, and A. Saradagi, "Control of
a driftless bilinear vector field on n-sphere," IEEE Transactions on
Automatic Control, vol. 64, no. 8, pp. 3226–3238, 2019.
[14] T. Ibuki, S. Wilson, A. D. Ames, and M. Egerstedt, "Distributed
collision-free motion coordination on a sphere: A conic control barrier function approach," *IEEE Control Systems Letters*, vol. 4, no. 4, pp.
976–981, 2020.
[15] D. Milutinovi´c, D. W. Casbeer, A. Von Moll, M. Pachter, and E. Garcia, "Rate of loss characterization that resolves the dilemma of the wall pursuit game solution," *IEEE Transactions on Automatic Control*, vol. 68, no. 1, pp. 242–256, 2023.

## Appendix Relative P -E Kinematics

Here we derive the rate of change of angular distance α,
α ∈ (0, π) from (7) for P and E that obey (8)-(9).

The time derivative of (7) yields

$$\dot{\vec{n}}_{GC}\sin\alpha+\vec{n}_{GC}\dot{\alpha}\cos\alpha=\frac{1}{R^{2}}\left(\dot{\vec{P}}\times\vec{E}+\vec{P}\times\dot{\vec{E}}\right).\tag{48}$$

Note that the magnitude $|\vec{n}_{GC}|=\sqrt{\vec{n}_{GC}\cdot\vec{n}_{GC}}=1$, where "$\cdot$" denotes the scalar product of vectors, therefore,

$$\frac{d|\vec{n}_{GC}|}{dt}=2\dot{\vec{n}}_{GC}\vec{n}_{GC}=0\Rightarrow\dot{\vec{n}}_{GC}\vec{n}_{GC}=0.\tag{49}$$
Because of that, we apply the scalar product ⃗nGC to both sides of (48) and obtain

˙α cos α = 1 R2 ( ˙⃗P × ⃗E) · ⃗nGC + 1 R2 (⃗P × ˙⃗E) · ⃗nGC. (50)

  To find
          ˙⃗P and
                 ˙⃗E, let us introduce a reference frame
composed of orthogonal unit vectors
                                   1
                                   R ⃗P, ⃗nGC and ⃗tP =
1
R ⃗P × ⃗nGC. In that reference frame, the P and E position
vectors are

⃗P = R � 1 R ⃗P � (51) ⃗E = R cos α � 1 R ⃗P � − R sin α � 1 R ⃗P × ⃗nGC � , (52)
and the velocity vectors ˙⃗P = vP ⃗p and ˙⃗E = vE⃗e are

˙⃗P = −vP cos uP � 1 R ⃗P × ⃗nGC � − vP sin uP (⃗nGC), (53) (54) ˙⃗E = − vE sin α cos uE � 1 R ⃗P � − vE sin uE(⃗nGC) − vE cos α cos uE � 1 R ⃗P × ⃗nGC � ,
which also account for the relation between ⃗tE and ⃗tP
(see Fig. 2).

Using vector identities, the two terms on the right side of
(50) are

( ˙⃗P × ⃗E) · ⃗nGC = 0 1 0 0 −vP sin uP −vP cos uP R cos α 0 −R sin α = −RvP cos uP cos α (55) ������ ������ 0 1 0 R 0 0 −vE sin α cos uE −vE sin uE −vE cos α cos uE = RvE cos uE cos α (56) (⃗P × ˙⃗E) · ⃗nGC = ������ ������
which yields

˙α cos α = 1 R(vE cos uE − vP cos uP ) cos α, (57)
and by matching the expressions on both sides of the equation, we can finally conclude that

˙α = vE R cos uP . (58) R cos uE − vP