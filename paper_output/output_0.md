# Bistatic Doppler Frequency Estimation With Asynchronous Moving Devices For Integrated Sensing And Communications

Gianmaria Ventura†, *Graduate Student Member, IEEE*, Zaman Bhalli†, *Graduate Student Member, IEEE*, Michele Rossi†∗ *Senior Member, IEEE*, Jacopo Pegoraro†, Member, IEEE

  Abstract—In this letter, we present for the first time a method
to estimate the bistatic Doppler frequency of a target with clock
asynchronous and mobile Integrated Sensing And Communication
(ISAC) devices. Existing approaches have separately tackled
the presence of phase offsets due to clock asynchrony or the
additional Doppler shift due to device movement. However,
in real ISAC scenarios, these two sources of phase nuisance
are concurrently present, making the estimation of the target's
Doppler frequency particularly challenging. Our method solves
the problem using the sole wireless signal at the receiver, by
computing Channel Impulse Response (CIR) phase differences
across different multipath components and subsequent time
instants. In this way, we cancel out phase offsets. Then, we
construct a system of equations that allows disentangling the
target's Doppler frequency from that of the moving device. The
proposed method is validated via simulation, exploring the impact
of different system parameters. Numerical results show that our
approach is a viable way of estimating Doppler frequency in
bistatic asynchronous ISAC scenarios with mobile devices.

  Index Terms—Integrated sensing and communication, clock
asynchrony, bistatic sensing, mobile devices, Doppler frequency.

## I. Introduction

Integrated Sensing And Communication (ISAC) has been identified as a prominent feature of next-generation wireless networks, endowing them with perception capabilities by exploiting the radar principle [1]. Among the objectives of ISAC systems, estimating the Doppler frequency caused by targets of interest is of key importance. It enables several applications such as movement speed estimation, enhanced resolution in target detection and tracking, target recognition, and human sensing for remote healthcare [2], [3].

In bistatic ISAC, where the transmitter (TX) and receiver
(RX) are spatially separated, the main challenge is the timevarying relative drift between their clocks, which is referred to as *asynchronism*. Clock asynchronism causes Timing Offset
(TO), Carrier Frequency Offset (CFO), and a random Phase Offset (PO) across different transmissions. Such offsets hinder coherent processing of the channel measurements across time, introducing errors in the estimate of the target's parameters, including the Doppler frequency [4]. Moreover, in real ISAC deployments, an additional Doppler frequency shift is caused by the movement of the TX or RX device, which are usually considered to be static in the ISAC literature. While CFO is the same for all propagation paths [5], but changes quickly over time, the device movement evolves slowly but causes a Engineering.

different frequency shift on each propagation path. This makes the combination of Doppler shift due to device movement and CFO particularly challenging to compensate for. Existing solutions have either focused on *moving* monostatic radar systems, which are not affected by CFO and PO [6], or have tackled asynchronous ISAC systems with *static* devices [5],
[7]–[9]. Hence, a key limitation of all these approaches is that they do not work in realistic scenarios where ISAC devices are both asynchronous *and* mobile. In this setting, the Doppler shift due to the movement of devices adds up to the CFO, and it is hard to disentangle from the target's Doppler frequency.

In this letter, we propose the first approach to estimate the Doppler frequency of a target in bistatic ISAC with asynchronous mobile devices using the sole wireless signal. The key challenge we solve is the superposition of (i) the target Doppler frequency, (ii) the TX or RX Doppler frequency, and (iii) the CFO and PO, where (ii) and (iii) act as a nuisance that hinders the estimation of the target Doppler. The proposed algorithm obtains phase measurements from different multipath reflections in the Channel Impulse Response (CIR) across time. Then, it removes phase offsets by computing phase differences between each path and the Line-of-Sight (LoS) path, leveraging the fact that phase offsets are constant for all propagation paths. In a second step, time-domain phase differences for each propagation path are obtained and used to construct a non-linear system with one equation per multipath component. Different multipath components are affected by the TX or RX motion in different ways, depending on the path geometry. We exploit this as a source of *diversity* to reduce the number of system variables. As a result, the system is solvable if at least 2 multipath components from static scatterers are available. In this case, the target Doppler frequency can be estimated and refined by aggregating results over a short processing window.

