# Movable Antenna Enabled Interference Network: Joint Antenna Position And Beamforming Design

Honghao Wang, Qingqing Wu, *Senior Member, IEEE,* and Wen Chen, Senior Member, IEEE
Abstract—This paper investigates the utility of movable antenna (MA) assistance for the multiple-input single-output (MISO) interference channel. We exploit an additional design degree of freedom provided by MA to enhance the desired signal and suppress interference so as to reduce the total transmit power of interference network. To this end, we jointly optimize the MA positions and transmit beamforming, subject to the signalto-interference-plus-noise ratio constraints of users. To address the non-convex optimization problem, we propose an efficient iterative algorithm to alternately optimize the MA positions via successive convex approximation method and the transmit beamforming via second-order cone program approach. Numerical results demonstrate that the proposed MA-enabled MISO interference network outperforms its conventional counterpart without MA, which significantly enhances the capability of intercell frequency reuse and reduces the complexity of transmitter design.

Index Terms—Movable antenna (MA), MISO interference channel, antenna position optimization, power minimization.

## I. Introduction

Spectrum sharing is extensively employed in contemporary cellular networks with increasing node density, which renders the overall network performance limited by the co-channel interference. Consequently, more sophisticated techniques for interference management with multi-cell cooperation become essential. Existing works have attempted to leverage intelligent reflecting surface (IRS) or reconfigurable intelligent surface (RIS), which serves as a promising component for the next generation of wireless communication systems [1], to enlarge the achievable rate region of the multiple-input single-output (MISO) interference network [2] and assist simultaneous wireless information and power transfer (SWIPT) in it [3]. However, the antenna scheme implemented at transceivers is predominantly the conventional FPA, which restricts the performance of interference networks due to underutilization of channel variation in the continuous spatial field.

To harness additional spatial degrees of freedom (DoFs)
in wireless channels for enhancing the diversity and spatial multiplexing of wireless systems, movable antenna (MA) [4] or fluid antenna system (FAS) [5] was conceived, which is designed to overcome the constraints of conventional fixedposition antennas (FPAs). Specifically, by connecting the MAs to radio frequency (RF) chains via flexible cables, the MA positions are allowed to be adjusted over a two-dimensional
(2D) region through motors or servos [6]. Based on this, MAs can be timely deployed to the positions with more favorable channel conditions for improving the quality-of-service.

With the aforementioned advantages, MA has garnered significant attention [7]–[10]. For instance, to further improve the channel capacity of multiple-input multiple-output (MIMO) system, authors in [7] proposed a new architecture incorporating MA, which demonstrates a substantial enhancement in communication performance compared to the conventional FPA system. Moreover, an MA-enabled multi-access channel for multi-user uplink transmission was investigated in [8], which leads to a noteworthy reduction in total transmit power as opposed to the FPA systems.

In light of the above, this paper investigates the MISO
interference channel aided by MAs at transmitters, leveraging the inherent characteristics of the multi-path channel and the extra spatial DoFs it offers to reduce inter-cell interference. The integration of MA introduces a new DoF in system design, enabling both desired signal enhancement and interference mitigation. To this end, by jointly optimizing MA positions and transmit beamforming, we aim to minimize the total transmit power under the individual signal-to-interference-plusnoise ratio (SINR) requirement of each user, which is a highly coupled non-convex problem. To address this challenge, an efficient algorithm based on block coordinate descent (BCD) is proposed, where MA positions and beamforming vectors are optimized in an alternating manner. Specifically, with fixed MA positions, the optimal beamforming vectors are obtained by second-order cone program (SOCP). On the other hand, by fixing beamforming vectors and scaling SINR constraints with a meticulously designed auxiliary value, the MA positions can be updated iteratively via successive convex approximation (SCA). Simulation results validate that the proposed algorithm can be effectively utilized in the MISO interference network, provided a certain region size for antennas moving is available. Consequently, the performance of spectrum sharing in interference network is dramatically improved. The MA system with simple beamforming, e.g., maximum ratio transmission (MRT), performs only slightly worse than that with complex beamforming and significantly better than the FPA system. Moreover, the number of antennas required for MA-aided interference network is drastically reduced, thus enabling the simplification of transmitter design.

