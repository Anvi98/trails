# Motion Prediction Of Multi-Agent Systems With Multi-View Clustering

Anegi James1 and Efstathios Bakolas2
University of Texas at Austin

## Abstract

This paper presents a method for future motion prediction of multi-agent systems by including group formation information and future intent. Formation of groups depends on a physics-based clustering method that follows the agglomerative hierarchical clustering algorithm. We identify clusters that incorporate the minimum cost-to-go function of a relevant optimal control problem as a metric for clustering between the groups among agents, where groups with similar associated costs are assumed to be likely to move together. The cost metric accounts for proximity to other agents as well as the intended goal of each agent. An unscented Kalman filter based approach is used to update the established clusters as well as add new clusters when new information is obtained. Our approach is verified through non-trivial numerical simulations implementing the proposed algorithm on different datasets pertaining to a variety of scenarios and agents.

## 1 Introduction

As the field of autonomous multi-agent systems continues to advance, motion prediction of such systems with varying levels of communication, similarity between system dynamics, operations and ability to reason is an essential concern. To achieve safe and reliable operation, these agents require accurate future predictions of the motion of the nearby agents in the surrounding environment, including other vehicles or humans and unexpected obstacles. Research towards predicting the motion of individual sub-groups such as road vehicles [1], drones [2], UAVs [3] and also robot-human interaction [4] scenarios is extensively explored.

In most settings which utilize an autonomous vehicle in motion, it is likely that the environment is populated by many different types of agents (e.g., pedestrians, bicyclists, vehicles), with their own distinct dynamics, motion and sensory capabilities. An agent might not have information or the ability to communicate with other agents in the domain but intentional grouping (such as groups of friends, cyclists travelling in groups) as well as unintentional grouping (such as those observed at pedestrian crossings or vehicles travelling at speeds restricted by traffic) is observed.

In this work, this inherent grouping of agents in multi-agent scenarios is explored. Figure 1 depicts one such scenario where we have multiple agents with differing dynamics and goals that must interact and navigate around each other. Various groups exist inherently for both the pedestrian and vehicular agents owing to personal relations and other connections such as proximity, environmental constraints and traffic patterns. This work aims to take advantage of the natural grouping present among agents to simplify the prediction process and provide truncated information for path planning. Accounting for these groups will reduce the computation time for prediction of the agent states and also identify denser regions of uncertainty that need to be avoided in the planning process.

## 1.1 Literature Review

Several authors [5–9] have proposed methods to detect the social grouping between pedestrians and identify or test several grouping models for urban crowds. Agent groups can be identified by analyzing predominant group features and patterns [6] or by taking a data-driven approach.

Data-focused approaches to finding groups/patterns in agent motion rely on data clustering models. Clustering methods are most commonly used in trajectory planning to group trajectory pathlines into clusters which provide intuition for planning applications [10], [11].

A wide variety of clustering techniques exist to separate large-scale data based on some similarity measure between data points. Well-known clustering models relevant for the purpose of grouping agents include hierarchical agglomerative clustering [12], K-means, density based clustering [13], multi-view clustering [14–16] to name but a few. While these methods have different benefits in producing clusters with similar data points, they also have limitations depending on the application. For example, the K-means algorithm is widely used, but produces clusters of the same size and also requires the total number of clusters as an input parameter. Agglomerative clustering approaches circumvent the need for specifying the number of clusters a-priori, avoiding expensive computations for every clustering process.

Prediction of the agent groups may be completed through various estimation filters. Mixture filters permit the inclusion of the inter-dependent nature of sub-groups in a multi-agent system. In [17–19] variations of an adaptive Gaussian filter are proposed that include both the Kalman filter update and a method to re-sample the weights.

The authors in [20] introduce a multi-level hierarchical Kalman filter method which samples from multiple levels to come to a consensus on the estimate. In [21], authors propose a Bayesian Gaussian mixture filter that can reduce the mixture component number and prevent exponential growth. The authors of [22] and [23] propose two variations of a particle Gaussian mixture filter that propagates the state of the multi-agent system with particle filter methods and Kalman measurement updates. The Unscented Kalman filter [24] also provides a method for nonlinear estimation through approximation of the nonlinear dynamics with a minimum number of sigma points.

[25] introduces the split and merge unscented Kalman filter which is applied to nonlinear cases, removing mixture components with low probability and merging ones with similar means. Authors in [26] and [27] adapt variations of a Kalman Filter for intention-based estimation of multi-agent systems.

## 1.2 Contributions

This paper contributes an improved method for efficient prediction of the evolution of the future Probability Density Function (PDF) and uncertain state trajectory of groups of agents which exploits their inherent tendency to form groups, building on our previous work [28] which only utilizes a distance based metric to incorporate various motion features. A novel multi-view clustering method with a cost-based metric is incorporated into the clustering scheme along with the distance-based metric.

An optimal control problem is defined which minimizes the control effort for an agent to exchange position and velocity with another agent in close proximity, resulting in an optimal cost-togo relating the two agents. Additionally, a similar problem is solved to identify the optimal cost-to-go relating the agent and its known goal which provides a similarity criterion between agents based on their intent. The introduced cost-based clustering framework is able to identify agent groups based on features such as their relative distance and orientation while accounting for their dynamics which ensures identification of purposeful agent groups. Further, individual cluster member information is maintained along with the propagation of the cluster mean and covariance which can be extracted from the Gaussian mixture representation.

The state prediction method is extended to include the ability of the clusters to split and merge as well as update cluster membership with subsequent measurement updates providing updated state information. The validity of the proposed method has been tested on both pedestrian and vehicular agents using publicly available datasets namely: Argoverse 2 and Trajnet++.

## 1.3 Outline

Section II provides an overview of the preliminary information relevant to the agent dynamics and the Unscented Kalman Filter which is utilized for motion prediction. Section III details the clustering method to organize agents into clusters and cluster manipulation. Section IV formalizes the problem definition. Section V provides information on the simulations to test the method and the associated results.

## 2 Preliminaries 2.1 Notation

The vertical concatenation of two vectors x ∈ Rn and y ∈ Rm is denoted as [x; y] ∈ Rn+m. The Hausdorff Distance (HD) between two non-empty subsets *X, Y* of a metric space is denoted by dH(*X, Y* ), where

