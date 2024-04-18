# Primary Rate Maximization In Movable Antennas Empowered Symbiotic Radio Communications

Bin Lyu∗, Hao Liu∗, Wenqing Hong∗, Shimin Gong†, and Feng Tian∗
∗ Nanjing University of Posts and Telecommunications, Nanjing 210003, China
† Sun Yat-sen University, Shenzhen 518055, China

  Abstract—In this paper, we propose a movable antenna (MA)
empowered scheme for symbiotic radio (SR) communication sys-
tems. Specifically, multiple antennas at the primary transmitter
(PT) can be flexibly moved to favorable locations to boost the
channel conditions of the primary and secondary transmissions.
The primary transmission is achieved by the active transmission
from the PT to the primary user (PU), while the backscatter
device (BD) takes a ride over the incident signal from the PT
to passively send the secondary signal to the PU. Under this
setup, we consider a primary rate maximization problem by
jointly optimizing the transmit beamforming and the positions
of MAs at the PT under a practical bit error rate constraint
on the secondary transmission. Then, an alternating optimiza-
tion framework with the utilization of the successive convex
approximation, semi-definite processing and simulated annealing
(SA) modified particle swarm optimization (SA-PSO) methods
is proposed to find the solution of the transmit beamforming
and MAs' positions. Finally, numerical results are provided
to demonstrate the performance improvement provided by the
proposed MA empowered scheme and the proposed algorithm.
  Index Terms—Movable antenna, symbiotic radio, alternating
optimization, simulated annealing modified particle swarm opti-
mization.

## I. Introduction

With the emergence of 6G communications, the requirements on spectrum and energy efficiency are becoming more and more stringent [1]. On one hand, 6G communications will facilitate the ubiquitous deployment of wireless devices, massive access to which poses a great challenge to the scarce spectrum resources. On the other hand, the radio-frequency
(RF) components used in wireless devices are energy-hungry, which is most unlikely to attain satisfactory energy efficiency performance. The two drawbacks may seriously restrict the application of 6G communications in the near future. Thus, how to overcome the drawbacks is worthy of investigations.

Recently, symbiotic radio (SR) communications [2] has been emerged as a promising solution to the above drawbacks. In a typical SR system, wireless devices from the secondary system can reuse the spectrum band allocated to the primary transmission and take a ride over the primary signals for passive information delivery. Thus, these devices do not need an additional spectrum band and are unnecessary to equip with RF components. This setup boosts the system spectrum and energy efficiency and is friendly to 6G communications. Motivated by this advantage, SR has been widely investigated
[2]–[5]. In [2], the parasitic SR (PSR) paradigm was designed to adapt the diversified communication requirements. In [3], the duration ratio between the primary and secondary signals to attain a mutualistic relationship for SR communications was investigated. In [4], the impact of finite blocklength channel codes on the secondary transmission was studied. In [5], the cell-free paradigm was proposed for SR communications to avoid the interference caused by the cellular network structure and extend network coverage. However, the system performance of [3]–[5], especially the secondary transmission, was not satisfactory. One important reason for this phenomenon is that the antennas at the primary transmitter (PT) in [3]–[5] was located on fixed positions, based on which the degrees of freedom (DoFs) for achieving high spatial diversity cannot be fully leveraged.

To address the challenge above, an emerging concept, movable antenna (MA), has been proposed as an efficient approach since it can make full use of the spatial DoFs [6]– [8]. Unlike conventional antennas with fixed positions, the flexible cable is utilized to establish the connection between each MA and its corresponding RF chain, enabling the position of each MA to be dynamically adjusted to construct a favorable wireless environment [6]. Currently, the investigation of MA
empowered wireless communications is in its quite early stage.

In [7], the positions of MAs at the transmitter and receiver were jointly optimized to capture the ultimate downlink system capacity. The authors in [8] shifted their attention to MA based uplink communication systems with multiple users. The results in [7] and [8] demonstrated that the application of MAs can achieve amazing system performance improvement.

