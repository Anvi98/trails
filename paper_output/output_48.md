# Strategic Network Creation For Enabling Greedy Routing

JULIAN BERGER, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany TOBIAS FRIEDRICH, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany PASCAL LENZNER, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany PARASKEVI MACHAIRA, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany JANOSCH RUFF, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany In this paper, we present the first game-theoretic network creation model that incorporates greedy routing, i.e., the agents in our model are embedded in some metric space and strive for creating a network where all-pairs greedy routing is enabled. In contrast to graph-theoretic shortest paths, our agents route their traffic along greedy paths, which are sequences of nodes where the distance in the metric space to the respective target node gets strictly smaller by each hop. Besides enabling greedy routing, the agents also optimize their connection quality within the created network by constructing greedy paths with low stretch. This ensures that greedy routing is always possible in equilibrium networks, while realistically modeling the agents' incentives for local structural changes to the network. With this we augment the elegant network creation model by Moscibroda, Schmidt, and Wattenhofer (PODC'06, [43]) with the feature of greedy routing.

For our model, we analyze the existence of (approximate)-equilibria and the computational hardness in different underlying metric spaces. E.g., we characterize the set of equilibria in 1-2-metrics and tree metrics, we show that in both metrics Nash equilibria always exist, and we prove that the well-known Θ-graph construction yields constant-approximate Nash equilibria in Euclidean space. The latter justifies distributed network construction via Θ-graphs from a new point-of-view, since it shows that this powerful technique not only guarantees networks having a low stretch but also networks that are almost stable.

CCS Concepts: - Computer systems organization → **Embedded systems**; *Redundancy*; Robotics; - Networks → Network reliability.

Additional Key Words and Phrases: Network Creation Games, Greedy Routing, Nash Equilibrium, Stretch, Theta-Graphs, Metric Space, Ad-Hoc Networks, Peer-to-Peer Networks
1
INTRODUCTION
Many important real-world networks, like the Internet or peer-to-peer ad-hoc networks among smart devices, are created by the decentralized interaction of various agents that pursue their own goals, like maximizing their centrality in the network, minimizing their latency, or maximizing the network throughput. These agents can thus be considered as acting selfishly and strategic, i.e., they individually try to optimize their costs for creating and using the network. This observation sparked a whole research area devoted to game-theoretic network formation models [45] and there is an abundance of interesting variants, typically called *network creation games*, that capture how networks emerge in different domains, e.g., communication networks or social networks.

Across various domains, the common purpose of networks is to enable communication between all the participants of the network. To this end, it is commonly assumed that shortest paths are used for routing traffic within the created network. However, to make this work, all agents need to know the global structure of the network. Moreover, in case of dynamic changes to the network, this global view must be updated or otherwise shortest path routing would fail. In case of the Internet, shortest path routing is currently ensured by the usage of extensive routing tables, that exactly specify which next-hop neighbor to use for which destination. All these routing tables must be ruff@hpi.de, Hasso Plattner Institute, University of Potsdam, Potsdam, Germany.

maintained and updated accordingly, even for insignificant changes in the network structure. A
solution to avoid the costly maintenance of such a global view is the usage of *greedy routing*, where in every network node every incoming packet is simply routed to a neighbor that is closer to the packet's destination. For this, geographic information is needed, e.g., every network node must be embedded in some underlying metric space and the positions in that space allow for deciding which next hop to use for routing. Exactly this has been proposed for the Internet [12], i.e., to map the nodes of the Internet into a metric space such that greedy routing works. This is called a greedy embedding and efficient algorithms have been proposed for computing them [10].

However, centrally computing a greedy embedding of network nodes does not account for the selfish strategic behavior of the network participants. The agents do not only want to ensure that greedy routing works, but at the same time they want to maximize their connection quality within the network, e.g., they want to minimize their average *stretch*. For two nodes, their stretch is the ratio of the length of their distance in the network and their distance in the metric space, i.e., their shortest possible distance. Thus, strategic agents would "rewire" a given greedy embedding, if this reduces their stretch. However, this might endanger greedy routing.

In this paper, we set out to investigate this tension between the stability of the network with respect to local structural changes by the agents and maintaining that greedy routing can be used.

## 1.1 Model And Preliminaries

We consider𝑛 agents that correspond to points P = {𝑝1*, . . . , 𝑝*𝑛} in some metric space M = (P,𝑑M), where 𝑑M(*𝑢, 𝑣*) denotes the distance of 𝑢 ∈ P and 𝑣 ∈ P in the metric space. Besides arbitrary metric spaces where 𝑑M has to satisfy the triangle inequality, we will also consider *1-2-metrics*, where 𝑑M(*𝑢, 𝑣*) ∈ {1, 2} for any *𝑢, 𝑣* ∈ P, *tree-metrics*, where the distances are determined by a given weighted spanning tree 𝑇, such that 𝑑M(𝑢, 𝑣) = 𝑑𝑇 (*𝑢, 𝑣*), i.e., the distance between points
𝑢, 𝑣 ∈ P is the length of the unique path between 𝑢 and 𝑣 in 𝑇, and the *Euclidean-metric*, where the points are located in Euclidean space and the distance is the Euclidean distance. We will omit the reference to the metric space M if it is clear from the context.

The goal of the agents is to create a directed network among themselves and for this each agent strategically decides over its set of outgoing directed edges. The *strategy of agent* 𝑢 is 𝑆𝑢 ⊆ 𝑉 \ {𝑢}, i.e., agent𝑢 can decide to create edges to any subset of the other agents. Moreover, let s = (𝑆1*, . . . ,𝑆*𝑛)
denote the *strategy-profile*, which is the vector of strategies of all agents. As shorthand notation, for any agent 𝑢 ∈ 𝑉 let s = (𝑆𝑢, s−𝑢), where s−𝑢 is the vector of strategies of all agents except agent 𝑢.

Any strategy-profile s uniquely defines a directed weighted network 𝐺(s) = (P, 𝐸(s), ℓ), where the edge-set 𝐸(s) is defined as 𝐸(s) = �
𝑢∈𝑉 {(*𝑢, 𝑣*) | 𝑣 ∈ 𝑆𝑢} and the length of any edge (*𝑢, 𝑣*) ∈ 𝐸(s) is equal to the distance of the positions of its endpoints in M, i.e., it is defined as ℓ(𝑢, 𝑣) = 𝑑M(*𝑢, 𝑣*).

Given a weighted directed network 𝐺 = (P*, 𝐸, ℓ*), where the nodes in P are points in metric space M, a *greedy path from* 𝑢 to 𝑣 in 𝐺 is a path 𝑥1,𝑥2*, ...,𝑥*𝑗, with 𝑥𝑖 ∈ P, for 1 ≤ 𝑖 ≤ 𝑗, where
𝑥1 = 𝑢, 𝑥𝑗 = 𝑣, and (𝑥𝑖,𝑥𝑖+1) ∈ 𝐸, for 1 ≤ 𝑖 ≤ 𝑗 − 1, such that 𝑑M(𝑥𝑖, 𝑣) > 𝑑M(𝑥𝑖+1, 𝑣) holds for all 1 ≤ 𝑖 ≤ 𝑗 − 1. Thus, such a path is a directed path from 𝑢 to 𝑣 in 𝐺, where along the path the nodes get strictly closer to the endpoint of the path in terms of their distance in the ground space M. For two nodes *𝑢, 𝑣* ∈ P, we define 𝑑greedy
𝐺
(*𝑢, 𝑣*) as the length of the shortest greedy path between 𝑢 and 𝑣 in 𝐺, where the length of a path 𝑥1,𝑥2*, ...,𝑥*𝑗 is �𝑗−1
𝑖=1 ℓ(𝑥𝑖,𝑥𝑖+1) = �𝑗−1
𝑖=1 𝑑M(𝑥𝑖,𝑥𝑖+1).

If no greedy path exists between 𝑢 and 𝑣 in 𝐺, then 𝑑greedy
𝐺
(*𝑢, 𝑣*) = ∞. We will call 𝑑greedy
𝐺
(*𝑢, 𝑣*) the greedy-routing-distance1 between 𝑢 and 𝑣 in network 𝐺. We say that *greedy routing is enabled* in 𝐺, if any pair of nodes in 𝐺 has finite greedy-routing-distance. See Figure 1 for an example.

For any two nodes 𝑢 and 𝑣 in network 𝐺, we will compare their greedy-routing-distance with their distance in the ground space M. The ratio of these values is called the *stretch*, i.e., we have
𝑑M (𝑢,𝑣)
, if a greedy path from 𝑢 to 𝑣 exists in 𝐺 , stretch𝐺 (*𝑢, 𝑣*) =
𝑍
, otherwise,
�𝑑greedy
𝐺
(𝑢,𝑣)
where 𝑍 is some arbitrarily large number that serves as a penalty for not having a greedy path.

Intuitively, the stretch measures the detour that the best greedy path has to take, compared to the shortest possible path, i.e., to having a direct edge to the target node.

Agents choose their strategy to minimize their *cost* within the formed network. The cost of agent 𝑢 in network 𝐺(s) is defined as
𝑐𝑢(s) = stretchcost𝑢(s) + edgecost𝑢(s),

where stretchcost𝑢(s) = �
                     𝑣∈P\{𝑢} stretch𝐺 (s) (𝑢, 𝑣) and edgecost𝑢(s) = 𝛼|𝑆𝑢|, for a given 𝛼 > 0.
The social cost of a network 𝐺(s) is defined as 𝑐(s) = �
                                             𝑢∈P 𝑐𝑢(s). For any set of points P, the
network 𝐺(s∗) = (P, 𝐸(s∗), ℓ) minimizing the social cost is called the social optimum network for P.
 An improving response for an agent 𝑢 for a strategy-profile s = (𝑆𝑢, s−𝑢) is a strategy 𝑆′
                                                                       𝑢 such
that 𝑐𝑢((𝑆′
       𝑢, s−𝑢)) < 𝑐𝑢((𝑆𝑢, s−𝑢)), i.e., by employing strategy 𝑆′
                                                  𝑢, agent 𝑢 has strictly lower cost
compared to using strategy 𝑆𝑢. A strategy 𝑆∗
                                 𝑢 is called a best response for agent 𝑢 for strategy-profile
s = (𝑆𝑢, s−𝑢), if 𝑐𝑢(𝑆∗
               𝑢, s−𝑢) ≤ 𝑐𝑢(𝑆′
                          𝑢, s−𝑢) for any other strategy 𝑆′
                                                  𝑢 ⊆ 𝑉 \ {𝑢}, i.e., a best response
strategy minimizes agent 𝑢's cost, given that the strategies of the other agents are fixed.
 A strategy-profile s is in pure Nash Equilibrium (NE) if no agent has an improving move for s, i.e.,
in s every agent already employs a best response. Since we have bijection between strategy-profiles
s and the corresponding networks 𝐺(s), we will say that network 𝐺(s) is in NE, if s is in NE. A
network 𝐺(s) is in Greedy Equilibrium (GE) [38] if no agent has an improving response that differs
from its current strategy in adding, swapping or deleting a single incident outgoing edge, where
a swap is a combination of deleting an incident outgoing edge and adding another one. Notice
that any network in NE is also in GE. A network 𝐺(s) is in 𝛽-approximate NE (𝛽-NE) if no agent 𝑢

1Note that the greedy-routing distance only depends on the network 𝐺 and the metric space M but not on any concrete
greedy routing protocol. This more abstract definition ensures robust bounds, since our distance measure always gives a
lower bound on the distance achieved by any particular greedy routing protocol.

can change its strategy such that its cost decreases below 1
𝛽𝑐𝑢(s), i.e., no agent has an improving response that reduces its cost by at least a factor of 𝛽.

An *improving (best) response path* is a sequence of strategy-profiles s0, s1, s2*, . . . ,* s𝑘, such that s𝑖 results from some agent changing to an improving (best) response in s𝑖−1, for 1 ≤ 𝑖 ≤ 𝑘. An improving (best) response cycle (IRC or BRC, respectively) is a cyclic improving response path, i.e., where s0 = s𝑘 holds. By definition, every best response path (cycle) is also an improving response path (cycle). The non-existence of improving response cycles, i.e., if every improvement path has finite length, is equivalent to the existence of an ordinal potential function [42]. The latter implies that NE can be found via natural sequential improvement dynamics. A strategic game is called weakly acyclic (weakly acyclic under best response) if from every strategy vector s there exists a finite improving (best) response path that starts in s and ends in a NE.

## 1.2 Related Work

Network Creation Games (NCGs) were first introduced by Fabrikant, Luthra, Maneva, Papadimitriou, and Shenker [27]. In their model, agents that correspond to nodes of a network strategically create incident undirected edges with the goal of minimizing their sum of hop-distances to all other agents.

They use constant edge costs, i.e., every edge costs 𝛼 > 0. As main results, they showed that NE
always exist, that the network minimizing the social cost is either a clique or a star, depending on 𝛼, and that computing a best response is NP-hard. Later, the Price of Anarchy was bounded by𝑜(𝑛𝜀) for any 𝜀 > 0 [23], and it was shown to be constant for wide range of 𝛼 [5, 23]. Also, it was shown that NCGs admit improving response cycles [35] and that any network in GE is in 3-NE [38]. Moreover, many variations of NCGs have been proposed and investigated, e.g., a bilateral version where both endpoints of an edge have to agree and pay for the edge [19, 29], variants with locality [8, 9, 21], with robustness considerations [16, 24, 40], with budget constraints [25, 37], with non-uniform edge prices [6, 15, 22, 39], and versions where only edge swaps are allowed [4, 20, 33, 41].

Closer to our model are NCGs that involve geometry. In the wireline strong connectivity game [26]
agents that correspond to points in the plane create undirected edges to ensure that they can reach all other agents. It is assumed that the cost of an edge equals its length. For this setting, NE exist and can be found efficiently. Geometric spanner games [1] are similar, but the agents want to ensure a given maximum stretch. While guaranteed existence of NEs was left open, it is shown that computing a best response is NP-hard. Bilò, Friedrich, Lenzner, and Melnichenko [7] defined a similar geometric model with undirected edges, where the agents want to minimize the sum of their shortest path distances to all other agents. They consider similar metrics as in our paper, in particular, they show that NE exist in 1-2-metrics and tree-metrics and that every GE is in 3-NE for any metric. Also, they prove that even on 1-2-metrics computing a best response is NP-hard. Later, it was shown that (𝛼 + 1)-NE always exist [28]. Closest to our model is the work by Moscibroda, Schmid, and Wattenhofer [43]. Their model involves agents that form directed edges and that have the same cost function as in our model. Thus, the main difference to our model is that instead of greedy paths they use shortest paths for defining the stretch. They show for Euclidean metrics that NE may not exist and that deciding NE existence is NP-hard.

To the best of our knowledge, the only exists one model that combines network creation with greedy routing, introduced by Gulyás, Biró, Kőrösi, Rétivári, and Krioukov [32]. In contrast to our model, their agents only want to ensure to reach all other agents via greedy routing. Also, they fix
𝛼 = 1 and hyperbolic space is assumed. However, their cost function only enforces greedy routing locally, i.e., that agents have edges to nodes that are closer to any possible destination. Thus, agents do not influence each other, i.e., this is not a game-theoretic setting.

Another line of research is to investigate specific random graph models that generate networks where greedy routing almost surely succeeds. Also for this, hyperbolic space is essential [11, 14].

1.3
Our Contribution We consider an augmented variant of the network creation model by Moscibroda, Schmidt, and Wattenhofer [43]. The key new feature of our model is that the agents that want form a communication network explicitly aim for creating a network where greedy routing between all pairs of nodes is possible. At the same time, each agent tries to find a sweet-spot between establishing costly direct connections and maintaining a low average stretch. Besides this new conceptual feature, we also extend the previous work by focusing on specific metrics like 1-2-metric, tree metrics and Euclidean metrics. This is valuable, since we show that the underlying metric has a severe influence on the obtained game-theoretic properties and the complexity of the involved computational problems. See Table 1 for a summary of most of our results.

For networks created in a 1-2-metric, we show that Nash equilibria always exist. Moreover, we characterize the set of all NEs for every edge price 𝛼. In particular, we show that all NEs must have a specific structure. Considering a weaker form of stability, we characterize the set of networks that are in Greedy Equilibrium. Also, we show that best response cycles are impossible, but that improving response cycles exist. Thus, best response dynamics are suitable for finding equilibria.

However, regarding the complexity, we show that for 𝛼 > 1
2 computing a best response and deciding if a given network is in NE is NP-hard. This raises the question of how to find equilibria efficiently.

For this, we show that O(log𝑛)-approximate Nash equilibria can be found in polynomial time.

Moreover, for 𝛼 ≤ 1
2 NEs can be computed efficiently.

In tree-metrics the picture changes drastically. We still have guaranteed existence of NE, but here we find that NEs (and even GEs) are unique and can be computed efficiently for any edge price
𝛼. Also, the game is weakly-acyclic under best responses, but computing a best response is NP-hard For Euclidean metrics, i.e., the case that is most relevant for practical applications, we transfer several negative results from [43] to our extended model: there are instances where no GE exist, which implies that also Nash equilibria are not guaranteed to exist. Moreover, computing a best response is NP-hard. On the positive side, show that the well-known Θ-graph-construction can be employed to efficiently compute a 4.87-approximate Nash equilibrium. While this concept is already known for guaranteeing low stretch, we further support the use of Θ-graphs by showing that at the same time, they also guarantee an almost stable network, i.e., the agents have a low incentive for local structural changes.

Finally, for general metric spaces, we adapt the proof from [43] that deciding if an instance admits a NE or a GE is NP-hard. On the positive side, we show that (𝛼 + 1)-approximate Nash equilibria always exist and can be computed efficiently.

2
1-2 METRICS
We consider metrics M where for every pair of nodes *𝑢, 𝑣* we have 𝑑M(*𝑢, 𝑣*) ∈ {1, 2}. We denote edges of weight 1 and 2 as *1-edges* and *2-edges*, respectively. 1-2-metrics is the simplest class of non-trivial metric spaces and they have often been studied, e.g., for the TSP [2, 34].

