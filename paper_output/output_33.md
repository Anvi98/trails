# Optimizing Queues With Deadlines Under Infrequent Monitoring

Faraz Farahvash and Ao Tang Abstract— In this paper, we aim to improve the percentage of packets meeting their deadline in discrete-time M/M/1 queues with infrequent monitoring. More specifically, we look into policies that only monitor the system (and subsequently take actions) after a packet arrival. We model the system as an MDP and provide the optimal policy for some special cases. Furthermore, we introduce a heuristic algorithm called "AB-n" for general deadlines. Finally, we provide numerical results demonstrating the desirable performance of "AB-n" policies.

## I. Introduction

In recent years, there have been a lot of queuing systems where packets have a deadline to meet [1], [2], [3]. Such queuing systems are called "real-time queuing systems" in the literature [4]. In these systems, packets missing their deadline are discarded. Thus, using smart queuing policies to increase the percentage of packets meeting their deadline is needed.

The classical result proposed by [5] states that the "Earliest Deadline First (EDF)" policy minimizes the percentage of packets missing their deadline in G/M/c + G queues. There have been numerous papers analyzing EDF. An approximation performance analysis is done by [6]. Also, [4] does a heavy traffic analysis for EDF queues. [7] argues that EDF is not necessarily optimal for wireless channels where queue failures can happen. Other related works include but are not limited to [8], [9], [10], [11], and [12].

A key assumption for the optimality of EDF policies is that a packet is dropped from the queue (or server)
as soon as its deadline elapses. Enforcing that requires the policy to constantly monitor the system. This is not always feasible. In this paper, we will look into cases where the queuing policy can only monitor the system infrequently. Infrequent monitoring will result in a possibility of packets being served past their deadline. Thus, to prevent that, dropping policies will have to drop packets before their deadline. However, by dropping packets prematurely, we can lose packets that could have made their deadline. Analyzing this tradeoff is the center of this paper.

More specifically, we will analyze a discrete-time M/M/1 queue where the policy can only drop packets after a packet arrival event happens. We assume all the packets have the same hard deadline (D). We use two different approaches to this problem.

As a first approach, we write the optimization problem as a Markov Decision Process (MDP). We find the optimal policies for small deadlines (D = 2, 3). We also mention some observations and properties of the optimal policies.

Noting that finding the optimal policy for general deadline using the MDP approach is inefficient, we will provide a heuristic policy called "AB − n". This policy reduces the computation complexity by only considering the first n packets in the queue and maximizing their chances of meeting their respective deadlines. We will show that this policy outperforms the previously proposed algorithms.

The rest of the paper is organized as follows. In section II, we formulate the problem and discuss the notion of extended states and infrequent monitoring. In section III, some previous results (namely EDF and DPGP) are mentioned. In section IV, we formulate the MDP for this problem. Section V presents the results for the optimal policy stemming from the MDP. The heuristic policy AB − n is introduced in section VI.

Section VII presents some experiments. Section VIII concludes the paper.

## Ii. Problem Formulation

In this section, we formally define the problem. We will use the conventional discrete-time model for the M/M/1 queue described in [13]. The time is divided into time slots of unit duration, and we have the following rules:

- At each time slot, at most one packet arrival or
service happens. Arrival and service can not occur at the same time slot.
- Events in different time slots are independent.
- At each time slot, an arrival happens with probability λ. If the queue is not empty, a packet service happens with probability µ.

Furthermore, all packets have the same hard deadline (D). Packets that do not meet the deadline are rendered pointless. We are trying to maximize the percentage of packets that meet their deadline.

At each time, the queue is recorded as T
=
(T1, ..., TN) where Ti is the age of the ith packet (i.e., the time elapsed since its arrival). We assume T1 is the head of the queue and TN is the tail. This is the same definition presented at [14] as extensive states.

Finally, unlike previous results (i.e., EDF), the queue is only monitored after a packet arrival (infrequent monitoring). In other words, the policy is only allowed to drop a packet (or packets) after a packet arrives at the queue. Packets are only dropped from the head of the queue.

## Iii. Previous Results

In this section, we will present some previous results that will serve as points of comparison. More specifically, we will look into two specific policies (DPGP and EDF) and explain why these policies are not optimal in our model.

## A. Earliest Deadline First (Edf)

In the real-time queuing literature, [5] provides the following definition for the Earliest Deadline First (or Shortest Time to Extinction (STE)) Policies and proves that EDF is the optimal policy for the discrete-time G/M/c+G queue.

Definition. A policy is an Earliest Deadline First policy
if (1) at any time, it always schedules the available packet
closest to its deadline, (2) the servers are always busy as
long as there are available packets (there are no forced idle
times), and (3) the packets are discarded (removed from the
queue and server) as soon as their deadline elapses.

Remark. Note that the third condition for EDF policies can
not be enforced with infrequent monitoring (the policy is only
allowed to drop at certain time slots).

  In the next part, we will provide an intuitive example
to illustrate the reason why EDF can be sub-optimal
with infrequent monitoring.

## B. An Intuitive Example

Let's assume we are looking into the queue at time slot t. Also, let the packet at the head of the queue (p1)
and the second packet (p2) have k and k + k′ timeslots till their deadline, respectively. We are interested in the expected number of the packets making their deadline out of these two packets (we ignore the rest of the queue). We want to see whether dropping the packet at the head of the queue at time t can increase this probability.

First, we look into the constant monitoring case.

By dropping the packet at the head of the queue at time t, the second packet will have k + k′ timeslots to be served. Thus, the expected number of packets served before their deadline is equal to A = 1 −
(1 − µ)k+k′. Now, by not dropping the packet, p1 will have k timeslots to be served. Furthermore, p2 will have at least k′ timeslots to be served. (because of the constant monitoring p1 is dropped after k timeslots if not served.) Hence, the expected number of packets being served is at least B = 2 − (1 − µ)k − (1 − µ)k′. It is easy to see that ∀k, k′ ∈ N, µ ∈ (0, 1), B ≥ A. Thus, dropping a packet before its deadline never increases the expectation (regardless of the values of t, k, k′, µ).

Now, we go back into the infrequent monitoring case.

Here, by dropping the packet at the head of the queue at time t, the desired expected value will be the same as the constant monitoring case (i.e., A). Finally, if we decide to not drop the packet at time t, p1 will still have k timeslots to be served. But contrary to the frequent monitoring case, p2 can have less than k′ timeslots to be served (depending on the next arrival and departure times). Thus, there exist cases where dropping will increase the expectation. We will inspect these cases more thoroughly in future sections.