However, how to apply MAs to handle the unsatisfactory communication performance in SR systems has not been solved, especially when both primary and secondary transmissions are taken into account. To fill in this research gap, in this paper, we propose an MA empowered scheme for the SR communication system, which comprises of a PT, a backscatter device (BD) and a primary user (PU). The PT is equipped with MAs to send primary signals to the PU with a fixed antenna (FA). By considering the PSR paradigm, the FA-based BD takes a ride over the primary signals for delivering its own information to establish the secondary transmission. Under this setup, the MAs at the PT are utilized to wholly explore the DoFs for boosting the primary and secondary transmissions. Moreover, we investigate a primary transmission rate maximization problem under the bit error rate (BER) constraint on the secondary transmission. To handle the non-convexity faced by the original problem, we propose an alternating optimization (AO) framework to decompose it into two sub-problems. For the sub-problem of designing the transmit beamforming, the successive convex approximation (SCA) and semi-definite processing (SDP) are both leveraged to find a near-optimal solution. While, the simulated annealing
(SA) modified particle swarm optimization (SA-PSO) method is utilized to solve the sub-problem of optimizing the positions of MAs. Finally, numerical results are conducted to demonstrate the superior performance provided by utilizing the MAs at the PT and the proposed algorithm with the SA-PSO.

## Ii. System Model

We consider an MA empowered SR communication system, in which there exist a PT with K MAs, a BD equipped with single FA, and a PU equipped with single FA. The illustration of the system model is shown in Fig. 1. For the k-th MA at the PT, it utilizes a flexible cable to connect with its corresponding RF chain for ensuring the movement. The position of the k-th MA is denoted by pk = [xk, yk]T , which can be updated in a two-dimensional region with size [xmin, xmax] × [ymin, ymax].

While the positions of the FAs at the BD and the PU are static and represented by pb = [xb, yb]T and pu = [xu, yu]T , respectively. Under this setup, the channel condition between the PT and the BD and that between the PT and the PU can be improved by moving the MAs to favorable positions.

## A. Channel Model

We consider a quasi-static fading channel model, based on which the channels remain static in each block when the MAs are fixed. We first describe the channels related with the PT.

Let Lt p represent the amount of transmit paths between the PT
and the node-κ, where κ = {b, u}, κ = b represents that the node is the BD, and κ = u represents that the node is the PU. The azimuth and elevation angles of departure (AoDs)
of the m-th transmit path between the PT and the node-κ
are presented by φt m and θt m, respectively, where m ∈ Lt, and Lt = {1, . . . , Lt p} is the set of the PT's transmit paths.

According to [7], the signal propagation difference between the m-th transmit path of the k-th MA and the origin of the transmit region, denoted by ρt m(pk), is expressed as

$$\rho^{t}_{m}(\mathbf{p}_{k})=x_{k}\sin\theta^{t}_{m}\cos\phi^{t}_{m}+y_{k}\cos\theta^{t}_{m},\tag{1}$$
where k ∈ K, m ∈ Lt, and K = {1, . . . , K} is the set of the MAs at the PT.

Similarly, for n ∈ Lr
κ, the n-th receive path's azimuth and elevation angles of arrival (AoAs) between the PT and the node-κ are denoted by φr
κ,n and θr
κ,n, respectively, where Lr
κ = {1, . . . , Lr
κ} is the set of the receive paths associated with the node-κ, and Lr
κ is the amount of corresponding receive paths. Denote the signal propagation difference between the n-th receive path of the node-κ and the origin of the receive region as ρr
κ,n(pκ), which is formulated as

$$\rho^{r}_{\kappa,n}(\mathbf{p}_{\kappa})=x_{\kappa}\sin\theta^{r}_{\kappa,n}\cos\phi^{r}_{\kappa,n}+y_{\kappa}\cos\theta^{r}_{\kappa,n},\tag{2}$$
where κ ∈ {b, u}, n ∈ Lr
κ.

The channel vector from the PT to the node-κ, denoted by hH
κ , is given by

$\mathbf{h}_{\kappa}^{H}=\mathbf{f}_{\kappa}^{H}\mathbf{\Sigma}_{\kappa}\mathbf{G},\ \kappa\in\{b,u\},$ (3)
λ ρr
κ,1, . . . , ej 2π
where fκ = [ej 2π

                               λ ρr
                                  κ,Lrκ ]T
                                          ∈ CLr
                                                κ×1 is the
receive field response vector at the node-κ, Σκ ∈ CLr
                                                       κ×Lt
                                                          p
is the path-response matrix, G = [gt(p1), . . . , gt(pK)] ∈
CLt
   p×K is the transmit field response matrix, and gt(pk) =

