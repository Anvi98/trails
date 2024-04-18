
## Robust Resource Allocation For Star-Ris Assisted Swipt Systems

Guangyu Zhu, Xidong Mu, *Member, IEEE,* Li Guo, *Member, IEEE,* Ao Huang, and Shibiao Xu, Member, IEEE

  Abstract—A simultaneously transmitting and reflecting recon-
figurable intelligent surface (STAR-RIS) assisted simultaneous
wireless information and power transfer (SWIPT) system is
proposed. More particularly, an STAR-RIS is deployed to assist
in the information/power transfer from a multi-antenna access
point (AP) to multiple single-antenna information users (IUs) and
energy users (EUs), where two practical STAR-RIS operating
protocols, namely energy splitting (ES) and time switching (TS),
are employed. Under the imperfect channel state information
(CSI) condition, a multi-objective optimization problem (MOOP)
framework, that simultaneously maximizes the minimum data
rate and minimum harvested power, is employed to investigate
the fundamental rate-energy trade-off between IUs and EUs. To
obtain the optimal robust resource allocation strategy, the MOOP
is first transformed into a single-objective optimization problem
(SOOP) via the ǫ-constraint method, which is then reformulated
by approximating semi-infinite inequality constraints with the
S-procedure. For ES, an alternating optimization (AO)-based
algorithm is proposed to jointly design AP active beamforming
and STAR-RIS passive beamforming, where a penalty method is
leveraged in STAR-RIS beamforming design. Furthermore, the
developed algorithm is extended to optimize the time allocation
policy and beamforming vectors in a two-layer iterative manner
for TS. Numerical results reveal that: 1) deploying STAR-RISs
achieves a significant performance gain over conventional RISs,
especially in terms of harvested power for EUs; 2) the ES protocol
obtains a better user fairness performance when focusing only
on IUs or EUs, while the TS protocol yields a better balance
between IUs and EUs; 3) the imperfect CSI affects IUs more
significantly than EUs, whereas TS can confer a more robust
design to attenuate these effects.

  Index Terms—Reconfigurable intelligent surfaces, simultane-
ous transmission and reflection, simultaneous wireless informa-
tion and power transfer, resource allocation, imperfect CSI.

## I. Introduction

With the rapid growth in the number of Internet-of-Things
(IoT) devices, the sustainability of equipment and energy supply has become one of the bottlenecks restricting the development of next generation wireless networks [2], [3].

Part of this work was presented at the IEEE International Conference on Communications (ICC), Rome, Italy, May 28– June 1, 2023. [1]
Guangyu Zhu, Li Guo, Ao Huang and Shibiao Xu are with the Key Laboratory of Universal Wireless Communications, Ministry of Education, Beijing University of Posts and Telecommunications, Beijing 100876, China, also with the School of Artificial Intelligence, Beijing University of Posts and Telecommunications, Beijing 100876, China, also with the Engineering Research Center of Ministry of Education for Chain Network Convergence Technology, and also with the National Engineering Research Center for Mobile Internet Security Technology, Beijing University of Posts and Telecommunications, Beijing 100876, China (email:{Zhugy, guoli, huangao, shibiaoxu}@bupt.edu.cn).

Xidong Mu is with the School of Electronic Engineering and Computer Science, Queen Mary University of London, London E1 4NS, U.K. (email:{xidong.mu}@qmul.ac.uk).

To address this issue, simultaneous wireless information and power transfer (SWIPT) as a promising technique has been investigated in [4], [5]. In the SWIPT system, as the carrier of both information and energy, radio-frequency (RF) signals can realize the parallel information exchange and energy supply for IoT devices. In this case, balancing wireless communication and energy transfer becomes an important criterion in the SWIPT system [6]. However, due to the drastically different power sensitivities to receiver and transmission environments, wireless power transfer (WPT) has a significant efficiency gap compared to wireless information transfer (WIT). Especially over a long communication distance, the propagation loss will seriously reduce the efficiency of WPT, which poses a huge challenge for resource allocation to balance the performance of information users (IUs) and energy users (EUs). In this connection, smart antenna technologies are introduced into the SWIPT system to improve user performance [7]. At the same time, however, it should be noted that the increase in active antennas will be accompanied by more energy consumption, higher design complexity, and higher hardware costs. This virtually brings new obstacles to implementation in practice.

Recently, reconfigurable intelligent surfaces (RISs) [8] have emerged as a key rising technology for future communication networks, thanks to their impressive performance in terms of energy efficiency [9]. An RIS is a two-dimensional (2D) surface, comprising large numbers of low-cost and passive meta-materials with tunable reflection properties. Ideally, each reconfigurable element can independently adjust the phase shift and amplitude of the incident signals according to the practical transmission needs, thus facilitating the creation of "Smart Radio Environments (SREs)" [10]. Besides, due to the near-passive operation and low hardware footprints, RIS assisted system is more cost-efficient and deployment-flexible compared to conventional active antenna systems. Given these appealing features, the combination of RISs and SWIPT has attracted increasing attention [11].

However, limited by their reflection-only nature, RISs can only serve transmitters and receivers located in the same side. This strict geographical restriction severely undermines user fairness and the effectiveness of introducing RISs. To break this limitation and thus achieve *full*-space SREs, a novel concept of RISs, i.e., simultaneously transmitting and reflecting RISs (STAR-RISs), has been proposed [12]. Unlike conventional reflecting-only RISs, STAR-RISs can not only reflect but also transmit the incident signals via dynamic configuration adjustment for all users located in both sides of STAR-RISs [13]. Furthermore, STAR-RISs can exploit extra degrees of freedom (DoFs) for system design [14], which may enable more flexible wireless resource allocation to coordinate the performance between WPT and WIT for SWIPT systems. A. Prior Works
1) *Studies on Resource Allocation for RIS Assisted SWIPT*:
Enlightened by the enormous potential gains of RISs to transmission efficiency, the new research paradigm of resource allocation for RIS assisted SWIPT has been extensively studied recently in [15]–[23]. In particular, the authors of [15] proposed a single-objective optimization problem (SOOP) for maximizing the weighted sum-power, subject to the individual signal-to-interference-plus-noise ratio (SINR) constraints for IUs in RIS aided multiple input single output (MISO) SWIPT systems. On the contrary, the maximization problem for weighted sum-rate, subject to the total harvested power constraints for EUs in RIS assisted multiple input multiple output (MIMO) SWIPT systems was considered in [16]. In other aspects, under the quality-of-service (QoS) requirements, the authors of [17] proposed to optimize the joint active and passive beamforming for transmit power minimization in a multiple RISs assisted SWIPT system. The authors further proposed two low-complexity suboptimal algorithms based on maximum ratio transmission (MRT) and zero-forcing (ZF) beamforming techniques to minimize the transmit power at the BS in [18]. Besides, the authors of [19] investigated a similar transmit power minimization problem for a large-scale RIS aided SWIPT system. Considering further the non-linear harvested model, the authors of [20] employed a block coordinate descent (BCD) method to jointly optimize the active beamforming and passive beamforming for minimization of transmit power under the imperfect channel state information
(CSI) assumption. However, the above studies only focus on either data rate or harvested power. To better portray the conflict between IUs and EUs in SWIPT, the rate-energy trade-offs were investigated in [21]–[23]. Specifically, a multi-objective optimization problem (MOOP) framework was studied by the authors of [21], where energy/information beamforming vectors at the BS and phase shifts at the RIS were jointly optimized to obtain the fundamental trade-off between sumrate and total harvested energy. In [22], the authors jointly optimized waveform, active and passive beamforming by applying a BCD method to achieve a rate-energy region. Besides, the authors of [23] adopted a realistic-based RIS model in a RIS assisted MISO multiuser SWIPT system, where the tradeoff between IUs and EUs was investigated by a penalty-based algorithm.

2) *Studies on STAR-RIS Assisted Communication*: There have been some early efforts to capitalize on the benefits of STAR-RIS deployment in wireless communication systems [12], [24]–[27]. In [12], the authors studied a STAR-RIS assisted two-user downlink MISO system and proposed three different protocols, i.e., energy splitting (ES), mode switching (MS), and time switching (TS), for practical operation. To explore the advantages of each protocol, the authors further study the power consumption minimization problems of unicast and multicast on different protocols. In [24], the authors considered a STAR-RIS aided multi-carrier communication network, where the resource allocation design was achieved for both non-orthogonal multiple access (NOMA)
and orthogonal multiple access (OMA) via jointly optimizing the channel assignment, power allocation, and the STAR- RIS configuration. The authors of [25] studied a STAR-RIS aided unmanned aerial vehicle (UAV) system and proposed a novel distributionally-robust reinforcement learning algorithm to get a robust design for sum-rate maximization. In [26], resource allocation for STAR-RIS assisted wireless powered mobile edge computing (MEC) systems was investigated, which illustrated that TS is a more suitable protocol for uplink transmission in MEC. Besides, the STAR-RIS assisted SWIPT was introduced in [27], where the achievable worstcase sum secrecy rate was maximized by applying a convex approximation method.

B. Motivations and Contributions Although the introduction of RISs brings significant performance improvements to SWIPT systems, the *half*-space coverage feature of reflecting-only RISs greatly limits its applicability in practical implementation. Benefiting from the simultaneous transmission and reflection characteristics, the STAR-RIS is envisaged as a potential technology to break this fundamental limitation. By leveraging enhanced DoFs, the STAR-RIS can not only improve SWIPT system performance, but also realize *full*-space coverage for both IUs and EUs.

Inspired by this, we propose to introduce the STAR-RIS into the SWIPT system in this paper. To the best of our knowledge, few efforts have been devoted to this topic. Therefore, there are several urgent issues that need to be explored before STAR- RISs can be harmoniously integrated into the existing SWIPT systems.

Firstly, thanks to the *full*-space coverage, the distribution of served users can be more random and dispersed in a STAR- RIS assisted SWIPT system. However, this potential variation may magnify the channel differences among users, thus posing a more intractable resource allocation challenge to balance the performance between IUs and EUs. More importantly, the addition of STAR-RISs will introduce more optimization variables that are not considered in the conventional reflectingonly RIS assisted SWIPT system. Accordingly, the formulated optimization problems will be more intractable, which is beyond the capabilities of the methods applied in [21]–[23]. As such, efficient algorithms need to be developed to resolve the resource allocation problem for STAR-RIS assisted SWIPT systems.

Secondly, most of the aforementioned researches [24]–[26]
assumed that the perfect CSI of all channels was available to the base station (BS) or access point (AP). However, since there are more channels associated with passive STAR-RISs, more overhead and advanced channel estimation algorithms than conventional reflecting-only RISs need to be invested in the acquisition of accurate CSI. This is a very challenging but still infancy task [28]. Therefore, in order to reduce the impact of channel uncertainty on system performance in practical scenarios, it is necessary to investigate a robust design to deal with channel estimation errors.

Thirdly, the authors of [12] proposed three different operating protocols for STAR-RIS and revealed their respective benefits for different communication scenarios and requirements.

Interestingly, EUs and IUs have different power sensitivities to signal beams, transmission environments, and inter-user interference in the SWIPT system. Bearing all this in mind, a new but crucial question, i.e., Which protocol is more suitable for the SWIPT system? is naturally raised. Note that the authors of [27] only considered the ES protocol for STAR-RIS assisted SWIPT and did not answer this question, which is still an open issue and needs to be answered.