C. Drop Positive Gain Policy (DPGP)
[14] argues that when deciding to drop a packet, two factors should be considered:

1) The probability of the packet making the deadline 2) The impact of the packet being dropped on the
probability of other packets meeting their respective deadlines.
Remark. The probability of the ith packet making the deadline is equal to Iµ(i, D − Ti − i + 1), Where I is the regularized incomplete beta function [15] (Section 6.6).

To formally compute the trade-off of the two factors, the paper introduces the concept of gain as follows (The original definition is for the continuous time queue. We change the definition to fit the discrete model).

Definition. The gain of dropping the ith packet in state s is defined as:

$$gain_{i}^{s}(\mu)=-I_{\mu}(i,D-T_{i}-i+1)\tag{1}$$ $$+\sum_{j=i+1}^{N}\left(I_{\mu}(j-1,D-T_{j}-j+2)-I_{\mu}(j,D-T_{j}-j+1)\right)$$

Using the gain function defined above and by proving that the gain function is maximized at the head of the queue, [14] introduces the Drop Positive Gain Policy as follows:

"Drop the packet at the head of the queue if and only if the $gain_{1}^{s}(\mu)>0$."
Remark. gain is a myopic concept and ignores future system evolution (packet arrival, service, or drop). Thus, DPGP is not the optimal policy.

Now that we have established that the previously proposed policies are not optimal, we will provide two different approaches to finding better policies. First, in section IV, we will try to find the optimal policy by formulating the queue as an MDP. Next, in section VI, using the intuition gained from the example above, we propose a heuristic policy.

IV. QUEUE AS AN MDP
Markov Decision Processes (MDPs) are used for making a sequence of decisions in situations where the outcomes are uncertain. This framework can fit the queue optimization problem that we are analyzing in this paper. The MDP we use for this problem is an infinite-horizon MDP where we are trying to maximize the average reward per stage

## A. General Definition

An MDP is defined as M = (S, A, P, r) where:

- S is the state space.
- A is the action space. It maps a state to admissible actions for that state.

In other words A : S → {*actions*}.

- P is the transition function. P : S *× A →* ∆(S)
where ∆(S) is the space of probability distributions
over S. In simple words, P explains the transition probability from a state and an action taken when in that state, to a new state.
* r is the reward function. $r:S\times\mathcal{A}\rightarrow\mathbf{R}$. $r(s,a)$ is the stage reward associated with taking action $a$ in state $s$. In a more general framework, $r(s,a)$ can be a random variable. We will try to optimize the average reward per stage starting from state $s$ (using policy $\pi$), which is defined as: $$J^{\pi}(s)=\lim_{N\rightarrow\infty}\frac{1}{N}\mathbf{E}\left[\sum_{t=0}^{N-1}r(s_{t},a_{t})|\pi,s_{0}=s\right]$$
In the next part, we will formulate the problem of maximizing the expected percentage of packets meeting the deadline as an MDP.

## B. Mdp Design

To derive the MDP for this problem, we will define each of $(S,\mathcal{A},P,r)$. We also note that state transitions will happen after a packet arrives, is served, or is dropped.

_1) S:_ The states are the same as $T$ (extensive states) with two additional binary bits $(b_{a},b_{r})$ which are defined as below:

$$b_{a}=\begin{cases}1,&\text{If we are allowed to drop packets}\\ 0,&\text{otherwise}\end{cases}\tag{2}$$
And:

$$b_{r}=\begin{cases}1,&\text{If}b_{a}=0\text{and the previously served}\\ &\text{packet made the deadline}\\ 0,&\text{otherwise}\end{cases}\tag{3}$$

In other words, $b_{a}$ accounts for whether or not a packet service was the reason for the previous state transition (this will help us define the action space). $b_{r}$ shows that if the previous state transition was caused by a packet service, whether the packet made the deadline or not (this will help us define the reward function).

To conclude, state s can be defined as:

$$s=((T_{1}^{s},...,T_{n}^{s}),b_{a}^{s},b_{r}^{s})$$
2) A: To define the action space, we will use ba. We have two possibilities:

- bs
a = 0: If bs
a = 0, a packet service was the reason
for the previous state transition. Thus, we are not allowed to drop a packet and:
$${\mathcal{A}}(s)=\{{\bar{d}}\}$$
Where ¯d means not dropping a packet.

- bs
a = 1: If bs
a = 1, a packet service was not the
reason for the previous state transition. Thus, we are allowed to drop a packet and:
$$\mathcal{A}(s)=\{\bar{d},d\}$$

Where $\bar{d}$ means not dropping a packet, and $d$ means dropping the packet at the head.
3) $P$: We will first provide the following lemma.

Lemma 1. If the queue is not empty, the interval between
two consecutive state transitions comes from a geometric
distribution with parameter λ + µ and the probability of an
arrival triggering the state transition is
                              λ

λ+µ.

Proof. If the queue is not empty, the probability of no
arrival and no service (failure) in a slot is 1 − µ − λ.
Thus, the probability distribution of the first success
(arrival or packet service) is geom(λ + µ). The proba-
bility of the success being from arrival is
                                                λ

λ+µ.

Remark. If the queue is empty, the interval between two
consecutive state transitions comes from a geometric distri-
bution with parameter λ.

  To describe the transition function, we condition it
on the action taken:

- a = d: The next state will be:
$$s^{\prime}=((T_{2}^{s},\ldots,T_{n}^{s}),1,0)$$
with probability 1.
- a = ¯d: Here the next state is stochastic. We have:
- n=0: Then the next state will be
$$s^{\prime}=((0),1,0)$$
with probability 1.

- n > 0: Then using lemma 1, we get that with
probability
λ
λ+µ:
$$s^{\prime}=((T_{1}^{s}+K,...,T_{n}^{s}+K,0),1,0)$$

where $K\sim\text{geom}(\lambda+\mu)$.

Otherwise, with probability $\frac{\mu}{\lambda+\mu}$:

$$s^{\prime}=((T_{2}^{s}+K,...,T_{n}^{s}+K),0,b_{r}^{s^{\prime}})$$

where $K\sim\text{geom}(\lambda+\mu)$ and:

$$b_{r}^{s^{\prime}}=\begin{cases}1,&\text{If}K\leq D-T_{1}^{s}\\ 0,&\text{Otherwise}\end{cases}$$
4) r: The reward function is pretty simple:
$$r(s,a)=2b_{r}^{s}$$
In the next part, we will provide reasoning on the equivalence of the MDP defined above and the optimization problem itself.