[ej 2π

λ ρt
  1, . . . , e
          j 2π

               λ ρt
                 Ltp]T ∈ CLt
                            p×1 is the transmit field response
vector associated with the k-th MA, and λ is the carrier
wavelength. It is noted that fκ is constant due to the static
position of the node-κ, and Gκ is a variable due to the movable
characteristic of the antennas at the PT.
  Then, we model the channel between the BD and the PU,
which is represented by hs. Similarly, hs can be expressed as

hs = f H
     u Σsgs,
                         (4)

where Σs ∈ CLr
               s×Lt
                  s is the path-response matrix, gs =
[ej 2π

λ ρt
  s,1, . . . , e
           j 2π

                λ ρt
                   s,Lts]T ∈ CLt
                               s×1 is the transmit field re-
sponse at the BD, Ls is the amount of transmit paths between
the BD and the PU, ρt
                      s,̺ = xb sin θt
                                   s,̺ cos φt
                                           s,̺ + yb cos θt
                                                        s,̺,
θt
 s,̺ represents the elevation AoD, φt
                                   s,̺ represents the azimuth
AoD, and ̺ = 1, . . . , Lt
                        s. Since both the BD and PU are
equipped with the FA, hs is also a constant.

## B. Transmission Model

In the considered system, the PT sends primary signals to the PU with the involvement of the BD. Denote the primary signal at the PT as ws(l), where s(l) is the primary signal with unit power, w ∈ CK×1 is the transmit beamforming vector satisfying ||w||2 ≤ Pmax, and Pmax is the maximum power provided by the PT. The incident signal at the BD from the PT is denoted by hH
b ws(l). By catching a ride over this incident signal, the BD can send its own information-carrying signal c(l), which is also named as the secondary signal.

Considering the implementation of the BD in reality, we adopt the binary phase shift keying modulation, i.e., c(l) ∈ {−1, 1}.

The received signal at the PU is formulated as [2]

$$y(l)=h_{u}^{H}ws(l)+\sqrt{\alpha}h_{s}h_{b}^{H}ws(l)c(l)+z(l),\tag{5}$$
where α ∈ [0, 1] is the reflection efficiency at the BD, z(l) ∼
CN(0, σ2) is the additive Gaussian white noise at the PU. The first term of (5) is the signal transmitted through the direct link, and the second term represents the reflected signal from the BD combing s(l) and c(l).

As the PSR paradigm is considered, the PU first decodes s(l) by treating the second term as the interference [2].

Accordingly, the expression of the signal to interference plus
noise ratio (SINR) is γp =
                               |hH
                                 u w|2

                     α|hs|2|hH
                          b w|2+σ2 . Then, the primary
rate from the PT to the PU is

$R_{p}=\log_{2}(1+\gamma_{p})$.

  After decoding s(l) and removing the first term from (5),
the signal to noise ratio (SNR) of decoding c(l) is given by
γc =
      α|hs|2|hH
             b w|2

γc

          σ2
                . According to [9] and [10], the average
BER for decoding c(l) is then expressed as ec = 1

1+γc .

2 − 1

2
 �

## Iii. Primary Rate Maximization

In this section, we investigate the primary rate maximization problem under the BER constraint for decoding the secondary signal. To be specific, the maximization problem is formulated as a joint optimization of the transmit beamforming and the positions of the MAs at the PT, which is formulated as

$$\max_{\mathbf{w},\mathbf{p}}R_{p}$$ s.t. C1: $$||\mathbf{w}||_{2}^{2}\leq P_{\max},$$ C2: $$c_{c}\leq\mathrm{e}_{\max},$$ (**P1**) C3: $$x_{\min}\leq x_{k}\leq x_{\max},$$ $$y_{\min}\leq y_{k}\leq y_{\max},\ k\in\mathcal{K},$$ C4: $$\|\mathbf{p}_{k}-\mathbf{p}_{\iota}\|_{2}\geq d_{\min},\ k,\iota\in\mathcal{K},\ k\neq\iota,$$

