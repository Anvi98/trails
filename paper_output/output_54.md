# Can Large Language Models Explore In-Context?

Akshay Krishnamurthy∗1, Keegan Harris†2, Dylan J. Foster1, Cyril Zhang1, and Aleksandrs Slivkins∗1
1Microsoft Research
2Carnegie Mellon University March 2024

## Abstract

We investigate the extent to which contemporary Large Language Models (LLMs) can engage in *exploration*, a core capability in reinforcement learning and decision making. We focus on native performance of existing LLMs, without training interventions. We deploy LLMs as agents in simple *multi-armed bandit* environments, specifying the environment description and interaction history entirely *in-context*, i.e., within the LLM prompt. We experiment with Gpt- 3.5, Gpt-4, and Llama2, using a variety of prompt designs, and find that the models do not robustly engage in exploration without substantial interventions: i) Across all of our experiments, only one configuration resulted in satisfactory exploratory behavior: Gpt-4 with chainof-thought reasoning and an externally summarized interaction history, presented as sufficient statistics; ii) All other configurations did not result in robust exploratory behavior, including those with chain-of-thought reasoning but unsummarized history. Although these findings can be interpreted positively, they suggest that external summarization—which may not be possible in more complex settings—is important for obtaining desirable behavior from LLM agents. We conclude that non-trivial algorithmic interventions, such as fine-tuning or dataset curation, may be required to empower LLM-based decision making agents in complex settings.

## 1 Introduction

In-context learning is an important emergent capability of Large Language Models (LLMs) that enables one to use a pre-trained LLM to solve a problem by specifying the problem description and relevant data entirely *in-context*, i.e., within the LLM prompt, with no updates to the LLM
parameters (Brown et al., 2020). For example, one can prompt an LLM with numeric covariate vectors and scalar targets and subsequently obtain regression-style predictions from the model by including new covariate vectors in the prompt (Garg et al., 2022). Perhaps surprisingly, LLMs are not explicitly trained for this behavior; instead the underlying algorithms employed for in-context learning are extracted from the training corpus and *emerge* at scale.

Since its discovery in the Gpt-3 model (Brown et al., 2020), in-context learning has been the subject of a growing body of research. These works include theoretical investigations into the underlying mechanisms (e.g., Xie et al., 2021; Aky¨urek et al., 2022), empirical probes (e.g., Garg et al., 2022; Kirsch et al., 2022), and works leveraging in-context learning in applications (e.g., Xu et al.,
2022; Som et al., 2023; Edwards et al., 2023). This literature predominantly studies in-context learning for prediction or supervised learning tasks, and while theoretical progress is in its infancy, our understanding of how to use *in-context supervised learning* (ICSL) in practice is rapidly taking shape.

Although supervised learning is an important capability, many applications demand the use of ML models for downstream *decision making*. Thus, *in-context reinforcement learning* (ICRL)
and sequential decision making is a natural next frontier. LLMs are already being used as decision making agents in applications ranging from experimental design in the natural sciences (Lee et al., 2023b) to game playing (Shinn et al., 2023; Wang et al., 2023), but our understanding—theoretically and operationally—of ICRL is far less developed than for ICSL. To date, we lack a systematic understanding as to whether LLMs can be considered general-purpose decision making agents.

Decision making agents must possess three core capabilities: *generalization* (required for supervised learning), *exploration* (making decisions that may be suboptimal in the short term for the sake of gathering more information) and *planning* (to account for long-term consequences of decisions). In this paper, we focus on exploration, the capability to deliberately gather information in order to evaluate alternatives and reduce uncertainty. A recent series of papers (Laskin et al., 2022; Lee et al., 2023a; Raparthy et al., 2023) demonstrates in-context reinforcement learning behavior (including exploration) in transformer models when they are *explicitly trained* to produce this behavior using data from reinforcement learning agents or expert demonstrations on related tasks. Such training tends to be laborious, expensive, and possibly task-specific. In particular, these findings do not shed light into whether exploratory behavior manifests in general-purpose LLMs obtained via standard training methods, which suggests the following basic question:
Do contemporary LLMs exhibit the capability to explore in-context?

Contributions. We investigate this question by deploying LLMs as agents in simple synthetic reinforcement learning problems, namely *multi-armed bandits (MABs)* (Slivkins, 2019; Lattimore and Szepesv´ari, 2020), specifying the environment description and interaction history entirely within the LLM prompt. Multi-armed bandits are a classical and well-studied type of RL problem that isolates the tradeoff between exploration and *exploitation*, i.e., making the best decision given the available data.

They are also a fundamental building block toward general sequential decision making; the ability to solve MABs is a prerequisite for more challenging reinforcement learning tasks. Their simplicity, centrality to RL, and focus on exploration versus exploitation make MABs a natural choice for systematically studying the in-context exploration abilities of LLMs.

We evaluate the in-context exploration behavior of Gpt-3.5 (Brown et al., 2020), Gpt-4 (OpenAI, 2023), and Llama2 (Touvron et al., 2023) in MAB environments, using a variety of prompt designs. In our experiments, we find that only a single configuration (i.e., a prompt design and LLM pair) results in satisfactory exploratory behavior. All other configurations exhibit exploration failures, failing to converge to the best decision (arm) with significant probability. We find that typically this happens due to *suffix failures*, where the LLM fails to select the best arm even once after some initial rounds (i.e., in some "time suffix"). This scenario is reflected in Figure 1(a): in particular, Gpt-4 with our basic prompt design experiences a suffix failure in > 60% of the replicates. An alternative failure mode we identify is where the LLM behaves "uniformly", selecting all arms near-equally often and failing to narrow down to the better ones.

The single configuration thato succeeds in our experiments involves a combination of Gpt-4 and an "enhanced" prompt that (a) provides a suggestive hint to explore, (b) externally summarizes the history of interaction into per-arm averages, and (c) asks the LLM to use zero-shot chain-of-thought reasoning (Wei et al., 2022; Kojima et al., 2022). This configuration is visualized in Figure 1(b). One can interpret this finding positively: state-of-the-art LLMs do possess the capability to robustly explore, provided that the prompt is carefully designed to elicit this behavior.

On the other hand, we find that the same configuration without external summarization fails, which leads to a negative interpretation: LLMs may fail to explore in more complex environments, where externally summarizing the history is a non-trivial algorithm design problem.1
We conclude that while the current generation of LLMs can perhaps explore in simple RL
environments with appropriate prompt engineering, training interventions—in the spirit of Lee et al. (2023a); Raparthy et al. (2023)—may be required to endow LLMs with more sophisticated exploration capabilities required for more complex settings. Methodology. An underlying technical challenge in assessing LLM capabilities and limitations is that one must search a combinatorially large space of prompt designs while obtaining statistically meaningful results, all while meeting the financial and computational constraints associated with LLMs. Assessing in-context bandit learning is even more challenging because (a) stochasticity in the environment demands a high degree of replication for statistical significance and (b) the sample complexity of learning/exploration demands that even a single experiment involve hundreds or thousands of LLM queries to obtain meaningful effect sizes (i.e., separation between successful and failing methods). To address these issues, our core technical contribution is to identify surrogate statistics as diagnostics for long-term exploration failure.

The surrogate statistics we consider characterize long-term exploration failure, yet can be measured at moderate scale with few replicates and short learning horizons, even when the standard performance measure (namely, reward) is too noisy to be useful.

## 2 Experimental Setup

Multi-armed bandits (MAB). We consider a basic multi-armed bandit variant, stochastic Bernoulli bandits.

There are K possible actions (*arms*), indexed as [K] := {1*, . . . , K*}.

Each arm a is associated with mean reward µa ∈ [0, 1], which is unknown. An agent interacts with the environment for T time steps, where in each time step t ∈ [T] the agent selects an arm at ∈ [K]
and receives a reward rt *∈ {*0, 1} drawn independently from a Bernoulli distribution with mean µat.

Thus, the MAB instance is determined by the mean rewards (µa : a ∈ [K]) and the time horizon T. The goal is to maximize the total reward, which roughly corresponds to identifying the best arm: an arm with the highest mean reward. A key feature of the MAB setup is that rewards for arms not chosen by the agent are not revealed, so exploration is necessary to identify the best arm.

We focus on MAB instances where the best arm has mean reward µ⋆ = 0.5+∆/2 for a parameter
∆ > 0, while all other arms have mean reward µ = 0.5−∆/2 (so, ∆ = µ⋆−µ is the *gap* between the best and the second-best arm). The main instance we consider has K = 5 arms and gap ∆ = 0.2.

We call this the hard instance, as we also consider an easy instance with K = 4 and ∆ = 0.5.2
Prompts. We employ LLMs to operate as decision making agents that interact with MAB instances by prompting them with a description of the MAB problem (including the time horizon T) and the history of interaction thus far. Our prompt design allows several independent choices. First is a "scenario", which provides a grounding for the decision making problem, positioning the LLM either a) as an agent choosing *buttons* to press, or b) as a recommendation engine displaying advertisements to users. Second, we specify a "framing" as either a) explicitly *suggestive* of the need to balance exploration and exploitation, or b) *neutral*. Third, the history can be presented
(a) Top row.

Gpt-4 with our basic prompt design with zero temperature.

The experiment runs for T = 500 rounds, and is replicated N = 20 times, varying environment randomness. This configuration exhibits highly bimodal behavior: a large (> 60%) fraction of replicates choose the best arm only a handful of times and exhibit suffix failures, similar to Greedy, and very unlike UCB and TS. This is suggestive of a long term failure to explore and, indeed, this configuration underperforms substantially in terms of reward. (b) Bottom row. Gpt-4 with a suggestive framing, summarized history, and chain-of-thought with zero temperature. The experiment runs for T = 200 rounds and is replicated N = 40 times.