C. On the equivalence of the MDP and original problem
Note that we are optimizing:

$$J^{\pi}(s)=\lim_{N\to\infty}\frac{1}{N}\mathbb{E}\left[\sum_{t=0}^{N-1}r(s_{t},a_{t})|\pi,s_{0}=s\right]$$
Now, first, note that each packet causes two state transitions (once with arrival and once with departure). Thus, asymptotically speaking, if we let the number of packets till state transition number N be YN, we have:

$$\lim_{N\to\infty}\frac{Y_{N}}{N}=\frac{1}{2}$$

and thus, we can rewrite $J^{\pi}(s)$:

$$J^{\pi}(s)=\lim_{N\to\infty}\frac{1}{2Y_{N}}\,\mathbf{E}\left[\sum_{t=0}^{N-1}2b_{r}^{s_{t}}|\pi,s_{0}=s\right]$$

$\sum_{t=0}^{N-1}b_{r}^{s_{t}}$ is equal to the number of packets meeting the deadline till N. Thus:

$$\lim_{N\to\infty}\frac{1}{Y_{N}}\,\mathbf{E}\left[\sum_{t=0}^{N-1}b_{r}^{s_{t}}|\pi,s_{0}=s\right]=\mathbf{P}(\text{meeting the deadline})$$
Thus, an optimal policy for the MDP problem maximizes the expected percentage of packets meeting the deadline. Furthermore, the reward incurred by a policy on the MDP is the same as the probability of a packet meeting the deadline if policy π is implemented for the original problem.

Thus, to the extent of our interest, these two problems are equivalent.

## V. Mdp Optimization

In this section, we present results on the optimal policies for the MDPs presented in previous sections.

As the number of states is infinite (or with some considerations mentioned in the next part, exponential), it is not efficient to solve this MDP using methods such as policy iteration or value iteration. But, we will provide the optimal policy for some special cases (i.e., D = 2, 3)
A. The case D=2
Here, we would define the optimal policy for the special case where the deadline is equal to 2. Any optimal policy would drop the packets that have missed the deadline (If they are allowed to drop packets). Furthermore, the queue under any optimal policy will never have a length of more than 3. Finally, if Ti ≥ D, we will say Ti = D since we only care that the packet has missed the deadline. Also, for simplicity define
α = λ + µ.

Using the above considerations, the queue for D=2
will have 9 possible states. We will describe the state transitions here:

1) ((), 0, 0): The only possible action is not dropping,
and the next state will be ((0), 1, 0) with probability 1.
2) ((), 0, 1): The only possible action is not dropping,
and the next state will be ((0), 1, 0) with probability 1.
3. $((0),1,0)$: The only possible action is not dropping (as if we drop the packet here, we will circulate between state $1$ and this state forever, and the reward would be zero.) We have: $$((0),1,0)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\mu\frac{(1-\alpha)^{2}}{\alpha}\\ ((),0,1),&\text{wp}\mu(2-\alpha)\\ ((1,0),1,0),&\text{wp}\lambda\\ ((2,0),1,0),&\text{wp}\lambda\end{cases}$$
4. $((1),0,1)$: The only possible action is not dropping, and the next state will be: $$((1),0,1)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\mu\frac{(1-\alpha)}{\alpha}\\ ((),0,1),&\text{wp}\mu\\ ((2,0),1,0),&\text{wp}\frac{\lambda}{\alpha}\end{cases}$$
5. $((2),0,0)$: The only possible action is not dropping, and the next state will be: $$((2),0,0)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\frac{\mu}{\alpha}\\ ((2,0),1,0),&\text{wp}\frac{\lambda}{\alpha}\end{cases}$$
6) ((1, 0), 1, 0): This is the most important state, and
we have two possible actions:
- Drop packet 1: The next state will be ((0), 1, 0)
with probability 1.
* Don't drop: The next will be:

((1), 0, 1),
wp µ
((2), 0, 0),
wp µ 1−α

$$((1,0),1,0)\ {\xrightarrow{d}}\ \Bigg\}$$

α
((2, 1, 0), 1, 0),
wp λ
((2, 2, 0), 1, 0),
wp λ(1−α)
α