In spaces where all edges have the same length, direct edges would be the only possible greedy paths and as such the agents' strategies would be independent of each other. We start by giving some general statements about greedy paths and agent strategies in 1-2-metrics.

Lemma 2.1. *For any network in a 1-2-metric, all greedy paths have stretch* 1 or 3
2 and consist of at most two edges.

| 1-2                        | Tree                | Euclidean           | General      |
|----------------------------|---------------------|---------------------|--------------|
| NE                         |                     |                     |              |
| NE always exist            | NE always exist     | no existence        | no existence |
| characterization for every |                     |                     |              |
| 𝛼                          |                     |                     |              |
| GE unique                  |                     |                     |              |
| Complexity                 |                     |                     |              |
| 𝛼                          | >                   |                     |              |
| 1                          |                     |                     |              |
| /                          |                     |                     |              |
| 2: BR-decision NP-hard     | BR NP-hard          | BR NP-hard          | BR NP-hard   |
| NE-decision NP-hard        | NE-decision P       | NE-decision NP-hard |              |
| 𝛼                          |                     |                     |              |
| ≤                          |                     |                     |              |
| 1                          |                     |                     |              |
| /                          |                     |                     |              |
| 2: BR-decision P           | GE-decision NP-hard |                     |              |
| NE-decision P              |                     |                     |              |
| Approx-NE                  |                     |                     |              |
| O(                         |                     |                     |              |
| log                        |                     |                     |              |
| 𝑛                          |                     |                     |              |
| )                          |                     |                     |              |
| 1                          | 4                   |                     |              |
| .                          |                     |                     |              |
| 87                         |                     |                     |              |
| 𝛼                          |                     |                     |              |
| +                          |                     |                     |              |
| 1                          |                     |                     |              |

Proof. Let *𝑢, 𝑣* ∈ P and 𝑢 ≠ 𝑣. If 𝑑(*𝑢, 𝑣*) = 1, there can be no other node closer to 𝑣 than 𝑢. Thus, the only possible greedy path is *𝑢, 𝑣* with a stretch of 1 that uses one edge. Otherwise, 𝑑(*𝑢, 𝑣*) = 2, and only nodes 𝑥 with 𝑑(*𝑥, 𝑣*) = 1 are closer to 𝑣 than 𝑢 and no other node is closer to 𝑣 than any such 𝑥. Thus, the only possible greedy paths are *𝑢, 𝑣* and *𝑢,𝑥, 𝑣* for any such 𝑥. These paths use one or two edges, respectively, and have stretches of 1 and either 1 or 3
2 depending on 𝑑(𝑢,𝑥).

□
When examining these possible greedy paths, we also directly get the following statement.

Remark 2.2. For any network in a 1-2-metric, 2-edges can only be the first edge of any greedy path.

Also, we find that 1-edges are crucial for enabling greedy routing.

Lemma 2.3. For any network in a 1-2-metric, if greedy routing is enabled then all 1-edges are built in both directions.

Proof. For the sake of contradiction, let *𝑢, 𝑣* ∈ P be such that 𝑑(*𝑢, 𝑣*) = 1 but there is no edge between 𝑢 and 𝑣 that 𝑢 can use as greedy path, i.e., agent 𝑢 does not build an edge to 𝑣. However, without such an edge no greedy path from 𝑢 to 𝑣 can exist because no other node can be closer to 𝑣
than 𝑢 itself, a contradiction.

□

## Equilibrium Existence. We Start By Showing The Equivalence Of Ne And Social Optima.

Theorem 2.4. In a 1-2-metric, every NE is a social optimum and every social optimum is a NE.

Proof. First, by Lemma 2.3, every outgoing 1-edge incident to an agent 𝑢 ∈ P needs to be part of all of its best responses. Second, by Remark 2.2, no 2-edge that any agent builds can be part of a greedy path that is used by any other agent. Thus, the strategy of an agent 𝑢 ∈ P does not influence the cost function of any other agent 𝑣 ∈ P \ {𝑢} beyond the 1-edges that need to be part of every strategy with costs less than 𝑍. Using this, we show by contradiction that every NE is a social optimum and vice versa.

If there was a NE that is not a social optimum, the latter would have lower social cost than the NE and thus, some agent 𝑢 must have lower cost in the social optimum compared to its cost in the NE. Hence, it could reduce its cost by deviating to its strategy in the social optimum network.

In the same vein, if there was a social optimum network that is not in NE, an agent 𝑢 would have an improving move that would also improve the social cost.

□
This implies that NE always exist. In the following we characterize all NEs. For this, we introduce Domination Set Graphs, which are based on the notion of a *directed dominating set* [30] of a directed graph 𝐺 = (*𝑉, 𝐸*). For any node 𝑢 ∈ 𝑉 , let 𝑊1(𝑢),𝑊1→1(𝑢),𝑊2(𝑢) denote the sets of nodes that node 𝑢 can reach by a 1-edge, by a path of two 1-edges, and by a 2-edge, respectively. We denote

by 𝑊 −
    2 (𝑢) the set of nodes that 𝑢 builds a 2-edge to and that 𝑢 cannot reach via a path of two
1-edges, i.e. 𝑊 −
           2 (𝑢) = 𝑊2(𝑢) \𝑊1→1(𝑢), and let 𝑊 +
                                       2 (𝑢) be the set of nodes from 𝑊2(𝑢) to which 𝑢
also has a path of two 1-edges, i.e., 𝑊 +
                              2 (𝑢) = 𝑊2(𝑢) ∩𝑊1→1. Note that 𝑊2(𝑢) = 𝑊 −
                                                                 2 (𝑢) ∪𝑊 +
                                                                         2 (𝑢)
and 𝑊 −
    2 (𝑢) ∩𝑊 +
            2 (𝑢) = ∅. The out-neighborhood of 𝑢 is the set 𝑁 (𝑢) = 𝑊1(𝑢) ∪𝑊2(𝑢).
 Subset 𝐷 ⊆ 𝑉 is dominating, if for every node 𝑣 ∈ 𝑉 \ 𝐷 there exists a node 𝑢 ∈ 𝐷 such that
(𝑢, 𝑣) ∈ 𝐸. For this we say that 𝑢 dominates 𝑣 and that 𝑢 dominates its out-neighborhood.

  Definition 2.5. Let 𝐺1
                        −𝑢 = �P \ {𝑢}, 𝐸1
                                          −𝑢
                                             � be the network without node 𝑢 that only contains all
the 1-edges, i.e., we have that 𝐸1
                                 −𝑢 =
                                       �
                                         (𝑣,𝑤) ∈ (P \ {𝑢})2 | 𝑑(𝑣,𝑤) = 1
                                                                            �
                                                                             .
  A Domination Set Graph (DSG) on a 1-2-metric (P,𝑑) is a network 𝐺 = (P, 𝐸) with:

(i) 𝐸 ⊇ {(𝑣,𝑤) ∈ P2 | 𝑑(𝑣,𝑤) = 1},
(ii) for every node 𝑢, its out-neighborhood must be dominating in the network 𝐺1
                                                                                                                  −𝑢, and

(iii) |𝑊 +
          2 (𝑢)| cannot be decreased by a single edge deletion or swap without increasing |𝑁 (𝑢)|.

  By (i), a DSG includes all 1-edges, by (ii), for every node 𝑢, its out-neighborhood is dominating
in the network without 𝑢 consisting of only the 1-edges. Condition (iii) states that in a DSG an
edge to a node 𝑣 ∈ 𝑊 +
                     2 (𝑢) cannot be removed or swapped with another one to a node 𝑤 ∉ 𝑊1→1(𝑢)
without resulting in the out-neighborhood of 𝑢 no longer being dominating in the network 𝐺1
                                                                                                  −𝑢.
  We now define more specific DSGs:

  Definition 2.6. A Minimum Domination Set Graph (MinDSG) is a DSG in which for every node 𝑢
its out-neighborhood contains all nodes reachable via 1-edges and the minimum number of nodes
reachable via 2-edges so that it is dominating in 𝐺1
                                                        −𝑢. Thus, all out-neighborhoods are minimum
size dominating sets given that they need to include all nodes reachable via 1-edges.

  Definition 2.7. A Maximum Domination Set Graph (MaxDSG) is a DSG that contains all possible
edges, except 2-edges (𝑢,𝑤), where (𝑢, 𝑣) and (𝑣,𝑤) both are 1-edges.

Note that MaxDSGs are unique and the stretch between any pair of nodes in a MaxDSG is 1.

2
 � |𝑊2(𝑢)| + 1

2, the BDSG corresponds to the MaxDSG.

  Definition 2.8. A Balanced Domination Set Graph for 𝛼 > 0 (BDSG(𝛼)), is a subclass of Domination
Set Graphs, where for any node 𝑢, the quantity �𝛼 − 1

                                                                             2 |𝑊 +
                                                                                 2 (𝑢)| is minimized, achieving
a balance between the number of 2-edges that 𝑢 builds in total, and the number of 2-edges to nodes
in 𝑊1→1(𝑢). Note that for 𝛼 < 1

See Figure 2 for examples. Next, we show that DSGs are useful for our analysis.

Lemma 2.9. In a 1-2-metric any network in GE is a DSG.

  Proof. By Lemma 2.3, all 1-edges need to be built in a GE network and thus condition (i) of a
DSG is met. Next, assume for the sake of contradiction, that condition (ii) of a DSG is violated and
that the set 𝑁 (𝑢) of nodes that some agent 𝑢 builds edges to is not dominating in 𝐺1
                                                                         −𝑢. In other
words, there is some node 𝑣 such that neither it nor any of its in-neighbors are in 𝑁 (𝑢). Thus, the
shortest path from 𝑢 to 𝑣 has at least 3 edges. By Lemma 2.1, no such path can be a greedy path
and thus agent 𝑢 could improve its cost by building an edge to 𝑣. Finally, we consider condition
(iii) that states that for any agent 𝑢, the size of |𝑊 +
                                          2 (𝑢)| cannot be decreased by a single operation
without increasing |𝑁 (𝑢)|, provided that 𝑁 (𝑢) is dominating in 𝐺1
                                                       −𝑢. For the sake of contradiction,
let us assume that this condition is violated in a GE network. There are two cases that this can
happen. In the first case, some agent 𝑢 removes an edge to a node 𝑣 ∈ 𝑊 +
                                                                2 (𝑢), while agent 𝑢's
out-neighborhood is still dominating in 𝐺1
                                   −𝑢. Thus, agent 𝑢 could reduce its edgecosts by removing
this edge, while its stretchcosts are not increased since the stretch to 𝑣 is already 1 (there is a path of
two 1-edges from 𝑢 to 𝑣) and the stretches to every other node remain the same. In the second case,

strategy in a BDSG since 0.5|𝑊2(𝑎)| + 0.5|𝑊 +
2 (𝑎)| is not minimal.

some agent 𝑢 swaps an edge to a node 𝑣 ∈ 𝑊 +
                                      2 (𝑢) with one to a node 𝑤 ∉ (𝑊2(𝑢) ∪𝑊1→1(𝑢)), while
agent 𝑢's out-neighborhood is still dominating in 𝐺1
                                              −𝑢. Thus, agent 𝑢 could reduce its stretchcost,
since the stretch to 𝑤 would become 1 instead of 3

                                                           2, while its edgecosts and the stretches to every
other node remain the same. Thus, we have that every GE is a DSG.
                                                                                                                  □

Lemma 2.10. In a 1-2-metric, in any DSG greedy routing is enabled.

  Proof. Every agent 𝑢 trivially has a greedy path to any node that it builds an edge to. For any
node 𝑣 that 𝑢 does not build an edge to, there is still a node 𝑥 in distance 1 from 𝑣 that 𝑢 builds an
edge to because the out-neighborhood of 𝑢 is by definition a dominating set in 𝐺1
                                                                    −𝑢. Thus, the path
𝑢,𝑥, 𝑣 exists in the DSG and it is a greedy path because 𝑑(𝑢, 𝑣) = 2 > 1 = 𝑑(𝑥, 𝑣).
                                                                                 □

We now show that DSGs can be used to characterize NE.

Theorem 2.11. In a 1-2-metric, for any 𝛼 > 0, all BDSG(𝛼) are the only NE.

  Proof. Let 𝑉1(𝑢) = {𝑣 ∈ P | 𝑑M(𝑢, 𝑣) = 1} and 𝑉2(𝑢) = {𝑣 ∈ P | 𝑑M(𝑢, 𝑣) = 2} be the
sets of nodes in distance 1 and in distance 2 from agent 𝑢 in the ground space. Also, let 𝑉 +
                                                                             2 (𝑢) =
𝑉2(𝑢) ∩𝑊1→1(𝑢) denote the set of nodes in distance 2 from 𝑢 that can be reached by a path of two
1-edges, and 𝑉 −
            2 (𝑢) = 𝑉2(𝑢) \𝑉 +
                          2 (𝑢) the set of nodes in distance 2 from agent 𝑢 that 𝑢 cannot reach
via a path of two 1-edges. Thus, we have 𝑉2(𝑢) = 𝑉 +
                                          2 (𝑢) ∪𝑉 −
                                                  2 (𝑢). The cost of any strategy-profile s
for agent 𝑢 is equal to

𝑐𝑢(s) = |𝑉1(𝑢)| + |𝑉 +
                    2 (𝑢)| + |𝑊 −
                               2 (𝑢)| + 3

By rearranging terms, we get:

2 � |𝑉 − 2 (𝑢)| − |𝑊 − 2 (𝑢)| � + 𝛼 �|𝑊 + 2 (𝑢)| + |𝑊 − 2 (𝑢)| + |𝑉1(𝑢)|� . 2 𝑐𝑢(s) = (𝛼 + 1)|𝑉1(𝑢)| + |𝑉 + 2 (𝑢)| + � 𝛼 − 1 � |𝑊 − 2 (𝑢)| + 3 2 |𝑉 − 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)|. (1)
Now, let s denote the strategy-profile of a BDSG(𝛼) network 𝐺(s). Assume towards a contradiction that there is an agent 𝑢 ∈ P that could decrease its cost in 𝐺(s) = 𝐺((𝑆𝑢, s−𝑢)) by deviating to some other strategy 𝑆𝑢 ≠ 𝑆𝑢. Let s = (𝑆𝑢, s−𝑢) denote the strategy-profile after the deviation of agent 𝑢. Note that, by Lemma 2.3, also in s all 1-edges have to be built, in particular, all outgoing 1-edges of agent 𝑢, since otherwise greedy routing would not be enabled and thus agent 𝑢 could not decrease its cost. Let𝑉1(𝑢),𝑉 +
2 (𝑢),𝑉 −
2 (𝑢),𝑊 +
2 (𝑢) and𝑊 −
2 (𝑢) denote the sets from

equation (1) with respect to strategy profile s and let 𝑉1(𝑢),𝑉 +
                                                              2 (𝑢),𝑉 −
                                                                      2 (𝑢),𝑊 +
                                                                              2 (𝑢) and𝑊 −
                                                                                          2 (𝑢) be the
sets from equation (1) for strategy-profile s. Also, remember that 𝑊2(𝑢) = 𝑊 +
                                                                               2 (𝑢) ∪𝑊 −
                                                                                         2 (𝑢) and let

𝑊2(𝑢) = 𝑊 +
     2 (𝑢) ∪𝑊 −
         2 (𝑢). Now, observe that 𝑉1(𝑢) = 𝑉1(𝑢), 𝑉 +
                             2 (𝑢) = 𝑉 +
                                 2 (𝑢), and 𝑉 −
                                       2 (𝑢) = 𝑉 −
                                           2 (𝑢),
since these sets only depend on the 1-edges built by agent 𝑢, which are the same in s and s. Thus,
equation (1) gives agent 𝑢's cost in strategy-profile s. For strategy-profile s, equation (1) yields

2 𝑐𝑢(s) = (𝛼 + 1)|𝑉1(𝑢)| + |𝑉 + 2 (𝑢)| + � 𝛼 − 1 � |𝑊 − 2 (𝑢)| + 3 2 |𝑉 − 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)|, (2)

Thus, using equation (1) and equation (2), that |𝑊2(𝑢)| = |𝑊 +
                                                             2 (𝑢)| + |𝑊 −
                                                                       2 (𝑢)|, that |𝑊2(𝑢)| =
|𝑊 +
  2 (𝑢)| + |𝑊 −
            2 (𝑢)|, and that agent 𝑢 has strictly lower cost in s compared to s, we have

2 2
𝑐𝑢(s) < 𝑐𝑢(s)
�
𝛼 − 1

� |𝑊 − 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)| < � 𝛼 − 1 2 2 � |𝑊 − 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)| � 𝛼 − 1 � �|𝑊2(𝑢)| − |𝑊 + 2 (𝑢)|� + 𝛼|𝑊 + 2 (𝑢)| < � 𝛼 − 1 2 2 2 2 � |𝑊2(𝑢)| − � 𝛼 − 1 � |𝑊 + 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)| < � 𝛼 − 1 � |𝑊2(𝑢)| − � 𝛼 − 1 � � |𝑊2(𝑢)| − |𝑊 + 2 (𝑢)| � + 𝛼|𝑊 + 2 (𝑢)| � 𝛼 − 1 2 2 � |𝑊2(𝑢)| + 1 � |𝑊2(𝑢)| + 1 � |𝑊 + 2 (𝑢)| + 𝛼|𝑊 + 2 (𝑢)| � 𝛼 − 1 2 |𝑊 + 2 (𝑢)| < � 𝛼 − 1 2 |𝑊 + 2 (𝑢)|.
This is a contradiction, because according to the definition of a BDSG(𝛼), in 𝐺(s) no agent 𝑢 can decrease the quantity 𝑏 = (𝛼 − 0.5)|𝑊2(𝑢)| + 0.5|𝑊 +
2 (𝑢)|. However, strategy 𝑆𝑢 of agent 𝑢 strictly decreases 𝑏. Therefore, a BDSG(𝛼) is a NE for any 𝑎 > 0, and it is the only one.