The main contributions of this letter are: 1) We propose the first solution to the problem of estimating the Doppler frequency of a target in bistatic ISAC systems with mobile asynchronous devices, affected by CFO and PO.

2) Our solution is based on an original approach that processes CIR phase measurements across multipath components and subsequent time frames, removing the undesired phase offsets caused by asynchrony and TX or RX movement.

3) We validate the proposed algorithm via numerical simulation under different system configurations, showing that it provides a viable way to estimate Doppler frequency in realistic bistatic ISAC systems.

## Ii. System Model

In this section, we introduce our system model including the reference scenario, the CIR, and the phase measurements.

## A. Reference Scenario

We consider a 2D scenario including two ISAC devices, namely, a transmitter (TX) and a receiver (RX). The aim is to estimate the bistatic Doppler frequency caused by a moving target of interest, as shown in Fig. 1, by using the channel estimates obtained from the ongoing communication traffic. For simplicity, we assume that the TX is static while the RX moves with velocity vrx(t) with an angle η(t) with respect to the segment connecting the TX and the RX (LoS segment), where t is the continuous-time variable. The symmetric case where the TX moves and the RX is static leads to similar derivations, as discussed in Section II-B, and it is omitted. The received signal includes M(t) delayed, Dopplershifted, and attenuated copies of the transmitted one, where M(t) corresponds to the number of multipath components caused by scatterers in the environment. As commonly done in ISAC, we only consider first-order reflections since they have significantly higher received power than higher-order ones [10]. Denote by λ = *c/f*c the transmission wavelength, with c being the speed of light and fc the carrier frequency.

The movement of the m-th scatterer causes a bistatic Doppler shift fD,m(t). The RX movement causes a Doppler shift equal to f rx D,m(t) = (vrx(t) cos ξm(t))/λ, where ξm(t) is the angle between the elongation of the segment connecting the mth scatterer to the RX and the RX velocity vector. In our scenario, we consider that the M(t) propagation paths can be partitioned as follows: (i) a LoS path, which represents the direct propagation from the TX to the RX (assumed to be available), (ii) a single moving target path, (iii) S(t) static scatterers paths for which fD,m(t) = 0. We assume that the orientation of the RX with respect to the TX is known and it has been compensated for, e.g., by using onboard sensors like a gyroscope.

## B. Channel Model

Consider the continuous-time channel between the TX and the RX and denote by τm(t), αm(t), and Am(t) the propagation delay, the Angle of Arrival (AoA), and the complex coefficient of the m-th path, respectively. Am(t) accounts for the propagation loss and the complex target reflectivity, hence it contains a phase term that depends on the path.

The TO, CFO, and random PO are denoted by τo(t), fo(t), and ψo(t), respectively. Denoting the Dirac delta function by δτ, the CIR at time t and delay τ is

$$h(t,\tau)=e^{j\psi_{\rm o}(t)}\sum_{m=1}^{M(t)}A_{m}(t)e^{j\vartheta_{m}(t)}\delta_{\tau-\tau_{m}(t)-\tau_{\rm o}(t)},\tag{1}$$

with $\vartheta_{m}(t)=2\pi(f_{\rm D,m}(t)+f_{\rm o}(t)+f_{\rm D,m}^{\rm x}(t))t$. Note that $f_{\rm D,m}(t)$ is summed to the CFO and the Doppler shift introduced by the receiver, which act as a nuisance.

In Single Carrier (SC) systems, e.g. IEEE 802.11ay, the RX estimates the CIR directly using cross-correlation of the received signal with a known pilot sequence. In Orthogonal Frequency Division Multiplexing (OFDM) systems, it can obtain the CIR via Inverse Discrete Fourier Transform (IDFT) from an estimate of the Channel Frequency Response (CFR).

The CIR estimation is repeated across multiple frames, indexed by k, with period T. Using a common assumption in ISAC and radar processing, we consider a short processing window of K frames [10], where the parameters, M(t), τm(t), fD,m(t), αm(t), Am(t), η(t), ξm(t), vrx(t), and consequently the RX motion-induced Doppler shift f rx D,m(t) can be considered constant. Conversely, all the nuisance parameters, τo(t), fo(t), ψo(t), are time-varying within the window.

The estimated discrete-time CIR at time kT with k =
0*, . . . , K* − 1 is