Motivated by these observations, we investigate the robust resource allocation for a STAR-RIS assisted SWIPT system based on the imperfect CSI assumption. In particular, two operating protocols, i.e., ES and TS, are considered. The main contributions of this paper are summarized as follows:

- We propose a STAR-RIS assisted SWIPT system, where
an STAR-RIS is deployed to assist a multi-antenna AP
to simultaneously transmit information and power to two types of single-antenna users, i.e., IUs and EUs. From a practical perspective, we consider the imperfect CSI for all channels. In order to investigate the fundamental tradeoff between IUs and EUs, we formulate MOOPs for both ES and TS to simultaneously maximize the minimum data rate for IUs and the minimum harvested power among EUs.
- For ES, we first leverage the ǫ-constraint method to
transform the resulting MOOP into a more tractable SOOP. Then, we adopt the general S-procedure to approximate the semi-infinite inequality constraints for any
given ǫ. Finally, to solve the reformulated highly-coupled
non-convex SOOP, we develop an efficient alternating optimization (AO) framework by solving the active AP beamforming and passive STAR-RIS beamforming in an iterative manner. In particular, a penalty-based method is leveraged to relax the rank-one constraint for STAR- RIS beamforming optimization. Besides, to ensure the
feasibility of ǫ-constraint method, we apply bisection
search to obtain the performance upper boundary of IUs
and determine the reasonable range for ǫ.
- For TS, we still apply the ǫ-constraint method and general
S-procedure to transform the MOOP. Subsequently, we extend the proposed algorithm for ES into a two-layer optimization algorithm to solve the reformulated SOOP. In the outer-layer iteration, we determine the optimal time allocation via one-dimensional search. While for the inner-layer, we update the remaining variables by utilizing the AO-based algorithm in each iteration.
- Our numerical results depict that 1) deploying STAR-
RISs can achieve a significant rate-energy region gain to conventional RISs in SWIPT systems, especially in terms of harvested power; 2) ES is more attractive for improving user fairness when focusing only on IUs or EUs, while TS is superior at balancing the performance between IUs and EUs. More importantly, TS can provide a more robust design under the imperfect CSI; 3) the deployment strategy of having all EUs on the same side of the STAR-RIS while all IUs on the other side yields higher performance gains, but also results in more
implementation difficulties.

## C. Organization And Notations

The rest paper is organized as follows: Section II introduces the system model and the joint beamforming MOOP formulations for both ES and TS protocols. In Section III, efficient solutions are proposed for robust resource allocation based on each operating protocol. Next, the numerical results are presented to verify the benefits of deploying the STAR-RIS in a SWIPT system in Section IV. Finally, Section V concludes the paper.

Notations: Scalars, vectors, and matrices are denoted by lower-case, bold lower-case letters, and bold upper-case letters, respectively. ∥a∥ denotes the Euclidean norm of vector a, aH and aT denotes the conjugate transpose and transpose of vector a, respectively. For a square matrix A, Tr(A), Rank(A), AH, AT denote its trace, rank, conjugate transpose, and transpose, respectively, while A ⪰ 0 represents that A is a positive semidefinite matrix. And Diag (A) denotes a vector whose elements are extracted from the main diagonal elements of matrix A. ∥A∥∗, ∥A∥2, ∥A∥F denote the nuclear norm, spectral norm, and Frobenius norm of matrix A, respectively.

CM×N and RM×N denote the space of M×N complex valued matrices and real valued matrices respectively. IM×M denotes an identity matrix of size M ×M. ⊗ represents the Kronecker product. Finally, the distribution of a circularly symmetric complex Gaussian (CSCG) random variable with mean µ and variance σ is denoted by CN(µ, σ2).

## Ii. System Model And Problem Formulation

As shown in Fig. 1, we consider a STAR-RIS assisted wireless system, where an STAR-RIS consisting of M elements is deployed to facilitate SWIPT from the AP with N antennas to two different sets of single-antenna users, i.e., IUs and EUs. The sets of IUs and EUs are denoted by KI = {1, · · · , KI} and KE = {1, · · · , KE}, respectively. We assume these users are randomly located in both the reflection (R) and transmission (T) regions of the STAR-RIS. Without loss of generality, we assume the direct links between the AP and users are blocked by obstacles, and the communication for users in blind spots is supported by the STAR-RIS enabled transmission and reflection links [24]–[27]. The quasi-static flat-fading model is assumed for all channels1, and the channel coefficients from the AP to the STAR-RIS, from the STAR-
RIS to IU i, and from the STAR-RIS to EU j are denoted by G ∈ CM×N, hi ∈ CM×1, and gj ∈ CM×1, respectively.

## A. Star-Ris Protocols And Models

In this paper, we consider the ES and TS protocols for STAR-RISs proposed in [12].

1) The ES protocol: All elements of the STAR-RIS can split an incident signal into two independent signals, i.e., reflected and transmitted signals. Based on energy splitting, the beamforming matrix is divided into the reflectioncoefficient part and the transmission-coefficient part, denoted by ΘES
r
=
diag
��

βr
 1ejθr
    1, · · · ,
         �

βr
 Mejθr
    M �
        and ΘES
             t
                =

diag
    ��

βt
 1ejθt
   1, · · · ,
        �

                βt
                 Mejθt
                     M
                       �
                        , respectively. Here, βr
                                        m, βt
                                           m
∈ [0, 1] and θr
          m, θt
             m ∈ [0, 2π), ∀m ∈ M = {1, 2, · · · , M}
denote the amplitude and phase shift coefficients of the m-th
element, respectively. Subject to the law of energy conserva-
tion, βr
    m + βt
         m = 1, ∀m ∈ M is satisfied2.
 2) The TS protocol: All elements of the STAR-RIS simul-
taneously complete the reflection/transmission of the signal in
different orthogonal time durations. Therefore, the reflection-
coefficient matrix and transmission-coefficient matrix are in-
dependent and given by ΘTS
                    r
                       = diag
                            �
                             ejθr
                               1, · · · , ejθr
                                      M �
                                          and

ΘTS
t = diag
     �
      ejθt
       1, · · · , ejθt
            M
            �
             , respectively, where θr
                        m, θt
                          m ∈
[0, 2π), ∀m ∈ M. Let λr, λt ∈ [0, 1] denote the time alloca-
tion for reflection and transmission, the constraint λr +λt = 1
holds for the whole communication period.

## B. Signal Transmission Model

In this paper, we consider a linear transmit precoding at the AP and assume that each IU $i$ and EU $j$ are assigned with one dedicated information/energy beam, which are denoted by $\mathbf{w}_{i}$, and $\mathbf{v}_{j}$, respectively. Consequently, the transmitted signal at the AP is written as

$$\mathbf{x}=\sum_{i\in\mathcal{K}_{\mathcal{I}}}\mathbf{w}_{i}x_{i}^{I}+\sum_{j\in\mathcal{K}_{\mathcal{E}}}\mathbf{v}_{j}x_{j}^{E},\tag{1}$$

where $x_{i}^{I}$ is the information-bearing signal for IU $i$, which is satisfied with $x_{i}^{I}\sim\mathcal{CN}(0,1)$, $\forall i\in\mathcal{K}_{\mathcal{I}}$, and $x_{j}^{E}$ is the energy-carrying signal for EU $j$ with $\mathbb{E}(|x_{j}^{E}|^{2})=1,\forall j\in\mathcal{K}_{\mathcal{E}}$. For simplification, we assume the information beam and energy beam are independent. Then we have

$$\mathbb{E}\{\mathbf{x}^{H}\mathbf{x}\}=\sum_{i\in\mathcal{K}_{\mathcal{I}}}\|\mathbf{w}_{i}\|^{2}+\sum_{j\in\mathcal{K}_{\mathcal{E}}}\|\mathbf{v}_{j}\|^{2}\leq P_{\max},\tag{2}$$
where Pmax is the power budget at the AP.

1In this paper, we consider the sub-6GHz frequencies and moderate size of AP and STAR-RIS arrays [24], [29]. Therefore, the simple far-field channel model is a safe approximation.

2In this paper, to determine the maximum performance gain, we investigate the beamforming design under the assumption of the phase shift coefficients for transmission and reflection can be adjusted independently. However, the proposed schemes can also be applied to the case where the phase shifts are coupled at the STAR-RIS with proper modifications [30].

1) ES: When the ES protocol is employed, the received signal at IU i is given by

$$y_{i}^{I}=\mathbf{h}_{i}^{H}\mathbf{\Theta}_{s_{i}}^{\text{ES}}\mathbf{G}\mathbf{x}+n_{i},\forall i\in\mathcal{K}\mathcal{I},\tag{3}$$
where si ∈ {t, r} indicates the region where IU i is located, and si = t if the user is located in T region, otherwise, si = r.

ni ∼ CN(0, σ2) denotes the additive white Guassion noise at IU i. Since the energy beam is a Gaussian pseudo-random sequence and carries no information, we assume it can be decoded by the receiving IU and removed from the received signal, as properly adopted in [31]. Therefore, the SINR of IU
i is given as

SINRi = | � uES si �H Hiwi|2 � k∈KI,k̸=i | � uES si �H Hiwk|2 + σ2 , (4)

where uES
       si
          = [
              �

βsi
 1 ejθ
    si
    1 , · · · ,
          �

                          βsi
                           Mejθ
                              si
                              M ]H, si ∈ {t, r},
Hi = diag(hi)G denotes as the cascaded channel from the
AP to IU i.

  On the other hand, due to the characteristics of energy
broadcasting, all information and energy beams are desirable
for each EU. At this point, the energy harvesting (EH) of EUs
is virtually unaffected by interference and noise [31]. Thus,
based on the linear EH model3 [15], [35], the received RF
energy/power4 at EU j is denoted as Pj, given by

,∀j ∈KE, Pj =η k∈KE i∈KI �� (5) �� � uES sj �H Gjvk ��2 � �� � uES sj �H Gjwi ��2+ �
where Gj = diag(gj)G denotes as the cascaded channel from the AP to EU j, sj ∈ {t, r} represents the located region for EU j. η ∈ (0, 1] represents the energy conversion efficiency for all EUs. For ease of analysis, we set η = 1 in the subsequent context.

2) TS: When the TS protocol is employed, the AP can communicate adaptively with users located in T and R regions in different time slots, so the interference among IUs from different regions can be ignored. For ease of identification and description, we re-denote ws i and vs j, s ∈ {t, r} as the beamforming for IU i and EU j, respectively. Note that wr i = 0 if IU i is located in the T region, and wt i = 0 if IU i is located in the R region. The same guidelines also apply to vs j for EU j. In this way, the SINR at IU i and the harvested power of EU j are rewritten as (6a) and (6b), respectively, which is shown at the top of the next page, where uTS
s = [ejθs
1, · · · , ejθs M ]H, s ∈ {t, r}.

