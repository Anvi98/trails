# Event-Triggered State Estimation Through Confidence Level

Wei Liu, Senior Member, IEEE

  Abstract—This paper considers the state estimation problem
for discrete-time linear systems under event-triggered scheme. In
order to improve performance, a novel event-triggered scheme
based on confidence level is proposed using the chi-square
distribution and mild regularity assumption. In terms of the novel
event-triggered scheme, a minimum mean squared error (MMSE)
state estimator is proposed using some results presented in this
paper. Two algorithms for communication rate estimation of the
proposed MMSE state estimator are developed where the first
algorithm is based on information with one-step delay, and the
second algorithm is based on information with two-step delay.
The performance and effectiveness of the proposed MMSE state
estimator and the two communication rate estimation algorithms
are illustrated using a target tracking scenario.

  Index Terms—Event-triggered state estimation, Confidence
level, Communication rate estimation, Discrete-time linear sys-
tems, Sensor networks

## I. Introduction

With the development of wireless sensor network technology, wireless networked control systems (WNCS) have attracted increasing attention, and have been successfully applied in various fields such as control, signal processing, robotics, power electronics, etc [1]−[6]. In WNCS, sensors, controllers, estimators and actuators are spatially distributed where sensor and estimator are usually far away from each other. In this case, the communication from sensor to remote estimator is costly because the communication requires consuming power of energy limited battery in the sensor where the battery is probably hard to replace due to its physical position.

Event-triggered scheme is an effective means to reduce sensorto-estimator communication cost since communication is not permitted unless a pre-defined triggered condition is satisfied.

Previous studies have shown that event-triggered scheme can strike a proper balance of trade-offs between communication cost and estimation performance [7]−[10].

As a fundamental issue, event-triggered state estimation has been extensively studied [10]−[24]. In [11], for a first order discrete-time linear system, the pre-processor and estimator were sought to minimize a cost with two terms. In [12], a centralized sensor network with multiple nodes were considered where each node yields measurement of the original system. Local event-triggered transmission strategies were developed, and the strategies's stability and performance were studied. For the balance between communication rate and state estimation performance, an event-triggered sensor data This work was partially supported by the National Nature Science Foundation of China (6207312).

Wei Liu is with the School of Information and Electronic Engineering, Zhejiang Gongshang University, Hangzhou 310018, China (e-mail: intervalm@163.com).

scheduler was presented in [10] where, for a specific threshold, this scheduler is determined by the H¨older infinity-norm of the innovation's linear operation. Using an approximation technique in nonlinear filtering, an approximate MMSE state estimator was proposed. The results of [10] were extended in [14] and [15] where the results presented in [14] considered separate transmission for each element of the measurement, and measurements from multiple sensors with separate eventtriggering conditions for each measurement were studied in [15]. The measurement prediction variance was used in [16] to determine whether the measurement is transmitted. Based on this kind of measurement transmission, the state estimator was designed, and the corresponding Riccati equation with periodic behavior was developed. In [17], the set-valued Kalman filtering problem for additional information with stochastic uncertainty was studied, and it was applied to event-triggered estimation. Two stochastic event-triggered sensor schedules were proposed in [18] where one schedule depends on the current measurement, and the other one depends on the innovation. Based on the two schedules, the MMSE state estimators were proposed, and the communication rates were analyzed. The results of [18] were generalized and extended in [19] and [20], respectively, where single-sensor was generalized to the case of multi-sensor in [19], and a stochastic eventtriggered mechanism based on information-state contribution was proposed in [20]. More results about event-triggered state estimation were provided in [21]−[24] and references therein.

Because additional information was introduced to the remote estimator when the measurement is not transmitted to the estimator, the state estimator developed in [10] can yield better performance. However, the results developed in [10] does not establish the connection between the innovation and the trigger threshold, which means the performance can be further improved through establishing a proper connection between them. So, it is necessary to propose an event-triggered scheme which can establish a proper connection of the innovation, the trigger threshold and other related parameters, and to design state estimator based on this scheme, which motivates our research.

In this paper, using the chi-square distribution, regular Gaussian assumption and the method of confidence level, we first propose an event-triggered scheme which establishes a proper connection of the tolerable upper bound of the innovation covariance, the innovation and the trigger threshold. However, the results proposed in [10] do not obtain any connection of these parameters. Also, to the best of the author's knowledge, the event-triggered scheme proposed in this paper is novel and different from the existing results. The novel event-triggered scheme paves the way for the design of state estimator with better performance.

Then, based on the novel event-triggered scheme, a MMSE
state estimator is proposed in a recursive form. It is worth mentioning that, due to the use of the novel event-triggered scheme, the strategy in computing the error covariance of the proposed MMSE state estimator is different in contrast to the existing results. Two algorithms for estimating the communication rate of the proposed state estimator are developed where the first algorithm uses information with one-step delay, and the second algorithm utilizes information with two-step delay. As far as the author knows, the strategy used in the second algorithm, namely, using information with two-step delay, cannot be found in the existing results for estimating the communication rate of event-triggered state estimator. In addition, the simulation results show that the second algorithm yields a better communication rate estimation of the proposed state estimator, which means that the strategy of using information with two-step delay is effective. Due to using information with two-step delay, the proof of the second algorithm becomes very challenging. In order to prove the second algorithm, we first prove Lemma 4 and Theorem 2 in Appendix C, and then we prove the second algorithm in Appendix D.

The remainder of this paper is organized as follows. The system and problem under consideration are provided in Section II. We also present an event-triggered scheme in Section II. A MMSE state estimator based on the presented eventtriggered scheme is proposed in Section III. Two algorithms for estimating the communication rate of the proposed MMSE state estimator are developed in Section IV. In Section V, the performance and effectiveness of the proposed results, including the MMSE state estimator and the communication rate estimation algorithms, are demonstrated via a target tracking scenario. The conclusion is drawn in Section VI.

Notation: The n-dimensional real Euclidean space is denoted by Rn, and N > 0 is used to denote the positive definite matrix N. For a matrix A, its transpose, determinant and inverse are represented by AT, |A| and A−1, respectively. The probability density function is denoted by f, and the n × n identity matrix is denoted by In.

� Φ(η)dη is used to stand for
� Φ(η)dη1dη2 ···dηn where η = (η1,η2,··· ,ηn)T ∈ Rn, and Φ(η) is a function of η. We use E[·] and Var(·) to stand for the expectation operation and the covariance operation, respectively.

## Ii. Problem Formulation A. System Description

Consider the following system

$$X_{k+1}=Ax_{k}+\omega_{k},\tag{1}$$ $$Y_{k}=Cx_{k}+\omega_{k},k=0,1,\cdots\tag{2}$$
where xk ∈ Rn is the unknown state; ωk ∈ Rn is the process noise; yk ∈ Rp is the measurement; υk ∈ Rp is the measurement noise; A and C are matrices of appropriate dimensions; and the initial state x0 is a random vector with mean ¯x0 and covariance matrix ¯P0.

Throughout the paper, we introduce the following two assumptions.

1) ωk and υk are zero-mean white Gaussian noise sequences with covariance matrices Q and R, respectively.
2) ωk is independent of υk, and x0 is independent of ωk
and υk.
Considering the event-triggered state estimation problem whose structure is given in Fig. 1. γk has two possible values
0 and 1, and the value of γk is determined by the trigger scheme. When γk = 1, the measurement yk is transmitted to the estimator via network, and the information Ik available for the estimator is Ik = (Ik−1,yk). When γk = 0, there is no data tramission, and the information Ik available for the estimator is Ik = (Ik−1,γk = 0). Hence, we have Ik =
�
(Ik−1,γk = 0),
γk = 0;
(Ik−1,yk),
γk = 1
with I0 =
�
(γ0 = 0),
γ0 = 0;
(y0),
γ0 = 1
.

The trigger scheme is based on confidence level, and it will
be proposed in the next part.
  Remark 1: For a joint probability density function f(x,y) in
probability theory, f(x = a,y = b) denotes the joint probability
density of x and y given (x = a,y = b) where (x = a,y = b)
stands for {x = a} ∩ {y = b} instead of {x = a} ∪ {y = b}.
As an extension, the conditional probability density of x = a
given y = b is defined as f(x = a|y = b) = f(x=a,y=b)

                                                                                        f(y=b)
                                                                                                       . It has to
be said that the conditional probability f(x = a|y = b) is not
equal to f(x=a∪y=b)

