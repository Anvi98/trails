
## Parametric Pde Control With Deep Reinforcement Learning And Differentiable L0-Sparse Polynomial Policies

Nicolò Botteghi Department of Applied Mathematics University of Twente Enschede, The Netherlands n.botteghi@utwente.nl

## Abstract

Optimal control of parametric partial differential equations (PDEs) is crucial in many applications in engineering and science. In recent years, the progress in scientific machine learning has opened up new frontiers for the control of parametric PDEs. In particular, deep reinforcement learning
(DRL) has the potential to solve high-dimensional and complex control problems in a large variety of applications. Most DRL methods rely on deep neural network (DNN) control policies. However, for many dynamical systems, DNN-based control policies tend to be over-parametrized, which means they need large amounts of training data, show limited robustness, and lack interpretability. In this work, we leverage dictionary learning and differentiable L0 regularization to learn sparse, robust, and interpretable control policies for parametric PDEs. Our sparse policy architecture is agnostic to the DRL method and can be used in different policy-gradient and actor-critic DRL algorithms without changing their policy-optimization procedure. We test our approach on the challenging tasks of controlling parametric Kuramoto-Sivashinsky and convection-diffusion-reaction PDEs. We show that our method (1) outperforms baseline DNN-based DRL policies, (2) allows for the derivation of interpretable equations of the learned optimal control laws, and (3) generalizes to unseen parameters of the PDE without retraining the policies. Code available on github.com/nicob15/PDE-Control-with-DRL.

Deep Reinforcement Learning, Parametric Partial Differential Equations, Sparse Dictionary Learning, L0 Regularization

## 1 Introduction

Many systems in engineering and science can be modeled by partial differential equations (PDEs). The control of these systems governed by PDEs poses a complex computational challenge [1]. Optimal control theory has been extensively studied [2–6] and has been used to solve different PDE control problems in a wide range of applications [7–9], from robotics and engineering [3, 10–13] to chemistry and biomedicine [14, 15]. Optimal control requires a (forward) dynamics model of the system. These models are traditionally derived from first principles or identified directly from data, e.g. by using system identification techniques [16]. Solving optimal control problems is computationally expensive due to the underlying optimization process that repeatedly needs to integrate the model forward in time, which is especially expensive for high-dimensional systems (*curse of dimensionality*). Additionally, optimal control strategies are often sensitive to changes in the system parameters and require solving the optimal control problem for each new instance of the parameters. This makes developing PDE control techniques that are computationally efficient and adaptable to changes in the system parameters very challenging.

The recent progress in scientific machine learning has drastically changed how we can discover and analyze dynamical systems. This progress has permeated into the field of control under the name of reinforcement learning (RL) [17]. RL aims to solve control problems (i.e. sequential decision-making processes in the RL jargon), by learning an optimal control law (the policy), while interacting with a dynamical system (the environment). RL assumes no prior knowledge Urban Fasel Department of Aeronautics Imperial College London London, United Kingdom u.fasel@imperial.ac.uk of the dynamics of the system, making RL a broadly applicable control approach when deriving or learning a dynamical system model is difficult. Deep reinforcement learning (DRL) is the extension of RL using *deep* neural network (DNN) policies [18–20]. DRL has shown outstanding capabilities in controlling complex and high-dimensional systems such as games [21–27], simulated and real-world robotics [28–35], and recently PDEs [36–45]. While DNNs are critical for the success of DRL, there are several drawbacks when using them, namely (i) their sample inefficiency and high training cost, (ii) limited robustness and generalization, (iii) and lack of interpretability of the learned policies. In particular, the DNN architectures used in DRL usually contain millions of parameters and need large amounts of training data and computations, which makes them unsuitable in most real-world applications where collecting data is expensive and time-consuming. Also, the control policies are often brittle to changes in the system parameters and fail when applied in different contexts or tasks without retraining. Additionally, the learned DNN policies are difficult to interpret and explain, limiting the possibility to perform stability or robustness analysis. These limitations are especially severe when dealing with scientific and engineering applications governed by PDEs due to the high computational cost of numerically solving PDEs, the possible variation of parameters of the PDE systems, and the missing interpretability and a posteriori analyses needed for deploying such DNN-based controllers on safety-critical real-world systems.

These challenges have been the core focus of recent research in the field, and many methods have been proposed to improve the sample efficiency, generalization, and interpretability of DRL. Successful methods include unsupervised representation learning [46, 47], i.e. the problem of learning reduced-order representation of the data; imitation learning and behavioral cloning [48–50], i.e. the use of expert trajectories to initialize the policies; transfer learning [51, 52], i.e. the process of transferring learned strategies to new situations; meta-learning [53, 54], i.e. the concept of learning policies that can quickly adapt to new scenarios; and explainable artificial intelligence [55], i.e. tools to help understand and interpret DNN predictions.

In our work, we combine DRL with ideas from dictionary learning and differentiable L0 regularization. We introduce our method starting from the observation that, for many dynamical systems, optimal control policies using DNNs tend to be over-parametrized. Sparse and simple (e.g. single-layer) NNs may be sufficiently expressive to approximate optimal control laws, and are more data efficient, quicker to train, and more interpretable compared to dense and complex DNNs [56]. Moreover, sparsifying or pruning DNNs to reduce the number of parameters not only reduces the training cost, but also improves the prediction robustness of the DNN [56–60]. Sparsity can be enforced using the L0 norm, which is non-convex and non-continuous, and therefore non-differentiable and difficult to introduce in gradient-based optimization used in DRL. In our work, we use pruning techniques in combination with dictionary learning [61, 62] to identify sparse DRL policies with a limited number of trainable parameters for the control of parametric PDEs. The method is shown in Figure 1. A policy function is learned, mapping the observed PDE states m and the parameters µ
to actions a by a sparse linear combination of candidate nonlinear functions from a chosen dictionary, i.e. polynomials
(although not limited to polynomials). The polynomial features are fed to a single-layer neural network, with parameters corresponding to the coefficients of the polynomial, that are sparsified using a differentiable version of the L0 norm [56].

This implementation of the L0 norm is suitable for gradient-based optimization techniques, e.g. stochastic gradient descent (SGD) or ADAM [63], and is compatible with any DRL algorithm. Therefore, our sparse polynomial policy can be directly and simply used to replace the DNN-based policies in any policy-based and actor-critic DRL algorithm.

Additionally, the choice of the library allows us to not only avoid the use of a DNN but also to inject any available prior knowledge into the learning process.

The paper is organized as follows: in Section 2, we introduce the building blocks of our framework, namely RL, sparse dictionary learning, and L0 regularization. In Section 3, we describe our L0 sparse dictionary control policies method, and in Section 4, and 5 we show the results and discuss the findings.

## 2 Preliminaries 2.1 Problem Settings

In this work, we consider the problem of controlling continuous-time dynamical systems that evolve according to:

$\dot{\mathbf{y}}(t)=f(\mathbf{y}(t),\mathbf{a}(t);\mathbf{\mu})$
where y(t) *∈ Y* is the set of states, ˙y(t) = dy dt is the time derivative of the state, a(t) *∈ A* is the control input (or action), and µ *∈ P* is a vector of the system parameters. We assume no knowledge of the function f : *Y × A × P → Y* but we can measure the evolution of the system at different discrete-time instants, resulting in a sequence of measurements mt, mt+1, *· · ·* , mt+H. We assume that only a small finite amount of sensors are available, therefore, measurements only contain a subset of the information of the full state of the system. Similarly, we assume a small finite number of actuators for controlling our systems. The limited number of sensors and actuators makes the PDE control problem extremely challenging.