3Although the non-linear EH model can capture the saturation effect more precisely for a single EH circuit [32], multi-parallel EH circuits effectively rectify the non-linear effect and cause a large linear conversion region [33]. Inspired by this, we adopt the linear EH model to investigate the fundamental design insights for STAR-RIS assisted SWIPT systems. Besides, by replacing the EH model with the non-linear model proposed in [19] and [34], our optimization framework is applicable, but some modifications still need to be investigated, which are our future focus topics.

4In this paper, we use the unit time of 1 second to measure system performance. Thus, the terms "power" and "energy" are interchangeable.

$$\text{SINR}_{i}^{s}=\frac{|\left(\mathbf{u}_{s}^{\text{TS}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{i}^{s}|^{2}}{\sum_{k\in\mathcal{K}_{\mathcal{I}},k\neq i}|\left(\mathbf{u}_{s}^{\text{TS}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{k}^{s}|^{2}+\sigma^{2}},\forall i\in\mathcal{K}_{\mathcal{I}},s\Rightarrow$$

$$P_{j}^{s}=\sum_{i\in\mathcal{K}_{\mathcal{I}}}\left|\left(\mathbf{u}_{s}^{\text{TS}}\right)^{H}\mathbf{G}_{j}\mathbf{w}_{i}^{s}\right|^{2}+\sum_{k\in\mathcal{K}_{\mathcal{E}}}\left|\left(\mathbf{u}_{s}^{\text{TS}}\right)^{H}\mathbf{G}_{j}\mathbf{v}_{k}^{s}\right|^{2},\forall j\in\mathcal{K}_{\mathcal{E}},s=$$
C. CSI Error Model Due to the passive property and channel complexity of the STAR-RIS, it is challenging to acquire the accurate CSI of the links associated with the STAR-RIS. To consider this effect on resource allocation design for the proposed system, we adopt a practical bounded CSI error model, where all possible channel errors are modeled by a bounded set [36], [37]5. To be more specific, we directly rewrite the cascaded channels from the AP to IUs/EUs via the STAR-RIS with the following models:

$$\mathbf{H}_{i}=\widehat{\mathbf{H}}_{i}+\triangle\mathbf{H}_{i},\forall i\in\mathcal{K}_{\mathcal{I}},\tag{7}$$ $$\mathcal{H}_{i}\triangleq\{\triangle\mathbf{H}_{i}\in\mathbb{C}^{M\times N}:\|\triangle\mathbf{H}_{i}\|_{F}\leq\varepsilon_{i}\},$$ (8) $$\mathbf{G}_{j}=\widehat{\mathbf{G}}_{j}+\triangle\mathbf{G}_{j},\forall j\in\mathcal{K}_{\mathcal{E}},$$ (9) $$\mathcal{G}_{j}\triangleq\{\triangle\mathbf{G}_{j}\in\mathbb{C}^{M\times N}:\|\triangle\mathbf{G}_{j}\|_{F}\leq\mu_{j}\},\tag{10}$$

where $\widehat{\mathbf{H}}_{i},\forall i\in\mathcal{K}_{\mathcal{I}}$ and $\widehat{\mathbf{G}}_{j},\forall j\in\mathcal{K}_{\mathcal{E}}$ are estimations of the corresponding channel $\mathbf{H}_{i}$ and $\mathbf{G}_{j}$, respectively[6]$\triangle\mathbf{H}_{i}$ and $\triangle\mathbf{G}_{j}$ denote the channel estimation errors. Sets $\mathcal{H}_{i}$ and $\mathcal{G}_{j}$ collect all possible channel estimation errors, $\varepsilon_{i}$ and $\mu_{j}$ denote the maximum threshold for the norms of the CSI estimation error vectors $\triangle\mathbf{H}_{i}$ and $\triangle\mathbf{G}_{j}$, respectively.

D. Problem Formulation In this paper, our goal is to simultaneously maximize the minimum data rate for IUs and harvested power for EUs to guarantee fairness among all users under imperfect CSI. For the conflict between two objectives, we apply a MOOP framework to elaborately design the robust resource allocation. More specifically, we consider the following MOOP formulations based on two different protocols for STAR-RIS operation, i.e., ES and TS.

1) MOOP Formulation for ES: To begin with, we only focus on maximizing the minimum harvested power among EUs, by jointly optimizing the active beamforming {wi}, {vj} and passive configuration {uES
s }. Under imperfect CSI, the robust design problem is formulated as

$$\max_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{E}}\}}\min_{j}\ P_{j}$$ s.t. $$\sum_{i\in\mathcal{K}_{\mathcal{I}}}\|\mathbf{w}_{i}\|^{2}+\sum_{j\in\mathcal{K}_{\mathcal{E}}}\|\mathbf{v}_{j}\|^{2}\leq P_{\max},\tag{11a}$$ $$\theta_{m}^{s}\in[0,2\pi),\forall m\in\mathcal{M},s\in\{t,r\},\tag{11b}$$ $\begin{cases}r,\text{if IU}i\text{located in R region,}\\ t,\text{if IU}i\text{located in T region.}\end{cases}$ (6a) $\begin{cases}r,\text{if EU}j\text{located in R region,}\\ t,\text{if EU}j\text{located in T region.}\end{cases}$ (6b) $\begin{cases}t,\text{if EU}j\text{located in T region.}\end{cases}$ (6c) $\begin{cases}\beta^{t}_{m},\beta^{r}_{m}\in[0,1],\ \beta^{t}_{m}+\beta^{r}_{m}=1,\forall m\in\mathcal{M}.\end{cases}$ (11c)
where constraint (11a) represents the total transmit power budget at the AP. (11b) and (11c) are the constraints on phase shift and amplitude for STAR-RIS elements, respectively. Next, with imposing the same constraints, the minimum data rate maximization problem for IUs is formulated as

$\max\limits_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{BS}}\}}\min\limits_{i}\log_{2}(1+\mathrm{SINR}_{i})$

s.t. (11a) - (11c). (12a)
Subsequently, the MOOP for ES based on problems (11) and (12) is formulated in the following:

* $\max\limits_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{BS}}\}}\min\limits_{j}\ P_{j}$
* $\max\limits_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{BS}}\}}\min\limits_{i}\ \log_{2}(1+\mathrm{SINR}_{i})$ (13a) s.t. (11a) - (11c). (13b)
2) MOOP Formulation for TS: Unlike in ES, where all users can access the entire communication time, TS introduces time allocation variables λr and λt for different regional users. The STAR-RIS will only provide services to users located in the corresponding region during the allocated time. Therefore, the MOOP framework for TS is formulated as

* $\max\limits_{\{\mathbf{w}_{i}^{s}\},\{\mathbf{v}_{j}^{s}\},\{\mathbf{u}_{i}^{s}\}}\min\limits_{i}\ \lambda_{s}P_{j}^{s}$
* $\max\limits_{\{\mathbf{w}_{i}^{s}\},\{\mathbf{v}_{j}^{s}\},\{\mathbf{u}_{i}^{s}\}}\min\limits_{j}\ \lambda_{s}\log_{2}(1+\text{SINR}_{i}^{s})$
* $\lambda_{r}\left(\sum\limits_{i\in\mathcal{K}_{\mathcal{I}}}\|\mathbf{w}_{i}^{r}\|^{2}+\sum\limits_{j\in\mathcal{K}_{\mathcal{E}}}\|\mathbf{v}_{j}^{r}\|^{2}\right)$ $$+\lambda_{t}\left(\sum\limits_{i\in\mathcal{K}_{\mathcal{I}}}\|\mathbf{w}_{i}^{t}\|^{2}+\sum\limits_{j\in\mathcal{K}_{\mathcal{E}}}\|\mathbf{v}_{j}^{t}\|^{2}\right)\leq P_{\max},$$ (14a) $$\theta_{m}^{s}\in[0,2\pi),\forall m\in\mathcal{M},s\in\{t,r\},$$ (14b) $$\lambda_{r},\lambda_{t}\in[0,1],\ \lambda_{r}+\lambda_{t}=1.$$ (14c)
Similar to problem (13), optimization objectives (Q3) and (Q4) denote the minimum harvested power and minimum data rate maximization, respectively. (14a) and (14b) are the constraints of the power budget at AP and the phase shift of the STAR- RIS, respectively. Besides, (14c) is a new constraint on time allocation introduced by the TS protocol.

Observe that both (13) and (14) are tricky problems that are challenging to solve directly. The main causes are as follows, briefly stated: 1) Since the two optimization objective functions of each problem are conflicting, there is no available resource allocation strategy to maximize the two goals simultaneously; 2) all optimization variables in the objective functions are closely coupled, which leads to the highly non-convexity for optimization problems; and 3) owing to the uncertainty of CSI, all objective functions have infinite possibilities, which are infeasible to handle in polynomial time. To sum up, the combination of the above factors makes it impossible to find an existing algorithm that can be directly applied to our formulated MOOPs. To circumvent this issue, we will explore efficient algorithms to solve the robust resource allocation problems (13) and (14) in the next.

## Iii. Solutions Of Robust Resource Allocation Problems In This Section, We First Propose An Ǫ-Constraint Based Ao Algorithm To Design The Joint Beamforming For Es. Then, The Algorithm Is Further Extended To Optimize The Time Allocation Policy And Beamforming Vectors With A Two-Layer Iterative Method For Ts.

A. Proposed Solution for ES
To start with, we investigate the robust resource allocation problem for ES by jointly optimizing the active beamforming
(i.e., {wi}and {vj}) at the AP and passive beamforming (i.e.,
{uES
s }) of the STAR-RIS. Inspired by the fact that the ǫ-
constraint method can generate the whole Pareto frontier of the two conflict objective values by setting different ǫ [40], we first adopt the ǫ-constraint method [41], which transforms
(Q2) into a constraint associated with ǫ and specifies (Q1) as the unique objective function. Accordingly, the original MOOP is reduced to the form of SOOP as follows:

$$\max_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{BS}}\}}\min\{P_{j}|j\in\mathcal{K}_{\mathcal{E}}\}$$ s.t. $$\log_{2}\left(1+\frac{|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{i}|^{2}}{\sum_{k\in\mathcal{K}_{\mathcal{I},k\neq i}}|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{k}|^{2}+\sigma^{2}}\right)\geq\epsilon,$$ $$\forall i\in\mathcal{K}_{\mathcal{I}},s_{i}\in\{t,r\},\tag{15a}$$ $$(11a)-(11c),\tag{15b}$$
where constraint (15a) indicates the minimum data rate requirements for IUs. It can be shown that the constraint will get equality at the optimal solution to problem (15). Otherwise, more communication resources can be shifted from IUs to EUs to improve the objective function while ensuring that (15a) holds. Therefore, different trade-offs between IUs and EUs will result from different ǫ values. By solving a series of SOOPs corresponding to the ergodic value of ǫ, the entire Pareto boundary of the trade-off region for original MOOP can be properly characterized.

However, the high coupling of variables and the infinite possibility of channel errors remain the main obstacles to solving SOOP (15). Let us define Wi ≜ wiwH
i , ∀i ∈ KI, Vj ≜ vjvH
j , ∀j ∈ KE as well as UES
s
≜ uES
s
�
uES
s
�H.

Then, by introducing an auxiliary variable η, which satisfies Pj ≥ η, ∀j ∈ KE, the considered problem (15) can be transformed into the following equivalent rank-constrained SDP:

$$\operatorname*{max}_{\{\mathbf{W}_{i}\},\{\mathbf{V}_{j}\},\{\mathbf{U}_{i}^{\mathrm{ess}}\},\eta}\eta$$ ≥ η, s.t. Tr GH j UES sj Gj � � k∈KE Vk �� � i∈KI Wi + � ∀j ∈ KE, ∀sj ∈ {t, r}, (16a) Tr     k∈KI,k̸=i Wk Γ − �  Wi  HH i UES si Hi  ≥ σ2, j∈KE Tr(Vj) ≤ Pmax, (16c) ∀i ∈ KI, ∀si ∈ {t, r}, (16b) � i∈KI Tr(Wi) + � Wi ⪰ 0, Rank(Wi) = 1, ∀i ∈ KI, (16d) Vj ⪰ 0, Rank(Vj) = 1, ∀j ∈ KE, (16e) UES s ⪰ 0, Rank � UES s � = 1, ∀s ∈ {t, r}, (16f) Diag � UES s � = βs, ∀s ∈ {t, r}, (16g) βt m, βr m ∈ [0, 1], βt m + βr m = 1, ∀m ∈ M, (16h)

where Γ = 2ǫ−1 denotes the minimum required SINR for IUs,
and βs ≜ [βs
          1, βs
             2, · · · , βs
                    M], ∀s ∈ {t, r} denotes the amplitude
adjustment vector. According to the identity Tr(AHBCD) =
vec(A)H(DT ⊗ B)vec(C), (16a) and (16b) can be further
expressed as

vec(Gj)H ⊗UES sj   �T k∈KE Vk i∈KI Wi + �  vec(Gj) ≥ η,  � � ∀j ∈ KE, ∀sj ∈ {t, r}, (17) T Wk vec(Hi)H     ⊗UES si k∈KI, k̸=i       vec(Hi) ≥ σ2,    Wi Γ − �    ∀i ∈ KI, ∀si ∈ {t, r}. (18)
Due to the uncertainty of Hi and Gj, there are an infinite number of such constraints (17) and (18) in problem (16). Next, we will draw on the following lemma to deal with this issue.

Lemma 1. (General S-Procedure [42]): Define the quadratic functions of the variable x ∈ CN×1:
fi(x) = xHAix + 2Re{xHbi} + ci, ∀i = 1, · · · , K,
⪰ 0.

−

�
 Ai
    bi
bH
 i
    ci

�

where $\mathbf{A}_{i}$ is the complex symmetric matrix, i.e., $\mathbf{A}_{i}=\mathbf{A}_{i}^{H}$. Then the $\{f_{i}(\mathbf{x})\geq0\}_{i=1}^{K}\Rightarrow f_{0}(\mathbf{x})\geq0$ holds if and only if there exists $\forall i,\lambda_{i}\geq0$ satisfying with

$$\begin{pmatrix}\mathbf{A}_{0}&\mathbf{b}_{0}\\ \mathbf{b}_{0}^{H}&c_{0}\end{pmatrix}-\sum_{i=1}^{K}\lambda_{i}\begin{pmatrix}\mathbf{A}_{i}&\mathbf{b}_{i}\\ \mathbf{b}_{i}^{H}&c_{i}\end{pmatrix}\succeq0.$$

�

$$\sum_{i=1}^{K}\lambda_{i}$$

  Next, we denote S1 =
                       ��
                          i∈KI Wi + �
                                       k∈KE Vk
                                                �T . With
Gj = �Gj + △Gj, (17) can be converted to the following
equivalent form:

$$\begin{array}{l}\mbox{vec}(\widehat{\mathbf{G}}_{j}+\triangle\mathbf{G}_{j})^{H}\left(\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\rm ES}\right)\mbox{vec}(\widehat{\mathbf{G}}_{j}+\triangle\mathbf{G}_{j})-\eta\\ =\mbox{vec}(\triangle\mathbf{G}_{j})^{H}\mbox{\bf Avec}(\triangle\mathbf{G}_{j})+2\mbox{\bf Re}\{\mbox{vec}(\triangle\mathbf{G}_{j})^{H}\mathbf{b}\}+c\geq0,\end{array}\tag{19}$$

where $\mathbf{A}=\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\rm ES}$, $\mathbf{b}=\mbox{\bf Avec}(\widehat{\mathbf{G}}_{j})$, $c=\mbox{vec}(\widehat{\mathbf{G}}_{j})^{H}\mathbf{b}-$
η. Besides, the following equation holds ∥△Gj∥F ≤ µj ⇒
∥vec(△Gj)∥2 ≤ µj. The uncertainty of CSI in (10) can be expressed as

$$-\text{vec}(\triangle\mathbf{G}_{j})^{H}\text{Ivec}(\triangle\mathbf{G}_{j})+\mu_{j}^{2}\geq0.\tag{20}$$

It is noted that by considering $\text{vec}(\triangle\mathbf{G}_{j})$ as the variable $\mathbf{x}$ in Lemma 1, (19) and (20) can be combined into a linear matrix inequality (LMI) as follows:

$$\left(\begin{array}{cc}\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\text{ES}}+\lambda_{1,j}\mathbf{I}&\left(\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\text{ES}}\right)\text{vec}(\widehat{\mathbf{G}}_{j})\\ \text{vec}(\widehat{\mathbf{G}}_{j})^{H}\left(\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\text{ES}}\right)&\alpha_{j}\end{array}\right)\succeq0,\tag{21}$$

where $\alpha_{j}=\text{vec}(\widehat{\mathbf{G}}_{j})^{H}\left(\mathbf{S}_{1}\otimes\mathbf{U}_{s_{j}}^{\text{ES}}\right)\text{vec}(\widehat{\mathbf{G}}_{j})-\eta-\lambda_{1,j}\mu_{j}$, $\{\lambda_{1,j}\geq0\}_{j=1}^{\kappa_{\varepsilon}}$ are the auxiliary variables.

Similarly, by denoting $\mathbf{S}_{2,j}=\frac{\mathbf{W}_{j}}{\mathbf{W}_{j}}-\sum_{k\in\kappa_{\varepsilon}}\mathbf{W}_{k}$, (18) is 
{λ1,j ≥ 0}KE
j=1 are the auxiliary variables.

Similarly, by denoting S2,i = Wi

converted into a LMI form:

$$\begin{pmatrix}\mathbf{S}_{2,i}\otimes\mathbf{U}_{s_{i}}^{\text{ES}}+\lambda_{2,i}\mathbf{I}&\left(\mathbf{S}_{2,i}\otimes\mathbf{U}_{s_{i}}^{\text{ES}}\right)\text{vec}(\widehat{\mathbf{H}}_{i})\\ \text{vec}(\widehat{\mathbf{H}}_{i})^{H}\left(\mathbf{S}_{2,i}\otimes\mathbf{U}_{s_{i}}^{\text{ES}}\right)&\varrho_{i}\end{pmatrix}\succeq0,\tag{22}$$

where $\varrho_{i}=\text{vec}(\widehat{\mathbf{H}}_{i})^{H}\left(\mathbf{S}_{2,i}\otimes\mathbf{U}_{s_{i}}^{\text{ES}}\right)\text{vec}(\widehat{\mathbf{H}}_{i})-\sigma^{2}-\lambda_{2,i}\varepsilon_{i}$ and $\left\{\lambda_{2,i}\geq0\right\}_{i=1}^{\mathcal{K}_{x}}$ are the auxiliary variables. Through these transformations above, problem (16) is recasted as

$$\max_{\{\lambda_{1,j}\},\{\lambda_{2,i}\},\{\mathbf{W}_{i}\},\{\mathbf{V}_{j}\},\{\mathbf{U}_{s}^{\text{ES}}\},\eta}\eta$$ s.t. $$(21),(22),(16c)-(16h).\tag{23a}$$
However, the optimization variables are still coupled in (21)
and (22), and it is challenging to optimize them simultaneously. To solve this issue, the AO method is applied to decompose problem (23) into two subproblems, i.e., active beamforming design and passive beamforming design, which can be alternatively optimized.

1) Active Beamforming Design: Here, we exclusively concentrate on active beamforming design. For given {UES
s }, original problem (23) is simplified to

$\{\lambda_{1,j}\},\{\lambda_{2,i}\},\{\Psi_{i}\},\{\Psi_{j}\},\eta$

s.t. (21), (22), (16c) - (16e). (24a)
As can be observed, the non-convexity of rank-one constraints
(16d) and (16e) restricts the solution of the new problem (24). To handle it, we employ semi-definite relaxation (SDR) and ignore the constraints (16d) and (16e) directly according to the following theorem.

Proof. Please refer to the Appendix.

Theorem 1. The optimal solutions for the relaxed version
of problem (24), i.e., without considering rank-one con-
straints, always satisfy Rank (W∗
                           i )
                               =
                                  1, ∀i ∈
                                          KI and
�
  j∈KE Rank
           �
            V∗
             j
              �
                ≤ 1 for feasible Pmax > 0 and ǫ > 0.

  As a result, the relaxed problem (24) is a standard SDP, and
can be efficiently solved via existing convex solvers such as
CVX [43].

2) Passive Beamforming Design: In this subproblem, we optimize the passive beamforming with fixed {Wi} and {Vj}.

This subproblem is reduced to

$\begin{array}{c}\max\\ \{\lambda_{1,i}\},\{\lambda_{2,i}\},\{\mathbf{U}_{s}^{\rm ES}\},\eta\\ \mbox{s.t.}\ \ (21),(22),(16\mbox{f})-(16\mbox{h}).\end{array}$ (25a)
Note that the difficulty in the design of STAR-RIS coefficients stems from the rank-one constraint (16f). Different from the relaxation of problem (24), we first rewrite this constraint as an equivalent form [44]:

$$\text{Rank}(\mathbf{U}_{s}^{\text{ES}})=1\Leftrightarrow\|\mathbf{U}_{s}^{\text{ES}}\|_{*}-\|\mathbf{U}_{s}^{\text{ES}}\|_{2}=0,\forall s\in\{t,r\},\tag{26}$$
where ∥UES
s ∥∗ = �

where $||\mathbf{U}_{s}^{\mathrm{ES}}||_{*}=\sum_{i}\sigma_{i}(\mathbf{U}_{s}^{\mathrm{ES}})$ and $||\mathbf{U}_{s}^{\mathrm{ES}}||_{2}=\sigma_{1}(\mathbf{U}_{s}^{\mathrm{ES}})$ denote the nuclear norm and spectral norm of $\mathbf{U}_{s}^{\mathrm{ES}}$, respectively, and $\sigma_{i}$ is the $i$-th largest singular value of $\mathbf{U}_{s}^{\mathrm{ES}}$. Then, the penalty method [45] is leveraged, where we convert the constraint (16f) into a non-negative penalty function term appended to the objective function as follows:

$$\max_{\{\lambda_{1,j}\},\{\lambda_{2,i}\},\{\mathbf{U}_{s}^{\mathrm{ES}}\},\eta}\eta-\xi\sum_{s\in\{t,r\}}\left(\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{*}-\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{2}\right)$$ s.t. $$(21),(22),(16g),(16h),\tag{27a}$$
where ξ > 0 is the penalty factor. Driven by the optimization goal, the value of the penalty term will decrease with the increase of ξ, and when ξ → +∞, the penalty term gradually converges to 0. At this point, the optimal solution UES
s of problem (27) always satisfies the equality constraint (16f).