where $\mathbf{p}=[p_{1}^{T},\ldots,p_{K}^{T}]^{T}$, $e_{\max}$ is the maximum allowable BER for decoding $c(l)$, $d_{\min}$ represents the minimum distance between any two MAS. C1 indicates that the transmit power at the PT is constrained by its available maximum power $P_{\max}$, C2 is the BER constraint at the PU for ensuring the quality of service of the secondary transmission, C3 restrains the movable region of the MAS, and C4 is the distance constraint to avoid the coupling effect on MAS.

It is observed that **P1** is a highly non-convex problem since the objective function and the constraints C1, C2 and C4 are all non-convex, especially the coupled variables in the objective function and C2. To make this challenging problem tractable, an alternating optimization (AO) framework is proposed, in which $\mathbf{w}$ and $\mathbf{p}$ are updated in an alternating manner. Specifically, the SCA and SDP methods are explored for the optimization of $\mathbf{w}$ to guarantee an accurate solution, and the SA-PSO method proposed in [11] is applied to optimize the positions of MAS.

## A. Optimization Of Transmit Beamforming

We first fix the positions of MAs and design w to maximize Rp by solving the following sub-problem

$$\max_{\mathbf{w}}R_{p}$$ s.t. C1: $$||\mathbf{w}||_{2}^{2}\leq P_{\max},$$ (P2) C2: $$e_{c}\leq e_{\max}.$$

Before solving **P2**, we first analyze the structure of the constraint C2. It is easy to prove that $e_{c}$ is a monotonically decreasing function associated with $\gamma_{c}$. Thus, C2 can be equivalently transformed as $\bar{\mbox{C2}}:\ \gamma_{c}\geq\gamma_{\min}$, where $\gamma_{\min}$ is the 
minimum SNR for ensuring the BER constraint and can be obtained under the condition ec = emax by using the bisection method. With ¯
C2, we then rewrite P2 as

$\begin{array}{ll}\mbox{max}&R_{p}\\ \mbox{s.t.}&\mbox{C1,}\mbox{C2.}\end{array}$
To handle the non-convexity of P2.1, we first introduce W =
wwH for reformulation. It is obvious W is a rank-one matrix, i.e., Rank(W ) = 1. By utilizing W , the constraints C1 and
¯
C2 are reformulated as

˜ C1 : Tr(W ) ≤ Pmax, ˜ C2 : α|hs|2Tr(hbhH b W ) σ2 ≥ γmin,
which are both affine. Similarly, Rp can be transformed as

Rp = log2 � 1 + Tr(huhH u W ) � . (7) α|hs|2Tr(hbhH b W ) + σ2
However, Rp defined in (7) is still non-convex due to the fractional form. To deal with this difficulty, the SCA method is utilized to derive the lower-bound of Rp, which is given by

Rp ≥ log2(Tr(huhH u W ) + α|hs|2Tr(hbhH b W ) + σ2) − log2(α|hs|2Tr(hbhH b W (ς)) + σ2) − α|hs|2Tr[hbhH b (W − W (ς))] ln(2)[α|hs|2Tr(hbhH b W (ς)) + σ2] ≜ ˜Rp, (8)
where W (ς) is a feasible point of W in the ς-th iteration of implementing the SCA method. It can be found that ˜Rp is a concave function associated with W . With the updated objective function and constraints and relaxing the constraint Rank(W ) = 1, P2.1 can be transformed into the following SDP problem max W
˜Rp

s.t. ˜ C1, ˜ C2. (P2.2)
The optimal solution to P2.2, denoted by ¯
W , can be attained by utilizing the interior-point method. According to [12], it is proved that
¯
W is a rank-one matrix, which ensures the optimality of the obtained solution from P2.2 after removing the rank-one constraint.

By iteratively solving P2.2 until the convergence, the optimal transmit beamforming matrix is finally obtained and denoted by W ∗. Then, the optimal solution of P2.1, denoted by w∗, is attained by implementing the singular value decomposition of W ∗.

## B. Optimization Of The Mas' Positions

With the attained solution in Section III-A, we then find the optimal positions of the MAs by solving P3 as

$\begin{array}{cccc}\max&R_{p}\\ &p&\\ \end{array}$ (P3)

s.t. C1, C2, C3, C4.

It is generally challenging to solve P3 due to the huge solution space, i.e., [xmin, xmax]K × [ymin, ymax]K, which results in an