## 2.2 Reinforcement Learning

Reinforcement learning (RL) [17] is the branch of machine learning focusing on solving sequential decision-making problems. RL has its foundation in the theory of Markov decision processes (MDP). An MDP is a tuple ⟨S, A, T, R⟩
where *S ⊂* RNs is the set of observable states1, *A ⊂* RNa is the set of actions, T : *S ×S ×A −→* [0, 1]; (s′, s, a) �−→
T(s′, s, a) = p(s′|s, a) is the transition function, describing the probability p(s′|s, a) of reaching state s′ from state s while taking action a, and R : *S × A −→* R; (s, a) *�−→* R(s, a) is the reward function. Any RL algorithm aims to find the optimal policy π, i.e. the mapping of states to actions, maximizing the total cumulative return Gt:

$$G_{t}=\mathbb{E}_{\pi}[r_{0}+\gamma r_{1}+\gamma^{2}r_{2}+\cdots+\gamma^{t}r_{t}+\cdots]=\mathbb{E}_{\pi}[\Sigma_{t=0}^{H}\gamma^{t}r_{t}],\tag{2}$$
where the subscript t indicates the timestep, γ is the discount factor, rt is the instantaneous reward received by the agent at timestep t, and H the control horizon that can be either finite or infinite2. An important element of RL is the notion of value function. The value function V : *S →* R and action-value function Q : *S × A →* R quantify the total cumulative return Gt (Equation (2)) of a state s or state-action pair (s, a).

RL algorithms are usually classified as value-based, policy-based, or actor-critic [17]. Value-based methods rely only on the estimation of the (action) value function and derive the optimal policy by greedily selecting the action with the highest value at each timestep. Examples of value-based methods are Q-learning [64] and its derivations relying on deep neural networks [21, 25–27]. Second, policy-based methods directly optimize the parameters of the policies with the intent of maximizing the return Gt. The most famous policy-based method is REINFORCE [65]. Third, actor-critic algorithms learn value function and policy at the same time. Actor refers to the policy acting on the environment, and critic refers to the value function assessing the quality of the policy. Examples are deep deterministic policy gradient
(DDPG) [66], proximal policy optimization (PPO) [67], and soft actor-critic (SAC) [68].

In this work, we present a method that can replace any policy function of policy-based and actor-critic methods. In our numerical experiments, we use the state-of-the-art actor-critic algorithm twin-delayed deep deterministic policy gradient.

## 2.2.1 Twin-Delayed Deep Deterministic Policy Gradient

In this work, we rely on the twin-delayed deep deterministic policy gradient (TD3) algorithm [69]. TD3 is an actor-critic algorithm learning a deterministic policy (the actor), and action-value function (the critic) by means of neural networks of parameters ξ and θ respectively. TD3 is capable of handling continuous state and action spaces, making it a suitable candidate for controlling parametric PDEs. We indicate the parametrized policy with π(s; ξ) and the action-value function with Q(s, a; θ). The action-value function Q(s, a; θ) is updated via temporal-difference learning [17] as:

L(θ) = Est,at,st+1,rt∼M[(rt + γ ¯Q(st+1, at+1; ¯θ) − Q(st, at; θ))2] = Est,at,st+1,rt∼M[(rt + γ ¯Q(st+1, ¯π(st+1; ¯ξ) + ϵ; ¯θ) − Q(st, at; θ))2], (3)
where the so-called target networks ¯Q(s, a; ¯θ) and ¯π(s; ¯ξ) are copies of Q(s, a; θ) and π(s; ξ), respectively, with parameters frozen, i.e.

not updated in the backpropagation step, improving the stability of the training,
ϵ ∼ clip(N(0, ¯σ), −*c, c*) is the noise added to estimate the action value in the interval [−*c, c*] around the target action, and M is the memory buffer containing the samples collected by the agent while interacting with the environment. To reduce the problem of overestimation of the target Q-values, TD3 estimates two value functions, namely Q(s, a; θ1) and Q(s, a; θ2) and computes the target values as:

rt + γ ¯Q(st+1, at+1; ¯θ) = rt + γ min i=1,2 ¯Q(st+1, at+1; ¯θi). (4) (5) The target networks, parametrized respectively by ¯θ1, ¯θ2, and ¯ϕ, are updated with a slower frequency than the actor and the critic according to: ¯θ1 = ρθ1 + (1 − ρ)¯θ1 ¯θ2 = ρθ2 + (1 − ρ)¯θ2 ¯ξ = ρξ + (1 − ρ)¯ξ,
where ρ is a constant determining the speed of the updates of the target parameters.

The action-value function Q(s, a; θ) is used to update the parameters of the deterministic policy π(s; ξ). In particular, the gradient of the critic guides the improvements of the actor:

$$\mathcal{L}(\mathbf{\xi})=[\mathbb{E}_{a_{i}\sim\mathcal{M}}|-\nabla_{a}Q(\mathbf{s}_{i},\pi(\mathbf{s}_{i};\mathbf{\xi});\mathbf{\theta})|.\tag{6}$$

To further stabilize the training, the actor is updated with a lower frequency than the critic.

## 2.3 Sparse Dictionary Learning

Dictionary-learning methods are data-driven methods aiming to approximate a nonlinear function by finding a linear combination of candidate dictionary functions, e.g. polynomials of degree d or trigonometric functions. Sparse dictionary-learning techniques additionally enforce sparsity and try to balance function complexity with approximation accuracy (identifying the smallest number of non-zero dictionary functions that can still accurately approximate the nonlinear function). In the context of learning and controlling dynamical systems from data, the sparse identification of nonlinear dynamics method (SINDy) [62] can discover governing equations by relying on sparse dictionary learning.

In particular, given a set of $N$ input data $S=[s_{1},\cdots,s_{N}]$ and labeled output data $A=[a_{1},\cdots,a_{N}]$, we want to identify the unknown function $f:S\to A$ such that $s=f(a)$. To find the best approximation of $f$, we construct a relation of $\sigma$ candidate functions $\Theta(S)=[\theta_{1}(S),\cdots,\theta_{N}(S)]$. Given this dictionary, we can write the input-output relation of:

$$A=\Theta(S)\Xi\tag{7}$$

where $\Xi$ is the matrix of coefficients to be fit. In contrast with neural networks, which pose no restriction on the function class that is approximated, the choice of dictionary restricts the possible functions that can be approximated and reduces the number of learnable parameters, in this case, the coefficients of the matrix $\Xi$.

## 2.4 Sparsifying Neural Network Layers With L0 Regularization

To sparsify the weight/coefficient matrix Ξ, the differentiable L0 regularization method introduced in [56] can be used. The method relaxes the discrete nature of L0 to allow efficient and continuous optimization.

Let $d$ be a continuous random variable distributed according to a distribution $p(d|\psi)$, where $\psi$ indicates the parameters of $p(d|\psi)$. Given a sample from $d\sim p(d|\psi)$, we can define:

$$z=\min(1,\max(0,d)).\tag{8}$$
The hard-sigmoid rectification in Equation (8) allows the gate to be exactly zero. Additionally, we can still compute the probability of the gate being action, i.e. non-zero, by utilizing the cumulation distribuition function P:

$p(z\neq0|\psi)=1-P(\mathbf{d}\leq0|\psi)$.

We choose as candidate distribution a binary concrete [70, 71]. Thus, the random variable d is distributed in (0, 1) with probability density p(d|ψ), cumulative density P(d|ψ), and parameters ψ = [log α, β], with log α the location and β
the temperature parameter. The distribution can be stretched to the interval (*γ, ζ*), where *γ <* 0 and *ζ >* 1, and then the hard-sigmoid on the samples analogously to Equation (8) can be applied:

$$\mathbf{u}\sim\mathcal{U}(\mathbf{0},\mathbf{1})$$ $$\mathbf{d}=\sigma((\log\mathbf{u}-\log(1-\mathbf{u})+\log\mathbf{\alpha})/\beta)\tag{10}$$ $$\bar{\mathbf{d}}=\mathbf{d}(\zeta-\gamma)+\gamma$$ $$\mathbf{z}=\min(\mathbf{1},\max(\mathbf{0},\bar{\mathbf{d}})),$$
where σ corresponds to the sigmoid activation function. We can now optimize the parameters ψ of the distribution and introduce the L0 regularization loss as:

$$L_{0}(\psi)=\sum_{j=1}^{|\mathbf{\xi}|}(1-P_{L_{j}}(0|\psi))=\sum_{j=1}^{|\mathbf{\xi}|}\sigma(\log\alpha_{j}-\beta\log\frac{\gamma}{\zeta}),\tag{11}$$

where $\mathbf{\xi}$ are the parameters of the model we want to sparsify. At test time, we can estimate the sparse parameters $\mathbf{\xi}^{0}$ by:

$$\mathbf{z}=\min(\mathbf{1},\max(\mathbf{0},\sigma(\log\alpha)(\zeta-\gamma)+\gamma))\tag{12}$$ $$\mathbf{\zeta}^{0}=\mathbf{\xi}\odot\mathbf{z}.$$
In the context of sparse dictionary learning, replacing the L1 norm with a L0 norm has shown to be beneficial in the context of SINDy [72, 73]. Moreover, recent work shows that replacing the truncated L1 norm with the L0 loss in Equation (11) provides improved performance when combining dimensionality reduction using variational autoencoders [74] with SINDy for discovering governing equations of stochastic dynamical systems [75].

## 3 Deep Reinforcement Learning With L0-Sparse Polynomial Policies

In this work, we introduce a sample efficient, interpretable, and robust DRL approach for efficient learning of optimal policies with a limited number of parameters. We devise a general method for policy approximation using dictionary learning with L0 regularization to enforce sparsity. Our method can be used in different policy-gradient and actor-critic DRL algorithms without changing their policy-optimization procedure. Central to our method is a differentiable L0
norm to enforce sparsity in the optimal policy, which makes the method compatible with gradient-based optimizations such as SGD or ADAM.

## 3.1 Twin-Delayed Deep Deterministic Policy Gradient With L0-Sparse Polynomial Policy

With reference to Figure 1, our sparse polynomial policy maps the state of the agent s
=
[m, µ]
=
[m1, · · · , mn, µ1, · · · *, µ*p] to control inputs a, where mi corresponds to the ith-sensory measurement, and µi to the ith-parameter value. The sparse polynomial policy is constructed as follows:

1. We encode the measurements m and parameters µ into a higher-dimensional space using a library of
polynomial functions Θ of degree d, such that: [m, µ]
Θ
−→ [1, m, m2, . . . , md, . . . , µ,
µ2*, . . .* µd] = [m1, . . . , mn, µ1, . . . , µp, md
1 . . . , md
n, µd
1, . . . , µd
p, m1µ1, . . . , m1µp, *· · ·* ] = Θ(s) = ˜s.
2. We feed the polynomial features ˜s to a single-layer neural network π(˜s; ξ) to obtain the control inputs
a = π(˜s; ξ) = Θ(s)Ξ, where the weights ξ of the neural network corresponds to the learnable coefficient of
the polynomial features and Ξ is the matrix representation of ξ.
3. We sparsify the weight matrix Ξ using a binary mask Z(Ψ) = z(ψ), where Z an Ψ indicate the matrix
representation of the mask z and the parameters ψ, respectively, that are trainable using L0 regularization (see
Equation (11) in Section 2.4).
The overall policy can be defined as:

$$\mathbf{a}=\pi(\mathbf{s};\mathbf{\xi},\mathbf{\psi})=\Theta(\mathbf{s})\Xi\odot Z(\Psi),\tag{13}$$
where ⊙ corresponds to the element-wise product.

In our method, we simply replace the neural network-based policy of TD3 (see Section 2.2.1) with the sparse polynomial policy in Equation (13). Additionally, we redefine the TD3 training objectives (Equation (6)) to promote sparsity using L0 regularization (Equation (11)). The new training objective of the policy becomes:

$${\cal L}(\mathbf{\xi},\mathbf{\psi})=\mathbb{E}_{\mathbf{s}_{t}\sim{\cal M}}[-\nabla_{\mathbf{a}}Q(\mathbf{s}_{t},\pi(\tilde{\mathbf{s}};\mathbf{\xi},\mathbf{\psi});\mathbf{\theta})+\lambda L_{0}(\mathbf{\psi})],\tag{14}$$
where λ is a scaling factor for the two loss terms. The complete algorithm is shown in Algorithm 2 and the implementation is detailed in Appendix B.

## Algorithm 1 Td3 With L0-Sparse Polynomial Policies

Initialize Q(s, a; θ1), Q(s, a; θ2), and π(˜s; ξ, ψ) with random parameters θ1, θ2, ξ, ψ
Initialize target networks ¯θ1 ← θ1, ¯θ2 ← θ2, ¯ξ ← ξ, ¯ψ ← ψ
Initialize memory buffer M
Select library of dictionary functions Θ
for e = 1 : Emax do

Initialize the system and get initial measurement s0 = [m0, µ]
for t = 1 : Tmax do

Compute polynomial features ˜st = [1, mt, m2
                                         t, . . . , md
                                                  t , . . . , µ, µ2, . . . µd]
                                                                      Θ
                                                                     ←− [mt, µ]

Sample action at ∼ π(˜st; ξ, ψ) + ϵ, where ϵ ∼ N(0, σ)
Observe reward r and new measurement [mt+1, µ]
Store tuple (st, a, r, st+1) in M

if train models then

Sample mini-batch (st, a, r, st+1) from M
Compute polynomial features ˜st+1, ˜st
                                   Θ
                                   ←− [mt+1, µ], [mt, µ]

at+1 ← ¯π(˜st; ¯ξ, ¯ψ) + ϵ, where ϵ ∼ clip(N(0, ¯σ), −c, c)
qt ← rt + γ mini=1,2 ¯Q(st+1, at+1; ¯θi)
Update critic parameters according:
L(θ) = Est,at,st+1,rt∼M[(qt − Q(st, at; θ))2]
if train actor then

Update policy parameters according to:
L(ξ, ψ) = Est[−∇aQ(st, π(˜st; ξ, ψ); θ) + λL0(ψ)]
Update target networks
¯θ1 = ρθ1 + (1 − ρ)¯θ1
¯θ2 = ρθ2 + (1 − ρ)¯θ2
¯ξ = ρξ + (1 − ρ)¯ξ
¯ψ = ρψ + (1 − ρ) ¯ψ

end if

end if

end for

end for

Our method allows us to retain the expressive power of the neural networks for approximating the value function, i.e.
the expected return of the state-action pairs which may be very difficult to approximate, while exploiting the simpler
structure and interpretability of polynomials for representing a policy. The algorithm is capable of learning complex
policies with limited number of parameters, but, differently from a neural network-based policy, it returns interpretable
polynomial expressions that can be used, for stability or robustness analysis. Eventually, it is worth mentioning that our
approach can be easily adapted to any policy-gradient or actor-critic DRL algorithms such as DDPG, PPO, and SAC.

## 4 Results

To test the validity of our approach, we study two control problems of different parametric PDEs, namely the Kuramoto-
Sivashinsky (KS) and the Convection-Diffusion-Reaction (CDR) PDE. We compare our sparse L0-sparse polynomial TD3 agent, with polynomial degree d = 3, with:

- the TD3 agent with value function and policy represented by neural networks. We utilize the default TD3
hyperparameters and architecture from [69]. Details of the implementation can be found in Appendix B,
- the L1-sparse polynomial TD3 agent, where we replace the L0 regularization with an L1 regularization (see
details in Appendix B.1), and
- the TD3 agent without the parameter µ in the agent state s.

## 4.1 Kuramoto-Sivashinsky Pde

The KS is a nonlinear 1D PDE describing pattern and instability in fluid dynamics, plasma physics, and combustion, e.g. the diffusive-thermal instabilities in a laminar flame front [76]. Similarly to [44], we write the KS PDE with state y(*x, t*) = y with the addition of a parametric spatial cosine term, breaking the spatial symmetries of the equation and making the search for the optimal control policy more challenging:

$$\frac{\partial y}{\partial t}+y\frac{\partial y}{\partial t}+\frac{\partial^{2}y}{\partial x^{2}}+\frac{\partial^{4}y}{\partial x^{4}}+\mu\cos{(\frac{4\pi x}{L})}=\phi(x,a)$$ $$\phi(x,a)=\sum_{i=1}^{N_{a}}a_{i}\psi(x,c_{i})\tag{15}$$ $$\psi(x_{i},c_{i})=\frac{1}{2}\exp(-(\frac{x_{i}-c_{i}}{\sigma})^{2})$$
where ϕ(*x, a*) is the control input function with ai ∈ [−1, 1], ψ(*x, c*i) is a Gaussian kernel of mean ci and standard deviation σ = 0.8, µ ∈ [−0.25, 0.25] is the parameter of interest of the system, and D = [0, 22] is the spatial domain with periodic boundary conditions. To numerically solve the PDE, we discretize the domain with Nx = 64. We assume to have 8 equally-spaced actuators and sensors. The state of the agent is composed of 8 sensory readings and the scalar value of the parameter, making each agent state s = [m1, · · · , m8, µ] of dimension Ns = 9. The complete implementation details for simulating the KS PDE are provided in Appendix A.1. Examples of solutions for different values of µ are shown in Figure 2.

The control problem is to steer the state of the PDE y towards a desired target value with the minimum control effort. Therefore, we can write the reward function as:

$$R(y,a)=-(c_{1}+\alpha c_{2})=-\Big{(}\frac{1}{N_{x}}\sum_{k=1}^{N_{x}}(y_{k,t}-y_{0nt})^{2}+\alpha\frac{1}{N_{a}}\sum_{j=1}^{N_{x}}(a_{j,t}-a_{nt})^{2}\Big{)}\tag{16}$$

where $y_{k,t}$, $a_{j,t}$ represent respectively the $n^{0}$, $n^{3}$, and represent of the discretized state vector $\mathbf{y}_{k}$ and control input $a_{k}$ at the timestep $t$, $y_{nt}=0$, $0$, $a_{nt}=0$, and $a_{j}=0$.1. The choice of $\alpha=0.1$ is dictated by the need for balancing the contribution of the state-tracking cost $c_{1}$ and the control-filter cost $c_{2}$. In particular, it can experiments we prioritize serving the system state to the reference over the minimization of the injected energy.

We train the control policies by randomly sampling a value of the parameter µ at the beginning of each training episode.

We choose µ ∈ [−0.2, −0.15, −0.1, −0.05, 0.0, 0.05, 0.1, 0.15, 0.2]. To test the generalization abilities of the policies, we evaluate their performance on unseen and randomly-sampled parameters from [−0.25, 0.25]. Additionally, to test the robustness of the policies, during the evaluation we add noise to the sensory readings mt = mt + ϵ with ϵ ∼ N(0*, σI*)
and σ = 0.25.

In Figure 3, we show training and evaluation results of the different methods. In particular, we show the reward (see Equation (16)), the state cost c1, and the action cost c2 over training and evaluation with and without noise on the measurements. Our L0-sparse polynomial TD3 agent achieves the highest reward and the lowest total cost over training and in evaluation to unseen parameters. Therefore, enforcing sparsity, either through L0 or L1 regularization, improves the performance of the agents even in the presence of a large amount of noise on the measurements.

In Figure 4, we show examples of optimal control solutions for the KS PDE for two different values of the parameter µ using the different DRL control policies. We highlight that those specific instances of the parameter µ were never seen by the agents during training. In particular, in Figure 4a), we select a value of µ within the training range to test the interpolation capabilities of the controllers, while in Figure 4b), we select a value of µ outside the training range to test the *extrapolation* capabilites of the controllers. In interpolation regimes, the L0-sparse polynomial TD3 outperforms the L1-sparse polynomial TD3, the DNN-based TD3, and the DNN-based TD3 without the parameter µ in the agent state s. In extrapolation regimes, we observe similar performance of the L0-sparse and the L1-sparse polynomial TD3, drastically outperforming their DNN-based counterparts. First, these results show the importance of observing the parameter µ of the PDE, and second, they show the importance of enforcing sparsity when developing controllers for parametric PDEs capable of generalizing to new instances of the parameter. Compared to black-box neural networks, our method learns polynomial controllers that can be written in closed form, and that can be analyzed and interpreted. In the case of the KS PDE, starting from an observation vector of dimension 9 (8-dimensional sensory measurements and 1-dimensional parameter) and a polynomial degree d = 3, we obtain a polynomial with 220 coefficients (we allow cross products between the different variables of the vector). Since we have
8 possible control inputs, the total number of learnable parameters is 220*8=1760, excluding the L0 mask coefficients.