Notations: x(n), X(*m, n*), ||X||F , λmax{X}, and vec(X)
represent the nth entry of vector x, the (*m, n*)th element of matrix X, the Frobenius norm of X, the maximum eigenvalue of X, and the vectorization of X, respectively. diag(x) denotes the diagonal matrix with diagonal elements being x.

## Ii. System Model And Problem Formulation

As shown in Fig. 1, we consider a MISO interference channel with K transmitter-user pairs, where each transmitter equipped with N MAs simultaneously transmits signals to its corresponding single-antenna user. Specifically, the MAs are connected to RF chains via flexible cables, enabling realtime adjustment of their positions [6]. The collections of coordinates of N MAs in each transmitter are denoted as Tj = [tj,1, . . . , tj,N] ∈ R2×N, j ∈ {1*, . . . , K*}, where tj,n = [xj,n, yj,n]T ∈ Cj for n ∈ {1*, . . . , N*} represented by Cartesian coordinates indicates the position of the nth MA
in transmitter j. Without loss of generality, Cj can be set as
2D square regions with the identical size of A × A wherein the MAs can move without restraint.

According to the field-response model [4], the channel vector hkj ∈ CN×1 from transmitter j to user k ∈ {1, . . . , K}
follows the structure as

$\mathbf{h}_{kj}=\mathbf{G}_{kj}^{H}\mathbf{\Sigma}_{kj}\mathbf{1}$, (1)
where 1 *∈ {*1}Lkj×1 is the all-one field response vector (FRV)
and Lkj is the number of channel paths from transmitter j to user k. The path-response matrix (PRM) is defined as Σkj =
diag
��
τkj,1, . . . , τkj,Lkj
�T �
∈ CLkj×Lkj, where τ*kj,l* is the complex response of the lth path for l = 1*, . . . , L*kj. Gkj =
[gkj,1, . . . , g*kj,N*] ∈ CLkj×N is the transmit field response matrix (FRM) at transmitter j, where g*kj,n* ∈ CLkj×1 is the transmit FRV between user k and the nth MA in transmitter j for n = 1*, . . . , N*. Denote λ as the carrier wavelength, the transmit FRVs are further given by

$$\mathbf{g}_{kj,n}=\left[e^{j\frac{2\pi}{\lambda}\mathbf{t}_{j,n}^{T}\mathbf{p}_{kj,1}},\ldots,e^{j\frac{2\pi}{\lambda}\mathbf{t}_{j,n}^{T}\mathbf{p}_{kj,L_{kj}}}\right]^{T},\tag{2}$$

where $\mathbf{p}_{kj,l}=\left[\sin\theta_{kj,l}\cos\phi_{kj,l},\cos\theta_{kj,l}\right]^{T}$, $\theta_{kj,l}\in[0,\pi]$ and $\phi_{kj,l}\in[0,\pi]$ denote the elevation and azimuth angles of the $l$th path from transmitter $j$ to user $k$, respectively. Moreover, the channel vectors can be reformulated as $\mathbf{h}_{kj}=\left[h_{kj}\left(\mathbf{t}_{j,1}\right),\ldots,h_{kj}\left(\mathbf{t}_{j,N}\right)\right]^{T}$, where

$$h_{kj}\left(\mathbf{t}_{j,n}\right)\stackrel{{\triangle}}{{=}}\sum_{l=1}^{L_{kj}}\tau_{kj,l}e^{-j\frac{2\pi}{\lambda}\mathbf{t}_{j,n}^{T}\mathbf{p}_{kj,l}}.\tag{3}$$

Let $\mathbf{w}_{j}\in\mathbb{C}^{N\times1}$ denote the transmit beamforming vector of transmitter $j$. Then, the baseband complex signal received at 
user k can be expressed as