This configuration exhibits a unimodal distribution of plays of the best arm, very few suffix failures, and reward that is comparable to TS. as a) a *raw* list over rounds, or it can b) be *summarized* via number of plays and average rewards of each arm. Fourth, the requested final answer can be a) a single *arm*, or b) a distribution over arms. Finally, we either a) request the answer only, or b) also allow the LLM to provide a
"chain-of-thought" (CoT) explanation. Altogether, these choices lead to 25 = 32 prompt designs, illustrated in Figure 2. More details about the prompt design, including examples, are provided in Appendix A.

The most basic prompt design from the options above uses the buttons scenario, neutral framing, and raw history, and requests the LLM to return only an arm with no CoT. Each of the five possible modifications to this prompt can potentially help the LLM, and our experiments evaluate this. For example, both the advertising scenario and suggestive framing might help invoke the LLM's knowledge of bandit algorithms (as bandit algorithms are commonly used in content recommendation). History summarization might help if the LLM cannot reliably summarize history itself (perhaps due to arithmetic errors3) and/or does not fully realize that it should. Returning a distribution might help if the LLM can identify a good distribution, but fails to correctly sample from it. Finally, chain-of-thought is known to help in a wide variety of LLM scenarios (Wei et al.,
2022; Malach, 2023), even when used in a zero-shot manner (Kojima et al., 2022) as we do here.

Prompts are presented to each LLM using both system and user messages (exposed by all three LLM APIs). The system message presents information about the scenario and framing and prompts the LLM about whether to use CoT and whether (and how) to return a distribution.

The user message presents the history and reminds the LLM about how to format its response.

For Gpt-4 only, we found that prompting the LLM to use CoT in the system prompt did not reliably elicit CoT outputs, so— for Gpt-4 only—we also consider a reinforced CoT prompt design that additionally reminds the LLM to use CoT at the end of the user prompt. See Appendix A for examples.

Figure 2: Prompt designs; see Figure 11 for a more detailed view.

A prompt is generated by traversing the graph from top to bottom.

LLM configurations.

We experiment with three LLMs: Gpt-3.5, Gpt-4, and Llama2.4
In addition to the prompt variations above, we also consider two choices for the temperature parameter, 0 and 1. A temperature of 0 forces the LLM to be deterministic and therefore isolates the "deliberate" exploration behavior of the LLM itself. A temperature of 1 provides a source of external randomness in the LLM responses, which may or may not result in randomization among the arms. Allowing the LLM to return a distribution instead of a single arm also provides external randomness (as we sample from the returned distribution); to isolate sources of randomness, we do not consider temperature 1 with "return distribution" prompt designs.

We refer to the tuple (prompt design, temperature) as the *LLM configuration*. We identify each configuration with a 5-letter "code" L1L2L3L4L5, with letters Li denoting the choices:

- L1: 'B' or 'A' for, resp., buttons or advertisements scenario; - L2: 'N' or 'S' for, resp., neutral or suggestive framing;
- L3: 'R' or 'S' for, resp., raw or summarized history;
- L5: '0', '1' or 'D' for, resp., temperature and returning a distribution (with temperature 0).
- L4: 'C' or '�C' or 'N' for, resp., chain-of-thought, reinforced CoT, or no CoT.
We refer to "BNRN0" as the *basic* configuration going forward. Most of our experiments consider the "buttons" scenario, and we use the "advertisements" scenario primarily as a robustness check.

For Gpt-3.5 and Llama2, we do not consider reinforced CoT as it is not required to reliably elicit CoT outputs; thus, we have 48 configurations total for these two LLMs. For Gpt-4, we primarily used reinforced CoT, but did experiment with some standard CoT prompt designs; thus, there are 72 configurations total for Gpt-4.

Baselines.

For baselines, we consider two standard MAB algorithms, UCB (Auer et al., 2002)
and Thompson Sampling (TS) (Thompson, 1933), which are optimal in a certain theoretical sense and also reasonably effective in practice. We also consider the Greedy algorithm, which does not explore and is known to fail.5 While all three baselines have tunable parameters, we perform no parameter tuning (see Section 4.1 for a detailed description of each algorithm with parameter settings). In addition to these baselines, some of our experiments include the the ϵ-Greedy algorithm6 with various choices of ϵ to quantitatively demonstrate tradeoffs between exploration and exploitation. We ran 1000 replicates for each baseline and each MAB instance (with rewards realized independently across the replicates). Scale of the experiments. Our main set of experiments has time horizon T = 100. To account for randomness in rewards (and possibly in the LLM, via temperature) we ran N *∈ {*10, 20} replicates for each LLM configuration and each bandit instance, with rewards generated independently across the replicates. As a robustness check, we ran a single experiment on Gpt-4 with the basic configuration for T = 500 rounds (with N = 20), and obtained consistent/stronger conclusions, depicted in Figure 1(a).

In more detail, for Gpt-3.5 we used N = 20 replicates across all 48 prompt configurations, resulting in ≈ 200K queries in total. Gpt-4 was an order of magnitude more expensive, considerably slower on throughput, and subject to unpredictable throttling. As such, we only used N = 10
replicates across 10 representative prompt configurations.7 For additional robustness checks, we ran four Gpt-4 configurations with T = 200, two for N = 20 replicates and two for N = 40 replicates.

In total, this resulted in ≈50K queries issued to Gpt-4. Llama2 was essentially free from our perspective (since it was locally hosted), but its performance was consistently sub-par; we limited our experiments to the hard MAB instance, 32 configurations, and N = 10 replicates.

We emphasize that bandit experiments with LLMs are quite costly in terms of money and time.

They take N · T LLM queries for each LLM configuration and each MAB instance being tested.

Both N and T must be relatively large to obtain statistically meaningful results: N governs the significance level and must be large to overcome randomness in reward realizations, while T governs the effect size and must be large so that good algorithms have enough time to identify the optimal arm. Both issues are more pronounced in harder MAB instances (many arms K and/or small gap
∆), but exploration failures also tend to be less frequent in (very) easy MAB instances.8 Further, we need to cover the space of possible prompt designs, which is essentially infinitely large, to ensure that our findings do not overfit to one particular design. Thus, ideally we would take N, T, the number of MAB instances, and the number of prompts to be rather large, but doing so is not practically feasible.9 Instead, we use moderately small gap ∆ = 0.2, moderately large choices for N *∈ {*10, 20} and T = 100, and the prompt design space as described above.

As we will see below, these choices (specifically, N *∈ {*10, 20} and T = 100 and ∆ = 0.2) do not provide enough statistical power to distinguish between successful and unsuccessful methods based solely on accumulated rewards. In lieu of further increasing the scale of the experiments, which is not practically feasible, we rely on *surrogate statistics* which can be detected at our moderate scale, and which are highly suggestive of long-term/persistent exploration failures. Our robustness checks with larger T and N, as well as qualitative findings that we report below provide supporting evidence for this methodology.

## 3 Experimental Results

In this section, we present our experimental findings, beginning with a summary in Section 3.1. In Section 3.2 we investigate failing LLM configurations in detail, and in Section 3.3 we focus on the single successful LLM configuration our experiments identified. Finally, in Section 3.4 we attempt to diagnose the underlying causes for exploration failures.

## 3.1 Overview

We find that all but one of the LLM configurations we consider exhibit exploration failures, not converging to the best arm with significant probability. This happens either due to suffix failures, where the LLM never selects the best arm after a small number of initial rounds, or (in a smaller number of configurations) due to *uniform-like failures*, where the LLM selects all arms at an approximately uniform rate, failing to eliminate poorly performing arms. The only one exception is Gpt-4 with the BSS�C0 configuration, i.e., with the buttons scenario, suggestive framing, summarized history, reinforced CoT, and temperature 0.

We summarize our key findings in Figure 3 and Figure 4. Figure 3 summarizes the main set of experiments (which we recall consider the hard MAB instance), visualizing each LLM configuration with a single point on a scatter plot where the axes correspond to two *surrogate statistics*, SuffFailFreq and MinFrac, which represent the strength of the two failure modes (SuffFailFreq measures suffix failures, and K · MinFrac measures uniform-like failures); these statistics are described in detail in the sequel. Figure 4 displays SuffFailFreq, MinFrac, GreedyFrac (which measures how similar a method is to Greedy), and additional summary statistics for each of the Gpt-4

TS
UCB
Greedy
BNRN0
BNRN1
BNRND
BNRC0
BNSN0
BSRN0
BSSC0
BSSC1
BSSCD
BSSC0
MedianReward
0.47
0.55
0.40
0.63
0.70
0.33
0.35
0.60
0.45
0.68
0.28
0.37
0.47
SuffFailFreq(T/2)
0.01
0.02
0.48
0.50
0.40
0.00
0.50
0.60
0.70
0.30
0.20
0.00
0.00
K*MinFrac
0.28
0.18
0.05
0.03
0.04
0.41
0.09
0.07
0.05
0.09
0.19
0.49
0.33
GreedyFrac
0.62
0.76
1.00
0.52
0.46
0.45
0.78
0.99
0.59
0.93
0.88
0.49
0.69
Replicates
1000
1000
1000
10
10
10
10
10
10
10
10
10
10