With only 1760 learnable coefficients, our method drastically reduces the number of learnable parameters compared to the standard 3-layers neural network used by TD3 (and in general by DRL algorithms). Examples of optimal sparse control policies are:

$$\begin{cases}a_{4}=\tanh\left(-7.524m_{4}+0.226m_{3}^{2}-2.128m_{3}m_{7}-2.659m_{8}\mu-0.691m_{1}\mu^{2}-0.317\mu^{3}\right)\\ a_{8}=\tanh\left(0.234+1.101m_{5}-1.853m_{7}-2.659m_{8}-6.481m_{8}^{3}-2.993m_{8}\mu^{2}-0.567\mu^{3}\right)\end{cases}\tag{17}$$

## A) Interpolation: 𝝁 = 𝟎. 𝟏𝟐𝟏 B) Extrapolation: 𝝁 = 𝟎. 𝟐𝟐𝟓

For Equation (17), it is possible to notice that the control laws are not only interpretable and sparse, i.e., composed of a few terms only, but they also strongly depend on local measurements, m4, m8 respectively, and on the parameter µ.

Additionally, the control laws present nonlocal terms, e.g., m1 in the first equation, indicating nonlocal information is essential to derive optimal control laws.

## 4.2 Convection-Diffusion-Reaction Pde

The CDR PDE describes the transfer of energy, or physical quantities withing a system due to convection, diffusion, and reaction processes. The CDR PDE with state y(*x, t*) = y can be written as:

$$\frac{\partial y}{\partial t}+c\frac{\partial y}{\partial x}-\nu\frac{\partial^{2}y}{\partial x^{2}}-ry=\phi(x,a)\tag{18}$$ $$\phi(x,a)=\sum_{i=1}^{N_{a}}a_{i}\psi(x_{i},c_{i}),$$