yk = +zk, ∀k, (4) j=1 hH kjwjsj+zk = hH kkwksk j̸=k hH kjwjsj K � + � � �� � desired signal � �� � interference
where sk is the information symbol for user k with normalized power, zk denotes the additive white Gaussian noise (AWGN)
at user k, which is assumed to be circularly symmetric complex Gaussian (CSCG) distributed with zero mean and power σ2
k, i.e., zk ∼ CN
�
0, σ2
k
�
. With interference treated as noise at each user and signaling assumed CSCG, the resulting SINR at user k is given by

γk = , ∀k. (5) ��hH kkwk ��2 � j̸=k ���hH kjwj ��� 2 + σ2 k
In this paper, we aim to minimize the total transmit power by jointly optimizing the MA positions {Tj}K
j=1 and beamforming vectors {wj}K
j=1, subject to the individual SINR
constraint of each user. Besides, to avoid coupling effect between MAs in transmit regions, a minimum distance D is required between each pair of MAs in the same transmitter, i.e., ||tj,n − tj,˜n|| ≥D, ∀j, n, ˜n, ˜n̸=n, ˜n ∈ {1*, . . . , N*}. Accordingly, the optimization problem is formulated as

j=1 ||wj||2 (6a) (P1) : min {wj}K j=1,{Tj}K j=1 K � s.t. γk ≥ γk,min, ∀k, (6b) tj,n ∈ Cj, ∀j, n, (6c)
||tj,n − tj,˜n|| ≥D, ∀*j, n,* ˜n, ˜n̸=n, (6d)
where γk,min is the minimum SINR requirement for user k.

Note that (P1) is a non-convex optimization problem due to the non-convexity of minimum SINR constraint in (6b) as well as minimum distance constraint in (6d), which makes (P1) challenging to address.

## Iii. Proposed Solution

In this section, by dividing problem (P1) into two subproblems (P2) and (P3), an alternating optimization (AO) algorithm based on the SOCP and SCA techniques is proposed, where the transmit beamforming and MA positions are updated alternately with the other fixed. First, we consider the subproblem of transmit beamforming optimization with given MA positions. In this case, problem (P1) is transformed into

(P2) : $\min\limits_{\left\{\mathbf{w}_{j}\right\}_{j=1}^{K}}\sum\limits_{j=1}^{K}\left\|\mathbf{w}_{j}\right\|^{2}$ (7a) s.t. (6b).

Problem (P2) is reduced to the transmit beamforming optimization problem of the conventional MISO interference channel, which can be optimally solved via SOCP together with the bisection search method [11], [12].

Next, for any given optimal {wj}K
j=1, problem (P1) is transformed into the following feasible check problem (P3),

2 fkj � ti j,n � + ∇f T kj � ti j,n � � tj,n − ti j,n � − δkj,n � tj,n − ti j,n �T � tj,n − ti j,n � ≤ fkj (tj,n) ≤ fkj � ti j,n � + ∇f T kj � ti j,n � � tj,n − ti j,n � + δkj,n λ2 ∂2fkj ∂x2 j,n = −4π2 a=1 b=a+1 ζn(*a, b, kj*) (− sin θ*kj,a* cos ϕ*kj,a* + sin θ*kj,b* cos ϕ*kj,b*)2 − 4π2 Lkj−1 � Lkj � λ2 ∂2fkj ∂y2 j,n = −4π2 a=1 b=a+1 ζn(*a, b, kj*) (− cos θ*kj,a* + cos θ*kj,b*)2 − 4π2 Lkj−1 � Lkj � ∂2fkj λ2 ∂xj,n∂yj,n = ∂2fkj ∂yj,n∂xj,n = −4π2 a=1 b=a+1 ζn(*a, b, kj*) (− sin θ*kj,a* cos ϕ*kj,a* + sin θ*kj,b* cos ϕ*kj,b*) (− cos θ*kj,a* + cos θ*kj,b*) Lkj−1 � Lkj � λ2 − 4π2 l=1 χn (*kj, l*) sin θ*kj,l* cos ϕ*kj,l* cos θkj,l. (15) Lkj � F = �∂2fkj λmax � ∇2fkj(tj,n) � = ����∇2fkj(tj,n) ����2 ≤ ����∇2fkj(tj,n) ����2 λ2  ≤ 4 a=1 b=a+1 2 |Vkj (*a, b*)| + 4π2 Lkj−1 � Lkj � 4π2 2 fkk � ti k,n � + ∇f T kk � ti k,n � � tk,n − ti k,n � − δkk,n � tk,n − ti k,n �T � tk,n − ti k,n �  ≥ γk,min j̸=k � fkj � ti j,n � + ∇f T kj � ti j,n � � tj,n − ti j,n � + δkj,n �
where the MA positions {Tj}K
j=1 can be optimized with the constraints (6b)-(6d).