$$d_{H}(X,Y)=\operatorname*{max}\{\operatorname*{sup}_{x\in X}d(x,Y),\operatorname*{sup}_{y\in Y}d(y,X)\},$$
where d(*x, Y* ) = infy∈Y ∥x − y∥2, d(*y, X*) = infx∈X ∥x − y∥2.

Let ρN (x; *µ, P*) represent the probability density function of a normal random variable x with mean
µ and covariance matrix P = P T > 0.

## 2.2 Agent Dynamics

Consider a group of N mobile agents whose motion in the 2D plane is described by a double integrator kinematic model. In particular, the equations of motion of agent i, for i ∈ {1 *. . . N*}, are given by

$$\vec{p}^{i}_{x}(t)=u^{i}_{x}(t),\qquad\vec{p}^{i}_{y}=u^{i}_{y}(t),\tag{1}$$
where pi x, pi y represent the coordinates of its position in the 2D plane (measured with respect to a given inertial frame), vi x, vi y its velocity components and ui x, ui y the acceleration components (the assumption here is that the agent can directly control its acceleration) at time t ≥ 0. The equations of motion of agent i can be represented in terms of a continuous-time state space model as follows:

$$\dot{x}^{i}(t)=f(x^{i}(t),u^{i}(t))\tag{2}$$

where xi ∈ R4 denotes the state of agent i at time t with xi = [pi
                                                         x; pi
                                                            y; vi
                                                               x; vi
                                                                 y]T, ui ∈ R2 denotes its
control input with ui = [ui
                      x; ui
                         y] and f denotes its vector field with

$$f(x^{i},u^{i})=[v_{x}^{i};v_{y}^{i};u_{x}^{i};u_{y}^{i}]^{\mathrm{T}}=A x^{i}+B u^{i},$$
where,

$$A=\begin{bmatrix}\mathbf{0}_{x\times2}&\mathbf{I}_{x\times2}\\ \mathbf{0}_{x\times2}&\mathbf{0}_{x\times2}\end{bmatrix}\qquad B=\begin{bmatrix}\mathbf{0}_{x\times2}\\ \mathbf{I}_{x\times2}\end{bmatrix}\tag{3}$$

We will also use the following notation for the state of agent $i$: $x^{i}=[p^{i};\ v^{i}]$, where $p^{i}=[p^{i}_{x};p^{i}_{y}]$ is the position vector of agent $i$ and $v^{i}=[v^{i}_{x};v^{i}_{y}]$ is its velocity vector.

We assume that each agent has a goal or desired state and can employ a steering law / controller that will steer it to the latter state. In particular, let us assume that agent $i$ is associated with the goal position, $p^{i}_{y}=[p^{i}_{x};p^{i}_{y}]$, which tries to reach with zero velocity (soft landing) asymptotically (or exponentially) as $t\rightarrow\infty$ (obviously, the agent will "partically" reach the $p^{i}_{y}$ in finite time). The  acceleration of the agent is composed of two acceleration components: 1) $u_d$ which represents the control action due to a proportional derivative controller and 2) $u_f$ which includes the interaction force between agents; in particular, $$u^i=u_d^i+u_f^i$$. 
We assume that the acceleration of the agent i for both x and y directions is conditioned on the proximity to the goal position in the 2D plane pi g which should be reached with zero velocity, and is defined as follows:

$$u^{i}_{d}(x^{i})=K_{p}(p^{i}-p^{i}_{g})+K_{v}v^{i}\tag{4}$$
where Kp, Kv ∈ R are, respectively, the position and velocity gains which are assumed to have constant values for all the agents for simplicity.

The acceleration due to interaction between agents and agent groups is modelled using the social force model (SFM) which accounts for the attraction and repulsion between agents and their environment [29]. The interaction force, F i int, accounts for the repulsive force between agents in close proximity that mimics their tendency to avoid collisions with each other. Let the radius of an individual agent i be given by ri > 0. The interaction force between two agents, i and j located at pi and pj respectively, is defined as:

$$F_{int}^{i,j}=A_{int}\exp\left(\frac{r_{i,j}-d_{i,j}}{B_{int}}\right)n_{i,j}\tag{5}$$

where $A_{int}>0$ and $B_{int}>0$ are constants, $d_{i,j}=|p^{i}-p^{j}|$ is the distance between the two agents, $r_{i,j}$ is the sum of the radius of both agents and $n_{i,j}=(p^{i}-p^{j})/d_{i,j}$ is the normalized vector pointing in the direction from agent $j$ to agent $i$. The overall interaction force on an agent $i$ is given by

$$F_{int}^{i}=\sum_{j=1,i\neq j}^{N_{int}}F_{int}^{i,j},\tag{6}$$
where Nint indicates the total number of other agents i ̸= j that are close to agent i and included in its interaction zone such that di,j ≤ dtol. As F i int depends on the distance between the agents, it is a function of the agent state xi and the dynamics in (7) have an additional non-linear component. After closing the loop by using the feedback controllers given in (4) and including the social interaction force in (5) and (6), the equations of motion of agent i are given by

$$\dot{x}^{i}(t)=f^{i}_{c}(x^{i}(t))=A_{\rm cl}x^{i}(t)+g^{i}+F_{int}(x^{i}(t)),\tag{7}$$
where

$$A_{\rm cl}=\begin{bmatrix}0&0&1&0\\ 0&0&0&1\\ K_{p}&0&K_{v}&0\\ 0&K_{p}&0&K_{v}\end{bmatrix},\quad g^{i}=-K_{p}\begin{bmatrix}p^{i}_{x,g}\\ p^{i}_{y,g}\end{bmatrix}.\tag{8}$$

## 2.3 Clusters Of Agents

Let us assume that the group of N agents can be divided into a collection of NC ≥ 1 clusters (or sub-groups). Let CJ, with J ∈ {1*, . . . , N*C}, denote the J-th cluster. In particular, CJ consists of the indices of the agents that the cluster is composed of and let |CJ| denote the cardinality of CJ. In this context, a cluster may comprise multiple agents moving as a group or an individual agent constituting a cluster group (in the latter case, CJ corresponds to a singleton).

To cluster CJ, we associate a state vector ¯xJ, where ¯xJ = [¯pJ
x; ¯pJ
y ; ¯vJ
x; ¯vJ
y ] which provides similar position and velocity information as with the individual agent case but for the cluster as a whole (each cluster is treated as a single "representative" agent). The cluster state corresponding to cluster CJ is defined to be equal to the mean of the states of each individual agent in this cluster, that is,

