# Information Compression In Dynamic Information Disclosure Games

Dengwang Tang and Vijay G. Subramanian

  Abstract— We consider a two-player dynamic information
design problem between a principal and a receiver—a game is
played between the two agents on top of a Markovian system
controlled by the receiver's actions, where the principal obtains
and strategically shares some information about the underlying
system with the receiver in order to influence their actions.
In our setting, both players have long-term objectives, and
the principal sequentially commits to their strategies instead
of committing at the beginning. Further, the principal cannot
directly observe the system state, but at every turn they can
choose randomized experiments to observe the system partially.
The principal can share details about the experiments to the
receiver. For our analysis we impose the truthful disclosure
rule: the principal is required to truthfully announce the details
and the result of each experiment to the receiver immediately
after the experiment result is revealed. Based on the received
information, the receiver takes an action when its their turn,
with the action influencing the state of the underlying system.
We show that there exist Perfect Bayesian equilibria in this
game where both agents play Canonical Belief Based (CBB)
strategies using a compressed version of their information,
rather than full information, to choose experiments (for the
principal) or actions (for the receiver). We also provide a
backward inductive procedure to solve for an equilibrium in
CBB strategies.

## I. Introduction

In many modern engineering and socioeconomic problems and systems, such as cyber-security, transportation networks, and e-commerce, information asymmetry is an inevitable aspect that crucially impacts decision making. In these systems, agents need to decide on their actions under limited information about the system and each other. In many situations, agents can overcome (some of) the information asymmetry by communicating with each other. However, agents can be unwilling to share information when agents' goals are not aligned with each other, since having some information that another agent does not know can be an advantage. In general, communication between agents with diverging incentives cannot be naturally established without rules/protocols that everyone agrees upon, and all agents suffer due to the breakdown of the information exchange. For example, drug companies are required by regulations to disclose their trial results truthfully. The public can then trust the results and This work is supported by NSF Grant No. ECCS 1750041, ECCS
2038416, ECCS 1608361, CCF 2008130, ARO Award No. W911NF-17- 1-0232, MIDAS Sponsorship Funds by General Dynamics, and Okawa Foundation Research Grant.

D. Tang is with Ming Hsieh Department of Electrical and Computer Engineering, University of Southern California, Los Angeles, CA 90089, USA dengwang@usc.edu V. G. Subramanian is with the Department of Electrical Engineering and Computer Science, University of Michigan, Ann Arbor, MI 48109, USA
vgsubram@umich.edu benefit from the drug. In turn, the drug companies can make a profit. Without government regulations, drug companies and the public will both suffer due to mistrust. In many realworld dynamic systems, information exchange and decision making can happen repeatedly as the system/environment changes over time—for example, public companies disclose information periodically which impacts stockholders' decisions; (COVID-19) vaccine producers conduct their trials and release results sequentially which impacts the government's purchasing decisions; during an epidemic, health authorities update their recommendations on the use of face masks over time according to changing levels of infection, etc. Therefore, in the face of information asymmetry, it is important to establish rules/protocols to facilitate repeated information exchange among agents in multi-agent dynamic systems.

In the economics literature, there are mainly two approaches to the above problem, namely mechanism design [1] and information design [2]. In mechanism design, less informed agents can extract information from more informed agents by committing to how they will use the collected information beforehand. Whereas in information design, more informed agents can partially disclose information to less informed agents. The more informed agents commit on the manner in which they partially disclose their information. In both approaches, all agents can benefit from the information exchange. For both approaches, one can classify the pertinent literature into two groups: (i) static settings, where both information disclosure and decision making take place only once; and (ii) dynamic settings, where agents repeatedly disclose information and take actions over time on top of an ever changing environment/physical system. Mechanism design and information design for the dynamic settings are more challenging than the static settings since agents need to anticipate future information disclosure when taking an action. Mechanism design in dynamic settings has been studied extensively in the literature [3], [4], [5], [6]. In most of the works on information design in dynamic settings, the receivers are assumed to be myopic [7], [8], [9], [10], [11], [12], [13]. This assumption greatly simplifies receivers' decision making. There have been a few papers studying information design problems where all agents in the system have long-term goals [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24]. These papers typically assume that the principal commits to their strategy for the whole game before the game starts as in a Stackelberg equilbrium [25]. The bulk of this literature also assumes that the principal observes the underlying state perfectly. However, these assumptions can be inappropriate for many applications. If the protocol gives more informed agents the power to commit to a strategy for the whole time horizon at the beginning of time, then the more informed agent can implement punishment strategies by threatening to withhold information if less informed agents do not obey their "instructions"—see Example 1. Thus, the informed agents could abuse their commitment power to implement otherwise non-credible threats instead of using it for efficient information disclosure. This is not a desirable outcome—for example, online map services should not threaten to withhold service if a driver refuses to take the recommended route; and similarly, public health authorities may want to use persuasion instead of threats to encourage mask wearing during an epidemic. Again, focusing on the public health setting, during an epidemic the authorities may not know the full extent of the disease spread, but only an estimate of it (using testing and other methods). In this context, transparency to the public on the part of the authorities—in disclosing measurement methods and data— is important for persuasion based schemes to be effective.

In this work, we focus on the dynamic information design problem. Specifically, we consider a dynamic game between a principal and a receiver on top of a Markovian system. Both the principal and the receiver have long-term objectives. The principal cannot directly (and perfectly) observe 1 the system state, but can choose randomized experiments to partially observe the system. The principal is also allowed to choose any experiment, but they must announce the experimental setup and results truthfully to the receiver before the receiver takes their action. Both these aspects of our model are motivated by the public health setting described earlier. The receiver takes action on each turn based on the information received to date, which then influences the underlying system.

Contributions: In the class of dynamic information disclosure games among a principal and a receiver discussed above, under the assumption of truthful disclosure, we identify compression based strategies, called Canonical Belief Based (CBB) strategies, for both players to play at equilibrium. Here both agents use strategies based on a compressed version of their information, rather than the full information, to choose their actions—experiments (for the principal), and actions (for the receiver). We develop a backward inductive sequential decomposition procedure to find such equilibrium strategies, and we show that the procedure always has at least one solution. Finally, we investigate examples of such games to provide insight to CBB-strategy-based equilibria.

Organization: The rest of this work is organized as follows: In Section I-A, we provide an example where a principal can abuse its commitment power. We formulate the problem in Section II. Then, we provide some preliminary results in discrete geometry in Section III. In Section IV we state our main results. In Section V we study some examples. We discuss difficulties with potential extensions of our result in Section VI. Finally, we conclude in Section VII. Details of all the technical proofs are in the Appendix.

Notation: We use capital letters to represent random variables, bold capital letters to denote random vectors, and lower case letters to represent realizations. We use superscripts to indicate teams and agents, and subscripts to indicate time. We use t1 : t2 to indicate the collection of timestamps (t1, t1 + 1, · · · *, t*2). For example X1
1:3 stands for the random vector (X1
1, X1
2, X1
3). For random variables or random vectors, we use the corresponding script capital letters (italic capital letters for greek letters) to denote the space of values these random vectors can take. For example, Hi t denotes the space of values the random vector Hi t can take. We use P(·) and E[·] to denote probabilities and expectations, respectively. We use ∆(Ω) to denote the set of probability distributions on a finite set Ω.

## A. A Motivating Example

The following is an example where given the power to commit to a strategy for the whole game before the game starts (i.e. the Stackelberg game setting), the principal can use otherwise non-credible threats.

Example 1. Consider a two-stage game of two players: the principal P, and the agent/receiver R. The state of the system at time t is Xt. The states are uncontrolled, and X1, X2
are i.i.d. uniform random variables taking values in {0, 1}.

The principal can observe Xt at time t while the receiver cannot. At stage t, The principal transmits message Mt to the receiver and the receiver takes an action Ut ∈ {*a, b, c, d*}.

The instantaneous payoff for both players are given by

rA
1 (0, a) = 1, rA
1 (0, b) = 1.01, rA
1 (0, c) = rA
1 (0, d) = −1000
rA
1 (1, c) = 1, rA
1 (1, d) = 1.01, rA
1 (1, a) = rA
1 (1, b) = −1000
rB
1 (0, a) = 500, rB
1 (0, b) = 1, rB
1 (0, c) = rB
1 (0, d) = −1000

rB
 1 (1, c) = 500, rB
               1 (1, d) = 1, rB
                            1 (1, a) = rB
                                      1 (1, b) = −1000

and rA
    2 (·, ·) = rB
             2 (·, ·) = rA
                      1 (·, ·).
  Suppose that the principal has the power to commit to a