f(y=b)
               , that is, f(x = a|y = b) ̸= f(x=a∪y=b)

                                                                                            f(y=b)
                                                                                                            , where
(x = a∪y = b) denotes {x = a}∪{y = b} which is the union of
two random variables. The conditional probability was used in
the wrong way in [10], which expressed the probability density
with the union of two random variables. For example, in [10],
the term fεk(ε|Ik−1) is equal to
                                                                   f(εk=ε∪Ik−1)

                                                                        f(Ik−1)
                                                                                        , and fεk(ε|Ik−1)
is obviously not equal to the conditional probability density
of εk = ε given Ik−1. However, the term fεk(ε|Ik−1) was used
as the conditional probability density, that is, the results were
developed based on the condition
                                                                       f(εk=ε∪Ik−1)

f(Ik−1)
                 = f(εk=ε,Ik−1)

                                                                                                         f(Ik−1)
                                                                                                                         .
Hence, the correctness of the corresponding results presented
in [10] is doubtful unless the information Ik−1 ∩ {γk = 0} is
used to replace Ik−1 ∪{γk = 0}.
    Remark 2: In
                                       [18],
                                                        Ik
                                                                  is
                                                                             defined
                                                                                                  by
                                                                                                               Ik
                                                                                                                      ≜
{γ0,γ1,··· ,γk,··· ,γ0y0,γ1y1,γkyk} = {Ik−1,γk,γkyk}. Because
the relation between Ik−1, γk and γkyk in Ik is not clearly
stated, we first assume that Ik = Ik−1 ∩ (γk ∪ γkyk). Then, we

have γk ∪ γkyk =
                �
                   γk = 0,
                                γk = 0;
                   (γk = 1)∪yk,
                                γk = 1
                                        , which means

that
      Ik =
             � Ik−1 ∩(γk = 0),
                                          γk = 0;
                Ik−1 ∩
                       �
                        (γk = 1)∪yk
                                      �
                                       ,
                                          γk = 1
                                                   .
                                                      We
                                                            easily

see that, under the above assumption, Ik is equal to the
description presented in [18] for γk = 0, but is not equal to
that for γk = 1. Second, we assume that Ik = Ik−1 ∩(γk ∩γkyk).
Then, we get γk ∩ γkyk = 0 in γk = 0. As a result, we derive
Ik = Ik−1 in γk = 0. It is obvious that, under the assumption
of Ik = Ik−1 ∩ (γk ∩ γkyk), Ik is not equal to the description
presented in [18] for γk = 0. Hence, no matter how we choose
the relation between Ik−1, γk and γkyk, Ik cannot completely

embody
       the
           description
                     Ik =
                         � (Ik−1,γk = 0),
                                        γk = 0;
                           (Ik−1,yk),
                                        γk = 1
presented
        in
           [18].
                This
                     means
                            that
                                the
                                    definition
                                             of
Ik ≜ {γ0,γ1,··· ,γk,··· ,γ0y0,γ1y1,γkyk} given in [18] is not
rigorous.

## B. Event-Triggered Scheme Based On Confidence Level

In order to propose the event-triggered scheme based on confidence level, we first present the following two remarks and one lemma.

Remark 3: Let w ∈ Rp be a Gaussian random vector with mean ¯w and covariance matrix S. Then, it was presented in Result 4.7 of [28] that (w − ¯w)TS−1(w − ¯w) obeys the distribution of χ2
p where χ2
p stands for the chi-square distribution with p degrees of freedom.

Remark 4: Let µ1, µ2, ···, µm be Gaussian and mutually independent. Then, it is well known that the linear combination of µ1, µ2, ···, µm is still Gaussian.

Lemma 1: Under the assumption that f(xk−1|Ik−1) is Gaussian, it holds that:
1). f(xk|Ik−1) is Gaussian.

2). f(yk|Ik−1) is Gaussian.

Proof: See Appendix A.

For notational simplicity, define

$$\hat{V}_{k,k-1}\stackrel{{\Delta}}{{=}}\mbox{E}[y_{k}|\mbox{I}_{k-1}],\tag{3}$$ $$\hat{V}_{k}\stackrel{{\Delta}}{{=}}y_{k}-\hat{V}_{k,k-1},$$ (4) $$N_{k}\stackrel{{\Delta}}{{=}}\mbox{Var}(y_{k}|\mbox{I}_{k-1}).\tag{5}$$
Under the assumption that f(xk−1|Ik−1) is Gaussian, we see from 2) of Lemma 1 that f(yk|Ik−1) is Gaussian. Then, using Remark 3, we find that ˜yT
k N−1
k
˜yk is distributed as χ2
p where ˜yk and Nk are defined in (4) and (5), respectively. Let N > 0 be a tolerable upper bound of Nk. When Nk exceeds the tolerable upper bound, namely, Nk > N, we need to take γk = 1 so that Nk+1 does not exceed the tolerable upper bound. When Nk > N, we have

$\Phi_{k}>\tilde{y}_{k}^{\rm T}N_{k}^{-1}\tilde{y}_{k}$ (6)
where

$\Phi_{k}=\tilde{\Psi}_{k}\Sigma_{k},\Sigma=\overline{N}^{-1}$.

Let χ2
α(p) denote the upper (l00α)th percentile of the χ2
p distribution, that is, P
�
˜yT
k N−1
k
˜yk ≤ χ2
α(p)
�
= 1 − α. In frequentist statistics, the 95% confidence level is the most often.

Hence, we can take 1 − α = 0.95 in confidence level for
˜yT
k N−1
k
˜yk. Then, we conclude from the theory of confidence level that ˜yT
k N−1
k
˜yk does not obey the χ2
p distribution if

˜yT
 k N−1
    k
       ˜yk > χ2
                α(p). Then, using (6), we get ϕk > ˜yT
                                                               k N−1
                                                                  k
                                                                      ˜yk >
χ2
 α(p) =⇒ ϕk > χ2
                       α(p) when Nk > N. Based on the above
discussion, we present the following event-triggered scheme:

$$\gamma_{k}=\begin{cases}\gamma_{k}=0,&\varphi_{k}\leq\chi_{\alpha}^{2}(p);\\ \gamma_{k}=1,&\varphi_{k}>\chi_{\alpha}^{2}(p).\end{cases}\tag{8}$$
where 1 − α = 0.95 is suggested to be taken considering the theory of confidence level. Since Σ is positive definite, Σ can be expressed as Σ = ΦTΦ such that Φ is invertible. Then, using (7) and noticing yk ∈ Rp, we have

$$\varphi_{k}=\tilde{y}_{k}^{\rm T}\Sigma\tilde{y}_{k}=\tilde{y}_{k}^{\rm T}\Phi^{\rm T}\Phi\tilde{y}_{k}=\tilde{z}_{k}^{\rm T}\tilde{z}_{k}=\sum_{i=1}^{P}\tilde{z}_{k,i}^{2}\tag{9}$$
where

$\mathbb{Z}_{k}\stackrel{{\Delta}}{{=}}\Phi\mathbb{Y}_{k}$ (10)
and zk,i denotes the ith element of zk.

Remark 5: An advantage of the event-triggered scheme proposed in this paper is that a proper connection of the tolerable upper bound N, the innovation ˜yk and the trigger threshold χ2
α(p) is established via confidence level and chisquare distribution, which leads to the performance improvement of the state estimator proposed in Section III in contrast to the state-of-the-art state estimator proposed in [10]. However, the event-triggered schemes provided in [10] and [17] do not establish any connection of these parameters. Also, the proposed event-triggered scheme is novel and different those presented in [11]−[16] and [18]−[27].

Let ˆxk ≜ E[xk|Ik] which is the optimal MMSE estimate of xk given Ik. The rest of the study has two main objectives.

The first objective is to design a MMSE state estimator using the above event-triggered scheme based on confidence level, which can recursively compute ˆxk under a regular assumption.

The second objective is to develop two algorithms for estimating the communication rate of the proposed MMSE state estimator.

## Iii. Mmse State Estimation

In this section, we study the MMSE state estimation problem based on the event-triggered scheme. More precisely, the computational strategy for the MMSE estimate ˆxk is studied in the section. For notational simplicity, let