□
Theorem 2.12. *In a 1-2-metric we have that (i) for* 𝛼 < 1
2, the MaxDSG is the only NE, (ii) for
𝛼 = 1
2, all DSGs are the only GE, but only the DSGs where no node builds edges to nodes reachable by two 1-edges are the only NE, (iii) for 𝛼 > 1
2, all MinDSG are GE.

Proof. First, let 𝛼 < 1
2. From Theorem 2.11 we have that *𝐵𝐷𝑆𝐺*(𝛼) are the only NE. When
𝛼 < 1
2, the network *𝐵𝐷𝑆𝐺*(𝛼) corresponds to the MaxDSG. Thus, the MaxDSG is the only NE.

Next, let 𝛼 = 1
2. Then, the network *𝐵𝐷𝑆𝐺*(𝛼) corresponds to DSGs where for every node 𝑢 the quantity |𝑊 +
2 (𝑢)| is minimized, i.e. no node builds edges to nodes that are reachable by two 1-edges.

Thus, this category of DSGs are the only NE.

Regarding GE, every DSG is a GE because removing any edge would either remove all greedy paths to some node or increase the stretch to the endpoint of the edge by at least 1
2 = 𝛼. Also adding any edge would decrease stretches by at most 1

adding any edge would decrease stretches by at most $\frac{1}{2}=\alpha$. Swapping an edge also cannot decrease stretches. The number of edges an agent $u$ builds remains the same after a swap. Consequently, agent $u$ can reduce its cost only by reducing its stretchcost. The stretchcost of agent $u$ is equal to

$$\frac{3}{2}\left(|V|-1\right)-\frac{1}{2}\left(|W_{1}(u)|+|W_{1-1}(u)|+|W_{2}^{-}(u)|\right)\tag{3}$$

since, by Lemma 2.1, all greedy paths have stretches $1$ or $\frac{3}{2}$. By Lemma 2.3, all 1-edges have to be built to enable greedy routing, thus agent $u$ can only swap 2-edges.

If after one swap the size of $|W_{2}^{-}(u)|$:

* decreases, then the stretchcost of agent $u$ increases because of (3):
- decreases, then the stretchcost of agent 𝑢 increases because of (3);

- remains the same, then the stretchcost of agent 𝑢 will remain the same;
- increases, that means that |𝑊 +
2 (𝑢)| will be decreased. By the definition of a DSG, the value
|𝑊 +
2 (𝑢)| cannot be decreased without increasing the size of the out-neighborhood of𝑢. Since
we are considering swaps, the number of edges that 𝑢 builds cannot change, a contradiction.
Therefore, swapping an edge is not an improving move for agent 𝑢. Since, by Lemma 2.9, all GE are
DSG, there can be no other GE.
Next, let 𝛼 > 1
2. Every MinDSG is a GE because removing an edge would also remove all greedy paths to some node and adding an edge would decrease stretches by at most 1
2 < 𝛼. As we showed before, swapping an edge is not an improving move either.

□
Dynamic Properties. We explore if NE networks can be found by allowing agents iteratively to select improving or best responses. First, we show that improving response cycles (IRCs) exist.

Then we contrast this with the positive result that best response cycles (BRCs) cannot exist. The proof of the former relies on the absence of greedy paths between certain agents, resulting in costs higher than 𝑍. This is necessary, since no IRCs can exist if the costs of all agents are less than 𝑍, i.e., if the network already enables greedy routing. This can be proven with the same arguments used below to show that best response cycles cannot exist.

Theorem 2.13. In a 1-2-metric, IRCs can exist for any 𝛼 > 0.

Proof. We show that there is an IRC in the metric shown in Figure 3a regardless the value of 𝛼.

In particular, in each step of the IRC, the stretchcosts of the agents that changes its strategy improves by exactly 𝑍 − 1. By definition of 𝑍, this will always outweigh any changes in the edgecosts, since agents always build the same number of edges of the same length.

Consider the network shown in Figure 3b. If agent 𝑢 changes its strategy from {𝑐,𝑑,𝑖} to {*𝑎,𝑏, 𝑣*}
we get the network shown in Figure 3c. With this agent 𝑢 only loses greedy paths of length 1 to the three nodes *𝑐,𝑑* and 𝑖 and of length 2 (and stretch 1) to node 𝑗 but it gains greedy paths of length 1 to the three nodes *𝑎,𝑏* and 𝑣 and of length 2 (and stretch 1) to the two nodes 𝑒 and 𝑓 . Thus, agent
𝑢's stretchcost improves by 𝑍 − 1.

a
u
c
a
u
a
c
u
a
c
u
a
c
u
c
u
u
u
u
u
d
d
d
d
d
i
i
i
i
i
b
b
b
b
b
j
j
j
j
j
f
f
f
f
f
h
h
h
h
h
e
e
v
g
e
e
e
vv
g
vv
g
vv
g
vv
g

In the network depicted in Figure 3c, if agent 𝑣 changes its strategy from {𝑒, 𝑓 ,𝑢} to {*ℎ,𝑔,𝑖*}
we get the network shown in Figure 3d. With this agent 𝑣 only loses greedy paths of length 1 to the three nodes *𝑒, 𝑓* and 𝑢 (note that the paths *𝑣,𝑢,𝑎* and *𝑣,𝑢,𝑏* are not greedy paths) but at the same time it establishes greedy paths of length 1 to the three nodes *𝑔,ℎ* and 𝑖 and of length 2 (and stretch 1) to 𝑗. Thus, agent 𝑣's stretchcosts improve by 𝑍 − 1.

In the network shown in Figure 3d, if agent 𝑢 changes its strategy {𝑎,𝑏, 𝑣} to {*𝑐,𝑑,𝑖*} we get the network shown in Figure 3e. With this, agent 𝑢 loses greedy paths of length 1 to the three nodes
𝑎,𝑏 and 𝑣 but it gains greedy paths of length 1 to the three nodes *𝑐,𝑑* and 𝑖 and of length 2 (and stretch 1) to 𝑗. Thus, agent 𝑢's stretchcosts improve by 𝑍 − 1.

Finally, if in the network shown in Figure 3e agent 𝑣 changes its strategy {ℎ,𝑔,𝑖} to {*𝑒, 𝑓 ,𝑢*} we get the network shown in Figure 3b. With this strategy change, agent 𝑣 only loses greedy paths of length 1 to the three nodes *𝑔,ℎ* and 𝑖 and of length 2 (and stretch 1) to 𝑗 but it gains greedy paths of length 1 to the three nodes *𝑒, 𝑓* and 𝑢 and of length 2 (and stretch 1) to the two nodes 𝑐 and 𝑑. Thus, agent 𝑣's stretchcost improves by 𝑍 − 1. As this is the same strategy-profile that we started with, we have found an improving response cycle.

□
Interestingly, if the agents iteratively select best response strategies, then no such cyclic behavior can occur. Thus, best response dynamics starting from any initial network are guaranteed to converge to a NE network. However, we will show later that computing a best response is hard.

Theorem 2.14. In a 1-2-metric, best response cycles cannot exist.

Proof. By Lemma 2.3, all best responses always build all 1-edges and thus, a best response cycle can never include changes of the 1-edges. By Remark 2.2, no 2-edge that any agent builds can be part of a greedy path that is used by any other agent and thus, any best response cycle cannot consist solely of changes of 2-edges either. Thus, best response cycles cannot exist.

□
Computational Complexity. Here, we investigate the computational complexity of computing a best response and of deciding if a given network is in NE. We use our characterization theorem and the tight connection to the Minimum Dominating Set problem, which asks for minimum size dominating set for a given network 𝐺. It is well-known that Minimum Dominating Set is NP-hard [31]. We get the following dichotomy results:
Theorem 2.15. In a 1-2-metric, computing a best response and deciding if a given network is in NE
is NP-hard for 𝛼 > 1
2.

2 *and polynomial time computable for* 𝛼 ≤ 1
Proof. We first show that computing a best response strategy is NP-hard with 𝛼 > 1

Proof. We first show that computing a best response strategy is NP-hard with $\alpha>\frac{1}{2}$. For this, we reduce from the Minimum Dominance Set problem. Given any graph $G=(V,E)$ for which we want to compute a minimum size dominating set. We embed the nodes of $G$ as follows into a 1-2-metric: Let $\mathcal{M}=(V\cup\{u\},d)$ be a 1-2-metric, with $u\notin V$ being a new node, where for all $x,y\in V\cup\{u\}$ we have

$$d(x,y)=\begin{cases}1&\text{,if}(x,y)\in E,\\ 2&\text{,otherwise.}\end{cases}$$
Furthermore, let s be a strategy-profile where in 𝐺(s) = (𝑉 ∪ {𝑢}, 𝐸(s)) all the edges in 𝐺 are built in both directions but no other edges. We now consider the best response of agent 𝑢 and let 𝐷 be the set of nodes that agent 𝑢 builds edges to in its best response in 𝐺(s). Since we have 𝑑(𝑢,𝑥) = 2
for every node 𝑥 ∈ 𝑉 , it follows that node 𝑢 has a stretch of 1 to all nodes in 𝐷 and a stretch of 3
2 to all nodes 𝑤 ∈ 𝑉 \ 𝐷 such that there exists a node 𝑣 ∈ 𝐷 with (𝑣,𝑤) ∈ 𝐸(s), i.e, the edge (𝑣,𝑤) is a 1-edge in 𝐺(s). Let 𝐶 be the set of these nodes, i.e., 𝐶 = {𝑤 ∈ 𝑉 \ 𝐷 | ∃𝑣 ∈ 𝐷 ∧ (𝑣,𝑤) ∈ 𝐸(s)}. Note that for any node 𝑧 ∈ 𝑉 \ (𝐶 ∪ 𝐷 ∪ {𝑢}), there cannot exist a greedy path from 𝑢 to 𝑧, since, by Lemma 2.1, any such path can have at most two edges. Thus, since for any such node 𝑧 agent 𝑢
would incur stretchcost of 𝑍 > 𝛼 + 3
2, no such node 𝑧 can exist if 𝐷 is agent 𝑢's best response. In this case, building an edge to 𝑧 would strictly decrease agent 𝑢's cost, i.e., we have that 𝐶 ∪ 𝐷 = 𝑉 .

Thus, the set 𝐷 must be a dominating set in 𝐺. Since every edge costs 𝛼 > 1
2 and building an edge to a node 𝑥 ∈ 𝑉 can decrease its stretchcost at most by 1
2, agent 𝑢's best response should buy as few edges as possible such that greedy routing is enabled, i.e., the set 𝐷 must be a minimum size dominating set in 𝐺. Thus, computing a best response strategy for agent 𝑢 is NP-hard.

Next, if we have 𝛼 ≤ 1
2 then the proof of Theorem 2.12 implies for every agent 𝑢 that building all the edges that are incident outgoing edges of 𝑢 in the unique MaxDSG is a best response. This can be computed in polynomial time, since these are all outgoing edges, except the 2-edges (𝑢,𝑤), where (*𝑢, 𝑣*) and (𝑣,𝑤) both are 1-edges.

The NP-hardness of deciding if a given network 𝐺 is in NE in a 1-2-metric follows from Theorem 2.11. There it is shown that for 𝛼 > 1
2 all NE must be BDSG(𝛼), i.e., the strategy of every agent
𝑢 must minimize the quantity (𝛼 − 1
2)|𝑊2(𝑢)| + 1
2 |𝑊 +
2 (𝑢)|. When |𝑊 +
2 (𝑢)| = 0, this corresponds to a minimum dominating set for the network 𝐺1
−𝑢 and this network can be arbitrary.

Finally, deciding if a given network is in NE with 𝛼 ≤ 1
2 can be done in polynomial time by Theorem 2.12.

□
The characterization in Theorem 2.12 and the above results directly imply that our results also hold for the problem of computing a NE network. This is true since MaxDSGs can be computed in polynomial time, whereas computing a MinDSG is NP-hard.

Corollary 2.16. *In a 1-2-metric computing a NE can be done in polynomial time if* 𝛼 ≤ 1
2 and it is NP-hard if 𝛼 > 1
2.

Greedy Equilibria. Since computing a best response is NP-hard if 𝛼 > 1
2, it is natural to consider simpler strategy changes, where an agent can only add, delete or swap a single edge to decrease its cost. Networks where no such strategy changes can improve the agents' cost are exactly the set of Greedy Equilibria (GE) [38]. For other related variants of network creation games, it has been shown that GE are good approximations of NE, i.e., that every GE is a 3-NE [7, 38]. We now show, that enforcing greedy routing changes this picture completely.

Theorem 2.17. In a 1-2-metric there are GE, that are not in Ω( 𝛼𝑛
𝛼+𝑛)-NE.

Proof. We begin by showing that there are networks in GE that are not in 𝛼𝑛−2𝛼+𝑛−1
2𝛼+𝑛
-approximate NE. For this, we examine the network 𝐺 in Figure 4.

First, we show that network 𝐺 is in GE by proving that no agent can decrease its cost by adding, removing, or swapping a single incident outgoing edge.

Let s be the strategy-profile such that 𝐺 = 𝐺(s). Agent 𝑢 cannot remove its edges to any node
𝑎𝑖 or 𝑤 as that would remove the greedy path to that node. The stretch to node 𝑣 is already 1, so adding or swapping an edge would not be beneficial either. No agent 𝑎𝑖 can remove its edge to nodes 𝑢 or 𝑣 as that would remove the greedy paths to them. The stretch to all other nodes 𝑎𝑖 and 𝑤
is already 1, so adding or swapping an edge would not be beneficial either. Agent 𝑣 cannot remove any edge to a node 𝑎𝑖 or 𝑤 because that would remove the greedy paths to them. The stretch to node 𝑢 is already 1 so adding or swapping an edge would not be beneficial either. Finally, agent 𝑤 cannot remove any edge to nodes 𝑢 or 𝑣 because otherwise there would be no greedy path to that node. The stretches to all nodes 𝑎𝑖 are already 1, so adding an edge or swapping one would not be beneficial either. Thus, the network 𝐺 is in GE. Let 𝑆𝑢 = {𝑎1, · · · ,𝑎𝑥,𝑤}, i.e., agent 𝑢's strategy in
𝐺(s) = 𝐺(𝑆𝑢, s−𝑢). The cost of agent 𝑢 is then given by
𝑐𝑢(𝑆𝑢, s−𝑢) = stretchcost𝑢(𝑆𝑢, s−𝑢) + edgecost𝑢(𝑆𝑢, s−𝑢) = 𝛼(𝑥 + 1) + 𝑛 − 1 = 𝑛(𝛼 + 1) − 2𝛼 − 1, since we have that 𝑥 = 𝑛 − 3.

Now, if in contrast agent 𝑢 would remove its edges to all nodes 𝑎𝑖 and instead build one edge to node 𝑣, i.e., the strategy 𝑆′
𝑢 = {𝑣,𝑤}, this yields a cost of
2.

𝑐𝑢(𝑆′
    𝑢, s−𝑢) = stretchcost𝑢(𝑆′
                             𝑢, s−𝑢) + edgecost𝑢(𝑆′
                                                  𝑢, s−𝑢) = 2𝛼 + 3

2𝑥 + 2 = 2𝛼 + 3

2𝑛 − 5

Thus, the network is not in 𝑐𝑢 (𝑆𝑢,s−𝑢 )

𝛼+𝑛)-approximate NE.
                                   □

𝑐𝑢 (𝑆′𝑢,s−𝑢 ) = 𝑛(𝛼+1)−2𝛼−1