$$h[k,l]=e^{j\psi_{\rm o}(kT)}\sum_{m=1}^{M}A_{m}e^{j\vartheta_{\rm o}[m]}\chi[l-\tau_{m}-\tau_{\rm o}(kT)],\tag{2}$$

where $\vartheta_{m}[k]=2\pi(f_{\rm D,}m+f_{\rm o}(kT)+f_{\rm D,}^{\rm x}m)kT$, $l$ is the discrete delay index, and $M$ is the number of resolvable paths within the window, with $M\leq M(t)$. In Eq. (2), $\chi[l]$ replaces the Dirac delta function to account for non-ideal autocorrelation of the pilot sequence (in single carrier systems) or the impact of the finite-length CFR estimate (in OFDM systems). In the following, we focus on estimating the target Doppler frequency under the nuisance due to the CFO, PO, and the RX motion. Hence, we assume that the RX can detect and separate the $M$ multipath components and extract their phase across time. To this end, the TO can be compensated for by obtaining _relative_ delay measurements with respect to the LoS, as done in [5].

Our model is agnostic to the number of available antennas at the RX. Multiple antennas could be used to estimate the AoAs of the different multipath components, which are needed in our processing pipeline. However, our system works even for analog beamforming-based receivers, with a single Radio Frequency (RF) chain, that estimate the AoAs using other techniques, such as that in [5].

## C. Phase Measurements

In this section, we model the phase of each multipath component in the CIR. We consider the phase measurements to be affected by Gaussian noise w[k] ∼ N(0, σ2
ϕ), where σ2
ϕ
is the noise variance. To simplify the equations, we group the phase nuisance terms, which are the same on all propagation paths, into Ψo(kT) = ψo(kT) + 2πfo(kT)kT. Moreover, we use subscripts ·LoS and ·t to refer to quantities related to the LoS and to the target-induced paths, respectively, as shown in Fig. 1. For the paths caused by static scatterers, we use index s = 1*, . . . , S*, where S is the number of

resolvable static scatterers detected in the processing window, with $S=M-2$. The phase of the LoS component is

$$\phi_{\rm LoS}[k]=\Psi_{\rm o}(kT)+\angle A_{\rm LoS}+2\pi kT\left(\frac{v^{\rm rx}}{\lambda}\cos\eta\right)+w_{\rm LoS}[k],\tag{3}$$

where $\angle\cdot$ is the phase operator. The phase of the target-induced path is affected by both the Doppler shift caused by the target, $f_{\rm D,t}$, and by the receiver motion as

$$\phi_{\rm t}[k]=\Psi_{\rm o}(kT)+\angle A_{\rm t}+2\pi kT\left(f_{\rm D,t}+\frac{v^{\rm rx}}{\lambda}\cos\xi_{\rm t}\right)+w_{\rm t}[k],\tag{4}$$

where $\xi_{\rm t}$ is the angle between the elongation of the segment connecting the target to the RX and the RX velocity vector. The phase of the $s$-th static multipath component is

$$\phi_{s}[k]=\Psi_{\rm o}(kT)+\angle A_{s}+2\pi kT\left(\frac{v^{\rm rx}}{\lambda}\cos\xi_{s}\right)+w_{s}[k].\tag{5}$$

From the CIR, the RX measures $\texttt{modd}_{2\pi}(\phi_{i}[k])$ where $i\in\{\rm t,LoS,s\}$, $k=0,\ldots,K-1$, and $\texttt{modd}_{2\pi}(\cdot)$ is the modulo $2\pi$ division, whose result is in $[0,2\pi]$.

## Iii. Methodology

In this section, we present our approach for estimating the bistatic Doppler frequency of the target from the phase measurements in Eqs. (3-5). It can be summarized as follows.

A. CFO and PO cancellation. By subtracting the phase of the LoS path from the other phase measurements we cancel out the nuisance component Ψo, without estimating it directly.

This is further detailed in Section III-A.

B. Time-domain phase differencing. By computing timedomain phase differences *for each path*, we cancel out the path-specific phase terms
̸ Ai, with i *∈ {*t, LoS, s}, as detailed in Section III-B. This yields phase differences whose value depends on the Doppler shifts of the RX and the target.

