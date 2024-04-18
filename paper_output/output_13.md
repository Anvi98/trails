# Transmission Benefits And Cost Allocation Under Ambiguity

Han Shu∗1 and Jacob Mays†2
1Systems Engineering, Cornell University, Ithaca, NY 14853
2Civil and Environmental Engineering, Cornell University, Ithaca, NY 14853
March 25, 2024

## Abstract

Disputes over cost allocation can present a significant barrier to investment in shared infrastructure.

While it may be desirable to allocate cost in a way that corresponds to expected benefits, investments in long-lived projects are made under conditions of substantial uncertainty. In the context of electricity transmission, uncertainty combined with the inherent complexity of power systems analysis prevents the calculation of an estimated distribution of benefits that is agreeable to all participants. To analyze aspects of the cost allocation problem, we construct a model for transmission and generation expansion planning under uncertainty, enabling the identification of transmission investments as well as the calculation of benefits for users of the network. Numerical tests confirm the potential for realized benefits at the participant level to differ significantly from ex ante estimates. Based on the model and numerical tests we discuss several issues, including 1) establishing a valid counterfactual against which to measure benefits, 2) allocating cost to new and incumbent generators vs. solely allocating to loads, 3) calculating benefits at the portfolio vs. the individual project level, 4) identifying losers in a surplus-enhancing transmission expansion, and 5) quantifying the divergence between cost allocation decisions made ex ante and benefits realized ex post.

Keywords: Electricity markets, transmission planning, cost allocation, uncertainty

## 1 Introduction

A wealth of recent research finds that large-scale expansion of regional and interregional transmission infrastructure in the U.S. would bring economic, reliability, and environmental benefits (MacDonald et al., 2016; Acevedo et al., 2021; Brown and Botterud, 2021). Planned additions to transmission, however, currently fall well short of the level deemed beneficial in models, with studies of deeply decarbonized U.S. systems projecting a need to double or even triple transfer capacity in the coming decades (Denholm et al., 2022; Jenkins et al., 2021). One of the major challenges holding up investment is cost allocation: since many stakeholders are likely to benefit from expanded transmission infrastructure, it is difficult to come to a consensus on how to divide project costs among them. While this issue is common to many types of shared infrastructure projects (see, e.g., Hamilton et al. (2022)), it may be particularly acute in the case of meshed electricity networks due to the potential for a change in one element to affect power flows across the entire system.

An underlying principle for cost allocation, codified by the Federal Energy Regulatory Commission (FERC)
in Order 1000 (Federal Energy Regulatory Commission, 2011), is that transmission costs should be allocated
"in a manner that is at least roughly commensurate with estimated benefits." In principle, sufficiently detailed planning models could be used both to establish the net social benefits of a project and to estimate a distribution of those benefits among users, and Hogan (2018) argues that these models would be the best available basis for determining a reasonable cost allocation. At the same time, both our information and our models fall well short of what would be needed for a precise computation, leading others to question the approach (Bushnell and Wolak, 2017). Judge Richard Cudahy of the U.S. Court of Appeals, dissenting in a case connected to Order 1000, articulates the opposing view as follows: "The majority has expressed a need for more precise numbers about benefits, burdens and a variety of other aspects. Now it has enhanced that need by suggesting the use of costbenefit analysis (a method, some think, of dressing up dubious numbers to reach more impressive solutions). I
will say preliminarily that I think the majority is under the impression that somehow there is a mathematical solution to this problem, and I think that this is a complete illusion. Despite the frequency with which costbenefit analysis is used, it does not resolve the difficulty of accurately or meaningfully measuring the costs and benefits involved with these grid strengthening projects. Cost allocation, particularly at these extraordinarily high voltages, is far from a precise science, and there are no mathematical solutions to determining benefits region by region or subregion by subregion" (United States Court of Appeals, 2014). This skepticism has perhaps been validated by the emergence since Order 1000 of a wide range of cost allocation methods that have all been determined to meet the "roughly commensurate" threshold, leading to inconsistent treatment of similar projects based on the process by which they were approved. Ongoing disputes led FERC to reopen the issue of cost allocation in a 2022 Notice of Proposed Rulemaking (Federal Energy Regulatory Commission, 2022).

This paper addresses several questions connected to the use of planning models in identifying beneficiaries of transmission expansion, calculating their benefits, and allocating cost in a manner consistent with the
"beneficiaries pay" standard.

Despite the challenges, Adamson (2018) reflects that "In the absence of an economically and politically acceptable formula, a direct benefits modeling approach as advocated by Hogan may prove the only workable solution." The Organization of MISO States (OMS), which includes regulators from a politically diverse set of states in the Midcontinent Independent System Operator (MISO) region, largely endorses the approach in its Statement of Principles for cost allocation (Organization of MISO States, 2021). In this context, the paper considers both how existing methods can create conflict by ignoring modeled benefits as well as the factors that may prevent a "direct benefits modeling" approach from being workable.

At least three categories of issues affect the computation of benefits and the translation of modeled benefits to a mutually agreeable cost allocation. The first category relates to the models themselves. Transmission planners use a variety of software tools to inform planning, which can be broadly split into 1) security analysis tools, involving detailed power flow models but no economic criteria, 2) production cost tools, which simulate market outcomes with a fixed resource mix, 3) expansion planning tools, which optimize the addition of new generation and transmission resources, and 4) resource adequacy tools, which evaluate the reliability provided by a given resource mix given simulated weather and outage scenarios. In principle, socially optimal transmission decisions could be given by an expansion planning model (number 3 above) that incorporated production cost simulations (2) on a number of scenarios comparable to that used in resource adequacy analysis (4) and including fully specified power flow constraints (1), while also considering the strategic behavior of market participants. The intractability of such a model means that benefit calculations must be performed on separate tools that are simplified along different dimensions, leading to the potential for benefits to be either omitted or duplicated. The second category relates to explicit disagreements on the value of particular benefits. While economic outcomes have a shared measure, benefits related to reliability and public policy are more difficult to quantify. In particular, different jurisdictions in the same regional market often assign different values to carbon reduction and air pollution mitigation. Additionally, some jurisdictions within a market may give more weight to producers of electricity (e.g., to support job creation), while others prioritize minimizing cost to consumers. The third category relates to uncertainty in the input parameters required for planning models (e.g., future demand growth and technology improvements). Even if the benefits could be quantified in a straightforward way, the significant uncertainty inherent to the system means that the ex ante estimates of expected benefits could be very different from the actual benefits seen ex post. Since participants are unlikely to agree on the probability of potential future scenarios, and may even benefit from strategically misrepresenting their views on those probabilities, they are unlikely to agree on estimated benefits.

We primarily address the first and third of these issues, leaving a more comprehensive discussion of the second to future work.

Existing model-based approaches for cost allocation can be divided between those assessing benefits based on changes in power flows (Galiana et al., 2003; Abou El Ela and El-Sehiemy, 2009;
Yang et al., 2015; Avar and Shiekh-El-Eslami, 2022) or in prices (Roustaei et al., 2014; Banez-Chicharro et al., 2017a,b; Kristiansen et al., 2018; Hogan, 2018; O'Neill, 2020). While physical approaches are sometimes used in practice, and it is possible that physical usage correlates with economic benefits, the connection is not clear and we take the more direct economic approach. The economics-based models can be further divided between those computing benefits directly (Roustaei et al., 2014; Hogan, 2018; O'Neill, 2020) and those employing concepts from cooperative game theory to address the bargaining power of different participants (Banez-Chicharro et al., 2017a,b; Kristiansen et al., 2018). Conceding the salience of bargaining power, we pursue the former approach due to its clearer connection to the "beneficiaries pay" principle. Among the models analyzed, none explicitly include uncertainty and only Kristiansen et al. (2018) includes recourse decisions in the form of generation investment. Along these lines, we extend the approach sketched on simple examples in O'Neill (2020) to a stochastic program co-optimizing the expansion of transmission and generation over a long time horizon. While such models have been considered by many researchers (Wogrin et al., 2021; Mu˜noz et al., 2014; Mu˜noz and Watson, 2015; Newlun et al., 2021), the primary focus in the literature has been identifying high-quality planning solutions rather than investigating the implications for cost allocation. Using our model, we establish beneficiaries and calculate benefits under many possible realizations of uncertainty, providing a more comprehensive understanding of the implications of network expansion for all involved parties. While we do not explicitly model the effect that cost allocation decisions may have on the network expansion decisions themselves, as in Bravo et al. (2016), these potential consequences are a theme throughout the discussion.

Through theoretical analysis and a numerical study on a stylized version of the Electric Reliability Council of Texas (ERCOT) system, we discuss five issues:

1. How to construct a valid counterfactual against which to measure benefits of a transmission investment.
Here, our primary argument is that at a minimum models must include the different generation investments likely to arise in response to different transmission expansion decisions.
2. When cost should be allocated to generators. While current practice in U.S. systems typically allocates
cost to new interconnecting generators but then excludes them from subsequent cost allocation, we conclude that a direct benefits modeling approach would instead allow new generators to connect without cost but then allocate cost to them throughout their life.
3. Whether to allocate costs on a project-by-project basis or as a portfolio. In the numerical study, allocation
at the project level implies that positive cost is allocated to participants with negative net benefits overall; on this basis, we find that portfolio-based allocation is more consistent with the "beneficiaries pay" principle.
4. The potential to compensate market participants who see negative expected benefits from expansion
decisions. Here we suggest that the surplus gained from transmission expansion could in principle be
used to compensate participants who see negative net benefits, potentially reducing conflicts.
5. The potential that participant-level benefits realized ex post will be significantly out of alignment with ex
ante estimates. Again with the intent of reducing conflicts, we suggest the possibility of defining financial contracts that would effectively reallocate cost ex post to market participants based on realized benefits.
While the first three are topics of active debate among regulators and thus have near-term policy implications, the last two raise issues for longer-term consideration.