2𝛼+3/2𝑛−5/2 ∈ Ω( 𝛼𝑛

Approximate Equilibria. For𝛼 > 1

                                          2, we know that NE exist, but even deciding if a given network is
in NE is NP-hard. Thus, aiming for approximate equilibria seems an appropriate solution. However,
we have seen that simply using GE for this is also an option. However, since approximation
algorithms exist for the Dominating Set problem, there is a different approach.

Theorem 2.18. In 1-2-metrics, a O(log𝑛)-approximate NE always exists.

2
 � |𝑊2(𝑢)| + 1

  Proof. By Theorem 2.11 we have that for 𝛼 > 0 all 𝐵𝐷𝑆𝐺(𝛼) are the only NE. That means that
for every node 𝑢 the quantity 𝑏 = �𝛼 − 1

                                                              2 |𝑊 +
                                                                   2 (𝑢)| should be minimum. Using the fact
that |𝑊2(𝑢)| = |𝑊 +
                    2 (𝑢)| + |𝑊 −
                                 2 (𝑢)|, we get that 𝑏 = �𝛼 − 1

                                                                   2
                                                                    � |𝑊 −
                                                                         2 (𝑢)| + 𝛼|𝑊 +
                                                                                        2 (𝑢)|.
  Then, we construct a network that is in O(log𝑛)-approximate NE as follows. To ensure that
greedy routing is enabled, we first construct a MaxDSG network 𝐺. Now, we consider every agent 𝑢
sequentially. We know that agent 𝑢's strategy must be a dominating set in the network 𝐺1
                                                                                                          −𝑢. Since
the Dominating Set problem is a special case of the Set Cover problem, we can use the standard
greedy approximation algorithm for Weighted Set Cover [17] to compute a dominating set that
is at most a factor of O(log𝑛) larger than the minimum size dominating set, where every node
𝑣 ∈ 𝑊 +
      2 (𝑢) has weight 𝛼, and every node 𝑥 ∈ 𝑊 −
                                                        2 (𝑢) has weight (𝛼 − 1

                                                                                  2). We now replace agent 𝑢's
strategy in 𝐺 by the computed approximate dominating set.
  With this, we ensure that greedy routing is still enabled, and we have that no agent can decrease
its edgecost by more than a factor of O(log𝑛) by any strategy change. Moreover, observe that,
since greedy routing is enabled, we have, by Lemma 2.1, that all pairwise stretches are at either 1 or
3
2. Thus, in any strategy that ensures that greedy routing works for some agent 𝑢, the stretchcosts
of 𝑢 can be at most a factor of 3

                                     2 ∈ O(log𝑛) higher that its best possible stretchcost. Thus, in the
constructed network, any agent𝑢 can improve its cost at most by a factor of O(log𝑛) by performing
a strategy change.
                                                                                                                  □

3
   TREE METRICS
Now we examine networks that are created with an underlying tree metric. Remember that in
a tree metric, a positively weighted undirected spanning tree 𝑇 is given, such that for all nodes
𝑢, 𝑣 ∈ P, we have 𝑑(𝑢, 𝑣) = 𝑑𝑇 (𝑢, 𝑣). In the following, we always use 𝑇 to denote this tree.
  Let s𝑇 denote the strategy-profile, where every edge of 𝑇 is created in both directions and let
𝐺𝑇 = 𝐺(s𝑇 ) be the corresponding created network, i.e., 𝐺𝑇 is identical to 𝑇, but every edge is
replaced by directed edges in both directions of the same weight as the respective edge in 𝑇. For
our analysis, we will consider the network 𝐺𝑇 = (P, 𝐸𝑇, ℓ) rooted at a node 𝑟 ∈ P, denoted as 𝐺𝑇
                                                                           𝑟 .
This is defined analogous to rooting the tree 𝑇 at node 𝑟. We say that node 𝑣 is the child of node 𝑢
in 𝐺𝑇
   𝑟 , if (𝑢, 𝑣) ∈ 𝐸𝑇 and if 𝑑(𝑢,𝑟) < 𝑑(𝑣,𝑟), i.e., if 𝑢 is closer to 𝑟 than 𝑣. Moreover, in 𝐺𝑇
                                                                    𝑟 node 𝑤 is
a descendant of node 𝑢, if a path 𝑢 = 𝑥1,𝑥2, . . . ,𝑥𝑘 = 𝑤 exists, such that 𝑥𝑖+1 is the child of 𝑥1, for
1 ≤ 𝑖 ≤ 𝑘 − 1. We assume that 𝑢 is also a descendant of itself.

Since for all our purposes the network 𝐺𝑇
𝑟 behaves exactly like the tree 𝑇 rooted at 𝑟, we will from now on use the terminology from trees, when working with 𝐺𝑇 or 𝐺𝑇
𝑟 . For example, for 𝐺𝑇
𝑟
we let *𝑠𝑢𝑏𝑡𝑟𝑒𝑒*(𝑢) denote the subtree of 𝐺𝑇
𝑟 rooted at node 𝑢 that includes all descendants of 𝑢
(including 𝑢). Furthermore, let *𝑏𝑒𝑙𝑜𝑤*(𝑢) refer to the set of subtrees {*𝑠𝑢𝑏𝑡𝑟𝑒𝑒*(𝑣) | 𝑣 is a child of 𝑢}.

We start with two general statements about greedy paths and strategies in tree metrics.

Lemma 3.1. In a tree metric, a greedy path from node 𝑢 to a node 𝑣 can only consist of nodes that are in the same subtree from 𝑏𝑒𝑙𝑜𝑤(𝑢) in 𝑇 rooted at 𝑢 that contains node 𝑣.

Proof. Let 𝑢 ∈ P and let 𝑣 ∈ P \ {𝑢}. Now, consider the set of subtrees *𝑏𝑒𝑙𝑜𝑤*(𝑢) of 𝑇 rooted at
𝑢. Note that the subtrees in *𝑏𝑒𝑙𝑜𝑤*(𝑢) include all agents except 𝑢. Hence, there exists a subtree 𝑇 ′ ∈
𝑏𝑒𝑙𝑜𝑤(𝑢), such that 𝑣 ∈ 𝑇 ′. To show our statement it thus suffices to show that, indeed, a path from 𝑢 to 𝑣 can only be a greedy path, if the path consists exclusively of nodes in 𝑇 ′. Towards a contradiction, consider any agent 𝑥 ∉ 𝑇 ′ and assume that 𝑥 is part of a greedy path from 𝑢 to 𝑣.

Observe that agent 𝑥 has a path to 𝑣 only via 𝑢, since 𝑇 is rooted at 𝑢 and 𝑥 and 𝑣 are nodes of two different subtrees of 𝑢. It follows that 𝑑𝑇 (𝑥, 𝑣) > 𝑑𝑇 (*𝑢, 𝑣*), which contradicts that the considered path is greedy path from 𝑢 to 𝑣 via 𝑥.

□
Lemma 3.2. In any strategy profile s that enables greedy routing with a tree metric, for any node 𝑢, in 𝐺(s) agent 𝑢 needs to have an edge to some node in every subtree in 𝑏𝑒𝑙𝑜𝑤(𝑢) of 𝑇 rooted at 𝑢.

Proof. Fix any agent 𝑢 ∈ P and consider the network 𝐺(s). For the sake of contradiction, let
𝑇 ′ ∈ *𝑏𝑒𝑙𝑜𝑤*(𝑢) be a subtree of 𝑇, such that agent 𝑢 does not build an edge to any node 𝑣 ∈ 𝑇 ′ in
𝐺(s). Then, fixing any 𝑤 ∈ 𝑇 ′ and, by Lemma 3.1, all greedy paths from 𝑢 to 𝑤 can only traverse nodes in 𝑇 ′. Thus, by recalling that agent 𝑢 has no edge to any vertex 𝑣 ∈ 𝑇 ′, agent 𝑢 cannot have a greedy path to 𝑤.

□
Equilibrium Existence. Here, we show the existence of equilibria and partially characterize them.

Theorem 3.3. In a tree metric, the network 𝐺𝑇 is always a NE and a social optimum.

Proof. Consider an agent 𝑢 ∈ P. First, observe that in 𝐺𝑇 all of agent 𝑢's distances and stretches are already minimal. Hence, adding any edges cannot improve its stretchcosts. Moreover, by Lemma 3.2, agent 𝑢 also cannot remove any edges. For the same reason, swapping an edge (*𝑢, 𝑣*)
with another edge (𝑢,𝑤) is only possible for 𝑇 ′ ∈ *𝑏𝑒𝑙𝑜𝑤*(𝑢), such that *𝑢, 𝑣* ∈ 𝑉 (𝑇 ′), i.e., if the two nodes belong to the same subtree. However, since swapping edges does not change agent
𝑢's edgecosts, such a swap cannot be an improving move since agent 𝑢's stretchcosts cannot be further improved. Hence, there are no improving moves for any agent and 𝐺𝑇 is a NE. Because all distances and stretches are minimal and there is no cheaper set of edges to enable greedy routing, the network 𝐺𝑇 must also be social optimum.

□
In the following, we show that GE are unique. This completely characterizes all GE and NE.

Theorem 3.4. In a tree metric, the network 𝐺𝑇 is the only GE.

Proof. We prove the statement in two steps while assuming, for the sake of contradiction, that there is a GE network 𝐺 that differs from 𝐺𝑇 . First, we show that in this case, network 𝐺𝑇 cannot be a proper subgraph of 𝐺, i.e., network 𝐺 contains all the edges of 𝐺𝑇 and at least one other edge.

Then, in a second step, we show that if 𝐺𝑇 is not a subgraph of 𝐺, i.e., if 𝐺 does not contain all the edges of 𝐺𝑇 , then 𝐺 is not in GE. This yields that any GE network must be identical to 𝐺𝑇 .

To show that 𝐺𝑇 = (P, 𝐸𝑇, ℓ) cannot be a proper subgraph of 𝐺 = (P*, 𝐸, ℓ*), we observe that if this was the case, then 𝐸𝑇 ⊂ 𝐸 holds, i.e., 𝐸 \ 𝐸𝑇 ≠ ∅. Thus, there exists at least one edge
𝑒 ∈ 𝐸 \ 𝐸𝑇 . However, by definition of 𝐺𝑇 , the total strechcosts and the distances are minimized in the network 𝐺𝑇 . Hence, removing the edge 𝑒 ∈ 𝐸 \𝐸𝑇 would be an improving move. A contradiction.

Let us now consider the case that 𝐺𝑇 is not a subgraph of 𝐺, while 𝐺 is a GE. We define
𝑓𝑎(𝑏) to be the number of descendants of node 𝑏 in 𝐺𝑇
𝑎 . We consider a specific edge, for this, let (*𝑢, 𝑣*) = arg min(𝑎,𝑏)∈𝐸𝑇 \𝐸 𝑓𝑎(𝑏), i.e., the tuple (*𝑢, 𝑣*) that is an edge in 𝐺𝑇 but not in 𝐺, that minimizes the number of descendants of node 𝑣 in 𝐺𝑇
𝑢 . Notice that such an edge always exists, since we assume that 𝐺𝑇 is not a subgraph of 𝐺 and thus, 𝐸𝑇 \ 𝐸 ≠ ∅.

We now examine the greedy path from node 𝑢 to node 𝑣 in network 𝐺. Since (*𝑢, 𝑣*) ∉ 𝐸, in conjunction with the assumption that 𝐺 is a GE, there must exist another node 𝑥 ≠ 𝑣, such that
(𝑢,𝑥) ∈ 𝐸, that enables a greedy path from 𝑢 to 𝑣 in 𝐺, i.e., the edge (𝑢,𝑥) is the first edge on this greedy path. By Lemma 3.1, node 𝑥 must belong to the same subtree𝑇 ′ as 𝑣 in *𝑏𝑒𝑙𝑜𝑤*(𝑢) in𝑇 rooted at 𝑢. Since 𝑣 is a child of 𝑢 in𝑇 rooted at 𝑢, we have that𝑇 ′ = *𝑠𝑢𝑏𝑡𝑟𝑒𝑒*(𝑣). It follows that (𝑢,𝑥) ∉ 𝐸𝑇 , since in 𝐺𝑇
𝑟 node 𝑢 only has 𝑣 as child in 𝑇 ′.

Next, recall that we assume that 𝐺 = 𝐺(s) = 𝐺(𝑆𝑢, s−𝑢) is a GE. It follows that for agent 𝑢 it is not an improving move to swap the edge (𝑢,𝑥) ∈ 𝐸 for the edge (*𝑢, 𝑣*) ∉ 𝐸. Now, let 𝑆′
𝑢 = 𝑆𝑢 \ {𝑥}
and let s𝑣 = (𝑆′
𝑢 ∪ {𝑣}, s−𝑢). For convenience, let s𝑥 = s = (𝑆′
𝑢 ∪ {𝑥}, s−𝑢).

We first show, that after the swap, i.e., in 𝐺(s𝑣), agent 𝑢 still has a greedy path to all nodes. Since in 𝐺(s𝑣) nothing changes for greedy paths that do not use 𝑥 as first hop, it suffices to focus on such paths. Thus, consider a greedy path 𝑃 from 𝑢 to 𝑧 ∈ P in 𝐺(s𝑥) that uses 𝑥 as first hop. Since 𝐺 is a GE, agent 𝑣 has a greedy path 𝑄 to 𝑥 in 𝐺. Moreover, since 𝑥 is in *𝑠𝑢𝑏𝑡𝑟𝑒𝑒*(𝑣), it follows that
𝑑𝑇 (𝑣,𝑥) < 𝑑𝑇 (𝑢,𝑥). Thus, in 𝐺(s𝑣) agent 𝑢 has a greedy path to 𝑥 via node 𝑣 and 𝑄. This implies that also in 𝐺(s𝑣) agent 𝑢 has a greedy path to 𝑧, since the path via 𝑣, 𝑄 and 𝑃 is a greedy path.

The swap from (𝑢,𝑥) to (*𝑢, 𝑣*) decreases agent 𝑢's stretch to 𝑣 but it does not change 𝑢's edgecost.

Since the swap does not reduce agent 𝑢's cost, there must be a node 𝑤 ∈ P to which agent 𝑢's stretch increases after the swap, i.e., stretch𝐺 (s𝑥 ) (𝑢,𝑤) < stretch𝐺 (s𝑣 ) (𝑢,𝑤). It follows, that in
𝐺 = 𝐺(s𝑥), agent 𝑢 has a greedy path via 𝑥 to 𝑤.

By Lemma 3.1, it follows that both nodes 𝑥 and 𝑤 must belong to the same subtree𝑇 ′ in *𝑏𝑒𝑙𝑜𝑤*(𝑢)
in 𝑇 rooted at 𝑢, which must be 𝑇 ′ = *𝑠𝑢𝑏𝑡𝑟𝑒𝑒*(𝑣).

Now, if stretch𝐺 (𝑣,𝑤) = 1, then agent 𝑢's stretch to 𝑤 must be optimal in 𝐺(s𝑣) and hence, the stretch cannot have increased compared to 𝐺(s𝑥). Hence, we can assume that stretch𝐺 (𝑣,𝑤) > 1. In this case, there there must be a vertex 𝑝 along the path from 𝑣 to 𝑤 in𝑇 that in 𝐺 does not create the edge to the next node 𝑞 on that path. Thus, the edge (𝑝,𝑞) is in 𝐸𝑇 \𝐸. Now, note that 𝑓𝑝 (𝑞) < 𝑓𝑢(𝑣), since 𝑞's subtree in 𝐺𝑇
𝑝 is completely contained in 𝑣's subtree in 𝐺𝑇
𝑢 . This is a contradiction to the choice of edge (*𝑢, 𝑣*), i.e., to (*𝑢, 𝑣*) having the minimum 𝑓 -value.

Thus, every edge of 𝐺𝑇 must be contained in 𝐺 and thus, 𝐺𝑇 is the only GE.

□
Dynamic Properties. We investigate if NE networks in tree metrics can be found by iteratively selecting best responses. The answer is affirmative.

Theorem 3.5. In a tree metric our game is weakly acyclic under best responses.

Proof. Fix any 𝑢 ∈ P and root 𝑇 in 𝑢. Consider any subtree 𝑇 ′ ∈ *𝑏𝑒𝑙𝑜𝑤*(𝑢). Recall that, by Lemma 3.2, agent 𝑢 needs to build an edge (*𝑢, 𝑣*), where 𝑣 ∈ 𝑇 ′, in order to enable greedy routing from 𝑢 to the set of nodes in 𝑇 ′. Note that in case that in a strategy-profile s all edges of 𝑇 ′ are created in both directions, then the best response of agent 𝑢 in s is to create the edge (𝑢,𝑢′), where
𝑢′ is the root of subtree 𝑇 ′, since 𝑢′ = arg min𝑣∈𝑉 (𝑇 ′) 𝑑𝑇 (*𝑢, 𝑣*).

We can now use this observation to get from any strategy-profile s to the strategy-profile s𝑇
by a finite sequence of best responses. For this, we root 𝑇 in 𝑢 and activate the agents of 𝑇 in a bottom-up fashion, i.e., starting with the leaves and then moving upwards. This ensures that all edges of 𝐺𝑇 are eventually created.

After all edges of 𝐺𝑇 are created, we activate all agents that still have edges that do not belong to 𝐺𝑇 in any order. Any such edge will be removed since the edges of 𝐺𝑇 already suffice to achieve optimal stretchcosts. Thus, since 𝐺𝑇 is a NE, our game is weakly acyclic under best responses.

□
Computational Complexity. Here, we investigate the computational complexity of computing a best response in tree metrics. We show, that this is a hard problem.

Theorem 3.6. In tree metrics, computing a best response is NP-hard.

Proof. The main argument of the proof is that computing a best response boils down to solving Set Cover [34]. To this end, we reduce from Set Cover and show that if the number of edges build in a best response strategy of an agent in our constructed instance could be computed in polynomial time, then the size of a minimum set cover could also be computed in polynomial time.

Let 𝑃 = ({𝑥1, ...𝑥𝑛}, {𝑄1*, ...,𝑄*𝑚}) be an instance of Set Cover, where {𝑥1*, ...𝑥*𝑛} is the set of elements that need to be covered and {𝑄1*, ...,𝑄*𝑚} is a collection of subsets of the elements that can be selected. Given a Set Cover-instance, we construct a corresponding bipartite graph 𝐺(*𝑉, 𝐸*)
with a node for every set 𝑄𝑖 and for every element 𝑥𝑖, and edges between every set and its contained elements. We add nodes *𝑢, 𝑣* and 𝑐 and connect node 𝑣 to node 𝑐 as well as every node 𝑄𝑖. The tree metric then is defined as in Figure 5a and we fix 𝛼 > 4.

Let 𝐶 be a minimum set cover of 𝑃. We show that the number of edges that agent 𝑢 builds in a best response in the corresponding game instance is 1 + |𝐶|. First, observe that node 𝑣 only inherits outgoing edges. Thus, agent 𝑢 has to create an edge to node 𝑣 to enable a greedy path to 𝑣. In contrast, consider the potential edge (𝑢,𝑐). Note that 𝑑 (𝑢,𝑣)+𝑑 (𝑣,𝑐)
2 by our metric in Figure 5 a.

𝑑 (𝑢,𝑐)
= 2 < 4 < 𝛼. This, in conjunction with the observation that a potential edge (𝑢,𝑐) would not affect the stretch to any other node, leads to the conclusion that the creation of an edge from 𝑢 to 𝑐 is not an improving move.

Let 𝐵 be the best response of agent 𝑢. Given 𝐵, where we do not necessarily know which nodes it contains, except for 𝑣 ∈ 𝐵 and 𝑐 ∉ 𝐵, we construct another strategy 𝐵′ = 𝜓 (𝐵). The mapping
𝜓 : 𝑋 → 𝑌, for *𝑋,𝑌* ⊆ 𝑉 , is defined as follows: For 𝑄 𝑗 ∈ 𝐵 or 𝑣 ∈ 𝐵 we simply map 𝜓 (𝑄 𝑗) = 𝑄 𝑗
and 𝜓 (𝑣) = 𝑣 respectively. In contrast, for any 𝑥𝑖 ∈ 𝐵 we have 𝜓 (𝑥𝑖) = 𝑄 𝑗, where (𝑄 𝑗,𝑥𝑖) ∈ 𝐸(𝐺).

Note that for any 𝑥𝑖 such a node 𝑄 𝑗 exists by the construction of 𝐺. Moreover, we observe that whenever 𝑥𝑖 ∈ 𝐵, then this implies that 𝑄 𝑗 ∉ 𝐵. To see this, consider any such pair (𝑄 𝑗,𝑥𝑖) and assume that 𝑄 𝑗,𝑥𝑖 ∈ 𝐵, i.e., in agent 𝑢's best response it builds an edge to both 𝑥𝑖 and 𝑄 𝑗.

We show that dropping the edge (𝑢,𝑥𝑖) would be a better response, hence, a contradiction to 𝐵
being the best response of agent 𝑢. To that end, consider the stretchcosts without (𝑢,𝑥𝑖). As 𝑢 has a greedy path to 𝑥𝑖 via 𝑄 𝑗, we get stretch𝐺 (𝑢,𝑥𝑖) = 𝑑 (𝑢,𝑄 𝑗 )+𝑑 (𝑄 𝑗,𝑥𝑖 )
𝑑 (𝑢,𝑥𝑖 )
= 3
In contrast, including the edge (𝑢,𝑥𝑖) entails an additional cost of 𝛼 with optimal stretch stretch𝐺 (𝑢,𝑥𝑖) = 1. Since 𝛼 > 4, this yields a larger cost for 𝑢 compared to dropping the edge. The contradiction is completed by noticing that the edge (𝑢,𝑥𝑖) does not enable any other greedy path for 𝑢. We conclude that our defined mapping 𝜓 : 𝑋 → 𝑌 is valid for our set 𝐵 and that |𝐵| = |𝐵′|
for 𝐵′ = 𝜓 (𝐵).

Next, we observe that 𝐵′ \ {𝑣} constitutes a set cover 𝑃. To see that, recall that greedy routing is enabled for agent 𝑢 via strategy 𝐵. Thus, strategy 𝐵′ also enables greedy routing for agent 𝑢 which entails that for all 𝑥𝑖 there exists an 𝑄 𝑗 such that (𝑢,𝑄 𝑗) and (𝑄 𝑗,𝑥𝑖).

Moreover, the set 𝐵′ \ {𝑣} must constitute a minimum set cover: Suppose that it were otherwise and a set cover 𝐶 with |𝐶| < |𝐵′| − 1 exists. We show that 𝐷 = 𝐶 ∪ {𝑣} is a better response than 𝐵, which yields a contradiction, since 𝐵 is the best response for agent 𝑢. In both strategies, agent 𝑢's distances to 𝑐 and 𝑣 are 𝑑(𝑢,𝑐) = 4 and 𝑑(*𝑢, 𝑣*) = 3 respectively, the distances to all 𝑄 𝑗 are either
𝑑(𝑢,𝑄 𝑗) = 3 or 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑄 𝑗) = 5 depending on whether there exists an edge (𝑢,𝑄 𝑗). Thus, the difference in stretch of a network including (𝑢,𝑄 𝑗), in contrast to the same network but without edge (𝑢,𝑄 𝑗), is Δ = 𝑑 (𝑢,𝑣)+𝑑 (𝑣,𝑄 𝑗 )
𝑑 (𝑢,𝑄 𝑗 )
− 𝑑 (𝑢,𝑄 𝑗 )
𝑑 (𝑢,𝑄 𝑗 ) = 2
3. In a similar fashion, recalling that if (𝑢,𝑥𝑖) is not included then agent 𝑢 creates the edge (𝑢,𝑄 𝑗), we have that the distance to 𝑥𝑖 is either 𝑑(𝑢,𝑥𝑖) = 4 or 𝑑(𝑢,𝑄 𝑗) + 𝑑(𝑄 𝑗,𝑥𝑖) = 6 depending on whether there is an edge (𝑢,𝑥𝑖). Moreover, the difference in stretch is then given by 𝛿 = 𝑑 (𝑢,𝑄 𝑗 )+𝑑 (𝑄 𝑗,𝑥𝑖 )
𝑑 (𝑢,𝑥𝑖 )
− 𝑑 (𝑥𝑖 )
𝑑 (𝑥𝑖 ) = 1
2. Then, setting 𝑋 = {𝑥1, · · · ,𝑥𝑛} and
𝑄 = {𝑄1, · · · ,𝑄𝑚}, the stretchcosts of 𝐵 are at least

𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑄 𝑗) 𝑑(𝑢,𝑄𝑖,𝑗) + 𝑑(𝑄𝑖,𝑗,𝑥𝑖) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑐) 𝑑(𝑢,𝑐) + 𝑑(*𝑢, 𝑣*) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑢,𝑄 𝑗) + 𝑑(𝑢,𝑥𝑖) + |𝐵| − 1 𝑚 ∑︁ 𝑛 ∑︁ 𝑄 𝑗 ∈𝑄\𝐵 𝑥𝑖 ∈𝑋\𝐵 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑄 𝑗) 𝑑(𝑢,𝑄𝑖,𝑗) + 𝑑(𝑄𝑖,𝑗,𝑥𝑖) ≥ 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑐) 𝑗=1 𝑖=1 𝑑(𝑢,𝑐) + 𝑑(*𝑢, 𝑣*) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑢,𝑄 𝑗) + 𝑑(𝑢,𝑥𝑖) − *𝑚𝑎𝑥*(𝛿, Δ)(|𝐵| − 1), 𝑚 ∑︁ 𝑛 ∑︁
where 𝑄𝑖,𝑗 is 𝑄 𝑗 such that (𝑄 𝑗,𝑥𝑖) ∈ 𝐸(𝐺). The last line follows as we overcount the number of edges by a factor of |𝐵| − 1 and we assume the discount factor of the stretches to be maximal
Δ = *𝑚𝑎𝑥*(𝛿, Δ) in order to achieve a lower bound. Plugging in the values now yields

3𝑚 + 6 4𝑛 − 2 stretchcost𝑢(𝐵) ≥ 4 2 + 3 3 + 5 3 (|𝐵| − 1). (4)
Analogously, we derive an upper bound on the stretchcost of agent 𝑢 applying strategy 𝐷, giving

𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑄 𝑗) 𝑑(𝑢,𝑄𝑖,𝑗) + 𝑑(𝑄𝑖,𝑗,𝑥𝑖) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑐) 𝑑(𝑢,𝑐) + 𝑑(*𝑢, 𝑣*) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑢,𝑄 𝑗) + 𝑑(𝑢,𝑥𝑖) + |𝐷| − 1 𝑚 ∑︁ 𝑛 ∑︁ 𝑄 𝑗 ∈𝑄\𝐷 𝑥𝑖 ∈𝑋\𝐷 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑄 𝑗) 𝑑(𝑢,𝑄𝑖,𝑗) + 𝑑(𝑄𝑖,𝑗,𝑥𝑖) ≤ 𝑑(*𝑢, 𝑣*) + 𝑑(𝑣,𝑐) 𝑗=1 𝑖=1 𝑑(𝑢,𝑐) + 𝑑(*𝑢, 𝑣*) 𝑑(*𝑢, 𝑣*) + 𝑑(𝑢,𝑄 𝑗) + 𝑑(𝑢,𝑥𝑖) − *𝑚𝑖𝑛*(𝛿, Δ)(|𝐷| − 1) 𝑚 ∑︁ 𝑛 ∑︁ = 4 3𝑚 + 6 4𝑛 − 1 2 + 3 3 + 5 2 (|𝐷| − 1). (5)
Thus, combining Equation (4) with Equation (5), the increase in stretch cost from strategy 𝐵 in comparison to strategy 𝐷 is at most

$$\operatorname{stretchcost}_{u}(D)-\operatorname{stretchcost}_{u}(B)\leq{\frac{2}{3}}|B|-{\frac{1}{2}}|D|-{\frac{1}{6}}<{\frac{2}{3}}|B|-{\frac{1}{2}}|D|.$$
This now stays in contrast to the reduction in edgecosts given by edgecost𝑢(𝐵) −edgecost𝑢(𝐷) =
(|𝐵| − |𝐷|)𝛼. We now recall that 𝛼 > 4 and by previous discussion it is finally revealed that

$\mathrm{edgecost}_{u}(B)-\mathrm{edgecost}_{u}(D)=(|B|-|D|)\alpha$

$$>(|B|-|D|)4$$ $$>\frac{2}{3}|B|-\frac{1}{2}|D|$$ $$>\mathrm{stretchcost}_{u}(D)-\mathrm{stretchcost}_{u}(B),$$
whereby the penultimate line follows since |𝐷| ≤ |𝐵|−1. Notice that edgecost𝑢(𝐵)−edgecost𝑢(𝐷) >
stretchcost𝑢(𝐷) − stretchcost𝑢(𝐵) entails that 𝑐𝑢(𝐵) > 𝑐𝑢(𝐷). Hence, if a best response of size 𝑘
could be computed in polynomial time, then the size of a set cover of size 𝑘 − 1 could be found in polynomial time, since our reduction is computable in polynomial time as well.

□
4
EUCLIDEAN METRICS
In this section, we study Euclidean metrics, which are metrics where there is a function that maps agents to points in a 𝑑-dimensional Euclidean space, such that the distances in the metric between agents correspond to the distances of their points in the Euclidean space. We use the 2-norm to measure distances in the Euclidean space. We focus on 2D-Euclidean metrics but all results regarding the existence of equilibria and computational complexity directly apply to higher dimensional spaces as well. Given three nodes *𝑢, 𝑣,𝑤* ∈ P in a Euclidean metric, let ∠𝑣𝑢𝑤 be the angle of 𝑢 formed by rays −→
𝑢𝑣 and −→
𝑢𝑤. We always consider the positive angle, which is at most 𝜋.

Equilibrium Existence. First, we show that GE may not exist, modifying the proof of Theorem
5.1 from Moscibroda, Schmid and Wattenhofer [43].

Theorem 4.1. In a 2D Euclidean metric there are instances of our game that do not have a GE.

Proof. Modifying the proof of Theorem 5.1 from Moscibroda, Schmid and Wattenhofer [43] for
𝑘 = 1, where 𝜖 > 0 is an arbitrarily small constant, we show that there are no GE in the network in Figure 6 for 𝛼 = 0.6. Differing from the construction in [43], we changed 𝑑(𝑏,𝑦) to enable greedy routing. To that end, we first establish general statements about the strategies of agents in NE to show that only the strategies for agents 𝑦 and 𝑧 shown in Figure 7 could possibly be part of a NE.

Then, we show that none of these strategies is in NE.

First, we note that the edges (𝑏,𝑎), (𝑏,𝑐), (𝑐,𝑏), (𝑦,𝑧) and (𝑧,𝑦) have to be built to enable greedy routing, because there is no other node closer to the head of each edge than the tail of that edge. Furthermore, agent 𝑎 also builds an edge to 𝑏 because the only other possible greedy path via 𝑐
would have a stretch of 𝑑 (𝑎,𝑐)+𝑑 (𝑐,𝑏)
𝑑 (𝑎,𝑏)
= 𝑑 (𝑎,𝑐)+1
1.14
> 1+𝛼 and thus adding the edge to 𝑏 is an improving move for 𝑎. Additionally, agent 𝑎 does not build an edge to 𝑐 because that would improve the stretch to 𝑐 by 𝑑 (𝑎,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑎,𝑐)
− 1 =
2.14
𝑑 (𝑎,𝑐) − 1 < 𝛼 without changing the stretch to any other agent.

Analogously, agent 𝑐 does not build an edge to 𝑎 because that would decrease stretches by at most
𝑑 (𝑐,𝑏)+𝑑 (𝑏,𝑎)
𝑑 (𝑐,𝑎)
− 1 + 𝑑 (𝑐,𝑏)+𝑑 (𝑏,𝑎)+𝑑 (𝑎,𝑦)−(𝑑 (𝑐,𝑎)+𝑑 (𝑎,𝑦))
𝑑 (𝑐,𝑦)
=
2.14
𝑑 (𝑎,𝑐) − 1 + 4.1−(𝑑 (𝑎,𝑐)+1.96)
𝑑 (𝑐,𝑦)
< 𝛼.

Moreover, agent 𝑦 also builds an edge to 𝑎 because the only other possible greedy path via
𝑏 has a stretch of 𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑎)
𝑑 (𝑦,𝑎)
= 3.14−𝜖
1.96
> 1 + 𝛼. Analogously, agent 𝑦 does not build edges to both 𝑏 and 𝑐 because if it would, it could simply remove the edge to 𝑐 and increase stretches by
𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑦,𝑐)
=
3−𝜖
𝑑 (𝑐,𝑦) − 1 < 𝛼. In fact, agent 𝑦 does not build an edge to 𝑐 because if they would, they could swap their edge from 𝑐 to 𝑏, changing the sum of stretches by at most 𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑦,𝑐)
−
𝑑 (𝑦,𝑐)+𝑑 (𝑐,𝑏)
𝑑 (𝑦,𝑏)
=
3−𝜖
𝑑 (𝑐,𝑦) − 𝑑 (𝑐,𝑦)+1
2−𝜖
< 0.

Additionally, agent 𝑧 has to build an edge to 𝑏 or 𝑐 because otherwise, there is no greedy path to 𝑐. Agent 𝑧 does not build both edges because if it did, it could remove its edge to 𝑐, increasing stretches by 𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑧,𝑐)
− 1 =
3
2+𝜖 − 1 < 𝛼. Finally, agent 𝑧 does also not build an edge to 𝑎 because the stretch to 𝑎 via 𝑦 is already 𝑑 (𝑧,𝑦)+𝑑 (𝑦,𝑎)
𝑑 (𝑧,𝑎)
= 2.96−2𝜖
𝑑 (𝑧,𝑎) < 1 + 𝛼 and the edge to 𝑎 would not provide shorter greedy paths to 𝑏 or 𝑐 because 𝑧 needs an edge to 𝑏 or 𝑐 in any case.

This leaves the potential strategies for nodes 𝑦 and 𝑧 shown in Figure 7. The strategies of 𝑎,𝑏
and 𝑐 beyond the edges already discussed do not matter for the strategies for 𝑦 and 𝑧 because any additional edges could not be part of a greedy path starting from them. We examine all of these possible cases and show that they cannot be part of a GE.

Case 1: In Figure 7a, if 𝑦 adds an edge to 𝑏, the stretch to 𝑏 decreases from 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏)
𝑑 (𝑦,𝑏)
= 3.1
2−𝜖
to 1 and the stretch to 𝑐 from 𝑑 (𝑦,𝑧)+𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)

𝑑 (𝑦,𝑐)
            =
               4−2𝜖
               𝑑 (𝑦,𝑐) to 𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)

𝑑 (𝑦,𝑐)
         =
             3−𝜖

                                                                              𝑑 (𝑦,𝑐) which is a total
improvement of more than 𝛼.
  Case 2: In Figure 7b, agent 𝑧 can swap its edge from 𝑏 to 𝑐, changing the sum of stretches by
𝑑 (𝑧,𝑦)+𝑑 (𝑦,𝑏)

2
   −
       3

𝑑 (𝑧,𝑏)
         − 𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)

𝑑 (𝑧,𝑐)
         = 3−3𝜖

                                          2+𝜖 < 0.
  Case 3: In Figure 7c, if agent 𝑦 removes its edge to 𝑏, the stretch to 𝑐 stays unchanged at
𝑑 (𝑦,𝑧)+𝑑 (𝑧,𝑐)

𝑑 (𝑦,𝑐)
         = 𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)

𝑑 (𝑦,𝑐)
        , while the stretch to 𝑏 increases from 1 to 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏)

                                                                           𝑑 (𝑦,𝑏)
                                                                                     =
                                                                                        3.1
                                                                                       2−𝜖 which is
an increase of less than 𝛼.
  Case 4: In Figure 7d, agent 𝑧 can swap their edge from 𝑐 to 𝑏, changing the sum of stretches by
𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)

𝑑 (𝑧,𝑐)
         − 𝑑 (𝑧,𝑐)+𝑑 (𝑐,𝑏)

𝑑 (𝑧,𝑏)
         =
            3

2+𝜖 − 3+𝜖

                                       2
                                          < 0.
Thus, there can be no GE in this instance.
                                                                                                               □

Computational Complexity. Next, we show that finding a best response is computationally hard.

Theorem 4.2. In a 2D Euclidean metric, computing a best response is NP-hard.

Proof. We reduce from Set Cover and show that, if the number of edges of an agent's best response could be computed in polynomial time, then the size of a minimum set cover could also be found in polynomial time, which would imply P = NP.

Given an instance of $\operatorname{S\pi}$r $\operatorname{Cover}P=(\{x_{1},...x_{n}\},(Q_{1},...,Q_{m}))$, we construct a bipartite graph analogously to the proof of Theorem 3.6. Then, by using the construction as given in Figure 8 and setting $\sigma>4$, the reduction from $\operatorname{S\pi}$r $\operatorname{Cover}$ follows by an almost verbatim repeating of the proof of Theorem 3.6.

We use the article as given in Figure 8 a. Moreover, for the minimal and maximal stretch gain we have $\delta=\frac{d(x_{i}Q_{i})\circ d(Q_{i}x_{i})}{d(x_{i}x_{i})}-\frac{d(x_{i})}{d(x_{i})}=\frac{4}{12}$ and $\Delta=\frac{d(u_{i}\circ u)\circ d(u_{i}Q_{i})}{d(u_{i}Q_{i})}-\frac{d(u_{i}Q_{i})}{d(u_{i}Q_{i})}=\frac{4}{5}$ respectively.

17 and Δ = 𝑑 (𝑢,𝑣)+𝑑 (𝑣,𝑄 𝑗 )
𝑑 (𝑢,𝑥𝑖 )
− 𝑑 (𝑥𝑖 )
𝑑 (𝑥𝑖 ) = 4