$$\bar{x}_{J}=(1/|C_{J}|)\sum_{i\in C_{J}}x^{i}.\tag{9}$$
In the case of clusters with |CJ| > 1 agents, the covariance matrix ΣJ of this cluster is initially calculated using the statistical covariance, that is,

$$\Sigma_{J}=\frac{1}{|C_{J}|-1}\Sigma_{t\in C_{J}}(x^{i}-\bar{x}_{J})(x^{i}-\bar{x}_{J})^{\rm T}.$$

For singleton clusters (that is, the clusters with $|C_{J}|=1$), the covariance is set to a user-defined positive definite diagonal matrix, that is, $\Sigma_{J}=\mbox{diag}(\sigma_{\sigma_{\tau}}\sigma_{\tau_{i}},\sigma_{\omega_{i}})$, where $\sigma_{\tau},\sigma_{\tau}>0$, are the variances of the position and velocity components, respectively (typically, both $\sigma_{\tau}$ and $\sigma_{\omega}$ should be taken to be sufficiently small numbers). Furthermore, the probability distribution of cluster $C_{J}$ is denoted by $\bar{u}_{J}$, where $\bar{u}_{J}=[\bar{u}_{J}^{i},\bar{u}_{J}^{j}]$. The dynamic model used for the evaluation of the state of the $J^{th}$ cluster in the 2D plane is also described by the dynamics given in (2) but with the cluster mean positions and velocities, that is,

$$\bar{\chi}_{J}(t)=f_{J}(\bar{x}_{J}(t),\bar{u}_{J}(t)),\tag{10}$$
and the corresponding controllers (defined similarly to (4))

$$u^{J}(\bar{x}_{J})=K_{p}(\bar{p}^{J}-p_{g}^{J})+K_{v}\bar{v}^{J}+F_{int}^{J}(\bar{x}_{J})\tag{11}$$
where the gains Kp and Kv are the same as in the definition of the controller of the ith agent given in
(4) and the interaction force is defined as in (6). Consequently, the closed loop dynamics of the cluster CJ is described by the same equation as in (7) after replacing pi g = [pi x,g; pi y,g] with pJ = [pJ
x,g; pJ
y,g].

## 2.4 Unscented Kalman Filter

The Unscented Kalman filter (UKF) is a variation of the Kalman filter that approximates the estimated Gaussian PDF using sigma points. In this work, we adapt the formulation of the UKF for a multi-agent cluster setup. The sigma points associated with the UKF propagate and track the state and covariance of each individual cluster member xi in a given cluster CJ, instead of tracking only the cluster mean and covariance.

Next, we will briefly review the basic concepts and main steps of the UKF (the reader can find more details in [30]). Let the dynamics and measurement model of the agent be represented by the following discrete-time state space model:

$$x_{k+1}=f_{d}(x_{k},\nu_{k})\tag{12}$$ $$z_{k+1}=h_{d}(x_{k},\epsilon_{k}),\tag{13}$$
where xk is the state of the single agent or the representative agent of the multi-agent cluster at time step k (perhaps, a more precise notation for that state would have been ¯xJ,k, which we will not use here in order to keep the notation simple), vk is the process noise. Furthermore, ϵk is the measurement error associated with the measurement zk. The measurement errors and process noise are assumed to be independently and identically distributed.

The UKF is characterized by the selection of L = 2n + 1 sigma points, χi, i ∈ {1 *. . . L*}, where n is the dimension of the state space.

For a cluster CJ with |CJ| number of members, let the associated cluster state vector be given by
¯xJ and the state of the individual members be represented by xj, where j ∈ C is the index of the constituting members. The first sigma point is given by the cluster mean ¯xJ. For subsequent sigma points, the cluster member states xj represent the other 2n (or greater) cluster points as in (14):

$$\chi^{0}_{k}=\bar{x}_{J}\tag{14}$$ $$\chi^{i}_{k}=x^{j},\quad i=1,\ldots,2n$$
The weights associated with the states are given by W m and the covariance by W c and are calculated using an uneven distribution of weights. The weight associated with the χ0 sigma point is selected such that this point provides the majority of the contribution to the cluster state propagated by the UKF; in particular, W m
0
= 0.5. The weights of the other sigma points χ1:2n are evenly distributed W m
1:2n = 0.5
2n . This weight distribution applies to the covariance case as well.

For singleton clusters consisting of only one member, the cluster mean $\bar{x}_{J}$ and the actual member state $x^{j}$ coincide and the usual formulation of the UKF is applied. The associated covariance with this single agent is given by $P_{x}$. In this case, we are required to generate the $2n+1$ sigma points following (15). The sigma points for singleton clusters $\chi_{k}^{1},i=0\ldots2n$ with associated covariance $P=P^{1}>0$ are given by:

$$\chi_{k}^{0}=x^{j}$$ $$\chi_{k}^{1}=x^{j}+\sqrt{(}n+\lambda)P\quad i=1\ldots n$$ $$\lambda=\alpha^{2}(n+\kappa)-n,$$

where $\alpha$, $\beta$ and $\kappa$ are pseudo-random parameters. In particular, $\alpha$ determines the distribution of the sigma points around the algorithm parameters. In particular, $\alpha$ determines the distribution usually set to $0$ and $\beta=2$ is the standard value for incorporating prior information given a Gaussian distribution [24]. The weight $W_{0}^{n}=\lambda/(\lambda+n)$

$$W_{0}^{n}=\lambda/(n+\lambda)+(1-\alpha^{2}+\beta)\tag{16}$$ $$W_{1}^{n}=W_{1}^{\kappa}=1/2(n+\lambda)\quad i=1\ldots2n$$

The weights associated with each of the sigma points $\chi_{k}$ are given by (16) for singleton clusters. $W^{n}$ indicate weights for the state propagation while $W^{\kappa}$ terms represent the weighting factors for the covariance. The sigma points are propagated through the dynamic model $f_{d}$ as follows assuming process noise $\nu_{k}$:

$$\tilde{\chi}_{k+1}^{i}=f_{d}(\chi_{k}^{i},\nu_{k})\quad i=0\ldots2n+1\tag{17}$$
The mean and covariance for the agent's state through the prediction step are approximated as follows:

$$\bar{y}=\sum_{i=1}^{2n}W_{i}^{m}\hat{\chi}_{k+1}^{i}$$ $$P_{y}=\sum_{i=0}^{2n}W_{i}^{r}(\hat{\chi}_{k+1}^{i}-y)(\hat{\chi}_{k+1}^{i}-y)^{\rm T}+Q_{k}\tag{18}$$

