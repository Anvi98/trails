
## Hyper Strategy Logic

Raven Beutner CISPA Helmholtz Center for Information Security Germany

## Abstract

Strategy logic (SL) is a powerful temporal logic that enables strategic reasoning in multi-agent systems. SL supports explicit (first-order) quantification over strategies and provides a logical framework to express many important properties such as Nash equilibria, dominant strategies, etc. While in SL the same strategy can be used in multiple strategy profiles, each such profile is evaluated w.r.t. a pathproperty, i.e., a property that considers the *single* path resulting from a particular strategic interaction. In this paper, we present Hyper Strategy Logic (HyperSL), a strategy logic where the outcome of multiple strategy profiles can be compared w.r.t. a *hyperproperty*, i.e., a property that relates *multiple* paths. We show that HyperSL
can capture important properties that cannot be expressed in SL, including non-interference, quantitative Nash equilibria, optimal adversarial planning, and reasoning under imperfect information. On the algorithmic side, we identify an expressive fragment of HyperSL with decidable model checking and present a model-checking algorithm. We contribute a prototype implementation of our algorithm and report on encouraging experimental results.

## Keywords

Strategy Logic, Hyperproperties, Model Checking, Imperfect Information, Nash Equilibrium, Information-Flow Cotrol ACM Reference Format:
Raven Beutner and Bernd Finkbeiner. 2024. Hyper Strategy Logic. In Proc.

of the 23rd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2024), Auckland, New Zealand, May 6 - 10, 2024, IFAAMAS,
18 pages.

## 1 Introduction

Two important developments in the area of reactive systems concern the study of strategic properties in multi-agent systems (MAS)
and the study of hyperproperties. *Strategic properties* analyze the ability of agents to achieve a goal against (or in cooperation) with other agents. Logics such as alternating-time temporal logic (ATL∗)
[2] and strategy logic (SL) [24, 45] reason about the temporal interaction of such agents and allow for rigorous correctness guarantees using techniques such as model-checking. *Hyperproperties* [27] are properties that relate *multiple* executions within a system. Hyperproperties occur in many situations in computer science where traditional path properties (that refer to *individual* system execution) are not sufficient. Typical examples include **(1)** *optimality*, e.g., This work is licensed under a Creative Commons Attribution International 4.0 License.

Bernd Finkbeiner CISPA Helmholtz Center for Information Security Germany

one path reaching a goal faster than all other paths; **(2)**_information-flow policies_, e.g., requiring that any two paths with identical low-security input should produce the same low-security output [42]; and **(3) robustness_, i.e., stating that similar inputs should lead to similar outputs [25].

Such hyperproperties are also of vital importance in MASs. For example, we might ask if some agent has a strategy to achieve a goal without leaking information (an information-flow property) or can achieve a goal faster than some other agent (an optimality requirement). Yet existing logics for strategic reasoning (such as variants of SL [24, 45]) cannot express such hyper-requirements (we discuss related approaches in Section 2). We illustrate this on the example of Nash equilibria.

Assume we are given a MAS with agents $\{1,\ldots,n\}$ and LTL properties $\psi_{1},\ldots,\psi_{n}$ that describe the objectives of the agents. Agent $i$ wants to make sure that $\mathsf{F}\,\psi_{i}$ holds, i.e., formula $\psi_{i}$_eventually_ holds. We want to check whether the system admits a Nash equilibrium, i.e., there exists a strategy for each agent such that no agent has an incentive to deviate in order to fulfill her objective [48]. In SL, we can express the existence of a Nash equilibrium as follows:

$$\exists x_{1},\ldots,x_{n}.\,\psi_{n}.\,\bigwedge_{i=1}^{n}\Bigl{(}(\mathsf{F}\,\psi_{i})(\vec{x}[i\mapsto y])\to(\mathsf{F}\,\psi_{i})(\vec{x})\Bigr{)}$$ where we abbreviate the strategy profiles $\vec{x}=(x_{1},\ldots,x_{n})$ and $\vec{x}[i\mapsto y]=(x_{1},\ldots,x_{i-1},y,x_{i+1},\ldots,x_{n})$. In the variant SL we consider here (similar to the SL by Chatterjee et al. [24]), atomic formulas have the form $\psi(\vec{x})$ where $\psi$ is an LTL formula, and $\vec{x}$ is a strategy profile that assigns a strategy to each agent. Formula $\psi(\vec{x})$ holds if the unique path that results from the interaction of the strategies in $\vec{x}$ satisfies $\psi$. The above formula thus states that if some agent $i$ can achieve $\psi$? by playing some deviating strategy $y$ instead of $x_{i}$, i.e., the unique play that results from strategy profile also holds under strategy profile $\vec{x}$.

In the formula, we effectively compare two plays under strategy profiles $\vec{x}$ and $\vec{x}[i\mapsto y]$. However, SL limits the comparison between multiple interactions to a boolean combination of LTL properties on their outcomes (paths). In game-theoretic terms, the above formula assumes that the reward for each agent is binary; the reward of agent $i$ is maximal if $\mathrm{F}\,\psi_{i}$ holds and minimal if it does not. This fails to capture quantitative reward, for example, in a setting where agent $i$ receives a higher reward (and thus deviates) by fulfilling $\psi_{i}$_someor_. To express the existence of such a quantitative equilibrium, a boolean formula over individual temporal properties on strategy profiles $\vec{x}$ and $\vec{x}[i\mapsto y]$ is not sufficient. We need a more powerful mechanism that can compare the temporal behavior of _multiple_ paths: a _hyperproperty_.

HyperSL. In this paper, we propose HyperSL - a new temporal logic that combines first-order strategic reasoning (as in SL) with

the ability to compare _multiple_ paths w.r.t. a hyperproperty. Syntatically, we use path variables to refer to multiple paths at the same time (similar to existing hypergencies such as HyperCTL[26] and HyperALPLE[14, 117]). In HyperS${}_{1}$, atomic formulas have the form $\psi[\pi_{1}:\vec{x}_{1}\ldots,\vec{x}_{m}:\vec{x}_{m}]$ where $\pi_{1},\ldots,\pi_{m}$ are path variables, $\vec{x}_{1},\ldots,\vec{x}_{m}$ are strategy profiles (assigning a strategy to each agent), and $\psi$ is an LTL formula where atomic propositions are indexed by path variables from $\pi_{1},\ldots,\pi_{m}$. The formula states that the plays resulting from strategy profiles $\vec{x}_{1},\ldots,\vec{x}_{m}$, when bound to $\pi_{1},\ldots,\pi_{m}$, (together) satisfy the hyperproperty expressed by $\psi$.

Coming back to the Nash equilibrium example from before, we can use HyperS${}_{1}$ to express the existence of a Nash equilibrium in a quantitative reward setting as follows:

$$\exists x_{1},\ldots,x_{n}.\forall y.\bigwedge_{i=1}^{n}\left((\neg\psi_{i\pi_{1}}\ \mathsf{W}\,\psi_{i\pi_{2}})\left[\pi_{1}:\vec{x}[i\mapsto y]\right]\right)$$