have $\delta=\frac{d(u_{Q})_{J}*d(Q_{j},\omega_{I})}{d(u_{\text{LC}})}-\frac{d(u_{I})}{d(\omega_{I})}=\frac{4}{1}$ and $\Delta=\frac{d(u_{P})*d(u_{Q})_{I}}{d(u_{Q})_{I}}-\frac{d(u_{Q})_{I}}{d(u_{Q})_{I}}=\frac{4}{9}$ respectively.

This in conjunction with similar calculations as carried out in Equation (4) and Equation (5) gives for the best response $B$ and the potential min set over $D$

$$\text{stretch}_{\text{out}}(D)-\text{stretch}_{\text{out}}(B)<\frac{4}{9}|B|-\frac{4}{17}|D|$$ $$<|(B-|D|)\alpha=\text{edges}_{u}(B)-\text{edges}_{u}(D),$$

where we made use of $|D|\leq|B|-1$ in conjunction with $\alpha>4$. We conclude that strategy $D$ is an improvement in total. Hence, if a best response could be found in polynomial time, then a minimum size set over could be found in polynomial time, because our reduction is computable in polynomial time as well.

Approximate Equilibria. Since GE do not always exist and finding a best response is computationally hard, approximate equilibria are only remaining option to construct almost stable networks in polynomial time. To that end, we employ Θ𝑘-graphs for 2D-Euclidean metrics.

First introduced independently by Clarkson [18] and Keil [36], Θ𝑘-graphs are constructed as follows: Each node 𝑢 partitions the plane into 𝑘 disjoint cones with itself as the apex, each having an aperture of 2𝜋
𝑘 . Then, for each cone, node 𝑢 adds an edge to the node 𝑣 whose projection onto the bisector of the cone is closest to 𝑢.

Θ-routing is a way of selecting paths in a Θ𝑘-graph. With this, to get from a node 𝑢 to a node 𝑣, the edge is used that 𝑢 created into the cone that contains node 𝑣. This procedure is repeated for each node until node 𝑣 is reached. First, we show that if 𝑘 is too small, Θ𝑘-graphs are not suited as approximate NEs. This result is well-known [44], but we prove it for the sake of completeness.

Theorem 4.3. For every 𝑘 ≤ 5, there exist 2D-Euclidean metrics where the Θ𝑘 graph with directed edges does not enable greedy routing.

Proof. We construct a 2D-Euclidean metric by placing nodes in a polar coordinate system. For now, we assume that the reference direction of the coordinate system is equal to the bisector of some cone used in the construction of the Θ𝑘-graph. The resulting metric is illustrated in Figure 9.

Let 𝑢 be located in the origin. Moreover, let 𝑣 be at distance 1 and angle − 7𝜋
36 , and 𝑤 at distance
1 + 𝜖 and angle 7𝜋
36 < 𝜋
36 . We call this construction 𝐶. Since both 𝑣 and 𝑤 are in the same cone for 𝑢 if
𝑘 ≤ 5 (because 7𝜋
5 ) and 𝑣's projection on the bisector of that cone is closer to 𝑢 than that of 𝑤, agent 𝑢 does not build an edge to 𝑤. But since 𝑑(𝑣,𝑤) > 𝑑(𝑢,𝑤), agent 𝑢 cannot use 𝑣 on a greedy path to 𝑤 and thus cannot have a greedy path to node 𝑤.

In a slightly modified construction, even a global rotation of the cones (i.e. the reference direction of the coordinate system not lining up with the bisector of any cone) cannot achieve better results: First, we note that with cone-rotations of less than 𝜋
𝑘 − 7𝜋
36 in either direction, the same cones stay occupied by nodes and thus the same argumentation still holds. Additionally, for any 𝛽 ∈ R, a rotation by 𝛽 is equal to a rotation by 𝛽 mod 2𝜋
𝑘 . Thus, we place 𝑚 = 2𝜋
𝑘 /( 𝜋
𝑘 − 7𝜋
36 ) copies of 𝐶, which we call 𝐶1*, ...𝐶*𝑚. Each 𝐶𝑖+1 is rotated by 𝜋
𝑘 − 7𝜋
36 , compared to 𝐶𝑖, and the distance between the centers of any 𝐶𝑖 and 𝐶𝑖′ is at least 𝑏 = 4. With this, in any rotation there is a 𝑢𝑖 in some 𝐶𝑖 for which their 𝑣𝑖 and 𝑤𝑖 are in the same cone. Since all nodes from other 𝐶𝑖′ have a distance of at least
𝑏 − 2 · 𝑑(𝑢,𝑤) = 2 − 2𝜖 to 𝑤𝑖, agent 𝑢𝑖 cannot use them on a greedy path 𝑤𝑖 either and thus 𝑢 has no greedy path to 𝑤𝑖.

□
With this limitation in mind, we give a general upper bound on the approximation ratio; although this leaves the case of𝑘 = 6 open for now. Let 𝑓 (𝑘) =
1
1−2𝑠𝑖𝑛( 𝜋
𝑘 ) be the maximum stretch of Θ-routing in a Θ𝑘-graph with 6 < 𝑘 < 𝑛 [46].

Theorem 4.4. For 6 < 𝑘 < 𝑛*, every 2D-Euclidean instance of our game has a* 𝑓 (𝑘) + 𝛼
𝑘
𝑛−1-NE.

Proof. Consider the Θ𝑘-graph on P. With 6 < 𝑘 < 𝑛, the stretch between any two nodes is at most 𝑓 (𝑘) with Θ-routing, which gives a greedy path. The best response of an agent has costs of at least 𝑛 − 1, because the stretch to every other node is at least 1. Thus, the Θ𝑘-graph constitutes a
𝑓 (𝑘) + 𝛼
𝑘
𝑛−1-approximate NE.

□
While this does not yield a constant approximation ratio, we note that, as 𝑛 → ∞, the approximation ratio goes to 𝑓 (𝑘), which can be arbitrarily close to 1; for 𝑘 ≥ 15, it is below 2.

In the following, we establish a baseline constant factor approximation.

Lemma 4.5. Every 2D-Euclidean instance of the game has a 5-approximate NE.

4𝑘+4 )
Proof. Consider the Θ8-graph on P. By Bose, De Carufel, Morin, van Renssen and Verdonschot [13], Θ-routing in any Θ4𝑘+4-graph gives stretches of at most 1 +
2 sin(
𝜋
cos(
𝜋
4𝑘+4 )−sin(
𝜋
4𝑘+4 ) . Thus, the
8 )
maximum stretch of Θ-routing in the Θ8-graph is 1 +
2 sin( 𝜋
cos( 𝜋
8 )−sin( 𝜋
8 ) = 1 +
√
2 , because otherwise
2, which yields a greedy path. In the best response of an agent, its stretch to any other agent is at least 1.

Every agent 𝑢 for whom the other agents are not within a cone with angle at most 𝜋 must build at least 2 edges in its best response. This stems from the fact that an edge to any node 𝑣 can only be part of a greedy path to a node 𝑖 with ∠𝑣𝑢𝑖 ≤ 𝜋
𝑑(𝑢,𝑖)2 = 𝑑(𝑢,𝑖),
𝑑(𝑣,𝑖) =
√︁
𝑑(𝑢,𝑖)2 + 𝑑(𝑢, 𝑣)2 − 2𝑑(𝑢,𝑖)𝑑(*𝑢, 𝑣*) cos(∠𝑣𝑢𝑖) >
√︁

by the law of cosines and as such the path would not be a greedy path.

For every agent $u$ for whom the other agents are within a cone with angle at most $\pi$, at least three cosines of the $\Theta_{5}$-graph are empty and as such agent $u$ only builds at most five edges in the $\Theta_{5}$-graph.

Finally, we consider our stretch function. Edgecos are at least $\alpha$ or $2\alpha$ in the best response, and at least $\alpha$ or $8\alpha$ in the $\Theta_{5}$-graph, depending on whether all other agents are within a cone with a angle at most $\pi$ or not.

Let $u\in\mathcal{P}$. Furthermore, let $\mathbf{s}_{0}$ be the strategy profiles of the $\Theta_{5}$-graph in a metric, where for agent $u$ not all other agents are within a cone with angle at most $\pi$. Also, let $\mathbf{s}_{0}^{\alpha}$ be the strategy of the $\Theta_{5}$-graph where all other agents are within a cone with angle at most $\pi$. Let $\mathbf{s}_{0r}$ and $\mathbf{s}_{0r}^{\beta}$ be the corresponding strategy profiles, where agent $u$'s strategy is changed to its best response, while all other strategies stay unchanged.

For our stretch protocol, we get that the $\Theta_{5}$-graph is a

$$\max\left(\frac{c_{u}(\mathbf{s}_{0r})}{c_{u}(\mathbf{s}_{0r})},\frac{c_{u}(\mathbf{s}_{0r}^{\alpha})}{c_{u}(\mathbf{s}_{0r}^{\beta})}\right)=\max\left(\frac{8\alpha+(1+\sqrt{2})(n-1)}{2\alpha+(n-1)},\frac{5\alpha+(1+\sqrt{2})(n-1)}{\alpha+(n-1)}\right)\leq5$$
2 in the Θ8-graph.

□

approximate NE, because the stretch to all $n-1$ other agents is at least $1$ in a best response and at most $1+\sqrt{2}$ in the $\Theta_{8}$-graph.

The following theorem gives a lower bound on the approximation ratio of Θ𝑘-graphs. For the
Θ8-graphs we used in the last theorem, this bound is tight.

Theorem 4.6. There are 2D-Euclidean instances of our game, where the Θ𝑘-graph is not a (⌈𝑘
2 ⌉ +
1 − 𝜖)-approximate NE.

Proof. We construct a 2D-Euclidean metric by placing nodes in a polar coordinate system.

For now, we assume that the reference direction of the coordinate system is equal to either the bisector of some cone used in the construction of the Θ𝑘-graph if ⌈𝑘
5𝑘 ; 𝜋
2 ⌉ + 1 is odd or the edge of a cone otherwise. Let 𝑢 be located at the origin and let 𝑣 be at distance 1 and angle 0. Let the nodes
𝑤1, ...,𝑤⌈ 𝑘
2 ⌉+1 be at angles evenly spaced out over the interval [− 𝜋
2 + 2𝜋
2 − 2𝜋
5𝑘 ] and at distances
1
2 and thus cos(∠𝑣𝑢𝑤𝑖) > 0). We call this construction 𝐶.

cos(∠𝑣𝑢𝑤𝑖 ) (this is possible, as ∠𝑣𝑢𝑤𝑖 < 𝜋
Agent 𝑢 builds edges to ⌈𝑘
2 ⌉ + 1 nodes in the Θ𝑘-graph because each 𝑤𝑖 is in a different cone. For all 𝑖, we have, by the law of cosines, that
𝑑(𝑢,𝑤𝑖)2 − 1 < 𝑑(𝑢,𝑤𝑖).

12 + 𝑑(𝑢,𝑤𝑖)2 − 2 · 1 · 𝑑(𝑢,𝑤𝑖) cos(∠𝑣𝑢𝑤𝑖) =
√︁
𝑑(𝑣,𝑤𝑖) =
√︁
As such, agent 𝑣 cannot use 𝑢 on greedy paths to any 𝑤𝑖, whereas 𝑢 can use 𝑣 for all of them. If 𝑣
would not have a greedy path to some 𝑤𝑖, this could not be a (⌈𝑘
2 ⌉ + 1 −𝜖)-approximate NE because adding edges to all 𝑤𝑖 without a greedy path would improve 𝑣's costs from at least 𝑍 to less than 𝑍, which by definition of 𝑍 is a large improvement, also by more than a factor of (⌈𝑘
2 ⌉ + 1 − 𝜖). Thus, agent 𝑢 could replace all of its edges with an edge to 𝑣 and still retain greedy paths to all nodes. Let
𝑠𝑐 and 𝑠𝑐′ be agent 𝑢's stretchcosts before and after this move. Agent 𝑢's total costs would improve by a factor of
(⌈ 𝑘
2 ⌉+1)𝛼+𝑠𝑐′
2 ⌉+1)𝑠𝑐−𝑠𝑐′−𝜖
𝛼+𝑠𝑐
which is at least ⌈𝑘
2 ⌉ + 1 − 𝜖 for 𝛼 ≥
(⌈ 𝑘
𝜖
.

In a slightly modified construction, even a global rotation of the cones (i.e. the reference direction of the coordinate system not lining up with the bisector/edge of any cone) cannot achieve better results: First, we note that with cone-rotations of less than 4𝜋
5𝑘 in either direction, the same cones stay occupied by nodes and as such, this construction still holds. Also, a rotation by 𝛽 is equal to a rotation by 𝛽 mod 2𝜋
𝑘 . Thus, we place two copies of 𝐶, which we call 𝐶1 and 𝐶2. The copy 𝐶2 is rotated by 𝑖 2𝜋
𝑘 + 𝜋
𝑘 , for some 𝑖 ∈ N, compared to 𝐶1, and its center is displaced. With this, in any rotation, one of 𝑢1 or 𝑢2 still has to build ⌈𝑘
2 ⌉ + 1 many edges. Additionally, by placing the 𝐶1 and
𝐶2 far enough apart and choosing 𝑖 for the rotation to ensure that they are each contained in cones of 𝑢 of the other that are occupied by some 𝑤𝑖, these do not impact the number of edges agent 𝑢
builds in the Θ𝑘-graph or needs to build in its best response.

□
Thus, we cannot get a better bound on the approximation ratio of Θ8-graphs. However, the approximation factor does not improve by choosing a smaller 𝑘: With 𝑘 = 7 being an odd number, Theorem 4.6 still gives the same lower bound of 5 − 𝜖. With 𝑘 = 6 the known bound on the stretch goes up to at least 7 (and that is not along necessarily greedy paths; to get greedy paths the stretch might be as large as the bound on Θ-routing of 12
√
3) [3]. For smaller values of 𝑘, by Theorem 4.3, there might be no greedy paths between some nodes. But we can achieve a lower approximation ratio by using 𝑘 = 6 or 𝑘 = 8, depending on the instance, which gives the following result.

2−60
√
Theorem 4.7. *Every 2D-Euclidean instance of our game has a* 4+4
√
3
√
3
≈ 4.87-approximate NE.

2−12
√
Proof. First, we note that in the Θ6-graph on P, the maximum stretch is 12
√

Proof.: First, we note that in the $\Theta_{0}$-graph on $\mathcal{P}$, the maximum stretch is $12\sqrt{3}$ with $\Theta$-routing [3], which gives greedy paths.

Let $u\in\mathcal{P}$. Furthermore, let $\mathbf{s_{0}}$ be the strategy profiles of the $\Theta_{k}$-graph in a metric where for agent $n$ out all other agents are within a cone with angle at most $\pi$ and let $\mathbf{s_{0}^{\pi}}$ be the strategy profiles of the $\Theta_{k}$-graph if all other agents are within a cone with angle at most $\pi$. Let $\mathbf{s_{0}}$ and $\mathbf{s_{0}^{\pi}}$ be the corresponding strategy profiles, where $u$'s strategy is changed to its best response, while all other strategies stay unpattern is.

Using the same argument as in Lemma 4.5, we get that the $\Theta_{0}$-graph is a

$$\max\left(\frac{c_{u}(s_{0})}{c_{u}(s_{0})},\frac{c_{u}(s_{0}^{\pi})}{c_{u}(s_{0}^{\pi})}\right)=\max\left(\frac{6\alpha+12\sqrt{3}(n-1)}{2\alpha+(n-1)},\frac{4\alpha+12\sqrt{3}(n-1)}{\alpha+(n-1)}\right)$$

-approximate NE. Next, we consider two cases:

If $\alpha\geq(12\sqrt{3}-\sqrt{2}-1)(n-1)$. Thus, $n\leq\frac{1}{12\sqrt{3}}$ $\frac{6\alpha+12\sqrt{3}(n-1)}{\alpha+(n-1)}$, $\frac{4\alpha+12\sqrt{3}(n-1)}{\alpha+(n-1)}$

$$\leq\max\left(\frac{6\alpha+12\sqrt{3}(\frac{\alpha+1}{12\sqrt{3}-\sqrt{2}-1}-1)}{2\alpha+(\frac{\alpha+1}{12\sqrt{3}-\sqrt{2}-1}-1)},\frac{4\alpha+12\sqrt{3}(\frac{\alpha+1}{12\sqrt{3}-\sqrt{2}-1}-1)}{\alpha+(\frac{\alpha+1}{12\sqrt{3}-\sqrt{2}-1}-1)}\right)$$ $$\leq\frac{4+4\sqrt{2}-60\sqrt{3}}{\sqrt{2}-12\sqrt{3}}$$
3 −
√

$\overline{2}-1)(n-1)$. Then we choose the $\Theta_{8}$-graph and obtain that it is a 
-approximate NE.

If 𝛼 ≤ (12
√

$\cdot$ 1). Then we

$$\max\left(\frac{8\alpha+(1+\sqrt{2})(n-1)}{2\alpha+(n-1)},\frac{5\alpha+(1+\sqrt{2})(n-1)}{\alpha+(n-1)}\right)$$ $$\leq\max\left(\frac{8(12\sqrt{3}-\sqrt{2}-1)(n-1)+(1+\sqrt{2})(n-1)}{2(12\sqrt{3}-\sqrt{2}-1)(n-1)+(n-1)},\right.$$ $$\left.\left.\frac{5(12\sqrt{3}-\sqrt{2}-1)(n-1)+(1+\sqrt{2})(n-1)}{(12\sqrt{3}-\sqrt{2}-1)(n-1)+(n-1)}\right)\right.$$ $$=\frac{4+4\sqrt{2}-60\sqrt{3}}{\sqrt{2}-12\sqrt{3}}$$

-approximate NE.

From Theorem 4.6, we immediately get a lower bound of 4 − 𝜖 for this construction. Improving the lower bound for constructions that involve Θ6-graphs is challenging, since any improvement would also imply an improved lower bound on the stretch factor of the Θ6-graph itself, for which the best known bound is also 4 − 𝜖 [3].