The time updated sigma points $\hat{\chi}_{k+1}^{i}$ are propagated through the measurement model:

$$Z^{\prime}=h_{d}(\hat{\chi}_{k+1}^{i},\epsilon_{k})\tag{19}$$ $$\bar{z}=\sum_{i=0}^{2n}Z^{\prime}W_{i}^{m}$$

The measurement update leverages the sigma points to calculate the covariance matrices $P_{zz},P_{xz},P_{k}$ for the update equation and the mean $x_{k+1}$ according to the following equations:

$$P_{zz}=\sum_{i=0}^{2n}W_{i}^{r}(Z^{i}-\bar{z})(Z^{i}-\bar{z})^{\rm T}\tag{20}$$ $$P_{xz}=\sum_{i=0}^{2n}W_{i}^{r}(\hat{\chi}_{k+1}^{i}-\bar{y})(Z^{i}-\bar{z})^{\rm T}$$ $$P_{k}=P_{y}-P_{zz}P_{xz}P_{xz}^{-1}$$ $$x_{k+1}=\bar{y}+P_{xz}P_{xz}^{-1}(z_{k}-\bar{z})$$

where $x_{k+1}$ is the updated state given the measurement update $z_{k}$ at time step $k$.

## 3 Methods 3.1 Similarity Metrics

In order for two agents to be categorized as members of the same cluster, it is necessary for them to satisfy three conditions simultaneously: (1) they should be in close spatial proximity, (2) they should exhibit similar orientations and velocities in their respective motions, and (3) the agents should be moving towards goals in close relative proximity.

## 3.1.1 Cost Distance

An optimal control based metric is designed to implicitly account for the previously stated conditions for the similarity metric. This metric ensures that agents grouped in the same cluster are likely to move in similar directions in future time steps. The utilized metric corresponds to the weighted sum of the optimal cost functions of two separate but similar optimal control problems, which we will describe next.

The first problem concerns two agents, namely agent i and agent j which attain respectively states xi = [pi; vi] and xj = [pj; vj] at time t ≥ 0 and governed by the agent dynamics defined in (2). The initial states of the two agents (at time t = 0) are denoted by xi
0 and xj
0, where xi
0 = [pi
0; vi
0] and xj
0 = [pj
0; vj
0], respectively. The problem's objective is to find an optimal control input u∗
i (·) (1) that will transfer agent i from the initial state xi(0) = [pi
0; vi
0] to the final state xi(Tf) = [pj
0; vj
0] (note that the terminal state of agent i corresponds to the initial state xj
0 of agent j) within the given time horizon [0, Tf] and (2) will minimize the control effort:

$$\min_{u_{i}}J_{1}(u_{i}(\cdot))=\int_{0}^{T_{f}}\left\|u_{i}(t)\right\|^{2}\mathrm{d}t$$ s.t. $$\dot{x}^{i}=f(x^{i},u^{i}),\quad t\in[0,T_{f}]\tag{21}$$ $$x^{i}(0)=x_{0}^{i}=[p_{0}^{i},v_{0}^{i}]$$ $$x^{i}(T_{f})=x_{0}^{j}=[p_{0}^{j},v_{0}^{j}]$$
where f is as defined in (2). The solution of the optimal control problem given in (21) will provide us with a suitable metric for clustering agents that is neither distance-based nor explicitly dependent on its orientation or velocity (essentially, the optimal cost of the proposed problem can be viewed as the control effort required for agent i to interchange its state with the state of agent j). As is shown in [31], the optimal control input u∗
i (t) that solves the optimal control problem (21), where the velocity at the final time is substituted as v(Tf) = vj
0, is given by

u∗ i (t) = a + tb (22) b = 1/T 3 f (12xi 0 − 12xj 0 + 6Tfvi 0 + 6Tfvj 0) a = −1/Tf(aT 2 f /2 + vi 0 − vj 0)
for all t ∈ [0, Tf]. The associated optimal cost, which is denoted by V1(xi
0, xj
0), given the optimal control input u∗
i (t) defined in (22), is calculated as:

V1(xi 0, xj 0) = J1(u∗ i (·)) = 1/2(Tf∥a∥2 + T 2 f aTb + 1/3T 3 f ∥b∥2). (23)
The cost function in (23) serves as one of the measures of dissimilarity between agents belonging to different clusters.

Similarly, the second component of the metric will be obtained by solving a second optimal control problem which seeks for the control input that will direct an agent to its (prescribed) goal destination while using minimum control effort. In particular, let agent i, whose motion is described by (2) attain the state xi = [pi; vi] at time t ≥ 0 (its initial state at time t = 0 is denoted by xi
0, where xi
0 = [pi
0; vi
0], as before), and let xi g, where xi g = [pi g; vi g], be its intended terminal (goal) state. Then, find a control input ui(·) that (1) will transfer agent i from its initial state xi
0 = [pi
0; vi
0], at time t = 0, to the final state xi Tf = [pi g; vi g] at the final time t = Tf for a given time horizon Tf, and (2) will minimize the control effort:

0 ∥ui(t)∥2 min ui J2(ui(·)) = � Tf (24) s.t. ˙xi = f(xi, ui), t ∈ [0, Tf] xi(0) = xi 0 = [pi 0; vi 0] xi(Tf) = xi g = [pi g; vi g] The solution of the optimal control problem given in (24) provides us with a suitable metric for clustering agents that also includes information about their intended goals, resulting in clusters that are potentially longer lasting. The optimal control input $u_{t}^{*}$ that solves the optimal control problem (24) is given by:

$$u_{t}^{*}(t)=\alpha+t\beta$$ $$\beta=-12/T_{f}^{j}(p_{b}^{*}-p_{0}^{j}+T_{f}v_{0}^{j})-(6/T^{j})v_{0}^{j}\tag{25}$$ $$\alpha=6/T_{f}^{j}(p_{b}^{*}-p_{0}^{j}-T_{f}v_{0}^{j})+(2/T_{f})v_{0}^{j}$$

The associated optimal cost, which is denoted as $\mathcal{V}_{2}(x_{0}^{j},x_{0}^{j})$, is given by the right hand side of (23) after replacing $x_{0}^{j}$ with $x_{g}^{j}$ and $a$, $b$ with $\alpha$, $\beta$ calculated on (24).

