# Multi-Agent Reinforcement Traffic Signal Control Based On Interpretable Influence Mechanism And Biased Relu Approximation

Zhiyue Luo , Jun Xu, Fanglin Chen

  Abstract—Traffic signal control is important in intelligent
transportation system, of which cooperative control is difficult
to realize but yet vital. Many methods model multi-intersection
traffic networks as grids and address the problem using multi-
agent reinforcement learning (RL). Despite these existing studies,
there is an opportunity to further enhance our understanding
of the connectivity and globality of the traffic networks by
capturing the spatiotemporal traffic information with efficient
neural networks in deep RL.
  In this paper, we propose a novel multi-agent actor-critic
framework based on an interpretable influence mechanism with a
centralized learning and decentralized execution method. Specif-
ically, we first construct an actor-critic framework, for which
the piecewise linear neural network (PWLNN), named biased
ReLU (BReLU), is used as the function approximator to obtain a
more accurate and theoretically grounded approximation. Then,
to model the relationships among agents in multi-intersection
scenarios, we introduce an interpretable influence mechanism
based on efficient hinging hyperplanes neural network (EHHNN),
which derives weights by ANOVA decomposition among agents
and extracts spatiotemporal dependencies of the traffic features.
Finally, our proposed framework is validated on two synthetic
traffic networks to coordinate signal control between intersec-
tions, achieving lower traffic delays across the entire traffic
network compared to state-of-the-art (SOTA) performance.

  Index
         Terms—Multi-agent
                            reinforcement
                                           learning,
                                                    biased
ReLU neural network, efficient hinging hyperplanes neural
network, traffic signal control.

I. INTRODUCTION
T
RANSPORTATION is the key driving force for economic and social growth and is one of the manifestations of urban competitiveness. With the rapid development of urbanization, traffic congestion has become a major challenge for cities around the world[1]. The increasing number of vehicles on the roads has led to longer travel times, increased fuel consumption, and higher levels of air pollution [2].

Traffic signal control is usually regarded as the most significant and effective method for quick and safe transportation, which reduces traffic congestion in the urban network by adjusting the signal phase at intersections[1]. Generally, traffic signal control methods can be mainly divided into This work was supported in part by the National Natural Science Foundation of China under Grant 62173113, and in part by the Science and Technology Innovation Committee of Shenzhen Municipality under Grant GXWD20231129101652001, and in part by Natural Science Foundation of Guangdong Province of China under Grant 2022A1515011584.(*Corresponding author: Jun Xu.*)
Zhiyue Luo, Jun Xu, and Fanglin Chen are with the School of Mechanical Engineering and Automation, Harbin Institute of Technology (Shenzhen), Shenzhen 518055, China (email: xujunqgy@hit.edu.cn).

three main types, including fixed time control[3], actuated control[4] and adaptive control[5],[6],[7]. However, neither fixed time control nor actuated control methods consider longterm traffic conditions, thus cannot optimize the traffic signal phases adaptively based on real-time traffic flow. In contrast, adaptive control can effectively mitigate traffic congestion and enhance transportation efficiency, which is currently a research hotspot. With the development of artificial intelligence, datadriven control methods play an increasingly important role in intelligent transportation systems. Traffic signal control is a sequential decision problem, which can be modeled as Markov Decision Process (MDP) and solved by reinforcement learning (RL). RL is a powerful dynamic control paradigm, making no additional assumptions on the underlying traffic transition model. Rather than computing explicit traffic flow dynamic equations, RL learns the optimal strategy based on its experience interacting with the traffic environment. The objective of traffic signal control is to minimize the total waiting time within the traffic network by controlling the phase of traffic signals at intersections.

Several RL methods have been applied to isolated traffic signal control [8], [9], [10], significantly impacting the field of traffic signal control problem. However, in real world, traffic networks are interrelated, and controlling a specific intersection signal will inevitably affect the traffic condition of the upstream and downstream intersections, leading to the chain reaction of the surrounding intersections. Multi-intersection traffic network is a complex and nonlinear system that can be quite challenging to model. The complexity arises from the need to process intricate spatiotemporal traffic flow data and address cooperative problems among agents, which are difficult to solve using a centralized approach. Consequently, many studies have explored the application of multi-agent RL (MARL) in cooperative traffic signal control problems. These studies aim to find a balance between centralized and decentralized training models, thus reaching an optimum strategy for all agents and minimizing the waiting time of vehicles within the traffic network. To explore further the spatial structural dependencies among different intersections, many researchers applied graph RL in multi-intersection traffic signal control, which uses graph neural networks to learn and exploits representations of each agent and its neighborhood in the form of node embedding.

Although the works mentioned above deal with the multiintersection traffic signal control problem through cooperative RL, the effect of coupled agents on the global performance of the traffic signal has yet to be considered explicitly. Hence, in this paper, we introduce a novel interpretable influence mechanism using efficient hinging hyperplanes neural networks (EHHNN) [11], which aims to capture the spatiotemporal dependencies of traffic information to better build the relationships among neighboring intersections. Then, we propose a multi-agent actor-critic framework with a centralized critic and decentralized actors. The main idea is to learn the critic using our interpretable influence mechanism to coordinate the interaction between different agents. Besides, we improve the function approximator used in the deep RL, which is a piecewise linear neural network (PWLNN), named biased ReLU (BReLU) neural network. This BReLU neural network can obtain superior performance than rectified linear units (ReLU) neural network in function approximation when reasonably dividing the piecewise linear (PWL) region [12].

We approximate both the value function and policy function with BReLU neural network, and thus construct the PWL- actor-critic framework. This also coincides with the conclusion that minimizing PWL functions over polyhedrons yields PWL solutions.

The technical contribution of this paper can be summarized as follows:

- A novel MARL framework is proposed, in which the
BReLU neural network is used as the approximator for both the value function and policy function to construct the PWL-actor-critic framework.
- We propose a novel influence mechanism using the
EHHNN and combine it with MARL. Compared to the graph-based approaches, our proposed mechanism does not require the pre-defined adjacency matrix of the traffic network and exhibits excellent capability in capturing the spatiotemporal dependencies of traffic flow data. Instead, it models the relationships by analyzing the impact of input variables on the output variables. Compared to the attention mechanism, the EHHNN-based influence mechanism has fewer parameters due to the sparsity of the EHHHNN and does not include a nonlinear activation function, which better explains the contribution of input features to a specific output variable. To the best of our knowledge, we are the first to use EHHNN to model multi-agent relationships and introduce a novel multiagent framework using EHHNN-based influence mechanism.
- Experiments are conducted on both the traffic grid and a
non-Euclidean traffic network. We compare the effectiveness of our solution with several state-of-the-art (SOTA) methods and further analyze the relation reasoning given by our influence mechanism.
The rest of this paper is organized as follows: Section II briefly introduces related work. Section III gives problem formulation of multi-intersection traffic signal control problem and models it as Partially-Observable MDP (POMDP). Section IV outlines the detailed implementations of our proposed multi-agent actor-critic framework, which is based on BReLU neural network approximation and employs a novel interpretable influence mechanism to learn the spatiotemporal dependency among different agents. Section V demonstrate the effectiveness of the EHHNN through traffic forecasting experiments, while also comparing our proposed multi-agent actor-critic framework with traditional fixed time control and SOTA MARL algorithm in two simulated environments of multi-intersection traffic signals control task. Finally, Section VI concludes the paper and outlines the main results.