## 5 General Metrics

In this section, we study our model in general metric spaces. Naturally, all negative results from the preceding sections, like hardness and non-convergence results, immediately carry over. Specifically, the results that are not implicit in the proofs in this section is that computing best responses is NP-hard, that GE are not Ω( 𝛼𝑛
𝛼+𝑛) -approximate NE and that GE may not exist.

Hardness of the Existence of Equilibria. Here, we show that deciding whether GE and NE exist in a given instance with an arbitrary metric is NP-hard.

Theorem 5.1. In general metric spaces, is both NP-hard to decide, whether an instance admits a NE
and whether it admits a GE.

Proof. We modify the proof for Theorem 6.1 from Moscibroda, Schmid and Wattenhofer [43]
for 𝑘 = 1 by changing the distances but retaining the same general structure of the space.

We reduce from the NP-complete 3-SAT variant, where each variable occurs in at most three clauses (with clauses with fewer than three literals being allowed) [47].

Let I be such a 3-SAT instance with variables X and clauses C. We use the same reduction function for both NE and GE and first show that the resulting instance has no GE, if there is no satisfying assignment of I and then, that it has a NE otherwise. This suffices, as every NE is a GE.

We construct a metric space with nodes {*𝑦,𝑧,𝑑*} ∪ {𝑎𝑖,𝑏𝑖,𝑐𝑖 | 𝑖 ≤ |C|} ∪ {𝑡𝑢, 𝑓𝑢 | 𝑢 ≤ |X|} with distances as shown in Figure 10, such that 𝑑(𝑐𝑖,𝑡𝑢) = 1.6 − 𝜖 for all positive literals 𝑥𝑢 in 𝐶𝑖 and
𝑑(𝑐𝑖, 𝑓𝑢) = 1.6 − 𝜖 for all negative literals 𝑥𝑢 in 𝐶𝑖. Furthermore, let 𝛼 = 0.6.

First, we note some general properties of NE and GE in this instance. We show that for every
𝑢 ≤ |X|, agent 𝑧 builds exactly one edge to either 𝑡𝑢 or 𝑓𝑢 in any GE. Assume at first, that 𝑧 does not build an edge to either of these nodes. In this case, agent 𝑧's stretch to both nodes is at least
𝑑 (𝑧,𝑐𝑖 )+𝑑 (𝑐𝑖,𝑡𝑢 )
𝑑 (𝑧,𝑡𝑢 )
= 3.6
1.6 > 1 + 𝛼 (each via some 𝑐𝑖 that is at distance 1.6 − 𝜖 to it) and adding one of the edges would be an improving move. Now, assume that 𝑧 builds an edge to both nodes. Since every variable appears in at most three clauses, one of 𝑡𝑢 or 𝑓𝑢 has at most one 𝑐𝑖 at distance 1.6 − 𝜖. If one of them has no 𝑐𝑖 at distance 1.6 − 𝜖, removing the edge to it would only increase the stretch to it by 𝑑 (𝑧,𝑓𝑢 )+𝑑 (𝑓𝑢,𝑡𝑢 )
𝑑 (𝑧,𝑡𝑢 )
− 1 = 2.45
1.6 − 1 < 𝛼. Let, w.l.o.g., 𝑡𝑢 only have 𝑐𝑖 at distance 1.6 −𝜖. If 𝑧 has a path of length at most 3.2 −𝜖 to 𝑐𝑖 that does not include 𝑡𝑢, then agent 𝑧 could remove the edge to 𝑡𝑢 and only the stretch to 𝑡𝑢 would increase from 1 to 𝑑 (𝑧,𝑓𝑢 )+𝑑 (𝑓𝑢,𝑡𝑢 )
𝑑 (𝑧,𝑡𝑢 )
= 2.45
1.6 which is an increase of less than 𝛼 while the stretch to 𝑐𝑖 would not increase. If 𝑧 does not have a path of length at most 3.2 − 𝜖
to 𝑐𝑖, that does not include 𝑡𝑢, then agent 𝑧 could swap the edge from 𝑡𝑢 to 𝑐𝑖 to increase the stretch to 𝑡𝑢 from 1 to 𝑑 (𝑧,𝑓𝑢 )+𝑑 (𝑓𝑢,𝑡𝑢 )
1.6 and decrease the stretch to 𝑐𝑖 from at least 3.2−𝜖
𝑑 (𝑧,𝑡𝑢 )
= 2.45
𝑑 (𝑧,𝑐𝑖 ) = 3.2−𝜖
2+𝜖 to 1
which is an improvement in total.

Thus, we have that for every 𝑢 ≤ |X|, agent 𝑧 builds exactly one edge to either 𝑡𝑢 or 𝑓𝑢 in any GE.

We also note that in any GE, for all *𝑖,𝑢*, the edges (𝑏𝑖,𝑐𝑖), (𝑐𝑖,𝑏𝑖), (𝑏𝑖,𝑎𝑖), (𝑦,𝑧), (𝑧,𝑦), (𝑡𝑢, 𝑓𝑢),
(𝑓𝑢,𝑡𝑢), (𝑎𝑖,𝑑), (𝑏𝑖,𝑑), (𝑐𝑖,𝑑), (𝑡𝑢,𝑑) and (𝑓𝑢,𝑑) have to be built to enable greedy routing because there are, respectively, no other nodes closer to the second node than the first node itself. Furthermore, every 𝑎𝑖 also builds an edge to 𝑏𝑖: If there was no edge to 𝑏𝑖, agent 𝑎𝑖 would need to build an edge to 𝑐𝑖 to have a greedy path to 𝑏𝑖. Then, swapping that edge to 𝑏𝑖 would decrease the stretch to
𝑏𝑖 by 𝑑 (𝑎𝑖,𝑐𝑖 )+𝑑 (𝑐𝑖,𝑏𝑖 )
𝑑 (𝑎𝑖,𝑏𝑖 )
−1 = 3.14
1.14 −1 > 0 while not changing the stretch to 𝑐𝑖 and thus be an improving move.

Agent 𝑦 also builds an edge to every 𝑎𝑖 because the only other possible greedy paths via 𝑏𝑖 and 𝑑
have stretches of 𝑑 (𝑦,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑎𝑖 )
1.96
> 1 + 𝛼 and 𝑑 (𝑦,𝑑)+𝑑 (𝑑,𝑎𝑖 )
𝑑 (𝑦,𝑎𝑖 )
= 3.14−𝜖
𝑑 (𝑦,𝑎𝑖 )
= 4.56
1.96 > 1 + 𝛼. Agent 𝑦 does not build an edge to both 𝑏𝑖 and 𝑐𝑖, for any 𝑖, because if it would do so, it could simply remove the edge to 𝑐𝑖 and increase stretches by at most 𝑑 (𝑦,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑐𝑖 )
𝑑 (𝑦,𝑐𝑖 )
− 1 = 3−𝜖
2+2𝜖 − 1 < 𝛼, because the shortest paths to any 𝑡𝑢 and 𝑓𝑢 use 𝑧 in either case. In fact, agent 𝑦 does not build an edge to any 𝑐𝑖, because if it would do so, it could swap its edge from 𝑐𝑖 to 𝑏𝑖, changing the sum of stretches by at most

$$\frac{d(y,b_{i})+d(b_{i},x_{i})}{d(y,x_{i})}-\frac{d(y,c_{i})+d(c_{i},b_{i})}{d(y,b_{i})}=\frac{3-\epsilon}{2+2\epsilon}-\frac{3+2\epsilon}{2-\epsilon}<0.$$
Now, let there be no satisfying assignment for I. We show that there is no GE in our instance.

Assume for the sake of contradiction that there is a GE. Since for every 𝑢 ≤ |X|, agent 𝑧 builds exactly one edge to either 𝑡𝑢 or 𝑓𝑢 in any GE and there is no satisfying assignment, there has to be some 𝑐𝑖, where 𝑧 does not have an edge to a 𝑡𝑢 or 𝑓𝑢 at distance 1.6 −𝜖. Let 𝑖 be such that this is true for 𝑐𝑖. For there to be a greedy path to 𝑐𝑖, agent 𝑧 needs to build an edge to 𝑏𝑖, 𝑐𝑖 or 𝑑. In fact, if 𝑧 does not build an edge to 𝑏𝑖 or 𝑐𝑖 but only to 𝑑, the stretch to 𝑐𝑖 would be 𝑑 (𝑧,𝑑)+𝑑 (𝑑,𝑐𝑖 )
𝑑 (𝑧,𝑐𝑖 )
= 4.1

does not build an edge to $b_{i}$ or $c_{i}$ but only to $\overline{d}$, the stretch to $c_{i}$ would be $\overline{d(z_{i}d)*d(k_{i}a_{i})}=\frac{4.1}{2*\epsilon}>1+\alpha$. As such, agent $z$ builds an edge to $b_{i}$ or $c_{i}$ Agent $z$ does not build both edges because if it did, it could remove its edge to $c_{i}$ and increase thresholds by

$$\frac{d(z,b_{i})+d(b_{i},c_{i})}{d(z,c_{i})}-1=\frac{3}{2+\epsilon}-1<\alpha.$$

Agent $z$ also does not build an edge to $a_{i}$, because the stretch to $a_{i}$ via $y$ is already $\frac{d(z,y)+d(y,a_{i})}{d(z,a_{i})}=\frac{2*6-2\epsilon}{2+2\epsilon}<1+\alpha$ and the edge to $a_{i}$ would not allow for any shorter greedy paths to $b_{i}$ or $c_{i}$, because 
2+2𝜖
< 1 + 𝛼 and the edge to 𝑎𝑖 would not allow for any shorter greedy paths to 𝑏𝑖 or 𝑐𝑖, because
𝑧 needs an edge to 𝑏𝑖 or 𝑐𝑖 either way.

When looking at the strategies of 𝑦 and 𝑧 pertaining to 𝑎𝑖,𝑏𝑖 and 𝑐𝑖, we again only get the four cases illustrated in Figure 11. We examine all of these possible cases and show that they cannot be part of a GE.

𝑎
𝑏
𝑐
𝑎
𝑏
𝑐
𝑎
𝑏
𝑐
𝑎
𝑏
𝑐

Case 1: In Figure 11a, if 𝑦 adds an edge to 𝑏, the stretch to 𝑏 decreases from 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏)
𝑑 (𝑦,𝑏)
= 3.1
2−𝜖
to 1 and the stretch to 𝑐 from 𝑑 (𝑦,𝑧)+𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑦,𝑐)
= 4−2𝜖
2+2𝜖 to 𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑦,𝑐)
=
3−𝜖
2+2𝜖 , which is a total improvement of more than 𝛼.

Case 2: In Figure 11b, agent 𝑧 can swap its edge from 𝑏 to 𝑐, changing the sum of stretches by
𝑑 (𝑧,𝑦)+𝑑 (𝑦,𝑏)
2
−
3
𝑑 (𝑧,𝑏)
− 𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑧,𝑐)
= 3−3𝜖
2+𝜖 < 0.

Case 3: In Figure 11c, if 𝑦 removes its edge to 𝑏, the stretch to 𝑐 stays unchanged at 𝑑 (𝑦,𝑧)+𝑑 (𝑧,𝑐)
𝑑 (𝑦,𝑐)
=
𝑑 (𝑦,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑦,𝑐)
, while the stretch to 𝑏 increases from 1 to 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏)
𝑑 (𝑦,𝑏)
= 3.1
2−𝜖 which is an increase of less than 𝛼.

Case 4: In Figure 11d, agent 𝑧 can swap its edge from 𝑐 to 𝑏, changing the sum of stretches by
𝑑 (𝑧,𝑏)+𝑑 (𝑏,𝑐)
𝑑 (𝑧,𝑐)
− 𝑑 (𝑧,𝑐)+𝑑 (𝑐,𝑏)
𝑑 (𝑧,𝑏)
=
3
2+𝜖 − 3+𝜖
2
< 0.

Thus, there can be no GE in this instance if there is no satisfying assignment for I.

Now, let 𝐴I be a assignment satisfying I. We construct a NE, as illustrated in Figure 12.

- Agent 𝑦 builds edges to 𝑧 and every 𝑎𝑖 and 𝑏𝑖. - Agent 𝑧 builds edges to 𝑦 and every 𝑡𝑢 where 𝑥𝑢 is true in 𝐴I and every 𝑓𝑢 where 𝑥𝑢 is false
in 𝐴I.
- Agent 𝑑 builds edges to every 𝑎𝑖,𝑏𝑖,𝑐𝑖,𝑡𝑢 and 𝑓𝑢. - Every 𝑎𝑖 build edges to *𝑑,𝑦* and its corresponding 𝑏𝑖. - Every 𝑏𝑖 build edges to 𝑑 and its corresponding 𝑎𝑖 and 𝑐𝑖.
- Every 𝑐𝑖 build edges to *𝑑,𝑧*, its corresponding 𝑏𝑖 and every 𝑡𝑢 and 𝑓𝑢 at distance 1.6 − 𝜖.
- Every 𝑡𝑢 and 𝑓𝑢 builds edges to *𝑑,𝑧*, its corresponding 𝑓𝑢 or 𝑡𝑢 and every 𝑐𝑖 at distance 1.6−𝜖.
We show that no agent has an incentive to change their strategy:
Agent 𝑦: As noted above, the edges to 𝑧 and any 𝑎𝑖 cannot be removed and the edges to any
𝑐𝑖 cannot be added. Thus, the only possible improving changes are dropping the edge to some 𝑏𝑖, adding an edge to 𝑑 or adding an edge to some 𝑡𝑢 or 𝑓𝑢 that 𝑧 does not have an edge to. Dropping an edge to a 𝑏𝑖 would increase stretches by 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏𝑖 )
𝑑 (𝑦,𝑏𝑖 )
− 1 + 𝑑 (𝑦,𝑎)+𝑑 (𝑎,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑐𝑖 )
𝑑 (𝑦,𝑐𝑖 )
− 𝑑 (𝑦,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑐𝑖 )
𝑑 (𝑦,𝑐𝑖 )
=
3.1
2−𝜖 − 1 +
4.1
2+2𝜖 − 3−𝜖
2+2𝜖 < 𝛼. Adding an edge to a 𝑡𝑢 or 𝑓𝑢 that 𝑧 does not have an edge to would decrease stretches by 𝑑 (𝑦,𝑧)+𝑑 (𝑧,𝑓𝑢 )+𝑑 (𝑓𝑢,𝑡𝑢 )
𝑑 (𝑦,𝑡𝑢 )
− 1 = 3.45−2𝜖
2.6−2𝜖 − 1 < 𝛼. Since both of these effects are independent, doing both would not be an improving move either. Adding an edge to 𝑑 would not decrease the stretch to any node even in combination with another change.

Agent 𝑧: As noted above, the edge to 𝑦 cannot be removed. For every 𝑐𝑖, 𝑧 has an edge to a 𝑡𝑢 or
𝑓𝑢 at distance 1.6 − 𝜖 because 𝐴I is a satisfying assignment. Since 𝑧 has to have an edge to exactly one of 𝑡𝑢 and 𝑓𝑢 for each 𝑢, adding or removing edges to any 𝑡𝑢 or 𝑓𝑢 cannot be an improving move either. Swapping an edge between a corresponding 𝑡𝑢 and 𝑓𝑢 only swaps their stretches and can not decrease any other stretches. The stretch to 𝑑 is already 1 and an edge to it cannot be part of any other shorter greedy paths either. Thus, the only possible improving changes are adding an edge to some 𝑎𝑖,𝑏𝑖 or 𝑐𝑖. Since all of these moves just add edges, if none of these is an improving move individually, a combination of them cannot be an improving move either. Adding an edge to some
𝑎𝑖 would decrease stretches by 𝑑 (𝑧,𝑦)+𝑑 (𝑦,𝑎𝑖 )
2+2𝜖
− 1 < 𝛼. Adding an edge to some 𝑏𝑖 would
𝑑 (𝑧,𝑎𝑖 )
− 1 = 2.96−2𝜖
decrease stretches by 𝑑 (𝑧,𝑦)+𝑑 (𝑦,𝑏)
2
− 1 + 3.2−𝜖
𝑑 (𝑧,𝑏)
− 1 + 𝑑 (𝑧,𝑡𝑢 )+𝑑 (𝑡𝑢,𝑐𝑖 )
2+𝜖 < 𝛼.

𝑑 (𝑧,𝑐𝑖 )
− 𝑑 (𝑧,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑐𝑖 )
𝑑 (𝑧,𝑐𝑖 )
= 3−3𝜖
2+𝜖 −
3
Adding an edge to some 𝑐𝑖 would decrease stretches by 𝑑 (𝑧,𝑡𝑢 )+𝑑 (𝑡𝑢,𝑐𝑖 )
𝑑 (𝑧,𝑐𝑖 )
− 1 = 3.2−𝜖
2+𝜖 − 1 < 𝛼.

Agent 𝑑: Dropping any edge would increase the stretch to that node by more than 𝛼 because the distance between any two nodes and thus the increase in distance if 𝑑 would drop an edge is more than 1.3𝛼 = 0.78. The stretch to 𝑦 and 𝑧 is already 1 via another node and an edge to them cannot be part of any other shorter greedy paths either. Thus, building any additional edges cannot improve costs either.

Agent 𝑎𝑖: As noted above, the edges to 𝑑 and any 𝑏𝑖 cannot be removed and the stretch to any node other than 𝑧 is already 1 and an edge to them cannot be part of any other shorter greedy paths either. Thus, the only possible improving changes are removing the edge to 𝑦 and adding one to 𝑧.

Doing both would change stretches by 𝑑 (𝑎𝑖,𝑦)+𝑑 (𝑦,𝑧)
𝑑 (𝑎𝑖,𝑧)
− 𝑑 (𝑎𝑖,𝑧)+𝑑 (𝑧,𝑦)
𝑑 (𝑎𝑖,𝑦)
= 2.96−2𝜖
2+2𝜖
−
3
1.96 < 0. Dropping the edge to 𝑦 would remove the only greedy path to 𝑦. Adding the edge to 𝑧 would decrease only the stretch to it by 𝑑 (𝑎𝑖,𝑦)+𝑑 (𝑦,𝑧)
𝑑 (𝑎𝑖,𝑧)
− 1 = 2.96−2𝜖
2+2𝜖
− 1 < 𝛼.