Here, we write $\psi_{i\pi_{1}}\left(\neg\psi_{i\pi_{1}}\ \mathsf{W}\,\psi_{i\pi_{2}}\right)$ to state that $\psi_{i}$ holds on path $\pi_{1}$ (resp. $\pi_{2}$). In the formula, we again quantify over a deviating strategy $y$, but can compare the two paths resulting from strategy $\vec{x}[i\mapsto y]$ and $\vec{x}$ within the _same_ temporal formula. This formula states that path $\pi_{1}$ (constructed using strategy profile $\vec{x}[i\mapsto y]$ does not satisfy $\psi_{i}$ strictly before $\psi_{i}$ holds on path $\pi_{2}$ (constructed using strategy profile $\vec{x})$.[1] If the above formula holds, $\vec{x}$ is thus constitutes a strategy profile such that no agent could achieve its goal strictly sooner (if at all).

Note that we can express any Nash equilibrium as long as "agent"
𝑖 (strictly) prefers the outcome on path 𝜋1 over that on path 𝜋2" is expressible using an LTL formula over 𝜋1, 𝜋2. Likewise, HyperSL
can, e.g., express that some strategy **(1)** reaches a goal without leaking information, **(2)** is at least as fast as any other strategy, or
(3) is robust w.r.t. the behavior of other agents.

Expressiveness of HyperSL. After we introduce HyperSL (in Section 4), we study its relation to existing logics (in Section 5). We show that HyperSL subsumes many non-hyper strategy logics as well as hyperlogics such as HyperCTL∗ [26], HyperATL∗ [14, 17], and HyperATL∗
𝑆 [18] (see Section 2). Moreover, HyperSL also admits reasoning under imperfect information despite having a semantics defined under complete information. The key observation here is that "acting under imperfect information" *is a hyperproperty*: a strategy acts under imperfect information if, on any *pair* of paths with the same observation, the strategy chooses the same action.

Formally, we show that HyperSL subsumes SLii [12, 13], a strategy logic centered around imperfect information.

Model Checking. HyperSL's ability to compare multiple strategic interactions renders model-checking (MC) undecidable. In Section 6, we identify a fragment of our logic - called HyperSL[SPE] - for which MC is possible. Intuitively, in HyperSL[SPE], the quantifier prefix should be such that we can group it into individual "blocks"
where the strategy variables from each block are used on independent path variables. HyperSL[SPE] subsumes SL[1G] (the singlegoal fragment of SL) [46], HyperLTL [26], HyperATL∗ [14, 17], and HyperATL∗
𝑆 [18], but also captures properties that cannot be expressed in existing logics. We argue that HyperSL[SPE] is the largest fragment with a decidable model-checking problem that is defined purely in terms of the quantification structure.

Implementation and Experiments. We implement our MC algorithm for HyperSL[SPE] in the HyMASMC tool [18] and experiment with various MAS models (in Section 7). Our experiments show that HyMASMC performs well on many *non*-hyper strategy logic specifications and can verify complex hyperproperties that cannot be expressed in any existing logic.

## 2 Related Work

SL has been extended along multiple dimensions, including agentunbinding [37], reasoning about probabilities [4], epistemic properties [7, 10, 41], and quantitative properties [20]. We refer to [45, 49] for a more in-depth discussion. The common thread in all the previous extensions is a focus on the temporal behavior on individual paths. HyperSL generalizes SL and is the first to compare multiple paths. Even quantitative extensions like SL[F ] [20] evaluate an LTL[F ]-formula on a *per-path* basis. In contrast, HyperSL can express complex relationships *between* paths.

Studying logics that can express strategic properties under imperfect information has attracted much attention and led to various extensions of ATL∗ [10, 11, 22, 29, 38] and SL [12, 36]. Berthon et al. [12] showed that their logic, SLii, subsumes most existing approaches. We show that HyperSL can also reason about imperfect information (and subsumes SLii) despite having a semantics that is defined under full information.

Logics for expressing hyperproperties in non-agent-based systems (e.g., labeled transition systems) have been obtained by extending existing temporal or first-order logics with explicit path quantification over path/trace variables or an equal-level predicate [15, 26, 28, 34, 35]. As strategic reasoning is significantly more powerful than pure path quantification, HyperSL subsumes HyperCTL∗ (when interpreting transition systems as single-agent MASs). HyperATL∗ [14, 17] and HyperATL∗
𝑆 [18] extend alternatingtime temporal logic (ATL∗) [2] with path variables and strategysharing constraints, leading to a strategic hyperlogic that can express important security properties such as non-deducibility of strategies [54] and simulation security [51]. Similar to ATL∗, the strategic reasoning in HyperATL∗ and HyperATL∗
𝑆 is limited to implicit reasoning about the strategic ability of coalitions of agents and cannot explicitly reason about strategies as, e.g., needed to express the existence of a Nash equilibrium.

Our model-checking algorithm for HyperSL[SPE] is based on an iterative elimination of path (variables) in an automaton, similar to existing algorithms for HyperCTL∗ [33] and HyperATL∗ [17, 18].

Compared to HyperATL∗, we need to eliminate paths by simulating an *arbitrary* prefix of strategy quantifiers, leading to a more involved construction and more complex correctness proof.

## 3 Preliminaries

We let AP be a fixed finite set of atomic propositions and fix a fixed finite set of agents Agts = {1*, . . . ,*𝑛}. Given a set 𝑋, we write 𝑋 +
(resp. 𝑋𝜔) for the set of non-empty finite (resp. infinite) sequences over 𝑋. For 𝑢 ∈ 𝑋𝜔 and 𝑗 ∈ N, we write 𝑥(𝑗) for the 𝑖th element,
𝑢[0, 𝑗] for the finite prefix up to position 𝑗 (of length 𝑗 + 1), and 𝑢[𝑗, ∞] for the infinite suffix starting at position 𝑗.

𝑖∈*Agts* 𝑎𝑖 for the action profile where each agent Concurrent Game Structures. As the underlying model of MASs, we use concurrent game structures (CGS) [2]. A CGS is a tuple G = (𝑆,𝑠0, A*,𝜅, 𝐿*) where 𝑆 is a finite set of states, 𝑠0 ∈ 𝑆 is an initial state, A is a finite set of actions, 𝜅 : 𝑆 × (*Agts* → A) → 𝑆 is a transition function, and 𝐿 : 𝑆 → 2AP is a labeling function. The transition function takes a state 𝑠 and an action profile �𝑎 : *Agts* → A
(mapping each agent an action) and returns a unique successor state
𝜅(𝑠, �𝑎). We write �
𝑖 is assigned action 𝑎𝑖.

A strategy in G is a function 𝑓 : 𝑆+ → A, mapping finite plays to actions. We denote the set of all strategies in G with Str(G). A *strategy profile* �
𝑖∈*Agts* 𝑓𝑖 assigns each agent 𝑖 a strategy 𝑓𝑖 ∈ *Str*(G). Given strategy profile �
𝑖∈*Agts* 𝑓𝑖 and state 𝑠 ∈ 𝑆, we can define the unique path resulting from the interaction between the agents: We define *Play*G(𝑠, �
𝑖∈Agts 𝑓𝑖 (𝑝[0, 𝑗]) in which each agent
𝑖∈*Agts* 𝑓𝑖) as the unique path 𝑝 ∈ 𝑆𝜔 such that 𝑝(0) = 𝑠 and for every 𝑗 ∈ N we have
𝑝(𝑗 + 1) = 𝜅�𝑝(𝑗), �
𝑖 plays the action determined by 𝑓𝑖 on the current prefix 𝑝[0, 𝑗].

𝑖∈Agts 𝑓𝑖 (𝑝[0, 𝑗])�. That is, in every step, we construct the action profile �
Alternating Automata. Our model-checking algorithm is based on alternating automata over infinite words. These automata generalize nondeterministic automata by alternating between nondeterministic and universal transitions [53]. For transitions of the former kind, we can choose *some* successor state; for transitions of the latter type, we need to consider *all* possible successor states. Formally, an *alternating parity automaton (APA)* over alphabet Σ is a tuple A = (𝑄,𝑞0*,𝛿,𝑐*) where 𝑄 is a finite set of states, 𝑞0 ∈ 𝑄 is an initial state, 𝑐 : 𝑄 → N is a color assignment, and 𝛿 : 𝑄 × Σ → B+(𝑄)
is a transition function that maps each state-letter pair to a positive boolean formula over 𝑄 (denoted with B+(𝑄)). For example, if 𝛿(𝑞,𝑙) = 𝑞1 ∨ (𝑞2 ∧ 𝑞3), we can - from state 𝑞 ∈ 𝑄 and upon reading letter 𝑙 ∈ Σ - either move to state 𝑞1 or move to *both* 𝑞2
and 𝑞3 (i.e., we spawn two copies of our automaton, one starting in state 𝑞2 and one in 𝑞3). We write L(A) ⊆ Σ𝜔 for the set of all infinite words for which we can construct a run tree that respects the transition formulas such that the *minimal* color that occurs infinitely many times (as given by 𝑐) is *even*. For space reasons, we cannot give a formal semantics of APA runs and instead refer the reader to Appendix A. No specific knowledge about APAs is required to understand the high-level idea of our algorithm.

A special kind of APAs are deterministic parity automata (DPA)
in which 𝛿 is a function 𝑄 × Σ → 𝑄 assigning a unique successor state to each state-letter pair. We can always determinize APAs:
Proposition 1 ([44, 50]). For any APA A with 𝑛 states, we can effectively compute a DPA A′ with at most 22O(𝑛) states such that L(A) = L(A′).

## 4 Hyper Strategy Logic

Our new logic HyperSL is centered around the idea of combining strategic reasoning (as possible in strategy logic [24, 45]) with the ability to express hyperproperties (as possible in logics such as HyperCTL∗ [26]). To accomplish this, we combine the ideas from both disciples. On the strategy-logic-side, we use strategy variables to quantify over strategies. On the hyper-side, we use path variables to compare multiple paths within a temporal formula.

Let X be a set of *strategy variables* and V a set of *path variables*.

We typically use lowercase letters (𝑥,𝑦,𝑧,𝑥1*, . . .*) for strategy variables and variations of 𝜋 (𝜋, 𝜋′, 𝜋1*, . . .*) for path variables. Path and state formulas in HyperSL are generated by the following grammar:
𝜓 := 𝑎𝜋 | 𝜑𝜋 | 𝜓 ∧𝜓 | ¬𝜓 | X𝜓 | 𝜓 U𝜓
𝜑 := ∀𝑥.𝜑 | ∃𝑥.𝜑 | 𝜓
�
𝜋1 : �𝑥1, . . . , 𝜋𝑚 : �𝑥𝑚
�
where 𝑎 ∈ AP is an atomic proposition, 𝜋, 𝜋1*, . . . , 𝜋*𝑚 ∈ V are path variables, 𝑥 ∈ X is a strategy variable, and �𝑥1, . . . , �𝑥𝑚 : *Agts* → X
are *strategy profiles* that assign a strategy variable to each agent.

We often write𝜓 [𝜋𝑘 : �𝑥𝑘]𝑚
𝑘=1 as a shorthand for𝜓 [𝜋1 : �𝑥1*, . . . , 𝜋*𝑚 :
�𝑥𝑚]. We use Q as a placeholder for either ∀ or ∃. We use the standard Boolean connectives ∨, →, ↔, and constants ⊤, ⊥, as well as the derived LTL operators *eventually* F𝜓 := ⊤ U𝜓 and globally G𝜓 := ¬ F ¬𝜓. For each formula 𝜓 [𝜋𝑘 : �𝑥𝑘]𝑚
𝑘=1, we assume that all path variables that are free in 𝜓 belong to {𝜋1*, . . . , 𝜋*𝑚}, i.e., all used path variables are bound to some strategy profile. We further assume that all nested state formulas are closed.

Note that our syntax does not support boolean combinations of state formulas as is usual in SL [45]. As we can evaluate a path formula on multiple paths, we can move boolean combinations within the path formulas.

  Example 1. Consider the SL formula ∃𝑥. (∃𝑦.(F𝑎)(𝑥,𝑦)) ∧ (∀𝑧.
(G𝑏)(𝑧,𝑥)), which can be expressed in HyperSL as follows: ∃𝑥. ∃𝑦. ∀𝑦.
(F𝑎𝜋1 ∧ G𝑏𝜋2)[𝜋1 : (𝑥,𝑦), 𝜋2 : (𝑧,𝑥)].
                                                        △

Semantics. We fix a game structure G = (𝑆,𝑠0, A,𝜅, 𝐿). A strategy
assignment is a partial mapping Δ : X ⇀ Str(G). We write {} for
the unique strategy assignment with an empty domain. In HyperSL,
a path formula 𝜓 refers to propositions on multiple path variables.
We evaluate it in the context of a path assignment Π : V ⇀ 𝑆𝜔 map-
ping path variables to paths (similar to the semantics of HyperCTL∗

[26]). Given 𝑗 ∈ N, we define Π[𝑗, ∞] as the shifted assignment
defined by Π[𝑗, ∞](𝜋) := Π(𝜋)[𝑗, ∞]. For a path formula 𝜓, we
then define the semantics in the context of path assignment Π:

Π |=G 𝑎𝜋
           iff
              𝑎 ∈ 𝐿�Π(𝜋)(0)�

Π |=G 𝜑𝜋
           iff
              Π(𝜋)(0), {} |=G 𝜑

Π |=G 𝜓1 ∧𝜓2
           iff
              Π |=G 𝜓1 and Π |=G 𝜓2
Π |=G ¬𝜓
           iff
              Π ̸|=G 𝜓

Π |=G X𝜓
           iff
              Π[1, ∞] |=G 𝜓

$$\Pi\models_{\mathcal{G}}\psi_{1}\cup\psi_{2}\qquad\text{iff}\quad\exists j\in\mathbb{N}.\Pi[j,\infty]\models_{\mathcal{G}}\psi_{2}\text{and}$$ $$\forall0\leq k<j.\Pi[k,\infty]\models_{\mathcal{G}}\psi_{1}$$

The semantics for path formulas synchronously steps through all paths in $\Pi$ and evaluate $a_{\pi}$ on the path bound to $\pi$. State formulas are evaluated in a state $s\in S$ and strategy assignment $\Delta$ as follows:

$$s,\Lambda\models_{\mathcal{G}}\forall x.\varphi\qquad\qquad\text{iff}\quad\forall f\in Str(\mathcal{G}).\,s,\Delta[x\mapsto f]\models_{\mathcal{G}}\varphi$$ $$s,\Lambda\models_{\mathcal{G}}\exists x.\varphi\qquad\qquad\text{iff}\quad\exists f\in Str(\mathcal{G}).\,s,\Delta[x\mapsto f]\models_{\mathcal{G}}\varphi$$ $$s,\Lambda\models_{\mathcal{G}}\psi\left[\pi_{k}:\vec{x}_{k}\right]_{k=1}^{m}\quad\text{iff}$$ $$\left[\pi_{k}\mapsto Play_{\mathcal{G}}\left(s,\prod_{i\in Agts}\Lambda(\vec{x}_{k}(i))\right)\right]_{k=1}^{m}\models_{\mathcal{G}}\psi$$

To resolve a formula $\psi\left[\pi_{k}:\vec{x}_{k}\right]_{k=1}^{m}$, we construct $m$ paths (bound to $\pi_{1},\ldots,\pi_{m}$), and evaluate $\psi$ in the resulting path assignment. The 
𝑘th path (bound to 𝜋𝑘) is the play where each agent 𝑖 plays strategy
Δ(�𝑥𝑘 (𝑖)), i.e., the strategy currently bound to the strategy variable
�𝑥𝑘 (𝑖). We write G |= 𝜑 if 𝑠0, {} |=G 𝜑, i.e., the initial state satisfies state formula 𝜑.

## 5 Expressiveness Of Hypersl

The ability to compare multiple paths within a temporal formula makes HyperSL a powerful formalism that subsumes many existing logics. We only briefly mention some connections to existing logics. More details can be found in Appendix B.

## 5.1 Sl And Hypersl

HyperSL naturally subsumes many (non-hyper) strategy logics
[24, 45], which evaluate temporal properties on *individual* paths.

We consider SL formulas defined by the following grammar:

$$\psi:=a\mid\varphi\mid\neg\psi\mid\psi\wedge\psi\mid\mathsf{X}\psi\mid\psi\cup\psi$$ $$\varphi:=\psi\mid\varphi\wedge\varphi\mid\varphi\vee\varphi\mid\forall x.\,\varphi\mid\exists x.\,\varphi\mid(i,x)\varphi$$

where $a\in AP$, $x\in\mathcal{X}$, and $i\in\mathit{Agts}$. We assume that nested state formulas are closed. In this SL, we can quantify over strategies and $bind$ a strategy $x$ to agent $i$ using $(i,x)$; see Appendix B.1 for the full semantics. We can show the following:
Lemma 1. For any SL formula 𝜑 there exists a HyperSL formula
𝜑′ *such that for any CGS* G, G |=SL 𝜑 *iff* G |= 𝜑′.

Proof Sketch. We use a unique path variable �𝜋. During translation, we track the current strategy (variable) for each agent and construct �𝜋 using the resulting strategy profile.

□

  Example 2. Consider the formula ∃𝑥. ∀𝑦. (1,𝑥)(2,𝑦)(3,𝑦) G F𝑎.
We can express this formula in HyperSL as ∃𝑥. ∃𝑦. � G F𝑎 �𝜋
                                                    �[ �𝜋 :
(𝑥,𝑦,𝑦)] where (𝑥,𝑦,𝑦) denotes the strategy profile mapping agent 1
to 𝑥, and agents 2 and 3 to 𝑦.
                                                       △

## 5.2 Hyperatl∗ And Hypersl

Compared to SL, ATL∗ [2] offers a weaker (implicit) form of strategic reasoning. The ATL∗ formula ⎷𝐴⌄𝜓 expresses that the agents in𝐴 ⊆
Agts have a joint strategy to ensure path formula𝜓 [2]. HyperATL∗
[14, 17] is an extension of ATL∗ that can express hyperproperties, generated by the following grammar:

$$\psi:=a_{\pi}\mid\neg\psi\mid\psi\wedge\psi\mid\mathsf{X}\,\psi\mid\psi\U\psi$$ $$\varphi:=\langle\!\langle A\rangle\!\rangle\pi.\,\varphi\mid[\![A]\!]\pi.\,\varphi\mid\psi$$

where $a\in AP$, $\pi\in\mathcal{V}$, and $A\subseteq\mathit{Agts}$. Formula $\langle\!\langle A\rangle\!\rangle\pi.\,\varphi$ states that the agents in $A$ have a strategy such that any path under that strategy, when bound to path variable $\pi$, satisfies the remaining formula $\varphi$. Likewise, $[\![A]\!]\pi.\,\varphi$ states that, no matter what strategy the agents in $A$ play, some compatible path, when bound to $\pi$, satisfies $\varphi$. See Appendix B.2 for the full HyperAIL${}^{*}$ semantics. We can show the following:
Lemma 2. For any HyperATL∗ formula 𝜑 there exists a HyperSL
formula 𝜑′ *such that for any CGS* G, G |=HyperATL∗ 𝜑 *iff* G |= 𝜑′.

Proof Sketch. Similar to the translation of ATL∗ to SL [24, 45], we translate each HyperATL∗ quantifier ⎷𝐴⌄𝜋 (resp. �𝐴�𝜋) using existential (resp. universal) quantification over fresh strategies for all agents in 𝐴, followed by universal (resp. existential) quantification over strategies for agents in *Agts* \ 𝐴 and use these strategies to construct path 𝜋.

□
Example 3. Consider the HyperATL∗ *formula* ⎷{1, 2}⌄𝜋1. ⎷{3}⌄
𝜋2. (𝑎𝜋1 U𝑏𝜋2). We can express this in HyperSL as ∃𝑥1,𝑥2. ∀𝑥3. ∃𝑦3.

∀𝑦1,𝑦2. (𝑎𝜋1 U𝑏𝜋2)
�
𝜋1 : (𝑥1,𝑥2,𝑥3), 𝜋2 : (𝑦1,𝑦2,𝑦3)
�
.

△
By Lemma 2, HyperSL thus captures the various security hyperproperties (such as non-deducibility of strategies [54] and simulation security [51]) that can be expressed in HyperATL∗ [14]. We can extend Lemma 2 further to also capture the strategy sharing constraints found in HyperATL∗
𝑆 [18].

  Lemma 3. For any HyperATL∗
                          𝑆 formula 𝜑 there exists a HyperSL
formula 𝜑′ such that for any CGS G, G |=HyperATL∗
                                         𝑆 𝜑 iff G |= 𝜑′.

  Moreover, HyperSL can express properties that go well beyond
the strict ∃∀ and ∀∃ quantifier alternation found in HyperATL∗ and
HyperATL∗
         𝑆 (as, e.g., needed for Nash equilibria).

## 5.3 Imperfect Information And Hypersl

In recent years, much effort has been made to study strategic behavior under *imperfect information* [9–12, 29, 36]. In such a setting, an agent acts strategically (i.e., decides on an action based on its past experience) but only observes parts of the overall system. Perhaps surprisingly, HyperSL is expressive enough to allow reasoning under imperfect information despite having a semantics with complete information (cf. Section 4). Concretely, we consider strategy logic under imperfect information (SLii), an extension of SL with imperfect information [12, 13] defined as follows:
𝜓 := 𝑎 | 𝜑 | ¬𝜓 | 𝜓 ∧𝜓 | X𝜓 | 𝜓 U𝜓
𝜑 := 𝜓 | 𝜑 ∧ 𝜑 | 𝜑 ∨ 𝜑 | ∀𝑥𝑜.𝜑 | ∃𝑥𝑜.𝜑 | (𝑖,𝑥)𝜑
where 𝑎 ∈ AP, 𝑥 ∈ X, 𝑖 ∈ *Agts*, and 𝑜 ∈ *Obs* is an observation that gets attached to each strategy. SLii is evaluated on CGSs under partial observation, which are pairs (G, {∼𝑜}𝑜∈Obs) consisting of a CGS G = (𝑆,𝑠0, A*,𝜅, 𝐿*) and an observation relation ∼𝑜⊆ 𝑆 × 𝑆 for each observation 𝑜 ∈ *Obs*. If 𝑠 ∼𝑜 𝑠′, then 𝑠 and 𝑠′ appear indistinguishable for a strategy with observation 𝑜. See Appendix B.3 for the full semantics.

We can effectively encode each MC instance of SLii into an equisatisfiable HyperSL instance (Note that the MAS models of SLii and HyperSL are different, so we cannot translate the formula directly but translate both the formula and the model).

Theorem 1. For any SLii MC instance �(G, {∼𝑜}𝑜∈Obs),𝜑�, we can effectively compute a HyperSL MC instance �G′,𝜑′�, such that
(G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 iff G′ |= 𝜑′.

Proof Sketch. The key observation is that a strategy acting under imperfect information is a hyperproperty [19, 21]: A strategy 𝑓 acts under observation 𝑜 ∈ *Obs* iff on any two finite paths under 𝑓 the action chosen by 𝑓 is the same, provided the two paths are indistinguishable w.r.t. ∼𝑜. We can extend the CGS G so that the above is easily expressible in HyperSL. We can then restrict quantification to strategies under an arbitrary observation and use a similar translation to the one used in Lemma 1.

□
As model checking of SLii is undecidable [12], we get:
Corollary 1. Model checking of HyperSL is undecidable.

## 6 Model Checking Of Hypersl

While HyperSL MC is undecidable in general (cf. Corollary 1), we can identify fragments for which MC is possible. For this, we cannot follow the approach of existing MC algorithms for (variants of) nonhyper SL, which use tree automata to summarize strategies [24, 45].

For example, given an atomic state formula 𝜓 [𝜋𝑘 : �𝑥𝑘]𝑚
𝑘=1, we cannot construct a tree automaton that accepts all strategies that fulfill𝜓. This automaton would need to *compare* (and thus traverse)
multiple paths in a tree at the same time. Instead - given the "hyper" origins of our logic - we approach the MC problem by focusing on the interactions of its path variables and use *word* automata to summarize satisfying path assignments.

Throughout this section, we assume that all strategy variables are 𝛼-renamed such that no variable is quantified more than once.

## 6.1 Hypersl[Spe]

We call the fragment of HyperSL we study in this section HyperSL[SPE] - short for HyperSL with Single Path Elimination.

Definition 1.: _A HyperSL[SPE] formula has the form_

$$\varphi=\mathfrak{b}_{1}\ldots\mathfrak{b}_{m}.\,\psi\left[\pi_{k}:\vec{x}_{k}\right]_{k=1}^{m},$$

_where $\mathfrak{b}_{1},\ldots,\mathfrak{b}_{m}$ are blocks of strategy quantifiers and for each $1\leq k\leq m$ and $i\in\mathit{Agts}$, strategy variable $\vec{x}_{k}(i)$ is quantified in $\mathfrak{b}_{k}$. We refer to $m$ as the block-rank of $\varphi$._
Intuitively, the definition states that we can partition the quantifier prefix into smaller blocks where the variables quantified in each block ♭𝑘 can be used to eliminate (construct) the (unique) path variable 𝜋𝑘. We will exploit this restriction during model-checking:
we can eliminate each block of quantifiers incrementally: as all strategies quantified in block ♭𝑘 are only needed for path 𝜋𝑘, we can "construct" 𝜋𝑘, and afterward forget about the strategies we have used. Note that the definition of HyperSL[SPE] only depends on the quantifier prefix and the path each strategy variable is used on; it does not make any assumption on the structure of 𝜓.

**Example 4**.: _Consider the following (abstract) HyperSL formula, where $\psi$ is an arbitrary LTL formula over $\pi_{1}$, $\pi_{2}$._

$$\underbrace{\exists c\cdot\exists z.\forall w.\exists v.\psi}_{b_{1}}\left[\begin{array}{c}\pi_{1}:(c,c,c,c)\\ \pi_{2}:(w,z,v,v)\end{array}\right]$$

_This formula is a HyperSL[SPE] formula: The first block $b_{1}$ consists of strategy variable $c$ and constructs $\pi_{1}$, and the second block $b_{2}$ constructs $\pi_{2}$. The block-rank of this formula is 2._

## 6.2 Expressiveness Of Hypersl[Spe]

Before we outline our model-checking algorithm for HyperSL[SPE] formulas, we point to some (fragments of) other logics that fall within HyperSL[SPE].

HyperATL∗ *and HyperSL[SPE].* When translating HyperATL∗ (or HyperATL∗
𝑆) formulas into HyperSL (cf. Lemmas 2 and 3), each quantifier ⎷𝐴⌄𝜋 (resp. �𝐴�𝜋) is replaced by a ∃∗∀∗ (resp. ∀∗∃∗)
block of strategy quantifiers that are used to construct 𝜋 (and only
𝜋). The resulting formula is thus a HyperSL[SPE] formula.

SL[1G] and HyperSL[SPE]. SL[1G] is a fragment of SL that allows a prefix of strategy quantifier and agent bindings followed by a single path formula (with no nested agent binding) [23, 45–47].

When translating SL[1G] into HyperSL, we obtain a formula of the form Q1𝑥1 *. . .* Q𝑚𝑥𝑚.𝜓 [𝜋 : �𝑥] (cf. Lemma 1), which is trivially HyperSL[SPE] as there is a single path variable (with block-rank 1).

Beyond HyperATL∗
𝑆 *and SL[1G].* Additionally, HyperSL[SPE] captures interesting hyperproperties that could not be captured in existing logics:

**Example 5**.: _Assume a MAS with Apts $=\{r,a,\,ndet\}$ describing a planning task between a robot $r$ that wants to reach a state where AP goal $\in AP$ holds, and an adversary a that wants to prevent the robot from reaching the goal. In each step, agent $r$ can select a direction to move in, and a can choose a direction it wants to push the robot to. Each combination of actions of $r$ and a results in a set of potential successor locations, and the nondeterminism agent $ndet$ decides which of those locations the robot actually moves to. We want to check if agent $r$ has a winning strategy that can reach the goal against all possible behaviors of agent $a$, i.e., $r$ needs to reach the goal under favorable non-deterministic outcomes. We can express this (non-hyper) property in HyperSL[SPE] as_

$$\exists x.\,\forall y.\,\exists z.\,\big{(}\,\mathbb{F}\,\mathit{goal}_{\pi}\big{)}\big{[}\pi:(x,y,z)\big{]},$$

_where we write $(x,y,z)$ for the strategy profile that assigns agent $r$ to $x$, agent $a$ to $y$, and agent $ndet$ to $z$. In HyperSL[SPE], we can additionally state that $r$ should reach the goal as fast as possible, i.e., at least as fast as any path in the MAS:_
∃𝑥. ∀𝑦. ∃𝑧. ∀𝑎. ∀𝑏. ∀𝑐. (¬goal𝜋′) U goal𝜋

$$\left[\begin{array}{l}{\pi:(x,y,z)}\\ {\pi^{\prime}:(a,b,c)}\end{array}\right]$$

Here, we quantify over any potential different path 𝜋′ and state that
𝜋 is at least as fast as 𝜋′. Such requirements cannot be expressed in SL
(even in quantitative versions like SL[F ]), nor can they be expressed
in HyperATL∗ or HyperATL∗
                           𝑆.
                                                                   △

## 6.3 Summarizing Path Assignments

In the remainder of this section, we prove the following:
Theorem 2. Model checking for HyperSL[SPE] is decidable.

We fix a CGS G = (𝑆,𝑠0, A*,𝜅, 𝐿*) and state �𝑠 ∈ 𝑆, and let 𝜑 =
♭1 . . . ♭𝑚.𝜓
�
𝜋𝑘 : �𝑥𝑘
�𝑚
𝑘=1 be a HyperSL[SPE] formula. We want to check if �𝑠, {} |=G 𝜑, i.e., 𝜑 holds in state �𝑠.

Zipping Path Assignments. The main idea of our algorithm is to summarize path assignments that satisfy subformulas of 𝜑, similar to MC algorithms for HyperLTL, HyperCTL∗, and HyperATL∗
[16–18, 33]. To enable automata-based reasoning about path assignments, i.e., mappings Π : 𝑉 → 𝑆𝜔 for some 𝑉 ⊆ V, we *zip* such an assignment into an infinite word. Concretely, given Π : 𝑉 → 𝑆𝜔
we define *zip*(Π) ∈ (𝑉 → 𝑆)𝜔 as the infinite word of functions where *zip*(Π)(𝑗)(𝜋) := Π(𝜋)(𝑗) for every 𝑗 ∈ N, i.e., the function in the 𝑗th step maps each path variable 𝜋 ∈ 𝑉 to the 𝑗th state on the path bound to 𝜋.

## Algorithm 1 Simulation Construction For Block Elimination.

1 **def** simulate(G = (𝑆,𝑠0, A,𝜅, 𝐿),�𝑠,𝜋,�𝑥,♭ = Q1𝑥1 *. . .* Q𝑛𝑥𝑛,A):

2
Adet = (𝑄,𝑞0*,𝛿,𝑐*) = toDPA(A) // Using Proposition 1
3
B
= (𝑄 × 𝑆, (𝑞0, �𝑠),𝛿′,𝑐′� where
4
𝑐′(𝑞,𝑠) := 𝑐 (𝑞)
𝑖∈Agts
𝑎 �𝑥 (𝑖)
��
𝑎𝑥𝑛 ∈A

5
𝛿′�(𝑞,𝑠), �𝑡� :=
𝑎𝑥1 ∈A
· · ·
Q1∨∧
Q𝑛∨∧

�
𝛿 �𝑞, �𝑡 [𝜋 ↦→ 𝑠]�,𝜅
                    �
                     𝑠,
                         �

6
return B
Summary Automaton. Given a quantifier block ♭ = Q1𝑥1 . . . Q𝑛𝑥𝑛
over strategy variables 𝑥1*, . . . ,𝑥*𝑛, we define �♭ as the analogous block of quantification of strategies 𝑓𝑥1*, . . . , 𝑓*𝑥𝑛, i.e.,�♭ := Q1𝑓𝑥1 ∈
Str(G) . . . Q𝑛𝑓𝑥𝑛 ∈ *Str*(G). At the core of our model-checking algorithm, we construct automata that accept (zippings of) partial satisfying path assignments. Formally:

  Definition 2. For 1 ≤ 𝑘 ≤ 𝑚 + 1, we say an automaton A over
alphabet ({𝜋1, . . . , 𝜋𝑘−1} → 𝑆) is a (G, �𝑠,𝑘)-summary if for every
path assignment Π : {𝜋1, . . . , 𝜋𝑘−1} → 𝑆𝜔 we have zip(Π) ∈ L(A)
if and only if

𝑗=𝑘 |=G 𝜓.

𝑖∈Agts
          𝑓�𝑥𝑗 (𝑖))
                    �𝑚

�
♭𝑘 · · · �
   ♭𝑚. Π
       �
       𝜋𝑗 ↦→ PlayG(�𝑠,
                 �

  That is, a (G, �𝑠,𝑘)-summary accepts (the zipping of) a path as-
signment Π over paths 𝜋1, . . . , 𝜋𝑘−1 if - when simulating the quan-
tification over strategies needed to construct paths 𝜋𝑘, . . . , 𝜋𝑚 and
adding them to Π - the body 𝜓 of the formula is satisfied.

  Example 6. We illustrate the concept using the abstract formula
from Example 4. A (G, �𝑠, 3)-summary is an automaton A3 over alpha-
bet ({𝜋1, 𝜋2} → 𝑆) such that for every Π : {𝜋1, 𝜋2} → 𝑆𝜔 we have
zip(Π) ∈ L(A3) iff Π |=G 𝜓. A (G, �𝑠, 2)-summary is an automaton
A2 over alphabet ({𝜋1} → 𝑆) such that for every Π : {𝜋1} → 𝑆𝜔

we have zip(Π) ∈ L(A2) iff

∃𝑓𝑧. ∀𝑓𝑤. ∃𝑓𝑣. Π
           �
           𝜋2 ↦→ PlayG(�𝑠, (𝑓𝑤, 𝑓𝑧, 𝑓𝑣, 𝑓𝑣))
                                �
                                 |=G 𝜓,

i.e., we mimic the quantification of block ♭2 to construct path 𝜋2 (using
the quantified strategies 𝑓𝑧, 𝑓𝑤, 𝑓𝑣 ∈ Str(G)) and add this path to Π
(which already contains 𝜋1).
                                                                       △

## 6.4 Constructing (G, �𝑠,𝑘)-Summaries

We write ∨∧Q for a conjunction (�) if Q = ∀ and a disjunction
(�) if Q = ∃. The backbone of our model-checking algorithm
(which we present in Section 6.5) is an effective construction of a
(G, �𝑠,𝑘)-summary A𝑘 for each 1 ≤ 𝑘 ≤ 𝑚 + 1. To construct these summaries, we simulate quantification over strategies. We describe this simulation construction in Algorithm 1. Before explaining the construction, we state the result of Algorithm 1 as follows:

  Proposition 2. Given �𝑠 ∈ 𝑆, 𝜋 ∈ V, a strategy profile �𝑥 : Agts →
X, a quantifier block ♭ such that for every 𝑖 ∈ Agts, �𝑥(𝑖) is quantified
in ♭, and an APA A over alphabet (𝑉 ⊎ {𝜋} → 𝑆). Let B be the
results of simulate(G,�𝑠,𝜋,�𝑥,♭,A). Then for any path assignment
Π : 𝑉 → 𝑆𝜔, we have zip(Π) ∈ L(B) iff

𝑖∈Agts
𝑓�𝑥 (𝑖)
���
∈ L(A).
(1)
�♭. zip
�
Π
�
𝜋 ↦→ *Play*G
��𝑠,
�
That is, the automaton B accepts the zipping of an assignment
Π : 𝑉 → 𝑆𝜔 iff by simulating the quantifier prefix in ♭, we construct a path for 𝜋 that, when added to Π, is accepted by A. Note the similarity to Definition 2: In Definition 2 we simulate multiple quantifier blocks to construct paths 𝜋𝑘*, . . . , 𝜋*𝑚 that, when added to
Π, should satisfy the body 𝜓. In Proposition 2, we simulate a single path that, when added to Π, should be accepted by automaton A.

We will later use Proposition 2 to simulate one quantifier block at a time, eventually reaching an automaton required by Definition 2.

Before proving Proposition 2, let us explain the automaton construction in simulate (Algorithm 1). In Eq. (1), �♭ quantifies over strategies in G, which are infinite objects (function 𝑆+ → A). The crucial point that we will exploit is that the underlying game the strategies operate on is *positionally determined*. The automaton we construct can, therefore, *simulate* the path 𝜋 in G and select fresh actions in each step (instead of fixing strategies globally)
[14, 17, 18]. To do this, we first translate the APA A to a DPA
Adet = (𝑄,𝑞0*,𝛿,𝑐*) (in line 2). The new automaton B then simulates path 𝜋 by tracking its current state in G and simultaneously tracks the current state of Adet, thus operating on states in 𝑄 × 𝑆.

We start in state (𝑞0, �𝑠), i.e., the initial state of Adet and the designed state �𝑠 from which we want to start the simulation of 𝜋.

The color of each state is simply the color of the automaton we are tracking, i.e., 𝑐′(𝑞,𝑠) = 𝑐(𝑞) (line 4). During each transition, we then update the current state of Adet and the state of the simulation
(defined in line 5). Concretely, when in state (𝑞,𝑠), we read a letter
�𝑡 : 𝑉 → 𝑆 that assigns states to all path variables in 𝑉 (recall that the alphabet of A is 𝑉 ∪ {𝜋} → 𝑆 and the alphabet of B is 𝑉 → 𝑆).

We update the state of Adet to 𝛿(𝑞, �𝑡 [𝜋 ↦→ 𝑠]), i.e., we extend the input letter �𝑡 with the current state 𝑠 of the simulation of path 𝜋
(note that �𝑡 [𝜋 ↦→ 𝑠] : 𝑉 ∪ {𝜋} → 𝑆). To update the simulation state 𝑠, we make use of the positional determinacy of the game: Instead of quantifying over strategies (as in Eq. (1)), we can quantify over actions in each step of the automaton. Concretely, for each universally quantified strategy variable in ♭, we pick an action conjunctively, and for each existentially quantified variable, we pick an action disjunctively. After we have picked actions 𝑎𝑥1, . . . ,𝑎𝑥𝑛
for all strategies quantified in ♭, we can update the state of the
𝜋-simulation by constructing the action assignment �
𝑖∈*Agts* 𝑎 �𝑥 (𝑖), i.e., assign each agent the corresponding action, and obtain the next state using G's transition function 𝜅.

  Example 7. Let us use Example 4 to illustrate the construction
in Algorithm 1. Assume we are given an (G, �𝑠, 3)-summary A3 over
alphabet ({𝜋1, 𝜋2} → 𝑆), i.e., for every Π : {𝜋1, 𝜋2} → 𝑆𝜔, we
have zip(Π) ∈ L(A3) iff Π |=G 𝜓 (cf. Example 6). We invoke
simulate(G,�𝑠,𝜋2,�𝑥,♭2,A3) where �𝑥 = (𝑤,𝑧, 𝑣, 𝑣) and ♭2 = ∃𝑧∀𝑤∃𝑣,
and let (𝑄,𝑞0,𝛿,𝑐) be the DPA equivalent to A3 (computed in line 2).
In this case, simulate computes the APA B = (𝑄 × 𝑆, (𝑞0, �𝑠),𝛿′,𝑐′)
over alphabet {𝜋1} → 𝑆 where 𝛿′�(𝑞,𝑠), �𝑡� is defined as
    �

�

�

𝑎𝑧 ∈A

𝑎𝑤 ∈A

𝑎𝑣 ∈A

�
𝛿(𝑞, �𝑡 [𝜋2 ↦→ 𝑠]),𝜅�𝑠, (𝑎𝑤,𝑎𝑧,𝑎𝑣,𝑎𝑣)��
                                           .

That is, in each step, we disjunctively choose an action 𝑎𝑧 (corre-
sponding to the action selected by existentially quantified strategy 𝑧),
conjunctively pick an action 𝑎𝑤 (corresponding to the action selected
by universally quantified strategy 𝑤), and finally disjunctively select

## Algorithm 2 Model-Checking Algorithm For Hypersl[Spe].

2
// Assume 𝜓 contains no nested state formulas

1 def modelCheck(G,�𝑠,𝜑 = ♭1 · · · ♭𝑚.𝜓
                                              �
                                               𝜋𝑘 : �𝑥𝑘
                                                       �𝑚
                                                        𝑘=1):

3
A𝑚+1 = LTLtoAPA(𝜓)
4
// A𝑚+1 is a (G, �𝑠,𝑚 + 1)-summary
5
for 𝑘 **from** 𝑚 to 1:
6
A𝑘 = simulate(G,�𝑠,𝜋𝑘,�𝑥𝑘,♭𝑘,A𝑘+1)
7
// A𝑘 is a (G, �𝑠,𝑘)-summary
8
if L(A1) ≠ ∅ then
9
return SAT // �𝑠, {} |=G 𝜑
10
else
11
return UNSAT
// �𝑠, {} ̸|=G 𝜑
action 𝑎𝑣. After we have fixed actions 𝑎𝑧, 𝑎𝑤 and 𝑎𝑣, we take a step in G by letting each agent 𝑖 play action 𝑎 �𝑥 (𝑖), i.e., agent 1 chooses action
𝑎𝑤, agent 2 chooses 𝑎𝑧, and agents 3 and 4 pick 𝑎𝑣. By Proposition 2, every Π : {𝜋1} → 𝑆𝜔 *satisfies zip*(Π) ∈ L(B) iff
∃𝑓𝑧. ∀𝑓𝑤. ∃𝑓𝑣. zip�Π[𝜋2 ↦→ PlayG(�𝑠, (𝑓𝑤, 𝑓𝑧, 𝑓𝑣, 𝑓𝑣))]� ∈ L(A3)
which (by assumption on A3) holds iff
∃𝑓𝑧. ∀𝑓𝑤. ∃𝑓𝑣. Π[𝜋2 ↦→ PlayG(�𝑠, (𝑓𝑤, 𝑓𝑧, 𝑓𝑣, 𝑓𝑣))] |=G 𝜓.

We have thus used simulate (Algorithm 1) to compute a (G, �𝑠, 2)- summary from a (G, �𝑠, 3)-summary (cf. Example 6).

△
We can now formally prove Proposition 2:
Proof Sketch of Proposition 2. The idea of automaton B constructed in Algorithm 1 is to simulate the path that corresponds to path variable 𝜋. To argue that B expresses the desired language, we make use of the positional determinacy of concurrent parity games
(CPG) [40]. A CPG is a simple multi-player game model where we can quantify over strategies for each of the players. For any fixed Π, we design an (infinite-state) CPG, that is won iff Eq. (1) holds. We then exploit the fact that CPGs are determined (cf. [40, Thm. 4.1]), i.e., instead of quantifying over entire strategies in the CPG, we can quantify over Skolem functions for actions in each step. This allows us to show that the CPG is won iff B has an accepting run (on the fixed Π), giving us the desired result. We refer the interested reader to Appendix D for details.

□

## 6.5 Model-Checking Algorithm

Equipped with the concept of (G, �𝑠,𝑘)-summary and the simulation construction, we can now present our MC algorithm for HyperSL[SPE] in Algorithm 2. The modelCheck procedure is given a CGS G, a state �𝑠, and a HyperSL[SPE] formula 𝜑, and checks if
�𝑠, {} |=G 𝜑. Our algorithm assumes, w.l.o.g., that the path formula
𝜓 contains no nested state formulas. In case there are nested state formulas, we can eliminate them iteratively: We recursively check each nested state formula on all states of the CGS, and label all states where the state formula holds with a fresh atomic proposition. In the path formula, we can then replace each state formula with a reference to the fresh atomic proposition. See, e.g., [18, 31]
for details.

The main idea of our MC algorithm is to iteratively construct a (G, �𝑠,𝑘)-summary A𝑘 for each 1 ≤ 𝑘 ≤ 𝑚 + 1. Initially, in line
4, we construct a (G, �𝑠,𝑚 + 1)-summary A𝑚+1 using a standard

𝒏
|𝑺|
|𝑺*reach* |
𝒕MCMAS-SL[1G]
𝒕HyMASMC
2
72
9
0.1
0.4
3
432
21
6.71
1.9
4
2592
49
313.7
24.5
5
15552
113
TO
332.1

construction to translate the LTL formula𝜓 to an APA over alphabet
({𝜋1*, . . . , 𝜋*𝑚} → 𝑆), as is, e.g., standard for HyperCTL∗ [33]. For each 𝑘 from 𝑚 to 1, we then use the (G, �𝑠,𝑘 + 1)-summary A𝑘+1 to compute a (G, �𝑠,𝑘)-summary A𝑘 using the simulate construction from Algorithm 1 (similar to what we illustrated in Example 7). From Proposition 2, we can conclude the following invariant:
Lemma 4. In line 7, A𝑘 is a (G, �𝑠,𝑘)-summary. After the loop, we are thus left with a (G, �𝑠, 1)-summary A1
(over the simpleton alphabet (∅ → 𝑆)) and can check if �𝑠, {} |=G 𝜑
by testing A1 for emptiness (line 8):
Lemma 5. For any (G, �𝑠, 1)-summary A*, we have that* L(A) ≠ ∅
if and only if �𝑠, {} |=G 𝜑.

From Lemmas 4 and 5, it follows that modelCheck(G,�𝑠,𝜑) returns SAT iff �𝑠, {} |=G 𝜑, proving Theorem 2.

## 6.6 Model-Checking Complexity

The determinization in line 2 of Algorithm 1 results in a DPA Adet of doubly exponential size (cf. Proposition 1). The size of B is then linear in the size of Adet and G. In the worst case, each call of simulate thus increases the size of the automaton by two exponents. For a HyperSL[SPE] formula with block-rank 𝑚, simulate is called 𝑚 times, so the final automaton A1 has, in the worst case, 2𝑚-exponential many states (in the size of 𝜓 and G). As we can check emptiness of APAs over the singleton alphabet (∅ → 𝑆) in polynomial time, we get:
Theorem 3. Model checking for a HyperSL[SPE] formula with block-rank 𝑚 *is in* 2𝑚-EXPTIME.

From Lemma 2 and the lower bounds known for HyperATL∗
[17], it follows that our algorithm is asymptotically almost optimal:
Lemma 6. Model checking for a HyperSL[SPE] formula with blockrank 𝑚 is (2𝑚 − 1)-EXPSPACE-hard.

## 6.7 Beyond Hypersl[Spe]

HyperSL[SPE] is defined purely in terms of the structure of the quantifier prefix. As soon as strategy variables are quantified in an order such that they cannot be grouped together, MC becomes, in general, undecidable: Already the simplest such property Q𝑥.Q𝑦.Q𝑧.Q𝑤.

𝜓 [𝜋1 : (𝑥,𝑧), 𝜋2 : (𝑦,𝑤)], leads to undecidable MC (see Appendix C.3). The fragment we have identified is thus the largest possible
(when only considering the quantifier prefix). Any further study into decidable fragments of HyperSL needs to impose restrictions

| Model                 | Sec   | GE   | Rnd   |
|-----------------------|-------|------|-------|
| 2                     |       |      |       |
| Rnd                   |       |      |       |
| 3                     |       |      |       |
| Rnd                   |       |      |       |
| 4                     |       |      |       |
| bit-transmission      | 0.6   | 0.7  | 0.8   |
| book-store            | 0.4   | 0.4  | 0.4   |
| card-game             | 0.4   | 0.5  | 0.4   |
| dining-cryptographers | 0.6   | 2.7  | 11.4  |
| muddy-children        | 0.4   | 3.0  | 1.7   |
| simple-card-game      | 0.3   | 3.4  | 2.9   |
| software-development  | -     | -    | -     |
| strongly-connected    | 0.6   | 0.8  | 0.8   |
| tianji-horse-racing   | 0.4   | 0.5  | 0.4   |

beyond the prefix and, e.g., analyze how different path variables are related within an LTL path formula (see also Section 8).

## 7 Implementation And Experiments

We have implemented our HyperSL[SPE] model-checking algorithm in the HyMASMC tool [18].

## 7.1 Model-Checking For Strategy Logic

We compare HyMASMC against MCMAS-SL[1G] [23] on (non-hyper)
SL[1G] properties (cf. Section 6.2). In Table 1, we depict the verification times for the scheduling problem from [23] (which can be expressed in SL[1G] and ATL∗). As in [18], we observe that HyMASMC
performs much faster than MCMAS-SL[1G], which we largely accredit to HyMASMC's efficient automata backend using spot [30]. Note that we use MCMAS-SL[1G] and HyMASMC directly on the original model, i.e., we did not perform any prepossessing using, e.g., abstraction techniques [5, 6, 8] (which would reduce the system size and make the verification more scaleable for both tools).

## 7.2 Model-Checking For Hyperproperties

In a second experiment, we demonstrate that HyMASMC can verify hyperproperties on various MASs from the literature. We use the ISPL models from the MCMAS benchmarks suit [39], and generate random HyperSL[SPE] formulas from various property templates:

- **(Sec):** We check if some agent 𝑖 can reach some target state
without leaking information about some secret AP via some
observable AP. Concretely, we check if 𝑖 can play such that on some other path, the same observation sequence is coupled with a different high-security input, a property commonly referred to
as *non-inference* [43] or *opacity* [52, 55].
- **(GE):** We check if a given SL[1G] formula holds on all input
sequences for which *some* winning output sequence exists, as is, e.g., required in *good-enough* synthesis [1, 3].
- **(Rnd):** We randomly generate HyperSL[SPE] formulas with blockrank 2, 3, and 4 (called Rnd2, **Rnd**3, and **Rnd**4, respectively).
We depict the results in Table 2, demonstrating that HyMASMC
can handle most instances. The only exception is the softwaredevelopment model, which includes ≈15k states and is therefore too large for an automata-based representation.

Size
40
50
60
70
80
90
100
110
120
t
14.2
22.0
31.2
42.5
57.6
70.1
86.8
104.6
TO

We stress that we do not claim that all formulas in each of the templates model realistic properties in each of the systems. Rather, our evaluation **(1)** demonstrates that HyperSL[SPE] can express interesting properties, and **(2)** empirically shows that HyMASMC can check such properties in existing ISPL models (confirming this via further real-world scenarios is interesting future work).

## 7.3 Model-Checking For Optimal Planning

In our last experiment, we challenge HyMASMC with planning examples as those outlined in Example 5. We randomly generate planning instances between the robot 𝑟, adversary 𝑎, and *ndet*, and check if robot 𝑟 *can* reach the goal following some shortest path in the problem. For a varying size 𝑛, we randomly create 10 planning instances with 𝑛 states. We report the verification times in Table 3.

With increasing size, the running time of HyMASMC clearly increases, but the increase seems to be quadratic rather than exponential.

## 8 Conclusion And Future Work

We have presented HyperSL, a new temporal logic that extends strategy logic with the ability to reason about hyperproperties. HyperSL can express complex properties in MASs that require a combination of strategic reasoning and hyper-requirements (such as optimalilty, GE, non-interference, and quantitative Nash equilibria); many of which were out of reach of existing logics. As such, HyperSL can serve as a unifying foundation for an exact exploration of the interaction of strategic behavior with hyperproperties, and provides a formal language to express (un)decidability results. Moreover, we have taken a first step towards the ambitious goal of automatically model-checking HyperSL. Our fragment HyperSL[SPE] subsumes many relevant other logics and captures unique properties not expressible in existing frameworks. Our implementation in HyMASMC
shows that our MC approach is practical in small MASs.

A particularly interesting future direction is to search for further fragments of HyperSL with decidable model checking. As argued in Section 6.7, any such fragment needs to take the structure of the LTL-formula(s) into account. For example, Mogavero et al. [46] showed that SL[CG] (a fragment of SL that only allows conjunctions of goal formulas) still admits behavioral strategies (i.e., strategies that do not depend on future or counterfactual decisions of other strategies). When extending this to our hyper setting, it seems likely that if a strategy is used on multiple path variables, but these paths occur in disjoint conjuncts of path formulas, MC remains decidable.

We leave such extensions as future work.

## Acknowledgments

This work was supported by the European Research Council (ERC)
Grant HYPER (101055412), and by the German Research Foundation
(DFG) as part of TRR 248 (389792660).

## References

[1] Shaull Almagor and Orna Kupferman. 2020. Good-Enough Synthesis. In International Conference on Computer Aided Verification, CAV 2020.
[2] Rajeev Alur, Thomas A. Henzinger, and Orna Kupferman. 2002. Alternating-time
temporal logic. *J. ACM* (2002).
[3] Benjamin Aminof, Giuseppe De Giacomo, and Sasha Rubin. 2021. Best-Effort
Synthesis: Doing Your Best Is Not Harder Than Giving Up. In International Joint Conference on Artificial Intelligence, IJCAI 2021.
[4] Benjamin Aminof, Marta Kwiatkowska, Bastien Maubert, Aniello Murano, and
Sasha Rubin. 2019. Probabilistic Strategy Logic. In International Joint Conference on Artificial Intelligence, IJCAI 2019.
[5] Thomas Ball and Orna Kupferman. 2006. An Abstraction-Refinement Framework
for Multi-Agent Systems. In *Symposium on Logic in Computer Science LICS 2006*.
[6] Francesco Belardinelli, Angelo Ferrando, Wojciech Jamroga, Vadim Malvone, and
Aniello Murano. 2023. Scalable Verification of Strategy Logic through Three-
Valued Abstraction. In International Joint Conference on Artificial Intelligence,
IJCAI 2023.
[7] Francesco Belardinelli, Sophia Knight, Alessio Lomuscio, Bastien Maubert,
Aniello Murano, and Sasha Rubin. 2021. Reasoning About Agents That May
Know Other Agents' Strategies. In International Joint Conference on Artificial
Intelligence, IJCAI 2021.
[8] Francesco Belardinelli and Alessio Lomuscio. 2017. Agent-based Abstractions
for Verifying Alternating-time Temporal Logic with Imperfect Information. In
Conference on Autonomous Agents and MultiAgent Systems, AAMAS 2017.
[9] Francesco Belardinelli, Alessio Lomuscio, and Vadim Malvone. 2019.
An
Abstraction-Based Method for Verifying Strategic Properties in Multi-Agent
Systems with Imperfect Information. In Conference on Artificial Intelligence, AAAI 2019.
[10] Francesco Belardinelli, Alessio Lomuscio, Aniello Murano, and Sasha Rubin.
2017. Verification of Multi-agent Systems with Imperfect Information and Public
Actions. In Conference on Autonomous Agents and MultiAgent Systems, AAMAS
2017.
[11] Raphaël Berthon, Bastien Maubert, and Aniello Murano. 2017. Decidability
Results for ATL* with Imperfect Information and Perfect Recall. In Conference on Autonomous Agents and MultiAgent Systems, AAMAS 2017.
[12] Raphaël Berthon, Bastien Maubert, Aniello Murano, Sasha Rubin, and Moshe Y.
Vardi. 2017. Strategy logic with imperfect information. In Symposium on Logic in
Computer Science, LICS 2017.
[13] Raphaël Berthon, Bastien Maubert, Aniello Murano, Sasha Rubin, and Moshe Y.
Vardi. 2021. Strategy Logic with Imperfect Information. ACM Trans. Comput.
Log. (2021).
[14] Raven Beutner and Bernd Finkbeiner. 2021. A Temporal Logic for Strategic
Hyperproperties. In International Conference on Concurrency Theory, CONCUR 2021.
[15] Raven Beutner and Bernd Finkbeiner. 2022. Software Verification of Hyperproperties Beyond k-Safety. In International Conference on Computer Aided Verification, CAV 2022.
[16] Raven Beutner and Bernd Finkbeiner. 2023. AutoHyper: Explicit-State Model
Checking for HyperLTL. In International Conference on Tools and Algorithms for the Construction and Analysis of Systems, TACAS 2023.
[17] Raven Beutner and Bernd Finkbeiner. 2023. HyperATL*: A Logic for Hyperproperties in Multi-Agent Systems. *Log. Methods Comput. Sci.* (2023).
[18] Raven Beutner and Bernd Finkbeiner. 2024. On Alternating-Time Temporal Logic,
Hyperproperties, and Strategy Sharing. In Conference on Artificial Intelligence, AAAI 2024.
[19] Raven Beutner, Bernd Finkbeiner, Hadar Frenkel, and Niklas Metzger. 2023.
Second-Order Hyperproperties. In International Conference on Computer Aided Verification, CAV 2023.
[20] Patricia Bouyer, Orna Kupferman, Nicolas Markey, Bastien Maubert, Aniello
Murano, and Giuseppe Perelli. 2019. Reasoning about Quality and Fuzziness of
Strategic Behaviours. In International Joint Conference on Artificial Intelligence, IJCAI 2019.
[21] Laura Bozzelli, Bastien Maubert, and Sophie Pinchinat. 2015. Unifying Hyper
and Epistemic Temporal Logics. In International Conference on Foundations of Software Science and Computation Structures, FoSSaCS 2015.
[22] Nils Bulling and Wojciech Jamroga. 2014. Comparing variants of strategic ability:
how uncertainty and memory influence general properties of games. Auton. Agents Multi Agent Syst. (2014).
[23] Petr Cermák, Alessio Lomuscio, and Aniello Murano. 2015. Verifying and Synthesising Multi-Agent Systems against One-Goal Strategy Logic Specifications.
In *Conference on Artificial Intelligence, AAAI 2015*.
[24] Krishnendu Chatterjee, Thomas A. Henzinger, and Nir Piterman. 2010. Strategy
logic. *Inf. Comput.* (2010).
[25] Swarat Chaudhuri, Sumit Gulwani, and Roberto Lublinerman. 2012. Continuity
and robustness of programs. *Commun. ACM* (2012).
[26] Michael R. Clarkson, Bernd Finkbeiner, Masoud Koleini, Kristopher K. Micinski,
Markus N. Rabe, and César Sánchez. 2014. Temporal Logics for Hyperproperties.
In *International Conference on Principles of Security and Trust, POST 2014*.

[27] Michael R. Clarkson and Fred B. Schneider. 2008. Hyperproperties. In Computer
Security Foundations Symposium, CSF 2008.
[28] Norine Coenen, Bernd Finkbeiner, Christopher Hahn, and Jana Hofmann. 2019.
The Hierarchy of Hyperlogics. In Symposium on Logic in Computer Science, LICS
2019.
[29] Catalin Dima and Ferucio Laurentiu Tiplea. 2011. Model-checking ATL under
Imperfect Information and Perfect Recall Semantics is Undecidable. *CoRR* (2011).
[30] Alexandre Duret-Lutz, Etienne Renault, Maximilien Colange, Florian Renkin,
Alexandre Gbaguidi Aisse, Philipp Schlehuber-Caissier, Thomas Medioni, Antoine Martin, Jérôme Dubois, Clément Gillard, and Henrich Lauko. 2022. From
Spot 2.0 to Spot 2.10: What's New?. In International Conference on Computer Aided Verification, CAV 2022.
[31] E. Allen Emerson and Joseph Y. Halpern. 1986. "Sometimes" and "Not Never"
revisited: on branching versus linear time temporal logic. *J. ACM* (1986).
[32] Bernd Finkbeiner, Christopher Hahn, Philip Lukert, Marvin Stenger, and Leander Tentrup. 2018. Synthesizing Reactive Systems from Hyperproperties. In
International Conference on Computer Aided Verification, CAV 2018.
[33] Bernd Finkbeiner, Markus N. Rabe, and César Sánchez. 2015. Algorithms for
Model Checking HyperLTL and HyperCTL*. In International Conference on Computer Aided Verification, CAV 2015.
[34] Bernd Finkbeiner and Martin Zimmermann. 2017. The First-Order Logic of
Hyperproperties. In Symposium on Theoretical Aspects of Computer Science, STACS 2017.
[35] Jens Oliver Gutsfeld, Markus Müller-Olm, and Christoph Ohrem. 2020. Propositional Dynamic Logic for Hyperproperties. In International Conference on Concurrency Theory, CONCUR 2020.
[36] Sophia Knight and Bastien Maubert. 2019. Dealing with imperfect information
in Strategy Logic. *CoRR* (2019).
[37] François Laroussinie and Nicolas Markey. 2015. Augmenting ATL with strategy
contexts. *Inf. Comput.* (2015).
[38] François Laroussinie, Nicolas Markey, and Arnaud Sangnier. 2015. ATLsc with
partial observation. In International Symposium on Games, Automata, Logics and Formal Verification, GandALF 2015.
[39] Alessio Lomuscio, Hongyang Qu, and Franco Raimondi. 2009. MCMAS: A Model
Checker for the Verification of Multi-Agent Systems. In International Conference on Computer Aided Verification, CAV 2009.
[40] Vadim Malvone, Aniello Murano, and Loredana Sorrentino. 2016. Concurrent
Multi-Player Parity Games. In International Conference on Autonomous Agents & Multiagent Systems, AAMAS 2016.
[41] Bastien Maubert and Aniello Murano. 2018. Reasoning about Knowledge and
Strategies under Hierarchical Information. In International Conference on Principles of Knowledge Representation and Reasoning, KR 2018.
[42] Daryl McCullough. 1988. Noninterference and the composability of security
properties. In *Symposium on Security and Privacy, SP 1988*.
[43] John McLean. 1994. A general theory of composition for trace sets closed under
selective interleaving functions. In Symposium on Research in Security and Privacy, SP 1994.
[44] Satoru Miyano and Takeshi Hayashi. 1984. Alternating Finite Automata on
omega-Words. *Theor. Comput. Sci.* (1984).
[45] Fabio Mogavero, Aniello Murano, Giuseppe Perelli, and Moshe Y. Vardi. 2014.
Reasoning About Strategies: On the Model-Checking Problem. ACM Trans. Comput. Log. (2014).
[46] Fabio Mogavero, Aniello Murano, and Luigi Sauro. 2013. On the Boundary of
Behavioral Strategies. In *Symposium on Logic in Computer Science, LICS 2013*.
[47] Fabio Mogavero, Aniello Murano, and Luigi Sauro. 2014. A Behavioral Hierarchy
of Strategy Logic. In International Workshop on Computational Logic in Multi-
Agent Systems, CLIMA 2014.
[48] John F Nash Jr. 1950. Equilibrium points in n-person games. Proceedings of the
national academy of sciences (1950).
[49] Marc Pauly and Rohit Parikh. 2003. Game Logic - An Overview. Stud Logica
(2003).
[50] Nir Piterman. 2007. From Nondeterministic Büchi and Streett Automata to
Deterministic Parity Automata. *Log. Methods Comput. Sci.* (2007).
[51] Andrei Sabelfeld. 2003. Confidentiality for Multithreaded Programs via Bisimulation. In International Conference on Perspectives of Systems Informatics, PSI 2003.
[52] Anooshiravan Saboori and Christoforos N. Hadjicostis. 2013. Verification of
initial-state opacity in security applications of discrete event systems. Inf. Sci.
(2013).
[53] Moshe Y. Vardi. 1995. Alternating Automata and Program Verification. In
Computer Science Today: Recent Trends and Developments.
[54] J. Todd Wittbold and Dale M. Johnson. 1990. Information Flow in Nondeterministic Systems. In *Symposium on Security and Privacy, SP 1990*.
[55] Kuize Zhang, Xiang Yin, and Majid Zamani. 2019. Opacity of Nondeterministic
Transition Systems: A (Bi)Simulation Relation Approach. IEEE Trans. Autom.
Control. (2019).

## A Additional Material For Section 3

In this section we give details on the semantics of APAs. To make our later proofs (which use the APA semantics) easier, we use a DAG-based semantics (opposed to the more prominently used - but equivalent - tree-based semantics). We refer the reader to [53] for more details.

Definition 3. For a set𝑄, we write B+(𝑄) for the set of all positive boolean formulas over 𝑄, i.e., all formulas generated by the grammar

$$\theta:=q\mid\theta_{1}\wedge\theta_{2}\mid\theta_{1}\vee\theta_{2}$$

_where $q\in Q$. Given a subset $X\subseteq Q$ and $\theta\in\mathbb{B}^{+}(Q)$, we write $X\models\theta$ if the assignment that maps all states in $X$ to $\top$ and those in $Q\setminus X$ to $\bot$ satisfies $\Psi$. For example $\{q_{0},q_{1}\}\models q_{0}\wedge(q_{1}\vee q_{2})$._
Let A = (𝑄,𝑞0*,𝛿,𝑐*) be an APA. A run DAG of A is a pair D = (*𝑉, 𝐸*) of nodes and edges such that𝑉 ⊆ 𝑄 ×N, 𝐸 ⊆ �
𝑖∈N(𝑄 ×
{𝑖})×(𝑄 ×{𝑖+1}). That is, each node in𝑉 consist of a state in 𝑄 and a depth and the edges in 𝐸 only reach from depth 𝑖 to depth 𝑖 +1. For every (𝑞,𝑖) ∈ 𝑉 , we define sucs(𝑞,𝑖) := {𝑞′ | ((𝑞,𝑖), (𝑞′,𝑖 + 1)) ∈ 𝐸}
as the state component of (𝑞,𝑖)'s successor nodes.

A run of A on a word 𝑢 ∈ Σ𝜔 is a run DAG D = (*𝑉, 𝐸*) such that
(𝑞0, 0) ∈ 𝑉 and for every (𝑞,𝑖) ∈ 𝑉 , sucs(𝑞,𝑖) |= 𝛿(𝑞,𝑢(𝑖)). That is, the run DAG starts in the initial state 𝑞0 at depth 0, and for each node in the DAG the successors of each node satisfy the transition formula given by the transition function 𝛿.

For example, consider a node (𝑞,𝑖) and assume that 𝛿(𝑞,𝑢(𝑖)) =
𝑞1 ∨ 𝑞2. Then the DAG must include either 𝑞1 or 𝑞2 (or both) as successors in the next level. In particular, if the transition function 𝛿 uses only disjunctions (no conjunctions) the automataon is non-deterministic. In this case, each node in the DAG can have a unique successor; the DAG is a line (a infinite sequence of states).

Conversely, if 𝛿(𝑞,𝑢(𝑖)) = 𝑞1 ∧ 𝑞2 then both 𝑞1 and 𝑞2 need to appear in the next level, i.e., we need to construct accepting runs from both of these states.

A run DAG D is accepting if for every infinite path in the DAG
the minimal color that occurs infinitely many times (as given by 𝑐)
is even. We define L(A) ⊆ Σ𝜔 as all infinite words on which A
has an accepting run DAG.

## B Additional Material For Section 5

We provide some background on the temporal logics HyperLTL, SL, HyperATL∗, and HyperATL∗
𝑆 and give their full semantics.

## B.1 Sl And Hypersl

In this subsection, we provide addition details on the relation of SL and HyperSL (cf. Section 5.1). We consider a variant of SL that allows multiple agents to share the strategy by using explicit agent binding, but disallows agent bindings under temporal operators.

Remark 1. The strategy logic by Mogavero et al. [45] allows arbitrary nesting of agent binding within temporal operators. Our variant is equivalent to SL[BG] [45] - a fragment that follows a strict separation between state and path formulas and thereby forbids agent binding under temporal operators. Note that SL[BG] strictly subsumes the strategy logic by Chatterjee et al. [24]. We choose to restrict to the SL[BG] fragment as it is syntactically closer to temporal logics like CTL∗ and HyperCTL∗ and, thereby, also to HyperSL.

State and path formulas in SL are defined as follows:
𝜓 := 𝑎 | 𝜑 | ¬𝜓 | 𝜓 ∧𝜓 | X𝜓 | 𝜓 U𝜓
𝜑 := 𝜓 | 𝜑 ∧ 𝜑 | 𝜑 ∨ 𝜑 | ∀𝑥.𝜑 | ∃𝑥.𝜑 | (𝑖,𝑥)𝜑
where 𝑎 ∈ AP, 𝑥 ∈ X, and 𝑖 ∈ *Agts*. Importantly, we assume that every state formula occurring in a path formula is closed.

The idea of SL is to separate the quantification of a strategy and the binding of a strategy to some agent. To accomplish the latter, it features an explicit agent-binding construct (𝑖,𝑥)𝜑 which evaluates
𝜑 after binding agent 𝑖 to strategy 𝑥.

Semantics. Assume G = (𝑆,𝑠0, A*,𝜅, 𝐿*) is a fixed CGS. Given a path 𝑝 ∈ 𝑆𝜔 we define the semantics of path formulas as expected:

𝑝 |=G 𝑎
iff
𝑎 ∈ 𝐿(𝑝(0))
𝑝 |=G 𝜑
iff
𝑝(0), {}, {} |=G 𝜑
𝑝 |=G 𝜓1 ∧𝜓2
iff
𝑝 |=G 𝜓1 and 𝑝 |=G 𝜓2
𝑝 |=G ¬𝜓
iff
𝑝 ̸|=G 𝜓
𝑝 |=G X𝜓
iff
𝑝[1, ∞] |=G 𝜓
𝑝 |=G 𝜓1 U𝜓2
iff
∃𝑗 ∈ N. 𝑝[𝑗, ∞] |=G 𝜓2 and

∀0 ≤ 𝑘 < *𝑗. 𝑝*[𝑘, ∞] |=G 𝜓1
In the semantics of state formulas, we keep track of a strategy for each strategy variable via a (partial) strategy assignment Δ : X ⇀
Str(G), similar to the HyperSL semantics. As SL works with explicit agent bindings, we also keep track of a strategy for each agent using a (partial) function Θ : Agts ⇀ *Str*(G). We can then define:
𝑠, Δ, Θ |=G ∀𝑥.𝜑
iff
∀𝑓 ∈ *Str*(G).𝑠, Δ[𝑥 ↦→ 𝑓 ], Θ |=G 𝜑

| 𝑠,   |  Δ   | ,   |  Θ   |
|------|------|-----|------|
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| ∃    |      |     |      |
| 𝑥.𝜑  |      |     |      |
| iff  |      |     |      |
| ∃    |      |     |      |
| 𝑓    |      |     |      |
| ∈    |      |     |      |
| Str  |      |     |      |
| (G)  |      |     |      |
| .𝑠,  | Δ    |     |      |
| [    |      |     |      |
| 𝑥    |      |     |      |
| ↦→   |      |     |      |
| 𝑓    |      |     |      |
| ]    |      |     |      |
| ,    | Θ    |     |      |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| (    |      |     |      |
| 𝑖    | ,𝑥   |     |      |
| )    |      |     |      |
| 𝜑    |      |     |      |
| iff  |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| [    |      |     |      |
| 𝑖    |      |     |      |
| ↦→   |      |     |      |
| Δ    |      |     |      |
| (    |      |     |      |
| 𝑥    |      |     |      |
| )] | |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 1    |      |     |      |
| ∧    |      |     |      |
| 𝜑    |      |     |      |
| 2    |      |     |      |
| iff  |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 1    |      |     |      |
| and  |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 2    |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 1    |      |     |      |
| ∨    |      |     |      |
| 𝜑    |      |     |      |
| 2    |      |     |      |
| iff  |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 1    |      |     |      |
| or   |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜑    |      |     |      |
| 2    |      |     |      |
| 𝑠,   | Δ    | ,   | Θ    |
| |    |      |     |      |
| =    |      |     |      |
| G    |      |     |      |
| 𝜓    |      |     |      |
| iff  |      |     |      |
| Play |      |     |      |
| G    |      |     |      |
| �    |      |     |      |
| 𝑠,   |      |     |      |
| �    |      |     |      |

$\theta$$\varphi_{1}$ or $s,\Delta,\theta$$\varphi_{\theta}$$\prod_{i\in Agts}\Theta(i)$$\varphi_{\theta}$$\psi$

Strategy quantification updates the binding in $\Delta$ (as in HyperSL), whereas strategy binding updates the assignment of agents in $\Theta$. For each path formula we use the strategy profile $\Theta$ (mapping each agent to a strategy) to construct the path on which we evaluate $\psi$. We write $\mathcal{G}$$\models_{\mathrm{SL}}\varphi$ if $s_{0}$, $\{\},\{\}$$\models_{\mathcal{G}}\varphi$ in the SL semantics.

Encoding. We can easily encode SL into HyperSL. Instead of using explicit agent bindings as in SL, in HyperSL, each path is annotated with an explicit strategy profile that assigns a strategy
(variable) to each agent. We assume that in the SL formula no two quantifiers quantify the same strategy variable (which we can always ensure by 𝛼-renaming). Let �𝜋 denote some *fixed* path variable. In our translation, we maintain an auxiliary mapping
�𝑥 : *Agts* ⇀ X mapping agents to strategy variables. We then translate path formulas as follows:

�𝑎� := 𝑎 �𝜋
�¬𝜓� := ¬�𝜓�
�𝜓1 ∧𝜓2� := �𝜓1� ∧ �𝜓2�
�𝜑� := �𝜑�{}
� X𝜓� := X �𝜓�
�𝜓1 U𝜓2� := �𝜓1� U �𝜓2�

For state formulas we define:
�𝜑1 ∧ 𝜑2��𝑥 := �𝜑1��𝑥 ∧ �𝜑2��𝑥
�𝜑1 ∨ 𝜑2��𝑥 := �𝜑1��𝑥 ∨ �𝜑2��𝑥
�∀𝑥.𝜑��𝑥 := ∀𝑥. �𝜑��𝑥
�∃𝑥.𝜑��𝑥 := ∃𝑥. �𝜑��𝑥
�𝜓��𝑥 := �𝜓�[ �𝜋 : �𝑥]
�(𝑖,𝑥)𝜑��𝑥 := �𝜑��𝑥 [𝑖↦→𝑥 ]
For path formulas, we resolve all atomic propositions on the fixed path variable �𝜋. For state formulas, we record the strategy variable played by each agent in the function �𝑥, and whenever we reach a path formula, use �𝑥 to construct the fixed path �𝜋. Note that the formula resulting from the translation uses boolean combination of state formulas. As already argued in Section 4, we can bring such formulas into the HyperSL syntax by introducing multiple paths
(see Example 1). We can show that our translation is correct and thus prove Lemma 1:
Lemma 1. For any SL formula 𝜑 there exists a HyperSL formula
𝜑′ *such that for any CGS* G, G |=SL 𝜑 *iff* G |= 𝜑′.

Proof. We can easily show that for any game structure G and SL formula 𝜑, we have that G |=SL 𝜑 if an only if G |= �𝜑�{}.

□
B.2
HyperATL∗ and HyperSL
In this subsection, we provide addition details on the relation of HyperATL∗ and HyperSL (cf. Section 5.2).

Our hyper variant of strategy logic considers strategies as firstorder objects that can be compared in different strategy profiles.

A weaker form of strategic reasoning is offered in ATL∗ [2] by only reasoning about the *outcome* of a strategic interaction. The ATL∗ formula ⎷𝐴⌄𝜓 expresses that the agents in 𝐴 have a joint strategy to enforce that the system follows some path that satisfies
𝜓. HyperATL∗ [14, 17] is a hyper-variant of ATL that combines strategic reasoning with the ability to express hyperproperties.

Similar to ATL∗, HyperATL∗ only considers the outcomes of a strategy but binds this outcome to a path variable which allows comparison w.r.t. a hyperproperty. Formulas in HyperATL∗ are generated by the following grammar:

$$\psi:=a_{\pi}\mid\neg\psi\mid\psi\wedge\psi\mid\mathsf{X}\psi\mid\psi\mathsf{U}\psi$$ $$\varphi:=\langle\!\langle A\rangle\!\rangle\pi.\,\varphi\mid\llbracket A\rrbracket\pi.\,\varphi\mid\psi$$

where $a\in AP$, $\pi\in\mathcal{V}$, and $A\subseteq\mathit{Agts}$.

_Semantics_. The semantics of HyperATL${}^{*}$ operates on a path assignment $\Pi:\mathcal{V}\to\mathcal{S}^{\omega}$. For path formulas, we follow a similar semantics as used in HyperSL (cf. Section 4):

Π |=G 𝑎𝜋
iff
𝑎 ∈ 𝐿(Π(𝜋)(0))
Π |=G 𝜓1 ∧𝜓2
iff
Π |=G 𝜓1 and Π |=G 𝜓2
Π |=G ¬𝜓
iff
Π ̸|=G 𝜓
Π |=G X𝜓
iff
Π[1, ∞] |=G 𝜓
Π |=G 𝜓1 U𝜓2
iff
∃𝑗 ∈ N. Π[𝑗, ∞] |=G 𝜓2 and
∀0 ≤ 𝑘 < 𝑗. Π[𝑘, ∞] |=G 𝜓1

For state formulas, we need to consider all possible outcomes under strategies for a subset of the agents. Given 𝐴 ⊆ *Agts* and strategies
{𝑓𝑖 | 𝑖 ∈ 𝐴} we define *out* G
�𝑠, {𝑓𝑖 | 𝑖 ∈ 𝐴}� ⊆ 𝑆𝜔 as

out G
     �𝑠,{𝑓𝑖 | 𝑖 ∈ 𝐴}� :=
       �
        PlayG(𝑠,
                  �

𝑖∈Agts
          𝑓𝑖) | ∀𝑖 ∈ Agts \ 𝐴. 𝑓𝑖 ∈ Str(G)
                                                           �
                                                             .

That is, out G
              �𝑠, {𝑓𝑖 | 𝑖 ∈ 𝐴}� contains all possible paths compatible
with the strategies in {𝑓𝑖 | 𝑖 ∈ 𝐴}. We can then evaluate a state
formula in the context of a state 𝑠 and path assignment Π.

𝑠, Π |=G 𝜓
                          iff
                                Π |=G 𝜓

𝑠, Π |=G ⎷𝐴⌄𝜋.𝜑
                          iff
                                ∃{𝑓𝑖 | 𝑖 ∈ 𝐴}.

∀𝑝 ∈ out G
       �𝑠, {𝑓𝑖 | 𝑖 ∈ 𝐴}�.𝑠, Π[𝜋 ↦→ 𝑝] |=G 𝜑

𝑠, Π |=G �𝐴�𝜋.𝜑
                          iff
                                ∀{𝑓𝑖 | 𝑖 ∈ 𝐴}.

∃𝑝 ∈ out G
       �𝑠, {𝑓𝑖 | 𝑖 ∈ 𝐴}�.𝑠, Π[𝜋 ↦→ 𝑝] |=G 𝜑

That is, a formula ⎷𝐴⌄𝜋.𝜑 holds when there exist strategies for
all agents in 𝐴 such that all possible outcomes under those fixed
strategies, when bound to 𝜋, satisfy 𝜑. Likewise, �𝐴�𝜋.𝜑 holds
when all possible strategies admits some path that, when bound
to 𝜋, satisfies 𝜑. We write G |=HyperATL∗ 𝜑 if 𝑠0, {} |=G 𝜑 in the
HyperATL∗ semantics.

  Encoding. Similar to the fact that ATL∗ can be encoded in SL
[24], we can encode HyperATL∗ in HyperSL. The idea is to treat
the ATL-quantifier ⎷𝐴⌄ as a strategy quantifier that existentially
quantifies over strategies for agents in 𝐴 and then universally over
strategies for agents outside of 𝐴. HyperATL∗ path formulas can be
translated verbatim into HyperSL path formulas. To translate state
formulas we maintain a auxiliary mapping 𝒍 : V ⇀ XAgts from
path variables to strategy profiles:

$$\left(\left|\psi\right|^{I}:=\psi\left[\pi_{1}:I(\pi_{1}),\ldots,\pi_{m}:I(\pi_{m})\right]\right.$$ $$\left.\left(\left|\left\langle A\right\rangle\pi.\varphi\right|\right)^{I}:=\underset{i\in A}{\exists}x_{i}.\quad\forall\quad x_{i}.\quad\left(\varphi\right)^{I}\left[\pi\mapsto\prod_{i\in Ag\mathrm{ts}}x_{i}\right]\right.$$ $$\left.\left(\left|\left[A\right]\pi.\varphi\right|\right)^{I}:=\underset{i\in A}{\forall}x_{i}.\quad\underset{i\in Ag\mathrm{ts}\setminus A}{\exists}x_{i}.\quad\left(\varphi\right)^{I}\left[\pi\mapsto\prod_{i\in Ag\mathrm{ts}\setminus A}x_{i}\right]\right.$$

In the first case, we assume that $\pi_{1},\ldots,\pi_{m}$ are the path variables used in $\psi$. In the second and third case, we assume that $x_{1},\ldots,x_{n}$ are fresh strategy variables for each agent. Intuitively, we replace each $\left\langle A\right\rangle\pi$ quantifier with existential quantification over fresh strategies for $A$, followed by universal quantification over strategies for $Ag\mathrm{ts}\setminus A$. In the auxiliary mapping $I$, we record which strategy profile we later want to use to construct $\pi$. For the path formula $\psi$ we then reconstruct all paths used in the formula using the strategy profiles recorded in $I$. We can use our translation to prove Lemma 2:
Lemma 2. For any HyperATL∗ formula 𝜑 there exists a HyperSL
formula 𝜑′ *such that for any CGS* G, G |=HyperATL∗ 𝜑 *iff* G |= 𝜑′.

Proof. An easy induction shows that for any game structure G and HyperATL∗ formula 𝜑 it holds that G |=HyperATL∗ 𝜑 if and only if G |= �𝜑�{}.

□

  HyperATL∗
          𝑆. As our translation �𝜑�{} explicitly quantifies over
strategies for all agents, we can easily enforce that two agents share
a strategy by simply using the same strategy (variable) for both.

Using a slight modification of the previous translation, we can thus
handle the sharing constraints from HyperATL∗
                                                𝑆 [18]:

  Lemma 3. For any HyperATL∗
                          𝑆 formula 𝜑 there exists a HyperSL
formula 𝜑′ such that for any CGS G, G |=HyperATL∗
                                         𝑆 𝜑 iff G |= 𝜑′.

## B.3 Slii And Hypersl

In this subsection, we provide addition details on the relation of SLii and HyperSL (cf. Section 5.3).

SLii [12] extends SL (cf. Section 5.1) by allowing strategies that only observe parts of the system. The formal model of SLii are game structures that are endowed with an observations. Let G =
(𝑆,𝑠0, A*,𝜅, 𝐿*) be a fixed game structure and let *Obs* be a fixed finite set of so-called *observations*. An observation family {∼𝑜}𝑜∈Obs associates an equivalence relation ∼𝑜⊆ 𝑆 × 𝑆 with each 𝑜 ∈ *Obs*.

For a strategy with observation 𝑜, two states 𝑠 ∼𝑜 𝑠′ appear identical. This naturally extends to finite plays: Two finite plays
𝑝, 𝑝′ ∈ 𝑆+ are 𝑜-indistinguishable, written 𝑝 ∼𝑜 𝑝′, if |𝑝| = |𝑝′|
and for each 0 ≤ 𝑖 < |𝑝|, 𝑝(𝑖) ∼𝑜 𝑝′(𝑖). An 𝑜*-strategy* is a function
𝑓 : 𝑆+ → A that cannot distinguish between 𝑜-indistinguishable plays, i.e., for all *𝑝, 𝑝*′ ∈ 𝑆+ with 𝑝 ∼𝑜 𝑝′ we have 𝑓 (𝑝) = 𝑓 (𝑝′). We denote with *Str*(G,𝑜) the set of all 𝑜-strategies in G. We consider SLii formulas that are generated by the following grammar:
𝜓 := 𝑎 | ¬𝜓 | 𝜓 ∧𝜓 | X𝜓 | 𝜓 U𝜓
𝜑 := 𝜓 | 𝜑 ∧ 𝜑 | 𝜑 ∨ 𝜑 | ∀𝑥𝑜.𝜑 | ∃𝑥𝑜.𝜑 | (𝑖,𝑥)𝜑
where 𝑎 ∈ AP, 𝑥 ∈ X, 𝑖 ∈ *Agts*, and 𝑜 ∈ *Obs* is an observation.

Compared to SL, strategy quantification in SLii does not range over arbitrary strategies but over strategies that respect a given observation.

Semantics. The semantics of SL (cf. Appendix B.1) only needs to be changed in the case of strategy quantification:
𝑠, Δ, Θ |=G ∀𝑥𝑜.𝜑
iff
∀𝑓 ∈ Str(G,𝑜).𝑠, Δ[𝑥 ↦→ 𝑓 ], Θ |=G 𝜑
𝑠, Δ, Θ |=G ∃𝑥𝑜.𝜑
iff
∃𝑓 ∈ Str(G,𝑜).𝑠, Δ[𝑥 ↦→ 𝑓 ], Θ |=G 𝜑
where we restrict quantification to 𝑜-strategies. Given a game structure G, a family {∼𝑜}𝑜∈Obs, and an SLii formula 𝜑 we write
(G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 if 𝑠0, {}, {} |=G 𝜑 in the SLii semantics. See
[12, 13] for concrete examples of SLii.

Injective Labeling and Action Recording. To prove Theorem 1, we need to translate SLii MC instances into equisatisfiable HyperSL
instances. In order to translate the model-checking instances, we first modify the underlying game structure. The reason for this is simple: Strategies are defined as functions 𝑆+ → A and ∼𝑜 is defined as a direct relation on states, i.e., both are defined directly on *components of the game structure*. In contrast, *within* our logic, we only observe the evaluation of the atomic propositions. In a first step, we thus modify the game structure provided us with sufficient information within its atomic propositions:
Definition 4. A game structure G = (𝑆,𝑠0, A*,𝜅, 𝐿*) is injectively labeled (IL), if 𝐿 : 𝑆 → 2AP is injective, i.e., two labels are equal iff the state is equal. A game structure is action recording (AR) if for each agent 𝑖 ∈ Agts and every action 𝑎 ∈ A, there exists an atomic proposition ⟨𝑖,𝑎⟩ ∈ AP that holds in a state exactly when 𝑖 played
𝑖∈Agts 𝑎𝑖, we have action 𝑎 in the last step. That is, for all 𝑠 ∈ 𝑆 and all action profile
�
𝑖∈Agts
{⟨𝑖,𝑎𝑖⟩}.

𝐿�𝜅(𝑠,
�
𝑖∈Agts
𝑎𝑖)� ∩ {⟨𝑖,𝑎⟩ | 𝑖 ∈ *Agts*,𝑎 ∈ A} =
�
We can always ensure that G is injectively labeled by adding at most ⌈log |𝑆|⌉ fresh atomic propositions. The evaluation of all formulas (which do not refer to these fresh propositions) remains unchanged when adding such fresh propositions. Similarly, we can always ensure that a structure records actions. This increases the number of states by a factor of |A||*Agts*| but does not increase the branching in the system, nor does it change the semantics of SLii if we extend ∼𝑜 to the new states in the obvious way:

  Lemma 7. Given an SLii MC instance (G, {∼𝑜}𝑜∈Obs,𝜑) there
exists an effectively computable SLii instance (G′, {∼′𝑜}𝑜∈Obs,𝜑′)
where (1) G′ is IL and AR, and (2) (G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 iff
(G′, {∼′𝑜}𝑜∈Obs) |=SLii 𝜑′.

Proof. Assume G = (𝑆,𝑠0, A,𝜅, 𝐿). Define AP′ := AP ⊎ {⟨𝑖,𝑎⟩ |

𝑖 ∈ Agts,𝑎 ∈ A}. We then define

𝑖∈Agts 𝑎), A,𝜅′, 𝐿′)

G′ = (𝑆 × (Agts → A), (𝑠0, �

where $a\in\mathbb{A}$ is some arbitrary action (in the initial state, we do not need to track the last played action). For an action profile $\prod_{i\in Agts}a_{i}$, we define $\kappa^{\prime}$ and $l^{\prime}$ by

$$\kappa^{\prime}\left((s,\_),\prod_{i\in Agts}a_{i}\right):=(\kappa(s,\prod_{i\in Agts}a_{i}),\prod_{i\in Agts}a_{i})$$

$$L^{\prime}(s,\prod_{i\in Agts}a_{i}):=L(s)\uplus\{\langle i,a_{i}\rangle\mid i\in Agts\}.$$
𝑖∈*Agts* 𝑎𝑖 in the second component to set the APs ⟨𝑖,𝑎𝑖⟩ for all 𝑖 ∈ *Agts*. We define {∼′𝑜}𝑜∈Obs by The idea behind G′ is that we record the action profile that was last used in the second component of each state. In each transition, we ignore the action profile in the current step, and record the new action profile n the second component. In the labeling function, we can then use the action profile �

∼′
𝑜:=
   ��(𝑠, _), (𝑠′, _)� | 𝑠 ∼𝑜 𝑠′�
                   .

That is, for any observation cannot distinguish states based on the
second position. In particular note that (𝑠, _) and (𝑠, _) are always
indistinguishable, i.e., all states we expanded that we added are
indistinguishable under the new observation.
  It is easy to see that G′ is AR and that (G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 iff
(G′, {∼′𝑜}𝑜∈Obs) |=SLii 𝜑. Note that we did not change the formula.
In a second step, we can ensure that G′ is also IL by simply adding
sufficiently many new propositions. As those new propositions are
never used in 𝜑 the semantics is unchanged.
                                                                 □

Identifying Indistinguishable States.In the next step, we construct a formula that identifies pairs of states that are indistinguishable according to $\sim_{o}$. For $o\in Obs$, we define formula $ind_{o}(\pi_{1},\pi_{2})$ as follows:

$$\bigvee_{(s,s^{\prime})\in\sim_{o}}\left(\bigwedge_{a\in L(s)}a_{\pi}\wedge\bigwedge_{a\in AP\setminus L(s)}a_{\pi}\wedge\bigwedge_{a\in L(s^{\prime})}a_{\pi^{\prime}}\wedge\bigwedge_{a\in AP\setminus L(s^{\prime})}\neg a_{\pi^{\prime}}\right)$$

It is easy to see that on any injectively labeled game structure $ind_{o}(\pi_{1},\pi_{2})$ holds if the two paths bound to $\pi_{1},\pi_{2}$ are $\sim_{o}$-related in their first state.

Enforcing Partial Information. Given an observation 𝑜 ∈ *Obs*, and strategy variable 𝑥, we define a formula *indStrat*𝑜 (𝑥) that holds on a strategy iff this strategy is an 𝑜-strategy (in all reachable situations and for all agents) as follows:

$$\begin{split}indStrat_{o}(x)&:=\forall y_{1},\ldots,y_{n},y^{\prime}_{1},\ldots,y^{\prime}_{n}.\\ &\bigwedge_{i=1}^{n}\psi^{i}_{o}\left[\pi_{1}:(y_{1},\ldots,y_{i-1},x,y_{i+1},\ldots,y_{n})\right]\\ &\pi_{2}:(y^{\prime}_{1},\ldots,y^{\prime}_{i-1},x,y^{\prime}_{i+1},\ldots,y^{\prime}_{n})\right]\end{split}$$

where

$$\psi^{i}_{o}:=\Big{(}\,\mathsf{X}\Big{(}\bigwedge_{a\in\mathbb{A}}\langle i,a\rangle_{\pi_{1}}\leftrightarrow\langle i,a\rangle_{\pi_{2}}\Big{)}\Big{)}\,\mathsf{W}\,\Big{(}\neg ind_{o}(\pi_{1},\pi_{2})\Big{)}.$$

The path formula $\psi^{i}_{o}$ compares two paths $\pi_{1},\pi_{2}$ and states that as long as a prefix on those to paths is $o$-indistinguishable (i.e., $ind_{o}(\pi_{1},\pi_{2})$ holds in each step), the action selected by agent $i$ is the same on both paths (using the fact that the structure records actions). As we do not know which agents might end up playing strategy $x$ we assert that $x$ behaves as a $o$-strategy for all agents. For each $i\in Agts$ we thus compare two paths where $i$ plays $x$, but all other agents play some arbitrary strategy, and assert that $\psi^{i}_{o}$ holds for those two paths. Strategy $x$ must thus respond to two $o$-indistinguishable prefixes with the same action in all reachable situations for all agents.

The Translation. Using *indStrat*𝑜 (𝑥) as a building block, we can modify the translation of SL into HyperSL from Appendix B.1, and instead translate the much stronger SLii.

Theorem 1. For any SLii MC instance �(G, {∼𝑜}𝑜∈Obs),𝜑�, we can effectively compute a HyperSL MC instance �G′,𝜑′�, such that
(G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 iff G′ |= 𝜑′.

Proof. In a first step, we use Lemma 7 to ensure that G is IL
and AR. We can then translate 𝜑 using a similar translation to the one used in Appendix B.1. The only cases that require changening are the translation of quantification:
�∀𝑥𝑜.𝜑��𝑥 := ∀𝑥. *indStrat*𝑜 (𝑥) → �𝜑��𝑥
�∃𝑥𝑜.𝜑��𝑥 := ∃𝑥. *indStrat*𝑜 (𝑥) ∧ �𝜑��𝑥
Note that the resulting formula uses implications between state formulas which is not supported by the HyperSL syntax. It is, however, easy to see that we can push the boolean operations into the path formula as observed in Example 1.

We claim that for any SLii MC instance (G, {∼𝑜}𝑜∈Obs,𝜑) where G is IL and AR, we have that (G, {∼𝑜}𝑜∈Obs) |=SLii 𝜑 iff G |= �𝜑�{}.

To prove the above we need to argue that *indStrat*𝑜 (𝑥) really expresses that 𝑥 is a 𝑜-strategy. It is easy to see that for any strategy
𝑓 ∈ *Str*(G) we have 𝑠, [𝑥 ↦→ 𝑓 ] |= *indStrat*𝑜 if and only if 𝑓 is a
𝑜-strategy in all reachable situations from 𝑠. That is, 𝑓 does not necessarily behave as an 𝑜-strategy in all situations, but at least in those situations that are actually reachable under 𝑓 . As any strategy will only ever be queried on plays that are compatible with the strategy itself, this suffices to encode the SLii semantics.

□

## C Additional Material For Section 6

In this section we prove the correctness of our HyperSL[SPE] model-checking algorithm (Algorithm 2). Our algorithm hinges on simulate procedure (Algorithm 1) and the resulting properties
(Proposition 2). We dedicate the entire Appendix D to a proof of Proposition 2, and here focus on the correctness (and complexity) of Algorithm 2.

## C.1 Correctness Proof Of Algorithm 2

As already argued in the main part of the paper, our correctness proof relies on an inductive argument that establishes that we compute (G, �𝑠,𝑘)-summaries for each 1 ≤ 𝑘 ≤ 𝑚 + 1.

Lemma 4. In line 7, A𝑘 is a (G, �𝑠,𝑘)-summary.

Proof. We show the statement by induction on 1 ≤ 𝑘 ≤ 𝑚 + 1
(from 𝑘 = 𝑚 + 1 to 𝑘 = 1). For the base case (𝑘 = 𝑚 + 1), we observe that the APA A𝑚+1 (computed in line 4) is a (G, �𝑠,𝑚 + 1)-summary.

For the induction step we can assume - by induction hypothesis –
that prior to line 6, A𝑘+1 is a (G, �𝑠,𝑘+1)-summary. Recall that A𝑘+1
is an APA over ({𝜋1*, . . . 𝜋*𝑘} → 𝑆) and A𝑘 over ({𝜋1*, . . . 𝜋*𝑘−1} →
𝑆). We claim that A𝑘 is a (G, �𝑠,𝑘)-summary. To show this, take any
Π : {𝜋1*, . . . 𝜋*𝑘−1} → 𝑆𝜔 and we need to show that (cf. Definition 2
of (G, �𝑠,𝑘)-summary) *zip*(Π) ∈ L(A𝑘) if and only if
𝑗=𝑘 |=G 𝜓.

𝑖∈Agts
𝑓�𝑥𝑗 (𝑖)
��𝑚

�
♭𝑘 · · · �
   ♭𝑚. Π
       �
       𝜋𝑗 ↦→ PlayG
               ��𝑠,
                 �

By adding parenthesis, the latter holds if and only if

𝑗=𝑘 |=G 𝜓
                �

𝑖∈Agts
          𝑓�𝑥𝑗 (𝑖)
                   ��𝑚

�
♭𝑘.
 �
  �
  ♭𝑘+1 · · · �
       ♭𝑚. Π
          �
           𝜋𝑗 ↦→ PlayG
                   ��𝑠,
                     �

which holds if and only if

𝑗=𝑘+1 |=G 𝜓
                    �

𝑖∈Agts
          𝑓�𝑥𝑗 (𝑖)
                   ��𝑚

�
♭𝑘.
 �
  �
  ♭𝑘+1 · · · �
       ♭𝑚. Π′�
           𝜋𝑗 ↦→ PlayG
                   ��𝑠,
                      �

                                                     𝑖∈Agts 𝑓�𝑥𝑘 (𝑖)
                                                                        ��
                                                                            . By the assumption
that A𝑘+1 is a (G, �𝑠,𝑘 + 1)-summary we can replace the inner part
and get that the above is equivalent to

where Π′ = Π[𝜋𝑘 ↦→ PlayG
                      ��𝑠, �

After unfolding the definition of Π′, this becomes

�
♭𝑘.zip(Π′) ∈ L(A𝑘+1).

𝑖∈Agts
          𝑓�𝑥𝑘 (𝑖)
                   ���
                         ∈ L(A𝑘+1).

�
♭𝑘. zip
   �
    Π
     �
      𝜋𝑘 ↦→ PlayG
              ��𝑠,
                �

Now recall that we defined A𝑘 = simulate(G,�𝑠,𝜋𝑘,�𝑥𝑘,♭𝑘,A𝑘+1).
By Proposition 2 we now have that the above holds iff

zip(Π) ∈ L(A𝑘).

as required.
                                                                 □

  Lemma 5. For any (G, �𝑠, 1)-summary A, we have that L(A) ≠ ∅
if and only if �𝑠, {} |=G 𝜑.

Proof. Note that the alphabet of $\mathcal{A}$ is the singleton set $(\emptyset\to S)$. We thus get that $\mathcal{L}(\mathcal{A})\neq\emptyset$ iff $\mathit{zip}(\{\})\in\mathcal{L}(\mathcal{A})$ where $\{\}$ is the unique path assignment $\emptyset\to S^{\omega}$ so $\mathit{zip}(\{\})$ is the unique word over $(\emptyset\to S)$. Now by Definition 2 we have that $\mathit{zip}(\{\})\in\mathcal{L}(\mathcal{A})$ iff

$$\tilde{b}_{1}\cdots\tilde{b}_{m}.\,\{\}\Big{[}\pi_{j}\mapsto\mathit{Play}_{\mathcal{G}}(\dot{s},\prod_{i\in\mathit{Alg}_{\mathcal{G}}(i)}f_{\tilde{\pi}_{j}(i)})\Big{]}_{j=1}^{m}\models_{\mathcal{G}}\psi$$ where we add all paths to the empty path assignment $\{\}$. As we add to the empty path assignment, the above is thus equivalent to

$$\widetilde{b}_{1}\cdots\widetilde{b}_{m}\cdot\left[\pi_{j}\mapsto\mathit{Play}_{\mathcal{G}}\left(\dot{s},\prod_{i\in\mathit{Alg}_{\mathcal{B}}^{\mathrm{r}}}f_{\widehat{x}_{j}\left(i\right)}\right)\right]_{j=1}^{m}\models_{\mathcal{G}}\psi$$

which exactly expresses $\dot{s}$, $\{\}\models_{\mathcal{G}}\varphi$ in the HyperSL semantics.

## C.2 Model-Checking Complexity

Theorem 3. Model checking for a HyperSL[SPE] formula with block-rank 𝑚 *is in* 2𝑚-EXPTIME.

Proof. Each time we invoke simulate (Algorithm 1) the automaton size increases by two exponents. A formula with block-rank 𝑚 requires 𝑚 applications of simulate (cf. Algorithm 2), so the final automaton A1 has size that is 2𝑚-times exponential in the size of
𝜓 and G. Automaton A1 operates on a singleton alphabet (∅ → 𝑆), so we can decide its emptiness in polynomial time. Model checking is thus in 2𝑚-EXPTIME in the size of 𝜓 and G.

□
Lemma 6. Model checking for a HyperSL[SPE] formula with blockrank 𝑚 is (2𝑚 − 1)-EXPSPACE-hard.

Proof. For HyperATL∗ it is known that checking a formula with 𝑚 quantifiers is (2𝑚 − 1)-EXPSPACE-hard (in the size of the formula) [17, Thm. 7.1 and 7.2]. As the translation of a HyperATL∗
formula with 𝑚 qunatifiers into a HyperSL[SPE] formula is linear
(cf. Lemma 2 and Appendix B.2) and yields a formula with blockrank 𝑚, the lower bound follows.

□

## C.3 Beyond Hypersl[Spe]

As we argued in Section 6.7, any HyperSL formula where the prefix cannot be grouped into blocks as in Definition 1, MC becomes in general undecidable.

Lemma 8. Model checking for a HyperSL formula of the form
∃𝑥.∃𝑦.∀𝑧.∀𝑤.𝜓
�𝜋1 : (𝑥,𝑧)
�
𝜋2 : (𝑦,𝑤)
is, in general, undecidable.

Proof. We encode the HyperLTL realizability problem of a ∀2

formula, which is known to be undecidable [32]. Given a HyperLTL formula $\varphi=\forall\pi_{1}.\forall\pi_{2}.\psi$ over $I\upharpoonright O$ we define

$$\psi^{\prime}:=\psi\wedge\left(\left(\chi\left(\bigwedge_{\alpha\in\mathcal{O}}a_{\pi_{1}}\leftrightarrow a_{\pi_{2}}\right)\right)\mathsf{W}\left(\bigvee_{\alpha\in I}a_{\pi_{1}}\leftrightarrow a_{\pi_{2}}\right)\right)$$

That is, the two paths $\pi_{1},\pi_{2}$ should satisfy $\psi$ and, in addition, when given the same sequence of inputs, the output should be the same. We claim that $\varphi=\forall\pi_{1}.\forall\pi_{2}.\psi$ is realizable if and only if

$$\mathcal{G}_{(I,O)}\models\exists x.\exists y.\forall z.\forall w.\,\psi^{\prime}\begin{bmatrix}\pi_{1}:(x,z)\\ \pi_{2}:(y,w)\end{bmatrix}$$

where $\mathcal{G}_{(I,O)}$ is the CGS in which agent $1$ can set the inputs $I$ and agent $2$ can set the outputs $O$ (see, e.g., [2]). The intuition is that the additional conjunct requires that the two strategies bound to $x$ and $y$ denote the _same_ strategy. The above formula thus states that there exists some strategy that controls the outputs such that all pairs of traces under that strategy satisfy $\psi$. Deciding the existence of such a strategy is undecidable [32], so we get the desired result.

## D Proof Of Proposition 2

In this section, we prove Proposition 2:

Proposition 2: _Given $\delta\in S,\pi\in\mathcal{V}$, a strategy profile $\vec{x}:\mathit{Apts}\to\mathcal{X}$, a quantifier block $\mathfrak{b}$ such that for every $i\in\mathit{Apts},\vec{x}(i)$ is quantified in $\mathfrak{b}$, and an APA $\mathcal{A}$ over alphabet $(V\upharpoonright\pi)\to S)$. Let $\mathcal{B}$ be the results of $\mathit{simulate}(\mathcal{G},\delta,\pi,\vec{x},\mathfrak{b},\mathcal{A})$. Then for any path assignment $\Pi:V\to S^{\omega}$, we have $\mathit{zip}(\Pi)\in\mathcal{L}(\mathcal{B})$ iff_

$$\widetilde{\mathfrak{b}}.\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}(\delta,\prod_{i\in\mathit{Apts}}f_{\vec{x}(i)})\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).\tag{1}$$

For any $m\in\mathbb{N}$, we define $[m]:=\{1,\ldots,m\}$. To make the proof of its correctness easier, we assume that

$$\mathfrak{b}=\forall1.\exists2.\forall3\ldots\exists2m.\tag{2}$$

That is, we assume that the strategy variables are number in $[2m]$. And, moreover, we assume the quantifier block alternates strictly in every step: odd strategy variables (numbers) are universally quantified and even variables are existentially quantified. Note that this assumption is w.l.o.g., we can always add quantification over additional strategy variables that wil never be used for the construction of $\pi$. Having a fixed alternation makes formal reasoning and notation easier.

The Candidate. Let Adet = (𝑄,𝑞0*,𝛿,𝑐*) be the DPA constructed from A in line 2 of Algorithm 1 (using Proposition 1). Following the construction in Algorithm 1, we get that B (the result of simulate(G,�𝑠,𝜋,�𝑥,♭,A)) satisfies B = �𝑄 × 𝑆, (𝑞0, �𝑠),𝛿′,𝑐′�, where 𝑐′(𝑞,𝑠) := 𝑐(𝑞), and for �𝑡 ∈ 𝑆𝑉 , 𝛿′�(𝑞,𝑠), �𝑡� is defined as as
�
�
𝑎1∈A
𝑎2∈A
· · ·
�
𝑎2𝑚 ∈A

𝑖∈Agts
         𝑎 �𝑥 (𝑖)
                  ��
                     ,

�
𝛿 �𝑞, �𝑡 [𝜋 ↦→ 𝑠]�,𝜅�𝑠,
                        �

With this construction fixed, it remains to argue that it accepts the
desired language. Expressed as a lemma:

**Lemma 9**.: _For any path assignment $\Pi:V\to S^{\omega}$ we have $zip(\Pi)\in\mathcal{L}(\mathcal{B})$ if and only if_

$$\widetilde{b}.\,zip\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}(\dot{s},\prod_{i\in\mathcal{A}_{\mathcal{B}}^{\mathrm{c}}\mathrm{rs}}f_{\widetilde{x}(i)})\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).\tag{3}$$

The main prove idea in showing that B accepts the language desired by Proposition 2, goes via the determinacy of concurrent parity games.

  Definition 5 (Concurrent Parity Game). A concurrent parity
game (CPG) is a a tuple P = (𝑉, 𝑣0, A,𝑚, 𝜇,𝑐) where 𝑉 is a (possibly
infinite) set of vertices, 𝑣0 ∈ 𝑉 is an initial vertex, A is a finite set of
actions, 𝑚 ∈ N gives the number of alternations (so 2𝑚 is the number
of player), 𝜇 : 𝑉 × ([2𝑚] → A) → 𝑉 is a transition function, and
𝑐 : 𝑉 → 𝐶 is a coloring for some finite 𝐶 ⊆ N.

  We refer to the protagonist in CPGs as players to distinguish
them from the agents in a game structure. Similar to the simplyfying
assumption we made of ♭, we will later quantify universally over
strategies for odd players and existentially for even players. A
strategy in P is a function 𝑓 : 𝑉 + → A and we write Str(P)

for the set of all strategies in P. When given a strategy profile
�𝑓 : [2𝑚] → Str(P) assigning a strategy for each player, and a
vertex 𝑣 ∈ 𝑉 , we define PlayP (𝑣, �𝑓 ) ∈ 𝑉 𝜔 as the unique play
𝑝 ∈ 𝑉 𝜔 such that 𝑝(0) = 𝑣, and for every 𝑗 ∈ N, 𝑝(𝑗 + 1) =
𝜇�𝑝(𝑗), �
          𝑙 ∈[2𝑚] �𝑓 (𝑙)(𝑝[0, 𝑗])� (similar to the definition in CGSs,
cf. Section 3). We say an infinite play 𝑝 ∈ 𝑉 𝜔 is even if the minimal
color that occurs infinity many times (as given by 𝑐) is even. In this
case we write even(𝑝).

Definition 6. The CPG P is won by the existential team if

$\forall f_{1}\in Str(\mathcal{P}).\exists f_{2}\in Str(\mathcal{P}).\forall f_{3}\in Str(\mathcal{P})\dots\exists f_{2m}\in Str(\mathcal{P}).$

$$\text{even}\Big{(}\text{Play}_{\mathcal{P}}(v_{0},\prod_{l\in[2m]}f_{l})\Big{)}.$$

That is we quantify over strategies in $\mathcal{P}$ for all player $l\in[2m]$; universally for odd player and existentially for even player in alternating fashion. The game is won (by the existential team) if the existential quantifier can ensure that the resulting play is even.

D.2
Construction of PΠ
Assume we are given a fixed strategy assignment Π : 𝑉 → 𝑆𝜔. We design an infinite-state CPG PΠ as PΠ = (𝑄 × 𝑆 × N, (𝑞0, �𝑠, 0), A*,𝑚, 𝜇,𝑐*′)
𝑖∈Agts
�𝑎(�𝑥(𝑖))�, 𝑁 + 1
�

where 𝑄 is the set of states in Adet, 𝑐′(𝑞,𝑠, 𝑁) := 𝑐(𝑞) and for each
action profile �𝑎 : [2𝑚] → A we define 𝜇�(𝑞,𝑠, 𝑁), �𝑎� as
     �
      𝛿 �𝑞, zip(Π)(𝑁)[𝜋 ↦→ 𝑠]�,𝜅�𝑠,
                               �

In the following we abbreviate 𝑉 := 𝑄 × 𝑆 × N for the vertices in
PΠ, and define 𝑣0 := (𝑞0, �𝑠, 0) as the initial vertex of PΠ.
  Let us discuss the construction of PΠ. Actions in PΠ are the
same as in G (i.e., A). For each quantified strategy variable 1, . . . , 2𝑚
(cf. Equation (2)), we have a corresponding player in PΠ (i.e., there
are 𝑚 alternations, so the set of players is [2𝑚]). We operate on
vertices (𝑞,𝑠, 𝑁), where 𝑞 ∈ 𝑄 and 𝑠 ∈ 𝑆 are similar to the construc-
tion of B. In addition we track the current step 𝑁. To update 𝑞 we
invoke the transition function 𝛿 of Adet on the current automaton
state and letter zip(Π)(𝑁)[𝜋 ↦→ 𝑠]. Note that this corresponds to
the input of B: B reads the zipping of a strategy assignment Π as
an input and thus the 𝑁th letter of the input is zip(Π)(𝑁). That is,
we "hardcode" Π into the game. For this, we maintain the current
step via counter 𝑁 and "pretend" the input in the 𝑁th step was
zip(Π)(𝑁). Similar to B, we update the automaton state by pass-
ing zip(Π)(𝑁)[𝜋 ↦→ 𝑠] to Adet's transition function. To update
the state of the simulation of G we proceed as in B, i.e., given a
function �𝑎 : [2𝑚] → A that fixes actions for all strategy variables
(or, equivalently, players in PΠ), each agent 𝑖 ∈ Agts will simply
play the action assigned to strategy variable �𝑥(𝑖), i.e., �𝑎(�𝑥(𝑖)).
  The idea of PΠ is to serve as intermediate representation be-
tween the target language (Eq. (3)) and the definition of B. In the
semantics of CPGs the quantification over strategies for the players
occurs "outside", i.e., strategies are fixed globally (cf. Definition 6).
As players in PΠ correspond exactly to the strategy variables used
in ♭ ([2𝑚]), this "outer" quantification mimics the quantification
found in Eq. (3). On the other hand, the updates of automaton and
system state in PΠ are similar to the updates performed in B.

## D.3 The First Implication

As a first step, we will show that PΠ is won by the existential player if and only Π satisfies Eq. (3). This step is easy: The quantification in PΠ and Eq. (3) is very similar (i.e., occurs "outside" the game).

We can, therefore, transfer strategies between G and PΠ as follows:
Lemma 10. The following holds:

* _For any_ $\Delta:[2m]\to\mathit{Str}(\mathcal{P}_{\Pi})$ _there exists a_ $\widetilde{\Delta}:[2m]\to\mathit{Str}(\mathcal{G})$ _such that_ $$\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}\big{(}\dot{s},\prod_{i\in\mathit{Agts}}\widetilde{\Delta}(\widetilde{x}(i))\big{)}\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).$$ _if and only if even_ $(\mathit{Play}_{\mathcal{P}_{\Pi}}(\mathcal{P}_{0},\Delta))$_._
* _For any_ $\Delta:[2m]\to\mathit{Str}(\mathcal{G})$ _there exists a_ $\widetilde{\Delta}:[2m]\to\mathit{Str}(\mathcal{P}_{\Pi})$ _such that_ $$\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}\big{(}\dot{s},\prod_{i\in\mathit{Agts}}\Delta(\widetilde{x}(i))\big{)}\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).$$
Proof. We show both claims separately.