## Ii. Related Work

In this section, we briefly introduce the related work of MARL and graph neural networks in traffic signal control. Additionally, we introduce the development of the EHHNN and its application.

## A. Deep Graph Convolutional Rl

In order to tackle the challenges of large-scale traffic signal control and address the issue of the curse of dimensionality in MARL, many studies have explored the application of MARL methods to traffic signal control problems, which includes approaches employing independent deep Q-network[13], [14], multi-agent deep deterministic policy gradient [15], multiagent advantage actor-critic [16], and large-scale decomposition method [17]. However, not all data in the real world can be represented as a sequence or a grid. To explore further the spatial structural dependencies among different intersections, many researchers applied graph RL in multi-intersection traffic signal control, which uses graph neural networks [18], [19], [20] to learn and exploits representations of each agent and its neighborhood in the form of node embedding. Then, researchers introduced structured perception and relational reasoning based on graph networks in MARL [21], [22], which aims to model the relationship in multi-agent scenarios. Following this line, graph-based RL methods have been used for traffic signal control to attain a deeper understanding of interactions among different intersections, e.g., graph convolutional network and graph attention network were applied in RL to process graph-structured traffic flow data [23], [24]. Several studies combined deep Q network method with graph neural networks [25], [26]. In another study, researchers introduced multi-agent advantage actor-critic algorithm to graph-based RL and proposed a decentralized graph-based method [27]. Furthermore, a spatiotemporal MARL framework was proposed, which considers the spatial dependency and temporal dependency of the traffic information [28].

## B. The Ehhnn

In deep RL, dealing with high-dimensional and intricate state spaces is a major challenge, so many studies use an effective function approximator to approximate the value function and policy function. Neural networks enable the integration of perception, decision-making, and execution phases, facilitating end-to-end learning. PWLNNs are now a successful mainstream method in deep learning, and ReLU is a commonly used activation function in PWLNNs. In typical neural networks, it is impossible to determine the contribution of different input variables to the output through neuron connections. Therefore, in the multi-agent cooperative control tasks, researchers have introduced methods incorporating attention mechanism and relational inductive biases to determine the weights of various input features through similarity measurement. However, we aspire to capture the influence of the inputs on outputs directly through an interpretable neural network.

In 2020, a novel neural network called EHHNN was proposed [11], which strikes a good balance between model flexibility and interpretability. The EHHNN is a kind of PWLNN derived from the hinging hyperplanes (HH) model [29], in which the ReLU neural network is a kind of the HH model [12]. When the HH model involves only one linear hyperplane passing through the origin, it becomes a ReLU neural network. The EHHNN exhibits a high flexibility in dynamic system identification due to its PWL characteristics. Furthermore, the network is interpretable, allowing for determining the impact of the input layer and hidden layer neurons on the output through the analysis of variance (ANOVA) [30], thereby facilitating the analysis of feature variables. In 2021, a new activation function called BReLU is proposed [12], which is similar to the ReLU. The BReLU neural network is also an HH model, i.e. a PWL function. Compared with ReLU, it employs multiple bias parameters, which can partition the input spaces into numbers of linear regions, thus resulting in high flexibility and excellent approximation capabilities, especially in regression problems.

## Iii. Marl For Traffic Control Problem

In multi-intersection traffic signal control problems, each signal controller reduces the traffic flow at the intersection by adjusting the phase to minimize the waiting time of the traffic flow in the whole traffic network. In this section, we first model an unstructured multi-intersection traffic network as a directed graph and give the formulation and assumptions used in the optimization problem. Then, we model the multiintersection traffic signal control as a MDP and give a detailed formulation of the state, action, and reward function.

## A. Traffic Signal Control Problem Formulation

We consider a more general traffic network, as shown in Fig. 1. For the urban traffic network may not be necessarily connected due to the limitation of the area for urban development [31]. Similar to related work [13],[25],[32], the typical intersection shapes are included in the traffic network, as shown in Fig. 1, v3 and v5 are three-way intersections, while others are crossroads. Besides, the length of lanes in the traffic network varies. We define intersections in the traffic network as nodes and the road between every two intersections as edges, then the multi-intersection traffic network can be modeled as a directed graph G(*V, E,* Ψ), where V = {vi}|V |
i=1
is the nodes set, |V | = N, refers N nodes (intersections) in the graph. E = {ej}|E|
j=1 is the edges set, |E| is the number of edges and there are lj lanes on the j-th edge. For each edge ej, there is a corresponding upstream node uj ∈ V and downstream node dj ∈ V . Ψ represents the global attribute of the traffic graph.

Before describing the traffic dynamic system, we make three reasonable assumptions.

Assumption 1: To simplify the large-scale traffic problem, we assume that the sampling time intervals ∆t of all intersections are the same, then the cycle time can be expressed as

$$T=k\cdot\Delta t\tag{1}$$
Assumption 2: We assume that the vehicles from upstream node uj entering edge ej will travel freely until they reach the tail of the waiting vehicle queues. And they will be divided to join the separated queues of the downstream node dj that they intend to go to.

Assumption 3: We assume that each intersection block is equipped with an individual roadside unit, which can observe and collect the traffic information and transmit it to the central controller.

Now, the dynamic traffic model can be derived as follows.

According to the vehicle conservation theorem, the number of vehicles on edge ej at step k is updated by

$$n_{j}(k+1)=n_{j}(k)+\left(I_{u_{j},d_{j}}-O_{d_{j},v}\right),v\in\mathcal{N}_{d_{j}}-\left\{u_{j}\right\}\tag{2}$$

where $I_{u_{j},d_{j}}$ denotes the traffic flow entering edge $e_{j}$, while $O_{v,u_{j}}$ denotes the traffic flow leaving edge $e_{j}$ reaching its next adjacent target node $v$, $\mathcal{N}_{d_{j}}$ represents the adjacent nodes of the downstream node $d_{j}$.