strategy (g1, g2) at the beginning of the game. Then, (given
the Stackelberg setting) an optimal strategy for the principal
is the following: fully reveal the state at t = 1 (i.e. M1 =
X1); if the receiver plays a or c at t = 1, then transmit no
information at t = 2; and if the receiver plays b or d at t = 1,
then fully reveal the state at t = 2. Then, the receiver's best
response to the principal's strategy is the following: at t = 1:
play b if M1 = 0, and play d if M1 = 1; and at time t = 2:
play a if M2 = 0, and play c if M2 = 1.
  In the resulting equilibrium, the principal effectively
threatens the receiver to comply to their interest at time t = 1
by not giving information at time t = 2, even though the
interests of both parties are aligned at t = 2. In fact, without
posing a threat to the receiver at time 2, the principal cannot
convince them to play b or d at time 1.

## Ii. Problem Formulation

We consider a finite-horizon two players dynamic game between the principal A and the agent/receiver B. The game consists of T stages, where, in each stage, the principal moves before the receiver. The game features an underlying dynamic system with state Xt. At each time t ∈ [T], the receiver chooses an action Ut. Then, the system transits to the next state Xt+1 ∼ Pt(Xt, Ut), where Pt : Xt × Ut �→
∆(Xt+1) is the transition kernel. The initial state X1 has prior distribution ˆπ ∈ ∆(X1). The initial distribution ˆπ and transition kernels P = (Pt)T
t=1 are common knowledge to both players. We assume that neither player can observe the state Xt directly. However, at each time t, the principal can conduct an *experiment* to learn about Xt. In this work, an experiment2 refers to an observation kernel that can be chosen by the principal. We impose the rule that the experiments are required to be public—both the principal and the receiver know the settings (the probabilities in the observation kernel), and the outcome (the observation itself) of the experiment. Specifically, at each time t, the principal chooses an observation kernel σt : Xt �→ ∆(Mt), and announces σt to the receiver. The experiment outcome Mt is then realized, and observed by both the principal and the receiver. Note that if the horizon T
= 1, then the above setting is the same as the classical information design problem considered in [2].

Assumption 1. Xt, Ut, Mt are finite sets with |Mt| sufficiently large.

  The order of events happening at time t is given as the
following: (1) The principal commits to an experiment σt,
and announces it to the receiver; (2) The measurement result
Mt is revealed to both the principal and receiver; (3) The
receiver takes action Ut; and (4) Xt transits to the next state.
  Let St be the space of experiments. The principal uses a
(pure) strategy to choose their experiment gA
                                           t
                                             : S1:t−1 ×
M1:t−1 × U1:t−1 �→ St. For convenience, define HA
                                                   t
                                                      =
S1:t−1×M1:t−1×U1:t−1. The receiver uses a (pure) strategy
gB
 t
   : S1:t × M1:t × U1:t−1 �→ Ut. For convenience, define
HB
 t
    = S1:t × M1:t × U1:t−1. The principal's goal is to
maximize JA(g) = Eg ��T
                          t=1 rA
                              t (Xt, Ut)
                                        �
                                         . The receiver's

goal is to maximize JB(g) = Eg ��T
                                   t=1 rB
                                        t (Xt, Ut)
                                                 �
                                                  . The
instantaneous reward functions (rA
                                 t , rB
                                    t )T
                                       t=1 are common
knowledge to both agents.
  The belief of the principal at time t is a function µA
                                                    t :
M1:t−1 × S1:t−1 × U1:t−1 �→ ∆(X1:t). The belief of the
receiver at time t (after knowing σt and observing Mt) is a
function µB
         t : M1:t × S1:t × U1:t−1 �→ ∆(X1:t).
  Inspired by the "mechanism picking game" defined in
[29], we call the above game a signal picking game, and
we will study Perfect Bayesian Equilibria for our game.

Definition 1 (PBE). A Perfect Bayesian Equilibrium is a pair (*g, µ*), where

- g is sequentially rational given µ (=
�
µA
1:T , µB
1:T
�
).
- µ can be updated using Bayes law whenever the denominator is non-zero.

## Iii. Background: Discrete Geometry

In this section, we introduce some notations and results of discrete geometry that are necessary for our main results.

Definition 2. Let f be a real-valued function on a polytope3
Ω. Then, f is called a (continuous) piecewise linear function if there exist polytopes C1, · · · *, C*k such that
- f is linear on each Cj for j = 1, · · · *, k*; and
- C1 *∪ · · · ∪* Ck = Ω.

Lemma 1. Let Ω1, Ω2 be polytopes. Let ℓ : Ω1 �→ Ω2 be
an affine function and f : Ω2 �→ R be a piecewise linear
function. Then the composite function f ◦ ℓ : Ω1 �→ R is
piecewise linear.

Proof. See Appendix A.

Next, we introduce the notion of a triangulation.

Definition 3. [30] Let Ω be a finite dimensional polytope. A
triangulation γ of Ω is a finite collection of simplices (i.e.
convex hulls of a finite, affinely independent set of points)
such that

(1) If a simplex C ∈ γ, then all faces of C are in γ;
(2) For any two simplices C1, C2 ∈ γ, C1 ∩ C2 is a
(possibly empty) face of C1; and
(3) The union of all simplices in γ equals Ω.
For a function f : Ω �→ R and a triangulation γ, let I(*f, γ*)
denote the linear interpolation of f based on the triangulation
γ, i.e.

$\mathbb{I}(f,\gamma)(\omega):=\alpha_{1}f(\omega_{1})+\cdots+\alpha_{k}f(\omega_{k})$.

if ω
        ∈ C, where C
                                 ∈ γ is a simplex with vertices
ω1, · · · , ωk, and ω
                              =
                                   α1ω1 + · · · + αkωk for some
α1, · · · , αk ≥ 0 such that α1 + · · · + αk = 1.

Lemma 2. For any real-valued function f on a polytope
Ω, I(f, γ) is a well-defined, continuous piecewise linear function.

3A polytope is a convex hull of a finite set in Rd where *d <* +∞.

Proof. See Appendix A.

For each ω ∈ Ω and triangulation γ, we have shown that there exists a unique way to represent ω as a convex combination of the vertices of one simplex from γ. One can treat this convex combination as a finite measure. Denote this finite measure by C(*ω, γ*). Then we have I(*f, γ*)(ω) =
�
f(·)dC(*ω, γ*).

Definition 4. Let f be a real-valued function on Ω. The concave closure cav(f) of f is defined as a function ρ such that

$\rho(\omega):=\sup\{z:(\omega,z)\in\mbox{cvxg}(f)\}\quad\forall\omega\in\Omega$
where cvxg(f) ⊂ Ω × R is the convex hull of the graph of f.

For certain functions f, their concave closures can be represented as a triangulation based interpolation of the original function. Define the set of all such triangulations as arg cav(f), i.e.

arg cav(f) := {γ is a triangulation of Ω : I(*f, γ*) = cav(f)}.

The following lemma identifies a class of functions with the above property.

Lemma 3. Let f1, · · · , fk, ρ1, · · · , ρk be continuous piecewise linear functions on a polytope Ω. For ω ∈ Ω, define

$\Upsilon(\omega)=\arg\max_{j=1,\cdots,k}f_{j}(\omega),$ and $\Psi(\omega)=\max_{j\in\Upsilon(\omega)}\rho_{j}(\omega).$
Then arg cav(Ψ) is non-empty, i.e. there exists a triangulation γ of Ω such that the concave closure of Ψ is equal to I(Ψ, γ).

Proof. See Appendix A.

## Iv. Main Results

In this section, we introduce our main result—Theorem
1—, which provides a dynamic programming characterization of a subset of PBE of the signal picking game.

Note that due to the assumption of public experiments, the signal picking game is a game with symmetric information 4
after each experiment is conducted. The principal's advantages lies in the fact that they have the power to determine the choice of experiments. Thus, standard results on strategyindependence of beliefs (e.g. [31]) imply that the beliefs of both players in this game are strategy-independent, i.e. there is a canonical belief system. Similar strategy-independent belief systems are also constructed and used in [32]. We describe this belief system as follows.

**Definition 5**.: Define the Bayesian update function $\xi_{t}:\Delta(\mathcal{X}_{t})\times\mathcal{S}_{t}\times\mathcal{M}_{t}\mapsto\Delta(\mathcal{X}_{t})$ by setting for each $x_{t}\in\mathcal{X}_{t}$