$$P_{k}\stackrel{{\triangle}}{{=}}\text{Var}(x_{k}|\text{I}_{k}),\tag{11}$$ $$\Omega_{k}\stackrel{{\triangle}}{{=}}\{z_{k}\in\mathbb{R}^{P}|\varphi_{k}\leq\chi_{\alpha}^{2}(p)\},$$ (12) $$\hat{x}_{k}^{[z]}\stackrel{{\triangle}}{{=}}\text{E}[x_{k}|\text{I}_{k-1},z_{k}],$$ (13) $$P_{k}^{[z]}\stackrel{{\triangle}}{{=}}\text{Var}(x_{k}|\text{I}_{k-1},z_{k}),$$ (14) $$\hat{x}_{k,k-1}\stackrel{{\triangle}}{{=}}\text{E}[x_{k}|\text{I}_{k-1}],$$ (15) $$\hat{x}_{k}\stackrel{{\triangle}}{{=}}x_{k}-\hat{x}_{k,k-1},$$ (16) $$M_{k}\stackrel{{\triangle}}{{=}}\text{Var}(x_{k}|\text{I}_{k-1}),$$ (17) $$N_{k}^{[z]}\stackrel{{\triangle}}{{=}}\text{Var}(z_{k}|\text{I}_{k-1}),$$ (18) $$K_{k}\stackrel{{\triangle}}{{=}}\text{E}\Big{[}\tilde{x}_{k}(z_{k}-\text{E}[z_{k}|\text{I}_{k-1}])^{\text{T}}\Big{]}\big{(}N_{k}^{[z]}\big{)}^{-1}.\tag{19}$$ _Lemma 2:_ Under the assumption that $f(x_{k-1}|\mathrm{I}_{k-1})$ is Gaussian, it holds that:

1. $f(z_{k}|\mathrm{I}_{k-1})$ is Gaussian.
2. $f(z_{k}|\mathrm{I}_{k-1})=\frac{g(z_{k})}{(2\pi)^{0.5p}\left|N_{k}^{[z]}\right|^{1.5}}$ with

$$g(z_{k})\triangleq\exp\{-\,0.5z_{k}^{\mathrm{T}}(N_{k}^{[z]})^{-1}z_{k}\}.$$

_Proof:_ See Appendix A.

_Lemma 3:_ Under the assumption that $f(x_{k-1}|\mathrm{I}_{k-1})$ is Gaussian, it holds that:

1. $\int_{\Omega_{k}}f(z_{k}|\mathrm{I}_{k-1})dz_{k}=\frac{h_{k}}{(2\pi)^{0.5p}\left|N_{k}^{[z]}\right|^{0.5}}$ where

$$h_{k}=\int\limits_{-b}^{\tilde{b}}dz_{k,1}\int\limits_{-\tilde{z}_{k,1}}^{\tilde{z}_{k,2}}dz_{k,3}\cdots\int\limits_{-\tilde{z}_{k,p-1}}g(z_{k})dz_{k,p}$$
with

$$\chi_{\alpha}^{2}(p)-z_{k,1}^{2},$$ $$\tilde{b}\triangleq\sqrt{\chi_{\alpha}^{2}(p),\tilde{z}_{k,1}}\triangleq\sqrt{\cdot}$$
ˇzk,2 ≜
�

χ2α(p)− 2 ∑ i=1 z2 k,i,··· , ˇzk,p−1 ≜ p−1 ∑ i=1 z2 k,i.

�
�
�
�χ2α(p)−

2).
   �
    Ωk f(zk|Ik−1)zkzT
                      k dzk =
                                    Ψk

(2π)0.5p��N[z] k ��0.5 with Ψk = (ψk,ij)p×p where ψk,ij = −ˇzk,1 dzk,2 ··· −ˇzk,p−1 g(zk)zk,izk,jdzk,p. −ˇb dzk,1 ˇb� ˇzk,1 � ˇzk,p−1 �
Proof: See Appendix A.

Considering that γk has two possible values 0 and 1, we deal with the problem under the following two cases:
1) γk = 1. Noticing the definition of Ik, we have Ik =
(Ik−1,yk). Then, using Kalman filter, we derive

ˆxk =ˆxk,k−1 + MkCT(CMkCT + R)−1 ˜yk, (20) Pk =Mk − MkCT(CMkCT + R)−1CMk (21)
where ˜yk = yk −Cˆxk,k−1, ˆxk,k−1 = Aˆxk−1 and Mk = APk−1AT +
Q.

2) γk = 0. We have Ik = (Ik−1,γk = 0) when γk = 0. Then, we present the following theorem to compute ˆxk in γk = 0.

Theorem 1: When f(xk−1|Ik−1) is Gaussian, the MMSE
state estimation ˆxk and the corresponding error covariance Pk in
γk = 0 can be computed according to the following equalities:

ˆxk =ˆxk,k−1, (22) Kk =MkCT(CMkCT + R)−1Φ−1, (23) P[z] k =Mk − MkCT(CMkCT + R)−1CMk, (24) Pk =P[z] k + 1 hk KkΨkKT k . (25)
Proof: See Appendix B.

Remark 6: In fact, ˆxk in (22) of Theorem 1 should be com-
ψk

puted via ˆxk = ˆxk,k−1+ek with ek ≜
                                   Kk
                                      �
                                     � Ωk f(zk|Ik−1)zkdzk
                                      Ωk f(zk|Ik−1)dzk
                                                      in which
�
 Ωk f(zk|Ik−1)zkdzk can be obtained via
                                         �
                                          Ωk f(zk|Ik−1)zkdzk =

(2π)0.5p��N[z]
           k
              ��0.5 where ψk = (ψk,1,ψk,2,··· ,ψk,p)T with ψk,i =

−ˇzk,1
dzk,2 ···
−ˇzk,p−1
g(zk)zk,idzk,p, i = 1,2,··· , p. Since ψk is
−ˇb dzk,1
ˇzk,1
�
ˇzk,p−1
�
ˇb�
almost equal to zero vector, we conclude that ek is almost equal to zero vector. Hence, ˆxk in Theorem 1 is calculated using (22).

Now, we can present the MMSE state estimator.

Starting with ˆxk−1 and Pk−1, the MMSE state estimator includes the following two steps.

Step 1: Compute ˆxk,k−1, ˜yk, Mk, hk and Ψk according to

$$\hat{X}_{k,k-1}=\hat{A}\hat{X}_{k-1},\tag{26}$$ $$\hat{Y}_{k}=\mathcal{Y}_{k}-C\hat{X}_{k,k-1},$$ (27) $$M_{k}=AP_{k-1}A^{\mathrm{T}}+Q,$$ (28) $$N_{k}^{[\hat{z}]}=\Phi(CM_{k}C^{\mathrm{T}}+R)\Phi^{\mathrm{T}},$$ (29) $$h_{k}=\int\limits_{\begin{array}{c}\hat{b}\\ -\hat{b}\end{array}}^{\hat{b}}dz_{k,1}\int\limits_{\begin{array}{c}\hat{z}_{k,p-1}\\ -\hat{z}_{k,p-1}\end{array}}^{\hat{z}_{k,p-1}}g(z_{k})dz_{k,p},$$ (30) $$\Psi_{k,ij}=\int\limits_{\begin{array}{c}\hat{b}\\ -\hat{b}\end{array}}^{\hat{b}}dz_{k,1}\int\limits_{\begin{array}{c}\hat{z}_{k,p-1}\\ -\hat{z}_{k,p-1}\end{array}}^{\hat{z}_{k,p-1}}g(z_{k})z_{k,i}\bar{z}_{k,j}dz_{k,p},$$ (31) \[\Psi_{k}=(\,\
where g(zk) is defined in 2) of Lemma 2, as well as ˇb and ˇzk,i with i = 1,2,··· , p − 1 are defined in 1) of Lemma 3.

Step 2: Compute ˆxk and Pk in terms of

$$P_{k}^{[z]}=M_{k}-M_{k}C^{\rm T}(CM_{k}C^{\rm T}+R)^{-1}CM_{k},\tag{33}$$ $$\hat{x}_{k}=\hat{x}_{k,k-1}+\gamma_{k}M_{k}C^{\rm T}(CM_{k}C^{\rm T}+R)^{-1}\tilde{y}_{k},$$ (34) $$K_{k}=M_{k}C^{\rm T}(CM_{k}C^{\rm T}+R)^{-1}\Phi^{-1},$$ (35) $$P_{k}=P_{k}^{[z]}+\frac{(1-\gamma_{k})}{h_{k}}K_{k}\Psi_{k}K_{k}^{\rm T}\tag{36}$$
where γk is determined by (8) and (7). For the proposed MMSE
state estimator, we easily see that we only need to prove (34) and (36) where we easily obtain (34) by using (20) and (22).