And consequently, we can update the density of the $j$-th edge from node $u_{j}$ to node $d_{j}$ at time $k$ as

$$\Phi_{u_{j},d_{j}}=\min\left(1,\frac{n_{j}(k)\cdot\tau}{L(e_{j})}\right)\tag{3}$$
where τ is a constant representing the vehicular gap and L(ej)
denotes the length of edge j.

The queue length quj,dj(k) is the number of vehicles waiting on edge ej at step k, which is the number of vehicles on edge ej with a speed of 0. And the total queue length at intersection i can be expressed as

$$Q_{i}(k)=\sum q_{u_{j},v_{i}}(k),u_{j}\in\mathcal{N}_{v_{i}}\tag{4}$$

The total vehicle waiting time at the intersection $i$ at step $k$ is denoted as $W_{i}(k)$.

Our objective is to minimize the total waiting queue of the global traffic network by controlling the phase of the intersection signals

$$Z^{*}=\min\sum_{k=0}^{T/\Delta t}\sum_{i=1}^{N}Q_{i}(k)\tag{5}$$

## B. Multi-Intersection Traffic Signal Control As Mdp

Due to the uncertainty and dynamics of the traffic system, the multi-intersection traffic signal control problem can be abstracted as a discrete stochastic control problem, and be modeled as POMDP, defined as a tuple ⟨O, A, R*, N, γ*⟩, where O
= {o1, o2*, . . . , o*N} is the set of observations, A =
{a1, a2*, . . . , a*N} is the set of actions, R = {r1, r2, . . . , rN}
is the set of reward, and N is the number of agents, also the number of intersections and the number of nodes in the graph G.

The observation of each agent i is defined as the vector of neighborhood queue length quj,vi of intersection vi, phase of current intersection signal ρ, and road density Φuj,vi, which can well represent the incoming traffic flow on the road and the queue numbers at the intersection. For agent i with uj ∈ Nvj neighboring intersection, the local observation at step k is

$$o_{i}(k)=[\rho_{i}(k),q_{u_{j},v_{i}}(k),\Phi_{u_{j},v_{i}}(k)],u_{j}\in\mathcal{N}_{v_{i}}\tag{6}$$
The joint state over the traffic network is expressed as S =
o1 × o2 × *. . . o*N.

Each intersection has a separate controller giving its signal
(or action). At each time step k, the controller of intersection i selects a discrete action, denoted as ai(k) *∈ A*i. The joint action grows exponentially with the number of agents. We consider only feasible sign configurations in the action set and use a four-stage green phase control.

In traffic signal control, researchers often use characteristic variables such as the total waiting time and the queue length of vehicles to define the reward function. Many studies use expressions such as Eq. (7) to define reward function, which uses changes in traffic characteristic variables Xtcv between adjacent time step.

$r_{tcv}(k)=X_{tcv}(k-1)-X_{tcv}(k)$ (7)
Using the expression above, agents tend to accumulate a certain amount of vehicles at the intersection and then release them to obtain larger rewards. This control strategy obviously does not conform to the real-world traffic application scenario. Therefore, in this paper, we propose an improved reward function based on Eq. (7). Considering the characteristics of largescale traffic network and the optimization objective of traffic control, the new reward function is shown in Eq. (8), where κ1,
κ2 and κ3 are hyperparameters of the reward function under different traffic conditions, ∆Qi(k) = Qi(k) − Qi(k − 1) is the changes in queue number between adjacent time step.