if and only if even(Play${}_{\rm{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{\bf{}}}}}}}}}}}}}}}}}}}}}$ (${}_{0}$, $\bar{\Delta}$)).

Proof. We show both claims sets
- We translate strategies in PΠ to strategies in G. Let 𝑓 : 𝑉 + → A
be some strategy in PΠ. We define �𝑓 : 𝑆+ → A as follows: Let
𝑢 ∈ 𝑆+ be given. Define 𝒒 ∈ 𝑄+ as follows: We define 𝒒(0) =
𝑞0 (the initial state of Adet). For 0 ≤ 𝑖 < |𝑢| we then define
𝒒(𝑖 + 1) := 𝛿(𝒒(𝑖), *zip*(Π)(𝑖)[𝜋 ↦→ 𝑢(𝑖)]). The sequence 𝒒 thus
gives the unique state sequence in Adet when reading the first
|𝑢| states of *zip*(Π) extended with 𝑢. Now consider the finite play
in PΠ
𝜏 = �𝒒(0),𝑢(0), 0� · · · �𝒒(|𝑢| − 1),𝑢(|𝑢| − 1), |𝑢| − 1�.
The intuition is that 𝜏 corresponds to the unique path in PΠ
that, when projected onto the system state, gives 𝑢. We define
�𝑓 (𝑢) := 𝑓 (𝜏).