The total cost distance is given by a weighted sum of the optimal cost functions associated with the solutions of the two optimal control problems we just described, that is,

$$\mathcal{V}(x_{0}^{j},x_{0}^{j},x_{g}^{j})=\lambda_{1}\mathcal{V}_{1}(x_{0}^{j},x_{0}^{j})+\lambda_{2}\mathcal{V}_{2}(x_{0}^{j},x_{g}^{j}).\tag{26}$$
The weighting factors λ1, λ2 are user-defined non-negative scalars and may be selected to reflect an interest in whether short term or long-term groupings are desired or depending on whether the agent intents are goal destinations or intermediate inferences on their projected path.

## 3.1.2 Geometric Distance

The closeness between individual agents is measured in terms of the Euclidean Distance (ED), di,j =
∥pi − pj∥2, while the Hausdorff distance measures the relative closeness of clusters. The Hausdorff Distance dH(CI, CJ) measures the dissimilarity between collections of agents CI = (x1*, . . . , x*NI) and CJ = (xNJ) comprising members of separate clusters. The Hausdorff distance is used when we are checking the inclusion of a singleton cluster (CJ) in another cluster (CI). Both cost distance and geometric distance are considered for multi-view clustering of the agents into objective groups.

## 3.2 Multi-View Clustering

The clustering of agents into different groups uses both cost and geometric distance methods for an agglomerative hierarchical clustering method that follows a bottom-up approach. Individual agents are first grouped into pairs and further pairs are grouped to form larger clusters. Clustering agents into pairs requires defining parameters and corresponding thresholds for comparison. The previous two sections detail the distance-based and physics-based clustering metrics.

Given a set of N mobile agents identified with a point-set X = {x1, . . . , xN} ⊂ R4 (X is the set comprising the states of the N agents), the process of estimating its future state is simplified by accounting for the presence of inherent groups in their interactions and movement. The identification of this grouping is performed using a multi-view clustering scheme that accounts for multiple factors characterizing the clusters.

This section details the clustering process used to group each agent given their state predictions xk+1 into an undefined number of clusters Nc. Let C = {C1*, . . . , C*Nc} represent the set of clusters, where the Jth member is represented as CJ and ¯xJ = [¯pJ; ¯vJ] defines the mean position and velocity of all the members in the cluster. In this work, the grouping between agents is considered to be influenced by their similarity metrics described in Section 3.1.

Identifying groups within the multi-agent system requires finding a consensus between the multiple clustering views, i.e., the cost based and distance based view. Algorithm 1 details the clustering scheme for the pairwise grouping of agents. Initially, every agent is assumed to belong to its own cluster. The minimum cost pair is calculated in lines 3-4 using (26) and the Euclidean distance for this pair is calculated in line 5. Agents are paired into a cluster, if there is consensus between their cost based metric and distance based metric, as calculated in lines 6-10.

Algorithm 2 provides the description of the remainder of the clustering process for cluster-agent and cluster-cluster merging. Figure 2 depicts the complete linkage clustering method which accounts for the linkages between the farthest neighbors. Consider two clusters CI and CJ with members i ∈ CI and j ∈ CJ. In line 2 of Algorithm 2, the agents with maximum distance between them, i ∈ CI and j ∈ CJ are identified. Steps 3 and 4 calculate the cost associated with these agents using equation (23)
and find the cluster with the minimum associated cost. These clusters are merged, if their distances Algorithm 1 Agent-Agent Grouping Algorithm Input : N > 0, x1, . . . , xN, dtol Output : Nc > 0, C1, . . . , CNc
1: Define C1 = {x1}, . . . , CN = {xN}
2: **for** i = 1 : N do
3:
Calculate cost for all other agents j ̸= *i, j* = 1 : N
4:
Find min cost agent xmin

5:
Find ED(xi, xj)
6:
if ED(xmin < dtol) then
7:
Cluster xi, xmin
8:
Nc = Nc + 1
9:
Apply Algorithm 2 to cluster & other agents j
10:
end if
11: end for
12: Cluster agents into groups CJ 13: Calculate cluster means ¯xJ
are within a predefined threshold dtol > 0 and the relative difference in cost is within a threshold ctol > 0. The tolerances may be chosen appropriately for the scale of the problem, for example, if the majority of the agents cover a smaller average distance over time, dtol will have a smaller value. Any discrepancies in the capabilities of different agents in the same multi-agent scenario will be taken into consideration by the cost distance.

Algorithm 2 Cluster-Cluster Grouping Algorithm Input : CI, CJ, dtol > 0, ctol > 0
Output : C1 . . . CM

1: Find (xi, xj) =
                           argmax
                        xi∈CI,xj∈CJ
                                       ∥xi − xj∥

2: Find optimal cost (V) for agents i ∈ CI and j ∈ Cj
3: if V(xi, xj) < ctol then

4:
        Calculate Hausdorff distance (dH(CI, CJ)) between clusters

5:
        Merge if dH ≤ dtol, Nc → Nc − 1

6: end if

## 3.3 Merge And Split Clusters

Merging and splitting is part of the re-clustering process which takes place after the estimation step.

Consider a set of clusters C with Nc members where the Jth cluster's state can be represented as ¯xk J at some time k with J ∈ {1*, . . . , N*c}. Post the prediction and measurement update, the propagated set of clusters will go through a re-clustering process as described in Algorithms 1 and 2. The resulting Jth cluster state at time k + 1 is given by ¯xk+1
J
with J ∈ {1 *. . . N*q}, where Nq is the resulting number of clusters which has no dependence on Nc. This will account for whether a cluster remains the same, adds new members or removes members that are no longer relevant to the group. It is also the prior for the UKF in the next timestep.

## 3.4 Insertion And Deletion Of Clusters

New clusters are formed post prediction and estimation step, if there is an unassigned observation that cannot be associated with existing clusters or their corresponding members. Such an unassigned observation is added to the existing agent states xi and Algorithms 1 and 2 provide the new cluster set Ck+1 with the updated information.

In our case, the cluster/agent will be deleted due to the absence of an observation zi for a particular agent state xi. However, the absence of a corresponding agent-observation pair does not necessarily indicate the irrelevance of that agent as the agent might have been missed by sensing systems for a number of reasons, including sensor fault or occlusion by the environment or other agents.

## 4 Problem Formulation 4.1 Problem Definition