However, it should be noted that the initial value of ξ has a significant impact on the effect of the algorithm. At the start of the iteration, if ξ is too large, the focus of optimization will shift from the original function η to the penalty item, which violates our intention. Hence, we need to initialize ξ
with a small value, and then gradually increase it until the convergence criterion of the rank-one constraint is met:

$$\max\{\|{\bf U}_{s}^{\rm ES}\|_{*}-\|{\bf U}_{s}^{\rm ES}\|_{2},s\in\{t,r\}\}\leq\epsilon_{1},\tag{28}$$
where ǫ1 is a predefined maximum violation of the equality constraint.

Nevertheless, the non-convexity of the penalty term makes the reformulated problem (27) still difficult to solve. Inspired by the successive convex approximation (SCA) technique, we approximate the penalty term by its first-order Taylor expansion to obtain the convex upper bound as (29), which is shown at the top of the next page, where ϕ
�
UES(l)
s
�
denotes

the eigenvector related to the largest eigenvalue of $\mathbf{U}_{s}^{\mathrm{ES}(l)}$. Next, by replacing the penalty term with its convex upper bound according to the given point $\{\mathbf{U}_{s}^{\mathrm{ES}(l)}\}$, problem (27) is approximated into the following optimization problem:

$$\max_{\{\lambda_{1,j}\},\{\lambda_{2,i}\},\{\mathbf{U}_{s}^{\mathrm{ES}}\},\eta}\eta-\xi\sum_{s\in\{t,r\}}\left(\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{*}-\overline{\mathbf{U}}^{\mathrm{ES}(l)}\right)$$ s.t. $$(21),(22),(16g),(16h).\tag{30a}$$
Now, problem (30) is a SDP and can be solved by the CVX. Based on this, solving the problem (30) repeatedly by

$$\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{*}\!-\!\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{2}\leq\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{*}\!-\!\left\{\|\mathbf{U}_{s}^{\mathrm{ES}(l)}\|_{2}+\mathrm{Tr}\!\left[\varphi\left(\mathbf{U}_{s}^{\mathrm{ES}(l)}\right)\varphi\left(\mathbf{U}_{s}^{\mathrm{ES}(l)}\right)^{H}\!\left(\mathbf{U}_{s}^{\mathrm{ES}}\!-\!\mathbf{U}_{s}^{\mathrm{ES}(l)}\right)\right]\right\}$$ $$\triangleq\|\mathbf{U}_{s}^{\mathrm{ES}}\|_{*}-\overline{\mathbf{U}_{s}^{\mathrm{ES}(l)}},$$

## Algorithm 1 Penalty-Based Algorithm For Solving Problem (30)

1: Initialize the feasible UES(0)
s
, penalty factor ξ and given
{Wi, Vj}, set the allowable ǫ1, ǫ2, and the maximum
number of iterations Lmax.
2: repeat
3:
Set iteration index l = 0;
4:
repeat
5:
For given {UES(l)
s
}, solve the problem (30);
6:
Update {UES(l+1)
s
} with the obtained optimal solutions, l = l + 1;
7:
until the iterative gain of the objective function value
is below a predefined threshold ǫ2 > 0 or l = Lmax.
8:
Update
{UES(0)
s
}
with
the
optimized
solutions
{UES(l)
s
}.
9:
Update ξ = τξ.
10: until the constraint violation is below a predefined threshold ǫ1 > 0.
exploiting SCA and updating the penalty factor with ξ = τξ
until (28) is satisfied, we can obtain the optimal passive beamforming in each AO iteration. And the penalty-based algorithm is summarized in Algorithm 1.

To this end, the original problem (23) with highly coupled variables was decomposed into two subproblems, i.e., problems (24) and (30), which are solved in an iterative manner, according to the AO method. Wherein, the non-convexity for active beamforming design is relaxed according to Theorem
1, while the rank-one constraint in STAR-RIS beamforming is solved by employing penalty-based Algorithm 1. On the one hand, the objective function of problem (30) will gradually converge with the increase of the penalty factor in each passive beamforming design [44]. On the other hand, the AO iteration algorithm is guaranteed to converge, and the relevant proofs can be found in the literature [17]. Therefore, our proposed algorithm for problem (23) will eventually converge to a stationary point. The specific details of the developed algorithm are presented in Algorithm 2.

In addition, there is a straightforward observation that the obtained solution to problem (23) is generally sensitive to the value of ǫ. In order to ensure the feasibility of problem (23), the value of ǫ should be in a reasonable range [0, Rmax]. Rmax is the maximum achievable data rate for this system, and might be attained by resolving the subsequent optimization problem:

$$\max_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{ES}}\},\gamma}\gamma$$ s.t. $$\frac{|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{i}|^{2}}{\sum_{k\in\mathcal{K}_{\mathcal{I}},k\neq i}|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{k}|^{2}+\sigma^{2}}\geq\gamma,$$ $$\forall i\in\mathcal{K}_{\mathcal{I}},s_{i}\in\{t,r\},\tag{31a}$$ $$(11\mathrm{a})-(11\mathrm{c}).\tag{31b}$$

## Algorithm 2 Ao Algorithm For Solving Problem (23)

1: Determine the value of ǫ and initialize feasible point
{UES(0)
s
} with random matrix and the iteration index
k = 0, set the allowable ε0, the maximum number of
iterations Kmax.
2: repeat
3:
For given {UES(k)
s
}, solve the problem (24) to obtain
the optimized {W(k)
i
, V(k)
j
};
4:
Update {UES(k+1)
s
} via solving the problem (30) by
applying Algorithm 1;
5:
Update k = k + 1;
6: until the iterative gain of the objective function value of
problem (23) is below a predefined threshold ε0 > 0 or
k = Kmax.
where $\gamma$ is an introduced auxiliary variable with $\gamma\geq0$. Next, in order to simplify the fractional constraint (31a), we construct the following function:

$$f(\gamma)\!=\!|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\!\mathbf{H}_{i}\mathbf{w}_{i}|^{2}\!-\!\gamma\left(\sum_{k\in\mathcal{K}_{\mathcal{I},k}\neq i}|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\!\mathbf{H}_{i}\mathbf{w}_{k}|^{2}\!+\!\sigma^{2}\right).\tag{32}$$
As can be seen, this function is monotonically decreasing with respect to γ when holding other variables constant. Hence, we can turn the goal of maximizing γ into finding the maximum value of the function f(γ) and use the bisection method to find the optimal γ. When the optimized maximum value of f(γ) > 0, we can further increase the value of γ while ensuring that the original problem is feasible. On the contrary, if the optimized maximum value of f(γ) < 0, we can only make the original problem feasible by reducing the value of
γ. Thus, only the γ that makes the optimized maximum value of f(γ) = 0 is the optimal solution for the original problem. Considering that the non-smoothness of f(γ) is difficult to handle, we introduce a new auxiliary variable t0 and yield a new optimization problem:

$$\max_{\{\mathbf{w}_{i}\},\{\mathbf{v}_{j}\},\{\mathbf{u}_{s}^{\mathrm{ES}}\},t_{0}}t_{0}$$ s.t. $$|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{i}|^{2}\neg\gamma\left(\sum_{k\in\mathcal{K}_{\mathcal{I}},k\neq i}|\left(\mathbf{u}_{s_{i}}^{\mathrm{ES}}\right)^{H}\mathbf{H}_{i}\mathbf{w}_{k}|^{2}+\sigma^{2}\right)\geq t_{0},$$ $$\forall i\in\mathcal{K}_{\mathcal{I}},s_{i}\in\{t,r\},\tag{33a}$$ $$(11\mathbf{a})-(11\mathbf{c}).\tag{33b}$$
In fact, given γ, problem (33) can also be solved directly by applying Algorithm 2. Along this line, we can update the search range [γmin, γmax] in the n-th iteration and determine
γn+1 =
γmax+γmin
2
for the next search. According to the bisection criterion, the value of γ will eventually converge

## Algorithm 3 Ǫ-Constraint Method Solving Moop (13)

1: Solve problem (31) by applying bisection search method
and Algorithm 2 to get the Rmax, initialize the factor
δ = 0 and step △δ.
2: repeat
3:
Update the ǫ with ǫ = δRmax;
4:
Given ǫ, reformulate MOOP (13) into a tractable SOOP
(23) via exploiting ǫ-constraint method and S-procedure;
5:
Solve problem (23) by applying Algorithm 2 to obtain
the optimized η corresponding to given ǫ;
6:
Update δ = δ + △δ ;
7: until δ > 1.
when the following inequality is satisfied:

$\left|\gamma_{n}-\gamma_{n+1}\right|\leq\varepsilon_{2}$, (34)
where ε2 is a predefined threshold. After solving the above, we determine the maximum feasible value of ǫ, i.e., Rmax =
log2 (1 + γ∗), for problem (23). Until here, the overall algorithm for the original MOOP (13) can be completely outlined in Algorithm 3.

## B. Proposed Solution For Ts

  In this subsection, Algorithm 2 is extended to solve MOOP
(14) for TS. Similar to ES, we aim to maximize the minimum
harvested power by EUs, subject to the minimum achievable
data rate constraint in the reformulated SOOP. The difference
is that new variables λt and λr for the time allocation need
to be optimized. Let Ws
                          i ≜ ws
                                 i (ws
                                     i )H, Vs
                                             j ≜ vs
                                                    j(vs
                                                        j)H and
UTS
  s ≜ uTS
         s
            �
             uTS
               s
                 �H. By applying the ǫ-constraint method and
Lemma 1, MOOP (14) is transformed into a SOOP as

     max
{Ws
  i },{Vs
     j},{UTS
         s },{λs},η η