For any strategy assignment Δ : [2𝑚] → *Str*(PΠ) in PΠ we define �Δ : [2𝑚] → *Str*(G) as the assignment obtained by applying�· point wise.

It is now easy to see that *Play*G
��𝑠, �

ing " point wise.

It is now easy to see that $Play_{\mathcal{G}}\big{(}i,\prod_{i\in Agt}\widetilde{\Delta}(\widetilde{x}(i))\big{)}\big{)}\in S^{\omega}$ equals $Play_{\mathcal{P}_{\Pi}}(v_{0},\Delta)$ (when projecting vertices in $Q\times S\times\mathbb{N}$ on $S$). By construction, the automaton component in each vertex of $\mathcal{P}_{\Pi}$ simply simulates $\mathcal{A}_{det}$ on the generated sequence of system state and thus accepts play iff the corresponding automaton sequence is accepting. We thus get that the

$$\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}\big{(}i,\prod_{i\in Agt}\widetilde{\Delta}(\widetilde{x}(i))\big{)}\big{]}\Big{)}\in\mathcal{L}(\mathcal{A})=\mathcal{L}(\mathcal{A}_{det})$$

if and only if $\mathit{even}(\mathit{Play}_{\mathcal{P}_{\Pi}}(v_{0},\Delta))$, as required.