$$\xi_{t}(x_{t}|\pi_{t},\sigma_{t},m_{t}):=\frac{\pi_{t}(x_{t})\sigma_{t}(m_{t}|x_{t})}{\sum_{\tilde{x}_{t}}\pi_{t}(\tilde{x}_{t})\sigma_{t}(m_{t}|\tilde{x}_{t})}$$

for all $(\pi_{t},\sigma_{t},m_{t})$ such that the denominator is non-zero. When the denominator is zero, $\xi_{t}(\pi_{t},\sigma_{t},m_{t})$ is defined to be the uniform distribution.

Definition 6. The canonical belief system is a collection
of functions (κA
               t , κB
                   t )t∈T , κi
                           t : Hi
                                 t �→ ∆(Xt), i ∈ {A, B}
defined recursively through the following step. Denote πi
                                                      t =
κi
 t(hi
    t), i ∈ {A, B}, t ∈ T , and then we have

- πA
   1 := ˆπ, the prior distribution of X1;

- πB
   t := ξt(πA
             t , σt, mt);

- πA
   t+1 := ℓt(πB
               t , ut), where ℓt : ∆(Xt)×Ut �→ ∆(Xt+1)
  is defined by

˜xt πt(˜xt)Pt(xt+1|˜xt, ut). ℓt(πt, ut)(xt+1) := �
We consider a subclass of strategies for both the principal and the receiver, called canonical belief based (CBB) strategies, wherein player i ∈ {*A, B*} chooses their experiment or action, respectively, at time t based solely on Πi t = κi t(Hi t)
instead of Hi t. Let λA
t : ∆(Xt) *�→ S*t be the CBB strategy of the principal, and λB
t : ∆(Xt) *�→ U*t be the CBB strategy of the receiver. Then, saying that player i is using CBB strategy
λi t is equivalent to saying that they are using the strategy

gi t(hi t) = λi t(κi t(hi t)), ∀hi t ∈ Hi t.
Given an experiment and a distribution on the state, the posterior belief of the receiver is a random variable (a function of the random outcome). In an information disclosure game, it is helpful to consider the following sub-problem: how to design an experiment such that the receiver's belief, as a random variable, follows a certain distribution. The next definition formalizes this concept. This concept was used in classical one-shot information design setting [2] as well.

Definition 7. [2] An experiment σt ∈ St is said to induce
a distribution η ∈ ∆f(∆(Xt))—that is, η is a distribution
with finite support on the set of distributions ∆(Xt)—from
πt ∈ ∆(Xt) [2] if for all ˜πt ∈ ∆(Xt),

˜xt
   σt( ˜mt|˜xt)πt(˜xt).

$$\eta(\tilde{\pi}_{t})=\sum_{\tilde{m}_{t}}{\bf1}_{\{\tilde{\pi}_{t}=\xi_{t}(\pi_{t},\sigma_{t},\tilde{m}_{t})\}}\sum_{\tilde{x}_{t}}$$
4As mentioned earlier—in Footnote 1—, there are significant challenges A distribution η is said to be *inducible from* πt if there exists some experiment σt that induces η from πt.

**Remark 1.** In [2], the authors showed that a distribution is $\eta\in\Delta_{f}(\Delta(\mathcal{X}_{t}))$ is inducible from $\pi_{t}$ if and only if $\pi_{t}$ is the center of mass of $\eta$, i.e. $\pi_{t}=\sum_{\tilde{\pi}_{t}\in\operatorname{supp}(\eta)}\eta(\tilde{\pi}_{t})\cdot\tilde{\pi}_{t}$.

We now introduce our main result, which describes a backward induction procedure to find a PBE where both players use CBB strategies.

## Theorem 1. Let

$$V_{T+1}^{A}(\cdot)=V_{T+1}^{B}(\cdot):=0$$

_For each $t=T,T-1,\cdots,1$ and $\pi_{t}\in\Delta(\mathcal{X}_{t})$, define_

$$\hat{q}_{t}^{i}(\pi_{t},u_{t}):=\sum_{\tilde{x}_{t}}r_{t}^{i}(\tilde{x}_{t},u_{t})\pi_{t}(\tilde{x}_{t})+V_{t+1}^{i}(\ell_{t}(\pi_{t},u_{t}))$$ $$\forall i\in\{A,B\};\tag{1a}$$ $$\Upsilon_{t}(\pi_{t}):=\max_{u_{t}}\max_{\hat{q}_{t}^{B}(\pi_{t},u_{t})};$$ (1b) $$\hat{v}_{t}^{A}(\pi_{t}):=\max_{u_{t}\in\Upsilon(\pi_{t})}\hat{q}_{t}^{A}(\pi_{t},u_{t});$$ (1c) $$\hat{v}_{t}^{B}(\pi_{t}):=\max_{u_{t}}\hat{q}_{t}^{B}(\pi_{t},u_{t});$$ (1d) $$\gamma_{t}\in\arg\operatorname{cov}(\hat{v}_{t}^{A});$$ (1e) $$V_{t}^{i}(\pi_{t}):=\mathbb{I}(\hat{v}_{t}^{i},\gamma_{t})\quad\forall i\in\{A,B\}.\tag{1f}$$

Let λ∗B
     t (πt) be any ut ∈ Ut that attains the maximum
in (1c). Let λ∗A
              t (πt) be any experiment that induces the
finite measure C(πt, γt) from πt. Then, the CBB strategies
(λ∗A, λ∗B) form (the strategy part of) a PBE, and V A
                                                    1 (ˆπ)
and V B
     1 (ˆπ) are the equilibrium payoffs for the principal and
the receiver respectively in this PBE.

Proof Outline. In Lemma 4 in Appendix B we construct a
belief system µ∗ that is consistent with any strategy profile.
Hence, we only need to show sequential rationality of λ∗.
  To show the receiver's sequential rationality, we prove
the following: Fixing the principal's strategy to be λ∗A, the
receiver is facing an MDP with state ΠB
                                      t and action Ut. The
proof then follows via standard stochastic control arguments.
  To show the principal's sequential rationality, we prove
the following: Fixing the receiver's strategy to be λ∗B, the
principal is facing an MDP with state ΠA
                                         t
                                            and action Σt.
This proof follows cia standard stochastic control arguments
coupled with information design results [2].
  The details of the proof are presented in Appendix B.

  The following proposition states that the sequential de-
composition procedure described in Theorem 1 is well de-
fined and always has a solution.

Proposition 1. There always exists a CBB strategy profile
(λ∗A, λ∗B) that satisfies Eqs. (1) in Theorem 1.

Proof. Induction on time t is used for the proof.
  Induction Invariant: V A
                          t , V B
                              t
                                  are well-defined continu-
ous piecewise linear functions.
  Induction Base: The induction variant is clearly true for
t = T + 1 since V A
                  T +1, V B
                        T +1 are constant functions.

Induction Step: Suppose that the induction invariant holds for t + 1.

- Step 1: For each ut *∈ U*t, using the fact that ℓt(πt, ut)
is affine in πt, by Lemma 1, qA
t , qB
t
are continuous
piecewise linear functions in πt.
- Step 2: By Lemma 3, γt is well-defined. - Step 3: By Lemma 2, V A
t , V B
t
are continuous piecewise
linear functions.
This completes the proof.

## A. Extension

In many real-world settings, the receivers have the option to quit the game at any time. Our model and results can be extended to finite horizon games where the receiver can decide to terminate the game at any time before time T.

Proposition 2. Let Ut ⊂ Ut be the set of actions that
terminates the game at time t. If we define V i
                                           t , qi
                                              t, λ∗i
                                                 t
                                                    for
each i ∈ {A, B}, t ∈ T as in (1) except that (1a) is changed
to

$\hat{q}_{t}^{i}(\pi_{t},u_{t})$

$:=\sum_{\tilde{x}_{t}}r_{t}^{i}(\tilde{x}_{t},u_{t})\pi_{t}(\tilde{x}_{t})+\begin{cases}V_{t+1}^{i}(\ell_{t}(\pi_{t},u_{t}))&\text{if}u_{t}\not\in\overline{\mathcal{U}}_{t}\\ 0&\text{if}u_{t}\in\overline{\mathcal{U}}_{t}\end{cases}$

for i ∈ {A, B}. Then the CBB strategies (λ∗A, λ∗B) form
(the strategy part of) a PBE, and V A
                                       1 (ˆπ) and V B
                                                    1 (ˆπ) are
the equilibrium payoff for the principal and the receiver
respectively in this PBE.

Proof. Similar to Theorem 1.

## V. Examples

We implement the sequential decomposition algorithm of Proposition 2 in MATLAB for binary state spaces (i.e. |Xt| =
2). We run the algorithm on the following examples of the signal picking game.