extremely high computational complexity. To handle this diffi-
culty and guarantee the solution accuracy, the SA-PSO based
method [11] is applied as an effective approach. By using
the SA-PSO method, we first introduce S particles, whose
initial positions and velocities are represented by P(0) =
{p(0)
  1 , p(0)
       2 , . . . , p(0)
                 S } and V(0) = {v(0)
                                      1 , v(0)
                                           2 , . . . , v(0)
                                                     S }, re-
spectively, and p(0)
                 s
                     = [p(0)
                          s,1, p(0)
                               s,2, . . . , p(0)
                                         s,K]. p(0)
                                                s
                                                    denotes a
possible solution of the positions with p(0)
                                           s,k = [x(0)
                                                    s,k, y(0)
                                                         s,k],
which satisfies xmin ≤ x(0)
                        s,k ≤ xmax and ymin ≤ y(0)
                                                s,k ≤ ymax. It
is known that the target of the SA-PSO method is to find the
best position among these particles and let it be a solution of
P3. The solving process of P3 based on the SA-PSO method
is summarized in Algorithm 1. The introduction of Algorithm
1 is given as follows.
  1) Definition of the fitness function: To evaluate the fitness
of each particle, i.e., evaluating whether the positions of these
particles can lead to satisfactory performance, we first define
the fitness function as

F(w∗, p(q) s ) = ˜Rp(w∗) − r1 ���R(p(q) s ) ��� . (9) In (9), ˜Rp(w∗) is the maximum primary rate derived by solving P2.2 in Section III-A with the fixed positions of MAs, p(q) s represents the updated positions of the q-th iteration of implementing the SA-PSO method, R(p(q) s ) is a set including the pair positions of MAs violating the constraint C4 and defined as ���R(p(q) s ) ��� = {(pk, pι)| ∥pk − pι∥2 < dmin, 1 ≤ k < ι ≤ K}, (10)
where
���R(p(q)
s )
��� represents the cardinality of R(p(q)
s ). Moreover, r1 is the penalty factor and set to be sufficiently large to satisfy ˜Rp(w∗) − r1 ≤ 0. This setting ensures that the constraint C4 can be finally met, i.e.,
���R(p(q)
s )
��� will trend to be zero with the iterations.

2) Updating of the particles' positions and velocities: The updating of the s-th particle's position is controlled by the locally optimal position of itself, i.e., p(q)
s,best, and the globally optimal position among all the particles, i.e., p(q)
best, which are evaluated by using the fitness function (9). According to [8], the velocity and position of the s-th particle are updated based on (11) and (12), which are given by

v(q+1) s = ωv(q) s + c1r2(p(q) s,best − p(q) s ) + c2r3(p(q) best − p(q) s ), s = 1, . . . , S, (11) p(q+1) s = p(q) s + v(q+1) s , s = 1, . . . , S, (12)
where ω is the inertia weight parameter, c1 and c2 are the step size factors, r2 and r3 are random parameters and uniformly generated from [0, 1]. If the updated positions violate the constraint C3, the following operation will be implemented as [8]

$$z_{s,k}^{(q)}=\begin{cases}z_{\min},&\text{if}\quad z_{s,k}^{(q)}<z_{\min},\\ z_{\max},&\text{if}\quad z_{s,k}^{(q)}>z_{\max},\\ z_{s,k}^{(q)},&\text{otherwise},\end{cases}\tag{13}$$

where $z_{s,k}^{(q)}\in\{x_{s,k}^{(q)},y_{s,k}^{(q)}\}$. The update of the particles' positions and velocities is presented in step 6 of Algorithm 1.

_3) Updating of the globally optimal position_: To avoid the solution space shrinking and the deterioration of solution accuracy suffered by the traditional PSO method, the SA method is adopted here, based on which a worse solution than the current one may be accepted with the probability $\epsilon$. This operation can prevent the solving process from being limited to the region of locally optimal solutions. It is known that an appropriate setting of $\epsilon$ is important for convergence performance and solution accuracy. According to [11], $\epsilon$ can be updated as