Let $f:S^{+}\to\mathbb{A}$ be a strategy in $\mathcal{G}$. We define 
- Let 𝑓 : 𝑆+ → A be a strategy in G. We define �𝑓 : 𝑉 + → A in
PΠ as follows: For any 𝑢 ∈ 𝑉 + let 𝒔 ∈ 𝑆+ be the projection on
the system state in 𝑢. We define �𝑓 (𝑢) := 𝑓 (𝒔), i.e., only query 𝑓
on the sequences of system states. For any strategy assignment
Δ : [2𝑚] → *Str*(G) in PΠ we define �Δ : [2𝑚] → *Str*(PΠ) as the
assignment obtained by applying�· point wise. As in the first case,
𝑖∈*Agts* Δ(�𝑥(𝑖))
�
) ∈ 𝑆𝜔 is equal to it is easy to see that *Play*G
��𝑠, �

_Play$\varphi_{\Pi}(v_{0},\widetilde{\Delta})$_ (when projecting vertices in $Q\times S\times\mathbb{N}$ on $S$). As $\mathcal{P}_{\Pi}$ simulates $\mathcal{A}_{\mathrm{def}}$ on the sequence of system states we thus get

$$\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}\big{(}\dot{s},\prod_{i\in\mathcal{A}_{\mathrm{f\!f\!f\!s}}}\Delta(\widetilde{x}(i))\big{)}\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).$$