Example 2. Consider the quickest detection game defined in [24]. In this game, the underlying state Xt is binary and uncontrolled, with Xt = {1, 2}. State 2 is an absorbing state, i.e. P(Xt+1 = 2 | Xt = 2) = 1, whereas the system can jump from state 1 to state 2 at any time with probability p, i.e. P(Xt+1 = 2 | Xt = 1) = p where p ∈ (0, 1).

The receiver would like to detect (the epoch of) the jump from state 1 to state 2 as accurately as possible. At each time the receiver has two options: Ut = j stands for declaring state j for j = 1, 2. The instantaneous reward of the receiver is given by

$$r_{t}^{B}(X_{t},U_{t})=\begin{cases}-1&\text{if}X_{t}=1,U_{t}=2\\ -c&\text{if}X_{t}=2,U_{t}=1\\ 0&\text{otherwise}\end{cases}$$

where $c\in(0,1)$. Once the receiver declares state 2, the game ends immediately.

The principal would like the receiver to stay in the system as long as possible. The instantaneous reward for the principal is

$$r_{t}^{A}(X_{t},U_{t})=\begin{cases}1&\text{if}U_{t}=1\\ 0&\text{otherwise}\end{cases}$$
Setting p = 0.2, c = 0.1, we obtained the qB
t and V A
t functions specified in Proposition 2 in Figure 4. The horizontal axis represents πt(1). In the figures for V A
t functions, the vertices of the triangulation γt are labeled. The vertices represent the set of beliefs that the principal could induce, and they completely describe the principal's CBB strategy. If the vertex is labeled with red circles, the receiver will take action Ut = 1 at this posterior belief. If, instead, the vertex is labeled with blue triangles, the receiver will take action Ut = 2 at this posterior belief.

From the figures, one can see that at any stage, there is only one possible belief that the principal would induce which leads to the receiver quitting the game (i.e. select Ut = 2). This is consistent with the principal's objective of keeping the receiver in the system. Just like in static information design problems [2], [33], when it is better off for the receiver to declare change, i.e., quit, under the current belief, the principal would promise to tell the receiver that the state is 2 with some probability ˜p when the state is indeed 2, and tell the receiver nothing otherwise. In doing so, the receiver would believe that the state is 1 with a higher probability when the principal does not tell the receiver anything. The principal chooses ˜p to be precisely the value for which the receiver is willing to stay in the system [2].

When t is close to T, the end of the game, the principal would only prefer to declare state 2 if they believe that πt(1)
is very small. This is due to the fact that "false alarms" are costlier than delayed detection in this game. When t is further away from T, the threshold of πt(1) for the principal to declare state 2 becomes larger. This holds because when the game is close to end, the receiver has the "safe" option to declare state 1 (at a small cost) until the end to avoid false alarms (which are costly). However, this option is less preferable when the gap between t and T is large.

When t is further away from T, the principal's value function seems to converge. This is due to the fact that the receiver has the option to quit the game and staying in the game is costly in general.

Example 3. Consider a game between a principal and a detector. In this game, the underlying state Xt is binary and uncontrolled with Xt = {−1, 1}. At any time, the system can jump to the other state with probability p ∈ (0, 1), i.e.

$$\mathbb{P}(X_{t+1}=-j\mid X_{t}=j)=p,\qquad\forall j\in\{-1,1\}.$$
The receiver has three actions: Ut = j stands for declaring state j for j = −1, 1. Both Ut = −1 and Ut = +1 terminate the game. In addition, the receiver can choose to wait at a cost with action Ut = 0. The instantaneous reward of the

receiver for $c\in(0,1)$ is given by

$$r_{t}^{B}(X_{t},U_{t})=\begin{cases}1&\text{if}X_{t}=U_{t}\\ -c&\text{if}U_{t}=0\\ 0&\text{otherwise}\end{cases}.$$

The principal would like the receiver to stay in the system as long as possible. The instantaneous reward for the principal is

$$r_{t}^{A}(X_{t},U_{t})=\begin{cases}1&\text{if}U_{t}=0\\ 0&\text{otherwise}\end{cases}$$
Setting p = 0.2 and c = 0.15, we obtained the qB
t and V A
t functions specified in Proposition 2—see Figure 5. The horizontal axis represents πt(−1). The figures follows the same interpretation as the figures in Example 2. (The markers for actions are different from previous figures, but they are self-explanatory.)
Different from Example 2, the value functions and CBB
strategies at equilibrium oscillate with a period of 4 (given p = 0.2, c = 0.15) instead of converging as t gets further away from the horizon T.

## Vi. Discussion

Naturally, one may consider extending the above result to two settings: (a) when a public noisy observation of the state is available in addition to the principal's experiment, (b) when there are multiple receivers. However, our result is immediately extendable to neither setting. This is since the techniques we use in this paper depend heavily on the piecewise linear structure of ˆq and V -functions in (1), as well as the preservation of this piecewise linear structure under backward induction. Specifically, when the functions
ˆqA
t , ˆqB
t are piecewise linear, the concave closure of ˆvA
t can be expressed as a triangulation based interpolation (through Lemma 3), which in turn allows us to apply the same triangulation to ˆvB
t , and thus ensuring the continuity and piecewise linearity of V B
t . However, this structure does not appear in general in the extensions.

We describe an attempt to extend Theorem 1 to settings
(a) and (b) in the most straightforward way. In the case of setting (a), one needs to change the belief update in (1a) from
ℓt(πt, ut) to some other update function that incorporates the public observation. However, unlike ℓt(πt, ut), the new update function may not be linear in πt. Therefore this procedure cannot preserve piecewise linear properties.

In the case of setting (b), ut will represent a vector of actions of all receivers, and one needs to change the definition of Υt(πt) in (1b) to be the set of mixed strategy Nash equilibrium (or alternatively correlated equilibrium) action profiles of the following stage game: Receiver i chooses an action in Ui t, and receives payoff ˆqi t(πt, ut). In this setting, Υt(πt) is a set of probability measures on the product set Ut. The new ˆvA
t function can then be given by

˜ut qA t (πt, ˜ut)ηt(˜ut) ˆvA t (πt) = arg max ηt∈Υt(πt) � However, in this case, continuity and piecewise linearity of $\hat{q}_{t}$ are not enough to ensure that the value function $V_{t}^{A}$ possesses the same property. To see this, consider the following example with two receivers $B$ and $C$. Let $\mathcal{U}_{t}^{B}=\mathcal{U}_{t}^{C}=\{1,2\}=\mathcal{X}_{t}=\{1,2\}$. Let $p=\pi_{t}(1)$. Then, all functions of $\pi_{t}$ can be expressed as a function of $p$. Suppose that

$$q_{t}^{B}(\pi_{t},u_{t})=\begin{cases}1&\text{if}u_{t}^{B}=u_{t}^{C}\\ 0&\text{otherwise}\end{cases},$$ $$q_{t}^{C}(\pi_{t},u_{t})=\begin{cases}p+1&\text{if}u_{t}^{B}=1,u_{t}^{C}=2\\ 1&\text{if}u_{t}^{B}=2,u_{t}^{C}=1\\ 0&\text{otherwise}\end{cases}.$$

It can be verified that, under either the concept of Nash equilibrium or correlated equilibrium, $\Upsilon_{t}(\pi_{t})$ contains only one element: player $B$ plays action 1 with probability $\frac{1}{2+p}$ and player $C$ plays their two actions with equal probability independent of player $B$'s action. Now suppose that

$$q_{t}^{A}(\pi_{t},u_{t})=\begin{cases}p&u_{t}^{B}=1\\ 0&\text{otherwise}\end{cases}.$$
Then we have ˆvA
t (πt) =
p

                      2+p for p ∈ [0, 1]. Observe that
ˆvA
t is a strictly concave function. Hence the concave closure
of ˆvA
   t is just ˆvA
           t itself, which is not piecewise linear.

## Vii. Conclusion And Future Work

In this work, we formulated a dynamic information disclosure game, called the signal picking game, where the principal sequentially commit to a signal/experiment to communicate with the receiver. We showed that there exist equilibria where both the principal and the receiver make decisions based on the canonical belief instead of their respective full information. We also provided a sequential decomposition procedure to find such equilibria.

Unlike the CIB-belief-based sequential decomposition procedures of [34], [35], [36], [37], the sequential decomposition procedure of Theorem 1 always has a solution. The main reason is that the CIB belief in the signal picking game is strategy-independent, just like in [32]. The result illustrates the critical difference between strategy-dependent and strategy-independent compression of information in dynamic games.