configurations in the main set of experiments. These statistics reveal that all of the LLM configurations, except for Gpt-4-BSS�C0 (the blue star in Figure 3), behave fundamentally differently from the baseline algorithms UCB and TS, and we find that these differences result in a large, persistent drop in performance. Conversely, we find that Gpt-4-BSS�C0 successfully explores and
(as a result) converges to the best arm.

## 3.2 Identifying Failures

We now give a precise overview of the exploration failures illustrated in Figure 3 and Figure 4, and provide additional results and figures that illustrate failure in greater detail. We focus on Gpt-4, as we find that Gpt-3.5 and Llama2 perform worse (and often *much* worse) in all experiments;
detailed results for Gpt-3.5 and Llama2 are included in Appendix B for completeness. We begin with detailed background on the surrogate statistics, SuffFailFreq and MinFrac, used to quantify failures in Figures 3 and 4 and beyond, providing evidence that exploration failure—as quantified by these statistics—results in a persistent drop in performance. Suffix failures. Most of the LLM configurations we consider exhibit highly *bimodal* behavior, whereby a large fraction of the replicates choose the best arm very rarely, and a few replicates converge to the best arm extremely quickly. Consistent with this bimodal behavior, we observe a large incidence of *suffix failures*, where the best arm is not selected even once after a small number initial of rounds (i.e., in some "time suffix"). Suffix failures are suggestive of a long-term failure to explore which cannot be improved by running the algorithm for longer, because, without playing the optimal arm, one cannot acquire information to learn that it is indeed optimal. Such behaviors are qualitatively similar to those of Greedy and qualitatively very different from those of UCB
and Thompson Sampling.

Our surrogate statistic for measuring suffix failures is defined as follows: For an experiment replicate R and round t, let SuffFail(*t, R*) be a binary variable that is 1 if the best arm is never chosen in rounds [*t, T*]. Then let SuffFailFreq(t) := mean({SuffFail(*t, R*) : replicates R}). Suffix failures manifest in most of our experiments at T = 100. In the scatter plot in Figure 3, the X-axis plots SuffFailFreq(T/2) for each LLM configuration, and we find that all but five configurations have SuffFailFreq(T/2) ≥ 15%. Recalling the definition of suffix failures, this means that ≥ 15%
of the time, these configurations do not pull the best arm *even once* in the last half of the rounds.

A more detailed view of suffix failures and bimodal behavior can be obtained by focusing on individual LLM configurations.

We visualize this for the basic configuration (Gpt-4-BNRN0)
in Figure 1 (top) for T = 500, and in Figure 5 for Gpt-4 (BNRN0 and BNRN1) at T = 100.

In these detailed views, the middle panels plot SuffFailFreq(t) at each time t for the given LLM
configurations, as well as UCB, TS, and Greedy. We find that these LLM configurations have much higher suffix failure rates than both UCB and TS. Bimodal behavior is visualized in the left panel of each plot, where for each configuration, a large fraction of replicates rarely pulls the best arm, while the remaining fraction almost always pulls the best arm. Because of this bimodal behavior (particularly because a constant fraction of replicates by chance almost always pull the best arm), suffix failures are not fully reflected in the total reward plots in the right panels of Figure 5, since the time horizon T = 100 is not large enough. However, as mentioned, suffix failures are suggestive of an irrecoverable failure to explore which leads to stark differences in reward for larger T. This is precisely what we find at T = 500 in Figure 1, which suggests that suffix failures indeed lead to poor long-term performance. Uniform-like failures. Returning to the left panel of Figure 3, we see that three Gpt-4 configurations avoid suffix failures. Two of these configurations exhibit a different type of failure, where the LLM selects arms in roughly equal proportions for the entirety of the T rounds and fails to exploit the acquired information to focus on the better arms. We call this a *uniform-like failure*.

Our surrogate statistic for measuring such failures is defined as follows: For a particular experiment replicate R and round t, let fa(*t, R*) be the fraction of rounds in which a given arm a is chosen, MinFrac(*t, R*) := mina fa(*t, R*), and MinFrac(t) := mean({MinFrac(*t, R*) : replicates R}).

Since MinFrac(t) ≤ 1/K, ∀t ∈ [T], we always plot K ·MinFrac(t), so as to rescale the range to [0, 1].

Larger MinFrac(t) corresponds to a more uniform selection of arms at time t. When an LLM's MinFrac(t) does not decrease over time and stays substantively larger than that of the baselines
(especially as t approaches the time horizon T), we take it as an indication of a uniform-like failure.

The Y-axis of Figure 3 records K · MinFrac(T) for each configuration, where we see that of the three Gpt-4 configurations that avoid suffix failures, two configurations have very high MinFrac(T)
relative to UCB and TS (the third configuration is Gpt-4-BSS�C0, which is successful). These two configurations are Gpt-4-BNRND and Gpt-4-BSSCD, both of which use the *distributional* output format. We provide a more detailed view of Gpt-4-BNRND (as well as Gpt-4-BNSND, which also exhibits uniform-like failures, but only differs from Gpt-4-BNRND in the use of summarized history) in Figure 6, which considers a longer horizon and more replicates (T = 200 and N = 20).

The middle panel reveals that K · MinFrac(t) does not decrease over time for these LLM
configurations, while it does for the baselines. This behavior results in no suffix failures, but leads to much lower reward than the baselines. In particular, we obtain a clear separation in total reward, showing that uniform-like failures indeed result in poor long-term performance.

Generality of the failures. To summarize, Figure 3 shows that all LLM configurations except Gpt-4-BSS�C0 exhibit either a suffix failure or a uniform failure for the hard MAB instance and the buttons scenario. Scatter plots for the other three experiments (i.e., the advertisements scenario and/or the easy MAB instance) are qualitatively similar and are deferred to Appendix B.

The same data, but with attributions to specific LLM configurations, are presented for *all* Gpt-
4 configurations in Figure 4; analogous tables for other LLMs and experimental settings are given in Appendix B. As it is not instructive to present detailed plots such as Figure 5 for every LLM configuration, Figure 4 summarizes the performance of each configuration with just a few statistics. We include:

- SuffFailFreq(T/2) and MinFrac(T), defined above.
- MedianReward: the rescaled median (over replicates) of the time-averaged total reward.10
- GreedyFrac: the fraction of *greedy rounds*, averaged over the replicates. A greedy round is
one in which an arm with a largest average reward is selected. This is one way to quantify the extent to which a configuration behaves like Greedy.
We now summarize further findings from the scatter plots (Figures 3 and 12) and the summary tables (Figures 13 to 19). First, Gpt-4 performs much better than Gpt-3.5, and Llama2 performs much worse (in particular, the suffix failure frequency for Llama2 ranges from that of Greedy to much larger). Second, we observe that all LLMs are sensitive to small changes in the prompt design. However, the different modifications we consider appear to interact with each other, and it is difficult to identify which individual modifications improve performance and which degrade it.

## 3.3 Investigating Successes

On the hard MAB instance, the only configuration in our experiments that avoids both suffix failures and uniform-like failures is Gpt-4 with the BSS�C0 prompt design. As can be seen from Figure 4, at T = 100, this configuration has no suffix failures, the K · MinFrac value is only slightly larger than TS, and the reward is comparable to TS. These statistics suggest that this configuration succeeds, and in this section we present further evidence supporting this claim.

| TS                | UCB   |   Greedy |
|-------------------|-------|----------|
| BSR               |       |          |
| C                 |       |          |
| 0                 | BSS   |          |
| C                 |       |          |
| 0                 |       |          |
| MedianReward      |       |          |
| 0.59              | 0.70  |     0.6  |
| SuffFailFreq(T/2) |       |          |
| 0.00              | 0.02  |     0.47 |
| K*MinFrac         |       |          |
| 0.23              | 0.12  |     0.03 |
| GreedyFrac        |       |          |
| 0.66              | 0.81  |     1    |
| Replicates        |       |          |
| 1000              | 1000  |  1000    |

To do so, we run Gpt-4-BSS�C0 on the hard MAB instance with T = 200 and N = 40 to obtain more statistically meaningful results. We also consider Gpt-4-BSR�C0, which swaps summarized history for raw history, as an ablation. Figure 7 provides a summary of the results from this experiment, while Figure 1(b) provides a detailed view of the BSS�C0 configuration. The figures reveal that BSS�C0 continues to avoid suffix failures and performs relatively well in terms of reward for larger T. On the other hand, we see that BSR�C0 exhibits a non-trivial fraction of suffix failures, demonstrating that this ablation results in fundamentally different behavior.

We also provide two additional visualizations that provide some qualitative evidence toward the success of BSS�C0, as well as the failure of other configurations. These are presented in Figure 8
and Figure 9. In Figure 8 we visualize the arm chosen at each time step for various replicates of several different methods (LLMs and baselines).

Specifically, Figure 8 shows four replicates for the basic configuration (BNRN0) and the two configurations with reinforced CoT (BSR�C0
and BSS�C0), as well as one replicate of each of the baseline algorithms. We see that the basic configuration BNRN0 tends to commit to a single arm for several rounds, a behavior that is similar to that of Greedy and very different from both UCB and TS. BSR�C0 also commits for long periods, but to a lesser extent than the basic configuration. In contrast, BSS�C0 switches arms much more frequently, and qualitatively appears much more similar to TS.

In Figure 9, we plot the fraction of rounds in [0, t] where the optimal arm was pulled as a function of t for individual replicates. BSR�C0 is visually similar to UCB, except that a non-trivial fraction of runs exhibit suffix failures (the curves that converge to 0 on the plot). Meanwhile, BSS�C0
is visually similar to TS, with almost all replicates slowly converging to 1. These visualizations, along with the summary statistics, suggest that BSS�C0 behaves most similarly to TS, which further suggests it will successfully converge to the optimal arm given a long enough time horizon.