## 2 Stochastic Expansion Planning

As a basis for analyzing the cost allocation problem, we construct a two-stage stochastic program optimizing expansion of generation and transmission over an extended horizon given an agreed-upon set of scenarios. Capacity expansion can be posed either as a social planning problem (De La Torre et al., 2008; Newlun et al.,
2021) or as a multi-agent game in a competitive market setting (Sauma and Oren, 2006; Wogrin et al., 2021). Given the complexity of modeling strategic behavior, system operators at present rely on more straightforward optimization formulations (Lau and Hobbs, 2021). We adopt the same approach, noting that because expansion of transmission tends to weaken the ability of generators to exercise local market power (Wolak, 2020), inclusion of strategic considerations in our model would likely shift our estimates of the distribution of benefits away from generators toward consumers. The first stage of the stochastic program includes decisions for the present year, while the second stage includes decisions to be made in several subsequent years. While the analysis could also be extended to a multistage setting with each year corresponding to a stage, we use a two-stage approximation to ensure scalability in the numerical study.

The problem is formulated as a mixed-integer programming (MIP) model with transmission line investment decisions as binary variables and generation investment decisions as continuous. Binary variables are needed to represent a key feature of transmission investments, namely, significant economies of scale. Further, it is typically impossible to build a transmission facility with a rating that exactly matches the need, as equipment is available only in a limited number of standardized voltage and power ratings. Transmission investments in the model can be selected from defined levels of expansion with costs reflecting economies of scale. For generation investments, we assume perfect competition and linear costs. These assumptions ensure that, conditional on the transmission network decisions, nodal electricity prices support a resource mix that maximizes long-term social welfare.

Rather than the development of the planning model itself, the primary focus of this study is the translation of the planning model results to cost allocation determinations. Many debates in transmission planning concern the selection of scenarios and benefit–cost thresholds used to justify the investment, as well as the subjective valuation of non-quantified benefits (Hogan, 2018). We set aside these issues, as it is sufficient for the discussion to have a planning tool that recommends transmission investments with positive expected net benefits in sample. We assume that a stakeholder process is able to construct scenarios and associated probabilities for use in the model, but do not assume that these scenarios are exhaustive, that the selected probabilities are accurate, or that the chosen scenarios and probabilities match the beliefs of individual market participants.

## 2.1 Notation

Sets:
y/Y: time index (years) n/N: nodes in a scenario tree
b/B (B′): buses (without reference bus)

t/T : time blocks

l/L: lines g/G: all generators
g/GR *⊆ G*: renewable generators
g/GT *⊆ G*: thermal generators
q/Q: transmission capacity increment options
i/I: power balance penalty curve segments
Parameters:
ζδ(n) (ζy): discount factor of node n (in time index y)

CINV
n,g : annualized generation investment cost of generation technology g in node n per unit capacity
($/MW)
CINV
l,q : annualized transmission investment cost of line l for expansion type q ($)
CFIX
g
: per unit fixed operation and maintenance cost of generation technology g ($/MW-yr)
CVOM
g
: per unit variable operation and maintenance cost of generation technology g ($/MWh)
CEN
n,g: per unit production fuel cost of generation technology g in node n ($/MWh)
γPB
i
: penalty value of power balance violation in segment i ($/MWh)
γLINE: penalty value of transmission line violation ($/MWh)
γLOAD: per unit benefit for serving load ($/MWh)
Tt: duration of time block t (h)
CA*b,g,t*: capacity availability of generation technology g located at bus b at time t RPSn: renewable portfolio standard in node n (%) D*n,b,t*: demand at bus b in time block t in node n
∆Lq: transmission capacity increment q SFl,b: shift factor matrix indexed by l ∈ L, b ∈ B′
ϕn: the probability of node n Zi: maximum MW violation of power balance constraint for segment i Variables:

ccap
n : the capital cost in node n ($)
cop
n : the operation cost in node n ($)
G*n,b,g*: total cumulative generation capacity of generation g at bus b in node n (MW)
∆G*n,b,g*: generation investment in generation technology g at bus b in node n (MW)
∆G*n,b,g*: generation retirement of existing generation g at bus b in node n (MW)
Ln,l: total cumulative transmission capacity of line l in node n (MW)
w*n,l,q*: binary variable to decide transmission increment q in line l in node n (MW)
p*n,b,g,t*: generation dispatch of generation technology g at bus b at time t in node n (MW)
z*n,b,t,i*: load curtailment segment i at bus b at time t in node n (MW)
NI*n,b,t*: power net injection at bus b in node n at time t (MW) sl*n,l,t*: slack variable for power flow on line l in node n at time t (MW)
Dual Variables:

π*n,b,t*: locational marginal price (LMP) at time block t at bus b in node n ($/MWh)
θ*n,b,g,t*: marginal value of a unit of generation technology g *∈ G* at time t ($/MWh)
νn: unit price for contributing to the renewable portfolio standard in node n ($/MWh)
Outputs:

Uload
b
: the aggregated load surplus at bus b
Ugen
b,g : the per unit generation surplus of generation technology g at bus b
rload
b
: cost allocation ratio of the transmission expansion to bus b (%)
rgen
b,g : cost allocation ratio of the transmission expansion to existing generation g at bus b (%)

## 2.2 Formulation

We employ a scenario tree with nodes n *∈ N* to represent the investment trajectory for the two-stage stochastic program. Each node represents a possible state of the world, associated with a set of data. The root node n = 0 in the first stage represents the current state of the world. The unique predecessor of any node n ̸= 0 is denoted as n− and the set of predecessors of node n on the path from n to the root node is denoted as P(n). The depth δ(n) of node n is the number of nodes on the path to node 0, with δ(0) = 1. The depth δ(n)
of node n also corresponds to a time index y *∈ Y*. We use ϕn to represent the probability that the path taken n∈N :δ(n)=y ϕn = 1 ∀y *∈ Y*. A visual representation of such a through the scenario tree includes node n, with �
scenario tree with Y = {1, 2, 3, 4} and 7 scenarios is drawn in Figure 1. As indicated by the dashed lines, nodes at depth 2 and 3 have a unique successor, reflecting the two-stage simplification previously mentioned. This tree structure mimics the scenario-based planning performed by many system operators, but forces convergence to a single decision in the present year. The focus of the cost allocation discussion will be on transmission investments made in the present year.

In each node n, the capital cost includes the transmission and generation investment costs incurred due to the cumulative investment decisions made on the path from node n to the root node, given by

$$c_{n}^{\rm cap}=\sum_{n^{\prime}\in\mathcal{P}(n)}\sum_{l\in\mathcal{L}}\sum_{g\in\mathcal{Q}}C_{l,g}^{\rm HV}w_{n^{\prime},l,g}+\sum_{n^{\prime}\in\mathcal{P}(n)}\sum_{b\in\mathcal{B}}\sum_{g\in\mathcal{G}}C_{n^{\prime},g}^{\rm HV}\Delta G_{n^{\prime},b,g}.\tag{1}$$
In other words, investments result in ongoing capital costs throughout the years are covered by the model. This formulation reflects the fact that resources built in the earlier nodes of the model will have completed a larger fraction of their useful lives by the end of the scenario tree.

At node n, the operating cost is

$$c_{n}^{\rm op}=\sum_{b\in\mathcal{B}}\sum_{g\in G}C_{g}^{\rm BX}G_{n,b,g}+\sum_{b\in\mathcal{B}}\sum_{g\in G}\sum_{t\in T}C_{g}^{\rm VOM}T_{t}p_{n,b,g,t}+\sum_{b\in\mathcal{B}}\sum_{t\in T}\sum_{g\in G}C_{n,g}^{\rm EN}T_{t}p_{n,b,g,t}\tag{2}$$ $$+\sum_{t\in T}\sum_{t\in\mathcal{I}}\sum_{t\in\mathcal{B}}T_{t}{}^{\rm np}z_{n,b,t}+\sum_{t\in\mathcal{I}}\sum_{t\in\mathcal{L}}T_{t}\gamma^{\rm LNE}sn_{n,l,t},$$
where the first two terms are the ongoing fixed and variable operation and maintenance costs of generation, the third term is the fuel cost, and the last two terms are penalties for curtailed load and for transmission constraint violations.

The system planner seeks to maximize the net present value of expected benefits over the assumed scenario tree. The model is formulated as follows:

$$\max\sum_{u\in\mathcal{N}}\phi_{u}\zeta_{\phi(u)}\left(\sum_{t\in\mathcal{T}}\sum_{b\in\mathcal{B}}T_{t}\gamma_{b}{}^{\mathrm{LAND}}D_{u,b,t}-c_{u}^{op}-c_{u}^{op}\right)$$ (3a) s.t. $$L_{u,l}=L_{o,l}+\sum_{u^{\prime}\in\mathcal{V}(\mathcal{V}_{l},\phi_{u})\in\mathcal{W}}w_{u^{\prime},l,u}\Delta L_{q}\quad\forall n\in\mathcal{N}\backslash0,l\in\mathcal{L}\tag{3b}$$ $$G_{n,b,g}=G_{0,h,g}+\sum_{u^{\prime}\in\mathcal{V}_{l}}\Delta G_{n^{\prime},h,g}-\sum_{u^{\prime}\in\mathcal{V}(\mathcal{V}_{l})}\Delta G_{n^{\prime},h,g}\quad\forall n\in\mathcal{N},b\in\mathcal{B},g\in\mathcal{G}$$ (3c) $$(\phi_{u}\zeta_{\phi(u)}T_{t}\theta_{n,h,g}):p_{n,h,g,t}\leq CA_{h,g,t}G_{n,h,g}\quad\forall n\in\mathcal{N},b\in\mathcal{B},g\in\mathcal{G},t\in\mathcal{T}\tag{3d}$$ t∈T t∈T b∈B b∈B TtDn,b,t ∀n ∈ N (3e)
(ϕnζδ(n)νn) :
�

� g∈GR Ttpn,b,g,t ≥ RPSn � � � i∈I zn,b,t,i − Dn,b,t ∀n ∈ N, b ∈ B, t ∈ T (3f) g∈G p*n,b,g,t* + �
(ϕnζδ(n)Ttπ*n,b,t*) :
NI*n,b,t* =
�

b∈B′ SFl,bNIn,b,t ≤ (Ln,l + sl*n,l,t*) ∀n ∈ N, l ∈ L, t ∈ T (3g) −(Ln,l + sln,l,t) ≤ � b∈B NI*n,b,t* = 0 ∀n ∈ N, t ∈ T (3h) � ∆Gn,b,g, ∆Gn,b,g, p*n,b,g,t* ≥ 0 ∀n ∈ N, b ∈ B, g ∈ G, t ∈ T (3i) b∈B zn,b,t,i ≤ Zi ∀n ∈ N, t ∈ T , i ∈ I (3k) z*n,b,t,i* ≥ 0 ∀n ∈ N, b ∈ B, t ∈ T , i ∈ I (3j) � sl*n,l,t* ≥ 0 ∀n ∈ N, l ∈ L, t ∈ T (3l) wn,l,q ∈ {0, 1} ∀n ∈ N, l ∈ L, q ∈ Q. (3m)
Constraint (3b) states that the total cumulative transmission capacity is equal to the initial existing transmission capacity plus the sum of the transmission capacity expansion along the path from node 0 to node n−, while constraint (3c) states that the total cumulative generation capacity is equal to the initial existing generation plus the sum of generation capacity expansion minus generation retirement along the path from node 0 to node n. The delayed in-service date for new transmission relative to new generation is intended to capture the longer development timelines typical for transmission projects. Constraint (3d) states that power production is limited by the total installed capacity of a given technology multiplied by its availability in each time block. Constraint (3e) enforces a system-wide renewable portfolio standard (RPS), mandating a percentage of the total amount of power generation coming from renewable energy sources. Constraint (3f) calculates the net power injection at bus b, while constraint (3g) is a soft constraint limiting power flow on a transmission line. Constraint (3h) states the sum of the net power injection in the network should be zero. Constraints (3j) and (3k) state that each load curtailment segment is non-negative and the sum of load curtailment segment cannot exceed the maximum MW violation of that segment. After fixing binary variables w, we can query the dual variables of the constraints in the resulting linear program. Dual variables are scaled in order to produced unscaled prices and inframarginal rents. The dual variable θ*n,b,g,t* of constraint (3d) can be interpreted as the marginal value of capacity of generation technology g at bus b in time block t. The dual variable π*n,b,t* of constraint (3f) is the locational marginal price (LMP). For completeness we define the linear program using the optimal values w∗
n,l,q found when solving model (3) as follows:

max (3a) s.t. (3b)-(3l) $$w_{n,l,q}=w_{n,l,q}^{*}\quad\forall n\in{\cal N},l\in{\cal L},q\in{\cal Q}.$$ (4a)

## 3 Establishing Beneficiaries

Supposing that system planners use model (3) to identify transmission expansion decisions, this section addresses the question of how to define beneficiaries, as well as the challenges that arise even when all parties agree on the formulation and scenarios used in the model.

## 3.1 Establishing A Counterfactual

To measure the benefits brought by a certain transmission project, we first need to define a counterfactual against which benefits will be measured.

Establishing a counterfactual to the construction of a particular transmission investment is complicated by the fact that subsequent transmission and generation investment, as well as operations, will change as a result of the investment under study. Some cost allocation schemes currently used in U.S. systems, especially those for investments motivated by reliability violations rather than economic efficiency, fail to establish a valid counterfactual because the models omit the possibility of operational changes or compensatory investments. As discussed in Mays (2023), the absence of a valid counterfactual is particularly clear in the case of interconnecting new generators.

After solving model (3) and determining expansion decisions for the present year, there are at least three ways that a counterfactual might be established. In each case, re-solving model (3) with additional constraints leads to an alternate solution with a higher objective function value. We define three options as follows:

1. Exclude the specific transmission investment and fix all other transmission and generation investments;
benefits reflect the difference in operating cost between the solutions.
2. Exclude the specific transmission investment, fix all other transmission investments, and allow generation investments to optimally readjust to the counterfactual network; benefits reflect the difference in investment and operating cost between the solutions.
3. Exclude the specific transmission investment (at all levels q *∈ Q* and for either all years y *∈ Y* or just the
present), but allow freedom in both generation and other transmission investments; benefits reflect the difference in investment and operating cost between the solutions.
The primary issue with the first option is that it is unrealistic and unnecessarily restrictive. Excluding the transmission investment without allowing any compensatory investments could lead to a situation with unsolvable reliability violations, leading either to an infeasible model or large costs driven by penalty parameters. The primary issue with the third option is that in order to determine participant-level benefits for the projects of interest, cost allocation determinations also need to be made for the counterfactual transmission projects. Since these allocations would in turn be determined against a similarly defined counterfactual, allowing these alternatives introduces a recursive aspect to the problem. Since allocations based on the first are guaranteed to be inaccurate and those based on the third would be impractical, we suggest that analysis should pursue the second option. Since investment in generation (as well as storage and distributed resources) is often exogenous or excluded from current models, we note the contrast between our recommendation and the claim in Hogan
(2018) that the information needed for cost allocation is already available in current planning models.

Putting this suggestion into practice could be challenging, especially in the case of upgrades prompted by reliability violations not observable in the linear approximations to the power flow equations typically used in capacity expansion models. At the expense of additional complexity, more complicated constraints could in principle be brought into model (3), making the construction of a valid counterfactual more straightforward. In practice, it is more common in such cases to skip the step of establishing a counterfactual altogether, instead socializing the cost of related upgrades or relying on power flow analyses with unclear connection to economic benefits. Even if an optimization model is not used, however, a better approach to assess benefits would be specifying a plausible alternative to resolve the identified reliability violations and measuring cost against this alternative. Noting the challenge, for the remainder of this paper we assume that benefits associated with the level of reliability are captured through penalties on power balance violations in model (3).

We can formalize the construction of a counterfactual as follows. Suppose we are interested in allocating the cost of one or more transmission investments represented by a subset WINV ⊂ W = *N × L × Q* of the binary variables w*n,l,q*, where we assume that the investments of interest occur at node n = 0. Then counterfactual generation investments, along with counterfactual prices and production quantities, can be found by solving

max (3a) (3b)-(3l) $$w_{n,l,q}=0\quad\forall(n,l,q)\in\mathcal{W}^{INV}$$ (5a) $$w_{n,l,q}=w_{n,l,q}^{*}\quad\forall(n,l,q)\in\mathcal{W}\setminus\mathcal{W}^{INV}.$$ (5b)

## 3.2 Generation

We first consider the potential for generators to benefit from transmission expansion. An important distinction is between new and existing generators. At present, most U.S. systems follow an "invest and connect"
approach in which the cost of network upgrades identified in interconnection studies is allocated to new generators. ERCOT, by contrast, uses a "connect and manage" approach that eschews network upgrades in the interconnection process but does not make any guarantees on the deliverability of energy from the interconnecting project. At present, no U.S. system allocates cost for subsequent network upgrades to generators after they have completed the interconnection process. The primary point of this subsection is to show that, in general, the direct benefits modeling approach pursued in this paper supports the "connect and manage" approach of allowing new generators to join the system without cost, but also supports the allocation of cost to existing generators on an ongoing basis.

Evaluated at node 0, the discounted operating profit expected by a unit of generation of type g at bus b can be calculated as

$$\mathbb{E}(\mathcal{U}_{b,g}^{\text{gen}})=\sum_{n\in\mathcal{N}}\zeta_{b(n)}\phi_{n}\left(\sum_{t\in\mathcal{T}}T_{t}\left(\pi_{n,b,t}-C_{n,g}^{\text{EN}}-C_{g}^{\text{YOM}}+\nu_{n}\mathbbm{1}_{\{g\in\mathcal{G}_{n}\}}\right)\frac{p_{n,b,g,t}}{G_{n,b,g}}-C_{g}^{\text{FIX}}\right),\tag{6}$$
where 1{g∈GR} = 1 if the generator can sell renewable energy credits and 0 otherwise.