Using (21) and (24), we see that

$P_{k}=P_{k}^{[z]}$ when $\gamma_{k}=1$. (37)
Putting (37) and (25) together, we prove (36).

Remark 7: The results for MMSE state estimation problem based on different event-triggered schemes were presented in [10], [14], [15], [16], [18], [19], [21], [22], [23] and [27]. However, compared with the results, the MMSE state estimator presented in this paper has a different strategy in computing the error covariance Pk because a novel confidence level based event-triggered scheme is applied to the design of the MMSE state estimator.

Remark 8: For the MMSE state estimator presented in
(26)−(36), we need to know the initial conditions ˆx0 and P0.

Hence, we present the following scheme to obtain ˆx0 and P0.

ˆx0 and P0 can be computed according to

$$\hat{\lambda}_{0}=\bar{x}_{0}+\gamma_{0}\bar{P}_{0}C^{\rm T}(C\bar{P}_{0}C^{\rm T}+R)^{-1}(y_{0}-C\bar{x}_{0}),\tag{38}$$

$$\bar{N}_{0}^{[z]}=\Phi(C\bar{P}_{0}C^{\rm T}+R)\Phi^{\rm T},\tag{39}$$ $$\bar{\Psi}_{0,ij}=\int\limits_{\begin{array}{c}b\\ -b\end{array}}dz_{0,1}\int\limits_{\begin{array}{c}z_{0,p-1}\\ -\bar{z}_{0,p-1}\end{array}}\rho(z_{0})z_{0,i}z_{0,j}dz_{0,p},\tag{40}$$ $$\bar{\Psi}_{0}=(\bar{\Psi}_{0,ij})_{p\times p},$$ (41) $$\alpha_{0}=\int\limits_{\begin{array}{c}b\\ dz_{0,1}\int dz_{0,2}\cdots\int\limits_{\begin{array}{c}z_{0,p-1}\\ -\bar{z}_{0,1}\end{array}}\rho(z_{0})dz_{0,p},$$ (42) $$\bar{K}_{0}=\bar{P}_{0}C^{\rm T}(C\bar{P}_{0}C^{\rm T}+R)^{-1}\Phi^{-1},$$ (43) $$P_{0}^{[z]}=\bar{P}_{0}-\bar{P}_{0}C^{\rm T}(C\bar{P}_{0}C^{\rm T}+R)^{-1}C\bar{P}_{0},$$ (44) $$P_{0}=P_{0}^{[z]}+\frac{(1-\gamma_{0})}{\alpha_{0}}\bar{K}_{0}\bar{\Psi}_{0}\bar{K}_{0}^{\rm T}\tag{45}$$
where γ0 is determined by (8) with ϕ0 = (y0 −C ¯x0)TΣ(y0 −
C ¯x0), as well as
α0 ≜
�
Ω0 ρ(z0)dz0,
ρ(z0) ≜ exp
�
−
0.5zT
0( ¯N[z]
0 )−1z0
�
, ¯N[z]
0 ≜ Var(z0) and ¯K0 ≜ Cov(x0,z0)
� ¯N[z]
0
�−1.

Making reference to the derivation of the MMSE state estimator, we can easily obtain (38)−(45).

IV. COMMUNICATION RATE ESTIMATION
In this section, we study the communication rate estimation problem for the proposed MMSE state estimator. More precisely, we will present two strategies for approximately computing E[γk].

E[γk] can be expressed as

$$\begin{array}{l}\mbox{E}[\gamma_{k}]=0\times P(\gamma_{k}=0)+1\times P(\gamma_{k}=1)\\ =P(\gamma_{k}=1)=1-P(\gamma_{k}=0)\end{array}\tag{46}$$
where

P(γk = 0) = � f(γk = 0,Ik−1)dIk−1 = � f(Ik−1)P(γk = 0|Ik−1)dIk−1. (47)
Remark 9: From (47), we see that the computation of P(γk = 0) is intractable because the computational complex of
� f(Ik−1)P(γk = 0|Ik−1)dIk−1 increases with k. Then, it follows from (46) that the computation of E[γk] is intractable.

In order to approximately compute E[γk], we will use two types of approximations where one type of approximation is E[γk] ≈ E[γk|Ik−1], and the other one is E[γk] ≈ E[γk|Ik−2]. We will present a strategy for computing E[γk|Ik−1] and E[γk|Ik−2], and we will test the two different approximations for E[γk] in Section V-A.

For notational simplicity, let

ˆγk,k−i ≜E[γk|Ik−i], (48) Pk,k−i(0) ≜P(γk = 0|Ik−i), (49) ⃗P[z] k (0) ≜P(γk = 0|Ik−2,zk−1), (50) ˘Pk(0) ≜P(γk = 0|Ik−2,γk−1 = 0), (51) ˆz⊲ k,k−1 ≜E[zk|Ik−2,zk−1], (52) ˜z⊲ k ≜zk − ˆz⊲ k,k−1, (53) ⃗N[z] k ≜Var(zk|Ik−2,zk−1), (54) ˆzk,k−1(0) ≜E[zk|Ik−2,γk−1 = 0], (55) Nk(0) ≜Var(zk|Ik−2,γk−1 = 0), (56) $$\Omega_{k}\stackrel{{\Delta}}{{=}}\{z_{k}\in\mathbb{R}^{P}|\varphi_{k}>\chi_{\alpha}^{2}(p)\}\tag{57}$$
with i = 1,2.

Starting with ˆxk−1 and Pk−1, ˆγk,k−1 can be recursively computed according to Algorithm 1. For Algorithm 1, we only

## Algorithm 1 : Communication Rate Based On Information Up To K − 1 Step 1: Compute ˆΓk,K−1 According To

$$P_{k,k-1}(0)=\frac{h_{k}}{(2\pi)^{0.5p}|N_{k}^{[\bar{z}]}|0.5}\,^{\dagger}\tag{58}$$ $$\hat{\gamma}_{k,k-1}=1-P_{k,k-1}(0)\tag{59}$$
where N[z]
k and hk are computed using (28)−(30) in sequence.

Step 2: Compute and store ˆxk and Pk for the derivation of ˆγk+1,k where ˆxk and Pk are computed via (26)−(36) in sequence.

need to prove (58) and (59). P(γk = 0|Ik−1) can be rewritten as

$$P(\gamma_{k}=0|\mathrm{I}_{k-1})=P(z_{k}\in\Omega_{k}|\mathrm{I}_{k-1})$$ $$=\int_{\Omega_{k}}f(z_{k}|\mathrm{I}_{k-1})dz_{k}=\frac{h_{k}}{(2\pi)^{0.5p}\left|N_{k}^{[z]}\right|^{0.5}}\tag{60}$$ $$\mathrm{st\ equality\ is\ due\ to\ 1}$$ $$\mathrm{I}_{k-1})\ \mathrm{by}\ P_{k-1}(0)\ \mathrm{we}$$
where Ωk is defined in (12), and the last equality is due to 1)
of Lemma 3. Then, replacing P(γk = 0|Ik−1) by Pk,k−1(0), we prove (58). Making reference to (46), we easily obtain (59).

In order to compute ˆγk,k−2, we propose the following theorem.

Theorem 2: When f(xk−1|Ik−1) is Gaussian, ˆγk,k−2 can be computed in terms of the following equalities:

⃗N[z] k =Φ � C(AP[z] k−1AT + Q)CT + R)ΦT, (61) hk−1 Kk−1Ψk−1KT k−1)AT + Q � CT + R � Nk(0) = Φ � C � A(P[z] k−1 + 1 × ΦT, (62) f(zk|Ik−2,zk−1) = ⃗g(zk) f(zk|Ik−2,zk−1) = ⃗g(zk) (2π)0.5p��⃗N[z] k ��0.5 , (63) f(zk|Ik−2,γk−1 = 0) = ˘g(zk) (2π)0.5p��⃗N[z] k ��0.5 , (64) (2π)0.5p��Nk(0) ��0.5 , (65) Ωk f(zk|Ik−2,zk−1)dzk, (66) ⃗P[z] k (0) = � Ωk f(zk|Ik−2,γk−1 = 0)dzk, (67) ˘Pk(0) = � ˘Ωk−1 ⃗P[z] k (0)f(zk−1|Ik−2)dzk−1, Pk,k−2(0) =Pk−1,k−2(0) ˘Pk(0)+ � (68) ˆγk,k−2 =1 − Pk,k−2(0) (69) where $$\vec{g}(z_{k})\stackrel{{\triangle}}{{=}}\exp\bigl{\{}-\,0.5z_{k}^{\mathrm{T}}(\vec{N}_{k}^{[z]})^{-1}z_{k}\bigr{\}},$$ $$\vec{g}(z_{k})\stackrel{{\triangle}}{{=}}\exp\bigl{\{}-\,0.5z_{k}^{\mathrm{T}}N_{k}(0)^{-1}z_{k}\bigr{\}}.\tag{70}$$

_Proof:_ See Appendix C.

Based on the above discussion, we present an algorithm to compute $\hat{\gamma}_{k,k-2}$ in a recursive structure. Starting with $P_{k-1}^{[c]}$, $h_{k-1},\ K_{k-1},\ \Psi_{k-1},\ \hat{x}_{k-1},\ P_{k-1}$ and $P_{k-1,k-2}(0),\ \hat{\gamma}_{k,k-2}$ can be recursively computed according to Algorithm 2 where the proof of Algorithm 2 is presented in Appendix D.

## Algorithm 2 : Communication Rate Based On Information Up To K − 2

Step 1: Compute ⃗N[z]
k and Nk(0) using (61) and (62), respectively.

Step 2: Compute ⃗P[z]
k (0) and ˘Pk(0) according to

$$\begin{array}{c}\tilde{b}\\ \tilde{b}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \tilde{R}_{k}^{[z]}(0)=\frac{-\tilde{b}}{\tilde{b}}\\ \end{array}\tag{71}$$
where ⃗g(zk) and ˘g(zk) are defined in (70).

Step 3: Compute Pk,k−2(0) using

$$P_{k,k-2}(0)=\vec{P}_{k}^{[z]}(0)+P_{k-1,k-2}(0)\big{(}\vec{P}_{k}(0)-\vec{P}_{k}^{[z]}(0)\big{)}.\tag{73}$$

**Step 4:** Compute $\hat{\gamma}_{k,k-2}$ in terms of (69).

**Step 5:** For computing the communication rate at time step $k+1$, update $P_{k}^{[z]}$, $h_{k}$, $K_{k}$, $\Psi_{k}$, $\hat{x}_{k}$, $P_{k}$ and $P_{k,k-1}(0)$ using the MMSE state estimator presented in (26)$-$(36) and using (58).

  Remark 10: Under the assumption that
                                       f(xk−1|Ik−1) is
Gaussian, we obtain ˆγk,k−2 using Algorithm 2 in a recursive
form where the proof of the algorithm is very challenging.
In order to prove Algorithm 2, Lemma 4 and Theorem 2 are
first proved in Appendix C, and then Algorithm 2 is proved
in Appendix D.
  Remark 11: If we take the approximation E[γk] ≈ ˆγk,k−1
where ˆγk,k−1 can be obtained from Algorithm 1, we need to
additionally obtain E[γ0] since Algorithm 1 starts with k = 1.
In the same way, we need to know E[γ0] and E[γ1] if we take
the approximation E[γk] ≈ ˆγk,k−2 using Algorithm 2. Hence,
we need to obtain E[γ0] and E[γ1].
We present a strategy for computing E[γ0] and E[γ1] with the
following content:

$$P(\gamma_{0}=0)=\frac{\alpha_{0}}{(2\pi)^{0.5p}|\tilde{N}_{0}^{[z]}|^{0.5}},\tag{74}$$ $$\mathrm{E}[\gamma_{0}]=1-P(\gamma_{0}=0),$$ (75) $$\tilde{N}_{1}^{[z]}=\Phi\big{(}C(AP_{0}^{[z]}A^{\mathrm{T}}+Q)C^{\mathrm{T}}+R\big{)}\Phi^{\mathrm{T}},$$ (76) $$\tilde{N}_{1}(0)=\Phi\Big{(}C\big{(}A(P_{0}^{[z]}+\frac{1}{\alpha_{0}}\tilde{K}_{0}\tilde{W}_{0}\tilde{K}_{0}^{\mathrm{T}})A^{\mathrm{T}}+Q\big{)}C^{\mathrm{T}}+R\Big{)}\Phi^{\mathrm{T}},\tag{77}$$ $$\begin{array}{c}\stackrel{{b}}{{\int}}dz_{1,1}\stackrel{{z_{1,1}}}{{\int}}dz_{1,2}\cdots\stackrel{{z_{1,p-1}}}{{\int}}\tilde{\rho}(z_{1})dz_{1,p}\\ \tilde{P}_{1}(0)=\stackrel{{-b}}{{\longrightarrow}}\stackrel{{-z_{1,1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}},\\ \stackrel{{b}}{{\longrightarrow}}\stackrel{{z_{1,1}}}{{\int}}dz_{1,2}\cdots\stackrel{{z_{1,p-1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}},\\ \stackrel{{P[z]}}{{\longrightarrow}}(0)=\stackrel{{-b}}{{\longrightarrow}}\stackrel{{-z_{1,1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}},\\ \end{array}\tag{78}$$

\[\begin{array}{c}\stackrel{{b}}{{\longrightarrow}}\stackrel{{z_{1,1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}} \stackrel{{z_{1,p-1}}}{{\longrightarrow}},\\ \stackrel{{P[z]}}{{\longrightarrow}}(0)=\stackrel{{-b}}{{\longrightarrow}}\stackrel{{-z_{1,1}}}{{\longrightarrow}}\stackrel{{z_{1,p-1}}}{{\longrightarrow}} \stackrel{{z_{1,p-1}}}{{\longrightarrow}},\\ \
where ¯N[z]
0 , α0 and P[z]
0 are computed using (39), (42) and (44);
and ¯N1(0) ≜ Var(z1|γ0 = 0), ¯N[z]
1 ≜ Var(z1|z0), ˘ρ(z1) ≜ exp
�
−
0.5zT
1
� ¯N1(0)
�−1z1
�
, ⃗ρ(z1) ≜ exp
�
−0.5zT
1
� ¯N[z]
1
�−1z1
�
, ¯P1(0) ≜
P(γ1 = 0|γ0 = 0) and ¯P[z]
1 (0) ≜ P(γ1 = 0|z0). Making reference to the derivation of Algorithm 1, we easily derive (74). Using
(46), we directly derive (75) and (81). Similar to the derivation of Algorithm 2, we easily obtain (76)−(80).

## V. Simulation Example

In this section, we illustrate the performance of the MMSE
state estimator and the communication rate estimation algorithms proposed in this paper via a target tracking scenario including two parts. More precisely, we test the performance of the proposed results in Section V-A, and we compare the MMSE state estimator proposed in this paper with the state estimator proposed in [10] in Section V-B. The state estimator proposed in [10] is referred as SEHI considering that its eventtriggered scheduler is based on H¨older infinity-norm.

## A. Performance Evaluation Of The Proposed Results

Consider a target tracking problem [29] where the statespace formulation of the target can be written as (1) with

$$x_{k}=\left(\begin{array}{c}p_{k}\\ v_{k}\\ a_{k}\end{array}\right),\,A=\left(\begin{array}{ccc}1&T&T^{2}\\ 0&1&T\\ 0&0&1\end{array}\right),$$

$$Q=2a\sigma_{m}^{2}\left(\begin{array}{ccc}T^{5}/20&T^{4}/8&T^{3}/6\\ T^{4}/8&T^{3}/3&T^{2}/2\\ T^{3}/6&T^{2}/2&T\end{array}\right).$$

$p_{k}$, $v_{k}$ and $a_{k}$ stand for the position, velocity and acceleration, respectively, of the target. $T$, $a$ and $\sigma_{m}^{2}$ denote the sampling period, the maneuver time constant's reciprocal and the target acceleration's variance, respectively. The measurement of the 
target can be modeled as (2) where C =
� 1
0
0
0
0
1
�
and R =
� 60
0
0
10
�
. The initial position, velocity and accelera-

tion of this target are 3410m, 30m/s and 0m/s${}^{2}$, respectively. We select

$$\bar{x}_{0}=\left(\begin{array}{cc}3500\\ 40\\ 0\end{array}\right),\,P_{0}=\left(\begin{array}{cc}60^{2}&60^{2}/T&0\\ 60^{2}/T&2\times60^{2}/T^{2}&0\\ 0&0&0\end{array}\right).$$

Also, we take $T=1$, $a=2$ and $\sigma_{m}^{2}=0.5$. We select $1-\alpha=0.95$ in confidence level. Then, noticing $p=2$ and using the  chi-square distribution table, we have $\chi_{\alpha}^{2}(p)=5.991$. For the tolerable upper bound $\overline{N}$, we take three different parameter values given by the following three cases:

$$\text{Case1:}\overline{N}=\left(\begin{array}{cc}50&4\\ 4&8\end{array}\right);\text{Case2:}\overline{N}=0.5\times\left(\begin{array}{cc}50&4\\ 4&8\end{array}\right);\text{Case3:}\overline{N}=\left(\begin{array}{cc}60&10\\ 10&20\end{array}\right).$$

We test the performance of the presented results using a Monte Carlo simulation with $N=5000$ trials, and we take $k=0,1,\cdots,100$ for each trial. We use the root-mean-square (RMS) error, the communication rate and the average communication rate as the performance evaluation criteria. At time step $k$, the RMS error is defined as $\sqrt{\frac{1}{N}\sum_{i=1}^{N}(\xi_{k,i}-\hat{\xi}_{k,i})^{2}}$ for $N$ trials where $\xi_{k,i}$ stands for the state of $\xi_{k}$ at the $i$th trial, and $\hat{\xi}_{k,i}$ stands for an estimate of $\xi_{k,i}$. Let $\gamma_{k,i}$ denote the state of $\gamma_{k}$ at the $i$th trial, and the communication rate for the proposed MMSE state estimator at time step $k$ can be computed using the approximation $\text{E}[\gamma_{k}]\approx\frac{1}{N}\sum_{i=1}^{N}\gamma_{k,i}$ where $\gamma_{k,i}$ is the 
N ∑N
i=1γk,i where E[γk] = 1

      N ∑N
         i=1 γk,i when N approaches infinity. The average
communication rate is defined as γ = lim
                                 k→∞
                                     1
                                     k ∑k−1
                                       j=0 E[γj], and

the average communication rate is approximately computed
via γ ≈
         1
        101 ∑100
             j=0 E[γj] in the Monte Carlo simulation. The

|   Case |   SECL |   Algorithm 1 |   Algorithm 2 |
|--------|--------|---------------|---------------|
|      1 | 0.3812 |        0.373  |        0.3761 |
|      2 | 0.5684 |        0.5696 |        0.5678 |
|      3 | 0.2798 |        0.275  |        0.2712 |

MMSE state estimator based on confidence level proposed in this paper is referred to as SECL. The RMS position and velocity errors of SECL for three different cases are given in Figs. 2 and 3, respectively. The communication rates of SECL, Algorithm 1 and Algorithm 2 at Cases 1, 2 and 3 are provided in Figs. 4, 5 and 6, respectively, where, without loss of generality, we take the information at the 40th trial for running Algorithms 1 and 2. From Figs. 2−6, we find that, for both position and velocity estimate at the three different cases, SECL has different performances, and the performance is connected with the communication rate. More precisely, the performance of SECL becomes better and better with the increase of communication rate. This indicates the effectiveness of the MMSE state estimator based on confidence level proposed in this paper. Figs. 4−6 also shows that Algorithm
2 provides a good estimate for the communication rate of SECL because the communication rate yielded by Algorithm 2 is close to the communication rate of SECL. The average communication rates of SECL, Algorithm 1 and Algorithm 2 for the three cases are provided in Table I. We see from Table I that the average communication rates of SECL, Algorithm 1 and Algorithm 2 are very close at all the three cases, which means that both Algorithm 1 and Algorithm 2 yield good performance for estimating the average communication rates of SECL.

Hence, the simulation results indicate that SECL is effective in solving state estimation with the trade-off between communication rate and state estimation performance, and that Algorithm 2 yields a good performance in estimating the communication rate and the average communication rate of SECL.

## B. Comparison With Sehi

We compare SECL with SEHI still using the above target tracking example where we take the same parameter values except for the tolerable upper bound N. In the comparison with SEHI, we take N = Na ≜ 0.695×
� 60
10
10
20
�
which is a slight change of N at Case 3 in Section V-A through multiplying by 0.695. After a Monte Carlo simulation, we get the average communication rate of SECL is 0.35 when N = Na.

Considering fairness, we compare SECL with SEHI under the same average communication rate. Using Monte Carlo simulation, we get δ = 1.5565 when the average communication rate of SEHI is 0.35. The target's RMS position errors of SECL
and SEHI under the same average communication rate 0.35 are provided in Fig. 7, and the corresponding velocity errors are provided in Fig. 8.

From observing Figs. 7 and 8, we find that SECL performs better than SEHI in target tracking accuracy for both position and velocity. Hence, the simulation results show that SECL yields better tracking performance in contrast to SEHI.

## Vi. Conclusion

Based on confidence level, a novel event-triggered scheme has been proposed using the chi-square distribution and regular Gaussian assumption. The novel scheme was applied to the state estimation problem for discrete-time linear systems in the environment of wireless sensor network so that a MMSE state estimator was proposed. Two algorithms for estimating the communication rate of the proposed state estimator have been developed where, at time step k, the first algorithm is based on information up to k−1, and the second algorithm is based on information up to k−2. A target tracking scenario has been given to examine the performance of the proposed results, and the simulation results have shown that the proposed state estimator performs better than SEHI under the same average communication rate. The simulation results have also shown that Algorithm 2 provides a good estimate for the communication rate of the proposed state estimator.

## Appendix A Proof Of Lemmas 1−3

Proof of Lemma 1: Using (1), we have

$$f(x_{k}|{\rm I}_{k-1})=f(Ax_{k-1}+\omega_{k-1}|{\rm I}_{k-1}).\tag{82}$$
From Assumptions 1 and 2, we see that ωk−1 is independent of xk−1 and Ik−1. Hence, f(xk|Ik−1) is a linear combination of two Gaussian and mutually independent random vectors f(xk−1|Ik−1) and ωk−1, that is Af(xk−1|Ik−1) + ωk−1.

Then, using Remark 4, we prove 1). Applying (2), we have f(yk|Ik−1) = f(Cxk + υk|Ik−1). Then, using 1) of Lemma 1, and referring to the proof of 1) of Lemma 1, we prove 2).

Proof of Lemma 2: 1). Using (10), (4) and (2), we get

$\mathbb{Z}=\Phi\mathbb{C}x_{k}+\Phi\mathbb{D}_{k}-\Phi\mathbb{D}_{k,k-1}$. (83)
Then, using 1) of Lemma 1, and making reference to the proof of 1) of Lemma 1, we prove 1). 2). Applying (10), (4) and (3), we get