≥ η, s.t. λsTr GH j UTS s Gj � � k∈KE Vs k i∈KI Ws i + � �� � ∀j ∈ KE, ∀s ∈ {t, r}, (35a) Tr     2 ǫ k∈KI,k̸=i Ws k λs − 1 − �   Ws i  HH i UTS s Hi  ≥ σ2, ∀i ∈ KI, ∀s ∈ {t, r}, (35b) j∈KE Vt j) ≤ PA, λr( � i∈KI Wr i + � j∈KE Vr j) + λt( � i∈KI Wt i+ � (35c)

Ws
 i ⪰ 0, Rank(Ws
      i ) = 1, ∀i ∈ KI, ∀s ∈ {t, r},
                 (35d)

Vs
j ⪰ 0, Rank(Vs
        j) = 1, ∀j ∈ KE, ∀s ∈ {t, r},
                       (35e)

UTS
s ⪰ 0, Rank
       �
        UTS
         s
          �
           = 1, ∀s ∈ {t, r},
                       (35f)

λr, λt ∈ [0, 1], λr + λt = 1.
                                   (35h)

$\mathbf{U}_{s}^{\text{TS}}=\mathbf{\Gamma}^{M\times M},\forall s\in\{t,r\},$ (35g) $\lambda_{r},\lambda_{t}\in[0,1],\lambda_{r}+\lambda_{t}=1.$ (35h)

It is intuitive to see that problem (35) for given {λt, λr} can
be considered as a simpler form of problem (16) without
amplitude adjustment constraint, which can be solved by
resorting to Algorithm 2. Therefore, the main difficulty in
solving problem (35) falls in the determination of the optimal

time allocation policy. To overcome this issue, a two-layer algorithm is proposed. In the outer layer, the one-dimensional search is used to obtain the optimal time allocation {λ∗
t , λ∗
r}.

While the remaining variables can be optimized by the innerlayer iteration with fixed {λ∗
t , λ∗
r}.

Likewise, in order to ensure the feasibility of the problem
(35), we explore the maximum value of ǫ allowed for TS
by invoking the similar method for ES. Specially, we first introduce a new variable γ0 that satisfies λs log2(1+SINRs i) ≥
γ0, s ∈ {t, r} and build a new function as (36), which is shown at the top of the next page. Then, a new optimization problem with introducing auxiliary variable T0 is formulated as

$\max\limits_{\{\mathbf{w}_{i}^{s}\},\{\mathbf{v}_{j}^{s}\},\{\mathbf{u}_{s}^{\mathrm{TS}}\},T_{0}}T_{0}$

s.t. $f(\gamma_{0})\geq T_{0},\forall i\in\mathcal{K}_{\mathcal{I}},n\in\{t,r\}$. (37a)

(14a) - (14c). (37b)
It is obvious that the problem (37) can be solved similarly to how the problem (35) was previously presented. Accordingly, we can update the value of γ0 with bisection criteria until (34)
is satisfied. As a result, by traversing the value of ǫ in this determined feasible region and solving the related SOOP, we can get a proper rate-energy trade-off region for TS. Since it is similar to Algorithm 3, the specific details of the algorithm proposed for TS are omitted here.

## C. Computational Complexity And Convergence Analysis

The computational complexity of the proposed algorithms is analyzed in the following. Since Algorithm 3 for obtaining the entire rate-energy region can be seen as multiple iterations of Algorithm 2 with different ǫ, its computational complexity is (Iǫ + Ib) times that of Algorithm 2, where Iǫ and Ib denote the ergodic number of the ǫ-constraint method and the number of bisection search for obtaining Rmax, respectively.

Thus, the computational complexity of Algorithm 2 becomes the focus of attention. Note that the transformed subproblems are both standard SDP problems. According to [46], the approximate computational complexity of (24) and (30)
is given by OA = O
�
(KE + KI)(M 3.5N 3.5 + N 3.5)
�
and OP = O
�
(KE + KI)(M 3.5N 3.5) + 2M 3.5)
�
, respectively.

Let IES
A
and IES
P
denote the iteration numbers of the AO
and penalty method, respectively. The overall complexity for Algorithm 2 is O
�
IES
A (OA + IES
P OP )
�
.

Based on this, the complexity of the proposed algorithm for ES is measured as OES = (Iǫ + Ib) O
�
IES
A
�
OA + IES
P OP
��
.

While for TS, one-dimensional search is used to find the optimal solution for time allocation. Let L denote the search times, and then the complexity of the proposed algorithm for TS
is measured as OTS = L (Iǫ + Ib) O
�
ITS
A
�
OA + ITS
P OP
��
, where ITS
A and ITS
P
denote the iteration numbers of the AO
and penalty method for TS, respectively. It can be seen that the complexity of the proposed TS algorithm is higher than that of ES due to the addition of one-dimensional search.

Note that the convergence of ǫ-constraint method, AO, SCA, and penalty method has been proved in [40], [43], [45]. Based on this, with predetermined convergence criterion, the proposed algorithm for ES will eventually converge a station-

γ0 λs −1 �  f(γ0)=| � uTS s �HHiws i |2− � 2 k∈KI,k̸=i | � uTS s �HHiws k|2+ σ2  �
ary point via many iterations. Additionally, one-dimensional search is also a method that guarantees convergence. Thus, the proposed algorithm for TS is also capable of reaching convergence.

## Iv. Numerical Results

Based on various operating protocols, numerical results obtained from different perspectives are presented to demonstrate the efficacy of the STAR-RIS on SWIPT systems.

## A. Simulation Setup

First we introduce the three-dimensional coordinate setup considered in our simulation. As shown in Fig. 2, the AP is located at $(0,0,0)$ meters, and the STAR-RIS with elements configured in a uniform planar array (UPA) is deployed at the user hotspot with coordinates $(15,0,0)$ meters. The EUs and IUs are randomly distributed in circle and ring-shaped areas centered at the STAR-RIS with a radius of $r_{E}=1$ and $r_{I}\in(1,6)$ m, respectively. For ease of illustration, we analyze a basic scenario where each side of the STAR-RIS is distributed with only one IU and one EU. In this paper, all channels are modeled as Rician fading channels as follows:

$$\mathbf{G}=\sqrt{\rho_{AS}}(d)\left(\sqrt{\frac{K_{AS}}{K_{AR}+1}}\mathbf{G}^{\mathrm{LoS}}+\sqrt{\frac{K_{AS}}{K_{AS}+1}}\mathbf{G}^{\mathrm{NLos}}\right),\tag{38a}$$ $$\mathbf{v}_{k}=\sqrt{\rho_{SU}}(d)\left(\sqrt{\frac{K_{SU}}{K_{SU}+1}}\mathbf{v}_{k}^{\mathrm{Los}}+\sqrt{\frac{K_{SU}}{K_{SU}+1}}\mathbf{v}_{k}^{\mathrm{NLos}}\right),$$ $$\mathbf{v}\in\{\mathbf{h},\mathbf{g}\}.\tag{38b}$$
where ρAS(d) =
ρ0

d
 αAS
 AS , ρSU(d) =
                  ρ0

                                  d
                                   αSU
                                   SU , and ρ0 represents the
path loss at reference 1 m, dAS and dSU,k denote the distance
from the AP to the STAR-RIS and from the STAR-RIS to the
k-th user, respectively, αAS and αSU denote the corresponding
path loss exponents. In addition, KAS and KSU are the
Rician factors, and GLoS and vLoS
                                 k
                                      are the corresponding
deterministic LoS components, while GNLoS and vNLoS
                                                    k
                                                         are
the corresponding deterministic NLoS components, which are

$$\left(\begin{array}{c}\Psi\in\mathcal{K}_{\mathcal{I}},s\in\{t,r\}.\end{array}\right.\tag{36}$$
modeled as random Rayleigh fading components. In addition, the normalized maximum channel estimation errors of IU i and EU j are set to be ρH =
εi
∥ �
Hi∥ and ρG =
µj
∥ �
Gj∥, respectively.

The specific system parameters are presented in Table I [12], [21].

To demonstrate the performance improvements introduced by deploying the STAR-RIS in a SWIPT system, two baselines are considered for comparison. 1) Baseline scheme 1 (also referred to as reflecting-only RIS): In this case, a reflectingonly RIS is deployed at the (15, 6, 0) meters to facilitate communication for all EUs and IUs via the passive reflective beamforming. 2) Baseline scheme 2 (also referred to as conventional RIS): In this case, a reflecting-only RIS and a transmitting-only RIS are deployed adjacent to each other for communication. For fairness in comparison, each conventional RIS consists of M/2 elements, and the coefficient matrices are regarded as βt = [11×M/2, 01×M/2]T for transmittingonly RIS and βr = [01×M/2, 11×M/2]T for reflecting-only RIS. It is worth noting that the resulting optimization problems for baseline schemes can also be solved directly by applying Algorithm 2. It is important to emphasize that the following results shown (i.e., Figs. 3-9) are obtained by averaging over 50 channel realizations unless otherwise specified. B. Convergence of Algorithm 2
In Fig. 3, we show the convergence behavior of the proposed Algorithm 2 for STAR-RIS ES and reflecting-only RIS with different STAR-RIS elements M. Specially, we set N = 4,
ρH = ρG = 0.01 and ǫ = 0. The results obtained for one random channel realization depict that the max-min harvested power of EUs increases quickly as the number of iterations increases, and finally converges to a value within 6 iterations for M = 8 and M = 16. Even when M = 32, our proposed algorithm can achieve convergence at the 8-th iteration.

However, compared to the reflecting-only RIS, the proposed

Carrier frequency
750MHz
Bandwidth
1MHz
Path loss at the reference distance of 1 meter
ρ0 = −30dB
Rician factor of the RIS assisted channels
KAS = KSU = 3dB
Path-loss exponents of the RIS assisted channels
αAS = αSU = 2.2
Maximum power budget
Pmax = 10 W
Noise power at receivers
σ2 = −90 dBm
Initialized penalty factor for Algorithms 2
ξ = 10−4
Maximum number of iterations for Algorithm 1 and 2
Lmax = 30, Kmax = 20
Convergence accuracy
ε0 = ǫ1 = ε2 = 10−3, ǫ2 = 10−7
Search step size st for ǫ-constraint method
△δ = 0.1

algorithm for the STAR-RIS converges more slowly. This is expected since the computational complexity increases with more variables to be optimized for the STAR-RIS with largerscale elements.

## C. System Performance Versus Number Of Ap Antennas

In Fig. 4(a), we examine the achievable rate-energy region in relation to the number of AP antennas. We set M = 8, and
ρG = ρH = 0.01. The results depict that the rate-energy region for all schemes expands with the number of antennas due to the active beamforming gain. In addition, regions obtained by the proposed scheme are larger than those obtained with reflecting-only RISs and conventional RISs because the former can take advantage of more DoFs. Further, regarding the performance for two protocols of STAR-RISs, ES is able to achieve both higher upper boundaries, i.e., Rmax and Emax, for IUs and EUs, respectively. However, TS can ensure better a performance balance for all users. This can be explained as follows. Compared to TS, ES accommodates all users to utilize the entire time resource for communication or charging, thus enabling a better upper bound on data rate/harvested power when only focusing on IUs or EUs. However, the time allocation for TS allows the AP and the STAR-RIS to serve users in only one region during each allocated time period, which reduces competition for communication resources between IUs and EUs as well as interference among IUs. As a result, the decline of harvested power is more moderate as the data rate increases, leading to a better balance between IUs and EUs.

In Fig. 4(b), we further explore the max-min harvested power for EUs versus the number of AP antennas. We set the max-min data rate of IUs to be Rmin = 4 bit/s/hz, M = 16, and ρG = ρH = ρ = 0.01. As depicted in Fig. 4(b), the maxmin harvested power for all schemes increases with the number of AP antennas, and STAR-RISs outperform reflecting-RISs and conventional RISs. This is expected because, compared with reflecting-RIS, although adopting STAR-RIS leads to energy leakage or time loss for each user, the flexible deployment of STAR-RIS can provide better channel conditions, which can make up for the loss of communication resources. More importantly, the enhanced DoFs exploited by STAR-RISs can further boost desired signals and suppress unwanted ones, thereby achieving a significant performance improvement.

## D. System Performance Versus Number Of Star-Ris Elements