With E(U∗gen b,g ) indicating expected benefits assuming the socially optimal transmission configuration and E(U′gen b,g ) indicating expected benefits with the counterfactual transmission configuration, the per unit expected benefit for generation of type g located at bus b from transmission expansion can then be calculated as the difference in expected operating profits:

$$\mathbb{E}(\Delta\mathcal{U}^{gen}_{b,g})=\mathbb{E}(\mathcal{U}^{gen}_{b,g})-\mathbb{E}(\mathcal{U}^{gen}_{b,g}).\tag{7}$$

## 3.2.1 Existing Generators

We first consider the case of existing generators, which can more clearly benefit or be harmed by transmission expansion. The presence of new generation in either the socially optimal or the counterfactual case can indicate how existing generators of the same type and located at the same bus are affected by the expansion. We state three cases formally as Theorem (1) and Corollaries (1) and (2). Theorem 1. Suppose new generation of type g is constructed at bus b in both the expansion scenario, i.e.,
∆G∗
0,b,g > 0, and the counterfactual scenario, i.e., ∆G′
0,b,g > 0. Then existing generation of that type at that bus neither benefits nor suffers losses from the expansion, i.e., E(∆Ugen b,g ) = 0.

Proof. For model (4), the KKT conditions on p*n,b,g,t* are

$$0\leq p_{n,h,g,t}\perp C^{\rm EN}_{n,g}+C^{\rm YOM}_{g}+\theta_{n,h,g,t}-\pi_{n,h,t}-\nu_{n}{\bf1}_{\{g\in\mathcal{G}_{R}\}}\geq0\qquad\forall n\in\mathcal{N},b\in\mathcal{B},g\in\mathcal{G},t\in\mathcal{T}.\tag{8}$$

By the complementarity condition, if pn,b,g,t > 0, we have θn,b,g,t = πn,b,t − CEN
                                                                           n,g − CVOM
                                                                                  g
                                                                                       + νn1{g∈GR}.

Then the discounted operating profit (6) can be written as

$$\mathbb{E}(\mathcal{U}_{b,g}^{\text{\tiny{even}}})=\sum_{n\in\mathcal{N}}\zeta_{\delta(n)}\phi_{n}\left(\sum_{t\in\mathcal{T}}T_{t}\theta_{n,b,t}\frac{p_{n,b,g,t}}{G_{n,b,g}}-C_{g}^{\text{\tiny{FIX}}}\right).\tag{9}$$
By complementary slackness, when θn,b,t > 0, pn,b,g,t Gn,b,g Gn,b,g = CA*b,g,t* holds. When θ*n,b,t* = 0, replacing pn,b,g,t with CA*b,g,t* would not affect the result. After replacement, the discounted operating profit (6) becomes

$$\mathbb{E}(\mathcal{U}_{b,g}^{\text{\tiny{on}}})=\sum_{n\in\mathcal{N}}\zeta_{\delta(n)}\phi_{n}\left(\sum_{t\in\mathcal{T}}T_{t}\theta_{n,b,t}CA_{b,g,t}-C_{g}^{\text{\tiny{FIX}}}\right).\tag{10}$$
For both models (4) and (5), the objective function and variable G*n,b,g* are defined to include summation over the path P(n). Given that node 0 is on the path of every node to the root node in the scenario tree, it follows that the KKT condition on ∆G0*,b,g* would aggregate over all nodes within the tree, given by

$$0\leq\Delta G_{0,b,g}\perp\sum_{n\in\mathcal{N}}\zeta_{\ell(n)}\phi_{n}\left(C_{0,g}^{\mathrm{INV}}+C_{g}^{\mathrm{FINX}}-\sum_{t\in\mathcal{T}}T_{t}CA_{b,g,t}\theta_{n,b,g,t}\right)\geq0\qquad\forall g\in\mathcal{G},b\in\mathcal{B}.\tag{11}$$
By complementary slackness, ∆G0*,b,g* > 0 implies

$$\sum_{n\in\mathcal{N}}\zeta_{\delta(n)}\phi_{n}\left(C_{0,g}^{\mathrm{INV}}+C_{g}^{\mathrm{FIN}}-\sum_{t\in\mathcal{T}}T_{t}C A_{b,g,t}\theta_{n,b,g,t}\right)=0.$$
When new generation of type g is constructed at bus b in the both expansion scenario and counterfactual n∈N ζδ(n)ϕnCINV
0,g . By the

scenario, i.e., ∆G∗
                  0,b,g > 0 and ∆G′
                                     0,b,g > 0, we have E(U∗gen
                                                               b,g ) = E(U′gen
                                                                            b,g ) = �

definition of benefits in (7), this leads to E(∆Ugen b,g ) = 0.

Corollary 1. Suppose new generation of type g is constructed at bus b in the expansion scenario, i.e., ∆G∗
0,b,g >
0, but not in the counterfactual scenario, i.e., ∆G′
0*,b,g* = 0. Then existing generation of that type at that bus benefits from the expansion, i.e., E(∆Ugen b,g ) > 0.

n∈N ζδ(n)ϕnCINV
0,g . ∆G′
0*,b,g* = 0 implies Proof. As shown in Theorem 1, ∆G∗
0*,b,g* > 0 implies E(Ugen b,g ) = �
n∈N ζδ(n)ϕnCINV
0,g . Therefore, by (7), the difference in expected operating profits is positive, i.e., E(U′gen b,g ) < �
E(∆Ugen b,g ) > 0.

Corollary 2. Suppose new generation of type g is constructed at bus b in the counterfactual scenario, i.e.,
∆G′
0,b,g > 0, but not in the expansion scenario, i.e., ∆G∗
0*,b,g* = 0. Then existing generation of that type at that bus suffers losses from the expansion, i.e., E(∆Ugen b,g ) < 0.

n∈N ζδ(n)ϕnCINV
0,g . ∆G′
0*,b,g* > 0 implies Proof. As shown in Theorem 1, ∆G∗
0*,b,g* = 0 implies E(Ugen b,g ) < �

E(U′gen
   b,g ) = �
         n∈N ζδ(n)ϕnCINV
                  0,g . Therefore, by (7), the difference in expected operating profits is negative, i.e.,

E(∆Ugen
   b,g ) < 0.

At a high level, it can be expected that generators in exporting regions will see benefits from transmission

expansion while generators in importing regions will suffer losses. Clear examples of this effect are shown in Hogan (2018) and O'Neill (2020), which analyze two-zone systems without subsequent generation investment. The more complex numerical study in this paper largely matches this intuition.

## 3.2.2 New Generators

We now turn attention to newly built generation. If these resources would have been built in the model even without the transmission expansion occurring in node 0, then benefits can be defined similarly to existing generators. In this case, Theorem 1 applies and we conclude that the new generation does not benefit from the transmission. If the generation would not otherwise be built, the zero-profit condition on investment in the socially optimal expansion nevertheless holds. Given perfect competition, condition (11) implies that investment in generation technology g will continue until operating profits fall to the level of annualized investment costs.

Under an optimization modeling approach, the implication of the zero-profit condition is that new generation cannot be identified as a beneficiary. We note that the assumptions of perfect competition and linear generation investment costs that underpin the zero-profit condition are standard in tools used for expansion planning.

Exceptions to this rule may apply, e.g., if there is a constraint on building generation, such that new capacity cannot be built to take full advantage of the new line. In this case, new generators would earn a rent associated with this constraint.

Such exceptions are likely to be less important for large lines that would facilitate production across a wider region. Alternatively, it may be argued that the computation of excess profit in Eq. (7) reflects too narrow a conception of benefits, and the existence of a new generator could itself be considered a benefit regardless of its profitability. In this case, additional assumptions outside the planning tool would be needed to define benefit estimates.

Given the recommendation not to allocate cost for network upgrades to new generators at the time of interconnection but then subsequently allocate cost to them throughout their life, the direct benefits modeling approach supports a significant change to current practice. The overall impact that such a change would have on the cash flows seen by generators over the course of their life is not clear. Suppose a new generator signed an interconnection agreement under a "connect and manage" approach, and then welfare-enhancing network upgrades were identified by a planning model. Since the model recommending these projects would assume the presence of the new generator, it would be more likely to recommend upgrades allowing the system to make use of the new generator's energy output. Projects identified to make use of the new generator could very well be the same as those that would be identified under the narrower models used in "invest and connect" interconnection procedures. Whereas current practice typically assigns the cost entirely to the new generator without accounting for externalized benefits, however, the proposed approach would allocate cost to other beneficiaries as well. As such, the overall effect would be to bring cost allocation in line with the beneficiaries pay principle.

## 3.3 Load

Benefits to different load zones can be defined much in the same way as benefits to generators. The major difference is that the planning model takes load as exogenous rather than as resulting from an expansion decision that may depend on transmission investment. Consumer surplus at bus b in node n is calculated as the difference between the value of energy consumed and payments made for energy and renewable energy credits. Since we are primarily interested in allocating cost between different zones, each of which comprises a diverse range of customers, it is reasonable to assume a single constant for the value of energy. However, we note that a more detailed representation of price-responsive load for individual customers would enable a more granular calculation of benefits. To simplify notation, we represent load curtailment at bus b at time t by zn,b,t

where $z_{n,b,t}=\sum_{i\in\mathcal{I}}z_{n,b,t}$. Evaluated at node 0, the expected value of consumer surplus can be written as