Agent 𝑏𝑖: As noted above, the edges to 𝑑 and any 𝑎𝑖 and 𝑐𝑖 cannot be removed and the stretch to any node other than 𝑦 and 𝑧 is already 1 and an edge to them cannot be part of any other shorter greedy paths either. Thus, the only possible improving changes are adding edges to 𝑦 or 𝑧.

Adding the edge to 𝑦 would decrease stretches by 𝑑 (𝑏𝑖,𝑎𝑖 )+𝑑 (𝑎𝑖,𝑦)
𝑑 (𝑏𝑖,𝑦)
−1+ 𝑑 (𝑏𝑖,𝑐𝑖 )+𝑑 (𝑐𝑖,𝑧)
𝑑 (𝑏𝑖,𝑧)
− 𝑑 (𝑏𝑖,𝑦)+𝑑 (𝑦,𝑧)
𝑑 (𝑏𝑖,𝑧)
=
2
< 𝛼. Adding the edge to 𝑧 would decrease stretches by 𝑑 (𝑏𝑖,𝑎𝑖 )+𝑑 (𝑎𝑖,𝑦)
2
− 3−3𝜖
𝑑 (𝑏𝑖,𝑦)
−
3.1
2−𝜖 − 1 + 3+𝜖
𝑑 (𝑏𝑖,𝑧)+𝑑 (𝑧,𝑦)
𝑑 (𝑏𝑖,𝑦)
+ 𝑑 (𝑏𝑖,𝑐𝑖 )+𝑑 (𝑐𝑖,𝑧)

𝑑 (𝑏𝑖,𝑧)
          − 1 =
                 3.1
                 2−𝜖 − 3−2𝜖

2−𝜖 + 3+𝜖

                                                           2 − 1 < 𝛼. Since both of these moves just add
edges and neither of them is an improving move individually, a combination of them cannot be an
improving move either.
  Agent 𝑐𝑖: As noted above, the edge to 𝑏𝑖 and 𝑑 cannot be removed and the stretch to any
node other than 𝑦 is already 1 and an edge to them cannot be part of any other shorter greedy
paths either. Furthermore, if 𝑐𝑖 were to remove any of the edges to some 𝑡𝑢 or 𝑓𝑢, the lowest
possible stretch to them even with additional edges elsewhere, would be 𝑑 (𝑐𝑖,𝑑)+𝑑 (𝑑,𝑡𝑢 )

𝑑 (𝑐𝑖,𝑡𝑢 )
          =
              2.6

                                                                                                            1.6−𝜖 >
1 + 𝛼 and thus including these edges would always be a better response. Thus, the only possible
improving changes are dropping the edge to 𝑧 and adding one to 𝑦. Doing both would change
stretches by 𝑑 (𝑐𝑖,𝑧)+𝑑 (𝑧,𝑦)

𝑑 (𝑐𝑖,𝑦)
         − 𝑑 (𝑐𝑖,𝑦)+𝑑 (𝑦,𝑧)

𝑑 (𝑐𝑖,𝑧)
          = 3−𝜖

2+𝜖 < 0. Adding the edge to 𝑦 would decrease

2+2𝜖 −
         3

stretches by 𝑑 (𝑐𝑖,𝑧)+𝑑 (𝑧,𝑦)

𝑑 (𝑐𝑖,𝑦)
         − 1 = 3−𝜖

$\frac{3-\epsilon}{2+2\epsilon}-1<\alpha.$ Dropping the edge to $z$ would increase stretches by ${}_{i})+d(a_{i},y)\qquad d(c_{i},z)+d(z,y)\ =\ \frac{3,2-\epsilon}{2,2-\epsilon}-1+\frac{4,1}{2,2-\epsilon}\ >\ \sigma.$

𝑑 (𝑐𝑖,𝑡𝑢 )+𝑑 (𝑡𝑢,𝑧)

𝑑 (𝑐𝑖,𝑧)
          − 1 + 𝑑 (𝑐𝑖,𝑏𝑖 )+𝑑 (𝑏𝑖,𝑎𝑖 )+𝑑 (𝑎𝑖,𝑦)

$\frac{d(c_{s}t_{n})+d(t_{n}x)}{A\mathbf{g}}-1+\frac{d(c_{s}b_{s})+d(b_{s}a_{s})+d(a_{s}y)}{A\mathbf{g}}-\frac{d(c_{s}x)+d(x,y)}{A\mathbf{g}}=\frac{3-x}{2+x}-1+\frac{41}{3+x}-\frac{3-x}{2+x}>a$.

**Agents $t_{n}$ and $t_{s}$**. As noted above, the edge to $f_{n}/t_{n}$ and $d$ cannot be removed and the stretch to any node is already $1$ and an edge to them cannot be part of any other shorter greedy paths either. Furthermore, analogously to the edges from some $c_{i}$ to some $t_{n}$ or $f_{n^{\prime}}$, the edges to any $c_{i}$ cannot be removed either. Thus, the only possible improving change is dropping the edge to $z$. Doing so would remove their only greedy path to $z$ however.

Thus, there exists a NE if and only if there is a satisfying assignment for $\mathcal{I}$ and there also exists a GE if and only if there is a satisfying assignment for $\mathcal{I}$. Hence, 3-SAT is reducible to our problems in polynomial time. Thus, they are NP-hard.

Approximate Equilibria. We consider the complete graph as approximate NE. The result that we give is the only one that does not depend linearly on 𝑛 or on the distances given by the metric.

Theorem 5.2. Every instance of our game has a (𝛼 + 1)-approximate NE.

Proof. Consider the complete graph on P. The cost of every agent is (𝛼 + 1)(𝑛 − 1) because every agent builds 𝑛 − 1 edges and the stretch to every other node is 1. Since the stretch to any other agent cannot be less than 1, the best response of an agent has costs of at least 𝑛 − 1. Thus, the complete graph constitutes a (𝛼 + 1)-approximate NE.

□
6
CONCLUSION
We give the first game-theoretic network formation model that focuses on creating networks where all-pairs greedy routing is enabled. We believe that this is only the first step to further models that guarantee even more favorable properties to hold in the created networks. For example, guaranteed maximum stretch and robustness aspects. Another avenue for further research is to consider different edge price functions. While we have considered that every edge costs a uniform price of 𝛼, recent work has also considered that the price of edges could depend on the length of the created edge [7]. Finally, it is interesting to explore other techniques for constructing approximate Nash equilibria in the Euclidean setting. We believe, that it might be possible to achieve a better approximation ratio by this.

## References

[1] Mohammad Abam and Mahnaz Qafari. 2019. Geometric Spanner Games. *Theoretical Computer Science* 795 (2019).
https://doi.org/10.1016/j.tcs.2019.07.020
[2] Anna Adamaszek, Matthias Mnich, and Katarzyna Paluch. 2018. New Approximation Algorithms for (1,2)-TSP. In
ICALP'18. 9:1–9:14. https://doi.org/10.4230/LIPIcs.ICALP.2018.9
[3] Hugo A. Akitaya, Ahmad Biniaz, and Prosenjit Bose. 2022. On the Spanning and Routing Ratios of the Directed
Θ6-graph. *Computational Geometry* 105–106 (2022), 101881. https://doi.org/10.1016/j.comgeo.2022.101881
[4] Noga Alon, Erik D. Demaine, Mohammad Taghi Hajiaghayi, and Tom Leighton. 2013. Basic Network Creation Games.
SIAM J. Discret. Math. 27, 2 (2013), 656–668. https://doi.org/10.1137/090771478
[5] Carme Àlvarez and Arnau Messegué Buisan. 2023. On the PoA Conjecture: Trees versus Biconnected Components.
SIAM J. Discret. Math. 37, 2 (2023), 1030–1052. https://doi.org/10.1137/21M1466426
[6] Davide Bilò, Tobias Friedrich, Pascal Lenzner, Stefanie Lowski, and Anna Melnichenko. 2021. Selfish Creation of Social
Networks. In *AAAI'21*. 5185–5193. https://doi.org/10.1609/AAAI.V35I6.16655
[7] Davide Bilò, Tobias Friedrich, Pascal Lenzner, and Anna Melnichenko. 2019. Geometric Network Creation Games. In
SPAA '19. 323–332. https://doi.org/10.1145/3323165.3323199
[8] Davide Bilò, Luciano Gualà, Stefano Leucci, and Guido Proietti. 2016. Locality-Based Network Creation Games. ACM
Trans. Parallel Comput. 3, 1 (2016), 6:1–6:26. https://doi.org/10.1145/2938426
[9] Davide Bilò, Luciano Gualà, and Guido Proietti. 2015. Bounded-Distance Network Creation Games. ACM Trans.
Economics and Comput. 3, 3 (2015), 16:1–16:20. https://doi.org/10.1145/2770639
[10] Thomas Bläsius, Tobias Friedrich, Maximilian Katzmann, and Anton Krohmer. 2020. Hyperbolic Embeddings for Near-
Optimal Greedy Routing. *ACM Journal on Experimental Algorithmics* 25 (2020), 1–18. https://doi.org/10.1145/3381751
[11] Thomas Bläsius, Tobias Friedrich, Maximilian Katzmann, and Daniel Stephan. [n. d.]. Strongly Hyperbolic Unit Disk
Graphs. In *STACS'23*. 13:1–13:17. https://doi.org/10.4230/LIPICS.STACS.2023.13
[12] Marián Boguná, Fragkiskos Papadopoulos, and Dmitri Krioukov. 2010. Sustaining the internet with hyperbolic
mapping. *Nature communications* 1, 1 (2010), 62.
[13] Prosenjit Bose, Jean-Lou De Carufel, Pat Morin, André van Renssen, and Sander Verdonschot. 2016. Towards Tight
Bounds on Theta-Graphs: More Is Not Always Better. *Theoretical Computer Science* 616 (2016), 70–93.
https:
//doi.org/10.1016/j.tcs.2015.12.017
[14] Karl Bringmann, Ralph Keusch, Johannes Lengler, Yannic Maus, and Anisur Rahaman Molla. 2017. Greedy Routing
and the Algorithmic Small-World Phenomenon. In *PODC'17*. 371–380. https://doi.org/10.1145/3087801.3087829
[15] Ankit Chauhan, Pascal Lenzner, Anna Melnichenko, and Louise Molitor. 2017. Selfish Network Creation with Nonuniform Edge Cost. In *SAGT'17*. 160–172. https://doi.org/10.1007/978-3-319-66700-3_13
[16] Ankit Chauhan, Pascal Lenzner, Anna Melnichenko, and Martin Münn. 2016. On Selfish Creation of Robust Networks.
In *SAGT'16*. 141–152. https://doi.org/10.1007/978-3-662-53354-3_12
[17] Vasek Chvátal. 1979. A Greedy Heuristic for the Set-Covering Problem. *Math. Oper. Res.* 4, 3 (1979), 233–235.
https://doi.org/10.1287/MOOR.4.3.233
[18] K. Clarkson. 1987. Approximation Algorithms for Shortest Path Motion Planning. In *STOC '87*. 56–65.
https:
//doi.org/10.1145/28395.28402
[19] Jacomo Corbo and David C. Parkes. 2005. The price of selfish behavior in bilateral network formation. In *PODC'05*.
99–107. https://doi.org/10.1145/1073814.1073833
[20] Andreas Cord-Landwehr, Martina Hüllmann, Peter Kling, and Alexander Setzer. 2012. Basic Network Creation Games
with Communication Interests. In *SAGT'12*. 72–83. https://doi.org/10.1007/978-3-642-33996-7_7
[21] Andreas Cord-Landwehr and Pascal Lenzner. 2015. Network Creation Games: Think Global - Act Local. In *MFCS'15*.
248–260. https://doi.org/10.1007/978-3-662-48054-0_21
[22] Andreas Cord-Landwehr, Alexander Mäcker, and Friedhelm Meyer auf der Heide. 2014. Quality of Service in Network
Creation Games. In *WINE'14*. 423–428. https://doi.org/10.1007/978-3-319-13129-0_34
[23] Erik D. Demaine, MohammadTaghi Hajiaghayi, Hamid Mahini, and Morteza Zadimoghaddam. 2007. The Price of
Anarchy in Network Creation Games. In *PODC '07*. 292–298. https://doi.org/10.1145/1281100.1281142
[24] Hagen Echzell, Tobias Friedrich, Pascal Lenzner, and Anna Melnichenko. 2020. Flow-Based Network Creation Games.
In *IJCAI'20*. 139–145. https://doi.org/10.24963/IJCAI.2020/20
[25] Shayan Ehsani, MohammadAmin Fazli, Abbas Mehrabian, Sina Sadeghian Sadeghabad, MohammadAli Safari, Morteza
Saghafian, and Saber ShokatFadaee. 2011. On a bounded budget network creation game. In *SPAA'11*. 207–214.
https://doi.org/10.1145/1989493.1989523
[26] Stephan Eidenbenz, V. S. Anil Kumar, and Sibylle Zust. 2006. Equilibria in Topology Control Games for Ad Hoc
Networks. *Mobile Networks and Applications* 11, 2 (2006), 143–159. https://doi.org/10.1007/s11036-005-4468-y
[27] Alex Fabrikant, Ankur Luthra, Elitza Maneva, Christos Papadimitriou, and Scott Shenker. 2003. On a Network Creation
Game. In *PODC'03*. 347–351. https://doi.org/10.1145/872035.872088
[28] Wilhelm Friedemann, Tobias Friedrich, Hans Gawendowicz, Pascal Lenzner, Anna Melnichenko, Jannik Peters, Daniel
Stephan, and Michael Vaichenker. 2021. Efficiency and Stability in Euclidean Network Design. In *SPAA '21*. 232–242.
https://doi.org/10.1145/3409964.3461807
[29] Tobias Friedrich, Hans Gawendowicz, Pascal Lenzner, and Arthur Zahn. 2023. The Impact of Cooperation in Bilateral
Network Creation. In *PODC'23*. 321–331. https://doi.org/10.1145/3583668.3594588
[30] Yumin Fu. 1968. Dominating set and converse dominating set of a directed graph. The American Mathematical Monthly
75, 8 (1968), 861–863.
[31] Michael R. Garey and David S. Johnson. 1979. *Computers and Intractability: A Guide to the Theory of NP-Completeness*.
[32] András Gulyás, József J. Bíró, Attila Kőrösi, Gábor Rétvári, and Dmitri Krioukov. 2015. Navigable Networks as Nash
Equilibria of Navigation Games. *Nature Communications* 6, 1 (2015), 7651. https://doi.org/10.1038/ncomms8651
[33] Christos Kaklamanis, Panagiotis Kanellopoulos, and Sophia Tsokana. 2018. On network formation games with
heterogeneous players and basic network creation games. *Theor. Comput. Sci.* 717 (2018), 62–72. https://doi.org/10.
1016/J.TCS.2017.03.041
[34] Richard M. Karp. 1972. *Reducibility among Combinatorial Problems*. 85–103. https://doi.org/10.1007/978-1-4684-2001-
2_9
[35] Bernd Kawald and Pascal Lenzner. 2013. On dynamics in selfish network creation. In *SPAA '13*. 83–92.
https:
//doi.org/10.1145/2486159.2486185
[36] J. Mark Keil. 1988. Approximating the Complete Euclidean Graph. In *SWAT 88*. 208–213. https://doi.org/10.1007/3-
540-19487-8_23
[37] Nikolaos Laoutaris, Laura J. Poplawski, Rajmohan Rajaraman, Ravi Sundaram, and Shang-Hua Teng. 2008. Bounded
budget connection (BBC) games or how to make friends and influence people, on a budget. In *PODC'08*. 165–174.
https://doi.org/10.1145/1400751.1400774
[38] Pascal Lenzner. 2012. Greedy Selfish Network Creation. In *WINE'12*. 142–155. https://doi.org/10.1007/978-3-642-
35311-6_11
[39] Eli A. Meirom, Shie Mannor, and Ariel Orda. 2014. Network formation games with heterogeneous players and the
internet structure. In *EC'14*. 735–752. https://doi.org/10.1145/2600057.2602862
[40] Eli A. Meirom, Shie Mannor, and Ariel Orda. 2015. Formation games of reliable networks. In *INFOCOM'15*. 1760–1768.
https://doi.org/10.1109/INFOCOM.2015.7218557
[41] Matús Mihalák and Jan Christoph Schlegel. 2012. Asymmetric Swap-Equilibrium: A Unifying Equilibrium Concept for
Network Creation Games. In *MFCS'12*. 693–704. https://doi.org/10.1007/978-3-642-32589-2_60
[42] Dov Monderer and Lloyd S Shapley. 1996. Potential games. *Games and economic behavior* 14, 1 (1996), 124–143.
[43] Thomas Moscibroda, Stefan Schmid, and Rogert Wattenhofer. 2006. On the Topologies Formed by Selfish Peers. In
PODC '06. 133–142. https://doi.org/10.1145/1146381.1146403
[44] Giri Narasimhan and Michiel Smid. 2007. *Geometric Spanner Networks*. Cambridge University Press. https://doi.org/
10.1017/cbo9780511546884
[45] Christos H. Papadimitriou. 2001. Algorithms, games, and the internet. In *STOC'01*. 749–753. https://doi.org/10.1145/
380752.380883
[46] Jim Ruppert and Raimung Seidel. 1991. Approximating the D-Dimensional Complete Euclidean Graph. In 3rd Canadian
Conference on Computational Geometry.
[47] Craig A. Tovey. 1984. A Simplified NP-complete Satisfiability Problem. *Discrete Applied Mathematics* 8, 1 (1984), 85–89.
https://doi.org/10.1016/0166-218X(84)90081-7