C. AoA-based simplification. By leveraging AoA estimation at the RX and the multipath geometry, we make a key simplification in the phase measurements model (see Section III-C). This allows reducing the number of unknowns, making the estimation of the target Doppler frequency feasible if at least 2 static multipath components are detected.

D. Doppler frequency estimation. We formulate the estimation of the target's Doppler frequency as a Nonlinear Least- Squares (NLS) problem across the multipath components (see Section III-D). A closed-form solution using S = 2 static paths is provided next to initialize the NLS problem.

## A. Cfo And Po Cancellation

We subtract $\phi_{\rm LoS}[k]$ from $\phi_{\rm t}[k]$ and $\phi_{s}[k]$, obtaining

$$\tilde{\phi}_{\rm t}[k]=\Omega_{\rm t}+2\pi kT\left(f_{\rm D,t}+\frac{v^{\rm rx}}{\lambda}\left(\cos\xi_{\rm t}-\cos\eta\right)\right)+w^{\prime}_{\rm t}[k],\tag{6}$$

$$\tilde{\phi}_{s}[k]=\Omega_{s}+2\pi kT\left(\frac{v^{\rm rx}}{\lambda}\left(\cos\xi_{s}-\cos\eta\right)\right)+w^{\prime}_{s}[k],\tag{7}$$

where $\Omega_{s}=\angle A_{s}-\angle A_{\rm LoS},\Omega_{\rm t}=\angle A_{\rm t}-\angle A_{\rm LoS}$, and $w^{\prime}_{i}[k]=w_{i}[k]-w_{\rm LoS}[k],i\in\{t,s\}$ is distributed as ${\cal N}(0,2\sigma_{\phi}^{2})$.

Computing phase differences *cancels out* CFO and PO without estimating them, since they are common to all propagation paths. Despite the absence of CFO and PO in Eq. (6), the estimation of the target's Doppler frequency remains nontrivial due to the presence of the undesired frequency term vrx (cos ξt − cos η) /λ caused by the receiver movement. Indeed, a direct application of standard Fourier-based processing to estimate the Doppler frequency would fail to separate fD,t from the Doppler due to the RX movement.

## B. Time-Domain Phase Differencing

After CFO and PO cancellation, the RX computes first-order, time-domain phase differences as $\Delta_{i}[k]=\texttt{mod}_{2\pi}\big{(}\tilde{\phi}_{i}[k]\big{)}-\texttt{mod}_{2\pi}\big{(}\tilde{\phi}_{i}[k-1]\big{)}$ with $i\in\{\texttt{t},s\}$ and $k=1,\ldots,K-1$. The phase differences are expressed as

$$\Delta_{\texttt{t}}[k]=2\pi T\left(f_{\texttt{D},\texttt{t}}+\frac{v^{\texttt{rx}}}{\lambda}\left(\cos\xi_{\texttt{t}}-\cos\eta\right)\right)+w_{\texttt{t}}^{\prime\prime}[k],\tag{8}$$ $$\Delta_{s}[k]=2\pi T\left(\frac{v^{\texttt{rx}}}{\lambda}\left(\cos\xi_{s}-\cos\eta\right)\right)+w_{s}^{\prime\prime}[k],\tag{9}$$

where $w_{i}^{\prime\prime}[k]=w_{i}^{\prime}[k]-w_{i}^{\prime}[k-1],i\in\{\texttt{t},s\}$ is a Gaussian noise term with zero mean and variance $4\sigma_{\phi}^{2}$.

In Eq. (8) and Eq. (9), we assume that the channel estimation period $T$ is sufficiently small, so that the phase change between two subsequent frames is smaller than $\pi$. This allows writing phase differences without the ambiguity due to the mode$\texttt{l}_{2\pi}$ operator. From Eq. (8), it can be seen that the noise-free phase differences $\Delta_{\texttt{t}}$ and $\Delta_{s}$ are upper bounded by $2\pi T(3f_{\texttt{max}})$, with $i\in\{\texttt{t},s\}$ and $f_{\texttt{max}}$ being the maximum Doppler shift caused by the RX (or the target). $f_{\texttt{max}}$ is a system design parameter that can be set depending on the specific scenario and application. To fulfill the assumption, it is sufficient to impose $|\Delta_{i}|<\pi$ which yields $T<1/(6f_{\texttt{max}})$. The choice of $T$ is further discussed in Section IV.

## C. Aoa-Based Simplification