$$\mathbb{E}\langle\mathcal{U}_{b}^{\text{Load}}\rangle=\sum_{n\in\mathcal{N}}\zeta_{b}(z_{n})\phi_{n}\left(\sum_{i\in\mathcal{I}}T_{i}\left(\gamma^{\text{LOAD}}-\pi_{n,b,t}-\nu_{n}RPS_{n}\right)\left(D_{n,b,t}-z_{n,b,t}\right)\right).\tag{12}$$
As with generation, we compute the benefits from transmission expansion to loads at bus b as the difference in surplus between the socially optimal case and the counterfactual case:

$$\mathbb{E}(\Delta\mathcal{U}_{b}^{load})=\mathbb{E}(\mathcal{U}^{*}_{b}^{load})-\mathbb{E}(\mathcal{U}^{*}_{b}^{load}).\tag{13}$$
As with existing generators, the surplus difference E(∆Uload b
) can be positive, zero, or negative for loads.

## 3.4 Congestion Rents

In addition to generator and consumer benefits, a third component of market surplus is transmission congestion rents, computed as the difference between the payments made by load and the revenue received by generators. Under idealized assumptions, the availability of congestion rents could make the problem of cost allocation easier to solve, since congestion revenues would be sufficient to support a socially efficient level of transmission expansion (Hogan, 2018; Joskow and Tirole, 2005). In this case a "top-down" cost allocation would not be required as such, since risk-neutral investors would be willing to build transmission in exchange for the resulting valuable transmission rights. In practice, economies of scale and unpriced reliability constraints mean that congestion rents are well below what would be needed to support an efficient level of investment. For example, Sherman (2023) estimates that U.S.-wide congestion rents averaged approximately $8.2B for 2016–2021, while U.S. Energy Information Agency (2023) estimates the average cost of transmission in 2022 at $15/MWh, implying a total annualized cost of roughly $63B for the current system. While imprecise, these estimates suggest that congestion rents are an order of magnitude lower than what would be required for investments in transmission to be sustained on a merchant basis.

In principle, rights to congestion rents can be allocated as part of the cost allocation process, either proportional to market participant contributions or by auction. In general, empirical evidence in U.S. markets shows that current markets for financial transmission rights result in large transfers from consumers to financial traders (Leslie, 2021; Opgrand et al., 2022), suggesting opportunities for improvements in allocation (Risanger and Mays, 2024). In the numerical results for this paper, we compute generator and consumer benefits without adjusting for any assigned transmission rights, noting that future studies assessing the effects of financial transmission rights would likely require downscaling the results of our zonal network model to a more detailed nodal representation.

## 3.5 Multi-Value Planning

Inconsistent and non-intuitive cost allocation outcomes in the U.S. context can stem from projects being designated as having a single primary purpose and being evaluated according to the benefits it provides only along that dimension. U.S. systems distinguish between projects undertaken for economics, reliability, public policy, and generator interconnection, while any transmission enhancement necessarily affects outcomes across all four areas (DeLosa et al., 2024). As previously noted, we leave a more complete discussion of public policy interactions for future work. We note here, however, that an advantage of the direct benefits modeling approach is that all categories of benefits can be incorporated in a consistent manner as long as a valid counterfactual can be established. From a modeling perspective, the only requirement for establishing a valid counterfactual is that model (5) must have a feasible solution after transmission expansion decisions have been fixed. Because the model penalizes power shortfalls rather than implementing a hard constraint, and because entry of new generation is not restricted, reliability constraints cannot cause infeasibility. Our implementation of an RPS in Eq. (3e) could in principle lead to infeasibility. In practice, however, most states have implemented Alternative Compliance Payments to limit the potential cost of RPS policies, meaning that a soft constraint would more accurately reflect the public policy. Once a counterfactual has been established, costs associated with reliability and public policy naturally flow into prices for energy and clean attributes, allowing straightforward inclusion in benefit calculations.

## 3.6 Cost Allocation

The analysis thus far leads to the conclusion that existing generation and load can be beneficiaries of transmission expansion over the long term, implying that both existing generation and load should share cost under the "beneficiaries pay" principle. In the numerical study we examine two different policies for allocating the cost of transmission investments made at node 0: allocating cost only to load, as in current practice, and allocating across both existing generation and load.

When allocating cost only to load, the allocation ratio to load at bus b is determined using the following equation:

$$r_{b}^{load}=\frac{[\mathbb{E}(\Delta d_{b}^{load})]_{+}}{\sum_{b^{\prime}\in\mathcal{B}}[\mathbb{E}(\Delta d_{b^{\prime}}^{load})]_{+}},\tag{14}$$
where [∗]+ denotes max{0, ∗}.

When allocating cost to both load and existing generation, with G0
b,g representing the quantity of existing capacity of generation g at bus b, allocation ratios are determined using the following equations:

$$r_{b}^{l_{\text{end}}}=\frac{[\mathbb{E}(\Delta t_{b}^{l_{\text{end}}})]_{+}}{\sum_{\nu\in B}\left([\mathbb{E}(\Delta t_{b}^{l_{\text{end}}})]_{+}+\sum_{\nu\in\mathcal{G}}[\mathcal{G}_{b,\nu}^{\text{in}}\mathbb{E}(\Delta t_{\nu,\sigma}^{l_{\text{end}}})]_{+}\right)};\tag{15a}$$ $$r_{b,\sigma}^{l_{\text{end}}}=\frac{[\mathcal{G}_{b,\sigma}^{\text{in}}\mathbb{E}(\Delta t_{b}^{l_{\text{end}}})]_{+}}{\sum_{\nu\in B}\left([\mathbb{E}(\Delta t_{b}^{l_{\text{end}}})]_{+}+\sum_{\nu\in\mathcal{G}}[\mathcal{G}_{b,\sigma}^{\text{in}}\mathbb{E}(\Delta t_{\nu,\sigma}^{l_{\text{end}}})]_{+}\right)}.\tag{15b}$$

The presence of the max operator ensures that market participants who do not benefit from a transmission 
investment are not allocated cost. However, it also implies that market participants that are harmed by an expansion project are not compensated as part of cost allocation. It would be straightforward mathematically to define negative allocations, i.e., compensatory payments to these participants. Since the planning model by assumption identifies a surplus-maximizing expansion plan, there would be sufficient surplus in the market to make these compensatory payments.

Several recent cases in the U.S. show the potential for states or incumbents hurt by transmission expansion to intervene and prevent it from occurring (see, e.g., Hausman (2024)), suggesting that compensatory payments or long-term financial rights that protected incumbents against the effect of transmission expansion could lead to fewer disputes in planning.

## 4 Numerical Study

This section presents results of a numerical example on a simplified model of the ERCOT system. Building on the discussion of Section 3, we document the different benefits and losses seen by generation and loads in different parts of the system. One major conclusion of the numerical study is that allocating cost on a portfolio basis is likely to be more consistent with the beneficiaries pay principle than allocating on a project-by-project basis. Further, we contrast ex post benefits derived from out-of-sample tests against in-sample estimation, computing the range of possible distributional outcomes from transmission expansion to provide insight into the challenge posed by ambiguity in future scenarios and probabilities.

## 4.1 Data And Study Assumptions

The study employs an 8-Bus ERCOT DC Test Case introduced by Battula et al. (2020), with the network shown in Figure 2. The generation technologies considered are natural gas combined cycle (CC), natural gas combustion turbine (CT), coal, nuclear, utility-scale solar, and land-based wind. Costs for these technologies are sourced from the NREL Annual Technology Baseline database (National Renewable Energy Laboratory, 2022). The existing generation capacity mix is obtained from the ERCOT Capacity, Demand and Reserves

| Generation type   | b     |
|-------------------|-------|
| 1                 |       |
| b                 |       |
| 2                 |       |
| b                 |       |
| 3                 |       |
| b                 |       |
| 4                 |       |
| b                 |       |
| 5                 |       |
| b                 |       |
| 6                 |       |
| b                 |       |
| 7                 |       |
| b                 |       |
| 8                 |       |
| Gas CC            | 0     |
| Gas GT            | 0     |
| Coal              |       |
| 0                 | 2,514 |
| Nuclear           | 2,400 |
| Solar             | 0     |
| Wind              | 0     |

(CDR) Report (Electric Reliability Council of Texas, 2023). Existing generation capacity, reported in Table 1, is assigned to different buses in the test system in a manner consistent with the ERCOT resource siting methodology report (Electric Reliability Council of Texas, 2022c,d), but should not be expected to match locations precisely.

Hourly load data for the year 2020 from Electric Reliability Council of Texas (2022a) is used to represent the load profiles in the system. For each node n, load D*n,b,t* is obtained by multiplying this profile by a demand growth factor βn. Hourly solar and wind availability profiles for the year 2020 are extracted from Pfenninger and Staffell (2023) using methods described in Pfenninger and Staffell (2016) and Staffell and Pfenninger (2016). To ensure computational tractability and account for operation costs, a K-means method is employed to cluster the year of data based on the net load, from which 20 representative days (480 hours) with varying weight, i.e., Tt, are selected to represent a simulation year.