where $\psi(x_{i},c_{i})$ is a Gaussian kernel with $a_{i}\in[-0.25,0.25]$, similar to the control input function in the KS PDE problem, $c\in[0.1,0.35]$ is the convection velocity, $\nu\in[0.001,0.000]$ is the diffusivity constant, $\nu\in[0.1,0.35]$ is the reaction constant, and $\mathcal{D}=[0,1]$ is the spatial domain with periodic boundary conditions. To solve the PDE, we assume 
a spatial discretization Nx = 200. We use 8 sensors and 8 actuators. In this PDE control problem, we have three parameters µ = [*ν, c, r*], therefore, the agent state s = [m1, · · · *, m*8, µ] is of dimension Ns = 11. The implementation details for simulating the CDR PDE [77] are provided in Appendix A.2, and examples of solutions for different values of µ are shown in Figure 5.

Similarly to KS, the control problem is to steer the state towards a desired target value with the minimum control effort.

Therefore, analogously to Equation (16), we can write the reward function as:

$$R(\mathbf{y}_{t},\mathbf{a}_{t})=-(c_{1}+\alpha c_{2})=-\Big{(}\frac{1}{N_{\rm a}}\sum_{k=1}^{N_{\rm a}}(y_{k,t}-y_{\rm ref})^{2}+\alpha\frac{1}{N_{\rm a}}\sum_{j=1,t}^{N_{\rm a}}(a_{j,t}-a_{\rm ref})^{2}\Big{)},\tag{19}$$

where $y_{k,t}$, $a_{j,t}$ represent respectively the $k^{th}$, $j^{th}$ component of the full state vector $\mathbf{y}_{t}$ and control input $\mathbf{a}_{t}$, $y_{\rm ref}=0.0$, $a_{\rm ref}=0.0$, and $\alpha=0.1$.

We train the control policies by randomly sampling values of the parameters c and r from [0.1, 0.125, 0.15, 0.175, 0.2]
and ν from [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007] at the beginning of each training episode. To test the generalization ability of the policies, we evaluate their performance on unseen and randomly sampled parameters within
(interpolation) and without (extrapolation) the training range. Additionally, to test the robustness of the policies, we add noise to the measurements mt = mt + ϵ with ϵ ∼ N(0*, σI*) and σ = 0.25 during the evaluation.

In Figure 6, we show training and evaluation results of the different methods. Our L0-sparse polynomial TD3 achieves higher reward over training and in evaluation to unseen parameters. It is worth noticing that enforcing sparsity improves the performance of the control policies even in the presence of large noise on the measurements. In Figure 7, we show examples of optimal control solutions for the CDR PDE for different values of the parameter vector µ using the different control policies. We highlight that those specific instances of the parameter vector µ were never seen by the agents during training. In particular, in Figure 7a) we select a value of µ within the training range to test the *interpolation* capabilities of the controllers, while in Figure 7b), we select a value of µ outside the training range to test the *extrapolation* capabilites of the controllers. Even for the CDR PDE, in interpolation regimes, the L0-sparse polynomial TD3 outperforms the L1-sparse polynomial TD3, the DNN-based TD3, and the DNN-based TD3 without the parameter µ in the agent state s. In extrapolation regimes, we observe similar performance of the L0-sparse and the L1-sparse polynomial TD3, drastically outperforming their DNN-based counterparts. Due to the limited actuation and sensing, the CDR PDE was found to be more challenging to control than the KS PDE, making the study of its observability and controllability in parametric settings an interesting direction for future research.

## A) Interpolation: 𝝁 = [𝟎. 𝟎𝟎𝟔, 𝟎. 𝟏𝟗𝟏, 𝟎. 𝟏𝟕𝟗] B) Extrapolation: 𝝁 = [𝟎. 𝟎𝟎𝟖, 𝟎. 𝟑𝟏𝟑, 𝟎. 𝟑𝟎𝟑] 5 Discussion And Conclusion

Despite the plethora of DRL and optimal control approaches for solving PDE control problems, these methods often focus on solving the control problems for fixed instances of the PDE parameters. However, learning optimal control policies that can generalize to unseen instances of the parameters without further retraining/optimizing is crucial for reducing the computational cost of solving these control problems and for tackling complex real-world applications. In this work, we introduce a DRL framework for addressing the problem of efficient control of parametric PDEs by learning sparse polynomial control policies. To reduce the number of coefficients of the polynomials, and consequently learn sparse polynomial control policies, we use dictionary learning and differentiable L0 regularization. We test our method on the challenging problem of controlling a parametric Kuramoto-Sivashinsky PDE (Equation (15)) and a parametric Convection-Diffusion-Reaction PDE (Equation (18)). While the control of these two PDEs has been the core focus of several works, to the best of our knowledge, these problems have not been addressed in parametric settings with large variations of the parameters. Also, recent work has not focused on learning optimal control policies with limited data (data collected at a limited number of parameters) and policies that can generalize to unseen parameters. Compared to recent work [44] introducing a multi-agent DRL framework for controlling the Kuramoto-Sivashinsky PDE with parameters µ ∈ [0.0, 0.02], we extend the range of parameters by more than one order of magnitude. Additionally, our framework learns control policies that require significantly less control effort, making them more suitable for energy-constrained real-world applications.

An important advantage of learning DRL policies with sparse polynomials is that interpretable control strategies can be obtained, compared to black-box DNNs. Polynomial control policies composed of only a few active terms allow for robustness and stability analysis, which are critical when deploying the policies in real-world and safety-critical applications. Also, sparse policies are more robust to noise, making them suitable for solving real-world problems where measurements are often corrupted by noise.

In this work, we use a dictionary of polynomial functions of degree d = 3. However, our approach is not limited to polynomials. Prior knowledge of the optimal control policy can be used to choose the library accordingly. Additionally, we can incorporate constraints by removing or adding specific terms to the library, which is difficult when using DNN
policies. Our work is inspired by the recent SINDy-RL algorithm that introduces the idea of dictionary learning with DRL [45]. SINDy-RL is a unifying framework that combines SINDy and DRL to learn representations of the dynamics model, reward function, and control policy. The three main differences between SINDy-RL and our work are:

1. SINDy-RL learns a DNN control policy and then approximates the optimal policy using SINDy (i.e. sparse
dictionary learning) to obtain a sparse polynomial control policy. Approximating the DNN policy a posteriori may introduce an additional approximation error that can deteriorate the policy performance. Our control policy is sparse and polynomial by construction, without utilizing a DNN.
2. SINDy uses sequentially thresholded least squares to find sparse solutions, while our method uses a differentiable L0-norm.
3. SINDy-RL is a model-based DRL method, learning the environment dynamics in addition to the policy and
reward function. Our work focuses on a model-free approach that can generalize across different parametric PDEs.
Many control problems require learning a sequence of decisions from high-dimensional inputs. A drawback of using a library of polynomials to pre-process the observations of the DRL agent is the limited scaling of the number of features with respect to the dimension of the input and the degree of the polynomial. However, this problem can be alleviated by finding compact and low-dimensional representations of the measurements. Extending our method to use ML-based dimensionality-reduction techniques, such as autoencoders, is an exciting direction for future research.

While we introduce the problem of controlling PDEs using limited amounts of sensors and actuators as an MDP, it is worth pointing out that the MDP formulation is violated for these kinds of problems. In particular, the reward function is commonly chosen as a function of the whole state of the system, i.e., the discretized PDE, but the state of the agent does not correspond to the state of the PDE. This problem may be formulated as a partially observable MDP [17]. However, due to the underlying structure of the PDE, in practice, only limited sensing and actuation and no memory structure are needed for the agent to find the optimal policy. Therefore, we can rely on the block MDP (BMDP) formulation [78] to describe these types of control problems. In a BMDP, each observation has only one corresponding environment state and can be considered *Markovian*, i.e., a single observation contains sufficient information for determining the state of the environment [47]. However, even when the observations are Markovian, encoding the relevant information from potentially noisy measurements and deriving the optimal policy remains challenging. Details on the BMDP formulation can be found in Appendix C.