## 3.4 Root Causes

|      |      |      |      |      | LeastFrac   | GreedyFrac   |
|------|------|------|------|------|-------------|--------------|
| 0.12 | 0.12 | 0.30 | 0.53 | 0.54 | 0.60        | TS           |
| 0.26 | 0.09 | 0.46 | 0.55 | 0.66 | 0.84        | UCB          |
| 0.24 | 0.30 | 0.30 | 0.50 | 0.36 | 0.34        | BNRN0        |
| 0.04 | 0    | 0.12 | 0.58 | 0.84 | 0.50        | BNRC0        |
| 0    | 0    | 0.28 | 0.84 | 0.94 | 0.82        | BNSN0        |
| 0.38 | 0.38 | 0.60 | 0.22 | 0.18 | 0.20        | BSRN0        |
| TS   | UCB  | Unif | TS   | UCB  | Unif        | Data source  |

Our experimental findings above shed light on how LLM-based decision making agents behave, but it is also worthwhile to understand *why* they behave the way they do (and particularly, why they fail). This question is rather challenging to answer decisively, but two natural hypotheses are that the configurations we consider (outside of Gpt-4-BSS�C0) are either a) too greedy, or b) too uniform-like. In this section, we describe how our experiments offer some insight into this hypotheses.

First, focusing on Gpt-4, our experiments reveal qualitatively different behavior between the easy and hard instances (Figure 13(a) and Figure 13(c)). Indeed, the easy instance appears to be *much* easier;
most Gpt-4 configurations avoid suffix failures and accrue large rewards on this instance, and the GreedyFrac statistic offers a potential explanation as to why. On the easy instance, most Gpt-
4 configurations have very high GreedyFrac values, so they behave similarly to Greedy, which performs quite well (even though Greedy provably fails with small constant probability and, empirically, has many suffix failures on this instance).11 A plausible hypothesis from this is that Gpt-4
performs quite well in low-noise settings, which is precisely when Greedy also performs well.

A stronger hypothesis would be that most Gpt-4 configurations (except perhaps those using reinforced CoT) behave like Greedy on *all* instances, but this hypothesis is invalidated by the GreedyFrac statistics for our experiments on the hard instance. On the hard instance, it seems that most Gpt-4 configurations are doing something non-trivial (albeit flawed); their behavior is neither completely Greedy-like nor like uniform-at-random.

Toward a more fine-grained understanding, we ran a collection of small-scale secondary experiments focusing on the *per-round decisions* of LLM-agents. The experiments focus on a single round t in a bandit problem. Each experiment considers a particular "data source" (a distribution of bandit histories), samples N = 50 bandit histories of length t from this distribution, and presents them to the agents (the LLMs and the baselines) and asks them to output an arm or distribution over arms.

We track two statistics for each agent: GreedyFrac and LeastFrac, the fraction of replicates in which the agent chose, resp., an empirically best arm so far and a least-chosen arm so far. We vary the data source, i.e., the algorithm which generates the history. In particular, we consider histories generated by sampling uniformly at random (Unif) and by running our baselines UCB and TS for t rounds.

Results are summarized in Figure 10. Unfortunately, we find that per-round performance of both the LLMs and the baselines is very sensitive to the particular data source. For example, the MinFrac statistic of UCB can vary from as high as 0.46 on histories generated uniformly at random to as low as 0.09 on histories generated by UCB itself. It seems plausible to conclude the BNSN0 is too greedy while BSRN0 is too uniform, but the statistics for the other two LLM configurations (BNRN0 and BNRC0)—both of which fail in our longitudinal experiments—fall within the reasonable range provided by the baselines. Thus, we find that it is challenging to assess whether LLM agents are too greedy or too uniform-like based on per-round decisions, even though these agents behave rather differently from the baselines in the longitudinal experiments.

## 4 Related Work

This paper belongs to a recent body of work that aims to understand the capabilities of LLMs, i.e., what they can and cannot do well, and why.

Capabilities that have received considerable attention, but are peripheral to the present paper, include general intelligence (Bubeck et al., 2023), causal (Kıcıman et al., 2023; Yiu et al., 2023) and mathematical reasoning (Cobbe et al., 2021; Lu et al., 2023), planning (Valmeekam et al., 2023; Momennejad et al., 2023; Brooks et al.,
2023), and compositionality (Yu et al., 2023).

In more detail, our work contributes to the broader literature on capabilities of in-context learning. Prior studies of in-context learning include theoretical (Xie et al., 2021; Aky¨urek et al., 2022; Zhang et al., 2023b; Abernethy et al., 2023; Zhang et al., 2023a; Han et al., 2023a; Cheng et al., 2023; Ahn et al., 2023; Wies et al., 2023; Fu et al., 2023; Wu et al., 2023; Huang et al., 2023; Hendel et al., 2023; Li et al., 2023; Von Oswald et al., 2023; Bai et al., 2023; Hahn and Goyal, 2023; Jeon et al., 2024) and empirical (Garg et al., 2022; Kirsch et al., 2022; Ahuja et al., 2023; Han et al., 2023b; Ravent´os et al., 2023; Weber et al., 2023; Bhattamishra et al., 2023; Guo et al., 2023; Shen et al., 2023; Aky¨urek et al., 2024) investigations, though as mentioned in the prequel, the vast majority of this work pertains to in-context supervised learning; in-context reinforcement learning has received far less attention. The small collection of empirical works that study in-context RL (Laskin et al., 2022; Lee et al., 2023a; Raparthy et al., 2023; Xu et al., 2022)
focus on models trained from scratch using trajectory data collected from another agent (either an RL algorithm or an expert); theoretically, Lee et al. (2023a) and later Lin et al. (2023) justify this approach with a Bayesian meta-reinforcement learning perspective (Simchowitz et al., 2021), and show that pre-trained transformers can implement classical exploration strategies like Thompson sampling and upper confidence bounds (UCB). However, these works require interventions to the *pre-training* phase of the language model, and do not study whether existing LLMs exhibit exploration capabilities under standard training conditions.

In parallel, there is a rapidly growing line of work that applies LLMs to real-world decisionmaking applications. Beyond previously mentioned works (Shinn et al., 2023; Wang et al., 2023; Lee et al., 2023b), which consider applications to gaming, programming, and medicine, highlights include Park et al. (2023), who introduce generative agents which simulate human behavior in an open-world environment, Ahn et al. (2022); Xu et al. (2023), who develop LLM-enabled robots.

Concurrent work of Wu et al. (2024) studies LLM performance in a battery of tasks that aim to characterize "intelligent agents", with two-armed bandits as a specific task of interest. Their bandit experiments differ in several key respects: They consider a very easy MAB instance (with 2 arms and a gap ∆ = 0.6, which is much easier than both of our instances), focus on a single prompt design (similar to our basic prompt), and compare to human players rather than algorithmic benchmarks. These differences lead to very different experimental findings. In particular, they find that Gpt-4 performs well on their simple MAB instance, converging very quickly to the best arm, while we find that Gpt-4 with a similar prompt fails on a harder MAB instance. However, their finding is consistent with ours, as we also find that several configurations of Gpt-4 do well on the easy MAB instance. As we discuss in Section 3.4, this instance is too simple to provide compelling evidence for principled exploratory behavior.

## 4.1 Further Background On Multi-Armed Bandits

Here, we provide additional background on the multi-armed bandit problem, and on the baseline algorithms used in this paper. Deeper discussion can be found in Bubeck and Cesa-Bianchi (2012); Slivkins (2019); Lattimore and Szepesv´ari (2020).

The UCB algorithm (Auer et al., 2002) explores by assigning each arm a an *index*, defined as the average reward from the arm so far plus a *bonus* of the form
�
C/na, where C = Θ(log T)
and na is the number of samples from the arm so far. In each round, it chooses an arm with the largest index. The bonus implements the principle of *optimism under uncertainty*. We use a version of UCB that sets C = 1 (a heuristic), which has been observed to have a favorable empirical performance (e.g., Slivkins et al., 2013; Ho et al., 2016).

Thompson Sampling (Thompson, 1933; Russo et al., 2018, for a survey) proceeds as if the arms'
mean rewards were initially drawn from some Bayesian prior. In each round, it computes a Bayesian posterior given the history so far, draws a sample from the posterior, and chooses an arm with largest mean reward according to this sample (i.e., assuming the sample were the ground truth). In our setting, the prior is essentially a parameter to the algorithm. We choose the prior that draws the mean reward of each arm independently and uniformly at random from the [0, 1] interval. This is one standard choice, achieving near-optimal regret bounds, as well as good empirical performance (Kaufmann et al., 2012; Agrawal and Goyal, 2012, 2017). Each arm is updated independently as a Beta-Bernoulli conjugate prior. Further optimizing UCB and Thompson Sampling is non-essential to this paper, as they already perform quite well in our experiments.

Provable guarantees for bandit algorithms are commonly expressed via *regret*:
the difference in expected total reward of the best arm and the algorithm. Both baselines achieve regret O(√KT log T), which is nearly minimax optimal as a function of T and K. They also achieve a nearly instance-optimal regret rate, which scales as O (K/∆ log T) for the instances we consider.

The ϵ-Greedy algorithm (Footnote 6) is fundamentally inefficient in that it does not adaptively steer its exploration toward better-performing arms. Accordingly, its regret rate scales as T 2/3 (for an optimal setting of ϵ ∼ T −1/3). Fixing such ϵ, regret does not improve for easier instances.