In the long-term planning model, the uncertainties included are the presence of an RPS, load growth, technology investment costs for wind and solar, and fuel cost. For each uncertainty except the RPS, low, medium, and high values are estimated based on National Renewable Energy Laboratory (2022); Electric Reliability Council of Texas (2022b). We note that given the high-quality solar and wind resources in Texas, the RPS constraint does not have a significant impact on the numerical results. A future scenario is defined as a subset of the uncertainty space that represents a specific combination of the five uncertainties. Considering a low, medium, and high value for each uncertainty, there will be a total of 35 = 243 possible future scenarios.

To ensure computational tractability for the MIP model, the number of scenarios must be reduced. In this study, seven scenarios with varying probabilities were selected based on the methodology described in Newlun et al. (2021). Since we wish to avoid making assumptions on underlying scenario probabilities, we do not claim that the transmission plan identified by the model is "optimal" as such. Out-of-sample tests show positive net benefits in all scenarios, however, suggesting that the chosen clustering and scenario selection procedures lead to a high-quality solution.

A 20-year planning horizon is simulated with investment decisions made every 5 years, resulting in a tree with depth four and seven scenarios. A discount rate of 7.78% is applied to compute the net present value of the total investment cost and operational cost in the objective function. It is assumed that the operational costs for each successive 5-year interval remain constant. In light of this assumption, the discount factor, denoted as
ζy for time index y *∈ {*1, 2, 3, 4}, is determined through the following formula:

$$\zeta_{y}=\frac{1}{(1+7.78\%)^{2(y-1)}}\left(1+\frac{1}{(1+7.78\%)^{1}}+\frac{1}{(1+7.78\%)^{2}}+\frac{1}{(1+7.78\%)^{3}}+\frac{1}{(1+7.78\%)^{4}}\right).$$
We use the power balance penalty curve shown in Table 2 and transmission line violation penalty γLINE = 9251
$/MW for all lines, congruent with the practices in ERCOT Electric Reliability Council of Texas (2021).

MW violation
≤ 5
5 ∼ 10
10 ∼ 20
20 ∼ 30
30 ∼ 40
40 ∼ 50
50 ∼ 100
≥ 100
γPB
i
($/MWh)
250
300
400
500
1000
2250
4500
5001

This case study assumes that there are seven types of transmission line expansion increments, with the same costs across all scenarios in each stage and for each corridor, as defined in Table 3. The per unit investment cost in Table 3 exhibits a significant decrease with increasing expansion capacity, reflecting economies of scale.

| Type   | Expansion (MW)   |   Amortized investment cost ( |
|--------|------------------|-------------------------------|
| $      |                  |                               |
| M/yr)  | Per unit cost (  |                               |
| $      |                  |                               |
| M/MW)  |                  |                               |
| 1      | 1400             |                         68.93 |
| 2      | 1800             |                         72.64 |
| 3      | 2300             |                         78.34 |
| 4      | 3000             |                         89.59 |
| 5      |                  |                               |
| 3600   | 98.79            |                          0.34 |
| 6      | 4200             |                        101.7  |
| 7      |                  |                               |
| 8000   | 154.96           |                          0.24 |

The models are implemented in Julia (Bezanson et al., 2017) using JuMP.jl (Dunning et al., 2017) and solved with Gurobi version 10.0.1 (Gurobi Optimization, LLC, 2020) using a MIP gap (where applicable) of 0.5%. The computations are performed on a Mac computer with an Apple M1 Max chip and 10 cores.

## 4.2 Expansion Plan

The transmission line expansions resulting from model (3) for the developed test system are summarized in Table 4. In the first stage (year 2023), corresponding to node 0 of the tree in Figure 1, six transmission expansion projects are selected. The largest of these is on path l2, connecting the generation-rich zone b3 with

| Year   | Scenario   |   l |
|--------|------------|-----|
| 1      |            |     |
| l      |            |     |
| 2      |            |     |
| l      |            |     |
| 3      |            |     |
| l      |            |     |
| 4      |            |     |
| l      |            |     |
| 5      |            |     |
| l      |            |     |
| 6      |            |     |
| l      |            |     |
| 7      |            |     |
| l      |            |     |
| 8      |            |     |
| l      |            |     |
| 9      |            |     |
| l      |            |     |
| 10     |            |     |
| l      |            |     |
| 11     |            |     |
| l      |            |     |
| 12     |            |     |
| l      |            |     |
| 13     |            |     |
| 2023   | -          |   0 |
| 2028   | 7          |     |
| 0      | 0          |   0 |
| 2033   | 1,2,6      |   0 |
| 2033   | 3,4        |   0 |
| 2033   | 5          |   0 |
| 2038   | 3          |   0 |

the population center b1.

Table 5 shows a weighted average of the total generation capacity additions made over the 20-year horizon in the seven modeled scenarios, as well as the same quantities in a counterfactual without any transmission expansion. In either case, the model builds new gas combustion turbines, solar, and wind, with no additions of coal, nuclear, or combined cycle gas in any scenario.

While we expected new transmission to support

| Generation Type   | Expansion   | No Expansion   |
|-------------------|-------------|----------------|
| Gas CC            | 0           | 0              |
| Gas CT            | 21,425      | 35,428         |
| Coal              | 0           | 0              |
| Nuclear           | 0           | 0              |
| Solar             | 9,859       | 14,938         |
| Wind              | 38,382      | 38,433         |

the deployment of additional wind, the primary effect of expansion in our model was instead to reduce the requirement for gas turbines: the model builds roughly the same amount of wind in the counterfactual case, but substantially more gas turbines. At node 0 of the model, new gas turbines are built at b1 in the expansion scenario, while new gas turbines are built at b1 and b8 in the counterfactual. No wind or solar is built in node 0, potentially due to our assumption that transmission expansions will enter service only in the second year index.

## 4.3 Portfolio Vs. Project-By-Project Allocation

The first policy question we address is whether to assess the benefit of the six projects selected at node 0 on a portfolio or project-by-project basis. In our notation, the question is whether to compute a single instance of the counterfactual model (5) with WINV including all six projects as a portfolio, or six separate instances of model (5) with a single element each in WINV . For purposes of this subsection, we allocate costs according to Eq. (14), i.e., only to loads and only to those with positive benefits, without compensating those harmed by the expansion. We conclude that assessment at the portfolio level results in a cost allocation more consistent with the beneficiaries pay principle.

Table 6 shows the benefits calculated for each project evaluated separately as well as the portfolio, along with an allocation percentage across the 8 buses. The first observation is that, for each individual project except the expansion on l6, the total expected benefit across all buses is negative. As a consequence, the projects would not pass a benefit–cost test when assessed as individual projects, despite being part of a beneficial portfolio of projects. While not guaranteed, each project has at least one bus with positive benefits, allowing a cost allocation to be defined under our formula.

| Project        | b      |
|----------------|--------|
| 1              |        |
| b              |        |
| 2              |        |
| b              |        |
| 3              |        |
| b              |        |
| 4              |        |
| b              |        |
| 5              |        |
| b              |        |
| 6              |        |
| b              |        |
| 7              |        |
| b              |        |
| 8              |        |
| Sum            |        |
| load ratio (%) | 33.95  |
| l              |        |
| 2              |        |
| 8000 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             |        |
| 4,904          | -1,488 |
| r              |        |
| b              |        |
| (%)            | 92.27  |
| l              |        |
| 3              |        |
| 2300 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             | 3,668  |
| r              |        |
| b              |        |
| (%)            |        |
| 100.0          | 0.0    |
| l              |        |
| 6              |        |
| 1800 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             | -67    |
| r              |        |
| b              |        |
| (%)            | 0.0    |
| l              |        |
| 7              |        |
| 3600 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             |        |
| -456           | -1,714 |
| r              |        |
| b              |        |
| (%)            |        |
| 0.0            | 0.0    |
| l              |        |
| 10             |        |
| 2300 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             | 181    |
| r              |        |
| b              |        |
| (%)            | 7.33   |
| l              |        |
| 12             |        |
| 2300 MW        |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             | 12     |
| r              |        |
| b              |        |
| (%)            | 0.66   |
| Projects Sum   |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             |        |
| 8,242          | -5,018 |
| r              |        |
| b              |        |
| (%)            |        |
| 40.54          | 13.57  |
| Portfolio      |        |
| ∆              |        |
| U              |        |
| b              |        |
| (              |        |
| $              |        |
| M)             | 6,215  |
| r              |        |
| b              |        |
| (%)            | 57.17  |

Figure 3 shows the benefit–cost ratio for the portfolio for each bus under each allocation method, with the benefits used for both subplots taken from the "Portfolio" row in Table 6. The result of the project-byproject allocation is that some loads, namely, those at b4 and b5, can be assigned positive cost despite having negative benefits from the overall portfolio. These positive allocations result from the positive benefits found for expansion on l6, l7, and l12 when assessed individually and imply that the benefit–cost ratio drops below zero for b4 and b5 in the project-by-project allocation. By contrast, the benefit–cost ratio is consistent across all load zones in the case of the portfolio-level allocation, with negatively impacted zones assigned no cost. If subjected to the project-by-project allocation, loads at b4 and b5 would likely object and work to prevent the socially beneficial expansion from occurring, e.g., by denying necessary permits. To avoid this issue, we suggest that it is preferable to allocate costs for a portfolio rather than individual projects.

## 4.4 Generator Impacts

While the previous subsection considered the impacts on load only, we now turn to impacts on generation.