We propose a data-efficient, robust, and interpretable method for approximating DRL policies for parametric PDE
control. Our parametric PDE control approach learns sparse polynomial policies by combining dictionary learning with L0 regularization. Our approach is completely differentiable, i.e. trainable with any gradient-based optimization algorithm, and outperforms state-of-the-art DRL methods in terms of training performance and evaluation performance on unseen instances of the parameters of the PDEs, especially in the presence of measurement noise. Our method can generalize to unseen parameters of the PDE, even when trained on a small number of instances of the parameters.

This opens up exciting avenues of future work, exploring the generalization capability and data-efficiency of our DRL
method in complex real-world dynamical systems.

## References

[1] Andrea Manzoni, Alfio Quarteroni, and Sandro Salsa. *Optimal control of partial differential equations*. Springer,
2021.
[2] Frank L Lewis, Draguna Vrabie, and Vassilis L Syrmos. *Optimal control*. John Wiley & Sons, 2012.
[3] Robert F Stengel. *Optimal control and estimation*. Courier Corporation, 1994.
[4] Michael Athans and Peter L Falb. *Optimal control: an introduction to the theory and its applications*. Courier
Corporation, 2013.
[5] Donald E Kirk. *Optimal control theory: an introduction*. Courier Corporation, 2004.
[6] Arthur Earl Bryson. *Applied optimal control: optimization, estimation and control*. CRC Press, 1975.
[7] Fredi Tröltzsch. *Optimal control of partial differential equations: theory, methods, and applications*, volume 112.
American Mathematical Soc., 2010.
[8] Jacques Louis Lions. *Optimal control of systems governed by partial differential equations*, volume 170. Springer,
1971.
[9] Eurika Kaiser, J Nathan Kutz, and Steven L Brunton. Sparse identification of nonlinear dynamics for model
predictive control in the low-data limit. *Proceedings of the Royal Society of London A*, 474(2219), 2018.
[10] Feng Lin and Robert D Brandt. An optimal control approach to robust control of robot manipulators. IEEE
Transactions on robotics and automation, 14(1):69–77, 1998.
[11] Andres Goza and Tim Colonius. A strongly-coupled immersed-boundary formulation for thin elastic structures.
Journal of Computational Physics, 336:401–411, 2017.
[12] Michelle K Hickner, Urban Fasel, Aditya G Nair, Bingni W Brunton, and Steven L Brunton. Data-driven unsteady
aeroelastic modeling for control. *AIAA Journal*, 61(2):780–792, 2023.
[13] W Fred Ramirez. *Application of optimal control theory to enhanced oil recovery*. Elsevier, 1987.
[14] M Miranda, Jean-Michel Reneaume, X Meyer, Michel Meyer, and F Szigeti. Integrating process design and
control: An application of optimal control to chemical processes. Chemical Engineering and Processing: Process
Intensification, 47(11):2004–2018, 2008.
[15] George W Swan et al. *Applications of optimal control theory in biomedicine*. M. Dekker New York, 1984.
[16] Lennart Ljung. System identification. In *Signal analysis and prediction*, pages 163–173. Springer, 1998. [17] Richard S Sutton and Andrew G Barto. *Reinforcement learning: An introduction*. MIT press, 2018.
[18] Kai Arulkumaran, Marc Peter Deisenroth, Miles Brundage, and Anil Anthony Bharath. Deep reinforcement
learning: A brief survey. *IEEE Signal Processing Magazine*, 34(6):26–38, 2017.
[19] Yuxi Li. Deep reinforcement learning: An overview. *arXiv preprint arXiv:1701.07274*, 2017. [20] Vincent François-Lavet, Peter Henderson, Riashat Islam, Marc G Bellemare, Joelle Pineau, et al. An introduction
to deep reinforcement learning. *Foundations and Trends® in Machine Learning*, 11(3-4):219–354, 2018.
[21] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex
Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. *nature*, 518(7540):529–533, 2015.
[22] Deheng Ye, Zhao Liu, Mingfei Sun, Bei Shi, Peilin Zhao, Hao Wu, Hongsheng Yu, Shaojie Yang, Xipeng Wu,
Qingwei Guo, et al. Mastering complex control in moba games with deep reinforcement learning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 6672–6679, 2020.
[23] Kun Shao, Zhentao Tang, Yuanheng Zhu, Nannan Li, and Dongbin Zhao. A survey of deep reinforcement learning
in video games. *arXiv preprint arXiv:1912.10944*, 2019.
[24] Guillaume Lample and Devendra Singh Chaplot. Playing fps games with deep reinforcement learning. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 31, 2017.
[25] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and
Martin Riedmiller. Playing atari with deep reinforcement learning. *arXiv preprint arXiv:1312.5602*, 2013.
[26] Hado Van Hasselt, Arthur Guez, and David Silver. Deep reinforcement learning with double q-learning. In
Proceedings of the AAAI conference on artificial intelligence, volume 30, 2016.
[27] Ziyu Wang, Tom Schaul, Matteo Hessel, Hado Hasselt, Marc Lanctot, and Nando Freitas. Dueling network
architectures for deep reinforcement learning. In *International conference on machine learning*, pages 1995–2003. PMLR, 2016.
[28] Long-Ji Lin. *Reinforcement learning for robots using neural networks*. Carnegie Mellon University, 1992. [29] Jens Kober, J Andrew Bagnell, and Jan Peters. Reinforcement learning in robotics: A survey. The International
Journal of Robotics Research, 32(11):1238–1274, 2013.
[30] Athanasios S Polydoros and Lazaros Nalpantidis. Survey of model-based reinforcement learning: Applications on
robotics. *Journal of Intelligent & Robotic Systems*, 86(2):153–173, 2017.
[31] Nicolò Botteghi, Beril Sirmacek, Khaled AA Mustafa, Mannes Poel, and Stefano Stramigioli. On reward shaping
for mobile robot navigation: A reinforcement learning and slam based approach. *arXiv preprint arXiv:2002.04109*,
2020.
[32] Fangyi Zhang, Jürgen Leitner, Michael Milford, Ben Upcroft, and Peter Corke. Towards vision-based deep
reinforcement learning for robotic motion control. In *Australasian Conference on Robotics and Automation 2015*.
Australian Robotics and Automation Association (ARAA), 2015.
[33] Shixiang Gu, Ethan Holly, Timothy Lillicrap, and Sergey Levine. Deep reinforcement learning for robotic
manipulation with asynchronous off-policy updates. In 2017 IEEE international conference on robotics and automation (ICRA), pages 3389–3396. IEEE, 2017.
[34] Wenshuai Zhao, Jorge Peña Queralta, and Tomi Westerlund. Sim-to-real transfer in deep reinforcement learning
for robotics: a survey. In *2020 IEEE symposium series on computational intelligence (SSCI)*, pages 737–744. IEEE, 2020.
[35] Nicolò Botteghi, Khaled Alaa, Mannes Poel, Beril Sirmacek, Christoph Brune, Abeje Mersha, and Stefano
Stramigioli. Low dimensional state representation learning with robotics priors in continuous action spaces. In
2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 190–197. IEEE, 2021.
[36] H Jane Bae and Petros Koumoutsakos. Scientific multi-agent reinforcement learning for wall-models of turbulent
flows. *Nature Communications*, 13(1):1443, 2022.
[37] Gerben Beintema, Alessandro Corbetta, Luca Biferale, and Federico Toschi. Controlling rayleigh–benard
convection via reinforcement learning. *Journal of Turbulence*, 21(9-10):585–605, 2020.
[38] Michele Buzzicotti, Luca Biferale, Fabio Bonaccorso, Patricio Clark di Leoni, and Kristian Gustavsson. Optimal
control of point-to-point navigation in turbulent time dependent flows using reinforcement learning. Springer, 2020.
[39] Jean Rabault, Feng Ren, Wei Zhang, Hui Tang, and Hui Xu. Deep reinforcement learning in fluid mechanics: A
promising method for both active flow control and shape optimization. *Journal of Hydrodynamics*, 32:234–246, 2020.
[40] Colin Vignon, Jean Rabault, and Ricardo Vinuesa. Recent advances in applying deep reinforcement learning for
flow control: Perspectives and future directions. *Physics of Fluids*, 35(3), 2023.
[41] Dixia Fan, Liu Yang, Zhicheng Wang, Michael S Triantafyllou, and George Em Karniadakis. Reinforcement
learning for bluff body active flow control in experiments and simulations. Proceedings of the National Academy of Sciences, 117(42):26091–26098, 2020.
[42] Jean Rabault and Alexander Kuhnle. Accelerating deep reinforcement learning strategies of flow control through
a multi-environment approach. *Physics of Fluids*, 31(9), 2019.
[43] Chengwei Xia, Junjie Zhang, Eric C Kerrigan, and Georgios Rigas. Active flow control for bluff body drag
reduction using reinforcement learning with partial measurements. *Journal of Fluid Mechanics*, 981:A17, 2024.
[44] Sebastian Peitz, Jan Stenner, Vikas Chidananda, Oliver Wallscheid, Steven L Brunton, and Kunihiko Taira.
Distributed control of partial differential equations using convolutional reinforcement learning. Physica D:
Nonlinear Phenomena, page 134096, 2024.
[45] Nicholas Zolman, Urban Fasel, J Nathan Kutz, and Steven L Brunton. SINDy-RL: Interpretable and efficient
model-based reinforcement learning. *arXiv preprint arXiv:2403.09110*, 2024.
[46] Timothee Lesort, Natalia Diaz-Rodriguez, Jean-Franois Goudou, and David Filliat. State representation learning
for control: An overview. *Neural Networks*, 108:379–392, 2018.
[47] Nicolò Botteghi, Mannes Poel, and Christoph Brune. Unsupervised representation learning in deep reinforcement
learning: A review. *arXiv preprint arXiv:2208.14226*, 2022.
[48] Ahmed Hussein, Mohamed Medhat Gaber, Eyad Elyan, and Chrisina Jayne. Imitation learning: A survey of
learning methods. *ACM Comput. Surv.*, 50(2), 2017.
[49] Faraz Torabi, Garrett Warnell, and Peter Stone. Behavioral cloning from observation. In Proceedings of the 27th
International Joint Conference on Artificial Intelligence, pages 4950–4957, 2018.
[50] Felipe Codevilla, Eder Santana, Antonio M López, and Adrien Gaidon. Exploring the limitations of behavior
cloning for autonomous driving. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 9329–9338, 2019.
[51] Lisa Torrey and Jude Shavlik. Transfer learning. In Handbook of research on machine learning applications and
trends: algorithms, methods, and techniques, pages 242–264. IGI global, 2010.
[52] Karl Weiss, Taghi M Khoshgoftaar, and DingDing Wang. A survey of transfer learning. *Journal of Big data*,
3(1):1–40, 2016.
[53] Timothy Hospedales, Antreas Antoniou, Paul Micaelli, and Amos Storkey. Meta-learning in neural networks: A
survey. *IEEE transactions on pattern analysis and machine intelligence*, 44(9):5149–5169, 2021.
[54] Ricardo Vilalta and Youssef Drissi. A perspective view and survey of meta-learning. *Artificial intelligence review*,
18:77–95, 2002.
[55] Filip Karlo Došilovi´c, Mario Brˇci´c, and Nikica Hlupi´c. Explainable artificial intelligence: A survey. In 2018
41st International convention on information and communication technology, electronics and microelectronics
(MIPRO), pages 0210–0215. IEEE, 2018.
[56] Christos Louizos, Max Welling, and Diederik P Kingma. Learning sparse neural networks through l_0 regularization. In *International Conference on Learning Representations*, 2018.
[57] Song Han, Huizi Mao, and William J Dally. Deep compression: Compressing deep neural networks with pruning,
trained quantization and huffman coding. *arXiv preprint arXiv:1510.00149*, 2015.
[58] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. Understanding deep learning
(still) requires rethinking generalization. *Communications of the ACM*, 64(3):107–115, 2021.
[59] Dmitry Molchanov, Arsenii Ashukha, and Dmitry Vetrov. Variational dropout sparsifies deep neural networks. In
International Conference on Machine Learning, pages 2498–2507. PMLR, 2017.
[60] Karen Ullrich, Edward Meeds, and Max Welling. Soft weight-sharing for neural network compression. In
International Conference on Learning Representations, 2016.
[61] Julien Mairal, Francis Bach, Jean Ponce, and Guillermo Sapiro. Online dictionary learning for sparse coding. In
Proceedings of the 26th annual international conference on machine learning, pages 689–696, 2009.
[62] Steven L Brunton, Joshua L Proctor, and J Nathan Kutz. Discovering governing equations from data by sparse
identification of nonlinear dynamical systems. *Proceedings of the national academy of sciences*, 113(15):3932– 3937, 2016.
[63] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*,
2014.
[64] Christopher JCH Watkins and Peter Dayan. Q-learning. *Machine learning*, 8:279–292, 1992.
[65] Ronald J Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning.
Machine learning, 8:229–256, 1992.
[66] Timothy P Lillicrap, Jonathan J Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and
Daan Wierstra. Continuous control with deep reinforcement learning. *arXiv preprint arXiv:1509.02971*, 2015.
[67] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization
algorithms. *arXiv preprint arXiv:1707.06347*, 2017.
[68] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy
deep reinforcement learning with a stochastic actor. In *International conference on machine learning*, pages
1861–1870. PMLR, 2018.
[69] Scott Fujimoto, Herke Hoof, and David Meger. Addressing function approximation error in actor-critic methods.
In *International conference on machine learning*, pages 1587–1596. PMLR, 2018.
[70] Chris J Maddison, Andriy Mnih, and Yee Whye Teh. The concrete distribution: A continuous relaxation of
discrete random variables. *arXiv preprint arXiv:1611.00712*, 2016.
[71] Eric Jang, Shixiang Gu, and Ben Poole. Categorical reparameterization with gumbel-softmax. arXiv preprint
arXiv:1611.01144, 2016.
[72] Peng Zheng, Travis Askham, Steven L Brunton, J Nathan Kutz, and Aleksandr Y Aravkin. A unified framework
for sparse relaxed regularized regression: Sr3. *IEEE Access*, 7:1404–1423, 2018.
[73] Kathleen Champion, Peng Zheng, Aleksandr Y Aravkin, Steven L Brunton, and J Nathan Kutz. A unified sparse
optimization framework to learn parsimonious physics-informed models from data. *IEEE Access*, 8:169259–
169271, 2020.
[74] Diederik P Kingma and Max Welling. Auto-encoding variational bayes. *arXiv preprint arXiv:1312.6114*, 2013.
[75] Mozes Jacobs, Bingni W Brunton, Steven L Brunton, J Nathan Kutz, and Ryan V Raut. Hypersindy: Deep
generative modeling of nonlinear stochastic governing equations. *arXiv preprint arXiv:2310.04832*, 2023.
[76] Nikolai A Kudryashov. Exact solutions of the generalized kuramoto-sivashinsky equation. *Physics Letters A*,
147(5-6):287–291, 1990.
[77] Xiangyuan Zhang, Weichao Mao, Saviz Mowlavi, Mouhacine Benosman, and Tamer Ba¸sar. Controlgym: Largescale safety-critical control environments for benchmarking reinforcement learning algorithms. arXiv preprint arXiv:2311.18736, 2023.
[78] Simon Du, Akshay Krishnamurthy, Nan Jiang, Alekh Agarwal, Miroslav Dudik, and John Langford. Provably
efficient rl with rich observations via latent state decoding. In *International Conference on Machine Learning*, pages 1665–1674. PMLR, 2019.