Fig. 5(a) shows the achievable rate-energy region versus the number of STAR-RIS elements. We set N = 4, and
ρG = ρH = 0.01. Firstly, it is seen that the rate-energy region grows for all schemes as M increases, and the performance gap between the proposed design and the baseline schemes becomes more pronounced. This is because more elements lead to higher transmission/reflection beamforming gains and DoFs benefits. Secondly, the power gain for EUs is more significant than the rate gain for IUs. This can be explained by citing the following causes. The calculation of the information rate requires a logarithmic operation, which weakens the gain brought by RISs to received SINR. Whereas, the calculation of harvested power does not involve logarithmic operations, thus resulting in the differences in growth rates. Similar reasons can be used to explain the higher performance gains for EUs than IUs via the introduction of STAR-RISs.

In Fig. 5(b), we further investigate the max-min harvested power for EUs versus the number of STAR-RIS elements under the max-min data rate Rmin = 4 bit/s/hz. We set N = 4, and ρG = ρH = 0.01. As can be observed, the max-min harvested power for all schemes increases with the STAR-RIS elements. Particularly, STAR-RISs rise noticeably faster than reflecting-RISs and conventional RISs. This is because the extra DoFs for STAR-RISs can extend the passive beamforming gains by more elements. Besides, the gap between TS and ES
increases as M increases. This is made possible by the fact that interference-free communication for TS can make up for the inefficient use of the communication time when the M is large.

## E. System Performance Versus Csi Uncertainty Levels

In Fig. 6(a), we study the achievable rate-energy region versus the cascaded channel uncertainty levels. We set M = 16, N = 4, and ρG = ρH = ρ for the system. Simulation results depict that the performance region for all schemes decreases as ρ increases, and the performance decline of our proposed scheme is more pronounced than the baseline schemes employing reflecting-only RISs and conventional RISs. This can be understood by pointing out that increasing design DoFs leads to a larger channel estimation error and reduces the robustness of user performance. In particular, the channel error has a greater impact on the IUs than the EUs for STAR-RISs working in ES mode and conventional RISs. This is because, the uncertainty of the channel can not only diminish the desired signal received by IUs like EUs, but also enhance the interference from other IUs. However, TS is able to minimize the interference between IUs, which leads to more robustness for IUs under imperfect CSI.

Fig. 6(b) further investigates the max-min harvested power versus the cascaded channel uncertainty levels under the maxmin data rate Rmin = 4 bit/s/hz. We set M = 16, N = 4, affect IUs more than EUs, and as ρ increases to also satisfy Rmin = 4 bit/s/hz, more communication resources need to be allocated to IUs, thus significantly weakening the performance of EUs. While TS can effectively eliminate interference with IUs, which results in more robustness. On the other hand, the

## F. Rate-Energy Region Versus Star-Ris Deployment Strategies

In Fig. 7, we investigate the impact of STAR-RISs deployment strategies on achievable rate-energy region. In addition to the deployment strategy of the basic scenario described above, here we consider a special deployment strategy of STAR-RISs that makes all IUs and EUs located in the T and R regions, respectively. For fairness of comparison, we set M = 16, N = 4 and ρG = ρH = 0.01. As can be seen, the special deployment strategy outperforms basic deployment strategy for all schemes. Following are some explanations for the causes of this. Considering the STAR-RISs ES protocol and conventional RISs, the phase shift design of RISs for the basic deployment strategy needs to balance the requirements of both IU and EU in the same region, but also to suppress the interference from IU located in another region, which cuts the passive beamforming gains. But the special deployment strategy only considers competition between users located in the same region for resource allocation, which reduces the energy leakage for each IU or EU and enhances resource dedication. While for the STAR-RISs TS protocol, more time resources can be allocated for all IUs and EUs by employing the special deployment strategy, which further compensates for the lack of time available in the basic deployment strategy. Therefore, the special deployment strategy results in a better rate-energy region. However, the stringent requirements for user distribution entail higher implementation difficulties, especially as the number of users grows.

In Fig. 8, we study the achievable rate-energy region versus different filters at the HAP. Here, the zero-forcing (ZF) beamforming scheme is introduced as a comparison for our proposed beamforming scheme under both the ES and TS
protocols. In the basic scenario, we set N = 4, M = 16, and
ρG = ρH = 0.01. The Fig. 8 depicts that our proposed scheme outperforms the ZF beamforming scheme for both ES and TS. Moreover, the performance improvement for EUs is greater than that for IUs. The reasons can be explained as follows. When the number of antennas is sufficient, ZF beamforming can fully suppress the interference between users. However, due to stringent interference elimination requirements, ZF beamforming also inevitably reduces the flexibility of communication resource allocation, which results in poorer performance gains for IUs than our proposed beamforming scheme. While for EUs, unlike ZF's obsession with eliminating all interference, our proposed scheme fully exploits the potential of constructive interference and suppresses destructive interference for each EU. As a result, our scheme achieve a more significant performance gain in EUs than ZF beamforming. On the other hand, since the TS protocol has effectively attenuated inter-user interference, there is a smaller performance gap between our proposed scheme and ZF beamforming compared to ES.

## H. Rate-Energy Region Versus Number Of Users

Fig. 9 characterizes the achievable rate-energy region versus the number of users. Compared to the basic setup, two new scenarios are considered with 4 EUs, 2 IUs and 2 IUs, 4
EUs, respectively, where we set M
= 16, N = 4 and
ρG = ρH = 0.01. For ease of exploration, we assume all IUs and EUs are uniformly located in the T and R regions. As clearly shown in Fig. 9, as the number of users increases, the obtained rate-energy region becomes smaller. This is a result of that when a new user accesses the system, in order to ensure fairness among users, the communication resources allocated to each user will decrease. Especially, increasing the number of IUs, the system performance degrades more significantly, as expected. This is because IUs are not only limited by their individual QoS requirements, but can also cause significant inter-user interference to other IUs. This fact also leads to TS
outperforming ES when the number of IUs is large. Because TS provides a good suppression on the inter-user interference, which can impair the impact of lost time resources and thus contribute to achieving higher performance gains.

## V. Conclusions

In this paper, the robust resource allocation design for STAR-RIS enabled SWIPT systems was investigated. Based on the assumption of imperfect CSI, two MOOP frameworks for different operating protocols were deployed to study the fundamental trade-off between the max-min data rate and harvested power. For each protocol, the MOOP was first converted into a SOOP by applying the ǫ-constraint method, and then an AO-based algorithm was proposed to explore the robust resource allocation design. Numerical results unveiled that STAR-RISs can greatly outperform conventional reflectingonly RISs in terms of system performance, especially for EUs. Also, the ES and TS protocols of STAR-RISs can enhance the SWIPT system from different perspectives. Imagine that, combined with implementation difficulties, these insights will offer helpful suggestions for the resource allocation design of STAR-RIS aided SWIPT systems in practical scenarios.

## Appendix A: Proof Of Theorem 1

The relaxed problem in (23) is jointly convex with respect to the optimization variables {Wi, Vj} and satisfies Slater's constraint qualification [47]. Therefore, strong duality of holds. Here, we take the Lagrangian function of (23) into consideration as (39), which is shown at the top of the next page, where we denote C1,j and C2,i as the abbreviations for LMIs in constraints (20) and (21), respectively. And λ ≥ 0, S1,j ⪰ 0
and Zj ⪰ 0, ∀j ∈ KE, S2,i ⪰ 0 and Yi ⪰ 0, ∀i ∈ KI are the dual variables for constraints (15c), (20) and (15e), (21)
and (15d), respectively. Besides, all terms that are unrelated to the proof make up the collection △. Now, we focus on those Karush-Kuhn-Tucker (KKT) conditions with respect to Wi and Vj, thus obtained as follows:

$\lambda^{*}\geq0,\mathbf{S}_{1,j}^{*}\geq0,\mathbf{S}_{2,i}^{*}\geq0,\mathbf{Y}_{i}^{*},\mathbf{Z}_{j}^{*}\geq0,$ (40a) Y∗ i W∗ i = 0, Z∗ jV∗ j = 0, (40b) a:b,c:d l=1 � vec(Hi)H C∗ 2,i Γi vec(Hi) � Y∗ i = λ∗IN − � M � a:b,c:d l=1 k̸=i M � − � � vec(Hi)HC∗ 2,kvec(Hi) � j∈KE l + � M � a:b,c:d � , (40c) � vec(Gj)HC∗ 1,jvec(Gj) � a:b,c:d , j∈KE l Z∗ j = λ∗IN − � M � � vec(Gj)HC∗ 1,jvec(Gj) � (40d)

where a = c = (l − 1)N + 1 and b = d = lN. As can be
observation from (40b), the rank of W∗
                                i is related to the rank
of Y∗
    i . Considering a feasible scenario with Pmax > 0 and
Γi > 0, λ > 0 and Wi ̸= 0 must always hold. Then, it can
be demonstrated that Rank (W∗
                          i ) = 1 by taking use of the
findings in [47]. Similarly, applying the method of [47], we
can also prove �KE
              j=1 Rank
                       �
                        V∗
                         j
                          �
                            ≤ 1.

## References

