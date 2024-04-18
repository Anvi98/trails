# Cooperative Agri-Food Export Under Minimum Quantity Commitments

Luis Guardiola1∗, Behzad Hezarkhani2†, Ana Meca3‡
1 Universidad de Alicante, Departamento de Matem´aticas,
03690 San Vicente del Raspeig, Alicante
2 Southampton Business School, University of Southampton, SO17 1BJ, United Kingdom,
3 Universidad Miguel Hern´andez de Elche-I.U. Centro de Investigaci´on Operativa,
03207 Elx, Alicante, Spain

## Abstract

International trade can be a profitable business for agri-food communities. However, access to international markets can be costly and thus unattainable for small and medium sized enterprises (SMEs). This problem is exacerbated under trade policies which require minimum quantity commitments (MQCs) on export volumes, e.g., licensing tariff rate quota (TRQ) mechanisms. We show how cooperative exporting among agri-food SMEs can tackle the barriers posed by the MQCs, and give market access to a broader range of SMEs. We formulate a class of cooperative games associated with these situations and find a gain-sharing mechanism that result in allocations in their corresponding cores. Thus, grand coalitions of cooperative exporting SMEs can form in stable manners. This allocation rule shares the export surplus only among the "essential" SME exporters, that is, the players who are sufficiently cost efficient. Thus, less cost efficient "complimentary" SMEs whose capacities are needed to maintain MQCs receive no benefit from collaborative exporting and their participation have to be altruistic. We propose two modifications to our original allocation rule to share a portion of export surplus among the complementary SMEs through taxing the essential SMEs: the first through egalitarian, and the second through revenue-based rates. We compare the performance of these allocations with the numerical examples and discuss their practical implications.

KEYWORDS: Production, Manufacturing, Transportation and Logistics, Game Theory, International Trade, Cooperative Export

## 1 Introduction

Trade brings about vital business opportunities for businesses in the food supply chain, while also helping to diminish global food insecurity and expanding consumer choices for various goods. The trade in agricultural and food products has experienced substantial growth in the past twenty years, averaging an annual increase of nearly 7% in real terms from 2001 to 2019. Agri-food trade is not only on the rise but is also progressively evolving into a truly global phenomenon (OECD, 2023). Agri-food trade is also heavily reliant on logistics to run the supply chains with costs rallying up against the farm-gate value (Hummels, 2007).

On the other hand, agricultural products have long held an exceptional place in international trade, with protectionist policies being the norm rather than the exception. The sector is often described as remaining sheltered from the large reductions in tariffs, and it is only with the 1994 Uruguay Round Agreement that modest tariff cuts were agreed (Bureau et al., 2019). A host of tariff and non-tariff barriers impede the trade of agri-food products.1 Tariff Rate Quota (TRQ)
mechanisms are the dominant form of tariff barrier in agricultural trade where the destination market rations the volume of exports by charging prohibitive tariffs on exports above certain thresholds (Skully, 2007).

In this paper, our setting resembles the case of exporting under licensing TRQ mechanisms, which are the most common implementation method of TRQ mechanisms (Hranaiova et al., 2006). A licensing mechanism operates in the following manner. Before the quota period begins, potential exporters are invited to apply for export licenses. Applicants specify their intended quantity of exports. After an exporter receives a license, he/she has the right to export their allocated license quantities at a lower tariff rate which would apply if export is done without a license. Deviating from the allocated license quantities involves penalties. Many countries also specify a minimum license amount (Skully, 1987). Such a minimum quantity commitment (MQC), the term we use in this paper, specifies the minimum license quantity that can be allocated to an exporter. Some examples are provided next.

The Australian government sets MQCs for some commodities as follows: 1 tonne for EU high quality beef, 500 tonnes for cotton exported to India, 1 tonne for carrots and potatoes exported to Indonesia, 1 tonne for FTA (Free Trade Agreement) butter and
(Gourdon et al., 2020).

for FTA cheddar cheese for export to the United States of America, among others.2 The Australian government also indicates penalties for underused quota entitlements, and that the amount of the allocation penalty is the amount of the person's tariff rate quota entitlement for the quota type in the next quota year.3 In Canada, license holders that are unable to use their licenses will have their allocations in the following year adjusted downward in proportion to the amount they did not use.4 The UK government indicates that new sugar export applicants must provide evidence to prove that they have exported at least 25 tonnes of sugar during the 12-month period ending two months before the first application.5
In the contemporary landscape of international trade, small and medium-sized enterprises
(SMEs) often find themselves facing formidable challenges when competing against larger industry counterparts. The inherent limitations of SMEs, such as restricted capital, limited production capacity, and narrower market access, can impede their ability to compete on a global scale (Fliess and Busquets, 2006). This hinders the profitability of trade and deprives such enterprises from important growth opportunities.

By joining forces through collaborative initiatives, SMEs can pool their resources, share expertise, and collectively navigate the complexities of international trade. This collaborative approach not only mitigates individual weaknesses but also creates synergies that enhance the overall competitiveness of the participating SMEs. There is a considerable amount of evidence and research on how SMEs can facilitate their access to global markets through collaborative exporter groups, a.k.a. exporter consortia (e.g., Forte and Oliveira (2019)).6
6The export consortia agreement signed by five Jordanian food supplements factories is a real-world example of successful collaboration supporting SMEs in Jordan. This joint effort aims to boost the private sector's contribution to job creation and economic inclusion, particularly for youth and women. Despite the challenges of COVID-19, the collaboration focuses on leveraging the valuable knowledge within the local food supplement sector to explore export markets.

This initiative, extended to sectors like garment and fashion, natural cosmetics, and food supplements exemplifies a collective endeavor to access non-traditional markets. Notably, the agreement with professional uniform clothing manufacturers aims to create an integrated collection targeting east Africa, demonstrating the potential for collaborative ventures to open new opportunities for SMEs.

Export consortia emerge as collaborative solutions, enabling SMEs to pool resources for joint export initiatives. Still, clear mechanisms for cost/gain sharing in such consortia have never been discussed. In this paper, we model cooperative games associated with agri-food export consortia, taking into account practical challenges such as MQCs, and examine cost/gain sharing mechanisms with desirable properties that could stabilize such organizations.

We construct a model wherein SMEs engage in the production of a certain agri-food commodity and, in line with a requirement of common market access mechanisms, are required to commit to the quantities they intend to export to a specific international market. The committed export quantity has to be at least as large as a predefined MQC that is established by regulatory authorities.

Initially, we analyze the optimal order quantities for each exporting company based on their costs and profit margins, leading to a categorization of firms according to their export strategies. Our focus then shifts to the examination of cooperation among SMEs, specifically those whose individual capacities fall below the MQC, a.k.a., SMEs. We demonstrate that identifying the optimal coalition of firms for export is an NP-Hard problem. The rationale for such cooperation becomes evident, as no single company or group has an incentive to abandon the grand coalition due to a profit distribution rule that satisfies all SMEs. Additionally, we explore two profit distribution rules to justly compensate complementary SMEs, those that individually find exporting unprofitable but do so for the benefit of the group. Finally, we provide several illustrative examples showcasing optimal benefits and orders for cooperating SMEs, applying and discussing various proposed profit distribution rules This paper is organized into five sections. Section 2 provides a review of the related literature.

Subsequently, Section 3 introduces definitions and notations in cooperative game theory. In Section 4, we present the individual export model, both with and without an MQC, examining the behavior of exporters and their optimal order size. Moving to Section 5, we analyze a model derived from scenarios where multiple SMEs, each with a MQC, collaborate to form a coalition. This section ranks the SMEs based on their costs and benefits, determining their optimal order size. In Section 6, we examine the cooperative model and demonstrate that identifying the subset of firms within a coalition that should engage in export activities to achieve the optimal profit is an NP-hard problem. Section 7 defines the cooperative game arising from this model, explores its primary properties, and establishes the stability (in the sense of the core) of the Non-essential Exporter Altruistic rule, distributing all profits among exporters without allocating any to others. Section 8 shifts focus to two alternative profit allocation methods that compensate complementary enterprises for their contribution to the overall profit increase. Finally, Section 9 offers a comprehensive summary of the paper's outcomes and contributions, concluding with suggestions for future research directions.

## 2 Literature Review

The literature on international trade in operations, logistics, and supply chain management is scarce but growing.

In Charoenwong et al. (2023), the authors employ firm-level global supply chain data, transaction-level shipping container data, and policy uncertainty indexes from prominent media outlets to investigate the correlation between policy uncertainty and shifts in supply chain networks.

Fan et al. (2022) provide an overview of operations and supply chain management research incorporating the role of political economy in global trade. Lam et al. (2022) investigate the impact of foreign competition on the product quality of domestic firms. Dong and Kouvelis (2020) examine the contemporary research on global supply chain management and study the effect of tariffs on the configuration of the global supply chain networks. Cohen and Lee (2020) explores research opportunities on how global supply chain modeling can inform the way firms react to changes in relevant government policies for manufacturing and logistics, including tariffs, content requirements, taxes, and investment incentives. Nagurney et al. (2019a,b,c) developed a spatialprice network equilibrium model of TRQ mechanisms to analyze the joint export quantity decisions, route selection, and equilibrium prices. This paper contributes to this line of work by introducing a pragmatic approach to cooperation among SME exporters to bypass challenges posed by MQC requirements in international trade.

There is a substantial body of work on trade mechanisms in the economics literature. Among the most notable contributions is Skully (1987) who develops a basic static model for TRQs and investigates different administration methods, including FCFS and license on demand. In Boughner et al. (2000), the authors study the economic effects of TRQ mechanism following the Uruguay Round Agreement on Agriculture, focusing on changes in tariffs, quotas, and market conditions. They emphasize how export quota allocation and distribution procedures impact TRQ efficiency. Gervais and Surprenant (2003) examines the impact of discretionary and non-discretionary methods for allocating TRQs in the Canadian chicken industry. Larue et al. (2007) compares export tariffs and quotas in Canada's dairy industry, managed by a marketing board. The study explores welfare rankings between price-equivalent quotas and tariffs, considering different assumptions about the marketing board's powers. Hezarkhani et al. (2023) examines the logistical issues associated with TRQ mechanisms in international trade and show how the lead-time, warehousing, and the choice of logistics channel impact the performance of TRQ mechanisms in terms of fill-rate and policymaker's revenue. Central to this paper is overcoming the constraints imposed by licensing TRQ
mechanisms with regard to MQCs through cooperation.