* (P3) : Find $\{\mathbf{T}_{j}\}_{j=1}^{K}$ (8a) s.t. (6b), (6c) and (6d).

Due to that for any user k, the channel power gain between a transmitter and that user is solely affected by the MA positions of that transmitter, i.e., the variables {Tj}K
j=1 are mutually independent, we decompose (P3) into N subproblems (P3.1.n), where the nth MA of each transmitter is optimized in parallel with all other MAs fixed in the nth subproblem.

(P3.1.n) : Find {tj,n}K j=1 (9a) s.t. γk ≥ γk,min, ∀k, (9b) tj,n ∈ Cj, ∀j, (9c) ||tj,n − tj,˜n|| ≥D, ∀j, ˜n, ˜n ̸= n. (9d)
By expanding the numerator and denominator of γk in (9b),

in terms of ���hH kjwj ��� 2 , we have the following reconstructed equation: ��hH kjwj ��2 = � wj,nvH kjgkj,n+ Gkj,˜n �� w∗ j,ngH kj,nvkj+ G∗ kj,˜n � = ��wj,nvH kjgkj,n ��2+2Re � G∗ kj,˜nwj,nvH kjgkj,n � +|Gkj,˜n|2 , (10) ˜n̸=n wj,˜n �Lkj l=1 τ ∗ kj,lej 2π where Gkj,˜n = �
fkj (tj,n) = tr (V*kj,n*) + |Gkj,˜n|2

                                         λ tT
                                            j,˜npkj,l, vkj =
vec (Σkj), wj,n = wj (n). Then, by denoting fkj (tj,n) =
���hH
  kjwj
       ���
        2
         , (10) can be further rewritten as

+ a=1 b=a+1 ζn(*a, b, kj*) + l=1 χn(l, kj) , (11) Lkj−1 � Lkj � Lkj �
where we define

2 � tj,n − ti j,n �T � tj,n − ti j,n � . (12) λ2 l=1 χn(*kj, l*) sin2 θ*kj,l* cos2 ϕkj,l. (13) Lkj � λ2 l=1 χn(*kj, l*) cos2 θkj,l. (14) Lkj � ∂xj,n∂yj,n ∂yj,n∂xj,n ∂x2 j,n ∂y2 j,n 2 �2 + � ∂2fkj �2 + � ∂2fkj �2 + �∂2fkj �2 . (16) λ2  l=1 2 |Gkj,˜n| |wj,n| |vkj,l| Lkj �  2  � tj,n − ti j,n �T � tj,n − ti j,n �� + σ2 k  , ∀k. (18) Vkj,n △=|wj,n|2vkjvH kj, rkj,n,l △=|Gkj,˜n||wj,n||vkj,l|, αn(*a, b, kj*) △=(2π/λ) � −tT j,npkj,a+tT j,npkj,b � , vkj,l △=vkj(l), ζn(*a, b, kj*) △=2|Vkj,n(*a, b*)| cos(αn(a, b, kj)+∠Vkj,n(a, b)), λ tT j,npkj,l−∠Gkj,˜n+∠wj,n−∠vkj,l χn(*kj, l*) △=2r*kj,n,l* cos �2π � .
Next, the SCA method is employed to tackle the non-convex constraint (9b) based on the formulations above. By applying the second-order Taylor expansion, we construct a quadratic surrogate function that serves as a global lower bound for γk in
(9b). Specifically, given the provided local point ti j,n obtained in the ith iteration, the inequality relationship (12) holds as shown at the top of this page. Accordingly, the upper and lower bounds of fkj(tj,n) are obtained, which can be achieved through the introduction of a positive real number δ*kj,n* such that δkj,nI2 ⪰ ∇2fkj(tj,n). According to (13)-(16), δ*kj,n* can be selected by calculating the Frobenius norm of the Hessian matrix of ∇2fkj(tj,n) as follows:

δ*kj,n* = 16π2 λ2   a=1 b=a+1 |Vkj (*a, b*)| + l=1 rkj,n,l Lkj−1 � Lkj � Lkj �   . (17) In this way, by tightening the numerator of $\gamma_{k}$ in (9b) to its lower bound and the denominator to its upper bound, (P3.1.n) is then reduced to problem (P3.2.n) in the $(i+1)$th iteration, where constraint (18) is shown at the top of this page.

$$\mbox{(P3.2.n)}:\ \ \mbox{Find}\ \ \left\{{\bf t}_{j,n}\right\}_{j=1}^{K}\tag{19a}$$

                        s.t.
                               (18), (9c) and (9d).
  Finally, we deal with the non-convex constraint (9d) via
the SCA method. Denote gradient vector of ||tj,n − tj,˜n||2
over tj,n as ∇ ||tj,n − tj,˜n||2 = (tj,n − tj,˜n) / ||tj,n − tj,˜n||2.
Since the denominator term ||tj,n − tj,˜n||2 ≥D>0, the gradient vector always exists. Furthermore, the following inequality
holds utilizing the first-order Taylor expansion at ti
                                                    j,n:

||tj,n−tj,˜n|| ≥ ����ti j,n−tj,˜n ����+ � ∇ ����ti j,n−tj,˜n �����T (tj,n−tj,˜n) = ����ti j,n − tj,˜n ���� + 1 ����ti j,n − tj,˜n ���� � ti j,n − tj,˜n �T � tj,n − ti j,n � = 1 ����ti j,n − tj,˜n ���� � ti j,n − tj,˜n �T (tj,n − tj,˜n) . (20)
Hereto, for a given ti j,n obtained in the ith iteration, (P3.2.n)
is evidently transformed into a convex position optimization problem (P3.3.n) in the (i + 1)th iteration.

(P3.3.n) : Find {tj,n}K j=1 (21a) s.t. (18), (9c). � ti j,n−tj,˜n �T (tj,n−tj,˜n) ����ti j,n−tj,˜n ���� ≥D, ∀j, ˜n, ˜n̸=n, (21b)
Based on the above derivations, the proposed algorithm for joint antenna position and beamforming design is summarized in **Algorithm 1**, where the objective function is monotonically non-increasing and lower bounded, thereby ensuring the convergence. The complexities for solving (P2)
and (P3.3.n) are O
�
K3.5N 3�
and O
�
K3.5N 1.5�
, respectively.

Therefore, the overall complexity of the proposed algorithm is O
�
I1
�
K3.5N 3 + NI2
�
K3.5N 1.5���
, where I1 and I2 denote the numbers of iterations.

## Algorithm 1 Joint Beamforming And Antenna Position Design

j=1.

Input: Convergence criteria and initial positions
�
T[0]
j
�K
1: repeat

�
.
Output: The optimized solution
��
w⋆
j
�K
j=1 ,
�
T⋆
j
�K
j=1
2:
Update
�
w⋆
j
�K
j=1 by solving (P2).
4: **until** The objective function of (P1) converges.
3:
Update
�
T⋆
j
�K
j=1 by solving (P3.3.n).

## Iv. Numerical Results