$$\mathrm{E}[z_{k}|\mathrm{I}_{k-1}]=\Phi\mathrm{E}[\hat{y}_{k}|\mathrm{I}_{k-1}]=\Phi(\hat{y}_{k,k-1}-\hat{y}_{k,k-1})=0.\tag{84}$$

Then, applying 1) of Lemma 2, we prove 2).
  Proof of Lemma 3: 1). From (8) and (9), it follows that
ϕk ≤ χ2
      α(p) is equivalent to ∑p
                           i=1 z2
                               k,i ≤ χ2
                                     α(p). Then, using the
definition of Ωk presented in (12), we obtain

p ∑ i=1 z2 k,i ≤ χ2 α(p) � . (85) Ωk = � zk,1,zk,2,··· ,zk,p ∈ R ���� Ωk f(zk|Ik−1)zkzT k dzk

Then, using (85) and 2) of Lemma 2, we prove 1).
2). Noticing zk ∈ Rp, we have zkzT
                                k = (ζk,ij)p×p with ζk,ij =
zk,izk,j. Then, using 2) of Lemma 2, we have
 �

g(zk) Ωk = � = 1 (2π)0.5p��N[z] k ��0.5 (ζk,ij)p×pdzk,1dzk,2 ···dzk,p Ωk g(zk)ζk,ijdzk,1dzk,2 ···dzk,p p×p . � �� (86) (2π)0.5p��N[z] k ��0.5 Ωk g(zk)ζk,ijdzk,1dzk,2 ···dzk,p
Using (85) and noticing ζk,ij = zk,izk,j, we have
�

= dzk,1 g(zk)zk,izk,jdzk,p (87) dzk,2 ··· ˇb � ˇzk,1 � ˇzk,p−1 � −ˇzk,1 −ˇzk,p−1 −ˇb Ωk f(zk|Ik−1)zkzT k dzk = (ψk,ij)p×p
where ˇb and ˇzk,i with i = 1,2,··· , p − 1 are defined in 1) of Lemma 3. Substituting (87) into (86), as well as using the definition of ψk,ij and Ψk given in 2) of Lemma 3, we have
�

(88) (2π)0.5p��N[z] k ��0.5 = Ψk (2π)0.5p��N[z] k ��0.5 .
This complete the proof of the statement.

## Appendix B Proof Of Theorem 1 Derivation Of (22). When Γk = 0, We Have

$$\hat{\hat{x}}_{k}=\int_{\mathbb{R}^{n}}x_{k}f(x_{k}|\mathrm{I}_{k})dx_{k}=\int_{\mathbb{R}^{n}}x_{k}f(x_{k}|\mathrm{I}_{k-1},\gamma_{k}=0)dx_{k}.\tag{89}$$
By (8), f(xk|Ik−1,γk = 0) can be expressed as

= f(xk|Ik−1,zk ∈ Ωk) f(xk|Ik−1,γk = 0) = f � xk|Ik−1,ϕk ≤ χ2 α(p) � = f(xk,Ik−1,zk ∈ Ωk) f(Ik−1,zk ∈ Ωk) = � Ωk f(xk,Ik−1,zk)dzk � Ωk f(Ik−1,zk)dzk = � Ωk f(xk|Ik−1,zk)f(zk|Ik−1)dzk � Ωk f(zk|Ik−1)dzk (90)
where the second and last equalities are due to (12) and Bayes' rule, respectively. Substituting (90) into (89) yields that

Rn xk ˆxk = � � Ωk f(xk|Ik−1,zk)f(zk|Ik−1)dzk � Ωk f(zk|Ik−1)dzk dxk = � Rn xk � Ωk f(xk|Ik−1,zk)f(zk|Ik−1)dzkdxk � Ωk f(zk|Ik−1)dzk = � Ωk f(zk|Ik−1) � Rn xk f(xk|Ik−1,zk)dxkdzk � Ωk f(zk|Ik−1)dzk = � Ωk f(zk|Ik−1)ˆx[z] k dzk � Ωk f(zk|Ik−1)dzk . (91) Making reference to the proof of Theorem 3.2 in [10], we can obtain � Ωk f(zk|Ik−1)ˆx[z] k dzk � Ωk f(zk|Ik−1)dzk =ˆxk,k−1. (92)
where ˆxk,k−1 is defined in (15). Substituting (92) into (91), we derive (22). Derivation of (23). Using (18) and the definition of conditional covariance matrix, we have Substituting (84) into (93), and using (10), we derive

N[z] k = E � (zk − E[zk|Ik−1])(zk − E[zk|Ik−1])T� . (93) N[z] k = E � zkzT k � = E � Φ ˜yk ˜yT k ΦT� = Φ(CMkCT + R)ΦT (94)
where Mk is defined in (17). Similarly, we have

$$\mathrm{E}\Big{[}\tilde{x}_{k}(z_{k}-[z_{k}|\mathrm{I}_{k-1}])^{\mathrm{T}}\Big{]}=\mathrm{E}\Big{[}\tilde{x}_{k}z_{k}^{\mathrm{T}}\Big{]}=M_{k}C^{\mathrm{T}}\Phi^{\mathrm{T}}.\tag{95}$$

Substituting (94) and (95) into (19) yields (23).

Derivation of (24). Utilizing Kalman filter, we get

$$\hat{x}_{k}^{[z]}=\hat{x}_{k,k-1}+K_{k}(z_{k}-\mathrm{E}[z_{k}|\mathrm{I}_{k-1}])\tag{96}$$
where ˆx[z]
k and Kk are defined in (13) and (19), respectively, and N[z]
k in Kk is defined in (18). Substituting (84) into (96), we obtain

ˆx[z] k = ˆxk,k−1 + Kkzk. (97)
From (14), (13) and the definition of conditional covariance matrix, it follows that

$$P_{k}^{[z]}=\mathrm{E}\bigg{[}\left(x_{k}-\hat{x}_{k}^{[z]}\right)\left(x_{k}-\hat{x}_{k}^{[z]}\right)^{\mathrm{T}}\bigg{]}.\tag{98}$$

Substituting (97) into (98) and using (16), we obtain  $$P(\gamma_{k}=0|\mathrm{I}_{k-2},\bar{z}_{k-1})=P(z_{k}\in\Omega_{k}|\mathrm{I}_{k-2},\bar{z}_{k-1})$$ $$=\int_{\Omega_{k}}f(z_{k}|\mathrm{I}_{k-2},\bar{z}_{k-1})dz_{k}.\tag{142}$$
Then, replacing P(γk = 0|Ik−2,zk−1) by ⃗P[z]
k (0), we derive (66).

In the same way, we can obtain (67) where ˘Pk(0) is defined in (51).

Derivation of (68). P(γk = 0|Ik−2) can be given by

$$P(\gamma_{k}=0|{\rm I}_{k-2})$$ $$=P(\gamma_{k-1}=0|{\rm I}_{k-2})P(\gamma_{k}=0|{\rm I}_{k-2},\gamma_{k-1}=0)$$ $$\quad+P(\gamma_{k-1}=1|{\rm I}_{k-2})P(\gamma_{k}=0|{\rm I}_{k-2},\gamma_{k-1}=1).\tag{143}$$
P(γk = 0|Ik−2,γk−1 = 1) can be given by

$$P(\gamma_{k}=0|\mathrm{I}_{k-2},\gamma_{k-1}=1)$$ $$=\frac{P(\mathrm{I}_{k-2},\gamma_{k-1}=1,\gamma_{k}=0)}{P(\mathrm{I}_{k-2},\gamma_{k-1}=1)}$$ $$=\frac{P(\mathrm{I}_{k-2},z_{k-1}\in\tilde{\Omega}_{k-1},\gamma_{k}=0)}{P(\mathrm{I}_{k-2},z_{k-1}\in\tilde{\Omega}_{k-1})}$$ $$=\frac{\int_{\tilde{\Omega}_{k-1}}f(\mathrm{I}_{k-2},z_{k-1},\gamma_{k}=0)dz_{k-1}}{\int_{\tilde{\Omega}_{k-1}}f(\mathrm{I}_{k-2},z_{k-1})dz_{k-1}}$$ $$=\frac{\int_{\tilde{\Omega}_{k-1}}\tilde{P}_{k}^{(2)}(0)f(\mathrm{I}_{k-2},z_{k-1})dz_{k-1}}{\int_{\tilde{\Omega}_{k-1}}f(\mathrm{I}_{k-2},z_{k-1})dz_{k-1}}$$ $$=\frac{\int_{\tilde{\Omega}_{k-1}}\tilde{P}_{k}^{(2)}(0)f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}}{\int_{\tilde{\Omega}_{k-1}}f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}}$$ $$=\frac{\int_{\tilde{\Omega}_{k-1}}\tilde{P}_{k}^{(2)}(0)f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}}{P(\gamma_{k-1}=1|\mathrm{I}_{k-2})}\tag{144}$$
where ˘Ωk and ⃗P[z]
k (0) are defined in (57) and (50), respectively.

Substituting (144) into (143), as well as replacing P(γk−1 =
0|Ik−2) by Pk−1,k−2(0), we obtain

$$P(\gamma_{k}=0|{\rm I}_{k-2})=P_{k-1,k-2}(0)P(\gamma_{k}=0|{\rm I}_{k-2},\gamma_{k-1}=0)$$ $$+\int_{\Omega_{k-1}}\vec{P}_{k}^{[\varepsilon]}(0)f(z_{k-1}|{\rm I}_{k-2})dz_{k-1}.\tag{145}$$
Then, replacing P(γk = 0|Ik−2) and P(γk = 0|Ik−2,γk−1 = 0)
by Pk,k−2(0) and ˘Pk(0), respectively, we derive (68). Making reference to (46), we easily obtain (69).

## Appendix D Proof Of Algorithm 2

Making reference to the proof of 1) of Lemma 3, we can obtain (71) by using (64) and (66). Similarly, we obtain (72) by using (65) and (67). From (66), (64) and (70), we see that $\vec{P}_{k}^{[z]}(0)$ does not contain the random vector $z_{k-1}$. Hence, we have