This paper examines the horizontal collaboration among producers in international supply chains. It applies cooperative game theory to establish appropriate ways to share gains among cooperating enterprises in supply chains (see Lozano et al. (2013) for a review of application domains in this context). Cooperative game theory has been used to address many supply chain problems, inasmuch as there are review papers tailored to specific contexts—e.g., cooperative transportation
(Cruijssen et al., 2007), cooperative logistics network design (Hezarkhani et al., 2021), cooperative inventory management (Fiestras-Janeiro et al., 2011, 2012, 2013, 2014, 2015), cooperation in assembly systems Bernstein et al. (2015), cooperative sequencing (Curiel et al., 2002), cooperative advertising (Jørgensen and Zaccour, 2014), cooperative distribution chain (Guardiola et al., 2007) and (Guardiola et al., 2023) among others. Still, there are many ad hoc application domains, e.g., cooperative procurement Hezarkhani and Soˇsi´c (2019), responsible sourcing (Fang and Cho, 2020), vaccination supply chains (Westerink-Duijzer et al., 2020). In Nagarajan and Soˇsi´c (2008), Meca and Timmer (2008) and Rzeczycki (2022) we find different surveys that examine the applications of cooperative game theory in the context of supply chain management. Our work constitutes yet another area of supply chain management which can be fruitfully analyzed through cooperative game theory.

Operations research has been intertwined with cooperative game theory to develop dedicated methods. Anily and Haviv (2010) and Karsten et al. (2015) study cooperation in service systems where enterprises pool capacities to serve costumers and studies the core of these games. Armony et al. (2021) further incorporates the strategic behaviour of customers in analyzing the pooling in service queues. He et al. (2012) further examines the submodularity of objective functions in joint replenishment games. Liu et al. (2018) introduces an instrument for maintaining the stability of grand coalitions by penalizing the deviations of the enterprises. Fang and Cho (2014) studies cooperative inventory transshipment games where endogenous coalition formation is allowed. Our paper combines OR models with the concept of core to characterizes conditions for stable cooperation among SME exporters to international markets.

## 3 Preliminaries Cooperative Game Theory

A cooperative game with transferable utility (TU-game) comprises a set of players N = {1, 2, ..., n}
and a characteristic function v, which associates each subset of N with a real number. The subsets of N are referred to as coalitions, denoted by S. Formally, the characteristic function is a mapping v : 2N −→ R such that v(∅) = 0. The value v(S) of the characteristic function represents the maximum benefit that members of the coalition S can achieve through cooperation. The coalition consisting of all agents, N, is termed the grand coalition. The subgame related to coalition S, is the restriction of the mapping v to the subcoalitions of S.

One of the central inquiries in cooperative game theory revolves around the equitable distribution of benefits within the grand coalition after its formation. This distribution is achieved through allocations, represented by a vector x ∈ Rn, where n denotes the number of players in the set N.

The class of superadditive games is particularly intriguing, serving as a motivation for the establishment of the grand coalition as it guarantees maximum profits for the coalition. Formally, a transferable utility (TU) game (*N, v*) is deemed superadditive if, for every two coalitions S, T ⊆ N with S ∩ T = ∅, it holds that v(S ∪ T) ≥ v(S) + v(T). Furthermore, TU-games characterized by higher profits for larger coalitions are termed strictly increasing monotone games. This can be expressed equivalently as v(S) ≤ v(T) for all S ⊆ T ⊆ N. An imputation for the game (*N, v*) is an the game is denoted by I(N, v).

allocation which verifies �
i∈N xi = v(N) and xi ≥ v({i}) for all i ∈ N. The set of imputations of Cooperative game theory provides diverse approaches for dividing the profits arising from collaboration. Two main categories of solutions exist: set solutions and point solutions. Set solutions involve the exclusion of allocations that fail to meet specific conditions, retaining only those that do. On the other hand, point solutions are derived through axiomatic characterization, meaning they are the unique allocations that satisfy specific properties.

The core of a game is defined as the primary set solution. It encompasses all efficient allocations that maintain coalition stability, meaning no coalition has a motivation to exit the grand coalition without diminishing its overall profit. In formal terms,

$$Core(N,v)=\left\{x\in\mathbb{R}^{n}:\sum_{i\in N}x_{i}=v(N)\text{and}\sum_{i\in S}x_{i}\geq v(S),\forall S\subset N\right\}.$$
The findings by Bondareva (1963) and Shapley et al. (1967) offer a crucial criterion: the core of a TU game is guaranteed to be non-empty if and only if the game is balanced. This represents a key theorem in cooperative game theory. It is a totally balanced game if the core of every subgame is nonempty. Totally balanced games were introduced in Shapley and Shubik (1969). A game (*N, v*)
is regarded as convex if for all i ∈ N and all *S, T* ⊆ N such that S ⊆ T ⊂ N with i ∈ S, then v(S)−v(S\{i}) ≤ v(T)−v(T \{i}). It is widely acknowledged that convex games are superadditive, and superadditive games are totally balanced. Shapley (1971) establishes that convex games are balanced and its core is large enough.

The nucleolus, a notable solution, is based on a notion of social equity. This solution relies on the concept of excess. Given a cooperative game (*N, v*) and an allocation x ∈ Rn, for any S ⊂ N the the degree of dissatisfaction of coalition S with the selected allocation x. The coalition with the excess of S with respect to x is defined by e(*S, x*) = �
i∈S xi − v(S). The excess function measures smallest excess is the coalition that most disagrees with the allocation. For any allocation x ∈ Rn, let θ(x) = (e(*S, x*))S⊆N;S̸=∅ ∈ R2n−1 be the vector of the excesses of the coalitions with respect to x with the coordinates rearranged in decreasing order. The nucleolus is the set of imputations which lexicographically maximizes the vector of excesses.

$$\eta(N,v)=\left\{x\in I(N,v):\theta(x)\succeq_{l e x}\theta(y),\forall y\in I(N,v)\right\}$$
where θ(x) ⪰lex θ(y) means θ(x) = θ(y) or there exists l, 1 ≤ l ≤ 2n − 1, such that θk(x) =
θk(y) for all *k < l,* and θl(x) *> θ*l(y). Although the nucleolus is defined as subsets of allocations, Schmeidler (1969) showed that each consists of a unique allocation. The nucleolus of a game whose core is non-empty belongs to the core and it is considered as the lexicographical centre of the core.

A point solution φ refers to a function that, for each TU-game (*N, v*), determines an allocation of v(N). Formally, we have φ : GN −→ Rn, where GN denotes the class of all TU-games with player set N, and φi(*N, v*) represents the profit assigned to player i ∈ N in the game v ∈ GN.

Therefore, φ(*N, v*) = (φi(*N, v*))i∈N is a profit vector or allocation of v(N). The nucleolus is a point solution. For a comprehensive overview of cooperative game theory, we recommend referring to Gonz´alez-Dıaz et al. (2010).

## 4 Model

A set of enterprises N = {1*, ..., n*} produce a common agri-food commodity. Each enterprise has the option to supply domestic market or export to international markets. For an arbitrary enterprise i ∈ N, we denote the production capacity with Qi > 0 which indicates the maximum amount of produce that the enterprise can supply. We normalize the cost of production to zero for all enterprises.

Enterprises must decide how much to export.7 But prior to that, an enterprise wishing to engage in exports must commit a specific quantity of export to the export control authority. This can be in the form of acquiring export licenses under a TRQ mechanism.8 The export commitment level of enterprise i is denoted with mi ≥ 0. That is, the export volume committed by the enterprise and approved by the export control authority. After making a commitment and at the time of export, an enterprise i needs to decide the export quantity which is denoted by 0 ≤ qi ≤ Qi.

For every unit of exported produce, enterprises gain the export revenue p ≥ 0. W.l.o.g, we normalize the revenue for supplying to domestic market to zero. To be able to export, however, the enterprise i has to incur a fix cost ci ≥ 0 in order to prepare the produce for international market. For instance, this pertains to measures specific to production or those related to sanitary and phytosanitary requirements mandated by the target market.

Deviating from a committed export volume entails two types of penalties: per unit over-supply penalty ro ≥ 0, and per unit under-supply penalty ru ≥ 0. For example, in case the commodity is subject to a TRQ mechanism, if an enterprise exports above the volume of licenses that it posses, an over-quota tariff rate will be applied to every unit of excess export. Under-supply penalty can be applied per unit or be in terms of sanctions for future exports. For example, many governments curtail the future access to licenses for an enterprise who fails to fulfil its committed volume of exports.

It is a customary practice for authorities to establish a minimum threshold for the export commitment level (see the introduction for specific examples). We call this a minimum quantity commitment (henceforth MQC) and denote it with m ≥ 0. Thus, in order for an enterprise i to export, it must make a commitment at least as large as the MQC, that is, mi ≥ m. The presence of positive MQCs has significant impacts on export decisions as we examine next.

pay the corresponding penalty. However, this is not practical and as such we exclude this possibility.

## 5 Individual Exporting

We initiate our analysis by considering the non-cooperative scenario in which enterprises export individually. Let ∆i := Qip − ci be the full capacity margin of exporting for an enterprise i ∈ N.

In order to examine the exporters decision making problems, we first consider the case with zero MQC, i.e., m = 0 and later on incorporate *m >* 0 into the model.

## 5.1 Exporting Under Zero Mqc

We refer to the case of m = 0 as a setting without a (positive) MQC. In this case, an enterprise's choice of commitment has no positive lower bound, that is, mi ≥ 0. We formulate the individual profit function of the enterprises next. The case of committing to zero exports (mi = 0) and the subsequent decision to export nothing (qi = 0), leading to the normalized profit of zero, is used as the benchmark against any positive export strategy. For an enterprise i ∈ N, the choice of commitment level mi > 0, and export quantity 0 ≤ qi ≤ Qi results in the following profit:

$$\Pi_{i}(q_{i},m_{i})={\bf1}_{q_{i}>0}\Delta_{i}-(q_{i}-m_{i})^{+}\,r^{o}-(m_{i}-q_{i})^{+}\,r^{u}.\tag{1}$$
where 1qi>0 = 1 if qi > 0 and 1qi>0 = 0 if qi = 0, and (·)+ = max{·, 0}. The optimization problem for i is thus:

$$\max\quad\Pi_{i}(q_{i},m_{i})\quad s.t.\quad m_{i}\geq0,0\leq q_{i}\leq Q_{i}.\tag{2}$$
The first observation is that without a positive MQC, agents bifurcate into two categories: those who fully utilize their capacity to export on the international market and those who focus on the domestic market. The Appendix provides the proofs of all results.

Lemma 1. *Without a MQC required for export, i.e.,* m = 0, for every enterprise i ∈ N the following holds:

(A) Exporters: If ∆i ≥ 0 we have q∗
i = m∗
i = Qi.
(B) Domestic producers: Otherwise, we have q∗
i = m∗
i = 0.
Without a MQC required for export, every enterprise i ∈ N with ∆i ≥ 0 could commit his entire capacity for export, i.e., mi = Qi. Otherwise, any enterprise i ∈ N such that ∆i < 0 is better off supplying the domestic market only. Figure 1 demonstrates these relationship graphically. The optimal profit of the enterprise i is the maximum of zero and his full capacity margin, that is:

$\Pi_{i}(q_{i}^{*},m_{i}^{*})=(\Delta_{i})^{+}$.

## 5.2 Exporting Under Positive Mqcs

We now incorporate the positive MQC constraint into the model. Define δi := Qi(p+ru)−ci as the under-supply adjusted (full capacity) margin of exporting for i. With the introduction of *m >* 0, the optimization problem of an enterprise i ∈ N becomes as