The Greedy algorithm (Footnote 5) does not explore at all, which causes suffix failures. This is obvious when the algorithm is initialized with a single sample (n = 1) of each arm: a suffix failure happens when the good arm returns 0, and one of the other arms returns 1. However, suffix failures are not an artifact of small n: they can happen for any n, with probability that scales as
Ω(1/√n) (Banihashem et al., 2023).

## 5 Discussion And Open Questions

Our investigation suggests that contemporary LLMs do not robustly engage in exploration required for very basic statistical reinforcement learning and decision making problems, at least without further intervention. In what follows, we identify several next steps to further evaluate this hypothesis and search for interventions to mitigate this behavior. Basic interventions and the need for methodological advancements. In light of our negative results, the most obvious interventions one might consider include:

1. *Experiment with other prompts.* As with many other settings (Sclar et al., 2023), it is possible
that small changes to our prompt template might improve performance. However, sensitivity to prompt design is already concerning.
2. *Experiment with few-shot prompting,* where the prompt contains examples of exploratory
behavior, or use such examples to *fine-tune* the LLM.
3. *Train the LLM to use auxiliary tools,* such as a calculator for basic arithmetic or a "randomizer" to correctly sample from a distribution.
While these steps are quite natural, cost, access to models, and compute pose significant barriers to further study, particularly because of the need to employ long horizons T and many replicates N to obtain statistically meaningful results. To this end, we believe that further methodological and/or statistical advancements to enable cost-effective diagnosis and understanding of LLM-agent behavior (e.g., our surrogate statistics) are essential. Implications for complex decision making problems.

Our focus on simple multi-armed bandit problems provides a clean and controllable experimental setup to study the exploratory behavior of LLMs and potential algorithmic interventions. Exploration failures here suggest that similar failures will also occur in more complex RL and decision making settings. On the other hand, caution must be exercised in developing mitigations, as solutions that succeed for the MAB setting may not generalize to more complex settings. For example, while Gpt-4 with summarized interaction history and reinforced CoT seems to successfully explore in our MAB setting, it is not clear how one should externally summarize the history in settings with complex, high-dimensional observations such as contextual bandits (see Footnote 1). Indeed, even for linear contextual bandits, the approach may not be applicable without a substantial algorithmic intervention (such as, e.g., a linear regression computed externally and included in the prompt) and the many explicit modeling and algorithmic choices involved in such interventions. We believe a deeper investigation of algorithmic interventions is essential to understand the extent to which LLMs can operate as decision making agents.

## References

