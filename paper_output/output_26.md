# A Benchmark For The Application Of Distributed Control Techniques To The Electricity Network Of The European Economic Area

A. Riccardi, L. Laurenti, and B. De Schutter Abstract The European Economic Area Electricity Network Benchmark (EEA-ENB) is a multi-area power system representing the European network of transmission systems for electricity to facilitate the application of distributed control techniques. In the EEA-ENB we consider the Load Frequency Control (LFC) problem in the presence of renewable energy sources (RESs), and energy storage systems (ESSs). RESs are known to cause instability in power networks due to their inertia-less and intermittent characteristics, while ESSs are introduced as a resource to mitigate the problem. In the EEA-ENB, particular attention is dedicated to Distributed Model Predictive Control (DMPC), whose application is often limited to small and homogeneous test cases due to the lack of standardized large-scale scenarios for testing, and due to the large computation time required to obtain a centralized MPC action for performance comparison with DMPC strategies under consideration. The second problem is exacerbated when the scale of the system grows. To address these challenges and to provide a real-world-based and control-independent benchmark, the EEA-ENB has been developed. The benchmark includes a centralized MPC strategy providing performance and computation time metrics to compare distributed control within a repeatable and realistic simulation environment.

A. Riccardi Delft Center for Systems and Control, Delft University of Technology, Mekelweg 2, 2628 CD Delft, The Netherlands e-mail: a.riccardi@tudelft.nl L. Laurenti Delft Center for Systems and Control, Delft University of Technology, Mekelweg 2, 2628 CD Delft, The Netherlands e-mail: l.laurenti@tudelft.nl B. De Schutter Delft Center for Systems and Control, Delft University of Technology, Mekelweg 2, 2628 CD Delft, The Netherlands e-mail: b.deschutter@tudelft.nl A. Riccardi, L. Laurenti, and B. De Schutter

## 1 Introduction 1.1 The Origin Of The Benchmark: Motivation And Challenges

The European Economic Area Electricity Network Benchmark (EEA-ENB) is a benchmark designed for the implementation and testing of distributed control strategies for large-scale power networks. The idea behind the benchmark is to build an abstract model of the European network of transmission systems for electricity. We represent each country of the European economic area as an independent electrical area connected to others through tie lines according to a predefined electricity network topology. The result is a real-world oriented benchmark that accounts for the presence of renewable generation and Energy Storage Systems (ESSs) in the load-frequency control (LFC) problem of the power network.

The development of the EEA-ENB is essential because no established control model for the European electricity transmission system consistently serves as a reference for distributed control techniques, especially with energy storage systems and renewable energy sources. Additionally, the use case for the EEA-ENB is not restricted only to the pure development of control strategies. With minimal modifications, it can also be used for other applications, such as the economic optimization of network operation, the study of network expansion strategies, testing of security and privacy features, and simulation of emergency situations such as cascading blackouts and network restoration.

To assess the time and computation requirements for the implementation of a distributed control strategy we implement centralized Model Predictive Control (MPC) on the network. Together with the value of the cost function of centralized MPC developed, this provides the user metrics to evaluate the advantages and disadvantages in the implementation of a specific distributed control technique. The EEA-ENB is formulated with a modular approach such that extensions can be implemented if needed, allowing for various application scenarios as mentioned before. The stability of the network is assessed through the study of the Load Frequency Control (LFC) problem. Moreover, another application that is particularly relevant for this benchmark is the economical optimization of energy trading among network agents. The EEA-ENB can also be employed to formulate Distributed MPC (DMPC) techniques in the presence of hybrid dynamics thanks to a modified ESS dynamics reported.

Additional extensions, not included in this work, include the characterization of each electrical area according to the deregulated energy market through the modeling of generation plants, the auction system for scheduling energy production across the various generation companies, and the market of power exchanges between different electrical areas [4].

The main challenge in controlling the EEA-ENB has to be sought in its scale: 26
electrical areas are considered, each subject to distinct variations in load requests and renewable generation. When using a growing number of control agents the computation time of a centralized control action becomes increasingly prohibitive, thus, distributed control approaches are required.

## 1.2 Load Frequency Control In Modern Power Networks

TheLFC problemis acrucial challengein powersystems,and ithas aparticular socioeconomic interest [15]. The LFC problem gained interest in the research community in the 1970s [9] after some major systems events led to cascading blackouts [12]. These problems typically arise when unexpected changes in the load of a power system occur, with consequent shifts in the operating frequency of the electrical area under consideration, and the propagation of this effect to neighboring areas. In the last decades cascading blackouts have been exacerbated by the increasing diffusion of renewable energy sources, which are posing new challenges for LFC of interconnected power grids due to their intermittent and stochastic nature, and inertia-less generation [20].

Nowadays, new strategies to increase network robustness are constantly sought
[4]. This is the reason why ESSs are fundamental in modern energy grids: they allow for more efficient use of energy, optimizing its usage based on the demand, and they can be used to counteract the inertia-less properties of renewable energy sources. Therefore, part of the modeling section of this chapter is dedicated to ESSs, from the simplest dynamical formulation to more complex hybrid formulations.

Formally, the main control problem solved in the EEA-ENB is the regulation to zero of the frequency deviation of the network from the nominal value. This problem is solved in the presence of unexpected changes in the load, renewable generation, and ESSs. Early approaches to the solution were mainly based on PID control theory. With the progression of technology, more advanced techniques have been implemented, such as variable gain scheduling, fuzzy logic control, artificial neural networks, and optimal control [15, 20].

In this chapter, we propose MPC as reference control technique for the benchmark, and DMPC as its natural extension. The choice of MPC is related to the fact that it provides the optimal control action according to a certain cost function defined by the user, while incorporating constraints on the evolution of the state and control. Nevertheless, the EEA-ENB is designed to be control-independent, and virtually all control techniques can be implemented on it. For a detailed list of control approaches for the LFC problem, we refer to [20].