There are a few future research problems arising from this work. The first problem is to extend our result to infinite horizon games. The second problem is to extend our result to settings with multiple senders.

## References

[1] R. B. Myerson, "Mechanism design," in Allocation, Information and
Markets.
Springer, 1989, pp. 191–206.
[2] E. Kamenica and M. Gentzkow, "Bayesian persuasion," American
Economic Review, vol. 101, no. 6, pp. 2590–2615, 2011.
[3] D. Bergemann and J. V¨alim¨aki, "The dynamic pivot mechanism,"
Econometrica, vol. 78, no. 2, pp. 771–789, 2010.
[4] S. Athey and I. Segal, "An efficient dynamic mechanism," Econometrica, vol. 81, no. 6, pp. 2463–2485, 2013.
[5] A. Pavan, I. Segal, and J. Toikka, "Dynamic mechanism design: A
Myersonian approach," *Econometrica*, vol. 82, no. 2, pp. 601–653, 2014.
[6] D. Bergemann and J. V¨alim¨aki, "Dynamic mechanism design: An
introduction," *Journal of Economic Literature*, vol. 57, no. 2, pp. 235– 74, 2019.
[7] D. Lingenbrink and K. Iyer, "Optimal signaling mechanisms in unobservable queues with strategic customers," in Proceedings of the 2017
ACM Conference on Economics and Computation, 2017, pp. 347–347.
[8] J. C. Ely, "Beeps," *American Economic Review*, vol. 107, no. 1, pp.
31–53, 2017.
[9] F. Farokhi, A. M. Teixeira, and C. Langbort, "Estimation with strategic
sensors," *IEEE Transactions on Automatic Control*, vol. 62, no. 2, pp. 724–739, 2016.
[10] M. O. Sayin, E. Akyol, and T. Bas¸ar, "Strategic control of a tracking
system," in 2016 IEEE 55th Conference on Decision and Control (CDC).
IEEE, 2016, pp. 6147–6153.
[11] J. Renault, E. Solan, and N. Vieille, "Optimal dynamic information
provision," *Games and Economic Behavior*, vol. 104, pp. 329–349, 2017.
[12] J. Best and D. Quigley, "Honestly dishonest: A solution to the
commitment problem in Bayesian persuasion," Mimeo, Tech. Rep., 2016.
[13] ——, "Persuasion for the long-run," Economics Group, Nuffield
College, University of Oxford, Tech. Rep., 2016.
[14] P. B. Luh, S.-C. Chang, and T.-S. Chang, "Solutions and properties
of multi-stage Stackelberg games," *Automatica*, vol. 20, no. 2, pp. 251–256, 1984. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/0005109884900347
[15] B. Tolwinski, "A Stackelberg equilibrium for continuous-time differential games," in *The 22nd IEEE Conference on Decision and Control*,
1983, pp. 675–681.
[16] ——, "Closed-loop Stackelberg solution to a multistage linearquadratic game," *Journal of Optimization Theory and Applications*, vol. 34, no. 4, pp. 485–501, 1981.
[17] F. Farhadi, D. Teneketzis, and S. J. Golestani, "Static and dynamic
informational incentive mechanisms for security enhancement," in 2018 European Control Conference (ECC).
IEEE, 2018, pp. 1048–
1055.
[18] L. Li, O. Massicot, and C. Langbort, "Sequential public signaling in
routing games with feedback information," in 2018 IEEE Conference
on Decision and Control (CDC), 2018, pp. 2735–2740.
[19] M. O. Sayin and T. Bas¸ar, "Dynamic information disclosure for
deception," in *2018 IEEE Conference on Decision and Control (CDC)*.
IEEE, 2018, pp. 1110–1117.
[20] M. O. Sayin, E. Akyol, and T. Bas¸ar, "Hierarchical multistage Gaussian signaling games in noncooperative communication and control systems," *Automatica*, vol. 107, pp. 9–20, 2019.
[21] M. O. Sayin and T. Bas¸ar, "On the optimality of linear signaling to
deceive Kalman filters over finite/infinite horizons," in International Conference on Decision and Game Theory for Security.
Springer,
2019, pp. 459–478.
[22] E. Meigs, F. Parise, A. Ozdaglar, and D. Acemoglu, "Optimal
dynamic information provision in traffic routing," arXiv preprint arXiv:2001.03232, 2020.
[23] H. Tavafoghi and D. Teneketzis, "Informational incentives for congestion games," in 2017 55th Annual Allerton Conference on Communication, Control, and Computing (Allerton).
IEEE, 2017, pp.
1285–1292.
[24] F. Farhadi and D. Teneketzis, "Dynamic information design: A simple problem on optimal sequential information disclosure," Dynamic
Games and Applications, vol. 12, no. 2, pp. 443–484, 2022.
[25] S. Heinrich Von, "Market structure and equilibrium," 2011. [26] R. B. Myerson and P. J. Reny, "Perfect conditional ε-equilibria of
multi-stage games with infinite sets of signals and actions," Econometrica, vol. 88, no. 2, pp. 495–531, 2020.
[27] M. Gentzkow and E. Kamenica, "Bayesian persuasion with multiple
senders and rich signal spaces," *Games and Economic Behavior*, vol. 104, pp. 411–429, 2017.
[28] ——, "Disclosure of endogenous information," Economic Theory
Bulletin, vol. 5, no. 1, pp. 47–56, 2017.
[29] L. Doval and V. Skreta, "Mechanism design with limited commitment," *arXiv preprint arXiv:1811.03579*, 2018.
[30] J. De Loera, J. Rambau, and F. Santos, Triangulations: Structures for
algorithms and applications.
Springer Science & Business Media,
2010, vol. 25.
[31] P. R. Kumar and P. Varaiya, Stochastic systems: Estimation, identification and adaptive control.
Prentice-Hall, Inc., 1986.
[32] A. Nayyar, A. Gupta, C. Langbort, and T. Bas¸ar, "Common
information based Markov perfect equilibria for stochastic games with asymmetric information: Finite games," IEEE Transactions on
Automatic Control, vol. 59, no. 3, pp. 555–570, 2013. [Online].
Available: https://doi.org/10.1109/tac.2013.2283743
[33] D. Bergemann and S. Morris, "Information design: A unified perspective," *Journal of Economic Literature*, vol. 57, no. 1, pp. 44–95, 2019.
[34] Y. Ouyang, H. Tavafoghi, and D. Teneketzis, "Dynamic games
with asymmetric information: Common information based perfect Bayesian equilibria and sequential decomposition," IEEE Transactions on Automatic Control, vol. 62, no. 1, pp. 222–237, 2016. [Online].
Available: https://doi.org/10.1109/tac.2016.2544936
[35] H. Tavafoghi, Y. Ouyang, and D. Teneketzis, "On stochastic dynamic
games with delayed sharing information structure," in 2016 IEEE 55th
Conference on Decision and Control (CDC).
IEEE, 2016, pp. 7002–
7009. [Online]. Available: https://doi.org/10.1109/cdc.2016.7799348
[36] D. Vasal, A. Sinha, and A. Anastasopoulos, "A systematic process for
evaluating structured perfect Bayesian equilibria in dynamic games with asymmetric information," IEEE Transactions on Automatic
Control, vol. 64, no. 1, pp. 81–96, 2019. [Online]. Available: https://doi.org/10.1109/tac.2018.2809863
[37] D. Tang, H. Tavafoghi, V. Subramanian, A. Nayyar, and D. Teneketzis,
"Dynamic games among teams with delayed intra-team information sharing," *Dynamic Games and Applications*, 2022. [Online]. Available:
https://doi.org/10.1007/s13235-022-00424-4

## Appendix A. Proofs Of Discrete Geometric Results

Proof of Lemma 1. Let C1, · · · *, C*k be polytopes such that (i) f is linear on each of C1, · · · *, C*k (ii) C1 *∪ · · · ∪* Ck = Ω2.

Since ℓ is an affine function, we have the pre-images Dj = ℓ−1(Cj), j = 1, · · · *, k* to be polytopes as well.

f ◦ ℓ is linear on each Dj (since it is the composition of two linear functions), and D1 *∪ · · · ∪* Dk = Ω1. We conclude that f ◦ ℓ is a piecewise linear function.

Proof of Lemma 2. First, for any ω, given a simplex C such that ω ∈ C, there is a unique way to represent ω as a convex combination of vertices of C.