By inspecting Fig. 1, a key simplification can be made in Eq. (8) and Eq. (9) noticing that

$$\cos\xi_{i}=\cos\left(\eta-\alpha_{i}\right)=\cos\left(\alpha_{i}-\eta\right),\tag{10}$$

with $i\in\left\{\mathrm{t},s\right\}$. This substitution removes the dependency on the unknown and path-dependent angle $\xi_{i}$. The new dependency on $\alpha_{i}-\eta$ is easier to handle since the RX estimates $\alpha_{i}$ and the unknown term $\eta$ is independent of the propagation paths. Note that, since $\alpha_{s}$ and $\alpha_{\mathrm{t}}$ are estimated by the RX, this operation reduces the unknowns from $S+4$, i.e., $f_{\mathrm{D,t}},v^{\mathrm{rx}},\eta,\xi_{\mathrm{t}},\xi_{1},\ldots,\xi_{S}$, to just 3, i.e. $f_{\mathrm{D,t}},v^{\mathrm{rx}},\eta$. This makes Eq. (8) and Eq. (9), for $s=1,\ldots,S$, a set of $S+1$ equations with 3 unknowns, which can be solved if the number of static multipath components satisfies $S\geq2$. In the next section, we provide our solution based on NLS.

## D. Doppler Frequency Estimation

We reformulate Eq. (8) and Eq. (9) in vector notation by introducing: the phase differences vector at time kT,
∆[k] = [∆t[k], ∆1[k]*, . . . ,* ∆S[k]]⊤, the unknown parameter

vector θ = [fD,t, η, vrx]⊤, the non-linear vector function g(θ),
which expresses the non-linear relations in Eq. (8) and Eq. (9).
The following model holds ∆[k] = g(θ) + w[k], where
w[k] ∼ N(0, 4σ2
                  ϕI) is the noise vector with components
w′′
 i [k], i ∈ {t, 1, . . . , S}. To reduce the impact of noise, we
average the measured phase differences over time obtaining
¯∆ = �K−1
        k=1 ∆[k]/(K − 1).
  1) Nonlinear least-squares solution: An NLS problem is
solved to retrieve an estimate of the unknown parameters

arg min θ || ¯∆ − g(θ)||2 2, (11)
from which we get the Doppler frequency estimate as the first component of the solution, which we denote by ˆfD,t. This problem can be solved using, e.g., the Levenberg-Marquardt algorithm with a suitable initialization [11].

2) Closed form solution: A closed-form solution using 3
multipath components is used to initialize the NLS. Consider Eq. (9) with 2 phase measurements from static paths, i.e., s = 1, 2. Using also Eq. (8), a system with 3 equations in
3 unknowns is attained, which can be solved for θ. Denoting by ¯∆t, ¯∆1, and ¯∆2 the time-averaged phase differences for the sensing path, and static paths 1 and 2, respectively, we compute

� . (12) ˜η = arctan � ¯∆2(cos α1 − 1) − ¯∆1(cos α2 − 1) ¯∆1 sin α2 − ¯∆2 sin α1
Then, ˆη is obtained as ˆη = mod2π(˜η) if the argument of the arctan is positive and ˆη = mod2π(˜η + π) otherwise. Eventually the expression of ˆfD,t is

ˆfD,t = 1 2πT � . (13) � ¯∆t − ¯∆1 cos(αt − ˆη) − cos ˆη cos(α1 − ˆη) − cos ˆη
The solution requires the following conditions to be met:
(i) αi ̸= 0, i *∈ {*1, 2, t}, (ii) αi ̸= αℓ, i ̸= ℓ *∈ {*1, 2, t}, and
(iii) αi ̸= 2ˆη, i *∈ {*1, 2}. Note that violating conditions (i) and
(ii) correspond to degenerate scenarios in which the LoS path is not available, or two static multipath components have the same AoA. Condition (iii) instead is violated if the AoA of one of the multipath components is equal to 2ˆη.

## Iv. Numerical Results

In this section, we present our simulation environment and numerical results.

## A. Simulation Setup

To validate the solution presented in Section III-D we perform simulations for 28 GHz and 60 GHz carrier frequencies, representing, e.g., Frequency Range 2 (FR2) 5G-NR and IEEE 802.11ay systems, respectively. We generate realistic values of fD,t, Ψo[k], vrx, αs, αt, and η considering low to moderate movement velocities for both the target and the RX. Furthermore, we set a minimum Doppler frequency for the target, fmin, below which we consider it to be static.