A summary of the aggregate allocation across all generators and loads, calculated with Eqs. (15a) and (15b), is shown in Table 7. We note that the aggregate benefits are substantially larger for generators than for loads in our case study, but we cannot make a general claim regarding how benefits are likely to be split in other instances. Consistent with intuition, we observe that the largest line expansion selected by the model, l2, connects the zone in which the largest benefits accrue to generators, b3, with the zone in which the largest benefits accrue to loads, b1.

| Participants   | b    |
|----------------|------|
| 1              |      |
| b              |      |
| 2              |      |
| b              |      |
| 3              |      |
| b              |      |
| 4              |      |
| b              |      |
| 5              |      |
| b              |      |
| 6              |      |
| b              |      |
| 7              |      |
| b              |      |
| 8              |      |
| Sum            |      |
| load           | r    |
| load           |      |
| b              |      |
| (%)            |      |
| 12.99          | 4.77 |
| generation     | r    |
| gen            |      |
| b              |      |
| (%)            | 0.0  |

As discussed in Section 3.2, generators can also experience significant losses from expansion. The total expected benefits that accrue to existing generation of different types across buses is shown in Figure 4. Whereas the allocation in Table 7 aggregates only the positive benefits, Figure 4 includes the negative impacts.

Just as loads at b1 and b2 see the largest benefits from expansion, generators in those zones see the largest losses. The largest generator benefits occur at b3, concentrated in existing thermal generators at that location.

## 4.5 In-Sample Vs. Out-Of-Sample Tests

The cost allocations defined above are calculated based on in-sample results, i.e., the expected zonal benefits determined as the weighted average across various scenarios where scenarios and scenario probabilities are taken from the planning model covering the whole planning horizon of 20 years. Table 6 and 7 show the in-sample cost allocation ratios under two policies. As discussed above, however, the scenarios and probabilities determined for the planning model do not reflect the full range of possible outcomes or participant beliefs. Accordingly, a key question is the validity of these estimates and the extent to which out-of-sample results might diverge from the in-sample expected value.

Estimating the benefits out of sample for the whole 20-year horizon is complicated computationally, because it would require definition of a complete policy describing how transmission and generation investments after the first stage will be made based on realizations of uncertainty that are not contained in our original planning model. In our context, such a policy cannot be defined: we rely on a stakeholder process to determine the scenarios and probabilities to be used in our planning model, and cannot fully specify the outcomes of future stakeholder processes. To avoid this issue, we instead perform out-of-sample tests for both cost allocation ratios on a single operating year. Specifically, we perform an out-of-sample analysis for y = 2, i.e., year 2028, to assess benefits of transmission expansion projects determined in y = 1, computing the distribution of realized benefits against the ex ante allocation. In out-of-sample tests, we used load and renewable availability data from 2022, sourced and processed in a manner consistent with the procedures outlined in Section 4.1. Since our out-of-sample tests do not have transmission investment, we employ a linear program covering the entire year of data instead of selecting representative days as in the MIP planning model. Benefits are computed for all 35 = 243 possible realizations of uncertainty described above. The aggregated generation and load benefits on each bus across different scenarios in year 2028 are shown in Figure 5. The scenarios are ordered by the gross social benefits from the transmission expansion. It is noteworthy that while not generalizable, in our case study the expansion is beneficial under all realizations of uncertainty. It can also be observed that, while the rank ordering of zones is relatively stable overall, there are wide swings in the absolute benefits realized in each zone.

The overall distribution of benefits evaluated ex post for generators and loads is shown in Figure 6, with generation of all types aggregated at each bus. The blue bars indicate the number of times (out of the 243 scenarios) ex post benefits are calculated to be in each range, while the red dashed line indicates the cost allocation determined ex ante (as in Table 7). Here, the consequences of uncertainty are apparent, as the ex post distribution of benefits in some cases does not contain the red dashed line. In absolute terms, the deviation can be quite significant: for example, generators at b3 may see almost 70% of total benefits from the portfolio after being allocated 46% of costs. One possible reason for biased estimates is that ex ante benefits are estimated over a longer horizon than those calculated ex post. Even if a less biased ex ante estimate could have been produced with a more targeted computation, however, the significant variance observed in realized benefits would remain.

To test how the benefits of the portfolio may evolve over the life of the new lines, we construct an additional test using realizations of uncertainty for the year 2038 and assuming that a 3000 MW capacity expansion on l8
has subsequently been added to the system. Referring back to Table 4, an expansion on l8 is chosen in each of the seven scenarios in the planning model, with the timing and size varying by scenario. With this 3000 MW expansion added to the system, we re-compute the benefits of the original portfolio of six transmission lines. Figure 7 shows the distribution of benefits when allocated only to load for the years 2028 and 2038. In year
2038, benefits shift away from loads at b1 to those at b2, b5, and b8. The shift exhibited in Figure 7 suggests an extension of the argument in Section 4.3 that a portfolio-level allocation should be preferred to a project-level allocation. Suppose two projects with 50-year expected lives are selected and built in consecutive years. Given that they will coexist in the network for 49 out of their 50 years, their benefits will necessarily be interdependent and could be better assessed jointly. Extending the argument further, estimates of the aggregate benefits of the network may be more accurate than estimates of the benefits provided by any subset of network elements.

Overall, the results confirm the potential for uncertainty to cause challenges in cost allocation given the disagreements that market participants will inevitably have on the probability of future scenarios. In the context of the "beneficiaries pay" standard, the distribution of possible outcomes makes it clear that an allocation of costs determined ex ante will not be commensurate with the benefits realized ex post. Economic theory offers a potential resolution to the resulting conflicts in the form of financial contracts issued ex ante that would effectively reallocate cost to the ultimate beneficiaries (Ferris and Philpott, 2022). Given the complications involved in defining such contracts, we defer the effort to future work.

## 5 Conclusion

Given the numerous ways in which motivated parties can intervene to prevent transmission expansion, disputes over cost allocation can hold up investment in regional and interregional projects. Out of fairness and to forestall such interventions, U.S. system planners have sought methods to allocate costs according to the estimated benefits that projects will bring. In a direct benefits modeling approach, planners could in principle solve an optimization model that both established the social benefits of a project and enabled an estimate of benefits at the participant level. However, inadequacies in both the models available and the information used in them can lead to significant disagreements about the fairness of the resulting allocations.

This paper identifies several challenges in the use of models to establish cost allocations. Given the complexity of the modeling task, planners typically use a combination of software tools to evaluate proposed projects. One consequence is that it may be difficult to establish a valid counterfactual against which benefits can be measured and to calculate all categories of benefits that could result from an expansion project. The challenge is even greater when assessing benefits out of sample, since a full calculation would require not only determining the range of scenarios to be tested but also specifying a policy for future expansion decisions given the realization of uncertainty.

Without fully resolving these challenges, the theoretical analysis and numerical study lead to five observations connected to the "beneficiaries pay" principle. First, benefit estimates should include some attempt to account for the change in the resource mix that is likely to occur with any change in the network. Second, cost should in general not be allocated to new entrants, but should be allocated to incumbents that benefit from transmission expansion. Third, allocations made on the basis of portfolios of projects are likely to be more defensible than those made on individual projects. Fourth, conflicts might be lessened with greater effort to compensate the losers from socially beneficial transmission expansion. Fifth, conflicts might be lessened with greater effort to address the risk that participant-level benefits will diverge significantly from ex ante allocation decisions.

## Acknowledgements

This research was supported by the Power Systems Engineering Research Center under Project M-43. The authors would like to thank Jim McCalley, Gustavo Cuello Polo, Ali Jahanbani Ardakani, Richard O'Neill, Abe Silverman, and members of the project advisory team for feedback and discussions.

## References