Suppose that ω is in both simplices C and C′. Then ω is in C ∩ C′, which is a face of both C and C′. Since C ∩ C′ is a simplex, ω can be uniquely represented as a convex combination of vertices of C ∩C′. Since the set of vertices of C ∩C′ is a subset of the vertices of both C and C′, we conclude that the above representation is also the unique way of representing
ω as a convex combination of vertices of C (and of C′). We conclude that for any ω, there is a unique way to represent ω
as a convex combination of vertices of any simplex in γ. Hence I(*f, γ*) is well defined.

For any simplex C ∈ γ, I(*f, γ*) is linear on C. Since the number of simplices in γ is finite and their union is Ω, we conclude that I(*f, γ*) is a continuous piecewise linear function on Ω.

Proof of Lemma 3. For j = 1, · · · *, k*, let Cj1, · · · *, C*jmj be polytopes corresponding to the piecewise linear function fj under Definition 2, i.e. fj is linear on each of Cj1, · · · *, C*jmj and Cj1 *∪ · · · ∪* Cjmj = Ω. Define

$$\mathcal{S}=\{C_{1i_{1}}\cap C_{2i_{2}}\cap\cdots\cap C_{ki_{k}}:1\leq i_{1}\leq m_{1},\cdots,1\leq i_{k}\leq m_{k}\}$$

$\mathcal{S}$ is a finite collection of polytopes. All of $f_{1},\cdots,f_{k}$ are linear on each element of $\mathcal{S}$. The union of $\mathcal{S}$ equals $\Omega$. Define

$$A_{j}:=\{\omega\in\Omega:f_{j}(\omega)\geq f_{j^{\prime}}(\omega)\quad\forall j^{\prime}=1,\cdots,k\},$$ $$\mathcal{S}_{j}=\{F\cap A_{j}:F\in\mathcal{S}\}.$$
Sj is the collection of subsets where fj is (one of) the maximum among f1, · · · *, f*k. Sj is also a finite collection of polytopes, since each F ∩ Aj is a subset of F that satisfy certain linear constraints.

Similarly, let Dj1, · · · *, D*jnj be polytopes corresponding to the piecewise linear function ρj. Define

$${\mathcal{R}}_{j}=\{F\cap D_{j i}:F\in{\mathcal{S}}_{j},1\leq i\leq n_{j}\}$$
For each polytope F *∈ R*j, ρj is linear on F, and fj is (one of) the maximum among f1, · · · *, f*k for all points in F.

The union of Rj equals Aj.

Let P be the set of vertices of polytopes in R1*∪· · ·∪R*k. P is a finite set. Define *B ⊂* Ω×R by B = {(ω, Ψ(ω)) : ω *∈ P}*.

Let Z be the convex hull of B. We have Z to be a polytope with its vertices contained in B.

Let ˆΨ be the concave closure of Ψ. We will show that the function ˆΨ is represented by the upper face of Z. Then we obtain a triangulation of Ω by projecting a triangulation of Z in a similar way to the construction of regular triangulations
(see Section 2.2 of [30]).

Step 1: Prove that ˆΨ(ω) = max{y : (ω, y) *∈ Z}*.

Define Ψ(ω) := max{y : (ω, y) *∈ Z}*. Ψ is a concave function.

It is clear that *Z ⊂* cvxg(Ψ), since B is a subset of the graph of Ψ. Therefore Ψ(ω) ≤ ˆΨ(ω).

Consider any ω ∈ Ω. Let j∗ be such that j∗ ∈ Υ(ω) and Ψ(ω) = ρj∗(ω). Then ω ∈ Aj∗. We have ω ∈ F for some F *∈ R*j∗. Let ω1, · · · , ωm *∈ P* be the vertices of F. We can write ω = α1ω1 + *· · ·* + αkωm for some α1, · · · , αm ≥
0, α1 + *· · ·* + αm = 1. Since ρj∗ is linear on F we have

$$\Psi(\omega)=\rho_{J^{*}}(\omega)=\alpha_{1}\rho_{J^{*}}(\omega_{1})+\cdots+\alpha_{k}\rho_{J^{*}}(\omega_{m})\tag{2}$$

Since $\omega_{1},\cdots,\omega_{m}\in F$ and $F\subset A_{J^{*}}$. By definition, $j^{*}\in\mathrm{T}(\omega_{i})$ for all $i=1,\cdots,m$. Therefore $\rho_{J^{*}}(\omega_{i})\leq\Psi(\omega_{i})$ for all $i=1,\cdots,m$. Consequently, combining (2) we have

$$\Psi(\omega)\leq\alpha_{1}\Psi(\omega_{1})+\cdots+\alpha_{k}\Psi(\omega_{m})$$
Given that (*ω, α*1Ψ(ω1) + · · · + αkΨ(ωk)) *∈ Z*, we have

$$\alpha_{1}\Psi(\omega_{1})+\cdots+\alpha_{k}\Psi(\omega_{k})\leq\overline{\Psi}(\omega)$$

Hence $\Psi(\omega)\leq\overline{\Psi}(\omega)$. Therefore, $\overline{\Psi}$ is a concave function above $h$. Since the concave closure $\hat{\Psi}(\omega)$ is the smallest concave function above $h$, we conclude that $\Psi(\omega)\leq\overline{\Psi}(\omega)$ for all $\omega\in\Omega$.

Therefore $\hat{\Psi}=\overline{\Psi}$, completing the proof of Step 1.

**Step 2:** Construct the triangulation $\gamma$ and show that $\hat{\Psi}=\mathbb{I}(h,\gamma)$.

Let *A ⊂* Ω × R be the graph of ˆΨ. A is also the union of upper faces of Z. Let ϑ be a point set triangulation (as defined in Def. 2.2.1 in [30]) of the finite point set B. (A point set triangulation of a finite set of points always exists. See Section
2.2.1 of [30].) Let ˆϑ be the restriction of ϑ to A, i.e. ˆϑ := {F : F ⊂ A, F ∈ ϑ}. It can be shown that ˆϑ is a simplicial complex (i.e. a polyhedral complex where all polytopes are simplices. See Def. 2.1.5 in [30].) with vertices contained in A ∩ B.

Since A is the upper convex hull of Z, the projection map projΩ : Ω × R �→ Ω, (*ω, y*) �→ ω is a bijection between A
and Ω. Let γ be the projection of ˆϑ on to Ω, i.e. γ = {projΩ(F) : F ∈ ˆϑ}. We conclude that γ is a simplical complex that spans Ω, i.e. a triangulation of Ω.

The inverse map proj−1
Ω
: Ω *�→ A* is a piecewise linear map that is linear on each simplex in γ. Therefore we have
ˆΨ(ω) = I(ˆΨ, γ)(ω) for all ω ∈ Ω. Since the vertices of ˆϑ are contained in both A and B, we have ˆΨ(ω) = Ψ(ω) for each vertex ω of γ. (Recall that B is a subset of the graph of h and A is the graph of ˆΨ.) Therefore we have ˆΨ(ω) = I(Ψ, γ)(ω)
for all ω ∈ Ω.

## B. Proof Of Main Results

Lemma 4. *There exist a belief system* µ∗ = (µ∗A, µ∗B) such that (i) µ∗ is consistent with any strategy profile (gA, gB);
(ii) the canonical belief system κ is the marginals of µ∗.

Proof of Lemma 4. Define µ∗i t : Hi t �→ ∆(X1:t) recursively through the following:

- µ∗A
1 (hA
1 ) := ˆπ.
˜x1:t µ∗A
t (˜x1:t|hA
t )σt(mt|˜xt)
- µ∗B
t (x1:t|hB
t ) :=
µ∗A
t (x1:t|hA
t )σt(mt|xt)
�
- µ∗A
t+1(x1:t+1|hA
t+1) := µ∗B
t (x1:t|hB
t )P(xt+1|xt, ut)
Through induction on t it is clear that κ is the marginal distribution derived from µ∗.
It remains to show the consistency of µ∗ w.r.t. any strategy profile g = (gA, gB). We will also show it via induction:
- µ∗A
1
is clearly consistent with any g since it is defined to be the prior distribution of X1.
- Suppose that µ∗A
t
is consistent with g. Then consider any hB
t = (σ1:t, m1:t, u1:t−1) ∈ HB
t such that Pg(hB
t ) > 0. Then
we have Pg(hA
t ) > 0, and µ∗A
t (x1:t|hA
t ) = Pg(x1:t|hA
t ) follows by induction hypothesis. Therefore
Pg(x1:t|hB t ) = Pg(x1:t|σt, mt, hA t ) = Pg(x1:t, σt, mt, hA t ) Pg(σt, mt, hA t ) ˜x1:t Pg(˜x1:t, hA t )Pg(σt|˜x1:t, hA t )Pg(mt|σt, ˜x1:t, hA t ) = Pg(x1:t, hA t )Pg(σt|x1:t, hA t )Pg(mt|σt, x1:t, hA t ) � ˜x1:t Pg(˜x1:t, hA t )gA t (σt|hA t )σt(mt|˜xt) = Pg(x1:t, hA t )gA t (σt|hA t )σt(mt|xt) � ˜x1:t Pg(˜x1:t|hA t )σt(mt|˜xt) = Pg(x1:t, hA t )σt(mt|xt) � ˜x1:t Pg(˜x1:t, hA t )σt(mt|˜xt) = Pg(x1:t|hA t )σt(mt|xt) � ˜x1:t µ∗A t (˜x1:t|hA t )σt(mt|˜xt) = µ∗B t (x1:t|hB t ) = µ∗A t (x1:t|hA t )σt(mt|xt) �
which means that µ∗B
t is consistent with g.