$$\int_{\Omega_{k-1}}\vec{P}_{k}^{[z]}(0)f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}$$ $$=\vec{P}_{k}^{[z]}(0)\int_{\hat{\Omega}_{k-1}}f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}$$ $$=\vec{P}_{k}^{[z]}(0)\Big{(}\int_{\mathbb{R}^{p}}f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}-\int_{\Omega_{k-1}}f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}\Big{)}$$ $$=\bar{P}_{k}^{[z]}(0)\Big{(}1-\int_{\Omega_{k-1}}f(z_{k-1}|\mathrm{I}_{k-2})dz_{k-1}\Big{)}$$ $$=\bar{P}_{k}^{[z]}(0)\Big{(}1-\frac{h_{k-1}}{(2\pi)^{0.5}p\big{|}N_{k-1}^{[z]}}\big{|}^{0.5}\Big{)}$$ $$=\bar{P}_{k}^{[z]}(0)\big{(}1-P_{k-1,k-2}(0)\big{)}\tag{146}$$

where the fourth equality is due to 1) of Lemma 3, and the last equality is because of (58). Substituting (146) into (68), we get

$$P_{k,k-2}(0)=P_{k-1,k-2}(0)\bar{P}_{k}(0)+\bar{P}_{k}^{[z]}(0)\big{(}1-P_{k-1,k-2}(0)\big{)}$$ $$=\bar{P}_{k}^{[z]}(0)+P_{k-1,k-2}(0)\big{(}\bar{P}_{k}(0)-\bar{P}_{k}^{[z]}(0)\big{)},\tag{1}$$
which means that (73) holds.

$$=\vec{P}_{k}^{[z]}(0)+P_{k-1,k-2}(0)(\vec{P}_{k}(0)-\vec{P}_{k}^{[z]}(0)),\tag{147}$$

that (73) holds.

## References

[1] J. P. Hespanha, P. Naghshtabrizi, and Y. Xu, "A survey of recent results
in networked control systems", *Proc. IEEE*, vol. 95, no. 1, pp. 138-162,
Jan. 2007.
[2] S. Wildhagen, J. Berberich, M. Hertneck, and F. Allg¨ower, "Data-driven
analysis and controller design for discrete-time systems under aperiodic
sampling", *IEEE Trans. Autom. Control*, vol. 68, no. 6, pp. 3210-3225,
Jun. 2023.
[3] J. Shang, H. Yu, and T. Chen, "Worst-case stealthy attacks on stochastic
event-based state estimation", *IEEE Trans. Autom. Control*, vol. 67, no.
4, pp. 2052-2059, Apr. 2022.
[4] W. Liu, P. Shi, and S. Wang, "Distributed Kalman filtering through trace
proximity", *IEEE Trans. Autom. Control*, vol. 67, no. 9, pp. 4908-4915,
Sep. 2022.
[5] J. Hu, B. Lennox, and F. Arvin, "Robust formation control for networked
robotic systems using negative imaginary dynamics", *Automatica*, vol.
140, 2022, Art. no. 110235.
[6] I. Z. Petric, P. Mattavelli, and S. Buso, "Multi-sampled grid-connected
VSCs: A path toward inherent admittance passivity", IEEE Trans. Power Electron., vol. 37, no. 7, pp. 7675-7687, Jul. 2022.
[7] J. J. Xiao, A. Ribeiro, Z. Q. Luo, and G. B. Giannakis, "Distributed
compression-estimation using wireless sensor networks", IEEE Trans. Signal Process. Mag., vol. 23, no. 4, pp. 27-41, Jul. 2006.
[8] A. Ribeiro, G. B. Giannakis, and S. I. Roumeliotis, "SOI-KF: Distributed
Kalman filtering with low-cost communications using the sign of innovations", *IEEE Trans. Signal Process.*, vol. 54, no. 12, pp. 4782-4795,
Dec. 2006.
[9] E. J. Msechu, S. I. Roumeliotis, A. Ribeiro, and G. B. Giannakis,
"Decentralized quantized Kalman filtering with scalable communication
cost", *IEEE Trans. Signal Process.*, vol. 56, no. 8, pp. 3727-3741, Aug.
2008.
[10] J. Wu, Q. S. Jia, K. H. Johansson, and L. Shi, "Event-based sensor
data scheduling: Trade-off between communication rate and estimation
quality", *IEEE Trans. Autom. Control*, vol. 58, no. 4, pp. 1041-1046,
Apr. 2013.
[11] G. M. Lipsa and N. C. Martins, "Remote state estimation with communication costs for first-order LTI systems", *IEEE Trans. Autom. Control*,
vol. 56, no. 9, pp. 2013-2025, Sep. 2011.
[12] G. Battistelli, A. Benavoli, and L. Chisci, "Data-driven communication
for state estimation with sensor networks", *Automatica*, vol. 48, no. 5,
pp. 926-935, May 2012.
[13] J. Sijs and M. Lazar, "Event based state estimation with time synchronous updates", *IEEE Trans. Autom. Control*, vol. 57, no. 10, pp.
2650-2655, Oct. 2012.
[14] K. You and L. Xie, "Kalman filtering with scheduled measurements",
IEEE Trans. Signal Process., vol. 61, no. 6, pp. 1520-1530, Mar. 2013.
[15] D. Shi, T. Chen, and L. Shi, "An event-triggered approach to state estimation with multiple point- and set-valued measurements", *Automatica*,
vol. 50, no. 6, pp. 1641-1648, Jun. 2014.
[16] S. Trimpe and R. D'Andrea, "Event-based state estimation with
variance-based triggering", *IEEE Trans. Autom. Control*, vol. 59, no. 12,
pp. 3266-3281, Dec. 2014.
[17] D. Shi, T. Chen, and L. Shi, "On set-valued Kalman filtering and its
application to event-based state estimation", *IEEE Trans. Autom. Control*,
vol. 60, no. 5, pp. 1275-1290, May 2015.
[18] D. Han, Y. Mo, J. Wu, S. Weerakkody, B. Sinopoli, and L. Shi,
"Stochastic event-triggered sensor schedule for remote state estimation",
IEEE Trans. Autom. Control, vol. 60, no. 10, pp. 2661-2675, Oct. 2015.
[19] S. Weerakkody, Y. Mo, B. Sinopoli, D. Han, and L. Shi, "Multi-sensor
scheduling for state estimationwith event-based, stochastic triggers",
IEEE Trans. Autom. Control, vol. 61, no. 9, pp. 2695-2701, Sep. 2016.
[20] A. Mohammadi and K. N. Plataniotis, "Event-based estimation with
information-based triggering and adaptive update", IEEE Trans. Signal
Process., vol. 65, no. 18, pp. 4924-4939, Sep. 2017.
[21] L. He, J. Chen, and Y. Qi, "Event-based state estimation: Optimal
algorithm with generalized closed skew normal distribution", IEEE Trans.
Autom. Control, vol. 64, no. 1, pp. 321-328, Jan. 2019.
[22] Z. Hu, B. Chen, R. Wang, and L. Yu, "Remote state estimation with
posterior-based stochastic event-triggered schedule", IEEE Trans. Autom. Control, vol. 69, no. 2, pp. 1194-1201, Feb. 2024.
[23] H. Yu, J. Shang, and T. Chen, "On stochastic and deterministic eventbased state estimation", *Automatica*, vol. 123, 2021, Art. no. 109314.
[24] G. Battistelli, L. Chisci, and D. Selvi, "A distributed Kalman filter with
event-triggered communication and guaranteed stability", *Automatica*,
vol. 93, pp. 75-82, Jul. 2018.
[25] M. Miskowicz, "Send-on-delta concept: An event-based data reporting
strategy", *Sensors*, vol. 6, no. 1, pp. 49-63, Jan. 2006.
[26] R. Cogill, S. Lall, and J. P. Hespanha, "A constant factor approximation
algorithm for event-based sampling", *in Proc. 2007 Amer. Control Conf.*,
New York, USA, Jul. 2007, pp. 305-311.
[27] L. Li, M. Lemmon, and X. Wang, "Event-triggered state estimation in
vector linear processes", *in Proc. 2010 Amer. Control Conf.*, Baltimore,
USA, Jun. 2010, pp. 2138-2143.
[28] R. A. Johnson and D. W. Wichern, Applied multivariate statistical
analysis, 6th ed., Upper Saddle River: Pearson prentice hall, 2007.
[29] R. A. Singer, "Estimating optimal tracking filter performance for manned
maneuvering targets", *IEEE Trans. Aerosp. Electron. Syst.*, vol. AES-6,
no. 4, pp. 473-483, Jul. 1970.