if and only if _even($\mathit{Play}_{\mathcal{P}_{\Pi}}(v_{0},\widetilde{\Delta})$)_, as required. $\Box$

Proposition 3. $\mathcal{P}_{\Pi}$_is won by the existential team if and only if_

$$\widetilde{b}.\mathit{zip}\Big{(}\Pi\big{[}\pi\mapsto\mathit{Play}_{\mathcal{G}}\big{(}\dot{s},\prod_{i\in\mathcal{A}_{\mathrm{f\!f\!s}}}f_{\widetilde{x}(i)}\big{)}\big{]}\Big{)}\in\mathcal{L}(\mathcal{A}).\tag{4}$$

Proof.: In $\mathcal{P}_{\Pi}$ we quantify over strategies in $\mathcal{P}_{\Pi}$ for each player in $[2m]$ (cf. Definition 6). Conversely, Eq. (4) uses the same quantization order (in the prefix $\widetilde{b}$) but quantifies over strategies in $\mathcal{G}$ via strategy variables $1,\ldots,2m$ (Eq. 2). Using the translation in Lemma 10 we can translate any strategy assignment in $\mathcal{P}_{\Pi}$ to an equivalent one in $\mathcal{G}$, and vice versa. As the type (i.e., universal or existential) and order of quantification is $\mathcal{P}_{\Pi}$ and Eq. (4) is the same (cf. Eq. 2) and we can translate strategies between $\mathcal{G}$ and $\mathcal{P}_{\Pi}$, the result follows.