## A Pde Implementation A.1 Kuramoto-Sivashinsky Pde

We translate into Python code, the Julia implementation of the KS PDE proposed in [44]. The parameters of our simulations are reported in Table 1.

| Parameter                | Value   |
|--------------------------|---------|
| Domain size (            |         |
| L                        |         |
| )                        | 22      |
| Spatial discretization ( |         |
| N                        |         |
| x                        |         |
| )                        | 64      |
| T                        | 300s    |
| Control starts           | 100s    |
| ∆                        | t       |
| 0.1s                     |         |
| ∆                        | t       |
| controller               | 0.2s    |
| α                        |         |
| 0.1                      |         |
| Sensors                  | 8       |
| Parameter                | 1       |
| State dimension (        |         |
| N                        |         |
| s                        |         |
| )                        | 9       |
| Actuators (              |         |
| N                        |         |
| a                        |         |
| )                        | 8       |
| Gaussian actuators       |         |
| σ                        |         |
| 0.8                      |         |

## A.2 Convection-Diffusion-Reaction Pde

For the CDR PDE, we improve the implementation of [77] by:

- replacing the support function of the actuators from a square wave to a Gaussian, and
- starting the controller at timestep 50, instead of 0, to allow the dynamics to evolve sufficiently, making the
control task more challenging.
The parameters used in our simulations are reported in Table 2.