All parameters are summarized in Tab. 1. In addition, we set T = 1/(6fmax) = 0.08 ms to avoid phase ambiguity as discussed in Section III-B. We perform 104 simulations for each set of parameters.

4 , π
Target Doppler frequency [Hz]
fD,t
±U(fmin, fmax)
LoS-RX velocity angle [rad]
η
U(0, 2π)
Receiver velocity [m/s]
vrx
U(0, vmax)
Angle-of-Arrival [rad]
αm
U
�
− π
4
�
Carrier wavelength [cm]
λ
{0.5, 1.07}
Max. RX/target velocity [m/s]
vmax
{5, 10}
Min. RX/target Doppler frequency [Hz]
fmin
{40, 18}
Max. RX/target Doppler frequency [kHz]
fmax
{2, 1.9}
CFO time difference stand. dev. [Hz]
σo
{481, 225}

  The CFO is modeled as a Gaussian random walk fo(kT) =
fo((k − 1)T) + wo(kT), where fo(0), wo(kT) ∼ N(0, σ2
                                                     o).
σ2
 o is chosen such that the frequency shift in 1 ms is between
±1 parts-per-million (ppm) of the carrier frequency. We model
the PO as ψo(kT) ∼ N(0, σ2
                          o). Note that, since our method
cancels out the CFO and PO without estimating them, the
estimation accuracy is independent of their magnitude. The
CIR phases, ϕi[k], are computed using Eqs. (3-5). The error
variance on the phase measurements, σ2
                                   ϕ, is varied to evaluate
its impact on the estimation, as discussed in the next section.
The error on the AoA estimates is modeled as an additive
Gaussian noise with zero mean and variance σ2
                                          α.

## B. Doppler Frequency Estimation Performance

We evaluate the performance of our Doppler frequency estimation algorithm in terms of normalized absolute estimation error, defined as εfD,t = |fD,t − ˆfD,t|/|fD,t|.

1) Number of static scatterers: The number of available static scatterers, S, is key in determining the performance of the algorithm. As detailed in Section III-D1, the target Doppler frequency can be estimated as long as at least 2
static scatterers are resolved at the RX. In Fig. 2a, we show that the estimation error is significantly reduced if more static scatterers are available. The median error lies below 5% of the actual Doppler frequency even with S = 2. Increasing S improves the median error and reduces the spread of the error distribution. This is because each scatterer adds one equation to the NLS problem in Eq. (11) without increasing the number of unknowns, leading to a more robust solution.

2) Processing window duration: In Fig. 2b, we evaluate the impact of averaging phase measurements over a longer processing window. A longer aggregation time clearly improves robustness to noise. However, our assumption is that the sensing parameters of the multipath reflections remain constant in the processing window. Hence, the window duration can not be increased arbitrarily but has to be tuned depending on the dynamicity of the multipath environment. As an example, for indoor human sensing applications, the movement velocities involved could be considered constant up to a few tens of milliseconds. In this case, our method provides a median error of about 3% of the true Doppler frequency.

3) Measurements error: In Fig. 2c, we show the Doppler frequency estimation error depending on the noise affecting phase (σϕ), and AoA measurements (σα). Note that the phase measurements error depends on the Signal-to-Noise Ratio (SNR) of the received signal as shown in [5]. For high noise variance in the measurements, the estimation becomes noisy, despite the low median normalized error of 0.06. This is due to the required trade-off in the choice of the CIR measurement interval T, which is discussed in the next section.

Fig. 2c also shows that the Doppler frequency estimate is not significantly affected by the AoA error, which means the phase measurements error has a much stronger impact.

4) CIR measurement interval analysis: As discussed in Section III-B, T has to be sufficiently small so as to avoid ambiguity in the phase measurements, i.e., the maximum phase shift across subsequent frames should not exceed π.