## D.4 Positional Determinacy

The more challenging direction is to show that PΠ is won by the existential team iff B accepts *zip*(Π). The key challenge is that the way strategies are quantified is fundamentally different: In PΠ we quantify over full strategies in advance (i.e., "outside") and in B
we (conjunctively or disjunctively) pick actions in each step of the automaton (i.e., "inside"). The key ingredient we use is the positional determinacy of CPGs. Intuitively, a positional strategy is one that decides on an action based solely on the current vertex of the game.

Definition 7. A positional strategy in P = (𝑉, 𝑣0, A,𝑚, 𝜇,𝑐) is a function 𝑓 : 𝑉 → A. We write *PosStr*(P) for the set of all positional strategies in P.

Positional determinacy in the context of (classical) turn-based
2-player parity games means that players can pick an action based solely on the current vertex of the game. In contrast, the quantification over strategies in CPGs can have multiple alternations, the strategy for each player thus depends on the current vertex of the game and the action selected by all strategies quantified before it. We will represent the existentially quantified strategies using Skolem functions (known, e.g., from first-order logic and sometimes called *dependence map* [45]) that get the actions selected by strategies quantified earlier as an explicit input.

Definition 8. A positional𝑘-Skolem strategy CPG P = (𝑉, 𝑣0, A,
𝑚, 𝜇,𝑐) is a function 𝜁 : 𝑉 × A𝑘 → A. We write SkoStr(P,𝑘) for the set of positional 𝑘-Skolem strategies in P.

A positional 𝑘-Skolem strategy 𝜁 can pick an action based on the current vertex of the game and 𝑘 actions that have been selected previously. The intuition is that the strategy for player (or strategy variable) 2𝑘 (which is existentially quantified) can observe the actions selected by the 𝑘-universally quantified strategies before it.

Definition 9. Assume 𝒆 *is a function that maps each* 𝑘 ∈ [𝑚]
to a positional 𝑘-Skolem strategy in P *and let* 𝒐 : [𝑚] → *PosStr*(P)
map each each 𝑘 ∈ [𝑚] to a positional strategy in P. We combine 𝒆
and 𝒐 into a mapping *com*(𝒆, 𝒐) : [2𝑚] → *Str*(P) as follows. For a path 𝑢 ∈ 𝑉 +, we define *last*(𝑢) ∈ 𝑉 as the last vertex in 𝑣. For an odd index 2𝑘 − 1 we then define com(𝒆, 𝒐)(2𝑘 − 1) : 𝑉 + → A as com(𝒆, 𝒐)(2𝑘 − 1)(𝑢) := 𝒐(𝑘)�*last*(𝑢)�
For an even index 2𝑘 we define com(𝒆, 𝒐)(2𝑘) : 𝑉 + → A as com(𝒆, 𝒐)(2𝑘)(𝑢) := 𝒆(𝑘)�last(𝑢), (𝒐(1)(last(𝑢)),
𝒐(3)(last(𝑢)),
. . . ,
𝒐(2𝑘 − 1)(*last*(𝑢)))�.

The idea of *com*(𝒆, 𝒐) is to combine the Skolem strategies in 𝒆
and the positional strategies in 𝒐 into a strategy for each player. For odd player we simply take the strategy given by 𝒐 (applying it to the last vertex in the given sequence). For even players, we query the Skolem strategy given by 𝒆 and provide it with the actions that all universally quantified (odd) strategies before it have selected.

We can now state that CPG are positionally determined by making use of Skolem functions:

Proposition 4 ([40]).: _Let $\mathcal{P}=(V,v_{0},\mathbb{A},m,\mu,c)$ be a CPG. We have that $\mathcal{P}$ is won by the existential players if and only if_

$$\begin{array}{c}\includegraphics[]{142.26378pt}\end{array}$$

$$\begin{array}{c}\includegraphics[]{142.26378pt}\end{array}$$

$$\begin{array}{c}\includegraphics[]{142.26378pt}\end{array}$$

$$\begin{array}{c}\includegraphics[]{142.26378pt}\end{array}$$

_where $\boldsymbol{e}(k):=\zeta_{k}$ and $\boldsymbol{o}(k):=f_{k}$ for $k\in[m]$._

Proposition 4 states that instead of following the quantifier prefix as in Definition 6 we can instead quantify over Skolem functions $\zeta_{1},\ldots,\zeta_{m}$ for all existentially quantified variables. Put informally, the proposition thus states that existentially quantified strategies only need to know the current vertex and all actions selected by universally quantified strategies quantified before it. A proof Proposition 4 follows directly from the the construction in [40, Thm. 4.1].

## D.5 The Second Implication

Using Proposition 4 we can now prove:
Proposition 5. PΠ is won by the existential team if and only if zip(Π) ∈ L(B).

We prove both directions of Proposition 5 separately (in Lemmas 11 and 12).

Lemma 11. If PΠ is won by the existential team then *zip*(Π) ∈
L(B).

Proof. Assume that $\mathcal{P}_{\Pi}$ is won by the existential player. Using Proposition 4 we thus get positional skeleton functions $\zeta_{1},\ldots,\zeta_{m}$ such that for