$$\epsilon=\exp\left(\frac{\mathcal{F}(\mathbf{w}^{*},\mathbf{p}_{\text{best}}^{(q)})-\mathcal{F}(\mathbf{w}^{*},\mathbf{p}_{\text{best}}^{(q+1)})}{T^{(q)}}\right),\tag{14}$$
where T (q) is the system temperature in the q-th iteration and updated as T (q+1) =
Q−q Q T (q), where Q is the maximum number of iterations for the SA-PSO method. It is known that the setting of T (0) is empirically. This update of the globally optimal position is shown in steps 13-23 of Algorithm
1. Specifically, in step 13, we sort p(q+1)
s for s = 1, . . . , S
in the decreasing order in terms of its corresponding fitness function F(w∗, p(q+1)
s
). From steps 16-20, the decision of whether accepting a worse solution than the current one is made. p(q+1)
̟
defined in step 17 of Algorithm 1 represents the
̟-th particle in the (q + 1)-th iteration, and ̟ is randomly generated from the region [0, q + 1].

## C. The Proposed Ao Algorithm For Solving P1

  In this subsection, we summarize the solving process of
P1 in Algorithm 2 based on the descriptions in Section III-A
and III-B. The computational complexity of Algorithm 2 is
O(A1SQ + A1A2K4.5 log( 1

                             ˆǫ)), where A1 is the iteration
number of implementing the AO framework, A2 is the iteration
number of implementing the SCA method for P2.2, and ˆǫ
is the computational accuracy required for implementing the
interior-point method. It is noted that the proposed algorithm
with the PSO can also be used to solve P1, the complexity
of which is approximately as O(A1SQ + A1A2K4.5 log( 1

                                                           ˆǫ)).
The performance comparison between the proposed scheme
with the two algorithms will be conducted in Section IV.

## Iv. Numerical Results

In this section, numerical results are conducted to evaluate the performance of the proposed MA empowered scheme with the SA-PSO. We consider a two-dimensional topology, in which the locations of the BD and the PU are set at
(30 m, 40 m) and (ˆξ, 0), respectively, and ˆξ is uniformly generated between 30 m and 60 m. The moving region for MAs at the PT is considered as a square area of size

## Algorithm 1 The Sa-Pso Based Method For Solving P3

1: Initialization: Positions P(q), velocities V(q), the iteration
index q = 0, the maximum iteration number Q, the system
temperature T (q).
2: Calculate F(w∗, p(q)
s ) based on (9).
3: Let
p(q)
s,best
=
p(q)
s
and
p(q)
best
=
arg max{F(w∗, p(q)
1 ), . . . , F(w∗, p(q)
S )}.
4: while q < Q do
5:
for s = 1 : S do
6:
Update v(q+1)
s
based on (11), and update p(q+1)
s
based on (12) and (13).
7:
if F(w∗, p(q+1)
s
) > F(w∗, p(q)
s,best) then
8:
Let p(q+1)
s,best = p(q+1)
s
.
9:
else
10:
Let p(q+1)
s,best = p(q)
s,best.
11:
end if
12:
end for
13:
Sort p(q+1)
s
for s
=
1, . . . , S in the decreasing
order in terms of its corresponding fitness function
F(w∗, p(q+1)
s
), and let ptemp = p(q+1)
1
.
14:
if F(ptemp) < F(p(q)
best) then
15:
Update ǫ based on (14).
16:
if ǫ > rand(0, 1) then
17:
Update p(q+1)
best
by letting p(q+1)
best
= p(q+1)
̟
.
18:
else
19:
p(q+1)
best
= p(q)
best.
20:
end if
21:
else
22:
p(q+1)
best
= ptemp.
23:
end if
24:
q = q + 1.
25: end while
26: Return p.

## Algorithm 2 The Ao Algorithm For Solving P1