Consider a group of N agents in motion with states denoted by xi and associated covariance P i as explained in Section 2.2 and let the field of view be a bird's eye view of the domain. Each agent follows the dynamic model given in equation (7). Time series data of state observations for all N agents is available for time t = t0. The associated probability density function ρN for this distribution is given by (27) which provides information about the density of the field at each point x:

$$\rho_{\mathcal{N}}(x;\mu^{i},P^{i})=\frac{1}{\sqrt{2\pi|P^{i}|}}\mathrm{e}^{-\frac{1}{2}(x-\mu^{i})^{T}P^{i-1}(x-\mu^{i})}.\tag{27}$$

We aim to predict the density evolution of the multi-agent system given an initial description of the multi-agent network's density.

For a given set of clusters C , the PDF at the initial time is given by a convex combination of the PDFs of the clusters within the cluster set, that is,

$$\rho(t_{0},\hat{x}(t_{0}))=\sum_{i=1}^{N_{c}}w_{i,0}^{i}\,\rho_{N}(\hat{x}(t_{0});\mu_{i_{0}}^{i},P_{i_{0}}^{i}),\tag{28}$$

where the weights of the Gaussian mixture PDF are such that $w_{i_{0}}^{i}\geq0$ and $\sum_{i}^{N_{c}}w_{i,0}^{i}=1,\forall i=1,\ldots,N_{c}$. The main aim is to predict the future PDF of the clusters from the initial time to the final simulation time $t_{f}$ based on maximum likelihood estimation. The distribution of agents also varies with time and their association with each other might not remain constant over time. Identifying and accounting for the initial time $t_{f}$, the probability of the population mean $t_{f}$ is the mean of the population mean.

The posterior PDF of each agent or cluster state is a Gaussian PDF. The posterior PDF distribution for the multi-agent system may be represented as a Gaussian mixture comprising the agent cluster position and velocity estimates at time $t_{f}$ using initially observed data which is given by

$$\rho(t_{f},\hat{x}(t_{f}))=\sum_{i=1}^{N_{c}}w_{i,0}^{i}\,\rho_{N}(\hat{x}(t_{f});\mu_{i,f}^{i},P_{i,f}^{i})\tag{29}$$

where the weights of the Gaussian mixture PDF are such that $w_{i}\geq0$ and $\sum_{i}^{N_{c}}w_{i}=1,\forall i=1,\ldots,N_{c}$. We identify the PDF of the position of the agent in the domain for the entire time span of the simulation $(t\in[t_{0},t_{f}])$. This provides a state estimate of every agent cluster at each time across the span and an overall density estimate of the occupied area in the domain.

## 4.2 Proposed Solution

The UKF, described in Section 2.4 is applied for state estimation of the multi-agent system. Provided initial state information at time t0 = 0, the agents are initially grouped into separate clusters based on Algorithm 1 and 2, where each agent is either part of a cluster group or forms a singleton cluster by itself. The optimal value function of the optimal control problem (21) which is defined in (23) provides a suitable metric for clustering agents that is neither distance-based nor explicitly dependent on its orientation or velocity. Algorithm 3 provides an overview of the process of computing the prediction and update steps given a set of cluster states. Lines 2-3 of Algorithm 3, set up the initial clusters as described in Section 3.2. Lines 5-7 update the cluster mean and covariances using the UKF described in Section 2.4. Any changes or updates to the clusters, including merging or deletion of clusters is indicated by the steps in lines 8-9.

Algorithm 3 Cluster motion prediction algorithm Input : Nc ≥ 0, N ≥ 0, x1
0, . . . , xN
0 , Tf Output : N(µ, Σ) = UKF(x1
Tf , . . . , xN
Tf )
1: xi ← xi
0

2: Cluster agents into groups CJ, J ∈ {1, . . . , Nc}
3: Calculate cluster mean ¯xJ
4: for t = 1 : Tf do
5:
        for J ∈ {1, . . . , Nc} do

6:
Run UKF on each cluster CJ
7:
end for
8:
Add/remove clusters using observation update
9:
Re-cluster agent groupings based on latest update.
10: end for

## 5 Results 5.1 Datasets