[1] G. Zhu, X. Mu, L. Guo, H. Ao, and S. Xu, "Robust beamforming
design for STAR-RIS assisted SWIPT systems," in Proc. IEEE Int. Conf.
Commun. (ICC), May 2023, to be published.
[2] S. Zhang, Q. Wu, S. Xu, and G. Y. Li, "Fundamental green tradeoffs:
Progresses, challenges, and impacts on 5G networks," IEEE Commun. Surv. Tut., vol. 19, no. 1, pp. 33–56, 1st Quart. 2017.
[3] S. Buzzi, C.-L. I, T. E. Klein, H. V. Poor, C. Yang, and A. Zappone, "A
survey of energy-efficient techniques for 5G networks and challenges
ahead," *IEEE J. Sel. Areas Commun.*, vol. 34, no. 4, pp. 697–709, Apr.
2016.
[4] I. Krikidis, S. Timotheou, S. Nikolaou, G. Zheng, D. W. K. Ng, and
R. Schober, "Simultaneous wireless information and power transfer in
modern communication systems," *IEEE Commun. Mag.*, vol. 52, no. 11,
pp. 104–110, Nov. 2014.
[5] Y. Zeng, B. Clerckx, and R. Zhang, "Communications and signals design
for wireless power transmission," *IEEE Trans. Commun.*, vol. 65, no. 5,
pp. 2264–2290, May 2017.
[6] X. Zhou, R. Zhang, and C. K. Ho, "Wireless information and power
transfer: Architecture design and rate-energy tradeoff," IEEE Trans. Commun., vol. 61, no. 11, pp. 4754–4767, Nov. 2013.
[7] Z. Ding, C. Zhong, D. Wing Kwan Ng, M. Peng, H. A. Suraweera,
R. Schober, and H. V. Poor, "Application of smart antenna technologies
in simultaneous wireless information and power transfer," IEEE Commun. Mag., vol. 53, no. 4, pp. 86–93, Apr. 2015.
[8] Y. Liu, X. Liu, X. Mu, T. Hou, J. Xu, M. Di Renzo, and N. Al-Dhahir,
"Reconfigurable intelligent surfaces: Principles and opportunities," IEEE
Commun. Surv. Tut., vol. 23, no. 3, pp. 1546–1577, 3rd Quart. 2021.
[9] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and
C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in
wireless communication," *IEEE Trans. Wireless Commun.*, vol. 18, no. 8,
pp. 4157–4170, Aug. 2019.
[10] M. Di Renzo, A. Zappone, M. Debbah, M.-S. Alouini, C. Yuen,
J. de Rosny, and S. Tretyakov, "Smart radio environments empowered by reconfigurable intelligent surfaces: How it works, state of research,
and the road ahead," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 11, pp.
2450–2525, Nov. 2020.
[11] Q. Wu, X. Guan, and R. Zhang, "Intelligent reflecting surface-aided
wireless energy and information transmission: An overview," Proc.
IEEE, vol. 110, no. 1, pp. 150–170, Jan. 2022.
[12] X. Mu, Y. Liu, L. Guo, J. Lin, and R. Schober, "Simultaneously
transmitting and reflecting (STAR) RIS aided wireless communications,"
IEEE Trans. Wireless Commun., vol. 21, no. 5, pp. 3083–3098, May
2022.
$$L=\eta-\lambda\left(\sum_{i\in\mathcal{K}_{\varepsilon}}\mathrm{Tr}(\mathbf{W}_{i})+\sum_{j\in\mathcal{K}_{\varepsilon}}\mathrm{Tr}(\mathbf{V}_{j})-P_{\max}\right.\tag{39}$$ $$\left.+\sum_{i\in\mathcal{K}_{\varepsilon}}\mathrm{Tr}(\mathbf{Y}_{i}\mathbf{W}_{i})+\sum_{j\in\mathcal{K}_{\varepsilon}}\mathrm{Tr}\left(\mathbf{Z}_{j}\mathbf{V}_{j}\right)+\triangle.\right.$$
[13] Y. Liu, X. Mu, J. Xu, R. Schober, Y. Hao, H. V. Poor, and L. Hanzo,
"STAR: Simultaneous transmission and reflection for 360° coverage by
intelligent surfaces," *IEEE Trans. Commun.*, vol. 28, no. 6, pp. 102–109,
Dec. 2021.
[14] J. Xu, Y. Liu, X. Mu, and O. A. Dobre, "STAR-RISs: Simultaneous
transmitting and reflecting reconfigurable intelligent surfaces," IEEE
Commun. Lett., vol. 25, no. 9, pp. 3134–3138, Sep. 2021.
[15] Q. Wu and R. Zhang, "Weighted sum power maximization for intelligent
reflecting surface aided SWIPT," *IEEE Wireless Commun. Lett.*, vol. 9,
no. 5, pp. 586–590, May 2020.
[16] C. Pan, H. Ren, K. Wang, M. Elkashlan, A. Nallanathan, J. Wang, and
L. Hanzo, "Intelligent reflecting surface aided MIMO broadcasting for
simultaneous wireless information and power transfer," IEEE J. Sel.
Areas Commun., vol. 38, no. 8, pp. 1719–1734, Aug. 2020.
[17] Q. Wu and R. Zhang, "Joint active and passive beamforming optimization for intelligent reflecting surface assisted SWIPT under QoS
constraints," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 8, pp. 1735–
1748, Aug. 2020.
[18] S. Zargari, S. Farahmand, and B. Abolhassani, "Joint design of transmit
beamforming, irs platform, and power splitting swipt receivers for
downlink cellular multiuser miso," *Physical Communication*, vol. 48,
p. 101413, 2021.
[19] D. Xu, X. Yu, V. Jamali, D. W. K. Ng, and R. Schober, "Resource
allocation for large IRS-assisted SWIPT systems with non-linear energy harvesting model," in Proc. IEEE Wireless Commun. Netw. Conf.
(WCNC), 2021, pp. 1–7.
[20] S. Zargari, S. Farahmand, B. Abolhassani, and C. Tellambura, "Robust
active and passive beamformer design for IRS-aided downlink MISO PS-
SWIPT with a nonlinear energy harvesting model," IEEE Trans. Green Commun. Netw., vol. 5, no. 4, pp. 2027–2041, Jun. 2021.
[21] A. Khalili, S. Zargari, Q. Wu, D. W. K. Ng, and R. Zhang, "Multiobjective resource allocation for IRS-aided SWIPT," IEEE Wireless Commun. Lett., vol. 10, no. 6, pp. 1324–1328, Jun. 2021.
[22] Y. Zhao, B. Clerckx, and Z. Feng, "IRS-aided SWIPT: Joint waveform, active and passive beamforming design under nonlinear harvester
model," *IEEE Trans. Commun.*, vol. 70, no. 2, pp. 1345–1359, Feb.
2022.
[23] D. Xu, V. Jamali, X. Yu, D. W. K. Ng, and R. Schober, "Optimal resource
allocation design for large IRS-assisted SWIPT systems: A scalable
optimization framework," *IEEE Trans. Commun.*, vol. 70, no. 2, pp.
1423–1441, Feb. 2022.
[24] C. Wu, X. Mu, Y. Liu, X. Gu, and X. Wang, "Resource allocation in
STAR-RIS-aided networks: OMA and NOMA," IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 7653–7667, Sep. 2022.
[25] J. Zhao, Y. Zhu, X. Mu, K. Cai, Y. Liu, and L. Hanzo, "Simultaneously
transmitting and reflecting reconfigurable intelligent surface (STAR-RIS)
assisted UAV communications," *IEEE J. Sel. Areas Commun.*, vol. 40,
no. 10, pp. 3041–3056, Oct. 2022.
[26] X. Qin, Z. Song, T. Hou, W. Yu, J. Wang, and X. Sun, "Joint resource
allocation and configuration design for STAR-RIS-enhanced wirelesspowered MEC," *IEEE Trans. Commun.*, vol. 71, no. 4, pp. 2381–2395,
Jan. 2023.
[27] H.
R.
Hashempour,
H.
Bastami,
M.
Moradikia,
S.
A.Zekavat,
H. Behroozi, and A. L. Swindlehurst, "Secure SWIPT in STAR-RIS
aided downlink MISO rate-splitting multiple access networks," [Online].
Available:https://arxiv.org/abs/2211.09081.
[28] H. Liu, X. Yuan, and Y.-J. A. Zhang, "Matrix-calibration-based cascaded channel estimation for reconfigurable intelligent surface assisted
multiuser MIMO," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 11, pp.
2621–2636, Nov. 2020.
$$\left(\begin{array}{l}{{}}\\ {{}}\end{array}\right)+\sum_{j\in{\mathcal{K}}_{\mathcal{E}}}\mathrm{Tr}\left(\mathbf{C}_{1,j}\mathbf{S}_{1,j}\right)+\sum_{i\in{\mathcal{K}}_{\mathcal{I}}}\mathrm{Tr}\left(\mathbf{C}_{2,i}\mathbf{S}_{2,i}\right)$$
[29] Z. Zhang, J. Chen, Y. Liu, Q. Wu, B. He, and L. Yang, "On the
secrecy design of STAR-RIS assisted uplink NOMA networks," IEEE Transactions on Wireless Communications, vol. 21, no. 12, pp. 11 207–
11 221, Jul. 2022.
[30] Z. Wang, X. Mu, Y. Liu, and R. Schober, "Coupled phase-shift STAR-
RISs: A general optimization framework," *IEEE Wireless Commun. Lett.*,
vol. 12, no. 2, pp. 207–211, Nov. 2023.
[31] J. Xu, L. Liu, and R. Zhang, "Multiuser MISO beamforming for
simultaneous wireless information and power transfer," IEEE Trans.
Signal Process., vol. 62, no. 18, pp. 4798–4810, Sep. 2014.
[32] E. Boshkovska, D. W. K. Ng, N. Zlatanov, and R. Schober, "Practical
non-linear energy harvesting model and resource allocation for SWIPT
systems," *IEEE Commun. Lett.*, vol. 19, no. 12, pp. 2082–2085, Sep.
2015.
[33] G. Ma, J. Xu, Y. Zeng, and M. R. V. Moghadam, "A generic receiver
architecture for MIMO wireless power transfer with nonlinear energy
harvesting," *IEEE Signal Process. Lett.*, vol. 26, no. 2, pp. 312–316,
Jan. 2019.
[34] S. Zargari, A. Khalili, Q. Wu, M. Robat Mili, and D. W. K. Ng, "Maxmin fair energy-efficient beamforming design for intelligent reflecting surface-aided SWIPT systems with non-linear energy harvesting model,"
IEEE Trans. Veh. Technol., vol. 70, no. 6, pp. 5848–5864, May 2021.
[35] G. Chen, Q. Wu, W. Chen, D. W. K. Ng, and L. Hanzo, "IRS-aided
wireless powered MEC systems: TDMA or NOMA for computation
offloading?" *IEEE Trans. Wireless Commun.*, vol. 22, no. 2, pp. 1201–
1218, Feb. 2023.
[36] X. Yu, D. Xu, Y. Sun, D. W. K. Ng, and R. Schober, "Robust and secure
wireless communications via intelligent reflecting surfaces," IEEE J. Sel.
Areas Commun., vol. 38, no. 11, pp. 2637–2652, Nov. 2020.
[37] G. Zhou, C. Pan, H. Ren, K. Wang, and A. Nallanathan, "A framework
of robust transmission design for IRS-aided MISO communications with
imperfect cascaded channels," *IEEE Trans. Signal Process.*, vol. 68, pp.
5092–5106, Aug. 2020.
[38] C. Wu, C. You, Y. Liu, X. Gu, and Y. Cai, "Channel estimation for
STAR-RIS-aided wireless communication," IEEE Wireless Commun. Lett., vol. 26, no. 3, pp. 652–656, Dec. 2022.
[39] J. Xu and R. Zhang, "Energy beamforming with one-bit feedback," IEEE
Trans. Signal Process., vol. 62, no. 20, pp. 5370–5381, Aug. 2014.
[40] K. Miettinen, *Nonlinear Multiobjective Optimization*.
New York, NY,
USA: Springer, 1999.
[41] A. Khalili, S. Zarandi, M. Rasti, and E. Hossain, "Multi-objective
optimization for energy- and spectral-efficiency tradeoff in in-band fullduplex (IBFD) communication," in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2019, pp. 1–6.
[42] S. Boyd and L. Vandenberghe, *Convex Optimization*. Cambridge, U.K.:
Cambridge Univ. Press, 2004.
[43] M. Grant and S. Boyd, "CVX: MATLAB software for disciplined convex programming, version 2.1," [Online]. Available:http://cvxr.com/cvx, 2014.
[44] X. Yu, D. Xu, D. W. K. Ng, and R. Schober, "Power-efficient resource allocation for multiuser MISO systems via intelligent reflecting surfaces,"
in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, 2020, pp. 1–6.
[45] J. Nocedal and S. Wright, *Numerical Optimization*.
New York, NY,
USA: Springer, 2006.
[46] Z.-Q. Luo, W.-K. Ma, A. M.-C. So, Y. Ye, and S. Zhang, "Semidefinite
relaxation of quadratic optimization problems," IEEE Signal Process. Mag., vol. 27, no. 3, pp. 20–34, May 2010.
[47] E. Boshkovska, X. Chen, L. Dai, D. W. K. Ng, and R. Schober, "Maxmin fair beamforming for SWIPT systems with non-linear EH model,"
in *Proc. IEEE 86th Veh. Technol. Conf. (VTC-Fall)*, 2017, pp. 1–6.