$$\max\quad\Pi_{i}(q_{i},m_{i})\quad s.t.\quad m_{i}\geq{\bf1}_{q_{i}>0}\underline{m},0\leq q_{i}\leq Q_{i}.\tag{4}$$
The maximization problem must maintain a commitment at least as large as the MQC whenever a positive quantity is to be exported. We follow the same logic as previous case to optimize the decisions on export quantity and commitment level.

Lemma 2. Given a MQC, m > 0, for any enterprise i ∈ N the following holds:

(A) Type α **Exporters:** If Qi ≥ m and ∆i ≥ 0, we have q∗
i = m∗
i = Qi.
(B) Type β **(SME) Exporters:** If Qi < m and δi − mru ≥ 0, we have q∗
i = Qi, and m∗
i = m.
(C) Domestic producers: Otherwise, we have q∗
i = m∗
i = 0.
All exporting enterprises would utilize their entire capacity to export. Type β exporters, which corresponds to SMEs due to their capacities being smaller than m, would have to under-supply with regard to the MQC and thus have to pay the under-supply penalty. Yet, type β SMEs find it profitable to do so. Figure 2 demonstrates these relationship graphically. The profit function of an enterprise i at optimality in this case is

$$\Pi_{i}(q_{i}^{*},m_{i}^{*})=\begin{cases}(\Delta_{i})^{+}&\text{if}Q_{i}\geq\underline{m}\\ (\delta_{i}-\underline{mp}^{u})^{+}&\text{if}Q_{i}<\underline{m}\end{cases}.\tag{5}$$

Comparing to the case without MPCs, we can see that in this scenario SMEs, i.e., those $i$ with 
Qi *< m*, would only export if they can afford the under-supply penalty. Therefore, the capacity of an enterprise in comparison with to the MQC is a major factor that determines SMEs' export strategies.

## 6 Cooperative Exporting

As seen above, the introduction of MQCs makes it more difficult for SMEs to export. This can be remedied through collaboration with other SMEs. We develop the decision making problem for a group of SMEs S ⊆ N with Qi *< m* for all i ∈ S, that is, a coalition of SMEs. From now on, we will refer to the enterprises as players.

We define a collaborative exporting situation, abbreviated as a CE-situation, by a tuple (*N, Q, C, p, m*)
where N stands for the set of players, Q = (Qi)i∈N denotes the vector of production capacities
(with Qi *< m* for all i ∈ N), C = (ci)i∈N represents the vector of fixed costs to export, and p and m referring to the export margin and the MQC as defined previously, respectively.

Let q = (qi)i∈N be the vector of export quantities (note that we do not restrict the vector to players in S in order to simplify notation). Also, suppose that the commitment level of the coalition

is fixed to $m\geq\underline{m}$. The profit function for $S$ is:

$$\Pi^{S}(q,m)=\sum_{i\in S}\mathbf{1}_{q_{i}>0}\Delta_{i}-\left(\sum_{i\in S}q_{i}-m\right)^{+}r^{o}-\left(m-\sum_{i\in S}q_{i}\right)^{+}r^{u}\tag{6}$$
The optimization problem for the coalition of players in S ⊆ N is

$$\max\quad\Pi^{S}(q,m)\quad s.t.\quad m\geq{\bf1}_{\sum_{i\in S}q_{i}>0}\underline{m},0\leq q_{i}\leq Q_{i},i\in S.\tag{7}$$
Let (qS, mS) be the optimal solution for S, i.e., the solution to the above problem.

It follows immediately that ΠS(qS, mS) ≥ 0. Given the structure of this optimization problem, it can be inferred that over-supply is never occurs at optimality. Thus ro never impacts the optimal solution.

In order to develop observations about the nature of optimal export consortia (coalitions), we define three player types.

Definition 1. Let S ⊆ N be a coalition of player. We define the following terms:
Essential SMEs of S: SE = {i ∈ S|Qi < m, ∆i ≥ 0}

## Potential Smes Of S: Sp = {I ∈ S|Qi < M, Δi ≥ 0} Complementary Smes Of S: Sc = Sp \ Se.

The *essential* SMEs have non-negative full capacity margins. If an essential SME would not export on his own, it would have been because of his capacity limitation rather than cost-inefficiency.

The *potential* SMEs have non-negative under-supply adjusted margins. Note that SE ⊆ SP since non-negativity of full capacity margins implies the non-negativity of under-supply adjusted margins.

The *complementary* SMEs are potential but not essential. For every players in SC we have ∆i < 0
and δi ≥ 0. Figure 3 demonstrates the different types of players in cooperative exporting graphically.

To focus on SMEs, from this point on we assume that N is solely comprised of SMEs, that is, we assume for every i ∈ N we have Qi *< m*. The following theorem illustrates the optimal export strategies (quantities and commitment levels) of a coalition and shed light on the the role of different types of players.

Theorem 1. Consider a coalition S ⊆ N and let (qS, mS) be an optimal solution for S.
                                                                      If
�
 i∈S qS
     i > 0, then we have the following cases:

(A) If �
i∈SE Qi ≥ m*, then* mS = �
i∈SE Qi, qS
i = Qi for all i ∈ SE, and qS
i = 0 for i ∈ S \ SE.
(B) If �
i∈SE Qi < m, then for some RS ⊆ S such that SE ⊆ RS ⊆ SP *, we have* mS =
If a coalition of SMEs exports at optimality, all essential players therein, i.e., SE, export their

max
�
m, �
i∈RS Qi
�
, qS
i = Qi for all i ∈ RS, and qS
i = 0 for i ∈ S \ RS.
full capacity. If the combined capacity of the essential players is large enough to match or surpass the MQC, then no other players would be exporting. However, if the combined capacity of essential players falls short of MQC, it could be optimal for some complementary players to export as well. Although these players do not have non-negative full capacity margins, their inclusion could be beneficial as they could reduce the under-supply penalty imposed to the essential players if they export on their own. Altogether, optimal export decisions of the complementary SMEs in a coalition depends on the capacities of the essential SMEs in that coalition. Theorem 1 reveals the intrinsic power of the essential players. If a player is essential, it always exports in a coalition which exports at optimality. The optimal profit of a coalition is bounded by their aggregate full capacity export margins, as shown in the next corollary.

As shown by Theorem 1, the exporting SMEs in a coalition only includes complementary players Corollary 1. For every S ⊆ N we have Π(qS, mS) ≤ �
i∈SE ∆i.

if the aggregate capacities of associated essential players is less than the MQC. In this case, however, one needs to find the optimal subset DS ⊆ SC of complementary SMEs.

We now discuss the

optimisation problem for finding $D^{S}$. For $S\subseteq N$, and $D\subseteq S^{C}$ we define the function $G$ as

$$G^{S}(D)=\sum_{i\in D}\Delta_{i}+\min\left\{\frac{m}{n}-\sum_{i\in S^{E}}Q_{i},\sum_{i\in D}Q_{i}\right\}r^{n}.\tag{8}$$
The value of GS(D) is the contribution of complementary players in D if they export along with the essential players SE in the export consortia of S. In coalitions that need complementary players, equivalent to maximizing the contribution of complementary players, as we show in the next result.

i.e., S ⊆ N such that �
i∈SE Qi *< m*, the problem of finding the optimal set of exporting players is DS ∈ arg maxD⊆SC GS(D).

Proposition 1. Given S ⊆ N*, if* �
i∈SE Qi < m and RS ̸= ∅, we have RS = SE ∪ DS where For every coalition S ⊆ N, finding the optimal set of complementary SMEs DS ∈ arg maxD⊆SC GS(D)
readily obtains the optimal set of exporting players by adding the corresponding essential players, i.e., RS = SE ∪ DS. However, this optimization problem is NP-hard.

## Proposition 2. The Problem Of Finding Ds Is Np-Hard.

As the proof shows, the problem of finding DS (which is equivalent to the problem of finding RS) is a variation of the {0, 1}-knapsack problem which is known to be NP-hard (Pisinger and Toth, 1998).

As we have just demonstrated, identifying the optimal set of exporters for a specific coalition of SMEs is not a trivial matter. Furthermore, the reader may wonder whether this collaboration makes sense, i.e., if it is beneficial for all coalition members, and if there are benefit-sharing allocations that can be acceptable by all coalition members. To address this issue, the next section will define the cooperative games associated with such situations and show that the cooperation among SMEs can always be made profitable for all the enterprises.

## 7 Cooperative Export Games

For each CE-situation (*N, Q, C, p, m*), we can define an associated TU-game (*N, v*), referred to as a cooperative export game (hereafter, a CE-game), where the value of a coalition is the optimal profit of that coalition as calculated in (7) in the previous section. Thus, for S ⊆ N the characteristic function is v(S) := ΠS(qS, mS). Note that the game can be explicitly defined as follows:

$$v(S)=\begin{cases}\sum_{i\in R^{S}}\Delta_{i}-\left(\underline{m}-\sum_{i\in R^{S}}Q_{i}\right)^{+}r^{u}&\text{if}R^{S}\neq\emptyset,\\ 0&\text{if}R^{S}=\emptyset.\end{cases}\tag{9}$$

where $R^{S}=\{i\in S:q_{i}^{S}>0\}\subseteq S^{P}$ is the optimal set of exporting players in $S$, and $v(\emptyset)=0$.

As we already mentioned in Section 6, v(S) ≥ 0. Alternatively, for every S ⊆ N such that 0 <

�
 i∈RS Qi ≤ m we have v(S) = �
              i∈S δi − mru, and for every S ⊆ N such that �
                                  i∈RS Qi > m we

be useful for the study of CE-games.

have v(S) = �
             i∈S ∆i. The following lemma highlights some properties of CE-situations that will

Lemma 3. Let (N, Q, C, p, m) be a CE-situation. Let S0 ⊆ NE be an arbitrary subset of essential

players and S = S0 ∪ NC. If RS, RN ̸= ∅. It holds that

(i) �
i∈DS ∆i ≤ �
i∈DN ∆i.
(ii) �
i∈DS ∆i −
�
m − �
i∈RS Qi
�+ ru ≤ �
i∈DN ∆i −
�
m − �
i∈RN Qi
�+ ru.
Recall that DS is the optimal set of complementary exporting SMEs in S. Property (i) asserts that the total full capacity margin of optimal complementary players in sub-coalitions, which include a subset of essential players, is never larger than that in the grand coalition. Considering that full capacity margins are negative for complementary players, in absolute terms, the grand coalition employs a set of complementary players with a smaller or equal full capacity margin. Property (ii) is a technical observation which helps in proving the subsequent results. The next proposition elucidates the main properties of CE-games, including superadditivity.

Proposition 3. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game.

The following statements hold:

(i) v(T) = 0 for all T ⊆ N \ NE.
(ii) v(S \ T) = v(S) for all T ⊆ S \ SP .
(iii) v(S ∪ T) ≥ v(S) + v(T) for all disjoint sets S, T ⊆ N.
(iv) v(S) ≤ v(T) for all S ⊆ T ⊆ N.
Property (i) indicates that in coalitions where there are no essential players, there is no export.