The proposed algorithm for motion prediction of the clustered multi-agent system (that is, Algorithm 3 presented in Section 4 is tested with real-world datasets: Trajnet++ [32] and Argoverse 2 [33], [34].

| Type    |   Time |     FDE |    ADE |
|---------|--------|---------|--------|
| Scene 1 |        |         |        |
| ED      | 0.0477 |  1.3051 | 1.2431 |
| CD      | 0.0067 |  0.633  | 1.1335 |
| Scene 2 |        |         |        |
| ED      | 0.011  |  6.9542 | 2.2399 |
| CD      | 0.0048 |  3.1392 | 1.0674 |
| Scene 3 |        |         |        |
| ED      | 0.0094 | 23.7522 | 6.035  |
| CD      | 0.0064 |  0.0336 | 1.123  |

The Trajnet++ datasets provide time series data of the x, y coordinates of the position of pedestrians, along with respective frame and scene information. Each scene is parsed through to obtain a dataseries with the required state of all agents on the scene.

The Argoverse 2 Motion Forecasting dataset provides extensive position and velocity data collected from various cities separated into scenarios of 11s segments with multiple types of agents such as vehicles, pedestrians, motorcycles and also static objects.

## 5.2 Simulation

For each scenario/scene, we isolate the initial positions and velocities of all of the agents in that scenario which is passed on to Algorithm 1 and Algorithm 2 to group the agents into clusters using their initial states. Algorithm 3 is employed to predict the future state of the clusters of agents as well as of the individual cluster members. The algorithm output provides a future mean and covariance estimate for the predicted position and velocity of each agent and cluster at the final time tf. Since the dataset for each sequence is complete, the algorithm is assumed to have access to observation data extracted from the original dataset at a lower frequency than the original.

## 5.2.1 Trajnet++

We will now present the clustering and prediction results based on data from the Trajnet++ which focuses on pedestrian agents. Figure 3 and Figure 4 represent the state mean predictions for two observed scenes of pedestrian data. The circular data points indicate predicted positions while the
′×′ markers represent the true agent data points. In these figures, the red circles represent the 3σ
confidence ellipsoids around the cluster mean. The presence of smaller ellipses is due to the truth data sampling. Additionally, the predicted trajectory tracks the true trajectory with small errors. The errors can be attributed to the simplicity of the dynamic model not being able to capture the agent intents. The average distance error (ADE) and final distance error (FDE) are calculated over a 100 different scenes and their values are added up for all agents on the scene whose trajectory has been predicted. The FDE measures the difference in the final predicted position of the agent and the actual true position while the ADE averages the error over all timesteps. In Figure 5, the FDE has a larger value over all scenes in the range 10 − 80 while the ADE averages under 5 for the same scenes. While the final distance error is significant, the lower values of the ADE imply that the algorithm is able to predict an overall trajectory that matches the true trajectory for each of the observed agents on the scene.

## 5.2.2 Comparison

The clustering algorithm given by Algorithm 1 and 2 is compared against another standard clustering algorithm that uses only a geometric distance based criterion. Assume CD refers to the clustering algorithm from Section III and ED to Density Based Spatial Clustering, a Euclidean Distance based clustering algorithm. Table 1 compares the result of both algorithms with several different scenes by evaluating the FDE and ADE as well as time taken for the simulation. Each scene is obtained from the Trajnet++ dataset and is less than 2s in length. From the table, we observe that for the same tolerance parameters, our algorithm performs better than a solely distance-based algorithm that does not take into account the other features of the agent motion.

Additionally, the effect of the parameters λ1, λ2 are explored using a comparative study varying the parameter and noting the differences in the clusters formed for the same agent scenario. This explores

(a) $\lambda_{1}=0,\lambda_{2}=1$ (b) $\lambda_{1}=0.5,\lambda_{2}=0.5$ (c) $\lambda_{1}=0.7,\lambda_{2}=0.3$ (d) $\lambda_{1}=1,\lambda_{2}=0$ (a) $t=1-2s$ (b) $t=2-5s$ (c) $t=5-8s$ (d) $t=8-11s$
the effect of both the goal based and the neighbour based cost criterion. The parameters are varied as λ1 ∈ [0, 1], λ2 = 1 − λ1 and the resulting clusters formed over the simulation time are observed in Figure 6.

## 5.2.3 Argoverse 2

The Argoverse 2 dataset focuses on vehicular agents on various types of roadways but also includes pedestrian and cyclist agents as well. The results from applying the algorithm to the Argoverse 2 data is provided in this section. We focus on individual scenarios within the dataset to highlight the capabilities of the algorithm in different situations.

Figure 7 illustrates a scenario of a roadway intersection with vehicles driving along the road while other vehicles wait at the intersection. The clustering algorithm prioritizes grouping agents traveling in the same direction within a certain distance. This distance depends on user-derived variable but can be adjusted for different general speeds and density of the road. Figure 8 depicts a close up view of the progression of a cluster with two members over time, where the red circle is centered at the cluster mean and has a diameter equal to the distance between the agents. From Figures 7 and 8, it is clear that the clustering algorithm prioritizes grouping agents that are traveling in the same direction. The range of the grouped agents does depend on user defined parameters and potentially would be adjusted for different scenarios depending on the location of the concerned agent in the scene, the type of roadway, the density of users on the road, the distance to the final goal etc.

In Figure 9, the effects of the dynamic clustering, are visualized. Agent 1 (blue) is initially close to Agent 2 (red) and were grouped into the same cluster.

At a future time, Agent 1 has passed Agent 2 and is closer to Agent 3 (green), so the clustering algorithm has split the initial cluster and re-clustered Agent 1 and 3 since they are closer in Euclidean distance and speed. The cluster centers (black triangles) are the mean position of the state estimate of all the individual members of the cluster. As a result, the cluster center skews towards its cluster members rather than a straight line that mimics Agent 1.

(a) $t=7.0-7.5s$ (b) $t=7.5-7.7s$ (c) $t=7.5-8.1s$ (a) $t=1.5s-1.8s$ (b) $t=1.9s-2.3s$ (c) $t=2.4s-2.6s$ (d) $t=2.7s-3.0s$

## 6 Conclusions

This paper has presented a novel method for the future motion prediction of a group of agents by incorporating agent grouping according to a cost based criterion combined with geometric distance. Agents are grouped according to their feature similarity and known intent using a hierarchical agglomerative clustering method, enabling the creation of clusters independent of size and number constraints. This work includes a new clustering method that accounts for the features of the agents without explicitly requiring several thresholds for the distinction between agent states. The proposed algorithm is able to incorporate various features of the agent interactions using only the information of its position and velocity. The automatic split and merge of clusters is also introduced here using the predictions at each time. Future work will conduct extensive simulations on large datasets with diverse scenarios to show that the algorithm is able to effectively cluster and accurately predict the agent trajectories.

## Acknowledgment

This research has been supported in part by NSF award ECCS-1924790.

## References

[1] N. Deo, A. Rangesh, and M. M. Trivedi, "How Would Surround Vehicles Move?
A Unified
Framework for Maneuver Classification and Motion Prediction," IEEE Transactions on Intelligent Vehicles, vol. 3, no. 2, pp. 129–140, 2018.
[2] H. Peng, A. Razi, F. Afghah, and J. Ashdown, "A unified framework for joint mobility prediction
and object profiling of drones in UAV networks," *Journal of Communications and Networks*, vol. 20, no. 5, pp. 434–442, 2018.
[3] R. Sharma and D. Ghose, "Collision Avoidance Between UAV Clusters using Swarm Intelligence
Techniques," *International Journal of Systems Science*, vol. 40, no. 5, pp. 521–538, 2009.
[4] J. Mainprice and D. Berenson, "Human-robot Collaborative Manipulation Planning using Early
Prediction of Human Motion," in 2013 IEEE/RSJ International Conference on Intelligent Robots
and Systems, pp. 299–306, 2013.
[5] M. Luber and K. O. Arras, "Multi-Hypothesis Social Grouping and Tracking for Mobile Robots.,"
in *Robotics: Science and Systems*, 2013.
[6] A. Gorrini, S. Bandini, and G. Vizzari, "Empirical Investigation on Pedestrian Crowd Dynamics
and Grouping," in *Traffic and granular flow'13*, pp. 83–91, Springer, 2015.
[7] G. Vizzari, L. Manenti, and L. Crociani, "Adaptive Pedestrian Behaviour for the Preservation of
Group Cohesion," *Complex Adaptive Systems Modeling*, vol. 1, no. 1, pp. 1–29, 2013.
[8] Q. Wang, M. Chen, F. Nie, and X. Li, "Detecting Coherent Groups in Crowd Scenes by Multiview
Clustering," *IEEE transactions on pattern analysis and machine intelligence*, vol. 42, no. 1, pp. 46–
58, 2018.
[9] L. Cheng, R. Yarlagadda, C. Fookes, and P. Yarlagadda, "A Review of Pedestrian Group Dynamics
and Methodologies in Modelling Pedestrian Group Behaviours," World Journal of Mechanical Engineering, vol. 1, no. 1, pp. 1–13, 2014.
[10] D. B. Nguyen, L. Zhang, R. S. Laramee, D. Thompson, R. O. Monico, and G. Chen, "Physics-
Based Pathline Clustering and Exploration," in *Computer Graphics Forum*, vol. 40, pp. 22–37, Wiley Online Library, 2021.
[11] J.-G. Lee, J. Han, and K.-Y. Whang, "Trajectory Clustering: A Partition-and-Group Framework,"
in *Proceedings of the 2007 ACM SIGMOD International Conference on Management of Data*, pp. 593–604, 2007.
[12] S. Shuming, Y. Guangwen, W. Dingxing, and Z. Weimin, "Potential-Based Hierarchical Clustering," in *2002 International Conference on Pattern Recognition*, vol. 4, pp. 272–275, IEEE,
2002.
[13] H.-P. Kriegel, P. Kr¨oger, J. Sander, and A. Zimek, "Density-based Clustering," Wiley interdisciplinary reviews: data mining and knowledge discovery, vol. 1, no. 3, pp. 231–240, 2011.
[14] S. F. Hussain, M. Mushtaq, and Z. Halim, "Multi-View Document Clustering via Ensemble
Method," *Journal of Intelligent Information Systems*, vol. 43, no. 1, pp. 81–99, 2014.
[15] Y. Yang and H. Wang, "Multi-View Clustering: A Survey," *Big Data Mining and Analytics*,
vol. 1, no. 2, pp. 83–107, 2018.
[16] S. Bickel and T. Scheffer, "Multi-View Clustering.," in *ICDM*, vol. 4, pp. 19–26, 2004.
[17] A. S. Stordal, H. A. Karlsen, G. Nævdal, H. J. Skaug, and B. Vall`es, "Bridging the Ensemble
Kalman Filter and Particle Filters: The Adaptive Gaussian Mixture Filter," Computational Geosciences, vol. 15, no. 2, pp. 293–305, 2011.
[18] J. H. Kotecha and P. M. Djuric, "Gaussian Sum Particle Filtering," IEEE Transactions on Signal
Processing, vol. 51, no. 10, pp. 2602–2612, 2003.
[19] G. Terejanu, P. Singla, T. Singh, and P. D. Scott, "Adaptive Gaussian Sum Filter For Nonlinear
Bayesian Estimation," *IEEE Transactions on Automatic Control*, vol. 56, no. 9, pp. 2151–2156,
2011.
[20] D. Guo, X. Wang, and R. Chen, "Multilevel Mixture Kalman Filter," EURASIP Journal on
Advances in Signal Processing, vol. 2004, no. 15, pp. 1–12, 2004.
[21] A. G. Wills, J. Hendriks, C. Renton, and B. Ninness, "A Bayesian Filtering Algorithm for
Gaussian Mixture Models," 2017.
[22] D. Raihan and S. Chakravorty, "Particle Gaussian Mixture Filters-i," *Automatica*, vol. 98,
pp. 331–340, 2018.
[23] D. Raihan and S. Chakravorty, "Particle Gaussian Mixture Filters-ii," *Automatica*, vol. 98,
pp. 341–349, 2018.
[24] E. A. Wan and R. Van Der Merwe, "The Unscented Kalman Filter for Nonlinear Estimation,"
in Proceedings of the IEEE 2000 Adaptive Systems for Signal Processing, Communications, and Control Symposium (Cat. No. 00EX373), pp. 153–158, Ieee, 2000.
[25] F. Faubel, J. McDonough, and D. Klakow, "The Split and Merge Unscented Gaussian Mixture
Filter," *IEEE Signal Processing Letters*, vol. 16, no. 9, pp. 786–789, 2009.
[26] M. B. Khalkhali, A. Vahedian, and H. S. Yazdi, "Multi-target State Estimation Using Interactive
Kalman Filter For Multi-Vehicle Tracking," IEEE Transactions on Intelligent Transportation Systems, vol. 21, no. 3, pp. 1131–1144, 2019.
[27] J. Schulz, C. Hubmann, J. L¨ochner, and D. Burschka, "Multiple Model Unscented Kalman Filtering in Dynamic Bayesian Networks for Intention Estimation and Trajectory Prediction," in 2018 21st International Conference on Intelligent Transportation Systems (ITSC), pp. 1467–1474,
IEEE, 2018.
[28] A. James and E. Bakolas, "Gaussian Mixture Based Motion Prediction for Cluster Groups of
Mobile Agents," *IFAC-PapersOnLine*, vol. 55, no. 37, pp. 408–413, 2022. 2nd Modeling, Estimation and Control Conference MECC 2022.
[29] D. Helbing and P. Molnar, "Social Force Model for Pedestrian Dynamics," *Physical review E*,
vol. 51, no. 5, p. 4282, 1995.
[30] S. S¨arkk¨a and L. Svensson, *Bayesian filtering and smoothing*, vol. 17. Cambridge university press,
2023.
[31] E. Bakolas and Y. Lee, "Decentralized Game-Theoretic Control for Dynamic Task Allocation
Problems for Multi-Agent Systems," in *2021 American Control Conference (ACC)*, pp. 3228–
3233, IEEE, 2021.
[32] P. Kothari, S. Kreiss, and A. Alahi, "Human Trajectory Forecasting in Crowds: A Deep Learning
Perspective," *IEEE Transactions on Intelligent Transportation Systems*, pp. 1–15, 2021.
[33] B. Wilson, W. Qi, T. Agarwal, J. Lambert, J. Singh, S. Khandelwal, B. Pan, R. Kumar, A. Hartnett, J. K. Pontes, D. Ramanan, P. Carr, and J. Hays, "Argoverse 2: Next Generation Datasets for Self-driving Perception and Forecasting," in Proceedings of the Neural Information Processing
Systems Track on Datasets and Benchmarks (NeurIPS Datasets and Benchmarks 2021), 2021.
[34] J. Lambert and J. Hays, "Trust, but verify: Cross-modality fusion for hd map change detection,"
in Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks (NeurIPS Datasets and Benchmarks 2021), 2021.