$$r_{i}(k)=\left\{\begin{array}{ll}\kappa_{1},&Q_{i}(k)=0\\ -W_{i}(k)/\kappa_{2},&\Delta Q_{i}(k)>0\\ -\kappa_{3}\cdot\Delta Q_{i}(k),&\Delta Q_{i}(k)\leq0\end{array}\right.\tag{8}$$
The global reward on the whole traffic network is a linear weighted sum of reward ri for each agent

$$r(k)=\sum_{i=1}^{N}r_{i}(k)\tag{9}$$

## Iv. Multi-Agent Brelu Actor-Critic With Interpretable Influence Mechanism

In this section, we propose a multi-agent BReLU actorcritic framework with an interpretable influence mechanism. We introduce a novel neural network called BReLU neural network, which offers improved function approximation for RL and constructs a PWL-actor-critic framework. Then, we extend the PWL-actor-critic framework to the MARL algorithm and employ the interpretable influence mechanism based on EHHNN to capture the spatiotemporal dependencies among different agents. We use a centralized training and decentralized execution method, where a joint value function is learned from the aggregated information and each actor learns its policy function based on the local observations.

## A. Overview

The overview framework of our proposed method is shown in Fig. 2. We first build a graph that comprises traffic signal agents and subsequently propose a novel influence mechanism to extract the spatial dependencies from the input graph. In detail, the observations of each agent
�
oi k
�N
i=1 go through a node embedding layer and the EHH-based mechanism to obtain the node embedding V in k for the actor layer and the aggregation embedding for the critic layer, respectively. The module inside the influence mechanism is shown on the righthand side of Fig. 2, the observations
�
oi k
�N
i=1 is fed into a linear transformation layer followed by an EHHNN to obtain the hidden variable Hk, then an ANOVA decomposition layer is designed for feature extraction to obtain the important coefficient σm. Finally, the aggregation embedding V out k is obtained through weighted aggregation. We approximate the policy function and value function in the actor-critic layers with a novel neural network named BReLU and thus construct a PWL-actor-critic framework. Next, we will provide a detailed description of each module within the proposed framework.

## B. Node Embedding

Firstly, we obtain the node embedding V in
                                       k
                                          =
                                             �
                                               vin
                                                i,k
                                                  �N

                                                                                    i=1
at the current time step k according to the neighboring edge
information of intersection vi, i.e. agent i. As mentioned in
Section III, each traffic intersection represents a node, and the
node and edge features in the graph network can be repre-
sented by the variables in the MDP. The traffic information
collected by edge ej at time k is defined the same as the
value of the local observation
                                            �
                                              oi
                                                k
                                                 �N
                                                   i=1 in the MDP

ej(k) = � ρdj(k), quj,dj(k), Φuj,dj(k) � , (10)
where uj and dj is the upstream node and downstream node of edge ej, respectly. The traffic information of edge ej can represent the interplay among agents, which offers a more comprehensive understanding of how upstream and downstream traffic flow effects propagate between adjacent intersections. Then, the node embedding can be expressed as the aggregation of its adjacent edges traffic information

vin
 i,k = f e→v (ej(k)) = f e→v �
                         euj,vi(k)
                                 �
                                  , uj ∈ Nvi
                                             (11)

where f e→v is a one-layer MultiLayer Perception (MLP) with the ReLU activation function.

## C. Interpretable Influence Mechanism Based On Ehhnn

The traffic model is a nonlinear system, which is challenging to model for its complex spatiotemporal traffic flow data. Therefore, establishing an interpretable influence mechanism and extracting the impact of neighboring traffic information can enhance collaborative control among different intersections. The EHHNN was first applied in short-term traffic flow prediction in 2022, which figured out the spatiotemporal factors influencing the traffic flow using ANOVA decomposition [33]. Compared with this work, we further explore the application of EHHNN in large-scale multi-intersection control problem. We propose an influence mechanism based on EHHNN, which can not only capture the spatiotemporal dependencies of traffic flow data, but also illustrate the relation representation among different agents, enabling multiagent cooperative control. The structure of our proposed interpretable influence mechanism module is shown in the blue box in Fig. 2.

� Firstly, we reduce the dimension of the local observation oi k
�N
i=1 through a linear transformation layer W to obtain the input variable Xin k for the EHH layer. Unlike other neural networks, the EHHNN possesses interpretability, allowing us to extract the interactions among different input variables through ANOVA decomposition and an interaction matrix. The hidden layer in EHHNN can be seen as a directed acyclic graph, as shown in the yellow box in Fig. 2. All nodes in the

directed acyclic graph contribute to the output, including two types of neurons, source nodes D and intermediate nodes C. In the EHHNN, the output of source nodes can be described as: z1,s = max {0, xm − βm,qm} (12)
where m represents the dimension of the input variable, and
βm,qm represents the qm-th bias parameters on the input variable xm.

In the hidden layer of the EHHNN, the intermediate nodes are obtained by minimizing existing neurons of the previous layers, which comes from different input dimension

zp,s = min nns1,...,nnsp∈Jp,s � max � 0, xnns1 − βs1 � , . . . max � 0, xnnsp − βsp � � (13)
where we define Jp,s =
�
nns1, . . . , nnsp
�
contains the indices of neurons generated by previous layers, and |Jp,s| = p, which represents the number of interacting neurons of the p-th layer.

Finally, the output of the EHHNN Hk = {hi,k}N
i=1 is the weighted sum of all neurons in the hidden layer:

Hk = α0 + s=1 α1,sz1,s(˜x) + p=2 s=1 αp,szp,s(˜x) (14) n1 � P � np �
where α1,s, αp,s are the weight of the EHHNN and α0 is the constant bias, ˜x = Xin k , n1 and np denotes the number of neurons in the 1-th and p-th layer, respectively.

In this paper, we employ a two-factor analysis of variance
(ANOVA) to determine the main effect of different traffic flow information as individual factors, as well as the interaction effect of bivariate factors on intersection congestion, i.e. P = 2
in Eq. (14). The first sum represents the influence of individual variables, the second sum represents the joint influence of two variables when P = 2. This characteristic of the EHHNN
provides insights into how different variables contribute to the overall prediction and facilitates a deeper understanding of the underlying relationships within the data. Similar to the related work in [30], [11] and [33], we can identify the hidden nodes that influence each output component in the ANOVA decomposition, which is calculated by

$$\sigma_{m}=\sqrt{\text{VAR}(f_{m}(\tilde{x}))}$$ $$f_{m}(\tilde{x})=\sum_{J_{p,s}=\{m\}}\alpha_{p,s}z_{p,s}(\tilde{x})\tag{15}$$
where VAR(·) denotes the corresponding variance of the prediction output related to the m-th component of input variable ˜x. The larger the value of σm, the greater the impact of its corresponding input variable on the degree of congestion of the traffic network.

Remark 1. Due to the physical connection between traffic data and road networks, many researchers employ relational reasoning through graph-based methods or attention mechanism. However, the graph-based methods require a predefined and fixed adjacency matrix to reflect the spatial dependencies of different nodes, which may not effectively capture the spatiotemporal dependencies in the dynamic traffic flow data. The attention mechanism computes the attention coefficient by performing the dot products for all input vectors and utilizes a nonlinear activation function, making it challenging to interpret the relationships between learned weights. Furthermore, most traditional neural networks lack interpretability, making it challenging to select and analyze the input variables while accurately predicting the complex spatiotemporal traffic flow. The EHHNN can meet the requirements above, which employs a unique network structure to capture spatiotemporal dependencies from the input data. It has fewer parameters due to the sparsity of the network structure and can extract the influence coefficients derived from ANOVA decomposition without knowing the node connectivity of the data, as illustrated in the framework shown in Fig. 3.

While achieving precise prediction, it processes interpretability through ANOVA decomposition, which obtains the important coefficients of the hidden variables σm as mentioned in Eq. (15). Additionally, since there is no nonlinear activation function after the linear transformation layer, the importance coefficients of input variables can be derived through inverse transformation:

$$\sigma_{i n}=W^{-1}\sigma_{m}\tag{16}$$

  Finally, we derive the aggregation embedding V out
                                                k
                                                     =
�
 vout
  i,k
     �N

sectionsi=1, which aggregates information from other inter-
                     vout
                       i,k =
                             �
                                 σmvin
                                      i,k
                                                          (17)

where vin
      i,k is the node embedding.
  This output graph V out
                   k
                      , which extracts the spatiotemporal
features through ANOVA decomposition of EHHNN, is used
as the input of the centralized critic to learn a joint value
function and faciliate collaboration among different agents.
While in decentralized execution, each actor learns its policy
function based on the locally observed embedding vector V in
                                                k .

D. Actor-Critic Framework based on BReLU neural network
approximation

The RL optimization problem is to obtain the optimal strategy $\mu^{*}=\{u_{0},u_{1},\dots\}$ that satisfies the constraints, while maximizing the total reward, which can be written as

$$\tilde{V}_{k+1}(x)=\max_{u\in\pi(x)}E\left\{g(x,u,w)+\gamma\tilde{V}_{k}(f(x,u,w))\right\}\tag{18}$$

where $x$ denotes the state, $w$ is a random disturbance with a probability distribution $P(\cdot|x,u)$, $\tilde{V}$ is the value function, $\pi$ denotes the policy function, $g(x,u,w)$ is the cost per step, $\gamma$ is the discount factor.

Lemma 1. When the value function ˜V is a PWL function, the policy function π is also a PWL function.

Proof.: According to the Bellman's equation, we have

$$\tilde{V}^{*}(x)=\max_{u\in\pi^{*}(x)}E\left\{g(x,u,w)+\gamma\tilde{V}^{*}(f(x,u,w))\right\}\tag{19}$$

this equation can be view as the limit as $k\rightarrow\infty$ of Eq. (18). Then the optimal strategy can be derived as

$$\mu^{*}=\arg\max E\left\{g(x,u,w)+\gamma\tilde{V}^{*}(f(x,u,w))\right\}\tag{20}$$ $$u\in\pi(x)$$
The cost function in Eq. (20) is g(*x, u, w*) + γ ˜V (f(*x, u, w*)), while g(*x, u, w*) is aslo known as the reward function in RL. In this paper, the reward function as shown in Eq. (8) is a PWL function with respect to state x. If the value function ˜V
is a PWL function, the cost function is the sum of two PWL functions, which is also a PWL function. It has been proved by bemporad in 2002 [34] that minimizing or maximizing a PWL cost function ˜V over a polyhedron yields a PWL solution
π. Therefore, if we approximate the value function ˜V using a PWLNN, the policy function π should also be a PWL solution, as stated in the conclusion above.

To align with the conclusion obtained from Lemma 1, we employ PWL neural networks to approximate the value function and policy function in actor-critic. The activation function plays an important role in neural network approximation, in which the ReLU activation function is prevalent in neural networks due to its simplicity and computation efficiency, and it can be defined as:

$\mathbb{Z}(x)=\max\left\{0,x\right\}$ (21)
where x = [x1, x2, . . . , xn]T
∈ R. The prevalent ReLU
network is a kind of HH neural network [12].

Based on ReLU neural network, in 2021, Liang and Xu [12]
proposed BReLU neural network, which can be expressed as:

$$z(x)=\max\left\{0,x_{i}-\beta_{i_{1}}\right\},\ldots,\max\left\{0,x_{i}-\beta_{i_{q_{i}}}\right\}\tag{22}$$

where $q$ represents the number of linear regions in each dimension of the input data.

Different from ReLU neuron, BReLU uses different bias parameters $\beta_{i_{q_{i}}}$ for variables in various dimensions, thereby partitioning the input spaces into a number of linear regions and take advantage of the characteristics of PWL functions. The input variables after normalization follow an approximately normal distribution, and the multiple bias parameters $\beta_{i_{q_{i}}}$ are determined by the distribution of the input data:

$$\beta_{i_{q_{i}}}=[-3\nu,-0.824\nu,-0.248\nu,0.248\nu,0.834\nu]+\eta\tag{23}$$
where the parameter *ν, η* represent the variance and expectation of input variable after normalization, respectly. qi is the number of bias parameters of the i-th layer and also represents the number of linear sub-regions. The selection of the value qi is a trade-off between network accuracy and the number of parameters. And the weights in BReLU neural network are obtained using the backpropagation method.

The BReLU neural network demonstrates higher flexibility and better approximation capabilities by effectively dividing the input spaces into numbers of linear regions, even when the output increases exponentially with the input. Therefore, we approximate the value function ˜V and policy function π
in the actor-critic framework using BReLU neural network, where the functions approximated by BReLU neural network are PWL. The reason for doing this is two-fold. First, it coincides with the conclusion that minimizing (maximizing) PWL functions over polyhedron yields PWL solutions. Second, the approximation of the value function and policy functions using BReLU neural network provides a more precise approximation than that of ReLU. The red box in Fig. 2 shows the structure of the BReLU neural network used in the proposed PWL-actorcritic framework.

Different from independent proximal policy optimization
(IPPO)[35], which lacks collaboration among agents, in our proposed multi-agent actor-critic algorithm, all critics are updated together to minimize a joint regression loss function as shown in Eq. (24), where the joint value function remains a PWL function. And ˆAi represents the advantage function, which is estimated by the truncated version of the generalized advantage estimation [36], Nb denotes the training batch size, b′ is an arbitrary sampling sequence after sample b, γ is the discount factor, λ is the regularization parameters and W is the weight of the neural network that approximates the value function ˜V .

$$L(\phi)=-\sum_{i=1}^{N}\sum_{b=1}^{N_{b}}(\hat{A}_{i}(b))^{2}+\lambda\left\|W\right\|_{1}\tag{24}$$ $$\hat{A}_{i}(b)=\sum_{b^{\prime}>b}\gamma^{b^{\prime}-b}r_{i}(b^{\prime})-\tilde{V}(v_{i,b}^{out})$$
Each decentralized actor updates its policy function only based on its local observations, which is updated using the proximal policy optimization method. And a clip function is used to limit the range of changes in the probability ratio rt(*θ, b*) of old and new strategies πi,θ−, πi,θ to avoid large variance changes and unstable training.

$$L_{i}(\theta)=\sum_{b=1}^{N_{b}}\min\left(r_{t}(\theta,b),\text{clip}\left(r_{t}(\theta,b),1-\epsilon,1+\epsilon)\right)\cdot\hat{A}_{i}(b)\right.$$ $$\left.r_{t}(\theta,b)=\frac{\pi_{i,\theta}(a_{b}|v_{i,b}^{in})}{\pi_{i,\theta^{-}}(a_{b}|v_{i,b}^{in})}\right.\tag{25}$$

where

To give an overview of the proposed multi-agent algorithm, we now summarize it in Algorithm 1 and briefly introduce the training process. During a total of $N_{ep}$ episodes, each lasting for a duration of $T$ in the training process, we store the transition $\left\{(o_{i}(k),a_{i}(k),o_{i}(k+1),r_{i}(k))\right\}_{i=1}^{N}$ into the memory buffer $\mathcal{M}$. When the recorded data exceeds the batch size $N_{b}$, we use the pre-trained EHHNN to compute the importance coefficients of the input features and update both the actor and critic network with constant learning rate.

## Algorithm 1 Multi-Agent Brelu Actor-Critic Framework

Input: A pre-trained EHHNN
Output: actor θi for i ∈ N, critic ϕ
1: Initialization: actor θi ← 0 and critic ϕi ← 0 for i ∈ N;
2: **for** ep = 1*, . . . , N*ep do
3:
for k = 1*, . . . , T/*∆t do
4:
Reset the environment, oi(k), M = ∅
5:
Sample ai(k) from πi(k)
6:
receive ri(k) (8) and oi(k + 1)
7:
end for
8:
Store transitions M ← M ∪ [oi(k), ai(k), ri(k)]N
i=1
9:
if N(M) *> N*b then
10:
Compute σ using the pre-trained EHHNN (15)
11:
Compute the aggregated result vout
i,k using (17)
12:
for i = 1*, . . . , N* do
13:
Calculate the advantage function ˆAi(b) (25)
14:
Update the actor θi by minimizing Li(θ) (25)
15:
end for
16:
Update the global critic ϕ by minimizing L(ϕ) (24)
17:
end if
18: end for

## V. Simulation Results

In this section, we evaluate our proposed method using the SUMO traffic simulator [37]. Firstly, we employ traffic data of Los Angeles country (METR-LA) dataset [38] for traffic forecasting, comparing existing attention mechanism and analyzing the effectiveness of the proposed interpretable influence mechanism based on EHHNN. Compared with the work in [33], we conduct the result on a different dataset and validate the performance of EHHNN on a much larger traffic network. Subsequently, we conduct both quantitative and qualitative experiments for multi-intersection traffic signal control on two synthetic traffic networks, and compare it to the traditional fixed time control method and the SOTA MARL controllers.

## A. Traffic Forecasting

1) Dataset Description: To validate the effectiveness and interpretability of the proposed influence mechanism, we conduct experiments on the METR-LA dataset . The METR-LA dataset consists of traffic data collected from circular detectors on highways in Los Angeles Country, comprising a total of 207 sensors. For our experiments, we selecte 15 adjacent nodes, as illustrated in Fig. 4. We evaluate the forecasting performance of the EHHNN compared with four baseline neural networks. Furthermore, we conducte the interpretability analysis of the EHH network to facilitate a deeper understanding of the underlying relationships between different nodes.

For the traffic data in METR-LA dataset, information is collected every 5 minutes, with an observation window of 60 minutes and a maximum prediction horizon of 45 minutes. We split the dataset into three distinct sets, including a training set, a validation set and a test set, with the training set accounting for 60% of the total samples, and the remaining 40% each allocated to the validation and test sets.

2) Measures of effectiveness: To evaluate the accuracy of different forecasting models, we employ three measures of effectiveness, including mean absolute error (MAE), R2
value[39] and root mean square error (RMSE):

$$\text{MAE}=\frac{1}{N\cdot T}\sum_{i=1}^{N}\sum_{t=1}^{T}|(x_{i,t}-\hat{x}_{i,t})|$$ $$\text{R}^{2}=1-\sum_{i=1}^{N}\sum_{t=1}^{T}(x_{i,t}-\hat{x}_{i,t})^{2}/\sum_{i=1}^{N}\sum_{t=1}^{T}(x_{i,t}-\bar{x})^{2}$$ $$\text{RMSE}=\sqrt{\frac{1}{N\cdot T}\sum_{i=1}^{N}\sum_{t=1}^{T}(x_{i,t}-\hat{x}_{i,t})^{2}}\tag{26}$$

where $N$ denotes the number of predicted nodes of METR-LA dataset, $T$ denotes the historical time window for prediction, $x_{i,t}$ is the input traffic flow data of the $i$-th node at time $t$, and $\bar{x}$ represents the mean value of the input traffic flow data $x_{i,t}$.

_3) Experimental Settings:_ All experiments are compiled and tested on Linux cluster (CPU: Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz GPU:NVIDIA GeForce RTX 3090). The EHHNN is a single hidden layer neural network. In the traffic forecasting experiments of this section, our model initially reduces the input dimension through a linear transformation layer. Then, the hidden variables after dimension 
reduction are fed into the EHHNN, which outputs the prediction results. Our proposed model is effectively a two-layer shallow neural network. Therefore, we compare it with three other shallow networks, including a two-layer fully connected (FC) neural network, a FC long short-term memory (FC- LSTM) neural network, and graph attention neural network
(GAT). Besides, we compared the EHHNN with a SOTA method in traffic forecasting, which is a deep network called Spatial-Temporal Graph Convolutional Network (STGCN). All models utilized the same training parameters, undergoing 300 epochs of training on the training set, employing a variable learning rate optimizer. Subsequently, the optimal parameters of the model were determined through performance evaluation on the validation set. Finally, the models were evaluated on the test set. All tests were conducted with a historical time window of 60 minutes, i.e. 12 sampling points, for predicting the traffic condition in the subsequent 15, 30, and 45 minutes.

4) Experiment Results: Table I demonstrates the results of EHHNN and baselines on the dataset METR-LA. Compared with the three shallow networks, the EHHNN achieved the best performance. In comparison with the STGCN deep network, our model outperformed in both RMSE and R2 metrics, indicating better fitting to large errors and overall predictions that better align with the actual trends in values.

Besides, due to the sparse connectivity and the neuronsconnected structure of the EHHNN, it can achieve superior prediction accuracy with fewer training parameters. The number of hidden layer neurons significantly impacts the performance and capability of a neural network. Increasing the number of hidden layer neurons enhances the expressive ability and complexity of the neural network. However, in a FC network, adding neurons implies increasing training parameters, leading to longer training times and heightened demands on computational resources. Compared with the FC network, FC-LSTM network, the EHHNN requires fewer training parameters when having the same number of hidden neurons.

## B. Multi-Intersection Traffic Signal Control

After evaluating the effectiveness and interpretability of the EHHNN in traffic forecasting, in this section, we apply the proposed influence mechanism based on EHHNN to the multiintersection traffic signal control problem, and evaluate the algorithm on two different synthetic traffic networks.

1) Traffic Signal Control using Synthetic Traffic Networks:
We evaluate our proposed method on two synthetic traffic networks, including a 5×5 traffic grid and a non-Euclidean traffic network, as shown in Fig. 5. The details are introduced as follows:

- Network5×5: A 5 × 5 traffic grid with three bidirectional
lanes in four directions at each intersection. The road length is 100m, and the lane speed limit is 13.89m/s. There are approximately 930 vehicles generated and added to the network per episode.
- Network*NonE*: An non-Euclidean traffic network with 8
intersections. The intersections are not connected in a grid-like pattern, and the length of roads varies between

Model
(15/30/60 min)
MAE ↓
R2 ↓
RMSE ↑
Params
Neurons
2-layers FC
8.26949/8.42299/8.70810
0.08866/0.07988/0.06103
19.86146/19.96055/20.17158
26029/28954/34804
64
FC-LSTM
4.01271/4.63315/5.66560
0.77434/0.72570/0.64237
9.78062/10.85584/12.69706
59181/93786/162996
64
GAT
5.30224/6.01932/6.77592
0.79210/0.71892/0.63816
9.48623/11.03227/12.52191
14339/15878/18956
64
STGCN
2.83072/ 3.61224/4.60460
0.83381/0.74521/0.64770
8.48147/10.50363/12.35573
96767/97154/97928
960
EHHNN
3.35360/4.21736/5.24809
0.84352/0.77446/0.66847
8.22992/9.88232/11.98600
42763/62293/101353
370

75m to 150m. There are 10 external road inputs, and approximately 250 vehicles are generated and added to the network per episode. We designed this network for the various buliding areas of the cities, as described in Subsection III-A.

2) Evaluation Metric: To quantitatively measure the condition of the traffic network, we define two metrics, as shown in Eq. (27) and Eq. (28). The average waiting time (AVE) is used to measure the overall congestion degree of the traffic network, while the traffic flow stability (STA) indicates the frequency of local vehicle accumulation that appears during the simulation time.

$$\text{AVE}=\frac{1}{T_{s}}\sum_{t=0}^{T_{s}}\sum_{i=1}^{N}W_{i}(t)\tag{27}$$

$$\text{STA}=\frac{1}{T_{s}}\sum_{t=0}^{T_{s}}\left[\sum_{i=1}^{N}W_{i}(t)-E\right]^{2}\tag{28}$$

where $T_{s}$ denotes the simulation time, $N$ denotes the number of intersections, i.e., agents.

_3) Methods Compared with:_ To evaluate the effectiveness of our proposed algorithm, we compare it with serval SOTA traffic signal control methods, including both traditional approach and RL methods.

- Fixed time control: a pre-defined rule-based traffic control
method, which uses a four-stage phase sequence control.
- Independent Deep Q Network (IDQN): a decentralized
method where each agent learns a Q network to maximize its reward independently without interacting with each other.
- Multi-Agent Deep deterministic Policy Gradient (MAD-
DPG): each agent learns a deterministic policy, and this method takes into account the interaction between different agents by sharing the experience pool and employing collaborative training methods.
- Independent Proximal Policy Optimization (IPPO): a
decentralized actor-critic-based method where each agent learns a truncated advantage function and a policy function to improve performance.
- Graph Convolution RL (DGN): a standard graph-based
RL method that uses graph convolution neural network and self-attention mechanism to extract the traffic feature, thereby learning the Q-values of the agents.
4) Simulation Settings: The simulation runs T = 2500s
per episode, and the traffic signal controllers update every ∆t = 5s. To ensure the safety at the intersection, we set the yellow phase to 2s, the minimum and maximum green time
gmin, gmax to 5s and 50s, respectively.
In the fixed time control, we set the green phase for each
traffic signal controller as 25s. And for all RL methods, we use the same training parameters. All methods are trained for 100 episodes, Table II shows the hyperparameters settings of the reward function in MDP and Algotithm 1.

| Variable                        |
|---------------------------------|
| extra reward                    |
| κ                               |
| 1                               |
| 25                              |
| reduce congestion parameter     |
| κ                               |
| 2                               |
| 5                               |
| increase congestion parameter   |
| κ                               |
| 3                               |
| 5                               |
| Q network learning rata         |
| α                               |
| Q                               |
| 0.01                            |
| critic learning rate            |
| ι                               |
| c                               |
| 0.01                            |
| actor learning rate             |
| ι                               |
| A                               |
| 0.001                           |
| hyperparameter of clip function |
| ϵ                               |
| 0.2                             |
| minibatch size                  |
| N                               |
| b                               |
| 32                              |

5) Experimental Results:
We compare our proposed method with the baseline methods on both the 5×5 traffic grid and non-Euclidean traffic network. Fig. 6 shows the comparison results of our proposed method and all the baseline algorithms on a 5×5 traffic grid. It is evident that, under the current parameter settings, the IDQN and MADDPG methods fail to alleviate traffic congestion, as shown in Fig. 6(b) that the reward of IDQN and MADDPG have been negative per episode. After excluding these two algorithms, as shown in Fig. 6, our proposed algorithm achieves similar performance to the two SOTA algorithm IPPO, DGN. Besides, compared to fixed time control, IDQN, MADDPG, our proposed mehtod achieves reduce the congestion on the traffic network.

Subsequently, as illustrated in Fig. 7, we conduct the results on an non-Euclidean traffic network. Our proposed algorithm exhibits better performance than IPPO, DGN and fixed time control method, and achieves reduced delay and smoother traffic flow conditions compared to other methods. Meanwhile, we conduct an ablation experiment, revealing that the performance obtained using reward function Eq. (7) is inferior to that achieved using the reward function proposed in this paper.

## Vi. Conclusion

In this paper, we have introduced a novel multi-agent actorcritic framework with an interpretable influence mechanism based on the EHHNN. Specifically, we used the BReLU neural network as a function approximator for both the value and policy functions and thus construct the PWL-actor-critic framework. Besides, the proposed influence mechanism based on the EHHNN can capture the spatiotemporal dependencies in traffic information without knowing the pre-defined adjacency matrix. The importance of the input variables using ANOVA decomposition of EHHNN, providing a deeper understanding of the underlying relationships within the data. Moreover, the approximation of the global value function and local policy functions using BReLU neural network not only provides a more precise approximation but also coincides with the conclusion that minimizing PWL functions over polyhedron yields PWL solutions. Simulation experiments on both the synthetic traffic grid and non-Euclidean traffic network demonstrate the effectiveness of the proposed multiagent actor-critic framework, which can effectively extract important information and coordinate signal control across different intersections, resulting in lower delays in the whole traffic network.

## References

[1]
D. Zhao, Y. Dai, and Z. Zhang. "Computational intelligence in urban traffic signal control: A survey". In: IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 42.4 (2011),
pp. 485–494.
[2]
S. Gupta, A. Hamzin, and A. Degbelo. "A low-cost open
hardware system for collecting traffic data using Wi-Fi signal strength". In: *Sensors* 18.11 (2018), p. 3623.
[3]
A. J. Miller. "Settings for fixed-cycle traffic signals".
In: *Journal of the Operational Research Society* 14.4 (1963), pp. 373–386.
[4]
S.-B. Cools, C. Gershenson, and B. D'Hooghe. "Selforganizing traffic lights: A realistic simulation". In: Advances in applied self-organizing systems (2013),
pp. 45–55.
[5]
P. Mannion, J. Duggan, and E. Howley. "An experimental review of reinforcement learning algorithms for adaptive traffic signal control". In: Autonomic road Transport Support Systems (2016), pp. 47–66.
[6]
A. Haydari and Y. Yılmaz. "Deep reinforcement learning for intelligent transportation systems: A survey".
In: IEEE Transactions on Intelligent Transportation Systems 23.1 (2020), pp. 11–32.
[7]
B. Abdulhai, R. Pringle, and G. J. Karakoulas. "Reinforcement learning for true adaptive traffic signal control". In: *Journal of Transportation Engineering* 129.3 (2003), pp. 278–285.
[8]
W. Genders and S. Razavi. "Using a deep reinforcement
learning agent for traffic signal control". In: arXiv
preprint arXiv:1611.01142 (2016).
[9]
E. Van Der Pol. "Deep reinforcement learning for
coordination in traffic light control". In: Master's thesis,
University of Amsterdam (2016).
[10]
K. Behrendt, L. Novak, and R. Botros. "A deep learning approach to traffic lights: Detection, tracking, and classification". In: 2017 IEEE International Conference on Robotics and Automation (ICRA). IEEE. 2017, pp. 1370–1377.
national Conference on Computer and Communication
Systems (ICCCS). IEEE. 2021, pp. 645–650.
[28]
Y. Wang, T. Xu, X. Niu, et al. "STMARL: A spatiotemporal multi-agent reinforcement learning approach for cooperative traffic light control". In: IEEE Transactions on Mobile Computing 21.6 (2020), pp. 2228–2242.
[29]
L. Breiman. "Hinging hyperplanes for regression, classification, and function approximation". In: IEEE Transactions on Information Theory 39.3 (1993), pp. 999– 1013.
[30]
J.
H.
Friedman.
"Multivariate
adaptive
regression
splines". In: *The Annals of Statistics* 19.1 (1991), pp. 1– 67.
[31]
B. Jiang and C. Claramunt. "A structural approach to
the model generalization of an urban street network". In: *GeoInformatica* 8 (2004), pp. 157–171.
[32]
S. S. Mousavi, M. Schukat, and E. Howley. "Traffic
light control using deep policy-gradient and valuefunction-based reinforcement learning". In: IET Intelligent Transport Systems 11.7 (2017), pp. 417–423.
[33]
Q. Tao, Z. Li, J. Xu, et al. "Short-term traffic flow
prediction based on the efficient hinging hyperplanes neural network". In: IEEE Transactions on Intelligent Transportation Systems 23.9 (2022), pp. 15616–15628.
[34]
A. Bemporad, M. Morari, V. Dua, and E. N. Pistikopoulos. "The explicit linear quadratic regulator for constrained systems". In: *Automatica* 38.1 (2002), pp. 3–20.
[35]
D. Guo, L. Tang, X. Zhang, and Y.-C. Liang. "Joint
optimization of handover control and power allocation based on multi-agent deep reinforcement learning". In: *IEEE Transactions on Vehicular Technology* 69.11 (2020), pp. 13124–13138.
[36]
J. Schulman, P. Moritz, S. Levine, et al. "Highdimensional
continuous
control
using
generalized
advantage
estimation".
In:
arXiv
preprint
arXiv:1506.02438 (2015).
[37]
M. Behrisch, L. Bieker, J. Erdmann, and D. Krajzewicz.
"SUMO–simulation of urban mobility: an overview". In: Proceedings of SIMUL 2011, The Third International Conference on Advances in System Simulation.
ThinkMind. 2011.
[38]
Y. Li, R. Yu, C. Shahabi, and Y. Liu. "Diffusion convolutional recurrent neural network: Data-driven traffic forecasting". In: arXiv preprint arXiv:1707.01926 (2017).
[39]
M. F. Niri, K. Liu, G. Apachitei, et al. "Machine learning for optimised and clean Li-ion battery manufacturing: Revealing the dependency between electrode and cell characteristics". In: Journal of Cleaner Production 324 (2021), p. 129272.
[11]
J. Xu, Q. Tao, Z. Li, et al. "Efficient hinging hyperplanes neural network and its application in nonlinear system identification". In: *Automatica* 116 (2020), p. 108906.
[12]
X. Liang and J. Xu. "Biased ReLU neural networks".
In: *Neurocomputing* 423 (2021), pp. 71–79.
[13]
E. Van der Pol and F. A. Oliehoek. "Coordinated
deep reinforcement learners for traffic light control". In: Proceedings of Learning, Inference and Control of Multi-agent Systems (NIPS) 8 (2016), pp. 21–38.
[14]
J. A. Calvo and I. Dusparic. "Heterogeneous multi-agent
deep reinforcement learning for traffic lights control". In: *AICS*. 2018, pp. 2–13.
[15]
N. Casas. "Deep deterministic policy gradient for
urban
traffic
light
control".
In:
arXiv
preprint
arXiv:1703.09035 (2017).
[16]
T. Chu, J. Wang, L. Codec`a, and Z. Li. "Multi-agent
deep reinforcement learning for large-scale traffic signal control". In: IEEE Transactions on Intelligent Transportation Systems 21.3 (2019), pp. 1086–1095.
[17]
T. Tan, F. Bao, Y. Deng, et al. "Cooperative deep
reinforcement learning for large-scale traffic grid signal control". In: *IEEE Transactions on Cybernetics* 50.6
(2019), pp. 2687–2700.
[18]
T. N. Kipf and M. Welling. "Semi-supervised classification with graph convolutional networks". In: arXiv preprint arXiv:1609.02907 (2016).
[19]
W. Hamilton, Z. Ying, and J. Leskovec. "Inductive
representation learning on large graphs". In: Advances in Neural Information Processing Systems 30 (2017).
[20]
P.
Veliˇckovi´c,
G.
Cucurull,
A.
Casanova,
et
al.
"Graph
attention
networks".
In:
arXiv
preprint
arXiv:1710.10903 (2017).
[21]
V. Zambaldi, D. Raposo, A. Santoro, et al. "Relational deep reinforcement learning". In: arXiv preprint
arXiv:1806.01830 (2018).
[22]
P. W. Battaglia, J. B. Hamrick, V. Bapst, et al. "Relational inductive biases, deep learning, and graph networks". In: *arXiv preprint arXiv:1806.01261* (2018).
[23]
J. Jiang, C. Dun, T. Huang, and Z. Lu. "Graph convolutional reinforcement learning". In: arXiv preprint arXiv:1810.09202 (2018).
[24]
H. Chen, Y. Liu, Z. Zhou, et al. "Gama: Graph attention multi-agent reinforcement learning algorithm for cooperation". In: *Applied Intelligence* 50 (2020),
pp. 4195–4205.
[25]
F.-X. Devailly, D. Larocque, and L. Charlin. "IG-RL:
Inductive graph reinforcement learning for massivescale traffic signal control". In: IEEE Transactions on Intelligent Transportation Systems 23.7 (2021), pp. 7496–7507.
[26]
L. Yan, L. Zhu, K. Song, et al. "Graph cooperation
deep reinforcement learning for ecological urban traffic signal control". In: *Applied Intelligence* 53.6 (2023), pp. 6248–6265.
[27]
Z. Zeng. "GraphLight: graph-based reinforcement learning for traffic signal control". In: 2021 IEEE 6th Inter-