## B Deep Reinforcement Learning Algorithms B.1 L1-Sparse Polynomial Td3

Analogously to the L0-sparse polynomial TD3, the L1-sparse polynomial TD3 replaces the neural network-based policy of TD3 (see Section 2.2.1) with a polynomial policy. However, we promote sparsity using L1 regularization. The new training objective of the policy becomes:

$$\mathcal{L}(\mathbf{\xi})=\mathbb{E}_{\mathbf{\mu}_{s},\mathbf{\mu}_{s}\sim\mathcal{N}}[-\nabla_{\mathbf{a}}Q(\mathbf{s}_{t},\mathbf{\mu}_{s}\left(\mathbf{\hat{\mathbf{s}}};\mathbf{\hat{\mathbf{\xi}}}\right);\mathbf{\theta})+\lambda L_{1}(\mathbf{\xi})],\tag{20}$$

where $\lambda$ is a scaling factor for the two loss terms and $L_{1}(\mathbf{\xi})=||\mathbf{\xi}||_{1}$. The complete algorithms is shown in Algorithm 2.

| Parameter                | Value   |
|--------------------------|---------|
| Domain size (            |         |
| L                        |         |
| )                        | 1       |
| Spatial discretization ( |         |
| N                        |         |
| x                        |         |
| )                        | 200     |
| T                        | 15s     |
| Control starts           | 5s      |
| ∆                        | t       |
| 0.1s                     |         |
| ∆                        | t       |
| controller               | 0.2s    |
| α                        |         |
| 0.1                      |         |
| Sensors                  | 8       |
| Parameters               | 3       |
| State dimension (        |         |
| N                        |         |
| s                        |         |
| )                        | 11      |
| Actuators (              |         |
| N                        |         |
| a                        |         |
| )                        | 8       |
| Gaussian actuators       |         |
| σ                        |         |
| 2.5                      |         |

## B.2 Hyperparameters

In Table 3, we report the (hyper)parameters used in the DRL algorithms, i.e., TD3, L0-sparse polynomial TD3, and L1-sparse polynomial TD3, respectively.

| Parameter                  | TD3    | L     |
|----------------------------|--------|-------|
| 0                          |        |       |
| poly. TD3                  | L      |       |
| 1                          |        |       |
| poly. TD3                  |        |       |
| batch size                 | 256    | 256   |
| hidden layer size          | 256    | 256   |
| learning rate              |        |       |
| 3                          | e      |       |
| −                          |        |       |
| 4                          | 3      | e     |
| −                          |        |       |
| 4                          | 3      | e     |
| −                          |        |       |
| 4                          |        |       |
| τ                          |        |       |
| 0.005                      | 0.005  | 0.005 |
| discount factor            |        |       |
| γ                          |        |       |
| 0.99                       | 0.99   | 0.99  |
| regularization coefficient |        |       |
| λ                          |        |       |
| -                          | 0.0005 | 0.005 |

## C Control Of Pde As A Block Markov Decision Process

In particular, a BMDP is a tuple ⟨S, A, O*, T,* Ω, R⟩ where S is the set of unobservable states, A is the set of actions, O is the observation space (here assumed Markovian), T : *S × S × A −→* [0, 1]; (s′, s, a) *�−→* T(s′, s, a) = p(s′|s, a) is the transition function, R : *S × A −→* R; (s, a) *�−→* R(s, a) is the reward function, and Ω : O × S × A −→
[0, 1]; (o, s, a) *�−→* Ω(o, s, a) = p(o|s, a) is the observation function.

## Algorithm 2 Td3 With L1-Sparse Polynomial Policies

Initialize Q(s, a; θ1), Q(s, a; θ2), and π(˜s; ξ) with random parameters θ1, θ2, ξ
Initialize target networks ¯θ1 ← θ1, ¯θ2 ← θ2, ¯ξ ← ξ
Initialize memory buffer M
Select library of dictionary functions Θ
for e = 1 : Emax do

Initialize the system and get initial measurement s0 = [m0, µ]
for t = 1 : Tmax do

Compute polynomial features ˜st = [1, mt, m2
                                         t, . . . , md
                                                  t , . . . , µ, µ2, . . . µd]
                                                                      Θ
                                                                     ←− [mt, µ]

Sample action at ∼ π(˜st; ξ) + ϵ, where ϵ ∼ N(0, σ)
Observe reward r and new measurement [mt+1, µ]
Store tuple (st, a, r, st+1) in M

if train models then

Sample mini-batch (st, a, r, st+1) from M
Compute polynomial features ˜st+1, ˜st
                                   Θ
                                   ←− [mt+1, µ], [mt, µ]

at+1 ←= ¯π(˜st; ¯ξ) + ϵ, where ϵ ∼ clip(N(0, ¯σ), −c, c)
qt ← rt + γ mini=1,2 ¯Q(st+1, at+1; ¯θi)
Update critic parameters according:
L(θ) = Est,at,st+1,rt∼M[(qt − Q(st, at; θ))2]
if train actor then

Update policy parameters according to:
L(ξ, ψ) = Est[−∇aQ(st, π(˜st; ξ); θ) + λL1(ξ)]
Update target networks
¯θ1 = ρθ1 + (1 − ρ)¯θ1
¯θ2 = ρθ2 + (1 − ρ)¯θ2
¯ξ = ρξ + (1 − ρ)¯ξ