$$\bigvee_{k\in[m]}f_{k}\in\mathit{PosStr}(\mathcal{P}).\;\mathit{even}\Big{(}\mathit{Play}_{\mathcal{P}_{\Pi}}(v_{0},\prod_{k\in[2m]}\mathit{com}(\boldsymbol{e},\boldsymbol{o})(k)\Big{)}\tag{5}$$

where $\boldsymbol{e}(k):=\zeta_{k}$ and $\boldsymbol{o}(k):=f_{k}$ for $k\in[m]$.

We use the Skolem functions to construct an accepting run DAG $\mathbb{D}$ of $\mathcal{B}$ on $\mathit{zip}(\Pi)$. We construct $\mathbb{D}$ iteratively. We begin with a DAG that consist of the single node $((q_{0},\dot{s}),0)$, i.e., we start with the  unique initial state of $\mathcal{B}$ (note that by definition of run DAGs, nodes are indexed by their current depth, cf. Appendix A). Now assume that there exists some node that we have not visited. Let this note be $((q,s),N)$. We observe that $(q,s,N)$ is a vertex in $\mathcal{P}_{\Pi}$.

The Nth input read by $\mathcal{B}$ on $zip(\Pi)$ is $zip(\Pi)(N)$. By definition of $\mathcal{B}$ the transition function from $(q,s)$ on the Nth input is

$$\delta^{\prime}\big{(}(q,s),zip(\Pi)(N)\big{)}=\bigwedge_{a_{1}\in\mathbb{A}}\bigvee_{a_{2}\in\mathbb{A}}\cdots\bigvee_{a_{2m}\in\mathbb{A}}(q^{\prime},s^{\prime})\tag{6}$$

where $q^{\prime}=\delta(q,zip(\Pi)(N)[\pi\mapsto s])$ and $s^{\prime}=\kappa\big{(}s,\prod_{i\in Agts}a_{\overline{x}\,(i)}\big{)}$.

We need to add children of the node $((q,s),N)$ that full the above formula. We will construct a set $Y\subseteq Q\times S$ that is a model for the above, i.e., $Y\models\delta^{\prime}\big{(}(q,s),zip(\Pi)(N)\big{)}$. We will construct $Y$ by following all the action selection in the prefix of $\delta^{\prime}\big{(}(q,s),zip(\Pi)(N)\big{)}$ and construct an intermediate set of functions $Z\subseteq([2m]\rightharpoonup\mathbb{A})$. We can think of $Z$ as combinations of actions $a_{1},\ldots,a_{2m}$ that we set 

and construct an intermediate set of functions 𝑍 ⊆ ([2𝑚] ⇀ A).
We can think of 𝑍 as combinations of actions 𝑎1, . . . ,𝑎2𝑚 that we se-
lect in the prefix of Eq. (6). This set 𝑍 is constructed in accordance
with the Skolem functions 𝜁1, . . . ,𝜁𝑚, i.e., for every disjunctive
choice we will selected the action that is picked by the respective
Skolem function. Initially, we set 𝑍 = {{}} as the singleton set
containing only the empty function {} : [2𝑚] ⇀ A. For every 𝑘
from 1 to 2𝑚 we do the following: If 𝑘 is odd, so action 𝑎𝑘 is cho-
sen conjunctively we add all possible actions. That is, we update
𝑍 := {�𝑎[𝑘 ↦→ 𝑎] | �𝑎 ∈ 𝑍,𝑎 ∈ A}. If 𝑘 is even, so 𝑘 = 2𝑘′ for some
𝑘′, we can pick one action for 𝑘 for each element in 𝑍. Given �𝑎 ∈ 𝑍
(so �𝑎 is a function {1, . . . ,𝑘 − 1} → A) we define the action 𝑎 �𝑎 as

𝑎 �𝑎 := 𝜁𝑘′ �(𝑞,𝑠, 𝑁), (�𝑎(1), �𝑎(3), . . . , �𝑎(2𝑘′ − 1))�.

𝑖∈Agts �𝑎(�𝑥(𝑖))�. We then define

That is, we use the 𝑘′th Skolem functions and query it with the
current vertex (𝑞,𝑠, 𝑁) and the action selected by all previously
chosen conjunctive action choices (at odd positions) in �𝑎. We then
update 𝑍 := {�𝑎[𝑘 ↦→ 𝑎 �𝑎] | �𝑎 ∈ 𝑍}.
  After repeating this procedure, we have constructed a set 𝑍 ⊆
([2𝑚] → A) that maps all players to actions. Informally, this corre-
sponds to a possible assignment of the actions selected in the prefix
of 𝛿′�(𝑞,𝑠), zip(Π)(𝑁)�. For each �𝑎 ∈ 𝑍 we can define a unique 𝑠 �𝑎
by following the construction in the definition of B. That is, we
define 𝑠 �𝑎 = 𝜅�𝑠, �

𝑌 :=
   ��𝛿(𝑞, zip(Π)(𝑁)[𝜋 ↦→ 𝑠]),𝑠 �𝑎
                         � | �𝑎 ∈ 𝑍
                               �
                                .

It is easy to see that 𝑌 |= 𝛿′�(𝑞,𝑠), zip(Π)(𝑁)�: In the selection of
actions (when constructing 𝑍) we have consider all possible actions
for each conjunctive choice and picked a particular action for each
disjunctive choice.
  In our run DAG we now add a node ((𝑞′,𝑠′), 𝑁 + 1) for each
(𝑞′,𝑠′) ∈ 𝑌, and add an edge from ((𝑞,𝑠), 𝑁) to ((𝑞′,𝑠′), 𝑁 + 1).
  Let D be the infinite DAG obtained by following this construction.
It is easy to see that D is a valid run of B on zip(Π) (as we have
argued above all children that we add to any given node satisfy the
transition formula).
  It remains to argue that D is accepting. For this we consider an
arbitrarily infinite path 𝜏 in D, s.t.,

𝜏 = ((𝑞0,𝑠0), 0)((𝑞1,𝑠1), 1)((𝑞2,𝑠2), 2) · · ·

We define an analogous path in PΠ as follows (by simply regrouping
parenthesis):

$$\tau^{\prime}=(q_{0},s_{0},0)(q_{1},s_{1},1)(q_{2},s_{2},2)\cdots.$$

In construction $\mathbb{D}$, we always mimicked the choice for each distinctively chosen action by using the Skolem functions $\zeta_{1},\ldots,\zeta_{m}$. We thus get that $\tau^{\prime}$ is a play in $\mathcal{P}_{\Pi}$ under these Skolem functions: That is, there exist $f_{1},f_{2},\ldots,f_{m}\in\mathit{P}\mathit{o}\mathit{S}tr(\mathcal{P}_{\Pi})$ such that

$$\mathit{Play}_{\mathcal{P}_{\Pi}}(v_{0},\prod_{k\in[2m]}com(\boldsymbol{e},\boldsymbol{o})(k))=\tau^{\prime}$$

where $\boldsymbol{e}(k):=\zeta_{k}$ and $\boldsymbol{o}(k):=f_{k}$ for $k\in[m]$. By the choice of $\zeta_{1},\ldots,\zeta_{m}$ (cf. Eq. (5)) we thus get that $even(\tau^{\prime})$.

Now the sequence of colors traversed in $\tau^{\prime}$ is the same as the sequence of colors in the path $\tau$ in the run DAG. The minimal color that appears infinitely often in $\tau$ is thus also even and so the path is accepting. As this holds for all paths, $\mathbb{D}$ is accepting.

We have constructed an accepting run DAG of $\mathcal{B}$ on $zip(\Pi)$, so $zip(\Pi)\in\mathcal{L}(\mathcal{B})$ as required.

Lemma 12. If *zip*(Π) ∈ L(B) then PΠ is won by the existential team.

(7)

Proof. Assume that $zip(\Pi)\in\mathcal{L}(\mathcal{B})$, and let $\mathbb{D}$ be an accepting run DAG of $\mathcal{B}$. We will use this DAG to construct Skolem functions $\zeta_{1},\ldots,\zeta_{m}$ such that

$$\bigvee_{k\in[m]}f_{k}\in\mathit{PosStr}(\mathcal{P}).\,\mathit{even}\Big{(}\mathit{Play}_{\mathcal{P}_{\Pi}}(v_{0},\prod_{k\in[2m]}com(\boldsymbol{e},\boldsymbol{o})(k))\Big{)}\tag{7}$$

where $\boldsymbol{e}(k):=\zeta_{k}$ and $\boldsymbol{o}(k):=f_{k}$ for $k\in[m]$. By Proposition 4 this would imply that $\mathcal{P}_{\Pi}$ is won by the existential team.

For any node $x=((q,s),N)$ in the run DAG $\mathbb{D}$, the children of $((q,s),N)$ satisfy 
�
𝑎1∈A

$$\begin{array}{c}\bigvee\cdots\bigvee(q^{\prime},s^{\prime})\\ a_{1}\in\mathbb{A}\quad a_{2m}\in\mathbb{A}\end{array}$$
𝛿′�(𝑞,𝑠), *zip*(Π)(𝑁)� =
�
where 𝑞′ = 𝛿(𝑞, *zip*(Π)(𝑁)[𝜋 ↦→ 𝑠]) and 𝑠′ = 𝜅�𝑠, �
𝑖∈*Agts* 𝑎 �𝑥 (𝑖)
�.

We will construct functions 𝛼𝑥
1 *, . . . , 𝛼*𝑥𝑚 where 𝛼𝑥
𝑘 : A𝑘 → A that will pick a choice for each disjunction based on the previous choices for each conjunction. We first define 𝛼𝑥
1 : A → A: For any 𝑎1 ∈ A
we define 𝛼𝑥
1 (𝑎1) by *fixing* the first conjunctively chosen action 𝑎1
in Eq. (8) to be 𝑎1. As 𝑎1 was chosen conjunctivley, the children of
𝑥 = ((𝑞,𝑠), 𝑁) still satisfy Eq. (8) with 𝑎1 fixed to 𝑎1. Now define
𝑎2 ∈ A as some valid choice for the (disjunctively chosen) 𝑎2. That is, we define 𝑎2 such that the children of 𝑥 = ((𝑞,𝑠), 𝑁) in D still form a model of Eq. (8) with actions 𝑎1 := 𝑎1,𝑎2 := 𝑎2 fixed. We set
𝛼𝑥
1 (𝑎1) := 𝑎2. After having defined 𝛼𝑥
1 we can define 𝛼𝑥
2 (𝑎1,𝑎3): We fix the first conjunctively chosen action be𝑎1, the second disjunctive action be 𝛼𝑥
1 (𝑎1) and the second conjunctive action be 𝑎3, and the define 𝛼𝑥
2 (𝑎1,𝑎3) as some action that we can select for the second disjunctive choice such that the children of 𝑥 = ((𝑞,𝑠), 𝑁) in D
satisfy the subformula with those actions fixed. The construction of the remaining 𝛼𝑥
1 *, . . . , 𝛼*𝑥𝑚 is analogous. Intuitively, each 𝛼𝑥
𝑘 serves as a Skolem function for the 𝑘th disjunctive action by fixing an action based solely on the earlier conjunctive actions. Together they guarantee that by following the selected action by each Skolem function for each disjunctive choice, we always reach some child of 𝑥 = ((𝑞,𝑠), 𝑁) in D.

We can now define the desired positional Skolem functions
𝜁1*, . . . ,𝜁*𝑚 for PΠ. We define 𝜁𝑘 as follows: Given any vertex 𝑣 =
(*𝑞,𝑠, 𝑁*) in PΠ and actions 𝑎1*, . . . ,𝑎*𝑘 ∈ A (corresponding to the actions selected by all universally quantified strategies before 2𝑘) we check if 𝑥 := ((𝑞,𝑠), 𝑁) is a node in D. If there does not exists such a node we can return an arbitrary action (we will later argue that this situation will never be reached in any play PΠ). Otherwise 𝑥 is a node in D and we get the Skolem functions 𝛼𝑥
1 *, . . . , 𝛼*𝑥𝑚 we have constructed earlier. We define 𝜁𝑘 (𝑣, (𝑎1, . . . ,𝑎𝑘)) := 𝛼𝑥
𝑘 (𝑎1*, . . . ,𝑎*𝑘), i.e., we select the action that 𝛼𝑥
𝑘 picks for the 𝑘th disjunction when using the actions 𝑎1*, . . . ,𝑎*𝑘 for the previous 𝑘 conjunctions.

It remains to argue that the Skolem functions 𝜁1*, . . . ,𝜁*𝑚 fulfill Eq. (7). Let 𝑓1, . . . .𝑓𝑚 ∈ *PosStr*(PΠ) and consider the resulting play

𝜏 = *Play*PΠ �𝑣0, � 𝑘∈[2𝑚] com(𝒆, 𝒐)(𝑘)� = (𝑞0,𝑠0, 0)(𝑞1,𝑠1, 1)(𝑞2,𝑠2, 2) · · ·
where 𝒆(𝑘) := 𝜁𝑘 and 𝒐(𝑘) := 𝑓𝑘 for 𝑘 ∈ [𝑚]. We consider the equivalent path in the run DAG (by regrouping parenthesis):

𝜏′ = ((𝑞0,𝑠0), 0)((𝑞1,𝑠1), 1)((𝑞2,𝑠2), 2) · · · .
By construction of 𝜁1*, . . . ,𝜁*𝑚 we always pick the actions that are disjunctively chosen in accordance with D. It is therfore easy to see that 𝜏′ is an infinite path in D. By the assumption that D is accepting the minimal color that appears infinitely often is even.

As the automaton state sequence agrees with that of 𝜏, we thus get that *even*(𝜏) holds. So 𝜁1*, . . . ,𝜁*𝑚 satisfy Eq. (7). By Proposition 4 this implies that PΠ is won by the existential team, as required.

□
By Proposition 3, we get that Π satisfies Eq. (3) iff PΠ is won by the existential team (Proposition 3). By Proposition 5, PΠ is won by the existential team iff *zip*(Π) ∈ L(B). Consequently, Π
satisfies Eq. (3) iff *zip*(Π) ∈ L(B), proving Lemma 9 and thus of Proposition 2.

## E Details On The Section 7

In this section, we provide additional details on the formulas checked in Section 7.

## E.1 Details On Section 7.1

We check the following HyperSL[SPE] formula:
∃𝑥. ∀𝑥1, . . . ,𝑥𝑛.

� 𝑛
�

𝑖=1
     G �⟨wt,𝑖⟩𝜋 → F ¬⟨wt,𝑖⟩𝜋
                                               �
                                                �

[𝜋 : (𝑠𝑐ℎ𝑒𝑑 ↦→ 𝑥,𝑦1 ↦→ 𝑥1, . . . ,𝑦𝑛 ↦→ 𝑥𝑛)]

This formula states that the scheduling agent sched has a strategy
such that none of the working agents 𝑦1, . . . ,𝑦𝑛 starves, i.e., when-
ever agent 𝑦𝑖 waits for a grant (modeled by proposition ⟨wt,𝑖⟩), it
will eventually not wait any more. Note that this formula is equiv-
alent to the SL[1G] specification used by Cermák et al. [23]. We
check it for various values of 𝑛 ∈ N and give the results in Table 1.

## E.2 Details On Section 7.2

In Section 7.2, we check random formulas from a range of different families. We assume we are given a CGS G over atomic proposition AP and agents *Agts* (These CGS are obtained automatically from the ISPL models from [39]).

Security (Sec). We select some agent 𝑖 ∈ *Agts* and some AP
𝑔 ∈ AP modeling a goal, an AP ℎ ∈ AP modelling a high-security input, and an AP 𝑜 ∈ AP modeling an observable output. We then construct the following HyperSL[SPE] formula:
∃𝑥. ∀𝑦1, . . . ,𝑦𝑖−1,𝑦𝑖+1, . . . ,𝑦𝑛. ∃𝑧1, . . . ,𝑧𝑛.

$$(\mathsf{F}\,g_{\pi}\wedge\mathsf{G}(o_{\pi}\leftrightarrow o_{\pi^{\prime}})\wedge\mathsf{F}(h_{\pi}\leftrightarrow h_{\pi^{\prime}}))$$ $$\begin{bmatrix}\pi:(y_{1},\ldots,y_{i-1},x,y_{i+1},\ldots,y_{n})\\ \pi^{\prime}:(z_{1},\ldots,z_{n})\end{bmatrix}$$

This formula states that $i$ has a strategy to eventually reach $g$. Moreover, it may not leak all information about $h$ via $o$. We model this using the idea of non-inference [43]. The idea is that the behavior in $o$ should not leak $h$, so there must be "plausible denomibility". That is, the same observation via $o$ is also possible for some different input sequence via $h$.

Concretely, $i$ should be able to reach $g$ on path $\pi$ no matter what the other agents play. In addition, there must exists some path $\pi^{\prime}$ (which we state by quantifying the strategies of all agents existentially), that has the same observations $\mathsf{G}(o_{\pi}\leftrightarrow o_{\pi^{\prime}})$ but a different high-security input $(\mathsf{F}(h_{\pi}\leftrightarrow h_{\pi^{\prime}}))$.

Good-Enough Synthesis (GE). In many situations, asking for a strategy that wins in all situations is too restrictive. Instead, it often suffices to look for strategies that are *good-enough* (GE), i.e., strategies that win on every possible input sequence for which there exists a winning output sequence [1, 3]. We can express this formally using HyperSL[SPE]. Concretely, assume that 𝜑 =
Q1𝑥1*, . . . ,* Q𝑚𝑥𝑚.𝜓 [𝜋 : �𝑥] is any HyperSL formula over a single path variable (or, equivalently, a SL[1G] formula). We want to express that that 𝜑 only needs to holds on traces with input 𝑖 ∈ AP, on which some path with the same input actually satisfies 𝜓.

We can express that 𝜑 is a GE-strategy as follows:

$$\mathbb{Q}_{1}x_{1},\ldots,\mathbb{Q}_{m}x_{m}.\,\forall y_{1},\ldots,y_{m}.$$ $$(\mathbb{G}(i_{\pi}\leftrightarrow i_{\pi^{\prime}})\wedge\psi[\pi^{\prime}/\pi])\to\psi$$

where we write $\psi[\pi^{\prime}/\pi]$ for the formula with all occurrences of $\pi$ replaced with $\pi^{\prime}$.

In the formula, we quantify over strategies $x_{1},\ldots,x_{m}$ as in $\varphi$ and use these strategies to construct path $\pi$. Afterwards, we universally quantify over any path $\pi^{\prime}$ in the system by picking strategies $y_{1},\ldots,y_{n}$ for all agents. We then state that $\psi$ only needs to hold on $\pi$ provided $\pi^{\prime}$ has the same input and satisfies $\psi$. Phased differently, $\pi$ only needs to win, provided some path with the same inputs can ensure $\psi$. Note that, depending on the prefix in $\varphi$, this is not expressible in weaker hyperlogics such as HyperATL${}^{*}$ and HyperATL${}^{*}_{S}$.

Random (Rnd). For the random category, we use a random LTL
formula (sampled using spot [30]) and add a prefix of quantifiers to yield a HyperSL[SPE] formula.