Abou El Ela, A. and R. El-Sehiemy (2009). Transmission usage cost allocation schemes. Electric Power Systems
Research 79(6), 926–936.
Acevedo, A. L. F., A. Jahanbani-Ardakani, H. Nosair, A. Venkatraman, J. D. McCalley, A. Bloom, D. Osborn,
J. Caspary, J. Okullo, J. Bakke, and H. Scribner (2021). Design and valuation of high-capacity hvdc macrogrid transmission for the continental US. *IEEE Transactions on Power Systems 36*(4), 2750–2760.
Adamson, S. (2018).
Comparing interstate regulation and investment in us gas and electric transmission.
Economics of Energy & Environmental Policy 7(1), 7–24.
Avar, A. and M.-K. Shiekh-El-Eslami (2022). A new benefit-based transmission cost allocation scheme based
on capacity usage differentiation. *Electric Power Systems Research 208*, 107880.
Banez-Chicharro, F., L. Olmos, A. Ramos, and J. M. Latorre (2017a). Beneficiaries of transmission expansion
projects of an expansion plan: an Aumann-Shapley approach. *Applied Energy 195*, 382–401.
Banez-Chicharro, F., L. Olmos, A. Ramos, and J. M. Latorre (2017b). Estimating the benefits of transmission
expansion projects: an Aumann-Shapley approach. *Energy 118*, 1044–1054.
Battula, S., L. Tesfatsion, and T. E. McDermott (2020). An ERCOT test system for market design studies.
Applied Energy 275, 115182.
Bezanson, J., A. Edelman, S. Karpinski, and V. B. Shah (2017).
Julia: A fresh approach to numerical
computing. *SIAM Review 59*(1), 65–98.
Bravo, D., E. Sauma, J. Contreras, S. de la Torre, J. Aguado, and D. Pozo (2016). Impact of network payment
schemes on transmission expansion planning with variable renewable generation.
Energy Economics 56,
410–421.
Brown, P. and A. Botterud (2021). The value of inter-regional coordination and transmission in decarbonizing
the US electricity system. *Joule 5*(1), 115–134.
Bushnell, J. and F. Wolak (2017, February). Beneficiaries-pay pricing and "market-like" transmission outcomes. Available at https://bushnell.ucdavis.edu/uploads/7/6/9/5/76951361/bushnell_wolak_18_ feb_2017.pdf.
De La Torre, S., A. J. Conejo, and J. Contreras (2008). Transmission expansion planning in electricity markets.
IEEE Transactions on Power Systems 23(1), 238–248.
DeLosa, Joe, I., J. P. Pfeifenberger, and P. Joskow (2024, March). Regulation of access, pricing, and planning
of high voltage transmission in the u.s. Working Paper 32254, National Bureau of Economic Research.
Denholm, P., P. Brown, W. Cole, T. Mai, B. Sergi, M. Brown, P. Jadun, J. Ho, J. Mayernik, C. McMillan,
et al. (2022). Examining supply-side options to achieve 100% clean electricity by 2035. Technical report, National Renewable Energy Lab.(NREL), Golden, CO (United States).
Dunning, I., J. Huchette, and M. Lubin (2017). JuMP: A modeling language for mathematical optimization.
SIAM Review 59(2), 295–320.
Electric Reliability Council of Texas (2021).
Other binding document revision request.
https:
//www.ercot.com/files/docs/2021/12/14/037OBDRR_01_Power_Balance_Penalty_Updates_to_
%20Align_with_PUCT_Approved_High_System_Wide_Offer_Ca.docx.
Electric Reliability Council of Texas (2022a).
2022 ERCOT hourly load data.
https://www.ercot.com/
gridinfo/load/load_hist.
Electric Reliability Council of Texas (2022b).
2022 long-term assessment for the ERCOT region.
https:
//www.ercot.com/gridinfo/planning.
Electric Reliability Council of Texas (2022c). 2022 long-term system assessment for the ercot region. Available
at https://www.ercot.com/files/docs/2022/12/22/2022_LTSA_Report.zip.
Electric Reliability Council of Texas (2022d).
Long-term system assessment resource siting methodology.
Available at https://www.ercot.com/files/docs/2022/12/22/2022_LTSA_Report.zip.
Electric Reliability Council of Texas (2023). Capacity, demand, and reserve (CDR) report. https://www.
ercot.com/gridinfo/resource.
Federal Energy Regulatory Commission (2011, July). Order 1000: Transmission planning and cost allocation by
transmission owning and operating public utilities. Available at https://www.ferc.gov/industries-data/
electric/electric-transmission/order-no-1000-transmission-planning-and-cost.
Federal Energy Regulatory Commission (2022, April). Building for the future through electric regional transmission planning and cost allocation and generator interconnection. Available at https://www.ferc.gov/
media/rm21-17-000.
Ferris, M. and A. Philpott (2022). Dynamic risked equilibrium. *Operations Research 70*(3), 1933–1952.
Galiana, F. D., A. J. Conejo, and H. A. Gil (2003). Transmission network cost allocation based on equivalent
bilateral exchanges. *IEEE Transactions on Power Systems 18*(4), 1425–1431.
Gurobi Optimization, LLC (2020). Gurobi optimizer reference manual.

Hamilton, A. L., H. B. Zeff, G. W. Characklis, and P. M. Reed (2022). Resilient California water portfolios require infrastructure investment partnerships that are viable for all partners. *Earth's Future 10*(4),
e2021EF002573.
Hausman, C. (2024, January). Power flows: Transmission lines and corporate profits. Working Paper 32091,
National Bureau of Economic Research.
Hogan, W. W. (2018). A primer on transmission benefits and cost allocation. Economics of Energy & Environmental Policy 7(1), 25–46.
Jenkins, J. D., E. N. Mayfield, E. D. Larson, S. W. Pacala, and C. Greig (2021). Mission net-zero america:
The nation-building path to a prosperous, net-zero emissions economy. *Joule 5*(11), 2755–2761.
Joskow, P. and J. Tirole (2005). Merchant transmission investment. *The Journal of industrial economics 53*(2),
233–264.
Kristiansen, M., F. D. Mu˜noz, S. Oren, and M. Korp˚as (2018). A mechanism for allocating benefits and costs
from transmission interconnections under cooperation: A case study of the north sea offshore grid. The
Energy Journal 39(6), 209–234.
Lau, J. and B. F. Hobbs (2021). Electricity transmission system research and development: Economic analysis
and planning tools.
Available at https://www.energy.gov/sites/default/files/2021-05/Economic%
20Analysis%20and%20Planning%20Lau%20Hobbs2.pdf.
Leslie, G. (2021). Who benefits from ratepayer-funded auctions of transmission congestion contracts? Evidence
from New York. *Energy Economics 93*, 105025.
MacDonald, A., C. Clack, A. Alexander, A. Dunbar, J. Wilczak, and Y. Xie (2016, May).
Future costcompetitive electricity systems and their impact on US CO2 emissions. *Nature Climate Change 6*(5), 526–
531.
Mays, J. (2023). Generator interconnection, network expansion, and energy transition. IEEE Transactions on
Energy Markets, Policy and Regulation 1(4), 410–419.
Mu˜noz, F. and J.-P. Watson (2015). A scalable solution framework for stochastic transmission and generation
planning problems. *Computational Management Science 12*(4), 491–518.
Mu˜noz, F. D., B. F. Hobbs, J. L. Ho, and S. Kasina (2014). An engineering-economic approach to transmission
planning under market and regulatory uncertainties: WECC case study.
IEEE Transactions on Power
Systems 29(1), 307–317.
National Renewable Energy Laboratory (2022). 2022 annual technology baseline. https://atb.nrel.gov/.

Newlun, C. J., J. D. McCalley, R. Amitava, A. J. Ardakani, A. Venkatraman, and A. L. Figueroa-Acevedo
(2021). Adaptive expansion planning framework for MISO transmission planning process. In 2021 IEEE
Kansas Power and Energy Conference (KPEC), pp. 1–6. IEEE.
Opgrand, J., P. Preckel, D. Gotham, and A. Liu (2022). Price formation in auctions for financial transmission
rights. *The Energy Journal 43*(3), 33–57.
Organization of MISO States (2021).
Organization of MISO states statement of principles: Cost allocation for long range transmission planning projects. Available at https://cdn.misoenergy.org/20210211%
20RECBWG%20Item%2003a%20CAPCom%20Cost%20Allocation%20Principles520802.pdf.
O'Neill, R. P. (2020).
Transmission planning, investment, and cost allocation in US ISO markets.
In
M. Hesamzadeh, J. Rosell´on, and I. Vogelsang (Eds.), Transmission Network Investment in Liberalized Power Markets, pp. 171–199. Switzerland: Springer, Cham.
Pfenninger, S. and I. Staffell (2016). Long-term patterns of European PV output using 30 years of validated
hourly reanalysis and satellite data. *Energy 114*, 1251–1265.
Pfenninger, S. and I. Staffell (2023). Renewables.ninja. www.renewables.ninja.
Risanger, S. and J. Mays (2024). Congestion risk, transmission rights, and investment equilibria in electricity
markets. *The Energy Journal 45*(1).
Roustaei, M., M. Sheikh-El-Eslami, and H. Seifi (2014).
Transmission cost allocation based on the users'
benefits. *International Journal of Electrical Power & Energy Systems 61*, 547–552.
Sauma, E. and S. Oren (2006). Proactive planning and valuation of transmission investments in restructured
electricity markets. *Journal of Regulatory Economics 30*(3), 358–387.
Sherman, A. (2023). Transmission congestion costs in the U.S. RTOs. Available at https://gridprogress.
files.wordpress.com/2023/04/transmission-congestion-costs-in-the-us-2021-update.pdf.
Staffell, I. and S. Pfenninger (2016). Using bias-corrected reanalysis to simulate current and future wind power
output. *Energy 114*, 1224–1239.
United
States
Court
of
Appeals
(2014).
Illinois
Commerce
Commission
v.
FERC,
756
f.3d.
https://wwws.law.northwestern.edu/research-faculty/clbe/events/energy/documents/illinois_
commerce_comn_v_federal_energy_regulatory_comn.pdf.
U.S. Energy Information Agency (2023).
Annual energy outlook.
Available at https://www.eia.gov/
electricity/data/eia861/.
Wogrin, S., D. Tejada-Arango, A. Downward, and A. Philpott (2021). Welfare-maximizing transmission capacity expansion under uncertainty. *Philosophical Transactions of the Royal Society A 379*(2202), 20190436.
Wolak, F. (2020). Transmission planning and operation in the wholesale market regime. In M. Hesamzadeh,
J. Rosell´on, and I. Vogelsang (Eds.), *Transmission Network Investment in Liberalized Power Markets*, pp.
101–133. Switzerland: Springer, Cham.
Yang, Z., H. Zhong, Q. Xia, C. Kang, T. Chen, and Y. Li (2015). A structural transmission cost allocation
scheme based on capacity usage identification. *IEEE Transactions on Power Systems 31*(4), 2876–2884.