Meanwhile, property (ii) asserts that players who do not export under any circumstances contribute no benefit to the coalition. Property (iii) states that CE-games are superadditive. Consequently, the formation of the grand coalition is justified. On the other hand, property (iv) shows that the game is monotone increasing.

Before exploring the allocation of profits from this cooperation among the players, we illustrate a three-player CE-situation and its associated game with an example.

| S    | R   |
|------|-----|
| S    |     |
| |    |     |
| (    | S   |
| \    |     |
| R    |     |
| S    |     |
| )    | v   |
| {    |     |
| 1    |     |
| }    | ∅|{ |
| 1    |     |
| }    |     |
| 0    |     |
| {    |     |
| 2    |     |
| }    |     |
| {    |     |
| 2    |     |
| }|∅  |     |
| 406  |     |
| {    |     |
| 3    |     |
| }    | {   |
| 3    |     |
| }|∅  |     |
| 18   |     |
| {    |     |
| 1    | ,   |
| }    | {   |
| 1    | ,   |
| }|∅  |     |
| 825  |     |
| {    |     |
| 1    | ,   |
| }    |     |
| {    |     |
| 1    | ,   |
| }|∅  |     |
| 437  |     |
| {    |     |
| 2    | ,   |
| }    | {   |
| 2    | ,   |
| }|∅  |     |
| 1034 |     |
| {    |     |
| 1    | ,   |
| }    | {   |
| 1    | ,   |
| }|∅  |     |
| 1383 |     |

Example 1. Consider a scenario with three players N = {1, 2, 3}*. We have* Q1 = 14 , Q2 = 33, Q3 = 21, c1 = 15, c2 = 7, c3 = 23*. Let* p = 21, m = 61*, and* ru = 10. The coalitions' optimal profits and strategies are shown in Table 1.

All players are essential, but player 1 cannot export profitably on his own unlike the other two players who could do so individually. Any coalition that is formed of two or more players will export profitably. Note that this game is not convex: 349 = v({1, 2, 3}) − v({2, 3}) *< v*({1, 2}) − v({2}) =
419. We can find stable allocations in the core for this game. For instance, distributing the benefits of the grand coalition proportionally to ∆i *among all essential players, that is* (279, 686, 418), gives an allocation in the core.

The CE-games are not generally convex as seen in Example 1, thus the Shapley value (Shapley,
1953) is not necessarily in the core (in addition to being computationally challenging). We now introduce the NEA-allocation rule which is always in the core and also computationally easy to calculate.

Let (*N, Q, C, p, m*) be a CE-situation, and let (*N, v*) be the corresponding CE-game, we define

the allocation $\phi(N,v)=(\phi_{i}(N,v))_{i\in N}$ as follows:

$$\phi_{i}(N,v):=\begin{cases}\dfrac{\Delta_{i}}{\sum_{j\in N^{E}}\Delta_{j}}v(N)&\text{if}i\in N^{E}\\ 0&\text{otherwise}\end{cases}\tag{10}$$

The above allocation rule divides the gains of the grand coalition among the essential players
proportional to their individual full capacity margins. All other players will receive zero benefit from cooperative exporting. This includes the the complementary SMEs who do export along with

| S   | R   |
|-----|-----|
| S   |     |
| |   |     |
| (   | S   |
| \   |     |
| R   |     |
| S   |     |
| )   | v   |
| {   |     |
| 1   |     |
| }   | ∅|{ |
| 1   |     |
| }   |     |
| 0   |     |
| {   |     |
| 2   |     |
| }   |     |
| ∅|{ |     |
| 2   |     |
| }   |     |
| 0   |     |
| {   |     |
| 3   |     |
| }   | ∅|{ |
| 3   |     |
| }   |     |
| 0   |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 9   |     |
| {   |     |
| 1   | ,   |
| }   |     |
| {   |     |
| 1   | ,   |
| }|∅ |     |
| 5.5 |     |
| {   |     |
| 2   | ,   |
| }   | {   |
| 2   | ,   |
| }|∅ |     |
| 5.5 |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 13  |     |

the essential players, i.e., DN. So, complementary SMEs' participation in the export consortia has to be without any expectations for receiving a positive gain. Due to this feature, we will call this allocation Non-essential Exporter Altruistic rule (henceforth NEA rule).

The next theorem shows that the NEA rule is coalitionally stable in the sense of the core.

Theorem 2. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game. Then, NEA rule, as defined in equation (10), belongs to the core of the game.

Following the above theorem, CE-games are balanced. It is easy to see that every subgame of CE-games is also a CE-game. Thus, CE-games are totally balanced.

As illustrated by Example 1, in situations where complementary players are absent, the NEA
rule emerges as a fair method for distributing the benefits generated by the grand coalition. Nevertheless, in the subsequent scenario involving the same number of SMEs, it becomes evident that not all exporting players see the benefits of their cooperation.

Example 2. Consider a scenario with three players N = {1, 2, 3}*. We have* Q1 = 5 , Q2 = 5, Q3 = 6, c1 = 20, c2 = 20, c3 = 35*. Let* p = 5.5, m = 11*, and* ru = 6. The coalitions' optimal profits and strategies are shown in Table 2.