Jacob Abernethy, Alekh Agarwal, Teodor V Marinov, and Manfred K Warmuth. A mechanism for
sample-efficient in-context learning for sparse retrieval tasks. *arXiv:2305.17040*, 2023.
Shipra Agrawal and Navin Goyal. Analysis of Thompson Sampling for the multi-armed bandit
problem. In *Conference on Learning Theory*, 2012.
Shipra Agrawal and Navin Goyal. Near-optimal regret bounds for thompson sampling. Journal of
the ACM, 2017. Preliminary version in *AISTATS 2013*.
Kwangjun Ahn, Xiang Cheng, Hadi Daneshmand, and Suvrit Sra. Transformers learn to implement
preconditioned gradient descent for in-context learning. *arXiv:2306.00297*, 2023.
Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David,
Chelsea Finn, Chuyuan Fu, Keerthana Gopalakrishnan, Karol Hausman, Daniel Herzon, Alexand Ho, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Eric Jang, Rosario Jauregui Ruano, Kyle Jeffrey, Sally Jesmonth, Nikhil J Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Kuang-Huei Lee, Sergey Levine, Yao Lu, Linda Luu, Carolina Parada, Peter Pastor, Jornell Quiambao, Kanishka Rao, Jarek Rettinghouse, Diego Reyes, Pierre Sermanet, Nicolas Sievers, Clayton Tan, Alexander Toshev, Vincent Vanhoucke, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Mengyuan Yan, and Andy Zeng. Do as I can, not as I say: Grounding language in robotic affordances. *arXiv:2204.01691*, 2022.
Kabir Ahuja, Madhur Panwar, and Navin Goyal. In-context learning through the bayesian prism.
arXiv:2306.04891, 2023.
Ekin Aky¨urek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou. What learning
algorithm is in-context learning? Investigations with linear models. *arXiv:2211.15661*, 2022.
Ekin Aky¨urek, Bailin Wang, Yoon Kim, and Jacob Andreas. In-context language learning: Architectures and algorithms. *arXiv:2401.12973*, 2024.
Peter Auer, Nicol`o Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit
problem. *Machine Learning*, 2002.
Yu Bai, Fan Chen, Huan Wang, Caiming Xiong, and Song Mei. Transformers as statisticians:
Provable in-context learning with in-context algorithm selection. *arXiv:2306.04637*, 2023.
Kiarash Banihashem, MohammadTaghi Hajiaghayi, Suho Shin, and Aleksandrs Slivkins. Bandit
social learning: Exploration under myopic behavior. *arXiv:2302.07425*, 2023.
Satwik Bhattamishra, Arkil Patel, Phil Blunsom, and Varun Kanade. Understanding in-context
learning in transformers and LLMs by learning to learn discrete functions. *arXiv:2310.03016*,
2023.
Ethan Brooks, Logan A Walls, Richard Lewis, and Satinder Singh. Large language models can
implement policy iteration. In *Advances in Neural Information Processing Systems*, 2023.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler,
Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems, 2020.

S´ebastien Bubeck and Nicolo Cesa-Bianchi.
Regret Analysis of Stochastic and Nonstochastic Multi-armed Bandit Problems.
Foundations and Trends in Machine Learning, 5(1):
1–122,
2012.
Published with Now Publishers
(Boston,
MA, USA). Also available at
https://arxiv.org/abs/1204.5721.
S´ebastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece
Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro, and Yi Zhang. Sparks of artificial general intelligence: Early experiments with gpt-4. *arXiv:2303.12712*, 2023.
Xiang Cheng, Yuxin Chen, and Suvrit Sra. Transformers implement functional gradient descent to
learn non-linear functions in context. *arXiv:2312.06528*, 2023.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems. *arXiv:2110.14168*, 2021.
Tim Dettmers and Luke Zettlemoyer. The case for 4-bit precision: k-bit inference scaling laws. In
International Conference on Machine Learning, 2023.
Carl N Edwards, Aakanksha Naik, Tushar Khot, Martin D Burke, Heng Ji, and Tom Hope.
Synergpt:
In-context learning for personalized drug synergy prediction and drug design.
arXiv:2307.11694, 2023.
Deqing Fu, Tian-Qi Chen, Robin Jia, and Vatsal Sharan. Transformers learn higher-order optimization methods for in-context learning: A study with linear models. *arXiv:2310.17086*, 2023.
Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and
Graham Neubig. Pal: Program-aided language models. In International Conference on Machine Learning, 2023.
Shivam Garg, Dimitris Tsipras, Percy S Liang, and Gregory Valiant. What can transformers learn
in-context? a case study of simple function classes. Advances in Neural Information Processing Systems, 2022.
Tianyu Guo, Wei Hu, Song Mei, Huan Wang, Caiming Xiong, Silvio Savarese, and Yu Bai. How
do transformers learn in-context beyond simple functions? A case study on learning with representations. *arXiv:2310.10616*, 2023.
Michael Hahn and Navin Goyal. A theory of emergent in-context learning as implicit structure
induction. *arXiv:2303.07971*, 2023.
Chi Han, Ziqi Wang, Han Zhao, and Heng Ji. Explaining emergent in-context learning as kernel
regression. *arXiv:2305.12766*, 2023a.
Xiaochuang Han, Daniel Simig, Todor Mihaylov, Yulia Tsvetkov, Asli Celikyilmaz, and Tianlu
Wang. Understanding in-context learning via supportive pretraining data. *arXiv:2306.15091*,
2023b.
Roee Hendel, Mor Geva, and Amir Globerson.
In-context learning creates task vectors.
arXiv:2310.15916, 2023.
Chien-Ju Ho, Aleksandrs Slivkins, and Jennifer Wortman Vaughan. Adaptive contract design for
crowdsourcing markets: Bandit algorithms for repeated principal-agent problems. Journal of Artificial Intelligence Research, 2016. Preliminary version in *ACM EC 2014*.
Yu Huang,
Yuan Cheng,
and Yingbin Liang.
In-context convergence of transformers.
arXiv:2310.05249, 2023.
Hong Jun Jeon, Jason D Lee, Qi Lei, and Benjamin Van Roy. An information-theoretic analysis of
in-context learning. *arXiv:2401.15530*, 2024.
Emilie Kaufmann, Nathaniel Korda, and R´emi Munos. Thompson sampling: An asymptotically
optimal finite-time analysis. In *International Conference on Algorithmic Learning Theory*, 2012.
Emre Kıcıman, Robert Ness, Amit Sharma, and Chenhao Tan. Causal reasoning and large language
models: Opening a new frontier for causality. *arXiv:2305.00050*, 2023.
Louis Kirsch, James Harrison, Jascha Sohl-Dickstein, and Luke Metz. General-purpose in-context
learning by meta-learning transformers. *arXiv:2212.04458*, 2022.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large
language models are zero-shot reasoners. *Advances in neural information processing systems*,
2022.
Michael Laskin, Luyu Wang, Junhyuk Oh, Emilio Parisotto, Stephen Spencer, Richie Steigerwald,
DJ Strouse, Steven Hansen, Angelos Filos, Ethan Brooks, Maxime Gazeau, Himanshu Sahni, Satinder Singh, and Volodymyr Mnih. In-context reinforcement learning with algorithm distillation. *arXiv:2210.14215*, 2022.
Tor Lattimore and Csaba Szepesv´ari. *Bandit Algorithms*. Cambridge University Press, 2020.
Jonathan N Lee, Annie Xie, Aldo Pacchiano, Yash Chandak, Chelsea Finn, Ofir Nachum,
and Emma Brunskill.
Supervised pretraining can learn in-context reinforcement learning.
arXiv:2306.14892, 2023a.
Peter Lee, Carey Goldberg, and Isaac Kohane. *The AI revolution in medicine: GPT-4 and beyond*.
Pearson, 2023b.
Yingcong Li, Muhammed Emrullah Ildiz, Dimitris Papailiopoulos, and Samet Oymak. Transformers
as algorithms: Generalization and stability in in-context learning. In International Conference on Machine Learning, 2023.
Licong Lin, Yu Bai, and Song Mei. Transformers as decision makers: Provable in-context reinforcement learning via supervised pretraining. *arXiv:2310.08566*, 2023.
Bingbin Liu, Jordan Ash, Surbhi Goel, Akshay Krishnamurthy, and Cyril Zhang. Exposing attention glitches with flip-flop language modeling. Advances in Neural Information Processing
Systems, 2024.
Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng,
Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. *arXiv:2310.02255*, 2023.
Eran Malach. Auto-regressive next-token predictors are universal learners. *arXiv:2309.06979*, 2023.
Ida Momennejad, Hosein Hasanbeig, Felipe Vieira, Hiteshi Sharma, Robert Osazuwa Ness, Nebojsa
Jojic, Hamid Palangi, and Jonathan Larson. Evaluating cognitive maps and planning in large
language models with cogeval. *arXiv:2309.15129*, 2023.
OpenAI. Gpt-4 technical report. *arXiv:2303.08774*, 2023. Joon Sung Park, Joseph O'Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein.
Generative agents: Interactive simulacra of human behavior.
In Symposium on User Interface Software and Technology, 2023.
Sharath Chandra Raparthy, Eric Hambro, Robert Kirk, Mikael Henaff, and Roberta Raileanu. Generalization to new sequential decision making tasks with in-context learning. *arXiv:2312.03801*,
2023.
Allan Ravent´os, Mansheej Paul, Feng Chen, and Surya Ganguli. Pretraining task diversity and the
emergence of non-bayesian in-context learning for regression. *arXiv:2306.15063*, 2023.
Daniel Russo, Benjamin Van Roy, Abbas Kazerouni, Ian Osband, and Zheng Wen. A tutorial on
thompson sampling. *Foundations and Trends in Machine Learning*, 2018.
Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. Quantifying language models' sensitivity to spurious features in prompt design or: How i learned to start worrying about prompt formatting. *arXiv:2310.11324*, 2023.
Lingfeng Shen, Aayush Mishra, and Daniel Khashabi.
Do pretrained transformers really learn
in-context by gradient descent? *arXiv:2310.08540*, 2023.
Noah Shinn, Federico Cassano, Beck Labash, Ashwin Gopinath, Karthik Narasimhan, and Shunyu
Yao. Reflexion: Language agents with verbal reinforcement learning. *arXiv:2303.11366*, 2023.
Max Simchowitz, Christopher Tosh, Akshay Krishnamurthy, Daniel J Hsu, Thodoris Lykouris,
Miro Dudik, and Robert E Schapire. Bayesian decision-making under misspecified priors with applications to meta-learning. *Advances in Neural Information Processing Systems*, 2021.
Aleksandrs Slivkins. Introduction to multi-armed bandits. Foundations and Trends in Machine
Learning, 2019.
Aleksandrs Slivkins, Filip Radlinski, and Sreenivas Gollapudi. Ranked bandits in metric spaces:
Learning optimally diverse rankings over large document collections. Journal of Machine Learning Research, 2013. Preliminary version in *ICML*, 2010.
Anirudh Som, Karan Sikka, Helen Gent, Ajay Divakaran, Andreas Kathol, and Dimitra Vergyri.
Demonstrations are all you need: Advancing offensive content paraphrasing using in-context learning. *arXiv:2310.10707*, 2023.
William R. Thompson. On the likelihood that one unknown probability exceeds another in view of
the evidence of two samples. *Biometrika*, 1933.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas
Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and fine-tuned chat models. *arXiv:2307.09288*, 2023.

Karthik Valmeekam, Matthew Marquez, Alberto Olmo, Sarath Sreedharan, and Subbarao Kambhampati. Planbench: An extensible benchmark for evaluating large language models on planning and reasoning about change. In Advances in Neural Information Processing Systems: Datasets and Benchmarks Track, 2023.
Johannes Von Oswald, Eyvind Niklasson, Ettore Randazzo, Jo˜ao Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov. Transformers learn in-context by gradient descent. In *International Conference on Machine Learning*, 2023.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv:2305.16291, 2023.
Lucas Weber, Elia Bruni, and Dieuwke Hupkes. The ICL consistency test. *arXiv:2312.04945*, 2023.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, and
Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems, 2022.
Noam Wies, Yoav Levine, and Amnon Shashua.
The learnability of in-context learning.
arXiv:2303.07895, 2023.
Jingfeng Wu, Difan Zou, Zixiang Chen, Vladimir Braverman, Quanquan Gu, and Peter L
Bartlett. How many pretraining tasks are needed for in-context learning of linear regression? arXiv:2310.08391, 2023.
Yue Wu, Xuan Tang, Tom Mitchell, and Yuanzhi Li.
Smartplay: A benchmark for LLMs as
intelligent agents. In *International Conference on Learning Representations*, 2024.
Sang Michael Xie, Aditi Raghunathan, Percy Liang, and Tengyu Ma. An explanation of in-context
learning as implicit bayesian inference. *arXiv:2111.02080*, 2021.
Mengdi Xu, Yikang Shen, Shun Zhang, Yuchen Lu, Ding Zhao, Joshua Tenenbaum, and Chuang
Gan. Prompting decision transformer for few-shot policy generalization. In International Conference on Machine Learning, 2022.
Mengdi Xu, Peide Huang, Wenhao Yu, Shiqi Liu, Xilun Zhang, Yaru Niu, Tingnan Zhang, Fei Xia,
Jie Tan, and Ding Zhao. Creative robot tool use with large language models. *arXiv:2310.13065*,
2023.
Eunice Yiu, Eliza Kosoy, and Alison Gopnik. Imitation versus innovation: What children can do
that large language and language-and-vision models cannot (yet)? *arXiv:2305.07666*, 2023.
Dingli Yu, Simran Kaur, Arushi Gupta, Jonah Brown-Cohen, Anirudh Goyal, and Sanjeev Arora.
Skill-mix: A flexible and expandable family of evaluations for ai models. *arXiv:2310.17567*, 2023.
Ruiqi Zhang, Spencer Frei, and Peter L Bartlett. Trained transformers learn linear models incontext. *arXiv:2306.09927*, 2023a.
Yufeng Zhang, Fengzhuo Zhang, Zhuoran Yang, and Zhaoran Wang.
What and how does
in-context learning learn?
bayesian model averaging, parameterization, and generalization.
arXiv:2305.19420, 2023b.

## A Prompt Designs A.1 Prompt Examples

Let us present three full examples of our prompts.

We remove the blank lines for the sake of readability.

(a) Our basic prompt design (i.e., BNRN, as temperature is specified elsewhere): the buttons scenario with neutral framing and raw histories, asking the LLM to return an action without chain-of-thought reasoning.

[SYSTEM] You are in a room with 5 buttons labeled blue, green, red, yellow, purple. Each button is associated with a Bernoulli distribution with a fixed but unknown mean; the means for the buttons could be different. For each button, when you press it, you will get a reward that is sampled from the button's associated distribution. You have 10 time steps and, on each time step, you can choose any button and receive the reward.

Your goal is to maximize the total reward over the 10 time steps. At each time step, I will show you your past choices and rewards. Then you must make the next choice, which must be exactly one of blue, green, red, yellow, purple. You must provide your final answer immediately within the tags <Answer>COLOR</Answer>
where COLOR is one of blue, green, red, yellow, purple and with no text explanation. [USER] So far you have played 2 times with the following choices and rewards: blue button, reward 1 green button, reward 0 Which button will you choose next? Remember, YOU MUST provide your final answer within the tags <Answer>COLOR</Answer> where COLOR is one of blue, green, red, yellow, purple.

(b) The adverts scenario with all the "advanced" modifications (i.e., ASSCD) : suggestive framing, summarized histories, asking the LLM to return a distribution over actions, and asking for a chainof-thought reasoning.

[SYSTEM] You are recommendation engine that chooses advertisements to display to users when they visit your webpage. There are 5 advertisements you can choose from, named A, B, C, D, E. When a user visits the webpage you can choose an advertisement to display and you will observe whether the user clicks on the ad or not. You model this by assuming that each advertisement has a certain click rate and users click on advertisements with their corresponding rates. You have a budget of 10 users to interact with and your goal is to maximize the total number of clicks during this process. A good strategy to optimize for clicks in these situations requires balancing exploration and exploitation.

You need to explore to try out all of the options and find those with high click rates, but you also have to exploit the information that you have to accumulate clicks. When each user visits the webpage, I will show you a summary of the data you have collected so far. Then you must choose which advertisement to display. You may output a distribution over the 5 choices formatted EXACTLY like "A:n1,B:n2,C:n3,D:n4,E:n5".

Let's think step by step to make sure we make a good choice. Then, you must provide your final answer within the tags <Answer>DIST</Answer> where DIST is the distribution in the format specified above.

[USER] So far you have interacted with 2 users. Here is a summary of the data you have collected: Advertisement A was shown to 1 users with an estimated click rate of 1.00 Advertisement B was shown to 1 users with an estimated click rate of 0.00 Advertisement C has not been shown Advertisement D has not been shown Advertisement E has not been shown Which advertisement will you choose next?

Remember, YOU MUST provide your final answer within the tags <Answer>DIST</Answer> where DIST is formatted like
"A:n1,B:n2,C:n3,D:n4,E:n5".

(c) The successful configuration for Gpt-4 (i.e., BSS�C, as temperature is specified elsewhere), which uses the buttons scenario, suggestive framing, summarized histories, and reinforced chainof-thought reasoning.

[SYSTEM] You are a bandit algorithm in a room with 5 buttons labeled blue, green, red, yellow, purple. Each button is associated with a Bernoulli distribution with a fixed but unknown mean; the means for the buttons could be different. For each button, when you press it, you will get a reward that is sampled from the button's associated distribution. You have 10 time steps and, on each time step, you can choose any button and receive the reward. Your goal is to maximize the total reward over the 10 time steps. At each time step, I will show you a summary of your past choices and rewards. Then you must make the next choice, which must be exactly one of blue, green, red, yellow, purple. Let's think step by step to make sure we make a good choice. You must provide your final answer within the tags <Answer>COLOR</Answer> where COLOR is one of blue, green, red, yellow, purple.

[USER] So far you have played 2 times with your past choices and rewards summarized as follows: blue button: pressed 1 times with average reward 1.00 green button: pressed 1 times with average reward 0.00 red button: pressed 0 times yellow button: pressed 0 times purple button: pressed 0 times Which button will you choose next? Remember, YOU MUST provide your final answer within the tags <Answer>COLOR</Answer> where COLOR is one of blue, green, red, yellow, purple. Let's think step by step to make sure we make a good choice.

## B Scatter Plots And Summary Tables

(a) Hard MAB instance (∆ = 0.2), buttons scenario, N = 10 replicates.

TS
UCB
Greedy
BNRN0
BNRN1
BNRND
BNRC0
BNSN0
BSRN0
BSSC0
BSSC1
BSSCD
BSSC0
MedianReward
0.47
0.55
0.40
0.63
0.70
0.33
0.35
0.60
0.45
0.68
0.28
0.37
0.47
SuffFailFreq(T/2)
0.01
0.02
0.48
0.50
0.40
0.00
0.50
0.60
0.70
0.30
0.20
0.00
0.00
K*MinFrac
0.28
0.18
0.05
0.03
0.04
0.41
0.09
0.07
0.05
0.09
0.19
0.49
0.33
GreedyFrac
0.62
0.76
1.00
0.52
0.46
0.45
0.78
0.99
0.59
0.93
0.88
0.49
0.69
Replicates
1000
1000
1000
10
10
10
10
10
10
10
10
10
10

(b) Hard MAB instance (∆ = 0.2), advertisements scenario, N = 3 replicates.

TS
UCB
Greedy
ANRN0
ANRN1
ANRND
ANRC0
ANSN0
ASRN0
ASSC0
ASSC1
ASSCD
MedianReward
0.47
0.55
0.40
0.00
-0.05
-0.15
0.35
0.40
0.45
0.15
0.60
-0.15
SuffFailFreq(T/2)
0.01
0.02
0.48
1.00
0.67
0.67
0.33
1.00
0.67
0.33
0.00
0.67
K*MinFrac
0.28
0.18
0.05
0.00
0.03
0.00
0.05
0.05
0.07
0.30
0.43
0.00
GreedyFrac
0.62
0.76
1.00
0.47
0.23
1.00
0.86
0.99
0.91
0.68
0.70
1.00
Replicates
1000
1000
1000
3
3
3
3
3
3
3
3
3

(c) Easy MAB instance (∆ = 0.5), buttons scenario, N = 3 replicates.

TS
UCB
Greedy
BNRN0
BNRN1
BNRND
BNRC0
BNSN0
BSRN0
BSSC0
BSSC1
BSSCD
MedianReward
0.84
0.88
0.92
0.90
0.92
0.56
0.92
0.96
0.92
0.92
0.90
0.58
SuffFailFreq(T/2)
0.00
0.00
0.19
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
K*MinFrac
0.14
0.09
0.04
0.05
0.03
0.43
0.05
0.04
0.03
0.04
0.09
0.35
GreedyFrac
0.88
0.94
1.00
0.97
0.99
0.56
0.99
1.00
0.73
0.99
0.93
0.63
Replicates
1000
1000
1000
3
3
3
3
3
3
3
3
3
TS
UCB
Greedy
ANRN0
ANRN1
ANRND
ANRC0
ANSN0
ASRN0
ASSC0
ASSC1
ASSCD
MedianReward
0.84
0.88
0.92
0.88
0.88
0.08
0.88
0.90
0.88
0.70
0.68
0.08
SuffFailFreq(T/2)
0.00
0.00
0.19
0.33
0.33
0.67
0.00
0.33
0.00
0.00
0.00
0.67
K*MinFrac
0.14
0.09
0.04
0.01
0.00
0.00
0.04
0.04
0.07
0.25
0.29
0.00
GreedyFrac
0.88
0.94
1.00
0.81
0.95
1.00
0.94
1.00
0.96
0.81
0.73
1.00
Replicates
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.47           |                0.01 |        0.28 |         0.62 |
| UCB            |                     |             |              |
| 0.55           |                0.02 |        0.18 |         0.76 |
| Greedy         |                     |             |              |
| 0.40           |                0.48 |        0.05 |         1    |
| BNRN0          |                     |             |              |
| 0.22           |                0.5  |        0.16 |         0.3  |
| BNRN1          |                     |             |              |
| 0.22           |                0    |        0.41 |         0.28 |
| BNRND          |                     |             |              |
| 0.12           |                0.55 |        0.07 |         0.4  |
| BNRC0          |                     |             |              |
| 0.12           |                0.8  |        0.01 |         0.51 |
| BNRC1          |                     |             |              |
| 0.10           |                0.5  |        0.03 |         0.57 |
| BNRCD          |                     |             |              |
| 0.65           |                0.45 |        0.01 |         0.75 |
| BNSN0          |                     |             |              |
| 0.12           |                0.85 |        0    |         1    |
| BNSN1          |                     |             |              |
| 0.22           |                0.25 |        0.04 |         0.76 |
| BNSND          |                     |             |              |
| 0.20           |                0.2  |        0.52 |         0.38 |
| BNSC0          |                     |             |              |
| 0.12           |                0.85 |        0    |         0.95 |
| BNSC1          |                     |             |              |
| 0.22           |                0.7  |        0.01 |         0.88 |
| BNSCD          |                     |             |              |
| 0.05           |                0.5  |        0.11 |         0.5  |
| BSRN0          |                     |             |              |
| 0.17           |                0.3  |        0.25 |         0.32 |
| BSRN1          |                     |             |              |
| 0.25           |                0    |        0.66 |         0.29 |
| BSRND          |                     |             |              |
| 0.42           |                0.25 |        0.12 |         0.33 |
| BSRC0          |                     |             |              |
| 0.10           |                0.65 |        0.03 |         0.44 |
| BSRC1          |                     |             |              |
| 0.05           |                0.25 |        0.12 |         0.47 |
| BSRCD          |                     |             |              |
| 0.28           |                0.15 |        0.11 |         0.6  |
| BSSN0          |                     |             |              |
| 0.12           |                0.85 |        0    |         1    |
| BSSN1          |                     |             |              |
| 0.25           |                0.3  |        0.03 |         0.78 |
| BSSND          |                     |             |              |
| 0.25           |                0.15 |        0.45 |         0.42 |
| BSSC0          |                     |             |              |
| 0.17           |                0.85 |        0    |         1    |
| BSSC1          |                     |             |              |
| 0.17           |                0.55 |        0.02 |         0.83 |
| BSSCD          |                     |             |              |
| 0.20           |                0.35 |        0.1  |         0.78 |
Replicates
1000 1000 1000
20 20 20 20
20
20 20 20 20 20 20 20 20 20 20 20 20
20 20 20 20 20 20 20
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.47           |                0.01 |        0.28 |         0.62 |
| UCB            |                     |             |              |
| 0.55           |                0.02 |        0.18 |         0.76 |
| Greedy         |                     |             |              |
| 0.40           |                0.48 |        0.05 |         1    |
| ANRN0          |                     |             |              |
| 0.22           |                0.65 |        0.03 |         0.48 |
| ANRN1          |                     |             |              |
| 0.22           |                0.5  |        0.05 |         0.33 |
| ANRND          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ANRC0          |                     |             |              |
| 0.15           |                0.85 |        0    |         0.98 |
| ANRC1          |                     |             |              |
| 0.20           |                0.5  |        0    |         0.8  |
| ANRCD          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ANSN0          |                     |             |              |
| 0.12           |                0.85 |        0    |         1    |
| ANSN1          |                     |             |              |
| 0.12           |                0.2  |        0.04 |         0.93 |
| ANSND          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ANSC0          |                     |             |              |
| 0.17           |                0.8  |        0    |         1    |
| ANSC1          |                     |             |              |
| 0.12           |                0.55 |        0.01 |         0.93 |
| ANSCD          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ASRN0          |                     |             |              |
| 0.25           |                0.7  |        0.03 |         0.48 |
| ASRN1          |                     |             |              |
| 0.05           |                0.42 |        0.06 |         0.28 |
| ASRND          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ASRC0          |                     |             |              |
| 0.37           |                0.4  |        0.06 |         0.64 |
| ASRC1          |                     |             |              |
| 0.30           |                0.25 |        0.11 |         0.65 |
| ASRCD          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ASSN0          |                     |             |              |
| 0.15           |                0.85 |        0    |         1    |
| ASSN1          |                     |             |              |
| 0.25           |                0.42 |        0.05 |         0.92 |
| ASSND          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
| ASSC0          |                     |             |              |
| 0.12           |                0.8  |        0.01 |         0.99 |
| ASSC1          |                     |             |              |
| 0.30           |                0.15 |        0.14 |         0.83 |
| ASSCD          |                     |             |              |
| 0.15           |                0.7  |        0    |         1    |
Replicates
1000
1000
1000
20 20 20 20
20 20 20 20 20 20 20 20 20 20 20 20
20
20 20 20 20 20 20 20
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.84           |                0    |        0.14 |         0.88 |
| UCB            |                     |             |              |
| 0.88           |                0    |        0.09 |         0.94 |
| Greedy         |                     |             |              |
| 0.92           |                0.19 |        0.04 |         1    |
| BNRN0          |                     |             |              |
| 0.23           |                0.55 |        0.02 |         0.85 |
| BNRN1          |                     |             |              |
| 0.72           |                0.05 |        0.16 |         0.62 |
| BNRND          |                     |             |              |
| 0.14           |                0.25 |        0.17 |         0.46 |
| BNRC0          |                     |             |              |
| 0.84           |                0.25 |        0.03 |         0.56 |
| BNRC1          |                     |             |              |
| 0.81           |                0.05 |        0.08 |         0.77 |
| BNRCD          |                     |             |              |
| 0.88           |                0.1  |        0.04 |         0.92 |
| BNSN0          |                     |             |              |
| 0.18           |                0.65 |        0    |         1    |
| BNSN1          |                     |             |              |
| 0.60           |                0.4  |        0.02 |         0.89 |
| BNSND          |                     |             |              |
| 0.26           |                0.1  |        0.54 |         0.52 |
| BNSC0          |                     |             |              |
| 0.18           |                0.65 |        0    |         1    |
| BNSC1          |                     |             |              |
| 0.16           |                0.55 |        0.01 |         0.95 |
| BNSCD          |                     |             |              |
| 0.62           |                0.35 |        0.03 |         0.77 |
| BSRN0          |                     |             |              |
| 0.73           |                0.3  |        0.11 |         0.57 |
| BSRN1          |                     |             |              |
| 0.35           |                0    |        0.48 |         0.42 |
| BSRND          |                     |             |              |
| 0.21           |                0.25 |        0.09 |         0.43 |
| BSRC0          |                     |             |              |
| 0.87           |                0.05 |        0.06 |         0.72 |
| BSRC1          |                     |             |              |
| 0.73           |                0.05 |        0.16 |         0.72 |
| BSRCD          |                     |             |              |
| 0.81           |                0.05 |        0.11 |         0.76 |
| BSSN0          |                     |             |              |
| 0.18           |                0.65 |        0    |         1    |
| BSSN1          |                     |             |              |
| 0.17           |                0.25 |        0.02 |         0.89 |
| BSSND          |                     |             |              |
| 0.26           |                0.3  |        0.39 |         0.6  |
| BSSC0          |                     |             |              |
| 0.19           |                0.6  |        0    |         0.99 |
| BSSC1          |                     |             |              |
| 0.53           |                0.35 |        0.03 |         0.82 |
| BSSCD          |                     |             |              |
| 0.78           |                0.25 |        0.02 |         0.9  |
Replicates
1000 1000 1000
20 20 20 20
20
20 20 20 20 20 20 20 20 20 20 20 20
20 20 20 20 20 20 20
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.84           |                0    |        0.14 |         0.88 |
| UCB            |                     |             |              |
| 0.88           |                0    |        0.09 |         0.94 |
| Greedy         |                     |             |              |
| 0.92           |                0.19 |        0.04 |         1    |
| ANRN0          |                     |             |              |
| 0.18           |                0.65 |        0.01 |         0.81 |
| ANRN1          |                     |             |              |
| 0.10           |                0.35 |        0.03 |         0.47 |
| ANRND          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ANRC0          |                     |             |              |
| 0.13           |                0.6  |        0    |         0.96 |
| ANRC1          |                     |             |              |
| 0.77           |                0.35 |        0.03 |         0.89 |
| ANRCD          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ANSN0          |                     |             |              |
| 0.18           |                0.65 |        0    |         1    |
| ANSN1          |                     |             |              |
| 0.69           |                0.15 |        0.03 |         0.97 |
| ANSND          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ANSC0          |                     |             |              |
| 0.23           |                0.6  |        0    |         1    |
| ANSC1          |                     |             |              |
| 0.71           |                0.2  |        0.03 |         0.96 |
| ANSCD          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ASRN0          |                     |             |              |
| 0.08           |                0.75 |        0.01 |         0.81 |
| ASRN1          |                     |             |              |
| 0.08           |                0.45 |        0.05 |         0.4  |
| ASRND          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ASRC0          |                     |             |              |
| 0.68           |                0.1  |        0.08 |         0.86 |
| ASRC1          |                     |             |              |
| 0.74           |                0    |        0.13 |         0.86 |
| ASRCD          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ASSN0          |                     |             |              |
| 0.29           |                0    |        0.04 |         0.92 |
| ASSN1          |                     |             |              |
| 0.79           |                0.1  |        0.05 |         0.93 |
| ASSND          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
| ASSC0          |                     |             |              |
| 0.89           |                0.2  |        0.01 |         1    |
| ASSC1          |                     |             |              |
| 0.82           |                0.1  |        0.11 |         0.92 |
| ASSCD          |                     |             |              |
| 0.10           |                0.55 |        0    |         1    |
Replicates
1000
1000
1000
20 20 20 20
20 20 20 20 20 20 20 20 20 20 20 20
20
20 20 20 20 20 20 20
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.47           |                0.01 |        0.28 |         0.62 |
| UCB            |                     |             |              |
| 0.55           |                0.02 |        0.18 |         0.76 |
| Greedy         |                     |             |              |
| 0.40           |                0.48 |        0.05 |         1    |
| BNRN0          |                     |             |              |
| -0.05          |                0.9  |        0    |         1    |
| BNRN1          |                     |             |              |
| 0.07           |                0.9  |        0    |         1    |
| BNRC0          |                     |             |              |
| 0.10           |                0.8  |        0.01 |         0.62 |
| BNRC1          |                     |             |              |
| 0.28           |                0.9  |        0    |         0.89 |
| BNSN0          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BNSN1          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BNSC0          |                     |             |              |
| 0.07           |                1    |        0    |         1    |
| BNSC1          |                     |             |              |
| 0.47           |                0.6  |        0    |         1    |
| BSRN0          |                     |             |              |
| -0.03          |                0.9  |        0    |         1    |
| BSRN1          |                     |             |              |
| -0.08          |                1    |        0    |         0.93 |
| BSRC0          |                     |             |              |
| 0.10           |                0.8  |        0.01 |         0.72 |
| BSRC1          |                     |             |              |
| -0.08          |                1    |        0.01 |         0.67 |
| BSSN0          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BSSN1          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BSSC0          |                     |             |              |
| 0.07           |                1    |        0    |         1    |
| BSSC1          |                     |             |              |
| 0.22           |                0.9  |        0    |         1    |
Replicates
1000 1000 1000
10
10 10 10 10 10 10 10 10 10 10
10
10 10 10 10
| MedianReward   |   SuffFailFreq(T/2) |   K*MinFrac |   GreedyFrac |
|----------------|---------------------|-------------|--------------|
| TS             |                     |             |              |
| 0.47           |                0.01 |        0.28 |         0.62 |
| UCB            |                     |             |              |
| 0.55           |                0.02 |        0.18 |         0.76 |
| Greedy         |                     |             |              |
| 0.40           |                0.48 |        0.05 |         1    |
| BNRN0          |                     |             |              |
| -0.05          |                0.9  |        0    |         1    |
| BNRN1          |                     |             |              |
| 0.07           |                0.9  |        0    |         1    |
| BNRC0          |                     |             |              |
| 0.10           |                0.8  |        0.01 |         0.62 |
| BNRC1          |                     |             |              |
| 0.28           |                0.9  |        0    |         0.89 |
| BNSN0          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BNSN1          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BNSC0          |                     |             |              |
| 0.07           |                1    |        0    |         1    |
| BNSC1          |                     |             |              |
| 0.47           |                0.6  |        0    |         1    |
| BSRN0          |                     |             |              |
| -0.03          |                0.9  |        0    |         1    |
| BSRN1          |                     |             |              |
| -0.08          |                1    |        0    |         0.93 |
| BSRC0          |                     |             |              |
| 0.10           |                0.8  |        0.01 |         0.72 |
| BSRC1          |                     |             |              |
| -0.08          |                1    |        0.01 |         0.67 |
| BSSN0          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BSSN1          |                     |             |              |
| 0.60           |                0.5  |        0    |         1    |
| BSSC0          |                     |             |              |
| 0.07           |                1    |        0    |         1    |
| BSSC1          |                     |             |              |
| 0.22           |                0.9  |        0    |         1    |
Replicates
1000 1000 1000
10
10 10 10 10 10 10 10 10 10 10
10
10 10 10 10