$$\bigstar|$$
7) ((2, 0), 1, 0):
Any
optimal
policy
would
drop
packet 1 as it has missed its deadline. Thus, the
next state will be ((0), 1, 0).
8) ((2, 1, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((1, 0), 1, 0).
9) ((2, 2, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((2, 0), 1, 0).
Thus, any policy has to decide which action to take in
state 6. Let's see what decision DPGP makes. gains
1(µ)
is equal to:
$$g a i n_{1}^{s}(\mu)=(\mu+\mu(1-\mu))-\mu^{2}-\mu=\mu-2\mu^{2}$$
Thus, DPGP will be:

$$a(s_{6})=\begin{cases}d,&\text{if}\mu<0.5\\ \bar{d},&\text{if}\mu\geq0.5\end{cases}\tag{4}$$

To compute the optimal policy, let $\pi^{d}$ be the stationary distribution of the Markov chain induced by policy 
d on our MDP. Now, by definition of the reward (r =
2br), the percentage of packets meeting the deadline will be 2(πd
2 + πd
4).

Thus, given λ, µ, the optimal policy maximizes
2(πd
2 + πd
4) (Call that AR(λ, µ)).

Depending on µ and λ, the optimal policy has one of these two forms:

$$\begin{array}{l l}{{\bullet}}&{{a(s_{6})=d}}\\ {{\bullet}}&{{a(s_{6})=\bar{d}}}\end{array}$$
We will compute the rewards of each policy and compute the optimal policy.

1) a(s6) = d: If we decide to drop from the head in
state 6, the Markov chain will have the structure shown in Fig. 1. The transition matrix would have the format
(deleting the states that we will never enter ):
$$P={\begin{bmatrix}1:&0&0&1&0&0\\ 2:&0&0&1&0&0\\ 3:&\mu\frac{(1-\alpha)^{2}}{\alpha}&\mu(2-\alpha)&0&\lambda&\lambda\frac{1-\alpha}{\alpha}\\ 6:&0&0&1&0&0\\ 7:&0&0&1&0&0\end{bmatrix}}$$
To compute the stationary distribution, we must have πP = π. We have:

$$\pi_{1}+\pi_{2}+\pi_{3}+\pi_{6}+\pi_{7}=1\tag{5}$$ $$\pi_{3}=\pi_{1}+\pi_{2}+\pi_{6}+\pi_{7}$$ (6) $$\pi_{2}=\mu(2-\alpha)\pi_{3}\tag{7}$$
Combining equation 5 and 6, we get that π3 = 0.5
and plugging it in equation 7, we get:

$$AR_{1}(\lambda,\mu)=2(\pi_{2}^{d}+\pi_{4}^{d})=\mu(2-\alpha)\tag{8}$$
2) a(s6) = ¯d: If we decide not to drop from the head
in state 6, the Markov chain will have the following
transition matrix
1. Without going into further detail, we present the stationary distribution for important states:

$$\pi_{2}=\frac{\mu}{2}[(2-\alpha)(1-\lambda)+\mu],\qquad\pi_{4}=\frac{\mu\lambda}{2}$$

We have:

$$\begin{split}AR_{2}(\lambda,\mu)&=2(\pi_{2}^{d}+\pi_{4}^{d})\\ &=\mu(2-\alpha)+\lambda\mu[2\mu+\lambda-1]\end{split}\tag{9}$$

Thus, the optimal policy would decide to drop the packet in state 6 if and only if $AR_{1}(\lambda,\mu)>AR_{2}(\lambda,\mu)$. This will happen when:
AR1(λ, µ) > AR2(λ, µ) ↔ 2µ + λ < 1

Therefore, the optimal policy is described below:

$$a^{*}(s_{6})=\begin{cases}d,&\text{if}2\mu+\lambda<1\\ d,&\text{Otherwise}\end{cases}\tag{10}$$
Fig. 2 shows the boundary of the optimal policy. For any pair (λ, µ) below the red line, the optimal policy would drop from the head when at state (1,0). Similarly, for any pair (λ, µ) above the red line, the optimal policy wouldn't drop any packets at state (1,0).

Remark. Note that DPGP is the same as the optimal policy
for λ = 0. This is true as DPGP ignores any effect that a
new arrival has on the system. Thus, for small arrival rates,
the myopic gain computed by DPGP is close to the actual
gain.

$$P=\begin{bmatrix}0&0&1&0&0&0&0&0&0\\ \mu\frac{(1-\alpha)^{2}}{\alpha}&0&1&0&0&0&0&0\\ \mu\frac{(1-\alpha)}{\alpha}&\mu(2-\alpha)&0&0&0&\lambda&\lambda\frac{1-\alpha}{\alpha}&0&0\\ \mu\frac{1}{\alpha}&\mu&0&0&0&0&\frac{\lambda}{\alpha}&0&0\\ \frac{\mu}{\alpha}&0&0&0&0&0&\frac{\lambda}{\alpha}&0&0\\ 0&0&0&\mu&\mu\frac{(1-\alpha)}{\alpha}&0&0&\lambda&\lambda\frac{1-\alpha}{\alpha}\\ 0&0&1&0&0&0&0&0\\ 0&0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&1&0&0\\ \end{bmatrix}$$

## B. The Case D=3

Here, we will define the optimal policy for the special case where the deadline is equal to 3. We have the same considerations as D=2. Without going into further detail (for a complete analysis, visit Appendix A), we mention that the system will have 20 states, and the optimal policy should decide in 3 different states (that are non-trivial) whether to drop from the head or not drop at all.

- ((1,0),1,0) - ((2,0),1,0)
- ((2,1,0),1,0)
We see that, depending on (λ, µ), the optimal policy has one of the following forms:
(a) Drops in all of the above states.

(b) Drops in states ((2,1,0),1,0) and ((2,0),1,0).

(c) Only drops in state ((2,1,0),1,0).

(d) Drops in none of the above states.

Fig. 3 shows the boundaries of the optimal policy.

(For the computation of these boundaries, visit Appendix A). For any pair (λ, µ) below the blue line, the optimal policy would be (a). For (λ, µ) between red and blue lines, policy (b) would be optimal. If the point is between red and yellow lines, we would only drop in the state ((2, 1, 0), 1, 0) (i.e., policy (c)). Finally, if we are above the yellow line, (d) is the optimal policy.

Alternatively, for any point below the yellow line, we would drop at state ((2,1,0),1,0). If (λ, µ) is below the red line, an optimal policy would drop at state ((2,0),1,0), and for all parameters below the blue line, we would drop at state ((1,0),1,0).

## C. On Properties Of The Boundaries

In this section, we will present some key properties of the boundaries of the optimal policies for general deadline D. (The boundaries for special cases can be seen in Fig. 2, 3, and 4)
From now on, for any state s, we will refer to the boundary point at λ = 0 as M(s). Also, we let µbound to be the service rate where gains
1(µs bound) = 0.

Theorem 1. *For any state s, M*(s) = µs bound.

Proof. If the arrival rate is equal to zero, we have two important observations:

1) The reward only depends on the packets already
in the system (there will not be packet arrivals).
2) As there are no arrivals in the future, we can
not drop any packets in the future, and thus the
probability of the ith packet making the deadline
is exactly Iµ(i, D − Ti − i + 1) if we decide to keep the packet at the head and Iµ(i − 1, D − Ti − i + 2)
if we decide to drop. (III-C)
Thus, the M(s) would be the service rate where the
gain is indifferent to the dropping policy at s. In other
words:
$$\sum_{j=1}^{N}I_{M(s)}(j,D-T_{j}-j+1)=\sum_{j=2}^{N}I_{M(s)}(j-1,D-T_{j}-j+2)$$
By a little rearrangement, we get:

$$\sum_{j=2}^{N}\left(I_{M(s)}(j-1,D-T_{j}-j+2)-I_{M(s)}(j,D-T_{j}-j+1)\right)$$ $$-I_{M(s)}(1,D-T_{1})=0$$
Which means:

$$gain_{1}^{s}(M(s))=0\to M(s)=\mu_{bound}^{s}\tag{11}$$
Finally, we will present a conjecture we suspect to be true regarding the boundary lines.

Conjecture 1. For a given deadline D, non-trivial states
have an ordering. More specifically, let Bs(λ) be the bound-
ary curve for the optimal policy at non-trivial state s. These
curves don't cross. More precisely:

$$\frac{\mathrm{d}s_{1},s_{2}\in S,\lambda<1:B^{s_{1}}(\lambda)=B^{s_{2}}(\lambda),B^{s_{1}}(\lambda)\neq1-\lambda\tag{12}$$
VI. HEURISTIC POLICY (AB − n)
As established in the previous section, finding the optimal policy using the MDP method is not feasible for larger deadlines. Thus, in this section, we will introduce a heuristic algorithm to approximate the optimal policy.

To do that, we will look back into the example provided in section III-B. Recall that we are looking into the first two packets at the head of the queue (with k and k + k′ timeslots until expiration), and we are trying to maximize the expected number of packets meeting their deadline out of the two packets.

If we decide to drop the packet at the head of the queue, the expectation is equal to A2(k, k′) = 1 − (1 −
µ)k+k′. Now, we compute the expectation without dropping the packet. Call this number B2(k, k′). We calculate this value by conditioning on the next event (arrival or departure). There are three types of possibilities for the next event.

1) An arrival event happens before the deadline of
the first packet: In this case, the expected value is
equal to *max*(A2(k − i, k′), B2(k − i, k′)) where i is
the time of the packet arrival.
2) A departure event happens before the deadline of
the first packet: In this case, the expected value is
equal to 2 − (1 − µ)k+k′−i where i is the time of the
packet departure.
3) An arrival or departure event happens after the
deadline of the first packet: In this case, the expected value is equal to 1 − (1 − µ)k+k′−i where i
is the time of the event happening.
Putting all the results above together, we get:

$$B_{2}(k,k^{\prime})=$$ $$\sum_{i=1}^{k}\lambda(1-\lambda-\mu)^{i-1}\underbrace{\max(A_{2}(k-i,k^{\prime}),B_{2}(k-i,k^{\prime}))}_{1}$$ $$+\sum_{i=1}^{k}\mu(1-\lambda-\mu)^{i-1}\underbrace{(2-(1-\mu)^{k+k^{\prime}-i})}_{2}$$ $$+\sum_{i=k+1}^{k+k^{\prime}}(\mu+\lambda)(1-\lambda-\mu)^{i-1}\underbrace{(1-(1-\mu)^{k+k^{\prime}-i})}_{3}\tag{13}$$

**Remark**.: _Note that $B_{2}(k,k^{\prime})$ only depends on $B_{2}(l,k^{\prime})$ with $l\leq k$. Thus, we can calculate $B_{2}(k,k^{\prime})$ without the need to solve linear equations._
Now, that we have calculated B2(k, k′), we can introduce the "AB − 2" policy:
AB − **2 Policy:** While deciding whether to drop in state T, the AB − 2 policy will drop the packet if and only if either T1 ≥ D or |T| > 1 and A2(D − T1, T2 − T1) >
B2(D − T1, T2 − T1).

Remark. *If the deadline is equal to 2 (D=2), the AB* − 2
policy would drop in state T = (1, 0) (the only nontrivial state) iff λ + 2µ < 1 which is the same as the optimal policy.

Note that by extending the number of packets considered in the expected value, we can improve the AB − 2 policy (We call it the Ab − n policy where n is the number of packets considered). A3 and B3 for AB − 3 policy can be seen in equations 14 and 15
respectively.

## Vii. Numerical Results And Experiments

In this section, we will present some numerical examples and experiments pertaining to the results of this paper.

## A. The D=4 Case

Here, we will experimentally find the optimal policy for the case where the deadline is equal to 4. In this case, we have 7 non-trivial states where our policy has to decide. To find the optimal policy, we implement the M/M/1 queue with different λ and µ using each policy and find the policy that maximizes the percentage of packets meeting their deadline. Fig. 4 shows the boundary of the optimal policies. For any pair (λ, µ) below each line, the optimal policy would drop from the head when at that state. For instance, if (λ, µ) is below the green line, we would drop at state ((3, 1, 0), 1, 0).

## B. Ab − N With Different N Values

Fig. 5, compares the performance of AB − n policies with different values of n for λ = 0.3, µ = 0.2. As can be seen, the percentage of packages meeting their deadlines improves by increasing the value of n, but the rate of improvement decreases as n gets larger.

## C. Ab − 5 Vs Dpgp And Edf

Fig. 6 compares the performance of AB − 5 policy with DPGP and EDF introduced in section III. Both EDF with frequent and infrequent monitoring are used.

AB − 5 outperforms both DPGP and infrequent EDF
for shorter deadlines. For larger deadlines, the performance of DPGP and AB − 5 becomes almost identical.

Generally speaking, we observe that, by increasing the deadline, DPGP will eventually outperform AB − n
(albeit slightly). But, by increasing n this phenomenon happens later.

## Viii. Conclusion

In this paper, we looked into discrete time M/M/1
queues where packets have a hard deadline. We assumed that continuous monitoring of the system is not feasible. Thus, we introduced infrequent monitoring, where the system is only monitored after a packet arrival event happens. We tried to maximize the percentage of packets meeting their deadline.

$$A_{3}(k_{1},k_{2},k_{3})=\max(A_{2}(k_{1}+i_{2},k_{3}),B_{2}(k_{1}+k_{2},k_{3}))\tag{14}$$

$$B_{3}(k_{1},k_{2},k_{3})=\sum_{i=1}^{k_{1}}\lambda(1-\lambda-\mu)^{i-1}\max\left(A_{3}(k_{1}-i,k_{2},k_{3}),B_{3}(k_{1}-i,k_{2},k_{3})\right)+$$ $$+\sum_{i=1}^{k_{2}+k_{3}}\lambda(1-\lambda-\mu)^{i-1}\max\left(B_{2}(k_{1}+k_{2}-i,k_{3}),A_{2}(k_{1}+k_{2}-i,k_{3})\right)+$$ $$+\sum_{i=1}^{k_{1}+k_{2}+k_{3}}\lambda(1-\lambda-\mu)^{i-1}(1-(1-\mu)^{k_{1}+k_{2}+k_{3}-i})+$$
We had two approaches to this problem. First, the queue was modeled as an MDP. We presented the optimal policy for small deadlines (D=2,3). Some properties of the optimal policies were discussed.

As a second approach, we introduced a heuristic policy (AB − n) which improves the performance of the queue compared with previous algorithms (DPGP and EDF). Finally, some numerical simulations were provided to verify the results.

Also, it is worth noting that, as a line of future works, this approach can be applied to latency based utility optimization (cases without a hard deadline).

$$\sum_{i=1}^{k_{1}}\mu(1-\lambda-\mu)^{i-1}(1+B_{2}(k_{1}+k_{2}-i,k_{3}))$$ $$\sum_{i=k_{1}+1}^{k_{1}+k_{2}}\mu(1-\lambda-\mu)^{i-1}B_{2}(k_{1}+k_{2}-i,k_{3})$$ $$\sum_{i=k_{1}+k_{2}+1}^{k_{1}+k_{2}+k_{3}}\sum_{j=i+1}^{k_{1}+k_{2}+k_{3}}(\mu^{2}+\mu\lambda)(1-\lambda-\mu)^{j-2}(1-(1-\mu)^{k_{1}+k_{2}+k_{3}-j})$$