- Suppose that µ∗B
t
is consistent with g. Then consider any hA
t+1 = (σ1:t, m1:t, u1:t) ∈ HA
t+1 such that Pg(hA
t+1) > 0.
Then we have Pg(hB
t ) > 0, and µ∗B
t (x1:t|hB
t ) = Pg(x1:t|hB
t ) follows by induction hypothesis. Then we have
Pg(x1:t+1|hA t+1) = Pg(x1:t+1, hA t+1) Pg(hA t+1) $$=\frac{\mathbb{P}^{g}(x_{1:t},h_{t}^{B})\mathbb{P}^{g}(u_{t}|x_{1:t},h_{t}^{B})\mathbb{P}^{g}(x_{t+1}|x_{1:t},u_{t},h_{t}^{B})}{\sum_{\tilde{x}_{1:t},\ \mathbb{P}^{g}(\tilde{x}_{1:t},h_{t}^{B})\mathbb{P}^{g}(u_{t}|\tilde{x}_{1:t},h_{t}^{B})}$$ $$=\frac{\mathbb{P}^{g}(x_{1:t},h_{t}^{B})g_{t}^{B}(u_{t}|h_{t}^{B})\mathbb{P}(x_{t+1}|x_{t},u_{t})}{\sum_{\tilde{x}_{1:t},\ \mathbb{P}^{g}(\tilde{x}_{1:t},h_{t}^{B})g_{t}(u_{t}|h_{t}^{B})}$$ $$=\frac{\mathbb{P}^{g}(x_{1:t},h_{t}^{B})}{\sum_{\tilde{x}_{1:t},\ \mathbb{P}^{g}(\tilde{x}_{1:t},h_{t}^{B})}}\cdot\mathbb{P}(x_{t+1}|x_{t},u_{t})=\mu_{t}^{*B}(x_{1:t}|h_{t}^{B})\mathbb{P}(x_{t+1}|x_{t},u_{t})$$ $$=\mu_{t}^{*A}(x_{1:t+1}|h_{t+1}^{A})$$
which means that µ∗A
t+1 is consistent with g.

Proof of Theorem 1. Let µ∗ be a belief system that satisfies Lemma 4. It is shown by Lemma 4 that µ∗ is consistent with
any strategy profile g. Hence to show that λ∗ forms a CBB-PBE we only need to show sequential rationality.
  Step 1: Fixing the principal's strategy to be λ∗A, show that λ∗B
                                                            τ:T is sequentially rational at any hB
                                                                                             τ ∈ HB
                                                                                                   τ at any time τ,
given the belief µ∗B
                τ (hB
                     τ ).
  To prove Step 1, we argue that at hB
                                    τ , the receiver is facing an MDP problem with state process ΠB
                                                                                                 t = κB
                                                                                                        t (HB
                                                                                                            t ) and
action Ut for t ≥ τ.
  First, we can write

� t=τ rB t (Xt, Ut) Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T � T � � t=τ Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T [rB t (Xt, Ut)|HB t , Ut] = Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T � T �

where for any hB
               t such that Pµ∗B
                             τ
                               (hB
                                 τ ),λ∗A
                                    t
                                      ,gB
                                        τ:T (hB
                                             t ) > 0 we have

˜x1:t rB t (˜xt, ut)Pµ∗B τ (hB τ ),λ∗A t ,gB τ:T (˜x1:t|hB t ) Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T [rB t (Xt, Ut)|hB t , ut] = � ˜xt rB t (˜xt, ut)πB t (˜xt) =: ˜rB t (πB t , ut) = �

where πB
      t := κB
            t (hB
                t ). The second equality is true due to Lemma 4.
  Therefore we can write

. � � t=τ ˜rB t (ΠB t , Ut) t=τ rB t (Xt, Ut) = Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T � T � Eµ∗B τ (hB τ ),λ∗A t ,gB τ:T � T �

 We now show that ΠB
                    t
                       is a controlled Markov Chain controlled by Ut. By Definition 6, we have ΠB
                                                                                         t+1
                                                                                             =
ξt+1(ΠA
     t+1, Σt+1, Mt+1), where ΠA
                          t+1 = ℓt(ΠB
                                   t , Ut), Σt+1 = λ∗B
                                                t+1(ΠA
                                                    t+1). Therefore we have

Pµ∗B τ (hB τ ),λ∗A t ,gB τ:T (πB t+1|hB t , ut) ˜mt+1 1{πB t+1=ξt+1(πA t+1,σt+1, ˜mt+1)}Pµ∗B τ (hB τ ),λ∗A t ,gB τ:T ( ˜mt+1|hB t , ut) = � ˜xt+1 σt+1( ˜mt+1|˜xt+1)Pµ∗B τ (hB τ ),λ∗A t ,gB τ:T (˜xt+1|hA t+1) = � ˜mt+1 1{πB t+1=ξt+1(πA t+1,σt+1, ˜mt+1)} � ˜xt+1 σt+1( ˜mt+1|˜xt+1)πA t+1(˜xt+1) = � ˜mt+1 1{πB t+1=ξt+1(πA t+1,σt+1, ˜mt+1)} � ˜xt+1 σt+1( ˜mt+1|˜xt+1)πA t+1(˜xt+1)

where πA
      t+1 = ℓt(πB
               t , ut), σt+1 = λ∗A
                             t+1(πA
                                  t+1). The last equality is true due to Lemma 4.
  By construction, σt+1 = λ∗A
                        t+1(πA
                             t+1) induces the distribution C(πA
                                                         t+1, γt+1) from πA
                                                                        t+1. This means that
                         �

˜mt+1 1{πB t+1=ξt+1(πA t+1,σt+1, ˜mt+1)} � = C(πA t+1, γt+1)(πB t+1)
We conclude that

Pµ∗B τ (hB τ ),λ∗A t ,gB τ:T (πB t+1|hB t , ut) = C(ℓt(πB t , ut), γt+1)(πB t+1).

  In particular, this means that the conditional distribution of ΠB
                                                                   t+1 given all of (ΠB
                                                                                       1:t, U B
                                                                                            1:t) is dependent only on (ΠB
                                                                                                                          t , Ut),
proving that ΠB
               t is a controlled Markov Chain controlled by Ut for t ≥ τ.
  Therefore, at hB
                  τ , the receiver faces an MDP problem with state ΠB
                                                                          t , action Ut, instantaneous reward ˜rB
                                                                                                                  t (ΠB
                                                                                                                      t , Ut) and
transition kernel P(πB
                     t+1|πB
                           t , ut) = C(ℓt(πB
                                            t , ut), γt+1)(πB
                                                            t+1).
  Now, by construction, we know that

ˆvB t (πB t ) = max ut � ˜xt rB t (˜xt, ut)πt(˜xt) + V B t+1(ℓt(πt, ut)) �� = max ut � ˜rB t (πB t , ut) + � ˆvB t+1(·)dC(ℓt(πB t , ut), γt+1) � (3)

and λ∗B
     t (πB
         t ) attains the maximum in (3). Therefore λ∗B
                                                τ:T solves the Bellman equation for the MDP problem specified
above, and hence is an optimal strategy. Furthermore, V B
                                                1 (ˆπ) =
                                                       �
                                                         ˆvB
                                                          1 (·)dC(ˆπ, γt) is the optimal total expected payoff for
the receiver when the principal plays λ∗A.
  Step 2: Fixing the receiver's strategy to be λ∗B, show that λ∗A
                                                      τ:T is sequentially rational at any hA
                                                                                     τ ∈ HA
                                                                                          τ at any time τ,
given the belief µ∗A
               τ (hA
                   τ ).
  Similar to Step 1, we argue that at hA
                                  τ , the principal is facing an MDP problem with state process ΠA
                                                                                         t = κA
                                                                                               t (HA
                                                                                                  t ) and
action Σt for t ≥ τ.
  First, we write

� � t=τ rA t (Xt, Ut) t=τ Eµ∗A τ (hA τ ),gA τ:T ,λ∗B t [rA t (Xt, Ut)|HA t , Σt] Eµ∗A τ (hA τ ),gA τ:T ,λ∗B t � T � = Eµ∗A τ (hA τ ),gA τ:T ,λ∗B t � T �

  Given that the receiver uses the CBB strategy λ∗B, we know that Ut = λ∗B
                                                                          t (ΠB
                                                                                t ) where ΠB
                                                                                            t = ξt(ΠA
                                                                                                     t , Σt, Mt). For any
hA
 t such that Pµ∗A
                τ
                  (hA
                    τ ),gA
                       τ:T ,λ∗B
                            t (hA
                                t ) > 0 we have

Eµ∗A τ (hA τ ),gA τ:T ,λ∗B t [rA t (Xt, Ut)|hA t , σt] ˜xt, ˜mt rA t (˜xt, λ∗B t (ξt(πA t , σt, ˜mt)))Pµ∗A τ (hA τ ),gA τ:T ,λ∗B t ( ˜mt, ˜xt|hA t , σt) = � ˜xt, ˜mt rA t (˜xt, λ∗B t (ξt(πA t , σt, ˜mt)))σt( ˜mt|˜xt)Pµ∗A τ (hA τ ),gA τ:T ,λ∗B t (˜xt|hA t , σt) = � $$=\sum_{\delta_{+},\eta_{t}}^{\pi,\pi}r_{t}^{A}(\tilde{x}_{t},\lambda_{t}^{\pi}{}^{B}(\xi_{t}(\pi_{t}^{A},\sigma_{t},\tilde{m}_{t})))\sigma_{t}(\tilde{m}_{t}|\tilde{x}_{t})\pi_{t}^{A}(\tilde{x}_{t})=:\tilde{r}_{t}^{A}(\pi_{t}^{A},\sigma_{t})$$

where $\pi_{t}^{A}:=r_{t}^{A}(h_{t}^{A})$. The third equality is true due to Lemma 4.

Therefore we can write

$$\mathbb{E}^{\mu,\tau^{A}(h_{t}^{A}),\sigma_{t-\tau}^{A},\lambda_{t}^{\pi}}\left[\sum_{t=\tau}^{T}r_{t}^{A}(X_{t},U_{t})\right]=\mathbb{E}^{\mu,\tau^{A}(h_{t}^{A}),\sigma_{t-\tau}^{A},\lambda_{t}^{\pi}}\left[\sum_{t=\tau}^{T}\tilde{r}_{t}^{A}(\Pi_{t}^{A},\Sigma_{t})\right].$$

We now show that $\Pi_{t}^{A}$ is a controlled Markov process with action $\Sigma_{t}$. We know that 

ΠA
 t+1 = ℓt(ΠB
       t , U B
         t ),
              U B
               t = λ∗B
                  t (ΠB
                     t ),
                          ΠB
                           t = ξt(ΠA
                                t , Σt, Mt).

Hence ΠA
       t+1 is a function of ΠA
                         t , Σt, and Mt. Furthermore,

˜xt σt(mt|˜xt)Pµ∗A τ (hA τ ),gA τ:T ,λ∗B t (˜xt|hA t , σt) Pµ∗A τ (hA τ ),gA τ:T ,λ∗B t (mt|hA t , σt) = � ˜xt σt(mt|˜xt)πA t (˜xt). = �

Therefore the conditional distribution of ΠA
                                           t+1 given (HA
                                                         t , Σt) depends only on (ΠA
                                                                                     t , Σt), proving that ΠA
                                                                                                            t is a controlled
Markov process. We conclude that at hA
                                       τ , the principal faces an MDP problem with state ΠA
                                                                                             t , action Σt, and instantaneous
reward ˜rA
        t (ΠA
             t , Σt) for t ≥ τ.
  Next we will show that λ∗A
                            τ:T is a dynamic programming solution of this MDP.
  Induction Variant: V A
                        t , as defined in (1f), is the value function for this MDP.
  Induction Step: Suppose that V A
                                   t+1 is the value function for this MDP at time t + 1 and consider the stage optimization
problem at πA
             t .
  Note that the instantaneous cost can be written as

˜xt, ˜mt rA t (˜xt, λ∗B t (ξt(πA t , σt, ˜mt)))σt( ˜mt|˜xt)πA t (˜xt) ˜rA t (πA t , σt) = � � ˜mt ˆxt σt( ˜mt|ˆxt)πA t (ˆxt) ˆxt σt( ˜mt|ˆxt)πA t (ˆxt) = � �� � �� ˜xt rA t (˜xt, λ∗B t (ξt(πA t , σt, ˜mt))) σt( ˜mt|˜xt)πA t (˜xt) � � ˜mt ˜xt rA t (˜xt, λ∗B t (ξt(πA t , σt, ˜mt)))ξt(πA t , σt, ˜mt)(˜xt) ˆxt σt( ˜mt|ˆxt)πA t (ˆxt) = � �� � �� = E � �� ˜xt rA t (˜xt, λ∗B t (ΠB t ))ΠB t (˜xt) ���πA t , σt
where ΠB
t is a random distribution that follows the distribution induced by σt from πA
t .

Hence objective function for the stage optimization can be written as

$$\tilde{Q}_{t}^{A}(\pi_{t}^{A},\sigma_{t})=\tilde{r}_{t}^{A}(\pi_{t}^{A},\sigma_{t})+\mathbb{E}[V_{t+1}^{A}(\Pi_{t+1}^{A})|\pi_{t}^{A},\sigma_{t}]$$ $$=\tilde{r}_{t}^{A}(\pi_{t}^{A},\sigma_{t})+\mathbb{E}[V_{t+1}^{A}(\ell_{t}(\Pi_{t}^{B},\lambda_{t}^{*B}(\Pi_{t}^{B})))|\pi_{t}^{A},\sigma_{t}]$$ $$=\mathbb{E}\left[\tilde{v}_{t}^{A}(\Pi_{t}^{B})|\pi_{t}^{A},\sigma_{t}\right]$$
where

$$\hat{v}_{i}^{A}(\pi_{i}):=\sum_{\pi_{k}}r_{i}^{A}(\hat{x}_{k},\lambda_{i}^{B}(\pi_{i}))\pi_{i}(\hat{x}_{k})+V_{i+1}^{A}(\ell_{i}(\pi_{i}^{B},\lambda_{i}^{B}(\pi_{i}^{B})))$$

By construction of $\lambda_{i}^{B}$, we know that $\hat{v}_{i}^{A}=\hat{v}_{i}^{A}$ (defined in (1c)). Therefore, the stage optimization problem can be reformulated as:

$$\max_{r_{i}\in\mathcal{U}_{i}(\mathcal{X}_{i}\cup\mathcal{X}_{i})}\left\{\hat{v}_{i}^{A}(\cdot)dv_{i}\right.$$ (SP) subject to $$\left.\nu_{i}\right.$$ is incomplete from $$\pi_{i}^{A}$$

and the optimal signal is any signal that induces an optimal distribution ν∗
                                                                           t of (SP) from πA
                                                                                            t .
  By the seminal result on one-shot information design in [2], we know that the optimal value of (SP) is given by the
concave closure of the function ˆvA
                                 t evaluated at πA
                                                  t .
  By construction, we have V A
                                t
                                   to be the concave closure of ˆvA
                                                                     t . Furthermore, λ∗A
                                                                                        t (πA
                                                                                             t ) is assumed to induce the
distribution νt = C(πA
                      t , γt), where we know that
                                                   �
                                                     ˆvA
                                                       t (·)dC(πA
                                                                t , γt) = V A
                                                                            t (πA
                                                                                t ). Hence λ∗A
                                                                                             t (πA
                                                                                                  t ) is an optimal solution
for the stage optimization problem, and V A
                                          t
                                             is the value function at time t, proving the induction step.

  We conclude that λ∗A
                    τ:T is an optimal strategy for the principal at hA
                                                                τ given the belief system µτ(hA
                                                                                             τ ) and the receiver's
strategy λ∗B. Furthermore, V A
                          1 (ˆπ) is the optimal total expected payoff for the principal when the receiver plays λ∗A. Hence
we have completed the proof of sequential rationality.