However, small values of T make the estimation of the Doppler frequency more sensitive to noise due to the structure of Eq. (13). We analyze the impact of increasing T in Fig. 3, showing the average Doppler frequency estimation error, ¯εfD,t, and its standard deviation, for different values of the number of static multipath components, S. Thanks to the robustness of the NLS formulation in Eq. (11), our method tolerates increasing T slightly above the maximum value needed to avoid ambiguity, which even yields lower estimation error due to the lower sensitivity to noise. However, further increasing T causes phase ambiguity to occur more often, consequently degrading the system's performance.

## V. Conclusion

In this letter, we proposed the first method to estimate the Doppler frequency of a target in an *asynchronous* ISAC system with *mobile* devices. Our approach can effectively disentangle the target's Doppler frequency from the CFO and the Doppler caused by the device movement. It does so by leveraging
(i) phase differences across multipath components, (ii) phase differences across time, and (iii) the multipath geometry. The Doppler frequency estimation is thus formulated as an NLS problem that can be solved as long as the LoS and at least 2
paths (reflections) from static scatterers are available.

Our simulation results show that the proposed method achieves accurate Doppler frequency estimation if the noise in the phase measurements is reasonably low, and it is robust to AoA estimation errors.

## References

[1] F. Liu, L. Zheng, Y. Cui, C. Masouros, A. P. Petropulu, H. Griffiths, and
Y. C. Eldar, "Seventy years of radar and communications: The road from separation to integration," *IEEE Signal Processing Magazine*, vol. 40,
no. 5, pp. 106–121, 2023.
[2] J. A. Zhang, M. L. Rahman, K. Wu, X. Huang, Y. J. Guo, S. Chen,
and J. Yuan, "Enabling joint communication and radar sensing in mobile networks—a survey," *IEEE Communications Surveys & Tutorials*, vol. 24, no. 1, pp. 306–345, 2021.
[3] A. Singh, S. U. Rehman, S. Yongchareon, and P. H. J. Chong, "Multi-
Resident Non-Contact Vital Sign Monitoring Using Radar: A Review," IEEE Sensors Journal, vol. 21, no. 4, pp. 4061–4084, 2021.
[4] J. A. Zhang, K. Wu, X. Huang, Y. J. Guo, D. Zhang, and R. W. Heath,
"Integration of radar sensing into communications with asynchronous transceivers," *IEEE Communications Magazine*, vol. 60, no. 11, pp. 106– 112, 2022.
[5] J. Pegoraro, J. O. Lacruz, T. Azzino, M. Mezzavilla, M. Rossi, J. Widmer, and S. Rangan, "JUMP: Joint communication and sensing with Unsynchronized transceivers Made Practical," IEEE Transactions on Wireless Communications, 2024.
[6] F. Zhang, J. Xiong, Z. Chang, J. Ma, and D. Zhang, "Mobi2Sense:
empowering wireless sensing with mobility," in Proceedings of the 28th Annual International Conference on Mobile Computing And Networking, ser. MobiCom '22.
New York, NY, USA: Association for Computing
Machinery, 2022, p. 268–281.
[7] J. Zhao, Z. Lu, J. A. Zhang, S. Dong, and S. Zhou, "Multiple-Target
Doppler Frequency Estimation in ISAC with Clock Asynchronism," IEEE Transactions on Vehicular Technology, vol. 73, no. 1, pp. 1382– 1387, 2024.
[8] F. Meneghello, D. Garlisi, N. Dal Fabbro, I. Tinnirello, and M. Rossi,
"SHARP: Environment and Person Independent Activity Recognition with Commodity IEEE 802.11 Access Points," IEEE Transactions on Mobile Computing, vol. 22, no. 10, pp. 6160–6175, 2023.
[9] K. Wu, J. Pegoraro, F. Meneghello, J. A. Zhang, J. O. Lacruz, J. Widmer,
F. Restuccia, M. Rossi, X. Huang, D. Zhang *et al.*, "Sensing in Bi-
Static ISAC Systems with Clock Asynchronism: A Signal Processing Perspective," *arXiv preprint arXiv:2402.09048*, 2024.
[10] J. A. Zhang, F. Liu, C. Masouros, R. W. Heath, Z. Feng, L. Zheng, and
A. Petropulu, "An overview of signal processing techniques for joint communication and radar sensing," IEEE Journal of Selected Topics in
Signal Processing, vol. 15, no. 6, pp. 1295–1315, 2021.
[11] J. Nocedal and S. Wright, *Numerical optimization*.
Springer Science
& Business Media, 2006.