## References

[1] C. Wilson, H. Ballani, T. Karagiannis, and A. Rowtron, "Better
never than late: Meeting deadlines in datacenter networks," in
Proceedings of the ACM SIGCOMM 2011 Conference, SIGCOMM
'11, (New York, NY, USA), p. 50–61, Association for Computing Machinery, 2011.
[2] M. Alizadeh, A. Greenberg, D. A. Maltz, J. Padhye, P. Patel,
B. Prabhakar, S. Sengupta, and M. Sridharan, "Data center tcp
(dctcp)," in *Proceedings of the ACM SIGCOMM 2010 Conference*,
SIGCOMM '10, (New York, NY, USA), p. 63–74, Association for Computing Machinery, 2010.
[3] B. Vamanan, J. Hasan, and T. Vijaykumar, "Deadline-aware datacenter tcp (d2tcp)," in Proceedings of the ACM SIGCOMM 2012
Conference on Applications, Technologies, Architectures, and Protocols for Computer Communication, SIGCOMM '12, (New York, NY,
USA), p. 115–126, Association for Computing Machinery, 2012.
[4] Łukasz Kruk, J. Lehoczky, K. Ramanan, and S. Shreve, "Heavy
traffic analysis for EDF queues with reneging," The Annals of Applied Probability, vol. 21, no. 2, pp. 484 - 545, 2011.
[5] S. S. Panwar and D. Towsley, "On the optimality of the ste rule
for multiple server queues that serve," tech. rep., USA, 1988.
[6] J. Hong, X. Tan, and D. Towsley, "A performance analysis of
minimum laxity and earliest deadline scheduling in a realtime system," *IEEE Transactions on Computers*, vol. 38, no. 12,
pp. 1736–1744, 1989.
[7] S. Shakkottai and R. Srikant, "Scheduling real-time traffic with
deadlines over a wireless channel," in Proceedings of the 2nd ACM international workshop on Wireless mobile multimedia, pp. 35–42,
1999.
[8] J. R. Haritsa, M. Livny, and M. J. Carey, "Earliest deadline
scheduling for real-time database systems," tech. rep., University of Wisconsin-Madison Department of Computer Sciences, 1991.
[9] L. Zhang, Y. Cui, J. Pan, and Y. Jiang, "Deadline-aware transmission control for real-time video streaming," in 2021 IEEE 29th International Conference on Network Protocols (ICNP), pp. 1–
6, IEEE, 2021.
[10] L.-O. Raviv and A. Leshem, "Maximizing service reward for
queues with deadlines," *IEEE/ACM Transactions on Networking*,
vol. 26, no. 5, pp. 2296–2308, 2018.
[11] B. Doytchinov, J. Lehoczky, and S. Shreve, "Real-time queues in
heavy traffic with earliest-deadline-first queue discipline," The
Annals of Applied Probability, vol. 11, no. 2, pp. 332 - 378, 2001.
[12] R. Atar, A. Biswas, and H. Kaspi, "Fluid limits of g/g/1+g
queues under the nonpreemptive earliest-deadline-first discipline," *Mathematics of Operations Research*, vol. 40, no. 3, pp. 683–
702, 2015.
[13] S. Mohanty and W. Panny, "A discrete-time analogue of the
m/m/1 queue and the transient solution: a geometric approach," *Sankhy¯a: The Indian Journal of Statistics, Series A*,
pp. 364–370, 1990.
[14] F. Farahvash and A. Tang, "Delay performance optimization
with packet drop," in 2023 59th Annual Allerton Conference on Communication, Control, and Computing (Allerton), pp. 1–7, 2023.
[15] M. Abramowitz, I. A. Stegun, and R. H. Romer, "Handbook
of Mathematical Functions with Formulas, Graphs, and Mathematical Tables," *American Journal of Physics*, vol. 56, pp. 958–958,
10 1988.

## Appendix A: The D=3 Case

Here, we provide a complete analysis of the D = 3
case. Let's remember that the optimal policy should decide in 3 different states (that are nontrivial) whether to drop from the head or not drop at all.

$$\begin{array}{l l}{{\bullet}}&{{((1,0),1,0)}}\\ {{\bullet}}&{{((2,0),1,0)}}\\ {{\bullet}}&{{((2,1,0),1,0)}}\end{array}$$

## A. Dpgp

Once again, we will see what DPGP does in the states above:

- s=((1,0),1,0): We have:
$$g a i n_{1}^{s}(\mu)=\mu(1-5\mu+3\mu^{2})$$
We have:

$$g a i n_{1}^{s}(\mu)>0\leftrightarrow\mu<\frac{5-\sqrt{13}}{6}$$
And:

$$a(s)=\begin{cases}d,&\text{if}\mu<\frac{5-\sqrt{13}}{6}\\ \bar{d},&\text{Otherwise}\end{cases}\tag{16}$$
- s=((2,0),1,0): We have:
$$g a i n_{1}^{s}(\mu)=\mu(2-6\mu+3\mu^{2})$$

We have:

$$g a i n_{1}^{s}(\mu)>0\leftrightarrow\mu<1-\frac{\sqrt{3}}{3}$$
And:

$$a(s)=\begin{cases}d,&\text{if}\mu<1-\frac{\sqrt{3}}{3}\\ \bar{d},&\text{Otherwise}\end{cases}\tag{17}$$
- s=((2,1,0),1,0): We have:
$$g a i n_{1}^{s}(\mu)=\mu(1+\mu-3\mu^{2})$$

We have:

$$g a i n_{1}^{s}(\mu)>0\leftrightarrow\mu<\frac{\sqrt{13}}{6}+1$$
And:

$$a(s)=\begin{cases}d,&\text{if}\mu<\frac{\sqrt{13}+1}{6}\\ \bar{d},&\text{Otherwise}\end{cases}\tag{18}$$

## B. States

Here, we mention all 20 states for D = 3:
1) ((), 0, 0): The only possible action is not dropping,
and the next state will be ((0), 1, 0) with probability 1.
2) ((), 0, 1): The only possible action is not dropping,
and the next state will be ((0), 1, 0) with probability 1.
3) ((0), 0, 0): The only possible action is not dropping
(as if we drop the packet here, we will circulate
between state 1 and this state forever, and the reward would be zero.) We have:

$$\begin{CD}\left\{\begin{array}{ll}(),0,0),&\text{wp}\ \mu(\frac{1-\alpha}{\alpha})\\ ((),0,1),&\text{wp}\ \mu(1-(1-\alpha)^{3})\\ ((1),0,1),&\text{wp}\ \lambda\\ ((2,0),1,0),&\text{wp}\ \lambda(1-\alpha)\\ ((3,0),1,0),&\text{wp}\ \lambda(\frac{1-\alpha}{\alpha})\end{array}\right.\end{CD}$$

4) $((1),0,1)$: The only possible action is not dropping, and the next state will be:

$$\begin{CD}((1),0,0)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\ \mu(\frac{1-\alpha}{\alpha})^{2}\\ (((),0,1),&\text{wp}\ \mu(2+\alpha)\\ ((2,0),1,0),&\text{wp}\ \lambda\ \frac{1-\alpha}{\alpha}\end{cases}$$

5) $((2),0,0)$: The only possible action is not dropping, and the next state will be:

$$\begin{CD}((2),0,0)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\ \mu\frac{1-\alpha}{\alpha}\\ (((3),0,1),0),&\text{wp}\ \mu\\ ((2,0),1,0),&\text{wp}\ \frac{1}{\alpha}\end{cases}$$

6) $((2),0,1)$: The transition probability is the same as previous state.
7) $((3),0,1)$: Again, we can not drop a packet here and:

$$((3),0,0)\stackrel{{d}}{{\rightarrow}}\begin{cases}((),0,0),&\text{wp}\ \frac{\mu}{\alpha}\\ ((3,0),1,0),&\text{wp}\ \frac{\lambda}{\alpha}\end{cases}$$
8) ((1, 0), 1, 0): Similar to D=2, we have two possible
actions:
- Drop packet 1: The next state will be ((0), 1, 0)
with probability 1.
* Don't drop: The next will be: $$\begin{array}{ll}\left\{\begin{array}{ll}((1),0,1),&\mbox{wp}\ \mu\\ ((2),0,1),&\mbox{wp}\ \mu(1-\alpha)\\ ((3),0,0),&\mbox{wp}\ \mu(\frac{(1-\alpha)^{2}}{\alpha}\\ ((2,1,0),1,0),&\mbox{wp}\ \lambda\end{array}\right.\end{array}$$

α
((2, 1, 0), 1, 0),
wp λ
((3, 2, 0), 1, 0),
wp λ(1 − α)
((3, 3, 0), 1, 0),
wp λ (1−α)2

α
         
9) ((2, 0), 1, 0): Similar to the previous state, we have
two possible actions:
- Drop packet 1: The next state will be ((0), 1, 0)
with probability 1.
* Don't drop: The next will be: $$\begin{array}{ll}\left\{\begin{array}{ll}((1),0,1),&\mbox{wp}\ \mu\\ ((2),0,0),&\mbox{wp}\ \mu(1-\alpha)\\ ((3),0,0),&\mbox{wp}\ \mu(\frac{(1-\alpha)^{2}}{\alpha}\\ ((3,1,0),1,0),&\mbox{wp}\ \lambda\end{array}\right.\end{array}$$

α
((3, 1, 0), 1, 0),
wp λ
((3, 2, 0), 1, 0),
wp λ(1 − α)
((3, 3, 0), 1, 0),
wp λ (1−α)2

α
         
10) ((2, 1), 0, 1): The only possible action is not dropping, and the next state will be:
11) $((3,0),1,0)$: Any optimal policy would drop packet 1 as it has missed its deadline. Thus, the next state will be $((0),1,0)$: The only possible action is not dropping, and the next state will be: $$((3,2),0,0)\stackrel{{\tilde{d}}}{{\rightarrow}}\begin{cases}((3),0,0),&\text{wp}\stackrel{{\mu}}{{\alpha}}\\ ((3,3),0),1,0),&\text{wp}\stackrel{{\lambda}}{{\alpha}}\end{cases}$$
13) $((3,3),0,0)$: The only possible action is not dropping, and the next state will be: $$((3,3),0,0)\stackrel{{\tilde{d}}}{{\rightarrow}}\begin{cases}((3),0,0),&\text{wp}\stackrel{{\mu}}{{\alpha}}\\ ((3,3),0),1,0),&\text{wp}\stackrel{{\lambda}}{{\alpha}}\end{cases}$$
14) ((2, 1, 0), 1, 0): we have two possible actions:
- Drop
packet
1:
The
next
state
will
be
((1, 0), 1, 0) with probability 1.
* Don't drop: The next will be: $$\left\{\begin{array}{ll}((2,1),0,1),&\mbox{wp}\ \mu\\ ((3,2),0,0),&\mbox{wp}\ \mu(1-\alpha)\\ ((3,3),0,0),&\mbox{wp}\ \mu\frac{(1-\alpha)^{2}}{\alpha}\\ ((3,2,1,0),1,0),&\mbox{wp}\ \lambda\\ ((3,3,2,0),1,0),&\mbox{wp}\ \lambda(1-\alpha)\\ ((3,3,3,0),1,0),&\mbox{wp}\ \lambda\frac{(1-\alpha)^{2}}{\alpha}\end{array}\right.$$
* $((3,1,0),1,0)$: Any optimal policy would drop packet 1 as it has missed its deadline. Thus, the next state will be $((1,0),1,0)$.