In this example, players 1 and 2 are essential while player 3 is complementary. Although player
3 exports with either 1 or 2, as well as in the grand coalition, the NEA rule distributes the profit in the following way: ϕ(*N, v*) = (6.5, 6.5, 0), allocating no profit to player 3. Nevertheless, there still exists alternative allocations in the core that could give as much as 4 units of profit to player 3 (for example, consider the allocation (4.5, 4.5, 4).

To address the incentive issues of the complementary exporting players, a possible alternative to the NEA rule would be to consider distributing the benefits of the grand coalition proportionally to δi for all exporters (essential and complementary). Consider then the following proportional allocation:

$$\omega_{i}(N,v):=\left\{\begin{array}{l l}{{\frac{\delta_{i}}{\sum_{j\in R^{N}}\delta_{j}}v(N)}}&{{\mathrm{if~}i\in R^{N}}}\\ {{0}}&{{\mathrm{otherwise}}}\end{array}\right.$$
Here, all exporting players receive an allocation proportional to their δi, and therefore we will call

$$\begin{array}{c}{{}}\\ {{}}\end{array}$$
it δ-proportional rule. Since all exporting players are compensated based on the same criteria, there is a natural 'fairness' intuition associated with this solution. Unfortunately, this allocation is not necessarily in the core.

A counterexample can be observed in Example 2 where we get
ω(*N, v*) = (4.47, 4.47, 4.06).

With this allocation we have v({1, 2}) = 8.94 < 9 which violates stability condition for this coalition.

Considering the nucleolus allocation for this example, we get η(*N, v*) = (5.5, 5.5, 2).

It removes one unit from each essential player and gives it to the complementary exporting player. The nucleolus also obtains a stable allocation in the sense of the core for these games, which are balanced. However, as the number of players increases, computing the nucleolus becomes computationally challenging. Perea and Puerto (2019) proposes a heuristic approach for calculating the nucleolus, which is based on sampling the coalitions space.

Although the NEA rule is in the core and it is computationally straightforward, it does not give any extra value to the complementary players that are part of the optimal exporters in N. Thus, one can argue that the NEA rule does not provide sufficient incentives for complementary exporting players to participate in the coalition even when their help is needed to achieve the economy of scale required for export. We address this issue next by refining the NEA rule by means of compensatory policies for complementary exporting players. In the following section, we introduce two alternative allocations, easily computable, aimed at compensating complementary exporting players for their contributions to the collective export benefit.

## 8 Compensation Policies For Complementary Exporting Players

The NEA rule is altruistic towards complementary exporting players since it don't give away any margins to these players. Thus, one remains dubious about the willingness of these players to join export consortia. In what follows, we give two modifications to this allocation rule to remedy this drawback. These allocations share a portion of export margins among complementary exporting players by taxing essential players. The first allocation rule does this by charging all essential players a fixed amount. The second allocation rule, on the other hand, charges an amount proportional to the gain received by each essential player.

## 8.1 Egalitarian Essential Rate

The first approach to modify the NEA allocation rule in (10) involves charging a fixed rate from the essential SMEs in the coalition and distribute the collected amount among the complementary exporting players. Let (αi)i∈DN be a system of non-negative weights for complementary exporting players in the grand coalition. That is, αj ≥ 0 for all j ∈ DN with at least a k ∈ DN such that
αk > 0. Given ρ ≥ 0, the *egalitarian essential rate* allocation rule ψρ(*N, v*) = (ψρ
i (*N, v*))i∈N is defined as follows:

$$\psi_{i}^{\rho}(N,v)=\begin{cases}\phi_{i}(N,v)-\rho&\text{if}i\in N^{E}\\ \dfrac{\alpha_{i}}{\sum_{j\in D^{N}}\alpha_{j}}|N^{E}|\rho&\text{if}i\in D^{N}\\ 0&\text{if}i\in N\setminus R^{N}\end{cases}\tag{11}$$

The egalitarian essential rate rule charges a fix amount $\rho\geq0$ from every essential player after 
allocating gains among players according the NEA allocation rule ϕ(*N, v*).

Our next objective is to find out what values of ρ (tax rate) are affordable for the essential players so that the associated allocation ψρ(*N, v*) is within the core. To do so, we will use the excess function for coalitions under NEA rule ϕ(*N, v*). That is, for a coalition S ⊂ N, let e(S, ϕ(*N, v*)) =
�
i∈S ϕi(*N, v*) − v(S).

Note that since ϕ(N, v) ∈ Core(*N, v*) we have e(S, ϕ(*N, v*)) ≥ 0 for all S ⊆ N. We are particularly interested in the coalition ˆS ⊂ N that attains the minimum excess per number of essential players it contains, that is:

$$\hat{S}\in\mathop{\arg\min}_{S^{\leq}_{\omega}N:S^{E}\neq0}\frac{e(S,\phi(N,v))}{|S^{E}|}.\tag{12}$$
As per formulation above, finding the coalitions with minimum excess per number of essential requires searching among all sub-coalitions which, as the number of players grow, can be computationally challenging. However, as our next result shows, such sub-coalitions can only be among certain groups of coalitions. Consider Mi(*N, v*) = v(N) − v(N *\ {*i}) as the marginal contribution of player i.

Lemma 4. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game.

Given the NEA rule ϕ(N, v), we have either ˆS = N \ {i∗} for i∗ ∈ N such that Mi∗(N, v) −
Mi(N, v) ≤ ϕi∗(N, v) − ϕi(N, v) for all i ∈ N*, or* ˆS = (N \ NE) ∪ {i∗} *for* i∗ ∈ arg mini∈NE ∆i.

The first possibility for the sub-coalition with minimum excess per number of essential players is the coalition which has only one essential player less than the grand coalition. The absent player, i∗, in this case is the essential player who receives the closest allocation to his/her maximum possible allocatable gain under the original NEA rule. Note that in this case we have | ˆS| ∈ {1, n − 1}. The second possibility for the sub-coalition with minimum excess per number of essential players is the coalition which includes all non-essential players and only the essential player with the minimum full capacity export margin. Figuring out ˆS allows us to calculate the maximum fix rate that can be deducted from the essential players to be redistributed among the complementary exporting players. The following result provides a sufficient condition for the egalitarian essential rate rule to belong to the core of the game.

Theorem 3. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game.

If DN ̸= ∅*, for every* 0 ≤ ρ ≤ e( ˆS,ϕ(N,v))
| ˆSE|
the allocation rule ψρ(N, v) is in the core of the associated game.

In light of the previous result, we have an interval to select an appropriate ρ within which so that the egalitarian essential rate allocation is stable in the sense of the core. However, we can set further criteria for choosing the appropriate ρ, which more 'fairly' compensates complementary exporting players. Therefore, we establish the proportional allocation in (11) as a reference for compensation for complementary exporting players, which, despite not belonging to the core, distributes profit proportionally to the under-supply adjusted (full capacity) margin of exporting players, and in that sense treats all players in a same way. With this objective in mind, we let αi = δi for all i ∈ DN, and define

$$\rho^{E}:=\min\left\{\frac{e(\hat{S},\phi(N,v))}{|\hat{S}^{E}|},\frac{v(N)\sum_{j\in D^{N}}\delta_{j}}{|N^{E}|\sum_{j\in D^{N}}\delta_{j}}\right\}.\tag{13}$$

One can observe that in this way, if the the second expression is less than or equal to the first expres
sions, then the egalitarian essential allocation generates the same allocations for complementary exporting players as that in (11) while ensuring that the resultant allocation is in the core.

## 8.2 Proportional Essential Rate

The second approach to modify the NEA allocation rule in (10) is to tax the essential SMEs in the coalition (with a fix percentage rate) and distribute the collected amount among the complementary exporting players. Let (αi)i∈DN be a system of non-negative weights for complementary exporting players in the grand coalition. Given ρ ≥ 0, the *proportional essential rate* allocation rule φρ(*N, v*) =
(φρ
i (*N, v*))i∈N is defined as follows:

$$\varphi_{i}^{\rho}(N,v)=\begin{cases}(1-\rho)\phi_{i}(N,v)&\text{if}i\in N^{E}\\ \dfrac{\alpha_{i}}{\sum_{j\in D^{N}}\alpha_{j}}\rho v(N)&\text{if}i\in D^{N}\\ 0&\text{if}i\in N\setminus R^{N}\end{cases}$$

The proportional essential rate allocation rule charges an amount $\phi_{i}(N,v)\rho\geq0$ from every es 
sential player, after allocating gains among players according the NEA rule ϕ(*N, v*), and then redistributes the aggregated amount among the complementary exporting players according to the weights (αi)i∈DN .

Consider the ratio of the excess value under the NEA rule assigned to a coalition which contains at least an essential player, and the aggregated allocation of that coalition under the NEA rule. Among these values of all feasible sub-coalition, we highlight the sub-coalition with the minimum ratio:

$$\hat{S}=\operatorname*{arg\,min}_{S\in\hat{N},\hat{S}\neq\emptyset}\frac{e(S,\phi(N,v))}{\sum_{v\in\hat{S}}\phi_{i}(N,v)}.\tag{14}$$

The following result shows that the coalition where the ratio is minimised, $\hat{S}$, can be found amongst 
a restricted set of possible sub-coalitions.

Lemma 5. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game.

Given the NEA rule ϕ(N, v), then ˇS = N \ {i∗} where i∗ ∈ arg mini∈NE
                                                                 e(N\{i},ϕ(N,v))
                                                                �
                                                                  j∈N\{i} ϕj(N,v).

In fact, ˇS has exactly one essential player less than the grand coalition N. Thus, finding the

latter sub-coalition is computationally straightforward. Our next result indicates a range for ρ that

results in the proportional essential rate allocation rule to belong to the core of the game. Theorem 4. Let (N, Q, C, p, m) be a CE-situation, and let (N, v) be the corresponding CE-game.

If DN ̸= ∅, for every 0 ≤ ρ ≤
                                      e( ˇS,ϕ(N,v))
                                     �
                                       i∈ ˇ
                                         S ϕi(N,v) the allocation rule φρ(N, v) is in the core of the associated

game.

A similar argument to the previous subsection allows us to define a particular value for ρ such

that the proportional essential rate allocation rule would belong to the core and approximates the compensation provided by the δ-proportional rule for complementary exporting players. For all

i ∈ DN let αi = δi, and define

$$\rho^{P}:=\min\left\{\frac{e(\tilde{S},\phi(N,v))}{\sum_{i\in S}\phi_{i}(N,v)},\frac{\sum_{j\in D^{N}}\delta_{j}}{\sum_{j\in R^{N}}\delta_{j}}\right\}.\tag{15}$$

| S   | R   |
|-----|-----|
| S   |     |
| |   |     |
| (   | S   |
| \   |     |
| R   |     |
| S   |     |
| )   | v   |
| {   |     |
| 1   |     |
| }   | ∅|{ |
| 1   |     |
| }   |     |
| 0   |     |
| {   |     |
| 2   |     |
| }   |     |
| ∅|{ |     |
| 2   |     |
| }   |     |
| 0   |     |
| {   |     |
| 3   |     |
| }   | {   |
| 3   |     |
| }|∅ |     |
| 0   |     |
| {   |     |
| 4   |     |
| }   | ∅|{ |
| 4   |     |
| }   |     |
| 0   |     |
| {   |     |
| 1   | ,   |
| }   |     |
| {   |     |
| 1   | ,   |
| }|∅ |     |
| 0   |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 0   |     |
| {   |     |
| 1   | ,   |
| }   | ∅|{ |
| 1   | ,   |
| }   |     |
| 0   |     |
| {   |     |
| 2   | ,   |
| }   |     |
| {   |     |
| 2   | ,   |
| }|∅ |     |
| 30  |     |
| {   |     |
| 2   | ,   |
| }   | ∅|{ |
| 2   | ,   |
| }   |     |
| 20  |     |
| {   |     |
| 3   | ,   |
| }   | {   |
| 3   | ,   |
| }|∅ |     |
| 20  |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 139 |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 104 |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 104 |     |
| {   |     |
| 2   | ,   |
| }   | {   |
| 2   | ,   |
| }|∅ |     |
| 110 |     |
| {   |     |
| 1   | ,   |
| }   | {   |
| 1   | ,   |
| }|∅ |     |
| 169 |     |

The reader may notice that 0 ≤ ρP < 1.

One can check that when the upper bound of ρ is large enough, ρP obtains allocations for the complementary exporting players that are equal to what allocation (11) obtains for these players. We comparing our modified allocation rules through numerical experiments in the next section.

## 9 Numerical Experiments

In this section, we compare the two modified solutions proposed in the previous section to examine which provides a greater compensation for complementary exporting players. We start by considering a CE-situation with four players.

Example 3. Consider a scenario with four players N = {1, 2, 3, 4}*. We have* Q1 = 10 , Q2 = 15, Q3 = 15, Q4 = 30, c1 = 1, c2 = c3 = 25, c4 = 200*. Let* p = 6, m = 50, ru = 5 and αi = δi for all i ∈ DN. The coalitions' optimal profits and strategies are shown in Table 3.

$$\begin{array}{c|c|c|c}{{\phi(N,v)}}&{{\omega(N,v)}}&{{\psi^{\rho^{E}}(N,v)}}&{{\varphi^{\rho^{P}}(N,v)}}&{{\eta(N,v)}}\\ {{}}&{{}}&{{}}\\ {{\left(\begin{array}{c}{{52.75}}\\ {{58.125}}\\ {{58.125}}\\ {{0}}\end{array}\right)}}&{{\left(\begin{array}{c}{{35.50}}\\ {{45.60}}\\ {{45.60}}\\ {{42.20}}\end{array}\right)}}&{{\left(\begin{array}{c}{{49.65}}\\ {{55}}\\ {{55}}\\ {{9.35}}\end{array}\right)}}&{{\left(\begin{array}{c}{{49.95}}\\ {{55}}\\ {{55}}\\ {{9.05}}\end{array}\right)}}&{{\left(\begin{array}{c}{{46.5}}\\ {{52.5}}\\ {{52.5}}\\ {{17.5}}\end{array}\right)}}\end{array}$$
In this example, players 1 is extremely efficient, with a very low cost. But he does not have sufficient quantity. Players 2 and 3 are symmetric with mid levels of efficiency and quantity. These three players are essential. Player 4 has the largest quantity but he is extremely inefficient, i.e., with a high cost. Thus player 4 is complementary. Table 4 exhibits the comparison among the rules studied in this research as well as the nucleolus.

Player 4 has an extremely high cost compare to the other three players so ∆4 < 0 and as such this is a complementary player. In the end, the NEA allocation rule gives him nothing, although the δ-proportional rule gives this player as high as 42. Our allocation rules recommend a maximum of ρE = 3.12 egalitarian payment from the three essential players 1,2,3, or ρP = 0.05 of their NEA
allocation back as tax ratio to compensate player 4. This gives the player 4 a maximum of 9.35 units of gained profit.

To exhibit the burden of player 4 to the rest of the players, consider an alternative situation where an additional efficient player 5, with same quantity as player 4, Q5 = Q4, but c5 = 5. Then the optimal set of exporters does not include player 4 and the essential players have increased their gains (under NEA allocation rule) to ϕ′
1 = 59, ϕ′
2 = 65, and ϕ′
3 = 65, that is around 15% increase on average.

Example 4. Consider a scenario with four players N = {1, 2, 3, 4}*. We have* Q1 = 8 , Q2 = 9, Q3 = 54, Q4 = 37, c1 = c3 = 10, c2 = 28, c4 = 15*. Let* p = 3, m = 103, ru = 12 and αi = δi for all i ∈ DN. In this example, players 1, 3 and 4 are essential and player 2 is complementary. The non-zero values of the objective function are: v({3, 4}) = 104, v({1, 3, 4}) = 214, v({2, 3, 4}) = 211
and v({1, 2, 3, 4}) = 261*. Moreover,* ρE = 5.9788 *and* ρP = 0.0687. The comparison of the different solutions is presented in Table 5.

Example 5. Consider a scenario with four players N = {1, 2, 3, 4}*. We have* Q1 = 43 , Q2 = 12,

$$\phi(N,v)\quad\quad\quad\quad\omega(N,v)\quad\quad\quad\psi^{\rho^{E}}(N,v)\quad\quad\quad\varphi^{\rho^{P}}(N,v)\quad\quad\quad\eta(N,v)$$

$$\left(\begin{array}{c}13.95\\ 0\\ 151.42\\ 95.63\end{array}\right)\left(\begin{array}{c}18.44\\ 17.93\\ 134.10\\ 90.53\end{array}\right)\left(\begin{array}{c}7.97\\ 17.93\\ 145.44\\ 89.66\end{array}\right)\left(\begin{array}{c}12.99\\ 17.93\\ 141.01\\ 89.07\end{array}\right)\left(\begin{array}{c}25\\ 23.5\\ 106.25\\ 106.25\\ 106.25\end{array}\right)$$

      
|     | ϕ    | (    | N, v   | )   |
|-----|------|------|--------|-----|
| ω   | (    | N, v | )      | ψ   |
| ρ   |      |      |        |     |
| E   |      |      |        |     |
| (   | N, v | )    | φ      |     |
| ρ   |      |      |        |     |
| P   |      |      |        |     |
|     |      |      |        |     |
| (   | N, v | )    | η      | (   |
| 111 | .    | 78   | 99     | .   |
|    |     |     |       |    |
| 23  | .    | 33   | 26     | .   |
| 0   | 7    | .    | 24     | 7   |
| 4   | .    | 89   | 6      | .   |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |
|    |      |      |        |     |

                                                       
Q3 = 4, Q4 = 3, c1 = 9, c2 = 17, c3 = 21, c4 = 6*. Let* p = 5, m = 68.5, ru = 18 and αi = δi for all i ∈ DN. In this example players 1, 2 and 4 are essential and player 3 is complementary. The non-zero values of the objective function are: v({1, 2}) = 6, v({1, 2, 3}) = 77, v({1, 2, 4}) = 69 and v({1, 2, 3, 4}) = 140*. Moreover,* ρE = 2.4132 *and* ρP = 0.0517. The comparison of the different solutions is presented in Table 6.

Note that in example 3, the nucleolus is close to the proposed alternative solutions. However, in examples 4 and 5, the nucleolus exhibits a very different behavior, as it penalizes an essential player. Specifically, in example 5 the nucleolus punishes player 1 with more than 50% of their profit while compensating not only the complementary player (player 3) but also the rest of the essential players (players 2 and 4). In example 4, it harms the essential player 3 with more than 25% of their profit. We would also like to note that the δ-proportional rule is a core allocation for examples 4 and 5, but not for examples 2 and 3.

## 10 Conclusions

International trade presents significant opportunities for agri-food communities to generate profits.

However, for small and medium-sized enterprises (SMEs), accessing international markets can be financially prohibitive, particularly under trade policies that impose minimum quantity commitments (MQCs) on export volumes, such as licensing tariff rate quota (TRQ) mechanisms.

In our study, we aim to address this challenging context with the goal of developing optimal strategies to facilitate international market exportation for Small and Medium-sized Enterprises (SMEs). The central idea is to design collaborative approaches, such as the formation of export consortia, that enable SMEs to join forces to overcome inherent barriers in global competition. In this regard, the implementation of strategies focused on export commitment and the optimization of the agri-food supply chain will be crucial.

By fostering collaboration and synergy between SMEs, we aim to contribute to a more robust and competitive commercial ecosystem where both types of businesses can mutually thrive in the international market. Adaptability in the face of global uncertainty will be a key element in our proposals, ensuring the long-term viability of these strategies in a dynamic business environment.

This paper demonstrates how cooperative exporting among agri-food SMEs can effectively overcome the challenges posed by MQCs, thereby expanding market access to a wider array of SMEs. By formulating a class of cooperative games tailored to these scenarios, we identify a gain-sharing mechanism that ensures allocations within their respective cores, facilitating the formation of stable grand coalitions among cooperative exporting SMEs.

Our proposed allocation NEA-rule distributes the export surplus exclusively among the "essential" SME exporters—those that demonstrate sufficient cost efficiency. Consequently, less costefficient "complementary" SMEs, whose capacities are essential for meeting MQCs, do not directly benefit from collaborative exporting and must participate altruistically.

To address this issue, we suggest two modifications to our original allocation rule aimed at sharing a portion of the export surplus with complementary SMEs through taxing the essential SMEs. These modifications include an egalitarian approach, which we called Egalitarian essential rate, and a revenue-based rate approach, called Proportional essential rate. Through numerical examples, we compare the performance of these allocation mechanisms and discuss their practical implications for cooperative exporting strategies in agri-food communities.

Future research in this domain could explore several avenues to further enhance our understanding and implementation of cooperative exporting strategies among agri-food SMEs. Firstly, investigating attainable allocations through the lens of a potential-based mechanism (PMAS) could offer insights into more dynamic and adaptive gain-sharing approaches, taking into account the evolving needs and capacities of participating SMEs. Secondly, delving into detailed characterizations of the proposed solutions, including their stability, fairness, and scalability under various market conditions and policy frameworks, would provide a deeper understanding of their practical implications and limitations. Finally, applying these cooperative exporting models to real-world data from agri-food exporting companies would offer empirical validation and refinement, enabling the development of more tailored and effective strategies to promote inclusive and sustainable international trade within the agricultural sector.

## Acknowledgements

This work is part of the R+D+I project grants PID2022-137211NB-100, that were funded by MCIN/AEI/10.13039/501100011033/ and by "ERDF A way of making Europe"/EU. This research was also funded by project PROMETEO/2021/063 from the Conselleria d'Innovaci´o, Universitats, Ci`encia i Societat Digital, Generalitat Valenciana.

## References

Anily, S. and Haviv, M. (2010). Cooperation in service systems. *Operations Research*, 58(3):660–
673.
Armony, M., Roels, G., and Song, H. (2021). Pooling queues with strategic servers: The effects of
customer ownership. *Operations Research*, 69(1):13–29.
Bernstein, F., K¨ok, A. G., and Meca, A. (2015). Cooperation in assembly systems: The role of
knowledge sharing networks. *European Journal of Operational Research*, 240(1):160–171.
Bondareva, O. N. (1963).
Some applications of linear programming methods to the theory of
cooperative games. *Problemy Kibernet*, 10:119.
Boughner, D. S., de Gorter, H., and Sheldon, I. M. (2000). The economics of two-tier tariff-rate
import quotas in agriculture. *Agricultural and Resource Economics Review*, 29(1):58–69.
Bureau, J.-C., Guimbard, H., and Jean, S. (2019). Agricultural trade liberalisation in the 21st
century: has it done the business? *Journal of agricultural economics*, 70(1):3–25.
Charoenwong, B., Han, M., and Wu, J. (2023). Trade and foreign economic policy uncertainty in
supply chain networks: Who comes home? *Manufacturing & Service Operations Management*,
25(1):126–147.
Cohen, M. A. and Lee, H. L. (2020). Designing the right global supply chain network. Manufacturing
& Service Operations Management, 22(1):15–24.
Cruijssen, F., Dullaert, W., and Fleuren, H. (2007).
Horizontal cooperation in transport and
logistics: a literature review. *Transportation journal*, 46(3):22–39.
Curiel, I., Hamers, H., and Klijn, F. (2002). Sequencing games: a survey. In Chapters in game
theory: in honor of Stef Tijs, pages 27–50. Springer.
Dong, L. and Kouvelis, P. (2020). Impact of tariffs on global supply chain network configuration:
Models, predictions, and future research.
Manufacturing & Service Operations Management,
22(1):25–35.
Fan, D., Yeung, A. C., Tang, C. S., Lo, C. K., and Zhou, Y. (2022).
Global operations and
supply-chain management under the political economy.
Fang, X. and Cho, S.-H. (2014). Stability and endogenous formation of inventory transshipment
networks. *Operations Research*, 62(6):1316–1334.
Fang, X. and Cho, S.-H. (2020). Cooperative approaches to managing social responsibility in a
market with externalities. *Manufacturing & Service Operations Management*, 22(6):1215–1233.
Fiestras-Janeiro, M. G., Garc´ıa-Jurado, I., Meca, A., and Mosquera, M. (2012). Cost allocation in
inventory transportation systems. *Top*, 20:397–410.
Fiestras-Janeiro, M. G., Garc´ıa-Jurado, I., Meca, A., and Mosquera, M. A. (2011). Cooperative
game theory and inventory management. *European Journal of Operational Research*, 210(3):459–
466.
Fiestras-Janeiro, M. G., Garc´ıa-Jurado, I., Meca, A., and Mosquera, M. A. (2013). A new cost
allocation rule for inventory transportation systems. *Operations Research Letters*, 41(5):449–453.
Fiestras-Janeiro, M. G., Garc´ıa-Jurado, I., Meca, A., and Mosquera, M. A. (2014). Centralized
inventory in a farming community. *Journal of Business Economics*, 84:983–997.
Fiestras-Janeiro, M. G., Garc´ıa-Jurado, I., Meca, A., and Mosquera, M. A. (2015). Cooperation
on capacitated inventory situations with fixed holding costs. European Journal of Operational Research, 241(3):719–726.
Fliess, B. and Busquets, C. (2006). The role of trade barriers in sme internationalisation. Forte, R. and Oliveira, T. (2019). The role of export consortia in the internationalization of small
and medium enterprises: A review. *International Entrepreneurship Review*, 5(4):7.
Gervais, J.-P. and Surprenant, D. (2003).
Evaluating the trq import licensing mechanisms in
the canadian chicken industry. Canadian Journal of Agricultural Economics/Revue canadienne d'agroeconomie, 51(2):217–240.
Gonz´alez-Dıaz, J., Garcıa-Jurado, I., and Fiestras-Janeiro, M. G. (2010). An introductory course
on mathematical game theory. *Graduate studies in mathematics*, 115.
Gourdon, J., Stone, S., and van Tongeren, F. (2020). Non-tariff measures in agriculture. Guardiola, L. A., Meca, A., and Puerto, J. (2023). Allocating the surplus induced by cooperation
in distribution chains with multiple suppliers and retailers. *Journal of Mathematical Economics*, 108:102889.
Guardiola, L. A., Meca, A., and Timmer, J. (2007). Cooperation and profit allocation in distribution
chains. *Decision support systems*, 44(1):17–27.
He, S., Zhang, J., and Zhang, S. (2012).
Polymatroid optimization, submodularity, and joint
replenishment games. *Operations research*, 60(1):128–137.
Hezarkhani, B., Arisian, S., and Mansouri, A. (2023). Global agricultural supply chains under
tariff-rate quotas. *Production and Operations Management*, 32(11):3634–3649.
Hezarkhani, B., Slikker, M., and Woensel, T. V. (2021). Collaboration in transport and logistics
networks. *Network Design with Applications to Transportation and Logistics*, pages 627–662.
Hezarkhani, B. and Soˇsi´c, G. (2019). Who's afraid of strategic behavior? mechanisms for group
purchasing. *Production and Operations Management*, 28(4):933–954.
Hranaiova, J., de Gorter, H., and Falk, J. (2006). The economics of administering import quotas
with licenses-on-demand in agriculture. *American journal of agricultural economics*, 88(2):338– 350.
Hummels, D. (2007). Transportation costs and international trade in the second era of globalization.
Journal of Economic perspectives, 21(3):131–154.
Jørgensen, S. and Zaccour, G. (2014). A survey of game-theoretic models of cooperative advertising.
European journal of operational Research, 237(1):1–14.
Karsten, F., Slikker, M., and Van Houtum, G.-J. (2015). Resource pooling and cost allocation
among independent service providers. *Operations Research*, 63(2):476–488.
Lam, H. K., Ding, L., and Dong, Z. (2022). The impact of foreign competition on domestic firms'
product quality: Evidence from a quasi-natural experiment in the united states.
Journal of
Operations Management, 68(8):881–902.
Larue, B., Gervais, J.-P., and Pouliot, S. (2007). Should tariff-rate quotas mimic quotas?: Implications for trade liberalization under a supply management policy. The North American Journal of Economics and Finance, 18(3):247–261.
Liu, L., Qi, X., and Xu, Z. (2018). Simultaneous penalization and subsidization for stabilizing
grand cooperation. *Operations Research*, 66(5):1362–1375.
Lozano, S., Moreno, P., Adenso-D´ıaz, B., and Algaba, E. (2013). Cooperative game theory approach to allocating benefits of horizontal cooperation. European Journal of Operational Research, 229(2):444–452.
Meca, A. and Timmer, J. (2008). Supply chain collaboration. Kordic, V.(Ed.), Supply Chain,
Theory and Applications, pages 1–18.
Nagarajan, M. and Soˇsi´c, G. (2008). Game-theoretic analysis of cooperation among supply chain
agents: Review and extensions. *European journal of operational research*, 187(3):719–745.
Nagurney, A., Besik, D., and Dong, J. (2019a).
Tariffs and quotas in world trade: a unified
variational inequality framework. *European Journal of Operational Research*, 275(1):347–360.
Nagurney, A., Besik, D., and Li, D. (2019b). Strict quotas or tariffs? implications for product
quality and consumer welfare in differentiated product supply chains. Transportation Research Part E: Logistics and Transportation Review, 129:136–161.
Nagurney, A., Besik, D., and Nagurney, L. S. (2019c). Global supply chain networks and tariff
rate quotas: equilibrium analysis with application to agricultural products. Journal of Global
Optimization, 75:439–460.
OECD
(2023).
Agricultural
trade.
https://www.oecd.org/agriculture/topics/
agricultural-trade/ [Accessed: 2024].
Perea, F. and Puerto, J. (2019). A heuristic procedure for computing the nucleolus. Computers &
Operations Research, 112:104764.
Pisinger, D. and Toth, P. (1998). Knapsack problems. Handbook of Combinatorial Optimization:
Volume1–3, pages 299–428.
Rzeczycki, A. (2022). Supply chain decision making with use of game theory. Procedia Computer
Science, 207:3988–3997.
Schmeidler, D. (1969). The nucleolus of a characteristic function game. SIAM Journal on applied
mathematics, 17(6):1163–1170.
Shapley, L. S. (1953). A value for n-person games. In Kuhn, H. W. and Tucker, A. W., editors,
Contributions to the Theory of Games II, pages 307–317. Princeton University Press, Princeton.
Shapley, L. S. (1971). Cores of convex games. *International journal of game theory*, 1:11–26.
Shapley, L. S. et al. (1967).
On balanced sets and cores.
Naval Research Logistics Quarterly,
14(4):453–460.
Shapley, L. S. and Shubik, M. (1969). On market games. *Journal of Economic Theory*, 1(1):9–25. Skully, D. (2007). 23 tariff rate quotas. *Handbook on International Trade Policy*, page 258.
Skully, D. W. (1987). *Economics of tariff-rate quota administration*. Number 1893. US Department
of Agriculture, Economic Research Service.
Westerink-Duijzer, L. E., Schlicher, L. P. J., and Musegaas, M. (2020). Core allocations for cooperation problems in vaccination. *Production and Operations Management*, 29(7):1720–1737.

## Appendix - Proofs

Proof of Lemma 1. It is straightforward to verify above since without any restriction on mi, and non-negative deviation penalties, it is always optimal to match export quantity with the commitment level, that is, q∗
i = m∗
i . This simplifies the profit function to ∆i1qi>0 and subsequently we get the two possibilities as stated above.

Proof of Lemma 2. If Qi ≥ m, the MQC would not affect the optimal solution and, similar to the

case in the previous section, we get q∗
                                     i = m∗
                                            i = Qi if ∆i ≥ 0 and q∗
                                                                   i = m∗
                                                                         i = 0 otherwise. Thus, for

the rest of the proof we assume Qi < m.

Since Qi < m, upon exporting there will be under supply penalty. Thus the best choice of

commitment if qi > 0 is m∗
                       i = m. The profit in this case is

$$\Pi(q_{i},\underline{{{m}}})=q_{i}(p+r^{u})-c_{i}-\underline{{{m}}}r^{u}$$
The first part is increasing on qi thus maximum profit is Qi(p + rU) − ci − mru. If this value is positive, that is, δi ≥ mru, then we have q∗
i = Qi. Otherwise, we have q∗
i = m∗
i = 0.

Proof of Theorem 1. Let RS ⊆ S be the subset of players in S such as qS
i > 0 for all i ∈ RS. We assume that cooperating via the export coalition is beneficial, that is, RS ̸= ∅. By Lemma 2, we have qS
i = Qi for all i ∈ RS. We consider the cases in the statement of the theorem in sequence:
We first show that SE ⊆ RS. Since mS ≥ m the profit function at optimality is

(A) "If �
          i∈SE Qi ≥ m then mS = �
                                     i∈SE Qi, qS
                                               i = Qi for all i ∈ SE, and qS
                                                                           i = 0 for i ∈ S \ SE."

i∈RS
       ∆i

ΠS(qS, mS) =
        �

Suppose the contrary, that is, there exist no optimal solution (qS, mS) where qS
                                                                                i
                                                                                  = Qi for

all i ∈ SE.
                In this case, let j ∈ S be a player such that j ∈ SE but j /∈ RS.
                                                                                                          Consider an

alternative solution with qj = Qj , qi = qS
i for all i ∈ S *\ {*j}, and m = mS + Qj. We have
ΠS(q, m) − ΠS(qS, mS) = ∆j ≥ 0 which is a contradiction. Thus SE ⊆ RS.

Next, we show that SE = RS. Suppose SE ⊊ RS, and let j ∈ RS \ SE. Consider an alternative solution with qj = 0, qi = qS
i for all i ∈ S *\ {*j}, and m = mS − Qj. Note that *m > m*. We have
ΠS(q, m) − ΠS(qS, mS) = ∆j < 0 which is a contradiction. Thus SE = RS.

(B) "If �
i∈SE Qi *< m* then for some RS ⊆ S such that SE ⊆ RS ⊆ SP , we have mS =
We first show that SE ⊆ RS. The optimal profit in this case is

$\max\left\{\underline{m},\sum_{i\in R^{S}}Q_{i}\right\}$, $q_{i}^{S}=Q_{i}$ for all $i\in R^{S}$, and $q_{i}^{S}=0$ for $i\in S\setminus R^{S}$."

We first show that $S^{E}\subseteq R^{S}$. The optimal profit in this case is

$$\Pi^{S}(q^{S},m^{S})=\sum_{i\in R^{S}}\left[Q_{i}(p+r^{u})-c_{i}\right]-m^{S}r^{u}.$$
Suppose the contrary, that is, there exist no optimal solution (qS, mS) where qS
i = Qi for all i ∈ RS.

In this case, let j ∈ S be a player such that j ∈ SE but *j /*∈ RS. There are different possibilities:

1. Qj *< m*S −�
RS Qi: Consider an alternative solution with qj = Qj , qi = qS
i for all i ∈ S\{j},
and m = mS = m. We have ΠS(q, m) − ΠS(qS, mS) = δj ≥ 0 which is a contradiction.
2. Qj ≥ mS −�
RS Qi: Consider an alternative solution with qj = Qj, qi = qS
i for all i ∈ S \{j},
which is a contradiction.
and m = �
i∈RS∪{j} Qi. We have ΠS(q, m) − ΠS(qS, mS) = ∆j +
�
m − �
i∈RS Qi
�
ru ≥ 0
Thus SE ⊆ RS.

Next, we show that there is no j ∈ RS such that j ∈ S \ SP . Suppose the contrary, that is, let j ∈ S \ SP and qS
j = Qj. We consider two cases again:

1. �
i∈RS Qi ≤ m: Consider an alternative solution with qj = 0 , qi = qS
i for all i ∈ S *\ {*j}, and
m = m. We have ΠS(q, m) − ΠS(qS, mS) = −δj ≥ 0 which is a contradiction.
2. �
i∈RS\{j} Qi ≥ m: Consider an alternative solution with qj = 0 , qi = qS
i for all i ∈ S *\ {*j},
and m = �
i∈RS\{j} Qi. We have ΠS(q, m)−ΠS(qS, mS) = −∆j ≥ 0 which is a contradiction.
3. �
i∈RS\{j} Qi *< m* and �
i∈RS Qi *> m*:
Consider an alternative solution with qj = 0,
qi = qS
i
for all i ∈ S *\ {*j}, and m = m.
We have ΠS(q, m) − ΠS(qS, mS) = −∆j −
�
m − �
i∈RS\{j} Qi
�
ru ≥ 0 which is a contradiction.
Thus SE ⊆ RS ⊆ SP .

Proof of Corollary 1. Considering Theorem 1, in case (A) we have Π(qS, mS) = �
i∈SE ∆i. In case

(B) we have Π(qS, mS) = �
                          i∈SE ∆i +�
                                     i∈RS\SE ∆i −
                                                 �
                                                  m − �
                                                         i∈RS Qi
                                                               �+ ru. Note that by definition

of complementary players, for any i ∈ RS \ SE we have ∆i < 0 which obtains Π(qS, mS) ≤
�
  i∈SE ∆i.

by Theorem 1 (B) that SE ⊆ RS. Consider ΠS(SE) as the profit function for coalition S in the Proof of Proposition 1. Take S ∈ N and suppose suppose that �
i∈SE Qi *< m*. If RS ̸= ∅, we know solution in which only the essential players export all of their capacity. Thus we can write

$$\Pi^{S}(S^{E})+G^{S}(D)=\sum_{i\in S^{E}}\Delta_{i}-\left(\underline{m}-\sum_{i\in S^{E}}Q_{i}\right)^{+}r^{u}+\sum_{i\in D}\Delta_{i}+\min\left\{\underline{m}-\sum_{i\in S^{E}}Q_{i}\sum_{i\in D}Q_{i}\right\}r^{u}$$ $$=\sum_{i\in S^{E}}\Delta_{i}+\sum_{i\in D}\Delta_{i}-\left(\underline{m}-\sum_{i\in S^{E}}Q_{i}\right)r^{u}+\min\left\{\underline{m}-\sum_{i\in S^{E}}Q_{i}\sum_{i\in D}Q_{i}\right\}r^{u}$$ $$=\sum_{i\in S^{E}\cup D}\Delta_{i}-\left(\underline{m}\sum_{i\in S^{E}\cup D}Q_{i}\right)^{+}r^{u}=\Pi^{S}(S^{E}\cup D)$$

Hence, finding optimal $R^{S}$ boils down to finding optimal $D$ for $G^{S}$; that is, $D^{S}\in\arg\max_{D\subseteq S^{C}}G^{S}(D)$.

Proof of Proposition 2. Consider DS such that maxD⊆SC{GS(D)} = GS(DS). Assume that DS in non empty. Suppose DS ̸= ∅ and let M = m − �
i∈SE Qi.

exceed M. This can be formulated through the following integer program:

   Suppose an oracle indicates that at optimality, �
                                                     i∈DS Qi ≤ M.
                                                                     Thus we have GS(DS) =
�
  i∈DS δi. In that case we can search among all groups of players whose total quantities does not

$$\operatorname*{max}\sum_{i\in S^{C}}x_{i}\delta_{i}$$ s.t.$\sum_{i\in S^{C}}x_{i}Q_{i}<M$

$$x_{i}\in\{0,1\}\qquad\forall i\in S^{C}$$
Given the optimal solution x∗ we have DS = {i : x∗
i = 1}. However, the program above is the
{0, 1}-Knapsack Problem which is NP-hard (Pisinger and Toth, 1998).

Proof of Lemma 3. (i) From Proposition 1 we can write

$$D^{N}\in\operatorname*{arg\,max}_{D^{\leq N^{c}}_{\leq}}\sum_{i\in D}\Delta_{i}+\min\left\{\underline{m}-\sum_{i\in N^{c}}Q_{i},\sum_{i\in D}Q_{i}\right\}r^{u}.$$

Thus $G^{N}(D^{N})=\sum_{i\in D^{N}}\Delta_{i}+\min\left\{\underline{m}-\sum_{i\in N^{c}}Q_{i},\sum_{i\in D^{N}}Q_{i}\right\}r^{u}.$ In the same manner we have

$$D^{S}\in\operatorname*{arg\,max}_{D^{\leq N^{c}}_{\leq}}\sum_{i\in D}\Delta_{i}+\min\left\{\underline{m}-\sum_{i\in S^{c}}Q_{i},\sum_{i\in D}Q_{i}\right\}r^{u}.$$
which is equivalent to

$$|S^{E}|(\sum_{i\in S^{E}}\Delta_{i}+\Delta_{j})-(|S^{E}|+1)\sum_{i\in S^{E}}\Delta_{i}\leq0$$
That is

$$|S^{E}|\Delta_{j}-\sum_{i\in S^{E}}\Delta_{i}\leq0$$
that is

$$\Delta_{j}\leq\frac{\sum_{i\in S^{E}}\Delta_{i}}{|S^{E}|}$$
- If RS∪{j} ̸= ∅, we have

$$\frac{e(S\cup\{j\},\phi(N,v))}{|S^{E}|+1}-\frac{e(S,\phi(N,v))}{|S^{E}|}=\frac{\frac{\sum_{i\in\mathcal{S}^{E}}\Delta_{i}+\Delta_{j}}{|S^{E}|+1}}{|S^{E}|+1}v(N)-\frac{v(S\cup\{j\})}{|S^{E}|+1}-\frac{\frac{\sum_{i\in\mathcal{S}^{E}}\Delta_{i}}{|S^{E}|}}{|S^{E}|}v(N)\leq0$$
We have

$|S^{E}|(\sum_{i\in S^{E}}\Delta_{i}+\Delta_{j})-|S^{E}|v(S\cup\{j\})-(|S^{E}|+1)\sum_{i\in S^{E}}\Delta_{i}\leq0$
That is

$$\Delta_{j}-v(S\cup\{j\})\leq\frac{\sum_{i\in S^{E}}\Delta_{i}}{|S^{E}|}$$

[Case II: $R^{S}\neq\emptyset$] In the next step, we show that there exists no $j\in N^{E}$, $j\notin\hat{S}$, such that $\hat{S}\cup\{j\}\subset N$. To see this, note that from proof of Theorem 2 we know that when $R^{S}\neq\emptyset$, then

$$\sum_{i\in S}\phi_{i}(N,v)-v(S)=-\frac{\sum_{i\in S^{E}}\Delta_{i}}{\sum_{j\in N^{E}}\Delta_{j}}\left[\left(\underline{m}-\sum_{i\in R^{N}}Q_{i}\right)^{+}r^{u}-\sum_{j\in D^{N}}\Delta_{j}\right]$$ $$+\left(\underline{m}-\sum_{i\in R^{S}}Q_{i}\right)^{+}r^{u}-\sum_{i\in R^{S}\setminus S^{E}}\Delta_{i}$$
property (ii) in Lemma 3, the bottom part also decreases when more essential players are included.

The first part decreases as more essential players are included (since $\sum_{i\in S^{K}}\Delta_{i}$ increases). By property (ii) in Lemma 3, the bottom part also decreases when more essential players are included.

i∈ ˆS∪{j} ϕi(*N, v*)−v( ˆS ∪{j}) and subsequently, e( ˆS ∪{j})/(| ˆSE|+
1) *< e*( ˆS)/| ˆSE|. Thus, if R ˆS ̸= ∅, there exists no j ∈ N, *j /*∈ ˆS, such that ˆS ∪ {j} ⊂ N. In this case Hence, �
i∈ ˆS ϕi(*N, v*)−v( ˆS) ≥ �
we have

$$\hat{S}\in\operatorname*{arg\,min}_{i\in N:\mathbb{R}^{N}\setminus\{i\}\neq\emptyset}\frac{e(N\setminus\{i\},\phi(N,v))}{|(N\setminus\{i\})^{E}|}$$

for $i^{*}\in\operatorname*{arg\,min}_{i\in N}\sum_{j\in N\setminus\{i\}}\phi_{j}(N,v)-v(N\setminus\{i\})$. Thus for all $i\in N$ we have

$$\sum_{j\in N\setminus\{i^{*}\}}\phi_{j}(N,v)-v(N\setminus\{i^{*}\})\leq\sum_{j\in N\setminus\{i\}}\phi_{j}(N,v)-v(N\setminus\{i\})$$
that is

$$v(N\setminus\{i\})+\phi_{i}(N,v)\leq v(N\setminus\{i^{*}\})+\phi_{i^{*}}(N,v)$$
that is

$v(N)-v(N\setminus\{i\})-\phi_{i}(N,v)\geq v(N)-v(N\setminus\{i^{*}\})-\phi_{i^{*}}(N,v)$
This can be written in terms of marginal contributions, that is, Mi∗(N, v)−Mi(N, v) ≤ ϕi∗(N, v)−
ϕi(*N, v*) for all i ∈ N.

In order to find ˆS we proceed as follows: We start with ˆS = N \ NE and add j∗ = minj∈NE ∆j.

If R ˆS ̸= ∅, then by part II above we have to find the minimizes among the sets N *\ {*i}. Otherwise, if R ˆS = ∅, then ˆS can be the minimizes. All other subsets does not need consideration because if we add more essential players, the value e(S,ϕ(N,v))
|SE|
can only be decreased if RS ̸= ∅, at this point, adding more essential players by step II make the value even smaller which brings us back to the case of N *\ {*i}.

(1) Find j∗ = minj∈NE ∆j and let S = {j∗}∪N\NE. (2) Find i∗ ∈ arg mini⊂N:RN\{i}̸=∅
e(N\{i},ϕ(N,v))
|(N\{i})E|
.

(3) If e(S, ϕ(*N, v*)) < e(S′,ˆϕ)
|S′| , then ˆS = {j∗} ∪ N \ NE, otherwise, ˆS = N *\ {*i∗}.

Proof of Theorem 3. The allocation ψρ(*N, v*) is evidently efficient. Take S ⊊ N, if SE = ∅ it is

$\sum_{i\in SE}\phi_i(N,v)-v(S)$ for all $S\subset N$
i∈SE ϕi(N,v)−v(S)
|SE|

trivial that $\sum_{i\in S}\psi_{i}^{\rho}(N,v)\geq0=v(S).$ Otherwise, if the allocation is in the core, we must have $\sum_{i\in S}\psi_{i}^{\rho}(N,v)\geq\sum_{i\in S^{E}}\phi_{i}(N,v)-|S^{E}|\rho\geq v(S)$. That is $\rho\leq\frac{\sum_{i\in S^{E}}\phi_{i}(N,v)-v(S)}{|S^{E}|}$ for all $S\subset N$ which require $\rho\leq\min_{S\subset N\leq S^{E}\neq\emptyset}\left\{\frac{\sum_{i\in S^{E}}\phi_{i}(N,v)-v(S)}{|S^{E}|}\right\}$.

which require ρ ≤ minS⊊N:SE̸=∅
� �
�
.

Proof of Lemma 5. The maximizer of r(S, ϕ(*N, v*)) occurs when all non-essential players are included. We now examine adding more essential players. Let S ⊂ N and suppose j ∈ NE such that j /∈ S.

[Case 1] RS ̸= ∅: In order to have r(S, ϕ(N, v)) ≥ r(S ∪ {j}, ϕ(*N, v*)) we have

v(S *∪ {*j}) � SE ∆i + ∆j ≥ v(S) � SE ∆i
{j}) − v(S) = ∆j + (yS − yS∪{j})ru ≥ ∆j, thus the inequality holds and adding more essential

That is $[v(S\cup\{j\})-v(S)]\sum_{S^{E}}\Delta_{i}\geq\Delta_{j}v(S)$. We have $\sum_{i\in S^{E}}\Delta_{i}\geq v(S)$. Also, we have $v(S\cup\{j\})-v(S)=\Delta_{j}+(y^{S}-y^{S\cup\{j\}})^{n_{X}}\geq\Delta_{j}$, thus the inequality holds and adding more essential 
players will increase the value of r(S, ϕ(*N, v*)).

[Case 2] RS = ∅: If RS∪{j} = ∅, we have r(S, ϕ(*N, v*)) = r(S ∪ {j}, ϕ(*N, v*)). Suppose RS∪{j} ̸= ∅.

In this case we have r(S, ϕ(*N, v*)) = 0, and r(S ∪ {j}, ϕ(*N, v*)) > 0 which completes the proof.

Proof of Theorem 4. The allocation φρ(*N, v*) is evidently efficient. Take S ⊊ N, if SE = ∅ it is i∈SE ϕi(N,v) for i∈SE ϕi(N,v) =
e(S,ϕ(N,v))
�

trivial that �
               i∈S φρ
                    i (N, v) ≥ 0 = v(S). Otherwise, if the allocation is in the core, we must have
�
  i∈S φρ
       i (N, v) ≥ (1 − ρ) �
                             i∈SE ϕi(N, v) ≥ v(S). That is ρ ≤ 1 −
                                                                           v(S)
                                                                       �

i∈SE ϕi(N,v)
                  �
                     .

all S ⊊ N with SE ̸= ∅, which require ρ ≤ minS⊊N:SE̸=∅
                                                                      �
                                                                          e(S,ϕ(N,v))
                                                                        �

