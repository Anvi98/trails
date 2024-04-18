# Uplink Soft Handover For Leo Constellations: How Strong The Inter-Satellite Link Should Be

2nd Alberto Tarable CNR-IEIIT
Torino, Italy alberto.tarable@cnr.it
1st Houcem Ben Salem CNR-IEIIT
Torino, Italy houcem.bensalem@ieiit.cnr.it

  Abstract—We consider a constellation of low-earth-orbit (LEO)
satellites connected to a handheld device on the ground. Due
to the very large orbital speed, an effective handover strategy
becomes of paramount importance. In particular, we study the
benefits of soft handover in the uplink from the physical-layer
point of view. We give a realistic model for both the ground-to-
satellite and the inter-satellite links, following the 3GPP channel
model for the former. We suppose that, during handover from
a serving satellite to a target satellite, one of the two satellites
forwards the received signal from the ground user to the other,
thus acting as a relay. We quantify through simulations the loss
of hard handover, compared to soft handover. For the latter,
we test both amplify-and-forward (AF) and decode-and-forward
(DF) relaying techniques and verify that, at least in the simulated
conditions, DF does not repay, in terms of block error rate
(BLER), the increase of complexity with respect to AF. Also,
we study the effect of the LEO constellation size on the network
BLER. Finally, we show that, with soft handover, the impact of
misalignment on the inter-satellite link is severe, especially at
optical frequencies.
  Index Terms—Non-Terrestrial Networks, LEO constellations,
soft handover, Inter-Satellite Link

## I. Introduction

The integration of terrestrial and non-terrestrial networks
(NTNs) is foreseen as one of the key factors that will enable ubiquitous connectivity in future 6G networks [1], [2]. NTNs can also play a fundamental role in ensuring connectivity in cases where the terrestrial infrastructure is missing or indequate to support the requested traffic, such as in rural areas or in disaster scenarios. In particular, low-earth orbit (LEO)
NTNs have now become an important research subject, also fostered by the surge of privately-owned LEO constellations put into operations by several companies.

LEO NTNs offer smaller round-trip times (up to 30 ms)
compared to geostationary NTNs, but they present a number of challenges. Since a LEO satellite provides a limited coverage on the earth surface, several tens of satellites need to be employed in the same LEO, in order to ensure uninterrupted connectivity with static ground users (GU). Even more importantly, LEO satellites have a very short orbital period. As an example, a satellite having height 550 km above the earth surface performs a revolution in about 1.6 hours. Thus, a LEO satellite remains in visibility for a limited amount of time (a few minutes), so that there is need for frequent handover,
4th Behrooz Makki Ericsson EAB
G¨oteborg, Sweden behrooz.makki@ericsson.com
3rd Alessandro Nordio CNR-IEIIT
Torino, Italy alessandro.nordio@cnr.it even for a static GU [3]. In this regard, we can distinguish two different system-level choices. In the first method, each satellite steers its antenna array so as to point always to the same ground area, therefore the cells are earth-fixed. In the second method, the satellite array points to a fixed direction, so that the cells are earth-moving. In the first case, handover between different satellites has to be performed every few minutes. In the second case, handover events are much more frequent, once every few seconds [3]. In both scenarios, it is clear that handling effectively the handover is crucial to ensure a high-level quality of service.

In this paper, we consider the uplink (UL) of a satellite communication system where a GU initially communicates with a serving satellite S. In an ideal hard-handover scenario, the GU instantaneously switches to a target satellite T, when its elevation on the horizon becomes greater than that of S (for a more realistic protocol, see, e.g., [3]). Instead, in soft handover the GU signal is received by both S and T for a short period of time. Then, the lower-elevation satellite (which is first T, then S) acts as a relay, by forwarding its received signal to the higher-elevation one through the inter-satellite link (ISL). In the following, we are particularly interested in understanding the role of the ISL to help the handover. We study the block error rate (BLER) when amplify-and-forward (AF) and decode-and-forward (DF) relaying techniques are applied. We consider realistic models for ground-to-satellite
(G2S) and ISL channels, following the recent 3GPP model for the former. Also, we assess the advantage of soft handover with respect to hard handover, and we study the effect of the size of the satellite constellation and of the misalignment in the ISL on the performance of soft-handover-based LEO systems.

A paper dealing with soft handover in the UL is [4], which considers multipacket transmission on a highly time-dispersive channel. However, the ISL is assumed ideal, and the satellite performs linear minimum-mean square error filtering on the signals received from several GUs. A paper that performs multi-satellite reception (without reference to handover) is the recent [5]. In that context, the channel model defined in [6], [7] is used and imperfect channel state information is taken into account. Performance is measured in terms of achievable capacity. However, also in that case, the ISL is assumed ideal.

Differently from previous works, we precisely address the role of the ISL in the performance of soft handover. We perform evaluation of BLER by simulating a realistic environment in which the time evolution of satellite elevations is obtained by geometrical considerations, the G2S link is based on the 3GPP standard channel model defined in [6], [7], and the ISL
channel model is based on [8]. 1
We will address the following questions:

- What is the advantage of soft handover, compared to hard
handover?
- What is the best strategy the relaying satellite can adopt?
To answer this question, we will compare the performance of AF and DF relaying techniques.
- What is the impact of the constellation size?
- How severe is the impact of misalignment for an optical ISL? In this respect, is an ISL in the THz band more robust?

In the following, we partially answer such questions, by concluding that, with a proper choice of the soft-handover scheme, and with a suitable design of the ISL, the performance gain of soft handover over hard handover justifies the additional complexity related to its implementation.

## Ii. System Description

A. Geometrical Model We consider a set of M satellites deployed on a circular orbit, with height on the ground h0 and inclination iK with respect to the equatorial plane. Satellites are angularly spaced on the orbit by α0 = 2π/M radiants, as depicted in Figure 1.

According to Kepler's laws, the angular speed of each satellite is given by [10]

(RE + h0)3 [rad/s], (1) ω = � µ
where RE = 6371 km is the earth radius and µ = 3.986 ×
105 km3s−2 is the gravitational constant. Let us denote by ℓ
either the serving satellite, ℓ = S, or the target satellite, ℓ = T .

Let αℓ(t) = ωt + αℓ(0), ℓ ∈ {S, T}, be the angular position of satellite ℓ at time t. Without loss of generality, we can set αS(0) = 0 and αT(0) = α0, i.e., S and T are adjacent satellites on the orbit. Also, let λℓ(t) ad φℓ(t) be the latitude and longitude of the sub-satellite point (SSP)2 of ℓ at time t.

By geometric considerations, we obtain

λℓ(t) = arcsin(sin iK sin αℓ(t)) (2)
where ωE is the earth angular speed,

φℓ(t) = mod � �φℓ(t) − ωEt + π, 2π � − π, (3) �φℓ(t) = atan2(cos iK sin αℓ(t), cos αℓ(t)), (4)
and atan2(·, ·) is the 4-quadrant inverse tangent function. With reference to Fig. 2, let λGU and φGU be latitude and longitude of the GU, supposed fixed in a single satellite pass3. Using the spherical law of cosines, the central angle between the GU and the SSP of satellite ℓ is given by [11]

$$\gamma_{\ell}(t)=\arccos\left(\sin\lambda_{\ell}(t)\sin\lambda_{\rm GU}+\cos\lambda_{\ell}(t)\cos\lambda_{\rm GU}\cos\Delta\phi_{\ell}(t)\right)\tag{5}$$

where $\Delta\phi_{\ell}(t)=\phi_{\rm GU}-\phi_{\ell}(t)$. The elevation of the satellite $\ell$ at time $t$, as observed by the GU, can be found using the law of sines [10], yielding

$$\delta_{\ell}(t)=\arctan\frac{\cos\gamma_{\ell}(t)-\frac{R_{\rm E}}{R_{\rm E}+h_{0}}}{\sin\gamma_{\ell}(t)}\,.\tag{6}$$
We define δmin as the minimum elevation that allows a successful communication between the GU and the satellite.

Finally, considering Fig. 2, the slant distance of the satellite ℓ
from the GU can be obtained by the law of cosines [6] as

$$d_{\ell}(t)=\sqrt{R_{\rm E}^{2}\sin^{2}\delta_{\ell}(t)+h_{0}^{2}+2h_{0}R_{\rm E}-R_{\rm E}\sin\delta_{\ell}(t)}\tag{7}$$

## B. Ground-To-Satellite Channel Model

We assume the narrow-band G2S channel model presented in [6], [7]. It is based on a Semi-Markov chain, where there are two states, good (G) and bad (B). State G represents a condition in which the effect of obstructions and fading is relatively low, while in state B shadowing and fading have a more severe impact on the received signal-to-noise ratio
(SNR). The evolution of the channel conditions corresponds to an alternate sequence of states G and B, where the duration of each state occurrence is a random variable independent of all the others. In both states, the duration has a lognormal probability density function (PDF), with different parameters for state-G and state-B occurrences.

Within a given state occurrence, the channel coefficients obey a Loo distribution, which is the superposition of a lognormal shadowing (modeling slow channel variations) and a Rayleigh fading. Under this model, a channel coefficient is a complex random variable with independent magnitude and phase. The phase is uniformly distributed in [0, 2π] and the magnitude has PDF

$$f_{\rm LOo}(x)=\frac{8.686x}{\Sigma_{\rm A}\sigma^{2}\sqrt{2}\pi}\int_{0}^{+\infty}\frac{1}{a}{\rm e}^{-\frac{(20\log_{10}(a)-M_{\rm A})^{2}}{2\Sigma_{\rm A}^{2}}}-\frac{x^{2}-a^{2}}{2\sigma^{2}}\tag{8}$$ $$\times I_{0}\left(\frac{ax}{\sigma^{2}}\right)\,{\rm d}a$$
where MA and ΣA are mean and standard deviation of the Line-of-Sight (LoS) component, while MP = 10 log10 σ2
is the power of the scattered component. In (8), I0(x) is the order-0 modified Bessel function of the first kind. The triple of parameters (MA, ΣA, MP) characterizing the Loo distribution is itself a random variable, with different PDF
depending on whether the state is good or bad, and sampled independently for each state occurrence. Correlation between successive channel coefficients is obtained by low-pass filtering on the LoS component and Jakes' filtering on the scattered component [7].

On the G2S link, the signal received by satellite ℓ at time t has SNR

$${\rm SNR}_{\ell}(t)=\frac{P_{\rm GU}G_{\rm GU}G_{\ell}L_{\ell}(t)|h_{\ell}(t)|^{2}}{N_{0}W_{\rm GS}}=\rho_{\ell}(t)|h_{\ell}(t)|^{2}\tag{9}$$
where

- PGU is the GU TX power;
- GGU and Gℓ are the antenna gains of the GU and of
satellite ℓ, respectively;
4πdℓ(t)fG2S
- Lℓ(t) =
�
c
�2
is the free-space path loss, with
c and fG2S being the speed of light and the carrier
frequency on the G2S link;
- hℓ(t) is the term in the G2S channel that accounts for
shadowing and fading;
- ρℓ(t) is the LoS SNR, without shadowing/fading;
- N0 is the noise power spectral density;
- WG2S is the signal bandwidth on the G2S channel.

## C. Isl Channel Model

For the ISL channel, we adopt the model reported in
[8]. In particular, we assume that the ISL works at a large operating frequency, so that the depolarization effect can be neglected. Moreover, the attenuation due to plasma frequency and collision frequency is very low, compared to the free-space path loss, thus it will also be neglected [8].

The inter-satellite channel model boils down to an AWGN
channel, with random SNR due to pointing errors, represented by a misalignment angle ξ between transmit and receive antennas. We assume that the antenna gain of both satellites on the ISL can be characterized as [8]

$$G=G_{0}{\rm e}^{-\nu\xi^{2}}\tag{109}$$
where G0 is the maximum antenna gain (achieved when the main lobe of the satellite antenna perfectly points towards the other satellite), ν = 4 ln 2/θ2
3dB is a parameter related to the
3-dB width θ3dB of the main lobe and ξ is a Gaussian random variable with zero mean and variance σ2
p.

Thus, we can compute the received SNR on the ISL as

$$\rho_{\rm ISL}=\frac{P_{T}L_{\rm ISL}G_{0}^{2}{\rm e}^{-2\nu\xi^{2}}}{k_{B}T_{0}W_{\rm ISL}}\tag{11}$$
where
- PT is the transmit power on the ISL link;
4πdISLfISL
�2
is the free-space path loss, with
fISL and dISL = 2(Re + h0) sin α0
- LISL =
�
c
2
being the carrier
frequency and the link length on the ISL, respectively;
- kB is the Boltzmann constant;
- T0 is the ambient noise temperature; - WISL is the signal bandwidth on the ISL.
We suppose perfect receiver knowledge of the ISL SNR.

## D. Signal Received On The G2S Link

In this subsection, we describe the communication channel in the G2S link.

The GU takes into information word $\mathbf{u}$ and encodes it with a rate-$R_{\ell}$ channel code. Then, the obtained codeword $\mathbf{c}=1,2,\ldots,N$, broadening the sequence of symbols $x[n]$, $n=1,2,\ldots,N$, taken from a size-$S$ unit-energy modulation, where $T_{s}$ is the symbol time.

In the soft-handover scenario, both satellites receive the signal transmitted by the GU. One of the two satellites works as relay (R), through the ISI, according to the relaying strategies described in Sect. II-E; the other as destination (D). More precisely, when $\delta_{\delta}(t)>\delta_{\mathrm{T}}(t)$, then $\mathrm{R}=\mathrm{T}$ and $\mathrm{D}=\mathrm{S}$. Both satellites are supposed to have perfect knowledge of their respective channel, because for example it has been estimated through the use of plots. The (normalized) signal received by satellite $\ell$ at time step $n$, $n=1,\ldots,N$ is given by

$$\begin{array}{l}y\ell[n]\ \sim\ \sqrt{\rho_{\ell}[n]h[n][n]+w\ell[n]},\end{array}\tag{12}$$

where $w_{\ell}[n]\sim\mathcal{CN}(0,1)$, i.e., it is a circularly-symmetric complex Gaussian noise sample with zero mean and unit variance, $\rho_{\ell}[n]\triangleq\rho_{\ell}(nT_{s})$ is the received LoS SNRs, while $h[n]\triangleq h(nT_{s})$ accounts for both shadowing and fading. For the sake of notation compactness, we define the vectors $\mathbf{y}_{\ell}=(y_{\ell}[1],\ldots,y_{\ell}[N])$, with $\ell\in\{\mathrm{S},\mathrm{T}\}$ if we consider the physical satellites or $\ell\in\{\mathrm{R},\mathrm{D}\}$ if we refer to the logical satellites, and analogously for $\rho_{\ell}$ and $\mathbf{h}_{\ell}$.

E. Relaying Techniques
  With soft handover, after reception from the GU, the relay-
ing satellite R may forward its received signal to satellite D.
We consider two possible choices for the relaying strategy, as
follows.

- *Amplify and forward (AF)*: Satellite R works as a repeater,
by only forwarding the received signal yR[n]. The normalized (unit-energy) forwarded signal on the ISL link then becomes
$$x_{\rm ISL}[n]=\frac{y_{\rm R}[n]}{\sqrt{q[n]}},\quad\forall n\tag{13}$$

where $q[n]={\mathbb{E}}[|y_{\rm R}[n]|^{2}]=\rho_{\rm R}[n]|h_{\rm R}[n]|^{2}+1$ is a normalization factor. Indeed, with AF relaying, the normalized signal in (13) is amplified with an amplification gain before transmission.
* _Decode and forward (DF)_: Satellite R demodulates and decodes the received signal. A block decoding error happens with probability $P_{B}$, according to the definition (24) given below. We suppose that satellite R is aware whether decoding is successful or not. If it is successful, it encodes the estimated information bits, modulates the coded bits and forwards the regenerated signal to S, so that $$x_{\rm ISL}[n]=x[n],\quad\forall n$$ (14)
If decoding is not successful, T forwards no signal to S.

F. Processing at Satellite D
The (normalized) signal received by satellite D on the ISL
from R at time step n is given by

$$y_{\rm{ISL}}[n]=\sqrt{\rho_{\rm{ISL}}x_{\rm{ISL}}[n]+w_{\rm{ISL}}[n]},\tag{15}$$
where ρISL is defined in (11), and wISL[n] ∼ CN(0, 1). For DF, ρISL = 0 in the case of unsuccessful decoding at R.

In order to improve the link reliability, satellite D then performs maximum ratio combining (MRC) of the two signals, the one received directly from the GU on the G2S link and the one relayed by R on the ISL link. For both AF and DF, after suitable normalization, we can write the MRC output as

$$\widetilde{y}_{\vartheta}[n]=\widetilde{h}_{\vartheta}[n]x[n]+\widetilde{w}[n],\tag{16}$$

where $\vartheta\in\{\text{AF},\text{DF}\}$, $\widetilde{w}[n]$ is a zero-mean complex Gaussian noise with variance 1 and $\widetilde{h}[n]$ is the equivalent channel at time step $n$. In the case of AF, we have

$$\widetilde{h}_{\text{AF}}[n]=\sqrt{\rho_{\text{D}}[n]|h_{\text{D}}[n]|^{2}+\frac{\rho_{\text{ISL}}\rho_{\text{R}}[n]|h_{\text{R}}[n]|^{2}}{\rho_{\text{ISL}}+q[n]}}\tag{17}$$

$$\widetilde{y}_{\text{AF}}[n]=\sqrt{\rho_{\text{D}}[n]\left(\frac{h_{\text{D}}[n]}{\widetilde{h}_{\text{AF}}[n]}\right)^{*}y_{\text{D}}[n]+}\tag{18}$$ $$+\frac{\sqrt{\rho_{\text{ISL}}q[n]\rho_{\text{R}}[n]}}{\rho_{\text{ISL}}+q[n]}\left(\begin{array}{c}\\ \\ \end{array}\right)^{*}y_{\text{ISL}}[n].$$
Instead, for DF,

$$\tilde{\tilde{h}}_{\rm H}\tilde{\tilde{\rm H}}_{\rm H}=\sqrt{\rho_{\rm H}}\left(\left[\frac{h_{\rm H}\tilde{\rm H}_{\rm H}}{h_{\rm H}\tilde{\rm H}_{\rm H}}\right]\right)+\sqrt{\rho_{\rm H}}\tilde{\tilde{\rm H}}_{\rm H}\tilde{\tilde{\rm H}}_{\rm H}\tilde{\rm H}_{\rm H}\tag{19}$$

Notice that $\Delta$F is continuous by replacing the $\tilde{\tilde{\rm H}}_{\rm H}$ and $\tilde{\tilde{\rm H}}_{\rm H}$. (20) as a multiple $0$-fold for pure water.

## Iii. Bler Analysis

In this section, we derive the final performance in terms of BLER for the combined signal at satellite D. Consider the AWGN channel $\mathcal{Y}=\sqrt{\rho}\mathcal{H}\mathcal{X}+\mathcal{W}$ with $\mathcal{W}\sim\mathcal{CN}(0,1)$ and $\mathcal{X}$ belonging to a size-$S$ modulation $\mathcal{S}$. Let $H\left(\mathcal{X}|y,\sqrt{\rho}h\right)$ be the equivocation on such channel when $\mathcal{Y}=y$ and $\mathcal{H}=h$, i.e.,

$$H\left(\mathcal{X}|y,\sqrt{\rho}h\right)=-\sum_{s\in\mathcal{S}}p\left(s|y,\sqrt{\rho}h\right)\log_{2}p\left(s|y,\sqrt{\rho}h\right)\tag{21}$$

$\cdot$
where

$$p\left(s|y,\sqrt{\rho}h\right)=\frac{\mathrm{e}^{-\mathrm{j}\,\mathrm{y}\cdot\sqrt{\rho}h^{\mathrm{T}}}}{\sum_{n^{\prime}\in\mathrm{C}}\mathrm{e}^{-\mathrm{j}\,\mathrm{y}\cdot\sqrt{\rho}h^{\mathrm{T}}}}\tag{22}$$

Then, the (conditional) natural information (MI) per bit is given by

$$C(y,\sqrt{\rho}h)=1-\frac{1}{\log_{2}S}H\left(X|y,\sqrt{\rho}h\right)\tag{23}$$

Suppose that the model of length $N_{c}$ symbols is transmitted on the AWGN channel and denote $\mathrm{y},\mathrm{h},\rho$ be length $\mathrm{y}_{c}$. Na vectors of realized control nodes and denote $\mathrm{y},\mathrm{h},\rho$ be length $\mathrm{y}_{c}$. Na SNR values, respectively. We assume that the channel decoder has a block error problem given by[4]

$$P_{H}(e|\mathbf{y},\sqrt{\rho}\odot\mathrm{h})=1,\ \frac{1}{0},\ \frac{\overline{C}(\mathbf{y},\sqrt{\rho}\odot\mathrm{h})}{\overline{C}(y,\sqrt{\rho}\odot\mathrm{h})}\leq C_{T}\tag{24}$$

where

$$\overline{C}(\mathbf{y},\sqrt{\rho}\odot\mathrm{h})=\frac{1}{N_{c}}\sum_{n^{\prime}\in\mathrm{C}}C(y_{n}|h,\sqrt{\rho}_{n}|h|n)\tag{25}$$

gives the variance of all per bit on the code block. In (24), $C_{T}$ is the threshold $\mathrm{M}$ on the AWGN channel for the channel code. Intuitively, (24) the model of the channel decoder on the transmission channel is large enough, the signal is correctly decoded, otherwise it is lost. Typically, (24) is a good 

## A. Soft Handover With Noiseless Isl

In this subsection, we derive the performance of soft handover, for both AF and DF, in the limit of ρISL → ∞. In such case, the considered system is equivalent to a virtual
1 × 2 single-input multiple-output system, in which there is only one satellite with two antennas, and the received signal is
(yD, yR). Notice that, given the elevations of the two satellites and thus the values of (ρD, ρR), the two branches of the received signal are independent in our model.

In such a scenario, the optimal receiver performs MRC
before decoding, as in the AF case. The instantaneous SNR after MRC will then be given by

$$\lim_{\rho_{\rm LSL}\rightarrow\infty}|\widetilde{h}_{\rm AF}[n]|^{2}=\rho_{\rm D}[n]|h_{\rm D}[n]|^{2}+\rho_{\rm R}[n]|h_{\rm R}[n]|^{2}\tag{28}$$

The advantage of AF-based soft handover with respect to hard handover, on a noiseless ISI, is then obvious, as the hard-handover SNR is equal to $\rho_{\rm D}[n]|h_{\rm D}[n]|^{2}$, so that hard handover is more prone to B-state channel conditions on the link between GU and satellite D. Notice that this conclusion can be generalized to a noisy ISI, as the SNR after MRC will always be larger than in the hard-handover case.

On the noiseless ISI, the DF strategy corresponds to separate decoding on ${\bf y}_{\rm D}$ and ${\bf y}_{\rm R}$, so that the transmitted block is lost if and only if both decoding attempts fail. Thus:

$$\lim_{\rho_{\rm ISL}\rightarrow\infty}P_{B,{\rm SH},{\rm DF}}(e)=\mathbb{E}_{\mathbf{\rho}_{\rm D},\mathbf{\rho}_{\rm R}}\left\{\mathbb{E}_{\bf y_{\rm D},{\rm h}_{\rm D}}P_{B}(e|{\bf y}_{\rm D},\sqrt{\mathbf{\rho}_{\rm D}}\odot{\rm h}_{\rm D})\right.$$ $$\left.\times\mathbb{E}_{\bf y_{\rm R},{\rm h}_{\rm R}}P_{B}(e|{\bf y}_{\rm R},\sqrt{\mathbf{\rho}_{\rm R}}\odot{\rm h}_{\rm R})\right\}\tag{29}$$
While DF proves suboptimal with respect to AF for a noiseless ISL, on a noisy ISL this may not be true in general, as the latter combines the noise on the ISL with the noise on the G2S link between the GU and satellite R.

## Iv. Simulation Results

In Table I, we report the main parameters of the simulation.

We consider a single satellite pass5. In that pass, we focus on the time window for which satellites T and S have the highest elevations (both larger than δmin) in the constellation.

The elevation time series for both satellites is quantized on the set of values {30◦, 45◦, 60◦, 70◦}, for which there exist tables of channel parameters in [7]. More precisely, we consider a carrier frequency fG2S = 2.2 GHz, and the suburban environment, so that the parameter tables for the different elevations can be found in [7, Annex 2, Sect. 2.2]. Given the parameters, the channel coefficients for the two G2S links are then generated independently. The visibility interval of both satellites lasts for about 2 minutes, during which we suppose that 500 code blocks are transmitted.

In the simulations, we consider as the independent variable a reference SNR, which is the LoS SNR when the satellite is at the minimum distance (i.e., the maximum elevation) from the

GU. In other words, the reference SNR for satellite $\ell=\{$S, T$\}$ is given by

$$\rho_{\rm ref}=\frac{P_{\rm GU}G_{\rm GU}G_{\ell}L_{\rm ref}}{N_{0}W_{\rm G2S}}\tag{30}$$

where

$$L_{\rm ref}=\left(\frac{c}{4\pi h_{0}f_{\rm G2S}}\right)^{2}\tag{31}$$
so that the actual LoS SNR is ρℓ[n] = ρrefLℓ[n]/Lref. With the parameters reported in Table I, a reference SNR of 20 dB
corresponds to a transmitted power PGU of about 50 mW.

| Parameter                      | Notation   | Value           |
|--------------------------------|------------|-----------------|
| Geometrical model              |            |                 |
| Orbit height                   |            |                 |
| h                              |            |                 |
| 0                              |            |                 |
| 550 km                         |            |                 |
| Orbit inclination              |            |                 |
| i                              |            |                 |
| K                              |            |                 |
| 45                             |            |                 |
| ◦                              |            |                 |
| Constellation size             |            |                 |
| M                              |            |                 |
| {                              | 42         |                 |
| ,                              |            |                 |
| 63                             | }          |                 |
| GU coordinates                 |            |                 |
| (                              |            |                 |
| λ                              |            |                 |
| GU                             |            |                 |
| , φ                            |            |                 |
| GU                             |            |                 |
| )                              |            |                 |
| (                              |            |                 |
| 45                             |            |                 |
| ◦                              |            |                 |
|                                |            |                 |
| N,                             |            |                 |
| 7                              |            |                 |
| ◦                              |            |                 |
|                                |            |                 |
| E)                             |            |                 |
| Minimum elevation              |            |                 |
| δ                              |            |                 |
| min                            |            |                 |
| 25                             |            |                 |
| ◦                              |            |                 |
| Ground-to-satellite (G2S) link |            |                 |
| Carrier frequency              |            |                 |
| f                              |            |                 |
| G2S                            |            |                 |
| 2.2 GHz                        |            |                 |
| Transmitted power              |            |                 |
| P                              |            |                 |
| GU                             |            |                 |
| See text                       |            |                 |
| GU antenna gain                |            |                 |
| G                              |            |                 |
| GU                             |            |                 |
| 0 dBi                          |            |                 |
| Satellite antenna gain         |            |                 |
| G                              |            |                 |
| S                              |            |                 |
| , G                            |            |                 |
| T                              |            |                 |
| 50 dBi                         |            |                 |
| Signal bandwidth               |            |                 |
| W                              |            |                 |
| G2S                            |            |                 |
| 5 MHz                          |            |                 |
| Environment                    | -          | Suburban        |
| Channel model parameters       | -          | From [7]        |
| Noise level                    |            |                 |
| N                              |            |                 |
| 0                              |            |                 |
| -174 dBm/Hz                    |            |                 |
| Inter-satellite link (ISL)     |            |                 |
| Carrier frequency              |            |                 |
| f                              |            |                 |
| ISL                            |            |                 |
| {                              | 2          |                 |
| ,                              |            |                 |
| 193                            | }          |                 |
| THz                            |            |                 |
| Transmitted power              |            |                 |
| P                              |            |                 |
| T                              |            |                 |
| {                              | 5          |                 |
| ,                              |            |                 |
| 10                             |            |                 |
| ,                              |            |                 |
| 15                             |            |                 |
| ,                              |            |                 |
| 20                             |            |                 |
| ,                              |            |                 |
| 25                             | }          |                 |
| dBW                            |            |                 |
| Ambient noise temperature      |            |                 |
| T                              |            |                 |
| 0                              |            |                 |
| 7000 K                         |            |                 |
| Signal bandwidth               |            |                 |
| W                              |            |                 |
| ISL                            |            |                 |
| 2%                             |            |                 |
| f                              |            |                 |
| ISL                            |            |                 |
| TX/RX antenna gain             |            |                 |
| G                              |            |                 |
| 0                              |            |                 |
| {                              | 60         |                 |
| ,                              |            |                 |
| 90                             | }          |                 |
| dBi                            |            |                 |
| Half-power beam width          |            |                 |
| θ                              |            |                 |
| 3dB                            |            |                 |
| 202                            |            |                 |
| .                              |            |                 |
| 5                              | ×          | 10              |
| −                              |            |                 |
| G                              |            |                 |
| 0                              |            |                 |
| /                              |            |                 |
| 20                             |            |                 |
|                                |            |                 |
| deg                            |            |                 |
| Misalignment variance          |            |                 |
| σ                              |            |                 |
| 2                              |            |                 |
| p                              |            |                 |
| See text                       |            |                 |
| Transmitted signal format      |            |                 |
| Channel coding rate            |            |                 |
| R                              |            |                 |
| c                              |            |                 |
| 1/2                            |            |                 |
| Channel code                   | -          | (3,6) LDPC code |
| Code threshold                 |            |                 |
| C                              |            |                 |
| T                              |            |                 |
| 0.5714 bits                    |            |                 |
| Modulation format              | -          | QPSK (          |
| S                              |            |                 |
| = 4                            |            |                 |
| )                              |            |                 |

A. Comparison between AF and DF
We first compare AF and DF in the scenario summarized by the parameters in Table I. In particular, we consider the case in which:

- there is no misalignment in the ISL; - the angular distance between the two satellites is α0 =
0.15 rad, corresponding to (about) M = 42 satellites in
the same orbit;
- the carrier frequency on the ISL is fISL = 193 THz (in the optical band), with an antenna gain G0 = 90 dB.

Figure 3 shows the numerical results. Blue curves represent the BLER for DF, with three different values of the transmit power PT on the ISL, namely PT ∈ {5, 10, 20} dBW. For the same values of PT , red curves depict the performance of AF. The thick black curve shows the BLER of hard handover, while the thick purple and green curves correspond to the BLER for AF and DF, respectively, with an infinite SNR on the ISL (or, equivalently, a noiseless ISL).

As it can be seen, at BLER
=
10−4 and with the parameter setting of the figure, the ultimate gain of soft handover, compared to hard handover, is 16 dB. Most of this potential advantage can be achieved by adopting an AF
relaying strategy with a transmitted power of PT = 20 dBW.

The comparison between red and blue curves reveals that, for low-to-intermediate transmitted power (PT = 10 dBW), AF
and DF show a comparable performance. Instead, for large PT , AF improves on DF, as the former seems to exploit better the diversity gain offered by multisatellite reception, in accordance with the analysis of Section III-A.

It is worth commenting the shape of the curves for different SNR values. For reference SNR lower than 10 dB, BLER curves decrease with SNR as expected, but for middle SNR values (say, around 10 to 12-15 dB, depending on the curve) there is a floor. This is due to the fact that, in the elevation time series, there is a time window where both satellites have a quantized elevation as low as 45◦, so that the channel model for both satellites shows a more severe impact of B-state events. As a result, the error floor appears when the reference SNR is not large enough to yield a good performance also in this time window.

B. Increasing the Size of the Constellation After obtaining in the previous subsection the BLER performance for a number of satellites in the same orbit equal to M = 42, in this subsection we obtain the same results for M = 63, corresponding to an angular distance between neighbor satellites of α0 = 0.1 rad. In both cases, the elevation time series for the two satellites are very similar, with one delayed with respect to the other. For M = 63, when the two satellites have about the same elevation, this elevation is close to 60◦, while for M = 42 it is close to 45◦, as already mentioned in Section IV-A. All the other parameters are as in Figure 3.

Figure 4 shows the BLER performance in the new scenario with more satellites. Blue curves are obtained for DF while red curves are for AF. As it can be seen, the maximum achievable gain of soft handover is reduced to about 2–2.5 dB. In this scenario, DF slightly outperforms AF for PT = 5 dBW, as its performance is not affected by the noise on the GU-to-T
link, while for larger PT AF is better than DF, as in Figure 3.

Overall, we can say that increasing the size of the constellation makes soft handover less awarding, as, for N = 63 satellites, a BLER of 10−3 is obtained with hard handover for a reference SNR equal to about 13 dB, while the same value for N = 42
satellites requires a reference SNR of at least 15 dB and a large ISL transmitted power (with AF). Also, we conclude that, in the simulated scenario, DF does not achieve the performance gain that would repay for its complexity increase with respect to AF.

Finally notice that, in this scenario, since there is always at least one satellite with quantized elevation larger than 45◦, there is no error floor for middle SNR values. C. The Impact of Misalignment Finally, we consider the impact on performance of misalignment in the ISL. Following [8], we consider two different carrier frequencies on the ISL, namely, fISL = 193 THz, as in Sections IV-A and IV-B, and fISL = 2 THz. In both cases, we adopt Kraus' approximate formula [12] to derive the halfpower beamwidth given the antenna gain, as shown in Table I.

For fISL = 193 THz, a gain of 90 dB yields a half-power beamwidth of 0.0064◦, while for fISL = 2 THz, we have set a gain G0 = 60 dB, which results in a half-power beamwidth equal to 0.2◦. The misalignment stays constant over a single code block.

For the two bands, Figures 5-6 show, for both DF and AF, the reference SNR needed to achieve BLER = 10−5, as a function of σ2
p, the misalignment variance. In Figure 5, which is for M = 42 satellites, the transmitted power on the ISL is set to PT = 25 dBW, while in Figure 6, for M = 63 satellites, PT = 15 dBW. The figures show similar behavior in the two bands. For low enough σ2
p, the performance reaches that of the no-misalignment case. Instead, for sufficiently high σ2
p, the soft-handover performance reaches the hard-handover BLER, with no help anymore from the ISL. As it was to be expected, the optical band is much more sensitive, due to the narrower beam. For instance, with the parameter settings of Figure 6 and threshold reference SNR equal to 12 dB, a 15 times larger misalignment variance can be tolerated in the case with fISL =
2 THz, compared to the case with fISL = 193 THz. It is worth noting that, in both figures and for σ2
p = 10−3, the performance in the THz band is still optimal, while the optical scenario shows already a completely spoiled contribution of the ISL. Of course, the larger bandwidth in the optical band allows to serve more users at the same time, and to potentially reduce the number of satellites connected to the ground by feeder links.

It is also worth noting that, when misalignment starts to worsen performance, the difference between AF and DF disappears.

## V. Conclusions

We considered a constellation of LEO satellites connected to a handheld device on the ground. In particular, we studied the benefits of soft handover in the UL from the physicallayer point of view. We have performed simulation results in a realistic scenario, where the impairments are taken into account both in the ground-to-satellite and the ISL.

Our results show that, although implying a larger computation complexity, soft handover can achieve a substantial performance gain over hard handover. Considering different relaying techniques, AF should be preferred to DF, as the former shows essentially the same performance of the latter for low-to-medium transmitted power on the ISL, and a definite advantage for large transmitted power. Moreover, AF has a lower complexity for the relaying satellite. Adding satellites to the constellation improves the performance of both hard handover and soft handover, and reduces the achievable gain of soft handover. Finally, our results show how important is to maintain a suitable alignment of the satellite antennas, to achieve the potential gain of soft handover, especially in the optical band.

## Acknowledgment

Funded by the European Union, under ANTERRA
101072363 HORIZON-MSCA-2021-DN-01. Views and opinions expressed are however those of the authors only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.

## References

[1] U. Gustavsson, P. Frenger, C. Fager, T. Eriksson, H. Zirath, F. Dielacher,
C. Studer, A. Parssinen, R. Correia, J. N. Matos, D. Belo, and N. B. Carvalho, "Implementation challenges and opportunities in beyond-5G
and 6G communication," *IEEE Journal of Microwaves*, vol. 1, no. 1,
pp. 86–100, 2021.
[2] N. Rajatheva, I. Atzeni, S. Bicais, E. Bjornson, A. Bourdoux, S. Buzzi,
C. D'Andrea, J.-B. Dore, S. Erkucuk, M. Fuentes, K. Guan, Y. Hu, X. Huang, J. Hulkkonen, J. M. Jornet, M. Katz, B. Makki, R. Nilsson, E. Panayirci, K. Rabie, N. Rajapaksha, M. Salehi, H. Sarieddeen, S. Shahabuddin, T. Svensson, O. Tervo, A. Tolli, Q. Wu, and W. Xu, "Scoring the terabit/s goal: Broadband connectivity in 6G," 2021.
[3] E. Juan, M. Lauridsen, J. Wigard, and P. Mogensen, "Handover solutions
for 5G low-earth orbit satellite networks," *IEEE Access*, vol. 10, pp.
93 309–93 325, 2022.
[4] G. Barros, J. Vieira, F. Ganhao, L. Bernardo, R. Dinis, P. Carvalho,
R. Oliveira, and P. Pinto, "A soft-handover scheme for LEO satellite
networks," in 2013 IEEE 78th Vehicular Technology Conference (VTC Fall), 2013, pp. 1–5.
[5] Y. Omid, Z. M. Bakhsh, F. Kayhan, Y. Ma, and R. Tafazolli, "Space
MIMO: Direct unmodified handheld to multi-satellite communication,"
2023.
[6] "3rd generation partnership project; technical specification group radio
access network: study on new radio (NR) to support nonterrestrial
networks (release 15)," June 2018.
[7] "Recommendation
of
radiocommunication
sector
of
international
telecommunication union: propagation data required for the design systems in the land mobile-satellite service (release 11)," August 2019.
[8] S. Nie and I. F. Akyildiz, "Channel modeling and analysis of inter-smallsatellite links in terahertz band space networks," IEEE Transactions on Communications, vol. 69, no. 12, pp. 8585–8599, 2021.
[9] E. G¨uven, O. B. Yahia, and G. Karabulut-Kurt, "Multi-state intersatellite channel models," in 2023 International Balkan Conference on Communications and Networking (BalkanCom), 2023, pp. 1–6.
[10] M. Richharia
and L. Westbrook,
Satellite
Systems for Personal
Applications: Concepts and Technology, ser. Wireless Communications
and
Mobile
Computing.
Wiley,
2010.
[Online].
Available:
https://books.google.it/books?id=TC1KZTaCLU8C
[11] L. M. Kells, W. F. Kern, and J. R. Bland, Plane and spherical
trigonometry.
McGraw Hill Book Company, Inc., 1940.
[12] J. D. Kraus and R. J. Marhefka, *Antenna for all applications*. McGraw-
Hill, 2002.