## 2 Problem Description 2.1 System Description

The EEA-ENB is composed of 26 interacting electrical areas connected through tie lines and uses real-world data acquired from the ENTSO-E transparency platform accessible from [1]. Each area represents an equivalent electrical machine aggregating the inertia and dispatchable capacity of generators in that specific area, a modeling technique commonly used in the context of LFC [15]. The electrical topol-

AT
BE
BG HR CZ
DK
EE
FI
FR
DE
GR
HU
IE
IT
LV
LT
NL
NO
PL
PT
RO SK
SI
ES
SE
CH
AT
0
0
0
0
2.65
0
0
0
0
4.82
0
5.61
0
4.76
0
0
0
0
0
0
0
5.88 1.85
0
0
5.58
BE
0
0
0
0
0
0
0
0
4.69
5.77
0
0
13.19
0
0
0
1.75
0
0
0
0
0
0
0
0
0
BG
0
0
0
0
0
0
0
0
0
0
4.02
0
0
0
0
0
0
0
0
0
3.01
0
0
0
0
0
HR
0
0
0
0
0
0
0
0
0
0
0
3.61
0
0
0
0
0
0
0
0
0
0
2.12
0
0
0
CZ 2.65
0
0
0
0
0
0
0
0
5.13
0
0
0
0
0
0
0
0
4.67
0
0
4.33
0
0
0
0
DK
0
0
0
0
0
0
0
0
0
5.03
0
0
17.82
0
0
0
5.44 11.56
0
0
0
0
0
0
10.22
0
EE
0
0
0
0
0
0
0
6.37
0
0
0
0
0
0
2.2
0
0
0
0
0
0
0
0
0
0
0
FI
0
0
0
0
0
0
6.37
0
0
0
0
0
0
0
0
0
0
8.99
0
0
0
0
0
0
8.89
0
FR
0
4.69
0
0
0
0
0
0
0
9.35
0
0
12.38 11.19
0
0
0
0
0
0
0
0
0
8.58
0
6.09
DE 4.82 5.77
0
0
5.13 5.03
0
0
9.35
0
0
0
0
0
0
0
4.98 15.23 9.06
0
0
0
0
0
13.41 4.84
GR
0
0
4.02
0
0
0
0
0
0
0
0
0
0
10.94
0
0
0
0
0
0
0
0
0
0
0
0
HU 5.61
0
0
3.61
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
5.87 1.48 4.63
0
0
0
IE
0
13.19
0
0
0
17.82
0
0
12.38
0
0
0
0
0
0
0
13.84 27.51
0
0
0
0
0
0
0
0
IT 4.76
0
0
0
0
0
0
0
11.19
0
10.94
0
0
0
0
0
0
0
0
0
0
0
3.81
0
0
5.84
LV
0
0
0
0
0
0
2.2
0
0
0
0
0
0
0
0
1.69
0
0
0
0
0
0
0
0
0
0
LT
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1.69
0
0
0
5.55
0
0
0
0
0
10.14
0
NL
0
1.75
0
0
0
5.44
0
0
0
4.98
0
0
13.84
0
0
0
0
16.99
0
0
0
0
0
0
0
0
NO
0
0
0
0
0
11.56
0
8.99
0
15.23
0
0
27.51
0
0
0
16.99
0
0
0
0
0
0
0
2.28
0
PL
0
0
0
0
4.67
0
0
0
0
9.06
0
0
0
0
0
5.55
0
0
0
0
0
3.37
0
0
10.93
0
PT
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
4.34
0
0
RO
0
0
3.01
0
0
0
0
0
0
0
0
5.87
0
0
0
0
0
0
0
0
0
0
0
0
0
0
SK 5.88
0
0
0
4.33
0
0
0
0
0
0
1.48
0
0
0
0
0
0
3.37
0
0
0
0
0
0
0
SI 1.85
0
0
2.12
0
0
0
0
0
0
0
4.63
0
3.81
0
0
0
0
0
0
0
0
0
0
0
0
ES
0
0
0
0
0
0
0
0
8.58
0
0
0
0
0
0
0
0
0
0
4.34
0
0
0
0
0
0
SE
0
0
0
0
0
10.22
0
8.89
0
13.41
0
0
0
0
0
10.14
0
2.28 10.93
0
0
0
0
0
0
0
CH 5.58
0
0
0
0
0
0
0
6.09
4.84
0
0
0
5.84
0
0
0
0
0
0
0
0
0
0
0
0

ogy of the network is derived from the grid map also provided by ENTSO-E [1]. The benchmark is constituted by 26 control areas due to considerations about the availability and scale of the data about the 31 members of the EEA. The electrical topology of the resulting network is reported in Figure 1, where each country is labeled with the respective ISO code. Positions of the areas in the space are selected according to their geographical centroids, and, on this basis, the lengths of the tie lines are defined using the Euclidean distance as reported in Table 1. In this graph representation, each node is associated with a dynamics incorporating generation, storage, consumption, and interaction behaviors of the considered electrical area and of its neighborhood. In particular, an electrical area is composed of a multiplicity of autonomous subsystems working together to guarantee the satisfaction of the set points assigned by the area-level controller. The aggregation of those subsystems allows one to define an equivalent electrical machine for each area. Specifically, each area may comprehend the following:

•
A *dispatchable generator* used to model all sources of energy that can be actively
controlled to balance the load. Conventional power sources are hydroelectric turbines, nuclear power plants and gas, oil, or coil turbines. Those sources are associated with an aggregated power generation that we can allocate at each time step according to the production limits of each area.
•
Non-dispatchable generation associated with renewable energy production, such
as wind and solar generation, which have intermittent and stochastic nature. We
assume that data are available both for the exact value of the produced power and for day-ahead forecasts.
•
An *Energy Storage System* (ESS) used to accumulate and supply energy at the best
convenience and according to the control strategy implemented. In general, energy storage systems can be classified into three macro-categories: electrical storage (e.g. ultracapacitors), electrochemical storage (e.g. batteries), and mechanical storage (e.g. water reservoirs). However, this distinction is not considered in the benchmark, but it is suggested as a possible extension. Following the same approach used for dispatchable generation, we consider the aggregated storage and power of all the ESSs in the electrical area.
•
A *load demand* for which measurements and day-ahead forecasts are available.
Those components contribute to the internal load-frequency balance of the electrical area. Moreover, a power exchange among areas is present over the tie lines reported in the electrical topology. This interaction must also be accounted for in the overall power balance.

## 2.2 System Dynamics

The topology of the power system is represented as a graph G = (V, E) where each node 𝑣𝑖 ∈ V is associated with an independent electrical area 𝑖, and each undirected edge 𝑒𝑖 𝑗 = 𝑒 𝑗𝑖 = (𝑣𝑖, 𝑣𝑗) ∈ E ⊆ V × V is a tie line connecting adjacent areas 𝑖
and 𝑗, allowing for bidirectional power flow. In our case, we have 26 nodes, one for each electrical area. The presence of an edge represents the existence of a power connection. For each node 𝑣𝑖, we define its neighborhood as N𝑖 = {𝑣 𝑗 ∈ V | (𝑣𝑖, 𝑣𝑗) ∈
E}, i.e. the set of nodes connected to the node 𝑣𝑖. To each node 𝑣𝑖, 𝑖 = 1*, . . . ,* 26
an equivalent electrical machine is associated according to the schematic in Figure
2. Each electrical area 𝑖 is always characterized by at least three states: the angle 𝛿𝑖
of the rotor, the operating frequency 𝑓𝑖 of the equivalent machine, and the energy
𝑒𝑖 stored in the ESS. The control inputs for the 𝑖-th area are the deviation Δ𝑃disp
𝑖

of dispatchable power production w.r.t. the scheduled value, and the power $P_{i}^{\text{ESS},\,\text{c}}$ supplied to or $P_{i}^{\text{ESS},\,\text{d}}$ withdrawn from the ESS. Additionally, each area is subjected to the influence of external inputs: the variation in the load request $\Delta P_{i}^{\text{load}}$, renewable energy production $\Delta P_{i}^{\text{exp}}$, and the power transmitted over the tie lines $\Delta P_{i}^{\text{e}}$ connected to $P_{i}^{\text{exp}}$.

For this system, it is common to assume [4, 15] a linearized discrete-time model around an operating point ($\delta_{0},f_{0}$) for the power angle and frequency dynamics. We assume $\delta_{0}=30$[deg], but this depends on the scheduled power exchanges among electrical areas as specified later, with limits $\delta_{0}\in(0,90)$[deg]; moreover, the operating frequency of the European power network is $f_{0}=50$[Hz][15]. Regarding the ESS of the $i$-th area, the simplest model capturing the charging and discharging characteristics of a storage system is the linear representation also reported in [22]. Expressions of this model, and alternative formulations of the ESS dynamics, as the PVA description in [18], are discussed in Section 2.4.1. For the tie lines interaction, we also use a linearized equation [15] under the assumption that machine angle deviations are small enough, which will be guaranteed through operating constraints in the control formulation.

To summarize, the state, input, and external input of the $i$-th area are the vectors:

$$\mathbf{x}_{i}=\left[\Delta\delta_{i}\ \Delta f_{i}\ e_{i}\ \right]^{\intercal}\quad\mathbf{u}_{i}=\left[\Delta P_{i}^{\text{disp}}\ P_{i}^{\text{ESS},\,\text{c}}\ P_{i}^{\text{ESS},\,\text{d}}\ \right]^{\intercal}\quad\mathbf{w}_{i}=\left[\Delta P_{i}^{\text{load}}\ \Delta P_{i}^{\text{ren}}\ \Delta P_{i}^{\text{iso}}\ \right]^{\intercal},\tag{1}$$

and their aggregation provides the respective definition of the state, input, and external input vectors for the overall network:

\[\mathbf{x}=\left[\mathbf{x}_{1}^{\intercal}\ \cdots\ \mathbf{x}_{26}^{\intercal}\
Assuming that the discrete-time dynamics obtained through forward Euler discretization has sampling time 𝜏, the dynamics of the 𝑖-th electrical area has the form:

$$\mathcal{S}_{i}:\begin{cases}\Delta\delta_{i}\left(k+1\right)=\Delta\delta_{i}\left(k\right)+\tau2\pi\Delta f_{i}\left(k\right)\\ \Delta f_{i}\left(k+1\right)=\left(1-\frac{\tau}{T_{\text{P},i}}\right)\Delta f_{i}\left(k\right)+\tau\frac{K_{\text{P},i}}{T_{\text{P},i}}\left(\Delta P_{i}^{\text{disp}}\left(k\right)-\Delta P_{i}^{\text{load}}\left(k\right)+\Delta P_{i}^{\text{ren}}\left(k\right)\right.\\ \left.-\Delta P_{i}^{\text{ide}}\left(k\right)-P_{i}^{\text{ESS},\,c}\left(k\right)+P_{i}^{\text{ESS},\,\text{d}}\left(k\right)\right)\\ e_{i}\left(k+1\right)=e_{i}\left(k\right)+\tau\left(\eta_{i}^{c}P_{i}^{\text{ESS},\,c}\left(k\right)-\frac{1}{\eta_{i}^{d}}P_{i}^{\text{ESS},\,\text{d}}\left(k\right)\right)\end{cases}\tag{3}$$

$$\Delta P_{i}^{\text{tie}}\left(k\right)=\sum_{j\in\mathcal{N}_{i}}T_{ij}\left(\Delta\delta_{i}\left(k\right)-\Delta\delta_{j}\left(k\right)\right),\tag{4}$$
where 𝐾p,𝑖 and 𝑇p,𝑖 are respectively the gain and the time constants of the dynamics of the rotating mass; 𝜂c
𝑖 and 𝜂d
𝑖 are charging and discharging rates of the battery with 0 *< 𝜂*c
𝑖, 𝜂d
𝑖 < 1; and 𝑇𝑖 𝑗 [GW/deg] is the gain associated with the tie line (*𝑖, 𝑗*), i.e. 𝑇𝑖 𝑗 = 𝑘𝑖 𝑗/𝑑𝑖 𝑗, which depends on the geographical distance 𝑑𝑖 𝑗 [km] among the electrical areas, and on the gain 𝑘𝑖 𝑗 [km·GW/deg], which is assumed to be equal to
1 for all 𝑖, 𝑗 in this chapter.

## 2.3 Assumptions And Operating Conditions

The electrical angle deviation is constrained as −30 ≤ Δ𝛿𝑖 ≤ 30, so that the electrical angle satisfies 0 ≤ 𝛿𝑖 ≤ 60, with 𝛿𝑖,0 = 30 [deg]. For the operating frequency we assume the range −0.04 ≤ Δ 𝑓𝑖 ≤ 0.04, with 𝑓𝑖,0 = 50 [Hz] [4, 15]. For the ESSs, we consider the maximum storage capacity to be equal to the total dispatchable capacity, i.e. 0 ≤ 𝑒𝑖 ≤ 𝑃disp
𝑖,max, for each area 𝑖. For each electrical area 𝑖 the following state constraints hold:

$$-30\leq\Delta\delta_{i}\leq30\qquad-0.04\leq\Delta f_{i}\leq0.04\qquad\quad0\leq e_{i}\leq P_{i,\max}^{\rm disp}\tag{5}$$
Input limits are selected such that the total available dispatchable or storage capacity can be allocated over one hour:

$$-\frac{P_{i,\max}^{\rm disp}}{\tau}\leq\Delta P_{i}^{\rm disp}\leq\frac{P_{i,\max}^{\rm disp}}{\tau}\qquad0\leq P_{i}^{\rm ESS,\,c},\ P_{i}^{\rm ESS,\,d}\leq\frac{P_{i,\max}^{\rm disp}}{\tau}\tag{6}$$
The sampling time of the system is 𝜏 = 2.5 [s], which is 10 times faster than the time constant 𝑇p,𝑖 = 25 [s]. A variation in the external inputs occurs every 1440 time steps, i.e. every hour. A simulation of 24 · 1440 = 34560 steps would use 24 hours of real-world data about load and renewable generation, see Section 3.1 for additional details.

An aspect not usually considered in LFC systems is the total dispatchable production limit. In this benchmark, using real-world data, we want to constrain the total

dispatchable production to be non-negative, and smaller than the overall capacity of a certain area, i.e. $0\leq P_{i,0}^{\rm disp}(k)\leq P_{i,\rm max}^{\rm disp}$. Some areas may have a renewable production that exceeds the total load request. Thus, this constraint ensures that the excess is stored for later use or transmitted to neighboring areas through machine angles adjustments. As initial condition, we assume to have a dispatchable production that compensates for the total load request and that accounts for the renewable generation:

$$P_{i,0}^{\rm disp}=\max\left\{0;\,P_{i,0}^{\rm load}-P_{i,0}^{\rm exp}\right\}\,.\tag{7}$$

To guarantee that $P_{i,0}^{\rm disp}$ is not negative we select it as the maximum between zero and the difference $P_{i,0}^{\rm load}-P_{i,0}^{\rm exp}$.

## 2.4 Extensions And Alternative Formulations

We propose three directions to modify or extend the proposed dynamics: a PWA formulation of the ESS dynamics, an extension to include the behavior of turbines and pumps, and an augmented state representation to describe the energy market. Other possible extensions are reported at the end of this section.

## 2.4.1 Ess Hybrid Dynamics

Assuming that the ESSs can only be in a charging or discharging state at each time step, their dynamics can be described with the following PWA equations [18]:

$$e_{i}(k+1)=\begin{cases}e_{i}(k)+\tau\eta_{i}^{e}\Delta P_{i}^{\text{ESS}}(k)\text{if}\Delta P_{i}^{\text{ESS}}(k)\geq0\\ e_{i}(k)+\tau\frac{1}{\eta_{i}^{q}}\Delta P_{i}^{\text{ESS}}(k)\text{if}\Delta P_{i}^{\text{ESS}}(k)<0\end{cases}\tag{8}$$
In this formulation, the charging and discharging inputs used in (3) are substituted by a single input 𝑃ESS
𝑖
, representing the total power exchange of the electrical area with the ESS. This formulation is completely different from the linear one in (3), and it can be demonstrated that the two representations are equivalent only if the ESS is lossless, i.e. is if 𝜂c = 𝜂d = 1.

## 2.4.2 Turbine And Pump Dynamics Extension

A finer representation of the system would include the presence of a turbine for the generation of the dispatchable power, and of a turbine/pump system for mechanical ESS to allocate and use energy in the water reservoirs (this is not necessary for other types of ESSs). This concept can be applied both to the ESS formulation in (3) and (8). Additional states are introduced in this new description: the signals previously considered in (3) and (8) as inputs are now the states of the turbines or pump. Additionally, new inputs 𝑢disp
𝑖
, 𝑢ESS, c
𝑖
, 𝑢ESS, d
𝑖
are introduced to control the turbines and pump. Specifically, if we consider the linear formulation (3) for the 𝑖-th electrical area we have:

x𝑖 = � Δ𝛿𝑖 Δ 𝑓𝑖 𝑒𝑖 Δ𝑃disp 𝑖 𝑃ESS, c 𝑖 𝑃ESS, d 𝑖 � ⊺ u𝑖 = � 𝑢disp 𝑖 𝑢ESS, c 𝑖 𝑢ESS, d 𝑖 � ⊺ (9)
and the dynamics (3) is augmented with the update equations:

� Δ𝑃disp 𝑖 (𝑘) + 𝜏 𝐾t,𝑖 Δ𝑃disp 𝑖 (𝑘 + 1) = � 1 − 𝜏 𝑇t,𝑖 (10) 𝑇c,𝑖 𝑇t,𝑖 𝑢disp 𝑖 𝑃ESS, c 𝑖 (𝑘 + 1) = � 1 − 𝜏 � Δ𝑃ESS, c 𝑖 (𝑘) + 𝜏 𝐾c,𝑖 𝑇d,𝑖 𝑇d,𝑖 𝑢ESS, d 𝑖 � Δ𝑃ESS, d 𝑖 (𝑘) + 𝜏 𝐾d,𝑖 𝑇c,𝑖 𝑢ESS, c 𝑖 𝑃ESS, d 𝑖 (𝑘 + 1) = � 1 − 𝜏
where𝑇t,𝑖,𝑇c,𝑖,𝑇d,𝑖 and 𝐾t,𝑖, 𝐾c,𝑖, 𝐾d,𝑖 are respectively the time constants and gains of the turbine and storage turbine/pump of the 𝑖-th electrical area. As good engineering practice, the time constants 𝑇t,𝑖, 𝑇c,𝑖, 𝑇d,𝑖 are selected to be at least 10 times smaller than 𝑇p,𝑖, and accordingly the sampling time 𝜏 has to be at least 100 times smaller than the original one in (3), i.e. 𝜏 = 0.025 [s]. For further details see [4, 7].

## 2.4.3 State Augmentation And The Energy Market

The energy market can be characterized by augmenting the difference equations of system (3). Specifically, by integrating the variation of dispatchable generation and power transmission via the tie lines, and considering the electricity prices for energy generation and trade, we can effectively model the electricity market of the EEA-ENB. To this end, the dynamics (3) are augmented with the two states 𝑃disp
𝑖
,
𝑃tie
𝑖 , which evolve according to:

$$\begin{array}{l}P_{i}^{\rm disp}(k+1)=P_{i}^{\rm disp}(k)+\tau\Delta P_{i}^{\rm disp}(k)\\ P_{i}^{\rm tie}(k+1)=P_{i}^{\rm tie}(k)+\tau\Delta P_{i}^{\rm tie}(k)\end{array}\tag{11}$$

In this way, we can also impose limits on the overall dispatchable generation for each electrical area according to the data acquired from [1]. Specifically, each area is subjected to $0\leq\Delta P_{i}^{\rm disp}(k)\leq P_{i,\rm max}^{\rm disp}$.

## 2.4.4 Additional Extensions

The equivalent machine modeling approach can also be applied to the deregulated energy market [4]. This approach involves defining various actors for electricity production in different regions, each with its dispatchable generation capacity. These actors, known as generation companies, can be represented by individual turbines that aggregate the inertia of all the generators within the same company. Additionally, there are ESSs that aggregate the storage capacities of each company. Thus, in each area 𝑖, there is a certain number of dispatchable generators and ESSs. A centralized auction system determines which generation company supplies energy to each area, considering cross-border production, electrical topology, and predefined operational strategies.

We also highlight the fact that each electrical area can be further subdivided into frontier sectors and a central sector, with tie-lines connecting them. This subdivision of the electrical topology can be used for energy trade modeling. The central sector may account for the generation of critical infrastructures and is connected to all the frontier sectors. Each frontier sector is connected to the frontier sector of a neighboring area and to the central sector of the area it belongs to. This further subdivision of the topology can be used to mitigate the effect of power transmission from adjacent areas, to ensure enhanced stability of the central sector, and to define scheduled power transmissions among neighboring areas.

Future research should also consider the exploration of different ESS technologies, the challenges related to their implementation, their feasibility, and economic sustainability, all aspects that can contribute to the further refinement of the EEA- ENB.

## 2.5 Goal Of The Control System

The main control goal for this system is to regulate the frequency deviation Δ 𝑓𝑖 =
𝑓𝑖 − 𝑓𝑖,0 of each electrical area to zero, so that the frequency of the network stays at the desired value 𝑓0 = 50 [Hz]. Moreover, we require to regulate the machine angle deviation Δ𝛿𝑖 = 𝛿𝑖 −𝛿𝑖,0 to zero, such that the efficiency of the machine is preserved.

In addition to the control objectives, the control system should also ensure that the operational constraints of Section 2.3 are satisfied.

However, other control goals can also be defined. First, if an economic MPC
problem is formulated using electricity prices, then the total monetary cost for running the network can be considered, defined as =C/MWh for each agent, for each energy source, and at each time step. With this approach, the least expensive network operation strategy can be defined, trading off the lower operational cost of the network with its stability. In this regard, if soft constraints are implemented to limit the frequency deviation, then the total-time-spent and the average-time-spent outside the optimal operation interval of the frequency can also be considered as a performance indicator. Moreover, other control goals can be considered that are more specific to the technological implementation of the network. Those could regard the number of charging and discharging cycles of the batteries, their average charge level, or also the electrical machine angle deviation w.r.t. the most efficient one. This means that we might incorporate operational and maintenance costs in the benchmark and consider them as a way to compare control strategies.

## 3 Benchmark Design 3.1 Input Data

The network of equivalent machines is modeled using real data about load requests, renewable generation, and dispatchable capacities of the 26 European states selected for the implementation. Data is acquired from the ENTSO-E electricity transparency platform [1]. As an example, data for the 24 hours of January 1, 2022, are reported in Figure 3. Raw data is available every hour for each area considered, both for measurements and day-ahead forecasts.

## 3.2 Implementation Details

Table 2 reports the parameters used in the benchmark. Their selection is done according to the parameters used in similar simulation designs [4, 7, 15]. The sampling time of the systems is selected as 𝜏 = 2.5 [s]. It follows that, for each hour, i.e. for each new data sample, 1440 steps of duration 𝜏 are considered in the control simulation. We use linear interpolation to compute the external inputs
Δ𝑃load, meas
𝑖
(𝑘) , for 𝑘 = 0*, . . . ,* 34559, from the data of 𝑃load, meas
𝑖
(ℎ) available every hour, for ℎ = 1*, . . . ,* 24. The same approach is used for renewable generation measurements 𝑃ren, meas
𝑖
, and for the forecasts 𝑃ren, for
𝑖
, 𝑃ren, for
𝑖
. The resulting signal variations are in Figure 4.

| 𝜏                   |
|---------------------|
| p                   |
| ,𝑖                  |
| 𝐾                   |
| p                   |
| ,𝑖                  |
| 𝜂                   |
| c                   |
| 𝑖                   |
| 𝜂                   |
| d                   |
| 𝑖                   |
| 2.5 [s] 25 [s] 0.05 |
| �                   |
| Hz                  |
| GW                  |
| �                   |
| 0.9 1.1             |

## 3.3 Comparison With Other Benchmarks In The Field

Several benchmarks for the simulation of power networks are present in the literature. Among the most popular ones, we can report the various implementations of IEEE buses [2]. Those benchmarks are oriented towards the simulation of power networks for electrical engineering applications. The benchmark we propose is instead oriented to the implementation of distributed control techniques, with predictive control as primary objective. To the best of our knowledge, an LFC-oriented benchmark modeled using data from the EEA is not present in the literature. A similar study was performed in [7] for the simulation of the Northern European network, but without considering renewable generation and ESSs.

## 3.4 Performance Metrics

To evaluate the system performance we consider a quadratic cost function (we will formally introduce and define the cost function in (12), Section 5). Specifically, since the EEA-ENB is structured for the implementation of distributed control techniques, the overall cost over one day of simulation for the network controlled with a centralized MPC architecture represents the optimality target for every alternative control formulation.

Another performance indicator of the control strategy is the computation time required to obtain the control action. Specifically, centralized MPC might not be suited for real-time control of the EEA-ENB due to the excessive computation time required to obtain the optimal control action. Distributed architectures are usually faster in obtaining the control law since they distribute the computational burden among the control agents, but they are more complex to implement. Also, the cost of communication among the control agents, represented by the total volume of information exchanged across the network, can be used as a metric.

## 3.5 Alternative Test Cases

We propose the simulation for a single day of operation of the network. However, data is available at [1] for every day of the year. Seasonality plays an important role in power generation from renewable sources. For example, solar production can increase or decrease depending on the presence of clouds, the temperature, and the length of the day. Load data is also affected by seasons. Evaluating the network with the average data about load and renewable generation of the four different seasons will give a clear view of the effectiveness of the control strategy considered over an entire year, with a mitigated variability introduced by a single day selection.

## 3.6 Output Data

Executing the benchmark will provide data about the electrical machine angles deviations, their frequency deviations, the energy stored in each area, the total power production and exchange with the ESSs, and the power transmitted over the tie lines. Those quantities are used to compute the performance metrics, and to evaluate the control strategy. Thus, both the evolution of the states of the system and the control actions can be collected and stored.

## 3.7 Essential Properties

The constraints provided for the frequency operation are essential for the stability of the network. Any prolonged deviation from the intervals provided will lead to emergency operation modes or failure of components, which in turn may generate cascading blackouts in the network. The implementation of soft constraints on the state can allow for this deviation outside safety margins, but always considering the stability of the operation of the network and the economic cost of such deviations. For more information, we refer the reader to [7, 12].

Regarding the MPC implementation, both the feasibility and stability properties should be met [3, 17]. Moreover, for the robustness of the system to the disturbances, which are the variations of the load and the renewable generation, an in-depth analysis of their evolution over an extended time window should be performed to characterize them correctly. Then, robust MPC synthesis methods could be used to guarantee this property [3].

## 4 Accessing The Benchmark 4.1 Links To Sources, Limitations, Costs, And Licensing

The benchmark is implemented in Matlab (r2023b), and the necessary files to execute it are available at [21]. Gurobi Optimizer1 is required for the computation of the centralized MPC strategy. Alternatively, the Matlab Optimization Toolbox2 can be used with minimal modifications.

The benchmark is provided for free as it is under MIT the license. Data from [1]
used for the construction of the benchmark is publicly available under the Creative Commons Attribution 4.0 International License (CC-BY 4.0).

## 4.2 Documentation

Documentation for the benchmark is available at: https://gitlab.tudelft.nl/ariccardi/ european-economic-area-electricity-network.

For clarity, in the following, we provide the user with information about the functions used. The data from [1] has been preliminarily checked for integrity, replacing missing entries with linear interpolations, and reported on a consistent scale. This process was performed with specialized scripts reported in the online documentation. The resulting preprocessed data set is also part of the benchmark and provided as .csv files. The benchmark is constituted by the following files:

- main.m: this is the principal script to run the control simulation. - data import.m: this script reads the preprocessed data about load demands and
renewable generation measurements and forecasts stored in .csv files, and returns the parameters and signals required for the simulation.
- state update network.m and state update model.m, which are identical
files in this first formulation, but might be distinguished later to implement model
mismatches or parameters inaccuracies. The former is used to simulate the system dynamics, and the latter as a prediction model for the centralized MPC strategy.

- objective function.m: this function takes as inputs the parameters, the current
value of the state, and the inputs and external inputs over the prediction window to return the total cost over that window.
- plot results.m: used to produce plots of the simulation results and input data.

## 5 Discussion For Future Comparison 5.1 Reference Approach: Centralized Predictive Control

The LFC problem has been extensively studied in the literature. As a source of references to existing approaches for its solution, we refer to the survey [20]. To provide a comparison case for the implementation of distributed control techniques, we have implemented a centralized MPC scheme [7, 18]. Considering the system described in (3), we define at each time step $k$ the following centralized control problem:

$$\min_{\mathbf{u}}\sum_{j=1}^{N}\mathbf{x}^{\intercal}(j|k)\mathbf{Rx}(j|k)+\mathbf{u}^{\intercal}(j-1|k)\mathbf{Qu}(j-1|k)$$ $$\text{s.t.dynamics(3)}\forall v_{i}\in\mathcal{V}\tag{12}$$ $$\mathbf{x}(0|k)=\mathbf{x}(k)\forall v_{i}\in\mathcal{V}$$ $$\text{constraints(5)}\forall v_{i}\in\mathcal{V}$$ $$\text{priorated}\mathbf{u}^{\intercal}(0|k)\sim\mathbf{u}^{\intercal}(N-1|k)\intercal,\ \mathbf{R}\ \text{and}\ \mathbf{Q}\ \text{are diagonal cost matrices of appropriate distributions,and}\ N\ \text{is the prediction horizon.According to the receding horizon logic of MPC,we apply}\ \mathbf{u}(0|k)\ \text{to the system,discard the remaining control actions,and therefore.Follow the existence problem,hence efficient algorithms for the problem (12) is a generalization of the optimization problem, the problem can be solved using an active-set or an interior point algorithm.

For the benchmark, the optimization is performed with Gurbloi Optimizer using the barrier algorithm. The simulation required 206 [1, 15], and 24[1] to be completed using a processor Intel Xeon-2637v3, with a phase clock of 3.5 GHz, and coupled with 128 GB of RAM. The solution of the optimal control problem is the vector of inputs $\mathbf{u}(t)$, $k=0$, $\ldots$, $3459$, (the power transmitted over the time times connecting its state), $t$ denotes the electrical areas is reported too, which allows quantifying the power trade necessary across electrical areas for the optimal operation of the network from a centralized and a cooperative perspective. Interactions among electrical areas, or agents in a generalized setting, is indeed one of the critical aspects of a distributed control strategy [8, 16], and often one of the aspects characterizing the control strategy of the definition of the sub-networks in cooperation/competition.

The evolution of the states resulting from the sequence of inputs obtained through MPC is reported in Figure 6. For the overall power balance of each country, please consult the online repository https://gitlab.tudelft.nl/ariccardi/european-economicarea-electricity-network.

The evolution of the cost function is presented in Figure 7. Its value is the metric to evaluate distributed control techniques w.r.t. the proposed centralized approach. In the application of distributed control, the performance of the system usually decreases to achieve auxiliary objectives such as improvement in the computation time required to obtain the control action, reduction in the volume of information exchanged across the network (with advantages in the sector of security too), or reliability and redundancy of control in the presence of faults or unforeseen events.

## 5.2 Other Possible Control Approaches

To develop a deeper insight into the topics of LFC, MPC, and distributed control some references are reported in the following. In the LFC literature, see also [20], many articles focus on PI control strategies where tuning of the parameters is performed through various optimization techniques [11, 14, 19]. Despite their promising validations and a general increase in performance w.r.t. conventional PI-based LFC, all these strategies still lack the fundamental advantages of model-based control: optimization of performance indices, incorporation of constraints into the control problem, ability to compensate for known external signals, and multi-objective optimization. On the other hand, PI control is easier to implement and has a faster computation speed.

A similar optimization-based tuning approach is used in [6], this time to tune the parameters of an MPC controller.

In [7] a centralized MPC approach similar to the one proposed in (12) is presented, but in [7], data of the Nordic transmission system is used to build an electricity network model. Power plant models are used to characterize the generation dynamics of each electrical area, but ESSs and renewable generation are not considered. Economic MPC is addressed too in [7] and the results of centralized MPC are compared with a PD controller.

The use of hydro-pumped storage for LFC of microgrids including renewable generation is explored in [5], where a control architecture based on a decentralized PD controller tuned using a Quasi-Netwon optimization method is implemented.

A characterization of an electricity network using hybrid dynamics is provided in [18]. There, PWA dynamics and binary decision variables are used, leading to a hybrid MPC problem formulated as a Mized Integer Linear Program (MILP), and solved using a branch-and-bound optimization algorithm. This approach is used to model three different aspects: the ESS, the operational mode of the microgrid, and the operational mode of the generation plants.

In [23] a distributed Linear Quadratic Regulator (LQR) is implemented to tackle the LFC problem. Methods for the distributed computation of the LQR control action are used in [23] to increase the modularity and the scalability of the control architecture. The advantages of this approach rely on the ease of implementation, and on the low computation time needed to compute the control action. The disadvantages are that the applicability of the approach is limited to linear unconstrained control problems.

A way to address Economic MPC can be found in [13]. There, both the LFC
and economic load dispatch problems for power networks are considered. Those problems are usually approached using hierarchical control structures, where the economic load dispatch is at the upper level, and LFC at a lower level. Instead, in [13] the two problems are considered simultaneously, to improve the economic performance of the systems.

Another Economic MPC strategy is reported in [10]. There, a multi-objective genetic algorithm predictive control technique is used to simultaneously optimize the conflicting objectives of LFC and security-constrained economic dispatch.

## 5.3 Summary

The LFC problem has been widely investigated in the literature, and we have proposed a benchmark to evaluate distributed control strategies for solving it. The challenges arising in recent years are often related to the ever-growing use of distributed energy sources which are inertia-less and can affect the frequency of the network. The use of ESSs can mitigate this effect, and we have proposed strategies to model their dynamics, extensions, and future directions for their exploration. Accordingly, future control strategies of electricity networks should account for the presence of distributed energy sources, and the implementation of distributed control strategies for efficient and resilient operation of the network. Those aspects are indeed part of the centralized MPC formulation that we have proposed as a benchmark scheme. An efficient distributed control strategy is expected to perform worse than the centralized one proposed here if only the value of the cost function is considered, but has additional properties such as a reduced computation complexity and computation time, a lower shared volume of information, or enhanced privacy, security and resilience properties.

## Acknowledgments

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (Grant agreement No. 101018826) - Project CLariNet

## References

1. ENTSO-E.
European
Network
of
Transmission
System
Operators
for
Electricity.
https://www.entsoe.eu.
2. Power and Energy. IEEE DataPort. https://ieee-dataport.org/topic-tags/power-and-energy. 3. A. Bemporad and M. Morari. Robust model predictive control: A survey. In A. Garulli and
A. Tesi, editors, *Robustness in Identification and Control*, pages 207–226. 1999.
4. H. Bevrani. *Robust Power System Frequency Control*. Springer, 2014.
5. H. H. Coban, A. Rehman, and M. Mousa. Load frequency control of microgrid system by
battery and pumped-hydro energy storage. *Water*, 14:1–22, 2022.
6. M. Elsisi, M. Soliman, M. A. S. Aboelela, and W. Mansour. Bat inspired algorithm based
optimal design of model predictive load frequency control. International Journal of Electrical
Power & Energy Systems, 83:426–433, 2016.
7. A. M. Ersdal, L. Imsland, and K. Uhlen. Model predictive load-frequency control. IEEE
Transactions on Power Systems, 31:777–785, 2016.
8. F. Fele, J.M. Maestre, and E.F. Camacho. Coalitional control: Cooperative game theory and
control. *IEEE Control Systems*, 37:53–69, 2017.
9. C. E. Fosha and O. I. Elgerd. The megawatt-frequency control problem: A new approach via
optimal control theory. *IEEE Transactions on Power Apparatus and Systems*, 89:563–577,
1970.
10. H. Golpˆıra and H. Bevrani. A framework for economic load frequency control design using
modified multi-objective genetic algorithm. *Electric Power Components and Systems*, 42:788–
797, 2014.
11. D. K. Gupta, A. V. Jha, B. Appasani, A. Srinivasulu, N. Bizon, and P. Thounthong. Load frequency control using hybrid intelligent optimization technique for multi-source power systems.
Energies, 14:1–16, 2021.
12. H. Haes Alhelou, M. E. Hamedani-Golshan, T. C. Njenda, and P. Siano. A survey on power
system blackout and cascading events: Research motivations and challenges. *Energies*, 12:1–
28, 2019.
13. Y. Jia, Z. Y. Dong, C. Sun, and K. Meng. Cooperation-based distributed economic MPC for
economic load dispatch and load frequency control of interconnected power systems. IEEE
Transactions on Power Systems, 34:3964–3966, 2019.
14. R. Kumar and V. K. Sharma. Whale optimization controller for load frequency control of
a two-area multi-source deregulated power system. *International Journal of Fuzzy Systems*,
22:122–137, 2020.
15. P. S. Kundur and O. P. Malik. *Power System Stability and Control*. McGraw Hill, second
edition, 2022.
16. J. M. Maestre and R. R. Negenborn, editors. *Distributed Model Predictive Control Made Easy*.
Springer, 2014.
17. D. Q. Mayne, J. B. Rawlings, C. V. Rao, and P. O. M. Scokaert. Constrained model predictive
control: Stability and optimality. *Automatica*, 36:789–814, 2000.
18. A. Parisio, E. Rikos, and L. Glielmo. A model predictive control approach to microgrid
operation optimization. *IEEE Transactions on Control Systems Technology*, 22:1813–1827,
2014.
19. T. D. Raj, C. Kumar, P. Kotsampopoulos, and H. H. Fayek. Load frequency control in two-area
multi-source power system using bald eagle-sparrow search optimization tuned PID controller.
Energies, 16:1–25, 2023.
20. M. Ranjan and R. Shankar. A literature survey on load frequency control considering renewable
energy integration in power system: Recent trends and future prospects. Journal of Energy
Storage, 45:1–33, 2022.
21. A. Riccardi, L. Laurenti, and B. De Schutter. European economic area electricity network
benchmark,
https://doi.org/10.4121/90ada13d-a6c9-4e4c-a046-2b984595bcdd,
2023.
22. R. Sioshansi, P. Denholm, J. Arteaga, S. Awara, S. Bhattacharjee, A. Botterud, W. Cole, and
A. Cort´es et al. Energy-storage modeling: State-of-the-art and future research directions. IEEE
Transactions on Power Systems, 37:860–875, 2022.
23. E. Vlahakis, L. Dritsas, and G. Halikias. Distributed LQR design for a class of large-scale
multi-area power systems. *Energies*, 12:1–28, 2019.