1: Initialization: The MAs' positions p(0), the AO iteration
index ξ = 0, the convergence tolerance ˆ̺.
2: repeat
3:
ξ = ξ + 1.
4:
Initialization: the SCA iteration index ς
= 0, the
transmit beamforming matrix W (ς).
5:
repeat
6:
ς = ς + 1.
7:
Update W (ς) by solving P2.2.
8:
until | ˜R(ς)
p
− ˜R(ς−1)
p
| ≤ ˆ̺.
9:
Obtain w(ξ) by implementing the singular value decomposition of W (ς).
10:
Update p(ξ) by implementing Algorithm 1.
11: until |R(ξ)
p
− R(ξ−1)
p
| ≤ ˆ̺.
12: Return w and p.
$\begin{bmatrix}[-\frac{A}{2},\frac{A}{2}]\:\times\:[-\frac{A}{2},\frac{A}{2}]\\ A\:=\:3\lambda\:\:\text{and}\:\:\lambda\end{bmatrix}$ $[-\frac{A}{2},\frac{A}{2}]\times[-\frac{A}{2},\frac{A}{2}]$ at the center of (0 m, 0 m), where $A=3\lambda$, and $\lambda$ is the carrier wavelength and set at 0.1 m. The amount of transmit/receives paths is set to be the same, i.e., $L_{p}^{t}=L_{s}^{t}=L_{\kappa}^{r}=L$[7]. The path-response matrices $\mathbf{\Sigma}_{\kappa}$ and $\mathbf{\Sigma}_{s}$ can be expressed as $\mathrm{diag}\{[\widehat{n}_{\kappa,1},\ldots,\widehat{n}_{\kappa,L}]\}$ and $\mathrm{diag}\{[\widehat{n}_{s,1},\ldots,\widehat{n}_{s,L}]\}$, respectively, where $\widehat{n}_{\kappa,7}$ and $\widehat{n}_{s,7}$ are the corresponding complex responses of the 7-th path for $\overline{l}=1,\ldots,L$ and satisfy $\mathcal{CN}(0,v\cdot d^{-\nu}/L)$. $v$ denotes the path-loss, $d$ represents the distance between two nodes, and $\nu$ is the pass-loss exponent. The AoAs and AoDs are uniformly generated from $[-\frac{\pi}{2},\frac{\pi}{2}]$. The remaining parameters are set as follows: $P_{\mathrm{max}}=38$ dBm, $\alpha=0.8$, $d_{\mathrm{min}}=0.5\lambda$, $v=-10$
2 ]. The remaining parameters are set as follows: Pmax = 38 dBm, α = 0.8, dmin = 0.5λ, υ = −10
dB, ν = 1.8, L = 9, Q = 150, S = 150, c1 = c2 = 1.4,
ω = 1.2, r1 = 50, σ2 = 10−8, and ˆ̺ = 10−2. For performance comparison, the proposed MA empowered scheme with the PSO, the FA empowered scheme and the random transmit beamforming scheme are exploited.

Fig. 2 investigates the variance of the primary rate versus the maximum transmit power. It is obvious that increasing the maximum transmit power results in the improvement of the primary rates for all schemes. As indicated in Fig. 2, the proposed scheme with the SA-PSO can achieve a higher primary rate than the proposed scheme with the PSO, which confirms that the modification on the PSO method by utilizing the SA can guarantee a satisfactory solution space and thus find a solution with better accuracy. Compared to the FA empowered scheme, the utilization of MAs at the PT can ensure better system performance. It is because moving the antenna positions can create favorable channel conditions between the PT and the PU and between the PT and the BD.

Fig. 3 shows how the number of transmit/receive paths affects the primary rate. It is seen that the existence of more paths has a positive effect on the improvement of the primary rate. This is due to the fact that more paths can ensure a greater multi-path gain, thereby enhancing the smallscale fading. From Fig. 3, we also find that optimizing the transmit beamforming is a significant factor affecting the primary rate. For example, compared to the FA empowered scheme, the random beamforming scheme even results in a
21.8% performance loss with L = 3. It is because without the beamforming design, the transmitted signal from the PT will not beam towards the PU and the BD, thereby reducing the received signal power at the PU.

Fig. 4 depicts the primary rate versus the number of antennas. By deploying more antennas at the PT, the primary rates of all schemes increase since an improved spatial diversity gain can be achieved. Similar to Figs. 2 and 3, our proposed scheme with the SA-PSO outperforms the benchmarks, which again demonstrates the effectiveness of utilizing the MA technology and the SA-PSO method to ensure favorable channel conditions.

Fig. 5 presents the position variation of a selected antenna versus the AO iterations. As shown in Fig. 5, the updating paths of the selected antenna for the SA-PSO and PSO are much different. Obviously, the SA-PSO method can provide a larger solution space for updating the antenna position. Moreover, we can find that the AO framework can converge after only five iterations. This observation indicates the superior convergence performance of the proposed algorithm.

## V. Conclusion