In this section, we provide the numerical simulations to validate the effectiveness of the proposed design. In particular, a MISO interference network with K transmitter-user pairs in a 2D coordinate system is assumed to randomly locate the transmitters and users with dkk = 50 m and dkj = 80 m, where dkj represents the distance between transmitter j and user k. We adopt the channel model in
(1), where the numbers of channel paths are assumed to be the same, i.e., Lkj = L, ∀*k, j*. The diagonal elements of PRM Σkj in (1) follow the CSCG distribution CN
�
0, c2
kj/L
�
, where c2
kj = β0d−α0
kj is the expected channel power gain of hkj, β0 = −40 dB represents the expected value of the average channel power gain at the reference distance of
1 m, and α0 = 2.8 denotes the pathloss exponent. It can be pointed out that the total power of the elements in the PRM is the same for the channels with different numbers of paths, i.e., E
�
tr
�
ΣH
kjΣkj
��
≡ c2
kj, which ensures the fairness of comparison. The elevation and azimuth angles of the channel paths are random variables following the joint probability density function (PDF) fA(θkj,l, ϕ*kj,l*) = sin θkj,l
2π
,
θkj,l ∈ [0, π], ϕkj,l ∈ [0, π], which indicates that the azimuth angles have the same probability for all directions in the front half-space of antenna array [4]. Due to limited scatters in the environment, the L × K elevation and azimuth angles of channel paths from the same transmitter are randomly selected out of the same set of S = 10 pairs of angles that are randomly generated with the previous joint PDF. Other adopted settings of simulation parameters are γk,min = γmin = 10 dB and
σ2
k = σ2 = −80 dBm. The results obtained by Algorithm 1
are termed as "Proposed algorithm". The benchmark schemes are defined as follows. "MA MRT": the antennas of each transmitter adopting MRT beamforming are deployed at the positions that minimize the total transmit power. "FPA SOCP": the antennas are fixed at 2D local coordinate systems, respectively, and the SOCP-based beamforming is adopted. "FPA MRT" can be similarly derived.

First, Fig. 2 shows the total transmit powers versus the numbers of channel paths with different numbers of transmitteruser pairs K, where the parameters are set to A = 4λ
and N = 4. It is observed that the powers of all schemes decrease with L and the proposed algorithm outperforms FPA scheme for any K due to the interference mitigation gain provided by MA positioning optimization. Besides, the decreasing transmit power of FPA system is not caused by the increasing average channel gain (normalized by L and therefore a constant) but due to the reduced interference. As the number of channel paths for each transmitter-user pair increases, the spatial diversity of MA is enhanced by leveraging the prominent channel variation, which decreases the correlation among channel vectors. However, as L is increased larger than 5, the descent rate for the total transmit power becomes small because of the fact that the channel correlation is constrained by the numbers of elevation and azimuth angles at transmitters. Specifically, according to the channel model in (1), if the total numbers of angles are limited, the FRMs of multiple channels are likely to have similar row vectors. Thus, the local movement of MAs cannot further bring a significant reduction in channel correlation. The result demonstrates that due to the strong ability of desired signal enhancement and interference suppression of MA, the total transmit power of the proposed algorithm with 5 transmitteruser pairs is even lower than that of FPA system with 3 pairs, which indicates that the MA-aided interference network can accommodate more cells without incurring any increase in total transmit power.

Fig. 3 shows the total transmit powers of different schemes versus the normalized region sizes for MAs moving at the transmitters, where the size of moving region is normalized by carrier wavelength, i.e., *A/λ*. The numbers of transmitteruser pairs, channel paths, and antennas are set as K = 2, L = 10, and N = 4, respectively. From the observation, the total transmit powers achieved by MA schemes decrease with the region size and are much lower than those of FPA schemes. Moreover, the powers of the proposed algorithm and "MA MRT" scheme both dramatically decrease as the region size increases from λ to 1.5λ, while achieving their lower bounds for A = 3λ. This results from the fact that the larger the region size, the more likely the MAs are to obtain more favorable channel conditions. It is worth noting that as long as the region size is guaranteed to be larger than λ, the total transmit power of MA system with simple MRT beamforming is significantly lower than that of FPA system, and the power gap becomes larger with the increase of region size. For a relatively large A, e.g., A = 2.5λ, the "MA MRT" scheme can reap more than 4 dB and 8 dB power-saving compared with the two FPA schemes, respectively.