16) ((3, 2, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((2, 0), 1, 0).
17) ((3, 3, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((3, 0), 1, 0).
18) ((3, 2, 1, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((2, 1, 0), 1, 0).
19) ((3, 3, 2, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((3, 2, 0), 1, 0).
20) ((3, 3, 3, 0), 1, 0): Any optimal policy would drop
packet 1 as it has missed its deadline. Thus, the next state will be ((3, 3, 0), 1, 0).

## C. Reward Computation

To compute the real optimal policy, let πd be the stationary distribution of the Markov chain induced by policy d on our MDP. Now, by definition of the reward (r = 2br), the percentage of packets meeting the deadline will be 2(πd
2 + πd
4 + πd
6 + πd
10).

Thus, given λ, µ, the optimal policy maximizes AR(λ, µ) = 2(πd
2 + πd
4 + πd
6 + πd
10).

Similar to D=2, We will state the rewards of each policy (we will skip the computation of stationary distribution and mention the probability of the important states here). Depending on (λ, µ), the optimal policy has one of the following forms:

(a) Drops in all of the above states: If we decide to drop
in all of the 3 nontrivial states, the important states in the stationary distribution will probabilities:
$$\pi_{2}^{d}=\frac{\mu}{2\alpha}(1-(1-\alpha)^{3}),\pi_{4}^{d}=0,\pi_{6}^{d}=0,\pi_{10}^{d}=0$$
Thus, the reward of this policy would be:

$$AR_{a}(\lambda,\mu)=\mu(3-3a+a^{2})\tag{19}$$
(b) Drops in states ((2,1,0),1,0) and ((2,0),1,0): If the
policy decides to keep the packets at state (1,0) and drop them in states (2,0) and (2,1,0), we will have:
$$\pi_{2}^{d}=\frac{\mu(1-\lambda)}{2}(3-3\alpha+\alpha^{2})+\frac{\mu^{2}\lambda}{2}(3-2\alpha)$$

$$\pi_{4}^{d}=\frac{\mu\lambda}{2},\quad\pi_{6}^{d}=\frac{\mu\lambda}{2}(1-\alpha),\quad\pi_{10}^{d}=0$$
Thus, the reward of this policy would be:

$$AR_{b}(\lambda,\mu)$$ $$=\mu(3-3\alpha+\alpha^{2})+\lambda\mu(\mu(3-2\alpha)-(\alpha-1)^{2})$$ $$=AR_{a}(\lambda,\mu)+\lambda\mu\left(-3\mu^{2}+(4\lambda-5)\mu+(\lambda-1)^{2}\right)\tag{20}$$
3. Only drops in the state ((2,1,0),1,0): For this policy, we have: $$\pi_{2}^{d}=\frac{\mu}{2}(1-\lambda-\frac{\lambda(1-\lambda)(1-\mu)}{1-\lambda\mu})(3-3\alpha+\alpha^{2})$$ $$+\frac{\mu^{2}\lambda}{2}(1+\frac{(1-\lambda)(1-\mu)}{1-\lambda\mu})(3-2\alpha)$$ $$\pi_{4}^{d}=\frac{\mu\lambda}{2}(1+\frac{(1-\lambda)(1-\mu)}{1-\lambda\mu})$$ $$\pi_{6}^{d}=\frac{\mu\lambda}{2}(1-\alpha),\quad\pi_{10}^{d}=0$$ Let $$K(\lambda,\mu)=\frac{(1-\lambda)(1-\mu)}{1-\lambda\mu}.$$ The reward will be: $$AR_{c}(\lambda,\mu)$$ $$=(\lambda,\mu)+\mu\lambda K(\lambda,\mu)\left(\mu(3-2\alpha)+1-(3-3\alpha+\alpha^{2})\right)$$ $$=AR_{b}(\lambda,\mu)-\mu\lambda K(\lambda,\mu)(3\mu^{2}-6\mu+\lambda^{2}-3\lambda+2)$$ (21)
Solving the second-degree equation, we get:

(d) Drops in none of the above states: If we decide on
not dropping packets in any of the nontrivial states, we would have:
$$AR_{\rm c}(\lambda,\mu)\geq AR_{b}(\lambda,\mu)$$ $$\frac{\mu^{2}}{2}(1-\frac{\lambda(1-\lambda)(1-\mu)}{1-\lambda\mu})(3-3\alpha+\alpha^{2})$$ $$+\frac{\mu^{2}\lambda}{2}(1-\lambda+\frac{(1-\lambda)(1-\mu)}{1-\lambda\mu})(3-2\alpha)$$ $$+\frac{\mu^{3}\lambda^{2}}{2}$$ $$AR_{\rm c}(\lambda,\mu)\geq AR_{b}(\lambda,\mu)$$ $$\frac{\uparrow}{\downarrow}$$ $$\mu\geq1-\frac{\sqrt{3}}{3}\sqrt{-\lambda^{2}+3\lambda+1}$$ Thus, policy (c) is better than policy (b) if and only if equation 24 holds.

- Comparison between policies (c) and (d): Finally,
for policies (c) and (d) we have
$$\pi_{4}^{d}=\frac{\mu\lambda}{2}(1+\frac{(1-\lambda)(1-\mu)}{1-\lambda\mu})-\frac{\mu\lambda^{2}}{2}AR_{d}(\lambda,\mu)\geq AR_{c}(\lambda,\mu)$$ $$\uparrow$$ $$\mu\lambda^{2}(3\mu^{2}+(2\lambda-1)\mu+\lambda-1)\geq0$$ $$\uparrow$$ $$3\mu^{2}+(2\lambda-1)\mu+\lambda-1\geq0$$ Solving the second-degree equation, we get:
Let K(λ, µ) = (1−λ)(1−µ)
1−λµ
. The reward will be:

$$AR_{d}(\lambda,\mu)\geq AR_{c}(\lambda,\mu)$$ $$\frac{\frac{\pi}{4}}{\lambda}\mu\geq\frac{1-2\lambda+\sqrt{4\lambda^{2}-16\lambda+13}}{6}\tag{25}$$ $$=AR_{c}(\lambda,\mu)+\mu\lambda^{2}\left(3\mu^{2}+(2\lambda-1)\mu+\lambda-1\right)$$
D. Choice of optimal policy
Thus, policy (d) is better than policy (c) if and only if equation 25 holds.

Fig. 3 shows the boundaries derived above. These boundaries do not cross, and thus, the analysis in section V-B is done.

In this part, we compute the conditions for which any of these policies become optimal.

- Comparison between policies (a) and (b): Plugging
in the results from the previous part, we get:
$AR_{b}(\lambda,\mu)\geq AR_{a}(\lambda,\mu)$

$\dagger$

$\lambda\mu(-3\mu^{2}+(4\lambda-5)\mu+(\lambda-1)^{2})\geq0$

$\dagger$

$-3\mu^{2}+(4\lambda-5)\mu+(\lambda-1)^{2})\geq0$
Solving the second-degree equation we get:

$$AR_{b}(\lambda,\mu)\geq AR_{a}(\lambda,\mu)$$ $$\stackrel{{\dagger}}{{\downarrow}}\tag{23}$$ $$\mu\geq\frac{5-4\lambda-\sqrt{4\lambda^{2}-16\lambda+13}}{6}$$
Thus, policy (b) is better than policy (a) if and only if equation 23 holds.

- Comparison between policies (b) and (c): Plugging
in the results from the previous part, we get:
$AR_{c}(\lambda,\mu)\geq AR_{b}(\lambda,\mu)$

$\dagger$

$\mu\lambda K(\lambda,\mu)(3\mu^{2}-6\mu+\lambda^{2}-3\lambda+2)\leq0$

$\dagger$

$(3\mu^{2}-6\mu+\lambda^{2}-3\lambda+2)\geq0$