In this paper, we have proposed an MA empowered scheme to create favorable channel conditions to boost the transmission efficiency of SR communication systems. To optimize the primary transmission rate under the BER constraint on the secondary transmission, we have proposed an AO framework to iteratively optimize the transmit beamforming by using the SCA and SDP methods and optimize the positions of MAs by using the SA-PSO method. Finally, we have conducted numerical results to demonstrate the effectiveness of the proposed MA empowered scheme with the SA-PSO.

From numerical results, we have derived the the following observations: 1) the flexible positions of antennas at the PT can provide a higher spatical diversity for both primary and secondary transmissions; 2) creating a multi-path environment has a positive effect on system performance.

## References

[1] Y.-C. Liang, Q. Zhang, E. G. Larsson, and G. Y. Li, "Symbiotic radio:
Cognitive backscattering communications for future wireless networks,"
IEEE Trans. Cogn. Commun. and Netw., vol. 6, no. 4, pp. 1242-1255,
Dec. 2020.
[2] R. Long, Y.-C. Liang, H. Guo, G. Yang, and R. Zhang, "Symbiotic radio:
A new communication paradigm for passive Internet of Things," IEEE
Internet Things J., vol. 7, no. 2, pp. 1350-1363, Feb. 2020.
[3] Q. Zhang, Y.-C. Liang, H.-C. Yang, and H. V. Poor, "Mutualistic
mechanism in symbiotic radios: When can the primary and secondary
transmissions be mutually beneficial?," *IEEE Trans. Wireless Commun.*,
vol. 21, no. 10, pp. 8036-8050, Oct. 2022.
[4] Z. Chu, W. Hao, P. Xiao, M. Khalily, and R. Tafazolli, "Resource
allocations for symbiotic radio with finite blocklength backscatter link,"
IEEE Internet Things J., vol. 7, no. 9, pp. 8192-8207, Sep. 2020.
[5] Z. Dai, R. Li, J. Xu, Y. Zeng, and S. Jin, "Rate-region characterization
and channel estimation for cell-free symbiotic radio communications,"
IEEE Trans. Commun., vol. 71, no. 2, pp. 674-687, Feb. 2023.
[6] L. Zhu, W. Ma, and R. Zhang, "Movable antennas for wireless communication: Opportunities and challenges," *IEEE Commun. Mag.*, doi:
10.1109/MCOM.001.2300212, 2023.
[7] W. Ma, L. Zhu, and R. Zhang, "MIMO capacity characterization
for movable antenna systems," *IEEE Trans. Wireless Commun.*, doi:
10.1109/TWC.2023.3307696, 2023.
[8] Z.
Xiao,
X.
Pi,
L.
Zhu,
X.-G.
Xia,
and
R.
Zhang,
"Multiuser communications with movable-antenna base station: Joint antenna positioning, receive combining, and power control," [Online] https://arxiv.org/abs/2308.095122, 2023.
[9] M. Hua, Q. Wu, L. Yang, R. Schober, and H. V. Poor, "A novel
wireless communication paradigm for intelligent reflecting surface based
symbiotic radio systems," *IEEE Trans. Signal Process.*, vol. 70, pp. 550-
565, 2022.
[10] J. G. Proakis, *Digital Communication*. New York, NY, USA: McGraw-
Hill, 1995.
[11] Z. Yu, Z. Si, X. Li, D. Wang, and H. Song, "A novel hybrid particle
swarm optimization algorithm for path planning of UAVs," IEEE Internet Things J., vol. 9, no. 22, pp. 22547-22558, Nov. 2022.
[12] B. Lyu, C. Zhou, S. Gong, D. T. Hoang, and Y. -C. Liang,
"Robust secure transmission for active RIS enabled symbiotic radio multicast communications," *IEEE Trans. Wireless Commun.*, doi:
10.1109/TWC.2023.3265770, 2023.
[13] Y.-C. Liang, Q. Zhang, J. Wang, R. Long, H. Zhou, and G. Yang,
"Backscatter communication assisted by reconfigurable intelligent surfaces," *Proc. IEEE.*, vol. 110, no. 9, pp. 1339-1357, Sep. 2022.
[14] Q. Zhang, Y.-C. Liang, and H. V. Poor, "Reconfigurable intelligent surface assisted MIMO symbiotic radio networks," *IEEE Trans. Commun.*,
vol. 69, no. 7, pp. 4832-4846, Jul. 2021.