In Fig. 4, we compare the total transmit powers of different schemes versus the numbers of antennas, where the parameters are set to K = 2, L = 10, and A = 4λ. As can be observed, the total transmit power decreases as the number of antennas increases for all schemes. The superiority of MA schemes over the others, regardless of the type of beamforming employed, becomes evident. This can be attributed to the substantial reduction of the correlation among channel vectors caused by the positioning optimization of MAs, which facilitates effective mitigation of interference among different transmitters and consequently leads to a decrease in total transmit power. It is noted that the utility of SOCP-based beamforming can be approximated by implementing simple MRT method in the MA system, which means that we can drastically reduce the complexity of transmit beamforming with negligible additional power. Besides, the MA scheme is also capable of effectively reducing the number of antennas required by more than half compared with FPA scheme while maintaining the same power constraint and communication metrics. For instance, only 4
antennas are utilized in "MA MRT" scheme to achieve the performance of "FPA SOCP" scheme that deploys 9 antennas, which simplifies the transmitter design.

V. CONCLUSION
In this paper, we investigated the MA-enabled MISO interference channel system, where each transmitter is equipped with N MAs. By leveraging the additional design DoF provided by MA, we formulated an optimization problem for minimizing the total transmit power of interference network by jointly optimizing the MA positions and transmit beamforming. Since the resultant problem is highly coupled and non-convex, we proposed an alternating optimization algorithm based on the BCD method, where the optimization variables are iteratively updated by introducing the welldesigned auxiliary value and invoking the SOCP and SCA techniques. Furthermore, numerical results were provided to clarify that the MA-aided interference network increases the number of cells that can be held and enables the simplification of transmitter design by moving antennas properly within a small region of several-wavelength size.

## References

[1] Q. Wu and R. Zhang, "Intelligent reflecting surface enhanced wireless
network via joint active and passive beamforming," IEEE Trans. Wireless Commun., vol. 18, pp. 5394–5409, Nov. 2019.
[2] W. Huang, Y. Zeng, and Y. Huang, "Achievable rate region of MISO
interference channel aided by intelligent reflecting surface," IEEE Trans. Veh. Technol., vol. 69, pp. 16264–16269, Dec. 2020.
[3] Y. Gao *et al.*, "Exploiting intelligent reflecting surfaces for interference
channels with SWIPT," *IEEE Trans. Wireless Commun.*, Oct. 2023.
[4] L. Zhu, W. Ma, and R. Zhang, "Modeling and performance analysis
for movable antenna enabled wireless communications," IEEE Trans.
Wireless Commun., Nov. 2023.
[5] K.-K. Wong *et al.*, "Fluid antenna system - Part I: Preliminaries," IEEE
Commun. Lett., vol. 27, pp. 1919–1923, Aug. 2023.
[6] S. Basbug, "Design and synthesis of antenna array with movable elements along semicircular paths," IEEE Antennas and Wireless Propagat. Lett., vol. 16, pp. 3059–3062, Oct. 2017.
[7] W. Ma, L. Zhu, and R. Zhang, "MIMO capacity characterization for
movable antenna systems," *IEEE Trans. Wireless Commun.*, Sep. 2023.
[8] L. Zhu, W. Ma, B. Ning, and R. Zhang, "Movable-antenna enhanced
multiuser communication via antenna position optimization," IEEE
Trans. Wireless Commun., Dec. 2023.
[9] H. Qin *et al.*, "Antenna positioning and beamforming design for
movable-antenna enabled multi-user downlink communications," arxiv:
2311.03046, 2023.
[10] G. Hu *et al.*, "Fluid antennas-enabled multiuser uplink: A lowcomplexity gradient descent for total transmit power minimization," 2024.
[11] L. Liu, R. Zhang, and K.-C. Chua, "Achieving global optimality for
weighted sum-rate maximization in the K-user Gaussian interference channel with multiple antennas," *IEEE Trans. Wireless Commun.*, vol. 11, pp. 1933–1945, May 2012.
[12] Q. Wu and R. Zhang, "Towards smart and reconfigurable environment:
Intelligent reflecting surface aided wireless network," IEEE Commun. Mag., vol. 58, pp. 106–112, Jan. 2020.