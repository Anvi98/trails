# Fundamentals Of Delay-Doppler Communications: Practical Implementation And Extensions To Otfs

Shuangyang Li, *Member, IEEE,* Peter Jung, *Member, IEEE,* Weijie Yuan, *Member, IEEE,* Zhiqiang Wei, *Member, IEEE,* Jinhong Yuan, *Fellow, IEEE,* Baoming Bai, *Senior Member, IEEE,* and Giuseppe Caire, Fellow, IEEE

## Abstract

The recently proposed orthogonal time frequency space (OTFS) modulation, which is a typical Delay-Doppler
(DD) communication scheme, has attracted significant attention thanks to its appealing performance over doublyselective channels. In this paper, we present the fundamentals of general DD communications from the viewpoint of the Zak transform. We start our study by constructing DD domain basis functions aligning with the time-frequency
(TF)- consistency condition, which are globally quasi-periodic and locally twisted-shifted. We unveil that these features are translated to unique signal structures in both time and frequency, which are beneficial for communication purposes. Then, we focus on the practical implementations of DD Nyquist communications, where we show that rectangular windows achieve perfect DD orthogonality, while truncated periodic signals can obtain sufficient DD orthogonality.

Particularly, smoothed rectangular window with excess bandwidth can result in a slightly worse orthogonality but better pulse localization in the DD domain. Furthermore, we present a practical pulse shaping framework for general DD
communications and derive the corresponding input-output relation under various shaping pulses. Our numerical results agree with our derivations and also demonstrate advantages of DD communications over conventional orthogonal frequency-division multiplexing (OFDM).

## Index Terms

Zak transform, delay-Doppler communications, OTFS, multicarrier modulation, pulse shaping.

This paper was presented in part at IEEE Global Communication Conference 2023 [1].

10587, Germany (e-mail: shuangyang.li, pter.jung, caire@tu-berlin.de). China (e-mail: yuanwj@sustech.edu.cn).

Z. Wei is with the School of Mathematics and Statistics, Xi'an Jiaotong University, Xi'an 710049, China (e-mail: zhiqiang.wei@xjtu.edu.cn).

J. Yuan is with the School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney, NSW 2052, Australia
(e-mail: j.yuan@unsw.edu.au).

B. Bai is with the State Key Lab. of ISN, Xidian University, Xi'an 710071, China. (e-mail: bmbai@mail.xidian.edu.cn).

## I. Introduction

Next generation wireless networks are expected to provide high throughput and ultra-reliable communications services to facilitate the various emerging applications. To meet the stringent requirements imposed by these emerging applications, such as high frequency bands, high mobility, conventional wireless waveforms, e.g., orthogonal frequency-division multiplexing (OFDM), require sophisticated adaptation, which not only complicates the system design but also degrade the system performance potentially. In light of this, new wireless waveforms need to be developed.

Orthogonal time frequency space (OTFS) modulation was recently proposed in [2] as a means for next generation wireless communications. The advantages of OTFS come from the symbol placement in the delay-Doppler (DD) domain, which allows the information symbol to have a direct interaction to the DD domain channels. As a result, appealing DD domain channel properties are naturally exploited, including quasi-static, path separability, and compactness [3], [4]. This channel exploitation has translated into various improvements of communication performance, as evidenced by many existing works [5]–[8]. In [9], a DD domain channel estimation scheme based on the embedded pilot was proposed, where one strong pilot symbol is placed in the DD domain with a sufficiently large guard space. Thanks to the DD domain path separability, good channel estimation performance can be achieved by simply comparing the received and the transmitted pilot symbols. The error performance of OTFS was studied in [10], where the authors have shown that OTFS almost surely achieves the full channel diversity over sparse Rayleigh fading channels even with a relatively small frame size. This conclusion is further extended in [11], which reported that coded OTFS systems have an important diversity and coding gain tradeoff depending on the number of resolvable paths in the channel. Consequently, OTFS only requires a relaxed code design comparing to OFDM. Furthermore, the DD domain path separability gives rise to novel MIMO communication designs using OTFS waveforms. Particularly, path-oriented precoding designs have shown good compatibility to both point-to-point (P2P) MIMO and multi-user (MU) MIMO transmissions in terms of both achievable rates and computational complexity [12], [13]. In addition, recent works on integrated communications and sensing (ISAC) have also demonstrated the great potential of OTFS [14], [15].

Let us have a historical recap of the OTFS literature. In the early papers [2], [16], [17], OTFS was implemented based on the overlay of OFDM by using the two-dimensional (2D) inverse symplectic finite Fourier transforms (ISFFT), which is known as the two-stage implementation. Such an implementation demonstrates a strong compatibility with the main stream OFDM standards but did not highlight the unique properties of OTFS promised by the Zak transform, which is the fundamental mathematical tool connecting the DD domain and the time/frequency domain. After several years of prosperity, OTFS has gradually become a popular topic in both academia and industry. However, most of the OTFS studies were still focused on the two-stage implementation of OTFS until now. Noticeably, the two-stage implementation is limited by the OFDM structure, where a time-frequency (TF) domain pulse, commonly a rectangular window with duration of an OFDM symbol, was adopted for carrying the precoded (using ISFFT) information symbols. Note that the ISFFT spreads each DD domain information symbol to all TF domain symbols, which are carried by different TF domain pulses. Consequently, each DD domain information symbol is modulated onto many different pulses, resulting in the so-called "pulse discontinuity" [18].

The pulse discontinuity may introduce abrupt changes of the transmitted signal, which can cause a large out-ofband (OOB) emission and thereby degrading the system performance. However, the impact of pulse discontinuity is almost invisible in numerical simulations if the OOB issue was not considered, which is often the case when the system was evaluated by Monte Carlo methods developed based on the discrete channel model, e.g., [19]. To solve the OOB issue, many OTFS variants have been proposed recently. The orthogonal delay-Doppler division multiplexing (ODDM) modulation was proposed in [18], where a realizable orthogonal basis with respect to DD resolutions was constructed using the staggered multi-tone modulation. In this context, the authors further proposed delay-Doppler multicarrier (DDMC) modulation using delay-Doppler orthogonal pulses (DDOP) and demonstrated that sufficient DD orthogonality can be achieved by using periodically extended root-raised cosine (RRC) pulses or a Nyquist pulse train [20]. Furthermore, a framework of pulse shaping on DD plane was reported in [21], where a low-complexity pulse shaping structure based on fast convolution was proposed. The proposed framework is compatible to various shaping pulses, and an end-to-end discrete system model was also provided.

More recently, researchers have realized the importance of the Zak transform to OTFS. The Zak transform was originally introduced in the field of solid state physics by J. Zak [22] and was then extended to the field of signal processing [22]. It is a mathematical tool that highlights the physical interpretation between time/frequency and DD. Compared to the OTFS implementation based on OFDM transceivers, implementation using the Zak transform requires less complexity and preserves clear physical insights. A main feature of OTFS transmissions based on the Zak transform is that it generally does not require the overlay with OFDM. Therefore, it is also known as the one-stage implementation. The discrete Zak transform (DZT)-based OTFS realization was proposed in [23], where input-output relation of OTFS was studied and discussed from the DZT viewpoint. However, due to the discrete nature of DZT, the DZT-based OTFS exhibits a degraded performance when the DD resolutions are not sufficient (commonly known as the "fractional delay and Doppler"). In [24], a Zak transform based implementation of OTFS was presented. Specifically, the DD domain continuous symbol carrier (known as the basis function) was derived according to the Zak transform, which was shown to be sufficiently localized. Furthermore, bandwidthlimited and time-limited window functions were applied to truncate the basis functions, where the author showed that rectangular windows can achieve the perfect DD orthogonality. This work has been extended to the OTFS
2.0 modulation recently in [25], [26]. The OTFS 2.0 highlights the DD domain information transmission based on the Zak transform, where the end-to-end input-output relation was characterized by the *twisted-convolution* in the DD domain. In particular, the OTFS 2.0 intentionally precoded information symbols to satisfy the quasi-periodicity property of the Zak transform, and apply DD domain shaping pulses at both the transmitter and receiver to convey information. As a result, OTFS 2.0 exhibits a mathematically simple input-output relation defined purely in the DD
domain. However, all real-world signal transmissions are essentially implemented in time, and unfortunately, not all DD domain signals are realizable in time1. Therefore, how to implement OTFS and in general DD communications in practice require further studies.

In this paper, we aim to fill the gap between the DD communication theory based on the Zak transform and its practical implementation. Specifically, we present the fundamentals of practical DD communications based on the Zak transform without relying on the overlay of the transceivers of TF domain multicarrier waveforms, e.g., OFDM. In contrast of the previous works [25], [26], we highlight the practical implementation of DD Nyquist communications using realizable pulse shaping filters, where an end-to-end input-output relation is also derived from the communication theory viewpoint. Our proposed DD communication framework enjoys sufficient DD orthogonality, which may be the exact motivation of OTFS. More importantly, we highlight the physical interpretation of DD and time/frequency from a signal processing point of view. We show that periodicities in time and frequency will result in localizations in Doppler and delay, according to the theory of Zak transform. However, exact periodicity requires infinite time and frequency resources, which are not realizable in practice. Therefore, truncating periodic time and frequency signals are well motivated, and the DD localizations are degraded to DD orthogonality due to the truncation. The main contributions of this paper are summarized as follows.

- We define a group of equally-spaced basis functions corresponding to information symbols, which are constructed in a special way such that their transformations in both time and frequency are consistent. Such basis functions naturally incorporate the twisted-convolution insight in the DD domain, which exhibit quasiperiodicity globally while are twisted-shifted locally. Particularly, the constructed basis function allows straightforward calculation of its ambiguity function, which is in line with the DD domain pulse shaping and matchedfiltering. Furthermore, we unveil that the DD domain global feature of such functions translates into a train of pulses, while their local feature translates into signal tones in both time and frequency. This unique structure
is known as the "pulsone" in the literature of OTFS.
- We further present the practical realization of basis function by applying practical filters to the ideal basis
functions for symbol transmissions. We introduce the TF-consistent pulse shaping for deriving the practical basis
functions, where both time domain and frequency domain window functions are applied for obtaining a roughly
time-limited and bandwidth-limited basis function. We derive the corresponding DD domain representation and
ambiguity function of such basis functions, and further demonstrate that basis functions enjoying sufficient localization and orthogonality can be achieved by applying truncated periodic signals for windowing. More
importantly, we verify that the rectangular windows enjoy perfect DD orthogonality.
- We present the practical pulse shaping implementation for DD communications in the time domain by introducing reasonable approximations. Based on the proposed implementation, we further derive the input-output relation of general DD communications with various shaping pulses over underspread channels. Particularly, we
demonstrate that the above input-output relation are well-characterized by the ambiguity function of the basis
function in the asymptotical regime, which yields essentially the same results as in [25], [26]. Furthermore, we also verify that the above input-output relation using rectangular windows converges to that of OTFS implemented using OFDM transceivers with rectangular TF pulses [19].
- We provide numerical results of DD communications using various shaping pulses in terms of the bit error
rate (BER), pragmatic capacity [27], [28], and power spectral density (PSD). The practical advantages of the
proposed scheme are verified based on these results.

Notations: The blackboard bold letters A, Z, and E denote the energy-normalized constellation set, the integer number field, and the expectation operator, respectively; "∗" and "⊗" denote the convolution and kronecker product, respectively; "[·]M" denotes the module-M operation. "(·)∗" denotes the conjecture operation. sinc (x) is the sinc function2 defined by sinc (x)
∆= sin(πx)
πx
.

We will interchangeably use two sets of representations to describe the same signal in different domains. For a time domain signal x(t), its Fourier transform and its Zak transform are denoted by X(f) and Zx (τ, ν), respectively. This type of representations highlights the transformation among different domains. Equivalently, we also use subscripts to highlight the domain in which signal is defined, e.g., ΦT(t), ΦF(f), and ΦDD(τ, ν) denote the same signal represented in time, frequency, and DD domains, respectively.

## Ii. Preliminaries On Zak Transform And Dd Domain Pulses

In this section, we will review some fundamental properties of the Zak transform that are available in the literature [22], [29]. We note that the Zak transform plays an important role in the context of the Gabor expansion [29], and its significance has been widely explored in many engineering aspects including image processing [30], texture segmentation [31], and more recently, wireless communications [2]. Note that the Zak transform is a version of the Poisson summation formula [32] and therefore it holds for general Schwartz functions. In fact, it is well-defined almost everywhere in the L2 space, see Lemma 8.2.1 in [32]. Specifically, the Zak transform can be defined equivalently for both time domain signals and frequency domain signals as shown in the following [32], where we assume that the underlying time domain signal and its Fourier transform are well-defined in the Wiener space.

Definition 1 (*The Zak Transform*): Let x (t) be a complex-valued time-continuous function, whose Fourier transform is given by X (f). Furthermore, let T be a positive constant. Then, the Zak transform can be defined equivalently in both time and frequency by [22], [29]

$$\mathcal{Z}_{x}\left(\tau,\nu\right)=\left(\mathcal{Z}\mathcal{T}_{\mathrm{T}}\ x\right)\left(\tau,\nu\right)\stackrel{{\Delta}}{{=}}\sqrt{T}\sum_{k=-\infty}^{\infty}x\left(\tau+kT\right)e^{-j2\pi k\nu T}\tag{1}$$
and

$$\mathcal{Z}_{x}\left(\tau,\nu\right)=\left(\mathcal{Z}T_{\mathrm{F}}\ X\right)\left(\tau,\nu\right)\stackrel{{\Delta}}{{=}}\frac{1}{\sqrt{\pi}}e^{j2\pi\nu\tau}\sum_{k=-\infty}^{\infty}X\left(\nu+\frac{k}{T}\right)e^{j2\pi k\frac{\pi}{T}},\tag{2}$$

respectively, for $-\infty<\tau<\infty$ and $-\infty<\nu<\infty$. Here, $\mathcal{Z}T_{\mathrm{T}}$ and $\mathcal{Z}T_{\mathrm{F}}$ are linear mappings that map signals in 
time or frequency to DD.

We highlight that the convergence in (1) and (2) holds almost everywhere in the L2 space [32]. In what follows, we restrict ourselves by only considering cases where the above convergence holds without explicitly mentioning. Conversely, the inverse Zak transform gives the corresponding time domain and frequency domain signals based on the DD domain signal response, and it is defined in the following.

| Signal in time         | Signal in frequency   | After Zak transform   |
|------------------------|-----------------------|-----------------------|
| Delay-Doppler shifting |                       |                       |
| e                      |                       |                       |
| j                      |                       |                       |
| 2                      |                       |                       |
| πν                     |                       |                       |
| 1                      |                       |                       |
| (                      |                       |                       |
| t                      |                       |                       |
| −                      |                       |                       |
| τ                      |                       |                       |
| 1                      |                       |                       |
| )                      |                       |                       |
| x                      | (                     | t                     |
| −                      |                       |                       |
| τ                      |                       |                       |
| 1                      |                       |                       |
| )                      | e                     |                       |
| −                      |                       |                       |
| j                      |                       |                       |
| 2                      |                       |                       |
| πfτ                    |                       |                       |
| 1                      |                       |                       |
| X                      | (                     | f                     |
| −                      |                       |                       |
| ν                      |                       |                       |
| 1                      |                       |                       |
| )                      |                       |                       |
| e                      |                       |                       |
| j                      |                       |                       |
| 2                      |                       |                       |
| πν                     |                       |                       |
| 1                      |                       |                       |
| (                      |                       |                       |
| τ                      |                       |                       |
| −                      |                       |                       |
| τ                      |                       |                       |
| 1                      |                       |                       |
| )                      |                       |                       |
| Z                      |                       |                       |
| x                      |                       |                       |
| (                      | τ                     |                       |
| −                      |                       |                       |
| τ                      |                       |                       |
| 1                      |                       |                       |
| , ν                    |                       |                       |
| −                      |                       |                       |
| ν                      |                       |                       |
| 1                      |                       |                       |
| )                      |                       |                       |
| √                      |                       |                       |
| T                      |                       |                       |
| �                      |                       |                       |
|                        |                       |                       |
| 1                      |                       |                       |
| Multiplication in time |                       |                       |
| x                      | (                     | t                     |
| ∗                      |                       |                       |
| Y                      | (                     | f                     |
| 0                      |                       |                       |
| T                      |                       |                       |
| Z                      |                       |                       |
| x                      |                       |                       |
| (                      | τ, ν                  |                       |
| ′                      |                       |                       |
| )                      |                       |                       |
| Z                      |                       |                       |
| y                      |                       |                       |
| (                      | τ, ν                  |                       |
| −                      |                       |                       |
| ν                      |                       |                       |
| ′                      |                       |                       |
| )d                     | ν                     |                       |
| ′                      |                       |                       |
| Convolution in time    |                       |                       |
| x                      | (                     | t                     |
| ∗                      |                       |                       |
| y                      | (                     | t                     |
| 1                      |                       |                       |
| √                      |                       |                       |
| T                      |                       |                       |
| �                      |                       |                       |
| T                      |                       |                       |
| 0                      |                       |                       |
|                        | Z                     |                       |
| x                      |                       |                       |
| (                      | τ                     |                       |
| −                      |                       |                       |
| τ                      |                       |                       |
| ′                      |                       |                       |
| , ν                    | )                     |                       |
| Z                      |                       |                       |
| y                      |                       |                       |
| (                      | τ                     |                       |
| ′                      |                       |                       |
| , ν                    | )d                    | τ                     |
| ′                      |                       |                       |

Definition 2 (*Inverse Zak Transform*): Given a signal x (t), whose Fourier transform and Zak transform are given by X (f) and Zx (τ, ν), respectively, we have [22], [29]

$$x\left(t\right)=\left(\mathcal{I}\mathcal{Z}\mathcal{T}_{\mathrm{T}}\ \mathcal{Z}_{x}\right)\left(t\right)\overset{\Delta}{=}\sqrt{T}\int_{0}^{\frac{1}{T}}\mathcal{Z}_{x}\left(t,\nu\right)\mathrm{d}\nu.\tag{3}$$
and

$$X\left(f\right)=\left(\mathcal{I}\mathcal{Z}\mathcal{T}_{\mathbb{P}}\ \mathcal{Z}_{x}\right)\left(f\right)\stackrel{{\Delta}}{{=}}\frac{1}{\sqrt{I}}\int_{0}^{T}\mathcal{Z}_{x}\left(\tau,f\right)e^{-j2\pi f\tau}\mathrm{d}\tau.\tag{4}$$
Here, IZT T and IZT F are linear mappings that map signals in DD to time or frequency.

In Table I, we summarize some important properties of the Zak transform with respect to the time and frequency operations, which will be frequently used throughout this paper. In addition, the following two lemmas will also be widely used throughout the paper, whose proofs can be found in [22], [29].

Lemma 1 (*Quasi-Periodicity*): The Zak transform is quasi-periodic along the delay axis with period T and periodic along the Doppler axis with period 1
T , i.e.,

$${\cal Z}_{x}\left(\tau+T,\nu\right)=e^{j2\pi T\nu}{\cal Z}_{x}\left(\tau,\nu\right),\tag{5}$$
and

$${\cal Z}_{x}\left(\tau,\nu+\frac{1}{T}\right)={\cal Z}_{x}\left(\tau,\nu\right).\tag{6}$$
Lemma 2 (*Zak Transform vs. Ambiguity Function*): The cross ambiguity function for functions x (t) and y (t)
is defined by

$$A_{x,y}\left(\tau,\nu\right)\triangleq\int_{-\infty}^{\infty}x\left(t\right)y^{*}\left(t-\tau\right)e^{-j2\pi\nu\left(t-\tau\right)}\mathrm{d}t=\int_{-\infty}^{\infty}X\left(f\right)Y^{*}\left(f-\nu\right)e^{j2\pi ft\tau}\mathrm{d}f,\tag{7}$$
where X (f) and Y (f) are the corresponding Fourier transforms of x (t) and y (t), respectively. Then, given Zx (τ, ν) and Zy (τ, ν), the Zak transforms of x (t) and y (t), we have

$$\mathcal{Z}_{x}\left(\tau,\nu\right)\mathcal{Z}_{y}^{*}\left(\tau,\nu\right)=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}A_{x,y}\left(nT,\frac{m}{T}\right)e^{-j2\pi\nu T}e^{j2\pi\frac{\nu}{T}\tau}.\tag{8}$$
Conversely, we have

$$A_{x,y}\left(nT,\frac{m}{T}\right)=\int_{0}^{T}\int_{0}^{\frac{1}{T}}\mathcal{Z}_{x}\left(\tau,\nu\right)\mathcal{Z}_{y}^{*}\left(\tau,\nu\right)e^{-j2\pi\Phi\cdot\tau}e^{j2\pi\nu\tau T}\mathrm{d}\nu\mathrm{d}\tau.\tag{9}$$

Finally, we highlight that not all DD domain signals satisfy the properties of the Zak transform and applying
the inverse Zak transform to arbitrary DD domain signals may not yield meaningful time or frequency signals.

| [                 | ]   |
|-------------------|-----|
| DD                |     |
| ,                 | X   |
| DD domain         |     |
| matched-filtering |     |
| [                 | ]   |
| DD                |     |
| ,                 | Y   |
| DD domain         |     |
| pulse shaping     |     |
| DD domain         |     |
| channel           |     |
| DD                |     |
| Y                 |     |
| (                 | )   |
| (                 | )   |
| DD                |     |
| ,                 | h   |
| t n               |     |
| ,                 |     |
| DD                |     |
| ,                 |     |
| l                 |     |
| t n               |     |
| k                 |     |
| t n               |     |
| F                 |     |
| DD                |     |
| X                 |     |
| *                 |     |
| ,                 |     |
| DD                |     |
| ,                 |     |
| l                 |     |
| t n               |     |
| k                 |     |
| t n               |     |
| é                 | ù   |
| ë                 |     |
| F                 |     |
| û                 |     |
| (                 | )   |

Therefore, in this paper, we focus on the application of practical DD domain shaping pulses that satisfy (5) and (6)
and therefore have meaningful time and frequency representations given by (3) and (4). For such pulses, the socalled "fundamental rectangle" is an important concept, which is a range of DD components of size τ ∈ [0, T)
sufficiently described by the signal behaviour in the fundamental rectangle [29]. This fact will be used in the T
�
. As suggested in Lemma 1, DD domain pulses satisfying the quasi-periodicity property must be and ν ∈
�
0, 1
following part of this paper for constructing DD domain basis functions.

## Iii. Fundamentals Of Delay-Doppler Domain Signaling

In this section, we focus on the application of Zak transform for communication systems, where the transmitted continuous signal is constructed by modulating a set of discrete information symbols using basis functions. Specifically, we consider a type of DD domain signal transmissions for communication as shown in Fig. 1, where a set of discrete DD domain symbols are linearly modulated onto a family of continuous DD domain waveforms, i.e., DD
domain basis functions. Let XDD be the DD domain symbol matrix of size M × N, where M and N are numbers of delay and Doppler bins, respectively. Let XDD [l, k] be the (l, k)-th element of XDD, which is modulated onto the corresponding DD domain basis function Φτl,νk DD (τ, ν) via DD domain pulse shaping. Therefore, the considered linearly modulated DD communication signal is formulated as

$$s_{\rm DD}\left(\tau,\nu\right)=\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}X_{\rm DD}\left[l,k\right]\Phi_{\rm DD}^{\tau_{\rm DD}}\left(\tau,\nu\right),\tag{10}$$

where $\Phi_{\rm DD}^{\tau_{\rm DD}}\left(\tau,\nu\right)$ is the DD domain basis function with offset $\tau_{l}$ and $\nu_{k}$ and it will be detailed in the coming 
subsection.

In this paper, we consider an arbitrary DD domain channel hDD (τ, ν), which is written as [4]

$$h_{\rm DD}\left(\tau,\nu\right)=\sum_{p=1}^{P}h_{p}\delta\left(\tau-\tilde{r}_{p}\right)\delta\left(\nu-\tilde{r}_{p}\right).\tag{11}$$

In (11), $P$ can be interpreted as the number of resolvable paths, $h_{p}$, $\tilde{r}_{p}$, and $\tilde{r}_{p}$ are the channel coefficient, delay,
and Doppler shift corresponding to the p-th path, respectively, where ˜τp = ˜τp′ and ˜νp = ˜νp′ for p ̸= p′ do not hold simultaneously. Furthermore, we consider that hDD (τ, ν) satisfy the *crystallization* condition [25], [26], which requires that

$$\tilde{\tau}_{\rm max}-\tilde{\tau}_{\rm min}<T\quad\mbox{and}\quad\tilde{\nu}_{\rm max}-\tilde{\nu}_{\rm min}<\frac{1}{T},\tag{12}$$
respectively. Here, ˜τmax and ˜τmin are the maximum and minimum values of the delays, while ˜νmax and ˜νmin are the maximum and minimum values of the Doppler shifts. Essentially, the crystallization condition suggests that the channel is *underspread* [4], [33], which can be achieved by carefully selecting T with respect to the channel condition. Without loss of generality, we further assume that ˜τ ∈ [0, T) , ˜ν ∈
�
− 1

2T ,
    1
    2T
      �
        , which can be achieved

by synchronizing the signal according to ˜τmin and ˜νmin.

With the considered communication channel given by (11), the received DD domain signal rDD (τ, ν) can be

derived by the following theorem.

Theorem 1 (DD Domain Twisted Convolution): The DD domain received signal rDD (τ, ν) before adding noise

is the result of the twisted convolution between the DD domain transmitted signal sDD (τ, ν) and the DD domain

channel response hDD (τ, ν), i.e.,

$$r_{\rm DD}\left(\tau,\nu\right)=h_{\rm DD}\left(\tau,\nu\right)*_{*}*_{\rm DD}\left(\tau,\nu\right)\triangleq\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}s_{\rm DD}\left(\tau-\tau^{\prime},\nu-\nu^{\prime}\right)h_{\rm DD}\left(\tau^{\prime},\nu^{\prime}\right)e^{j2\pi\nu^{\prime}\left(\tau-\tau^{\prime}\right)}{\rm d}\nu^{\prime}{\rm d}\tau^{\prime},\tag{13}$$
where ∗σ is the twisted convolution operator [25].

Proof: Let sT (t) and rT (t) be the time domain signals corresponding to sDD (τ, ν) and rDD (τ, ν), respectively.

Then, according to [2], we have

$$r_{\rm T}\left(t\right)=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}h_{\rm DD}\left(\tau,\nu\right)e^{j2\pi\nu\left(t-\tau\right)}s_{\rm T}\left(t-\tau\right){\rm d}\nu{\rm d}\tau.\tag{14}$$
Then, by applying the Zak transform to rT (t), we obtain

T rDD (τ, ν) = √ k=−∞ rT (τ + kT) e−j2πkνT ∞ � T = √ −∞ −∞ hDD (τ ′, ν′) ej2πν′(τ+kT −τ ′)sT (τ + kT − τ ′) e−j2πkνT dν′dτ ′ � ∞ � ∞ k=−∞ ∞ � = √ −∞ −∞ � ∞ T � ∞ k=−∞ sT (τ − τ ′ + kT)e−j2πk(ν−ν′)T hDD (τ ′, ν′) ej2πν′(τ−τ ′)dν′dτ ′ ∞ � −∞ sDD (τ − τ ′, ν − ν′)hDD (τ ′, ν′) ej2πν′(τ−τ ′)dν′dτ ′. (15) −∞ � ∞ = � ∞ ■
To extract the transmitted information from the received signal rDD (τ, ν), we apply the matched filtering in the DD domain, yielding

$$Y_{\rm DD}\left[l,k\right]=\int_{0}^{T}\int_{0}^{\frac{1}{T}}r_{\rm DD}\left(\tau,\nu\right)\left[\Phi_{\rm DD}^{\tau_{l},\nu_{k}}\left(\tau,\nu\right)\right]^{*}{\rm d}\nu{\rm d}\tau,\tag{16}$$
where YDD is the set of sufficient statistics used for symbol detection. Based on the above overview of the DD
communications, we in the following discuss the design of DD domain basis functions.

## A. Delay-Doppler Domain Basis Functions

Recall that M and N are the numbers of delay and Doppler bins within the fundamental rectangle, respectively.

Thus, a family of equally-spaced DD domain basis functions can be defined by

$$\Xi_{\text{DD}}\triangleq\left\{\Phi_{\text{DD}}^{\tau_{l},\nu_{k}}\left(\tau,\nu\right)|\,\tau_{l}=l\frac{T}{M},\nu_{k}=k\frac{1}{NT},l\in\left\{0,...,M-1\right\},k\in\left\{0,...,N-1\right\}\right\}.\tag{17}$$
Each element in ΞDD is referred to as a DD domain basis function with delay and Doppler offsets τl and νk. To ensure that the family of basis functions in ΞDD can be efficiently implemented by a single prototype pulse in practice, we require that

$$\Phi_{\rm DD}^{\tau_{i},\nu_{h}}\left(\tau,\nu\right)=e^{j2\pi\nu_{h}\left(\tau-\tau_{i}\right)}\Phi_{\rm DD}^{0,0}\left(\tau-\tau_{i},\nu-\nu_{k}\right),\tag{18}$$
holds for any τ ∈ (−∞, ∞) and ν ∈ (−∞, ∞). The phase term ej2πνk(τ−τl) in (18) comes from the delay-Doppler shifting property in Table I, and it is applied to ensure that shifting the DD pulse Φ0,0
DD (τ, ν) along delay and Doppler axes by τl and νk is corresponding to the application of time delay τl and phase rotations ej2πνk(t−τl)
to the time domain equivalent pulse3, i.e., the time domain basis function Φ0,0
T (t). More specifically, applying the

inverse Zak transform in (3) to Φτl,νk
                                 DD (τ, ν), the time domain basis function Φτl,νk
                                                                              T
                                                                                   (t) can be shown to satisfy

$$\Phi_{\rm F}^{\tau_{1}\cdots\tau_{k}}\left(t\right)=\sqrt{T}\int_{0}^{T}\Phi_{\rm DD}^{\tau_{1}\cdots\tau_{k}}\left(t,\nu\right){\rm d}\nu=e^{j2\pi\nu_{k}\left(t-\tau\right)}\Phi_{\rm F}^{0,0}\left(t-\tau_{l}\right).\tag{19}$$

Similarly, we can also derive the frequency domain basis function $\Phi_{\rm F}^{0,\tau_{1}}\left(f\right)$ based on (4), i.e.,

$$\Phi_{\rm F}^{\tau_{1}\cdots\tau_{k}}\left(f\right)=\frac{1}{\sqrt{T}}\,\int_{0}^{T}\Phi_{\rm DD}^{\tau_{1}\cdots\tau_{k}}\left(\tau,f\right)e^{-j2\pi f\tau}{\rm d}\tau=e^{-j2\pi f\tau_{1}}\Phi_{\rm F}^{0,0}\left(f-\nu_{k}\right).\tag{20}$$
From (19) and (20), we observe that the construction in (18) allows the symmetrical treatment for both time and frequency, where the time and frequency domain basis functions are of similar structure, i.e., a carrier that is time/frequency shifted and phase-rotated. In what follows, we shall refer to (18) as the TF-consistency condition defined in the DD domain, and we say a family of DD domain basis functions are *TF-consistent* if the functions within ΞDD satisfy (18). In particular, for TF-consistent family of DD domain basis functions, the following lemma holds.

Lemma 3 (*DD shifts for TF-consistent DD basis functions*): Let (τ0, ν0) be a pair of delay and Doppler offsets with arbitrary values. Then, for Φτ1,ν1
DD (τ, ν) from ΞDD, we have

$$e^{j2\pi\nu_{1}(\tau-\tau_{1})}\Phi_{\rm DD}^{0,0}\left(\tau-\tau_{0}-\tau_{1},\nu-\nu_{0}-\nu_{1}\right)=e^{j2\pi\nu_{1}\tau_{0}}\Phi_{\rm DD}^{\tau_{1}\nu_{1}}\left(\tau-\tau_{0},\nu-\nu_{0}\right).\tag{21}$$
Proof: Define τ ′ = τ − τ0 and ν′ = ν − ν0. Then,

$$e^{j2\pi\nu_{1}(r-r_{1})}\Phi_{\rm DD}^{0,0}\left(r-\tau_{0}-\tau_{1},\nu-\nu_{0}-\nu_{1}\right)=e^{j2\pi\nu_{1}\tau_{0}}e^{j2\pi\nu_{1}\left(r^{\prime}-\tau_{1}\right)}\Phi_{\rm DD}^{0,0}\left(r^{\prime}-\tau_{1},\nu^{\prime}-\nu_{1}\right)\tag{22}$$ $$=e^{j2\pi\nu_{1}\tau_{0}}\Phi_{\rm DD}^{\tau_{1}\nu_{1}}\left(\tau-\tau_{0},\nu-\nu_{0}\right).$$
■
From (18) and (21), we notice that the TF-consistency condition states that the basis functions are symmetrically modulated in both time and frequency following the same operations. More importantly, the following theorem shows the important connection between TF consistency and ambiguity function.

Theorem 2 (*TF-consistency vs. Ambiguity Function*): Let (τ1, ν1) and (τ2, ν2) be two pairs of arbitrary delay

and Doppler offsets. Then, the following holds

$$\begin{split}&\int_{0}^{T}\int_{0}^{+}e^{j2\pi\nu_{2}(r-r_{1})}\mathcal{Z}_{x}\left(r-r_{2},\nu-\nu_{2}\right)e^{-j2\pi\nu_{1}(r-r_{1})}\mathcal{Z}_{x}^{*}\left(r-r_{1},\nu-\nu_{1}\right)\mathrm{d}\nu\mathrm{d}\tau\\ &=e^{j2\pi\nu_{2}(r_{1}-r_{2})}A_{x}\left(r_{1}-r_{2},\nu_{1}-\nu_{2}\right),\end{split}\tag{23}$$
where Ax (∆τ, ∆ν) denotes the auto-ambiguity function of x (t) with respect to the delay offset ∆τ and Doppler

offset $\Delta\nu$. Particularly, for $\Phi_{\text{DD}}^{\text{x,y,x}}\left(\tau,\nu\right)$ and $\Phi_{\text{DD}}^{\text{x,y}}\left(\tau,\nu\right)$ belonging to $\mathfrak{B}_{\text{DD}}$, (23) suggests

$$\int_{0}^{T}\int_{0}^{\frac{T}{2}}\Phi_{\text{DD}}^{\text{x,y}}\left(\tau,\nu\right)\left(\Phi_{\text{DD}}^{\text{x,y}}\left(\tau,\nu\right)\right)^{*}\text{d}\nu\text{d}\tau=e^{j2\pi\nu_{0}\left(\tau_{1}-\tau_{2}\right)}A_{\Phi}\left(\tau_{1}-\tau_{2},\nu_{1}-\nu_{2}\right),\tag{24}$$

where $A_{\Phi}\left(\Delta\tau,\Delta\nu\right)$ denotes the auto-ambiguity function of $\Phi_{\text{T}}^{0,0}\left(t\right)$.

Proof: The theorem can be straightforwardly derived based on Lemma 2 and the delay-Doppler shifting property in Table I.

■
Notice that (24) is of the form of DD domain matched-filtering. Essentially, the property in (24) suggests that the DD domain signal transmission with a family of TF-consistent DD domain basis functions can be characterized the ambiguity function of Φ0,0
T (t). Given above, we shall view Φ0,0
DD (τ, ν) as the DD domain *prototype pulse* for DD pulse shaping.

Remark 1: We highlight that the above description aligns with the DD domain modulation discussed in [25],
[26], where the authors have shown that the twisted-convolution discussed in Theorem 1 is the DD domain basic operations characterizing the DD pulse shaping, signal transmission, and the matched-filtering. In comparison to this descriptions, the description above highlights the intrinsic connections among different DD domain basis functions from the view point of communication theory by explicitly offering the mathematical description of carrier pulses with respect to each information symbol. In the following subsections, we will reveal the important insights of such constructions for practical communication implementations.

## B. Constructing Delay-Doppler Domain Basis Functions

Note that any DD domain signal satisfying the quasi-periodicity property can be sufficiently characterized by the corresponding response in the fundamental rectangle. Thus, we are motivated to construct the DD domain basis function by extending the "atom pulse" in the fundamental rectangle following the quasi-periodicity. Let ϕ (τ, ν)
be the atom pulse, whose support is the fundamental rectangle. According to Lemma 1, Φ0,0
DD (τ, ν) can then be obtained by quasi-periodically extending ϕ (τ, ν) [25], [26], such as

$$\Phi_{\rm DD}^{0,0}\left(\tau,\nu\right)\stackrel{{\Delta}}{{=}}\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\varphi\left(\tau-nT,\nu-\frac{m}{T}\right)e^{j2\pi\nu T}.\tag{25}$$
By substituting (25) into (18), we obtain

$$\Phi_{\rm DD}^{\tau_{\rm f},\nu_{\rm h}}\left(\tau,\nu\right)=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}e^{j2\pi\nu_{\rm h}\left(\tau-\tau_{\rm f}\right)}\varphi\left(\tau-\tau_{\rm f}-nT,\nu-\nu_{\rm h}-\frac{m}{T}\right)e^{j2\pi n(\nu-\nu_{\rm h})T}.\tag{26}$$

We summarize the properties of the DD domain basis functions in Fig. 2, where we assume that $M=N=2$
such that there are MN = 4 DD domain basis functions in the fundamental rectangle. We observe that the DD
domain basis functions exhibit quasi-periodicity globally, and its constructed by locally twisted-shifting the atom pulse ϕ (τ, ν). Specifically, the quasi-periodicity aligns with the property of the Zak transform, which characterizes the global structure of the DD domain basis functions across infinite numbers of regions with the size of the fundamental rectangle. On the other hand, the twisted-shift aligns with the TF-consistency condition, characterizing the local structure of the DD domain basis functions across M delay bins and N Doppler bins.

The significance of the characteristics of the DD domain basis functions have been discussed [25], [26]. But here we propose a different viewpoint from the DD domain pulse structures. We argue that the global and local characteristics allow the DD domain basis functions have direct time domain and frequency domain interpretations via exploiting the properties of the Zak transform, e.g., (3) and (4). Specifically, by substituting (25) into (19), we obtain the time domain basis function by

$$\Phi_{\rm T}^{0,0}\left(t\right)=\sqrt{T}\int_{0}^{\frac{T}{4}}\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\varphi\left(t-nT,\nu-\frac{m}{T}\right)e^{j2\pi\nu nT}{\rm d}\nu=\sqrt{T}\sum_{n=-\infty}^{\infty}\int_{-\infty}^{\infty}\varphi\left(t-nT,\nu\right)e^{j2\pi\nu nT}{\rm d}\nu.\tag{27}$$
Similarly, by substituting (26) into (4), we obtain the frequency domain basis function by

$$\Phi_{\rm F}^{0,0}\left(f\right)=\frac{1}{\sqrt{T}}\,\int_{0}^{T}\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\varphi\left(\tau-nT,f-\frac{m}{T}\right)e^{j2\pi nfT}e^{-j2\pi f\tau}{\rm d}\tau\tag{28}$$ $$=\frac{1}{\sqrt{T}}\,\sum_{m=-\infty}^{\infty}\int_{-\infty}^{\infty}\varphi\left(\tau,f-\frac{m}{T}\right)e^{-j2\pi f\tau}{\rm d}\tau.$$
Furthermore, according to (19) and (4), we have

$$\Phi_{\rm T}^{\tau_{\rm f}\tau_{\rm h}}\left(t\right)=e^{j2\pi\nu_{\rm h}\left(t-\tau_{\rm f}\right)}\Phi_{\rm T}^{0,0}\left(t-\tau_{\rm f}\right)=\sqrt{T}e^{j2\pi\nu_{\rm h}\left(t-\tau_{\rm f}\right)}\sum_{n=-\infty}^{\infty}\int_{-\infty}^{\infty}\varphi\left(t-\tau_{\rm f}-nT,\nu\right)e^{j2\pi\nu T}{\rm d}\nu,\tag{29}$$
and

T Φτl,νk F (f) = e−j2πfτlΦ0,0 F (f − νk) = 1 √ � ∞ m=−∞ � e−j2πfτdτ. (30) −∞ ϕ � τ, f − νk − m T e−j2πfτl ∞ �
Based on (29) and (30), we observe that the DD domain basis functions can be understood as a mixture of the time domain and frequency domain pulses/tones [25], [26], by noticing that integrals in (29) and (30) result in purely one-dimensional (1D) time and frequency signals. As an example, we demonstrate the basis functions in different domains in Fig. 3, where we assume M = N = 2 and mark the corresponding time and frequency pulses the same colors as those in the DD grids. As shown in the figure, the DD domain basis function becomes 1D pulsone in either time or frequency, while showing a particular response pattern according to the delay and Doppler offsets. Particularly, we have the following observations:

- DD domain global properties characterize the time and frequency periodicity: The DD domain global
characteristics are translated into the summation and integral terms in (29) and (30), which leads to a train of
pulses in the time and frequency domains that are apart in time by T and apart in frequency by 1
T , respectively.
- DD domain local properties characterize time and frequency tones: The DD domain local characteristics
are translated into the phase terms (signal tones) ej2πνk(t−τl) and e−j2πfτl in (29) and (30).
- Time and frequency spreading: The DD domain basis function is spread in both time and frequency
simultaneously following a periodic manner with respect to T and
1
T , leading to a potential of achieving
full channel diversity4. Specifically, the special signal structure of (29) and (30) is known as the *pulsone* [25],
[26], which is essentially a *pulse train* modulated by a *complex tone*.
- Time and frequency limiting cases: By letting T → ∞, the time domain basis functions are separated only
by the time offset τl, yielding a pure time division multiplexing (TDM)-type of signaling; By letting T → 0,
the frequency domain basis functions are separated only by the frequency offset νk, yielding a pure frequency
division multiplexing (FDM)-type of signaling.

## Iv. Properties Of Dd Domain Basis Function And It'S Truncation

In this section, we study the properties of DD domain basis functions based on the fundamental understanding from the previous sections. Perhaps, the *ideal* DD domain basis functions may be a set of quasi-periodically extended delta pulses (distributions), i.e., ϕ (τ, ν) = δ (τ) δ (ν), which are ideally localized in the fundamental rectangle and thereby minimizes the interference among information symbols. It should be noted that the wellknown *Heisenberg's uncertainty principle* forbids the existence of fully localized pulses in the TF domain [34].

However, the Heisenberg's uncertainty principle does not apply to the Zak domain directly. More specifically, we shall highlight that the ideal DD domain basis functions are only fully localized in the fundamental rectangle, while are in fact quasi-periodic in the whole DD domain globally according to (26). Particularly, by considering

$$\Phi_{\rm DD}^{\tau_{1}\tau_{k}}\left(\tau,\nu\right)=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}e^{j2\pi\nu_{k}\left(\tau-\tau_{l}\right)}\delta\left(\tau-\tau_{l}-nT\right)\delta\left(\nu-\nu_{k}-\frac{m}{T}\right)e^{j2\pi\nu_{k}\left(\nu-\nu_{k}\right)T},\tag{31}$$
we obtain

$$\Phi_{\rm T}^{\tau_{1}\cdot\nu_{\rm n}}\left(t\right)=\sqrt{T}e^{j2\pi\nu_{\rm n}\left(t-\tau_{1}\right)}\sum_{n=-\infty}^{\infty}\delta\left(t-\tau_{1}-nT\right),\tag{32}$$
and

$$\Phi_{\rm F}^{\tau_{1},\nu_{k}}\left(f\right)=\frac{1}{\sqrt{T}}e^{-j2\pi f\tau_{1}}\sum_{m=-\infty}^{\infty}\delta\left(f-\nu_{k}-\frac{m}{T}\right)\tag{33}$$
respectively. Furthermore, we have

$$A_{\Phi}\left(\tau_{1}-\tau_{2},\nu_{1}-\nu_{2}\right)=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\delta\left(\tau_{1}-\tau_{2}-nT\right)\delta\left(\nu_{1}-\nu_{2}-\frac{m}{T}\right),\tag{34}$$

whose detailed derivation is given in Appendix A. In DD communications, the ambiguity function of the form 
of (34) minimizes the potential interference among different information symbols, but it only exists in theory but not in practice, because (32) and (33) clearly suggest infinite time and frequency resources. Therefore, we propose to apply practical filters and windows to limit the occupied TF resources of (32) and (33).

## A. Time-Frequency Consistent Filtering And Windowing

The idea of applying filtering and windowing for limiting the TF resources is straightforward, and previous implementation on OTFS based on this appears in [24]. However, what is not obvious and easy to be overlooked is the TF-consistency condition. We have shown in (23) that the TF-consistency condition directly connects the DD domain matched-filtering and the ambiguity function. Consequently, filtering or windowing that does not align with the TF-consistency will break the DD domain integrity, and therefore degrades the communication performance.

In the following, we study the time domain TF-consistent filtering/windowing for the sake of practical implementation. For a family of DD domain basis functions, we shall define the TF-consistent filtering/windowing in the following Proposition.

Proposition 1 (*TF-Consistent Filtering/Windowing*): Define a family of DD domain basis functions ΞDD that are delay and Doppler shifted with respect to a prototype pulse Φ0,0
DD (τ, ν) in a TF-consistent manner, i.e., (18).

Define another family of DD domain basis functions ˜ΞDD that are obtained by time domain filtering or windowing each corresponding time domain basis function from ΞDD. We call the filtering/windowing is TF-consistent if and only if ˜ΞDD is TF-consistent.

To study the operational meaning of the TF-consistent filtering/windowing. Let us define an arbitrary time domain function x (t) as the filter/window function. Let us first study the TF-consistent time domain filtering. We define

˜Φ0,0
  DD (τ, ν) =
                 1
                √

we shall write

T
 � T
  0 Φ0,0
      DD (τ − τ′, ν) Zx (τ ′, ν)dτ ′, i.e., ˜Φ0,0
                                    T (t) = Φ0,0
                                              T (t)∗x (t). Immediately from Proposition 1,

$$e^{j2\pi\nu_{0}(\tau-\tau_{0})}\tilde{\Phi}^{0,0}_{\rm DD}\left(\tau-\tau_{0},\nu-\nu_{0}\right)=\frac{1}{\sqrt{\mathcal{I}}}\,\int_{0}^{T}e^{j2\pi\nu_{0}(\tau-\tau_{0})}\Phi^{0,0}_{\rm DD}\left(\tau-\tau^{\prime}-\tau_{0},\nu-\nu_{0}\right)\mathcal{Z}_{\pi}\left(\tau^{\prime},\nu-\nu_{0}\right)\mathrm{d}\tau^{\prime}$$ $$=\frac{1}{\sqrt{\mathcal{I}}}\,\int_{0}^{T}e^{j2\pi\nu_{0}\tau^{\prime}}\Phi^{\nu_{0},0}_{\rm DD}\left(\tau-\tau^{\prime},\nu\right)\mathcal{Z}_{\pi}\left(\tau^{\prime},\nu-\nu_{0}\right)\mathrm{d}\tau^{\prime}.\tag{35}$$
where (35) comes from (21). By taking the inverse Zak transform of (35), we obtain

$$\hat{\Phi}_{T}^{x_{\rm{D}},\nu}\left(t\right)=\Phi_{T}^{x_{\rm{D}},\nu}\left(t\right)*\left(e^{j2\pi\nu t}x\left(t\right)\right).\tag{36}$$

For the time domain windowing, let us define $\hat{\Phi}_{\rm{DD}}^{x_{\rm{D}}}\left(\tau,\nu\right)=\sqrt{\tau}\ \int_{0}^{\tau}\Phi_{\rm{DD}}^{\rm{D}}\left(\tau,\nu-\nu^{\prime}\right)\mathcal{Z}_{x}\left(\tau,\nu^{\prime}\right)\mathrm{d}\nu^{\prime}$, i.e., $\hat{\Phi}_{T}^{x_{\rm{D}}}\left(t\right)=\left(\frac{\tau}{\tau}\right)^{\frac{\nu}{\nu}}$.

Φ0,0
 T (t) x (t). Again from Proposition 1, we shall write

$$\overline{T}\int_{0}^{\overline{T}}$$ $$e^{j2\pi\nu_{0}\left(\tau-\tau_{0}\right)}\tilde{\Phi}_{\rm DD}^{\,0,0}\left(\tau-\tau_{0},\nu-\nu_{0}\right)=\sqrt{T}\int_{0}^{+}e^{j2\pi\nu_{0}\left(\tau-\tau_{0},\nu-\nu^{\prime}\right)}\Phi_{\rm DD}^{\,0,0}\left(\tau-\tau_{0},\nu-\nu_{0}-\nu^{\prime}\right)\mathcal{Z}_{x}\left(\tau-\tau_{0},\nu^{\prime}\right)\mathrm{d}\nu^{\prime}$$ $$=\sqrt{T}\int_{0}^{+}\Phi_{\rm DD}^{\,\nu_{0}\nu_{0}}\left(\tau,\nu-\nu^{\prime}\right)\mathcal{Z}_{x}\left(\tau-\tau_{0},\nu^{\prime}\right)\mathrm{d}\nu^{\prime},\tag{37}$$
where (37) comes from (21). By taking the inverse Zak transform of (37), we obtain

$$\tilde{\Phi}_{\rm T}^{\tau_{0},\nu_{0}}\left(t\right)=\Phi_{\rm T}^{\tau_{0},\nu_{0}}\left(t\right)x\left(t-\tau_{0}\right).\tag{38}$$
It can be seen from that (36) and (38) suggest that TF-consistency condition can be preserved if the filter/window function is frequency/time shifted according to the Doppler/delay offsets. In fact, this result is not unexpected.

Note that both ΞDD consists of a family of pulses with different Doppler/delay offsets. Therefore, to make sure each pulse undergoes the exactly same effect of filtering/windowing, it is necessary to also adapt the filter/window response according to the Doppler/delay offsets.

## B. Dd Domain Tf-Consistent Pulse Shaping With Truncated Periodic Signals

We now discuss the DD domain basis function after TF-consistent filtering and windowing. Considering the practical implementation of DD communications, we restrict ourselves to only consider the case that the DD
domain basis function is firstly truncated in frequency and then truncated in time following the TF-consistency condition. As a result, we shall notice that such a truncation produces a roughly time and frequency limited signal.

Let ˜Φτ0,ν0
DD (τ, ν) be the truncated DD domain basis function, whose equivalent time domain representation satisfies

$$\Phi_{\rm T}^{\rm w,\,t_{0}}\left(t\right)\triangleq\left\{\Phi_{\rm T}^{\rm w,\,t_{0}}\left(t\right)\bullet\left(e^{j2\pi\omega_{\rm T}t}\mathsf{FWT}\left(t\right)\right)\right\}\,\mathsf{TW}_{\rm T}\left(t-r_{0}\right),\tag{39}$$

where $\mathsf{FWT}_{\rm T}\left(t\right)$ and $\mathsf{TW}_{\rm T}\left(t\right)$ are the time domain representations of arbitrary frequency domain and time domain 
windows, respectively. Corresponding to (39), the frequency domain basis function after truncation is given by

$$\tilde{\Phi}_{\rm D}^{\gamma_{\rm D}\,\nu_{0}}\left(f\right)\stackrel{{\Delta}}{{=}}\left\{\Phi_{\rm D}^{\gamma_{\rm D}\,\nu_{0}}\left(f\right){\rm FW}_{\rm F}\left(f-\nu_{0}\right)\right\}*\left(e^{j2\pi\,f\,\nu_{0}}{\rm TW}_{\rm F}\left(f\right)\right).\tag{40}$$

Furthermore, according to the properties in Table I, we obtain the truncated DD domain basis function as

$$\tilde{\Phi}_{\rm DD}^{\gamma_{\rm D}\,\nu_{0}}\left(\tau,\nu\right)=\int_{0}^{\frac{1}{2}}\int_{0}^{T}\Phi_{\rm DD}^{\gamma_{\rm D}\,\nu_{0}}\left(\tau-\tau^{\prime},\nu-\nu^{\prime}\right){\rm FW}_{\rm DD}\left(\tau^{\prime},\nu-\nu^{\prime}-\nu_{0}\right)e^{j2\pi\,\nu_{0}\,\tau^{\prime}}{\rm TW}_{\rm DD}\left(\tau-\tau_{0},\nu^{\prime}\right){\rm d}\tau^{\prime}{\rm d}\nu^{\prime}.\tag{41}$$
By substituting (31) into (42) and considering τl = νk = 0, we obtain

˜Φ0,0 DD (τ, ν) T 0 0 � T = � 1 T n=−∞ � ej2πn(ν−ν′)T FWDD (τ ′, ν − ν′)TWDD (τ, ν′) dτ ′dν′ m=−∞ δ (τ − τ ′ − nT)δ � ν − ν′ − m ∞ � ∞ � T = T T m T � (n+1)T � m+1 n=−∞ m=−∞ nT δ (τ −τ ′) δ (ν−ν′) ej2πn(ν−ν′)T FWDD � τ ′ − nT, ν − ν′ − m � TWDD � τ, ν′ − m � dτ ′dν′ ∞ � ∞ � −∞ −∞ δ (τ − τ′) δ (ν − ν′) FWDD (τ ′, ν − ν′)TWDD (τ, ν′) dτ ′dν′ = � ∞ � ∞ =FWDD (τ, 0) TWDD (τ, ν) . (42)
It is not surprising to see from (42) that the truncated DD domain basis function is fully determined by the DD domain representations of the time and frequency windows. More specifically, we notice that the the resultant truncated DD domain basis function coincide with the shape of the time domain window along the Doppler axis, while its response along the delay axis is determined jointly by both the time and frequency domain windows.

To further discuss the insight based on (42), let us consider time and frequency windows with specific constraints.

We consider the time domain window has a finite time duration from t ∈
                                                                      �
                                                                       0, ˜NT
                                                                             �
                                                                              , while the frequency domain

window has a finite bandwidth f ∈
                                  �
                                    0,
                                      ˜
                                      M
                                      T
                                        �
                                         , respectively, where ˜N ≥ N and
                                                                           ˜
                                                                          M ≥ M. Notice that the Zak

transform involves periodic summations in time or frequency as shown in (1) and (2). We are motivated to consider

periodic windows in time and frequency for DD basis function truncation. Specifically, we call a time domain

window TWT (t) T -periodic if TWT (t) = TWT (t + T ), for t ∈
                                                   �
                                                   0,
                                                     �
                                                      ˜N − 1
                                                           �
                                                             T
                                                              �
                                                               . Similarly, a frequency domain

T
�
. With time and frequency periodic windows described above, (42) is

˜
M
T -periodic window satisfies f ∈
                                   �
                                    0,
                                       ˜
                                       M−1

further simplified by

$$\Phi_{\text{DD}}^{0,0}\left(r,\nu\right)=\frac{1}{\sqrt{\Upsilon}}\,\sum_{t=0}^{\Omega-1}\mathsf{PW}_{\text{F}}\left(\frac{t}{T}\right)e^{j2\pi\text{i}\phi}\sqrt{\Upsilon}\sum_{k=0}^{\Omega-1}\mathsf{TW}_{\text{T}}\left(r+kT\right)e^{-j2\pi\text{i}\nu T}\tag{43}$$ $$=\mathsf{FW}_{\text{F}}\left(0\right)\mathsf{TW}_{\text{T}}\left(\tau\right)\sum_{k=0}^{\Omega-1}e^{j2\pi\text{i}\phi}\sum_{k=0}^{\Omega-1}e^{-j2\pi\text{i}\nu T}$$ $$=\mathsf{FW}_{\text{F}}\left(0\right)\mathsf{TW}_{\text{T}}\left(\tau\right)e^{j\pi\left(\tilde{N}_{\text{T}}\left(\tilde{N}_{\text{T}}\right)+\phi_{-}j\pi\left(\tilde{N}_{-1}\right)\right)\tau}\frac{\sin\left(\pi\tilde{M}\tilde{\Upsilon}\right)}{\sin\left(\pi\tilde{\Upsilon}\right)}\frac{\sin\left(\pi\tilde{N}\nu T\right)}{\sin\left(\pi\nu T\right)},$$

where the summations in (43) are commonly referred to as the Dirichlet kernel. Furthermore, it is interesting to 
T )

notice from (44) that the signal strength of ˜Φ0,0
                                              DD (τ, ν) is dominated by the terms
                                                                                    sin(π ˜
                                                                                         M τ

sin(πνT ) . In fact,

sin(π τ

T )
    and
        sin(π ˜
             NνT)

T )

signals of the form of
                       sin(π ˜
                           M τ

sin(πνT )
            are commonly referred to as aliased sinc functions, or for short,

sin(π τ

T )
    and
         sin(π ˜
             NνT)

asinc functions, in the literature, which are a special type of quasi-orthogonal signals with respect to the intervals T

sin(πνT ) , its value is zero if ν is integer multiple of the quasi-orthogonality period
                                                                                                           1

NT ,

                                                                                                                    ˜
                                                                                                                   M
and
     1
     ˜
    NT , respectively. For sin(πNνT )

except for the case where ν = lN

NT with any integer l. Therefore, the DD domain basis function of the form (44) is

desirable in the sense that it naturally provides sufficient orthogonality in the fundamental rectangle for τ ∈ [0, T)

This observation indicates that DD Nyquist communications can be achieved by simply applying periodic windows

T
 �
  . Moreover, (44) suggests that any periodic windows essentially lead to very similar ˜Φ0,0
                                                                               DD (τ, ν).

and ν ∈
       �
        0, 1

without the need of sophisticated pulse design.

For completeness, let us also discuss the time and frequency domain basis functions after such windowing. Note

that the time and frequency domain windows are of finite duration. Therefore, their signal responses are invariant

after multiplying a rectangular window function in the corresponding domain, such as

$$\hat{\Phi}_{\mathrm{T}}^{\,\tau_{0}\,\tau_{0}}\left(t\right)=\frac{\hat{M}}{T}\,\left\{\Phi_{\mathrm{T}}^{\,\tau_{0}\,\tau_{0}}\left(t\right)*\left(e^{j2\pi\tau_{0}\,t\,e^{j2\pi\frac{\hat{M}}{T}t}\mathrm{FWT}_{\mathrm{T}}\left(t\right)\mathrm{sinc}\left(\frac{\hat{M}}{T}t\right)}\right)\right\}\mathrm{TWT}_{\mathrm{T}}\left(t-\tau_{0}\right)$$ $$=\frac{\hat{M}}{\sqrt{T}}e^{j2\pi\tau_{0}\left(t-\tau_{0}\right)}\sum_{n=-\infty}^{\infty}e^{j2\pi\frac{\hat{M}}{T}\left(t-\tau_{0}\right)}\mathrm{FWT}_{\mathrm{T}}\left(t-\tau_{0}-nT\right)\mathrm{sinc}\left(\frac{\hat{M}}{T}\left(t-\tau_{0}-nT\right)\right)\mathrm{TWT}_{\mathrm{T}}\left(t-\tau_{0}\right),\tag{45}$$
and

$$\hat{\Phi}_{\rm F}^{\rm v_{0}\to v_{0}}\left(f\right)=\tilde{N}T\left\{\Phi_{\rm F}^{\rm v_{0}\to v_{0}}\left(f\right){\sf P}{\sf W}_{\rm F}\left(f-v_{0}\right)\right\}*\left(e^{j2\pi f\nu_{0}}e^{-j\pi\tilde{N}\,f\,T}{\sf W}_{\rm F}\left(f\right){\rm sinc}\left(\tilde{N}Tf\right)\right)\tag{46}$$ $$=\tilde{N}\sqrt{T}e^{-j\pi f\nu_{0}}\sum_{m=-\infty}^{\infty}e^{-j\pi\tilde{N}\,(f-\nu_{0})T}{\sf W}_{\rm F}\left(f-\nu_{0}-\frac{m}{T}\right){\rm sinc}\left(\tilde{N}T\left(f-\nu_{0}-\frac{m}{T}\right)\right){\sf P}{\sf W}_{\rm F}\left(\frac{m}{T}\right).$$
Based on (45) and (46), we observe that both the time and frequency domain basis still follows the pulsone structure, but, instead of the periodic summation of delta functions in (32) and (33), the basis functions are constituted by the periodic summation of the product of the window function and sinc pulse. The time and frequency domain basis functions with rectangular windows are shown in Fig. 4(a) and Fig. 4(b), where M = 16, N = 8, and T = 1. As shown in the figure, the basis functions in both time and frequency domains remain the pulsone structure, where the " local pulses" in time and frequency are sufficiently narrow and are separated by T and 1/T , respectively. In fact, this is not unexpected as the width of these pulses are roughly determined by the inverse of the windows'
bandwidth and time duration [25], [26]. We shall refer to this property as the *TF separability property* of the basis function, which holds sufficiently in the asymptotical regime, i.e., sufficiently large ˜
M and ˜N. Furthermore, we note that the frequency domain signal has slight excessive bandwidth due to the time domain windowing, which is commonly referred to as the OOB emission. Note that the impact of the OOB emission is determined by the underlying time domain window.

We demonstrate the truncated DD domain basis functions with different windows in Fig. 5(a) to Fig. 5(d), including the rectangular window (termed "Rect + Rect"), the root-raised cosine (RRC) window5 with a roll-off factor 0.3 (termed "RRC + RRC"), and cosine window (termed "Cos + Cos"), which is obtained by truncating the

continuous cosine signal cos (t) from t ∈
                                         �
                                          0, ˜NT
                                                �
                                                  in time and f ∈
                                                                  �
                                                                   0,
                                                                       ˜
                                                                      M
                                                                      T
                                                                        �
                                                                          in frequency, respectively. Specifically,

we consider M = N = 32 and T = 1, and we intentionally consider the DD domain basis function located in

the middle of the fundamental rectangle for a better illustration. For both "Rect + Rect" and "Cos + Cos" cases,

we have ˜
       M = M and ˜N = N, while for the "RRC + RRC" case, ˜
                                                          M and ˜N are slightly larger than M and N

to account for the excessive bandwidth/time duration. From Fig. 5(a), we observe that using rectangular windows for basis function truncation results in a sufficiently localized pulse in the DD domain, while suffering from slight

power leakage in both the delay and Doppler dimensions. Furthermore, for RRC windows with excessive time and frequency resources, we can see that the truncated basis function is still sufficiently localized but enjoys a much less power leakage in both the delay and Doppler dimensions, as shown in Fig. 5(b). This is thanks to the quick decay property of RRC pulses. The delay and Doppler responses of truncated DD domain basis functions with the three windows are presented in Fig. 5(c) and Fig. 5(d). From these two figures, we notice that both "Rect + Rect"
and "Cos + Cos' cases share roughly the same delay and Doppler responses, except for the fact that the "Cos
+ Cos" case shows slightly less power leakage around τ = 0.25 and τ = 0.75. This observation is in line with our derivation in (44), where the actual shape of the time domain window only affect the delay domain response slightly. On the other hand, we notice that the "RRC + RRC" case indeed enjoys a quick decay in both delay and Doppler dimensions. However, it may not enjoy the perfect orthogonality as "Rect + Rect" and "Cos + Cos" cases, as some non-zero values appear at integer times of delay and Doppler resolution.

## C. The Ambiguity Function Of Truncated Dd Domain Basis Functions

In this subsection, we will focus on the ambiguity function of truncated DD domain basis functions. We have demonstrated some properties of truncated DD domain basis functions using some specific windows. Here, we will continue our discussions by highlighting their connections to the ambiguity function. Notice that after TF-
consistent filtering and windowing, the ambiguity function of ˜Φ0,0
DD (τ, ν) sufficiently characterizes the DD domain matched-filtering output. Therefore, we are motivated to only consider the ambiguity function of ˜Φ0,0
DD (τ, ν), which is defined as A˜Φ (τ, ν). In particular, the following theorem characterizes the connections between A˜Φ (τ, ν) and the adopted windows.

Theorem 3 (*Ambiguity Function of Truncated Basis Function*): For DD domain basis functions of the form (31)
that are frequency and time truncated as (42), its ambiguity function satisfies

$$A_{4}\left(\tau,\nu\right)=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}A_{\text{FW}}\left(\tau-nT,\frac{m}{T}\right)A_{\text{FW}}\left(\tau,\nu-\frac{m}{T}\right).\tag{47}$$

**Proof:** The proof is given in Appendix B.

Theorem 3 states that the ambiguity function of truncated DD domain basis functions can be represented by infinite summations of the ambiguity function of the adopted windows in both time and frequency. From Theorem 3, various truncated DD domain basis functions with desired ambiguity function can be designed by carefully selecting the windows in time and frequency. For completeness, we shall also highlight the calculation of A˜Φ (τ, ν) from the DD domain by making use of the TF-consistency condition. Recalling (24), and considering (43), after some mathematical manipulations, we arrive at

$$A_{\Phi}\left(\tau_{1},n_{1}\right)=\int_{0}^{T}\int_{0}^{\tau}\hat{\Phi}_{\text{DD}}^{\text{op}}\left(\tau,\nu\right)\left[\hat{\Phi}_{\text{DD}}^{\text{op}}\left(\tau,\nu\right)\right]^{\text{\tiny{$\alpha$}}}\text{d}\nu\tag{48}$$ $$=\frac{\left|\text{FW}_{T}\left(0\right)\right|^{2}}{T}\sum_{k=0}^{N-1}e^{-j2\pi kn_{1}T}\sum_{l=0}^{N-1}\sum_{p=0}^{N-1}\int_{0}^{T}e^{j2\pi l\cdot\frac{p}{T}}e^{-j2\pi\nu_{1}\left(\tau-\nu_{1}\right)}\text{TW}_{T}\left(\tau\right)\text{TW}_{T}^{*}\left(\tau-\tau_{1}\right)\text{d}\tau.\tag{49}$$
Based on (49), we notice that the Doppler orthogonality can be achieved by general periodic windows in time. However, the delay orthogonality depends on the shape of the adopted time domain window. More precisely, we consider delay and Doppler at integer times of the resolutions, i.e., τ1 = l1 T

˜
M and ν1 =
              k1
              ˜
             NT with − ˜
                         M ≤ l1 ≤ ˜
                                     M

and − ˜N ≤ k1 ≤ ˜N, which leads to the following theorem.

Theorem 4 (DD Orthogonality): Rectangular windows achieve the DD orthogonality, while general periodic

windows achieve the DD orthogonality approximately for sufficiently large ˜
                                                                         M and ˜N. Specifically, we have

$$A_{\Phi}\left(\tau_{1},\nu_{1}\right)=\tilde{M}\tilde{N}|{\rm FW}_{\rm F}\left(0\right)|^{2}|{\rm TW}_{\rm T}\left(0\right)|^{2}\delta\left[l_{1}\right]\delta\left[k_{1}\right],\tag{50}$$
for rectangular windows, and

$$A_{\Phi}\left(\tau_{1},\nu_{1}\right)\approx\tilde{M}\tilde{N}\frac{\left[\mathsf{PW}_{\mathrm{F}}\left(0\right)\right]^{2}}{T}\int_{0}^{T}\mathsf{TW}_{\mathrm{T}}\left(\tau\right)\mathsf{TW}_{\mathrm{T}}^{*}\left(\tau-\tau_{1}\right)\mathrm{d}\tau\delta\left[l_{1}\right]\delta\left[k_{1}\right],\tag{51}$$
for general periodic windows.

## Proof: The Proof Is Given In Appendix C. ■

Theorem 4 essentially states that truncating DD domain basis functions with general periodic windows will result in sufficient orthogonality in both delay and Doppler with respect to T
˜
M and
1
˜
NT , where the actual shape of the periodic windows do not matter very much as discussed in the previous subsection. Furthermore, using the methodology adopted in Appendix C, we can show that the ambiguity function also enjoys a semi-periodic response, T
�
, for any integer m and n, i.e., the ambiguity function shall have similar responses at (τ, ν) and
�
τ + nT, ν + m given a sufficient time duration and bandwidth of the truncated DD domain basis function6. This observation is in line with the quasi-periodicity of the Zak transform. In fact, this is commonly referred to as the delay and Doppler ambiguities in radar theory. However, when the underlying channel is underspread, i.e., the channel satisfies the crystallization condition, the delay spread and Doppler spread are no longer than T and
1
T as indicated by (12).

Such ambiguities do not affect the sensing or communication performance, because the orthogonality is roughly preserved. Furthermore, notice that RRC windows are approximately periodic within their supports for small rolloff factors. Therefore, the DD orthogonality can also be approximately achieved by RRC windows with a smaller roll-off factor. In fact, the above discussions align well with the response of the truncated DD domain basis function in the fundamental rectangle discussed in the previous subsection. Particularly, we may use either RRC windows or periodic windows interchangeably for achieving DD Nyquist signaling in practice. As a matter of fact, a DD
domain signaling of using both RRC window and rectangular window appears in [18], [20].

Remark 2: In fact, the localization in (34) and the orthogonality suggested by Theorem 4 are well-aligned with the intuitions of delay and Doppler by considering the time and frequency partition under critical sampling.

Intuitively, the delay and Doppler implies how significant the signal changes in frequency and in time. Clearly, for periodic signals in time and frequency, their Doppler and delay responses will be fully localized, as will their ambiguity functions. However, for periodic signals with truncation, their delay and Doppler responses will not be fully localized, because the signal periodicity is broken due to the truncation. Consequently, their Zak transforms will be sufficiently concentrated depending on the duration of the truncation window in time and frequency, following a "sinc-like" pattern. This is because the truncation in time and frequency can be viewed as the multiplication of time and frequency rectangular windows, and the "sinc-like" pattern appears naturally as the result of the Zak transform to a rectangular window.

We demonstrate the DD orthogonality using various time and frequency windows in Fig. 6(a) to Fig. 6(c), where we consider M = N = 32, and three different windows, namely the rectangular window (termed "Rect + Rect"), RRC windows with roll-off factor β = 0.3 (termed "RRC + RRC"), and Cosine window in time and RRC window in frequency (termed as "Cos + RRC"). We show the zero-Doppler cuts (ambiguity function with zero Doppler) and the zero-delay cuts (ambiguity function with zero delay) of the three cases in Fig. 6(a), and Fig. 6(b), where it is observed that all the three cases can achieve the sufficient delay orthogonality. Furthermore, we observe that both ("RRC + RRC") and ("Cos + RRC") cases have an almost zero response for normalized delay around − T
2
and T
2 . This is due to the quick decay of RRC pulses at the cost of the excess bandwidth. As a result, we can observe a "spike-like" ambiguity function, which may also be of interest for radar sensing. We also present the plot of ambiguity function for the ("RRC + RRC") case in Fig. 6(c), where we observe that the ambiguity function does have a response that is quasi-periodic along both delay and Doppler, while sufficiently localized within the fundamental rectangle.

## V. Practical Pulse Shaping For Delay-Doppler Communications

In this section, we will discuss the practical pulse shaping for general DD communications and we will also highlight the input-output relation for DD communications with practical pulse shapes.

Recall the TF-consistent filtering and windowing discussed in the previous section. We notice that in order to implement this, multiple time domain and frequency domain windows shall be used to truncate the DD domain basis function. Particularly, according to (10) and (39), the transmitted DD communication signal with roughly limited time and frequency resources can be written by

$$s_{\rm T}\left(t\right)=\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]\hat{\Phi}_{\rm T}^{T,\nu_{k}}\left(t\right)$$ $$=\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]\left\{\left[e^{j2\pi\nu_{k}\left(t-\tau_{l}\right)}\Phi_{\rm T}^{T,\nu_{k}}\left(t-\tau_{l}\right)\right]*\left[{\sf FW}_{\rm T}\left(t\right)e^{j2\pi\nu_{k}t}\right]\right\}{\sf WT}_{\rm T}\left(t-\tau_{l}\right)$$ $$=\forall T\,\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]e^{j2\pi\nu_{k}\left(t-\tau_{l}\right)}\sum_{n=-\infty}^{\infty}{\sf PW}_{\rm T}\left(t-\tau_{l}-nT\right){\sf TW}_{\rm T}\left(t-\tau_{l}\right),\tag{52}$$
where we assume that both FWT (t) and TWT (t) have unit power. According to (52), it is possible to design the DD pulse shaping using a filter bank structure, which includes MN filters that are shifted in time and frequency with respect to the delay and Doppler offsets associated to xDD [l, k]. Such an implementation is straightforward but may not be practical due to the high hardware complexity required for realizing the filter bank. Therefore, we are motivated to consider a simplified and more practical implementation by applying a *sufficiently narrow* time domain pulse FWT (t). In this case, (52) can be shown to converge to

$$s_{\rm T}\left(t\right)\simeq\sqrt{T}\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]\sum_{n=-\infty}^{\infty}e^{j2\pi m\tau_{l}T}{\sf F}{\sf W}_{\rm T}\left(t-\tau_{l}-nT\right){\sf T}{\sf W}_{\rm T}\left(t\right).\tag{53}$$

The convergence of (53) holds for practical signals, such as RBC signals, when $M$ is large, which can be explained
NT into (53),

by the TF separability property discussed previously. Furthermore, by substituting τl =
                                                                                        l
                                                                                        M T and νk =
                                                                                                        k

we obtain

$$s_{\rm T}\left(t\right)\simeq\!\!\!\vee\!\!T\,\sum_{l=0}^{M-1}\,\sum_{n=-\infty}^{\infty}\,\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]e^{j2\pi n\frac{\star}{M}}{\sf FWT}\left(t-\frac{l}{M}T-nT\right){\sf TWT}\left(t\right)\tag{54}$$ $$=\!\!\!\vee\!\!NT\,\sum_{l=0}^{M-1}\,\sum_{n=-\infty}^{\infty}\,\tilde{x}_{\rm T}\left[l+nM\right]{\sf FWT}\left(t-\frac{l}{M}T-nT\right){\sf TWT}\left(t\right),$$
where

$$\tilde{x}_{\rm T}\left[l+nM\right]\stackrel{{\Delta}}{{=}}\frac{1}{\sqrt{N}}\,\sum_{k=0}^{N-1}x_{\rm DD}\left[l,k\right]e^{j2\pi n\frac{k}{N}},\tag{55}$$
NT is a normalization factor that

is the _inverse discrete Zak transform_ (IDZT) [35] of $\mathbf{X}_{\rm DD}$, and the constant $\sqrt{\cdot}$
roughly agrees with time duration of sT (t) in order to maintain the average symbol energy. Notice that (54) involves an infinite summation of with respect to n. Let us define xT
∆= [˜xT [0] , ˜xT [1] , ..., ˜xT [MN − 1]]T as a length-MN
vector, and we shall highlight that ˜xT is a periodically extended version of xT. Furthermore, notice that TWT (t)
has a time duration roughly NT . Therefore, it is natural to approximate ˜xT by xT in practice. In fact, such an approximation is commonly adopted in the OTFS literature, where xT is often time domain symbol vector for OTFS
transmission. As suggested by (54), we can achieve DD pulse shaping by filtering xT in a way similar to that of the single-carrier transmission. However, this must be done with care because the underlying wireless channel may introduce additional delay and Doppler shifts. Therefore, as a common method, we propose to append a sufficiently long cyclic prefix (CP) at the beginning of the frame. Note that the insertion of CP effectively transforms the linear convolution of the time domain channel to the circular convolution. As a result, the received signal can be viewed as a periodized version of the xT shifted by channel delay and Doppler, whose DZT aligns with XDD [29]. In fact, this CP structure is commonly referred to as the "reduced-CP" structure in the OTFS literature [19].

Given the discussions above, we shall consider the DD Nyquist pulse shaping structure as shown in Fig. 7.

In Fig. 7, the DD domain symbol matrix XDD is first passed to the IDZT module, yielding xT of length-MN.

After appending a CP with duration longer than the maximum path delay, the resultant vector is then convoluted with FWT (t) and followed by windowing based on TWT (t), obtaining the time domain transmitted signal sT (t).

Particularly, we require the adopted time domain window is long enough to cover the CP part as well, as shown in Fig. 87. In the figure, we adopt a time domain window with excessive duration for transmission, where we demonstrate the interaction between time and frequency domain windows. We use dashed and solid curves to mark the CP part and the information part of the signal and LCP here denotes the CP length.

At the receiver side, the time domain received signal rT (t) is first windowed by TW∗
T (t) and then filtered by FW∗
T (t), where the connection between sT (t) and rT (t) is given by (14). After removing the CP, the resultant where (τ, ν) is a pair of arbitrary delay and Doppler shifts that satisfies the *underspread* channel condition, i.e.,
τ ∈ [0, T), and ν ∈
�
0, 1
T
�
. Furthermore, let L be the maximum length of intersymbol interference (ISI), i.e.,

$\frac{1}{T}$) and $|k^{\prime}-k|>L$. Thus, we obtain 

g(τ,ν)
 k,k′ ≈ 0 for any τ ∈ [0, T) , ν ∈
                             �
                              0, 1

$${\bf y_{T}}=\sum_{p=1}^{P}{\bf H}_{\rm T}^{(p)}{\bf x_{T}}+{\bf n_{T}},\tag{59}$$
where H(p)
T
is the effective time domain channel matrix of size MN × MN for the p-th resolvable path, given by



$$\begin{array}{ccccccccccccc}g_{0,L}^{(r_{p},\nu_{p})}&\ldots&g_{L,0}^{(r_{p},\nu_{p})}&0&\cdots&0&g_{-L,0}^{(r_{p},\nu_{p})}&\ldots&g_{-L,0}^{(r_{p},\nu_{p})}\\ \vdots&\ddots&\ddots&\ddots&\ddots&\ddots&\vdots\\ g_{0,L}^{(r_{p},\nu_{p})}&\ldots&\ldots&g_{L,0}^{(r_{p},\nu_{p})}&\ldots&0&g_{-L,L-1}^{(r_{p},\nu_{p})}\\ \mathbf{H}_{\mathrm{T}}^{(p)}=h_{p}&0&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&&\ddots&\ddots&\ddots&\ddots&\ddots&\vdots\\ &&\ddots&\ddots&\ddots&\ddots&\ddots&\ddots&\ddots\\ 0&\ldots&0&g_{N,-L-1,MN-1}^{(r_{p},\nu_{p})}&\ldots&\ldots&g_{MN-1,MN-1}^{(r_{p},\nu_{p})}\\ \end{array}\tag{60}$$


We observe that H(p)
T
has a banded structure with small portion of non-zero elements placed on the top-right corner due to the appended CP. Based on (60), the effective time domain channel matrix that considers the effect of P
using matrix forms [36]. We can then derive the DD domain input-output relation, such as

paths can be written as HT
                            ∆= �P
                                 p=1 H(p)
                                       T . Furthermore, notice that the both IDZT and DZT can be described

$${\bf y_{DD}=H_{DD}x_{DD}+n_{DD}},\tag{61}$$
DD domain AWGN vector with the variance of the AWGN samples being N0.

where HDD
          ∆= (FN ⊗ IM) HT
                          �
                           FH
                             N ⊗ IM
                                   �
                                     is the effective DD domain channel matrix and nDD is the effective

## B. Asymptotical Dd Domain Input-Output Relation

In this subsection, we study the simplification of the input-output relation discussed in the previous subsection, by focusing on sufficiently large M and N. In such a case, the convergence of time domain pulse shaping in (53)
holds generally. Furthermore, following the same reasoning of the transmitter part, we have

$$y_{\rm DD}\left[l,k\right]\simeq\int_{-\infty}^{\infty}r_{\rm T}\left(t\right)\left[\hat{\Phi}_{\rm T}^{\tau_{l},\nu_{k}}\left(t\right)\right]^{*}{\rm d}t=\int_{0}^{T}\int_{0}^{\frac{1}{T}}r_{\rm DD}\left(\tau,\nu\right)\left[\hat{\Phi}_{\rm DD}^{\tau_{l},\nu_{k}}\left(\tau,\nu\right)\right]^{*}{\rm d}\tau{\rm d}\nu.\tag{62}$$
Notice that

$$r_{\text{DD}}\left(\tau,\nu\right)\simeq\sum_{p=1}^{P}h_{p}s_{\text{DD}}\left(\tau-\tau_{p},\nu-\nu_{p}\right)e^{j2\pi\tilde{\nu}_{p}\left(\tau-\tilde{\nu}_{p}\right)}+n_{\text{DD}}\left(\tau,\nu\right)\tag{63}$$ $$=\sum_{p=1}^{P}h_{p}\sum_{l=0}^{M-1}\sum_{k=0}^{N-1}x_{\text{DD}}\left[l,k\right]e^{j2\pi\tilde{\nu}_{p}\left(\tau-\tilde{\nu}_{p}\right)}\tilde{\Phi}_{\text{DD}}^{\tau,\nu_{p}}\left(\tau-\tilde{\tau}_{p},\nu-\tilde{\nu}_{p}\right)+n_{\text{DD}}\left(\tau,\nu\right),\tag{64}$$
where (63) is derived by substituting (11) into (13). Then, (62) can be further simplified by

$$y_{\rm DD}\left[l,k\right]=\sum_{p=1}^{P}\hbar_{p}\sum_{l^{\prime}=0}^{M-1}\sum_{k^{\prime}=0}^{N-1}x_{\rm DD}\left[l^{\prime},k^{\prime}\right]\int_{0}^{T}\int_{0}^{\frac{1}{2}}e^{j2\pi\hat{p}_{p}(\tau-\hat{p}_{p})}\hat{\Phi}_{\rm DD}^{\tau_{p}\tau_{p^{\prime}}}\left(\tau-\hat{p}_{p},\nu-\hat{\nu}_{p}\right)\left[\hat{\Phi}_{\rm DD}^{\tau_{\rm DD}\tau_{p}}\left(\tau,\nu\right)\right]^{*}{\rm d}\nu{\rm d}\tau.\tag{65}$$

To further characterize (65), let us consider the following corollary.

Corollary 2 (Symbol-wise DD Domain Input-Output Relation): Let ˜Φτl,νk
                                                               DD (τ, ν) and ˜Φτl′,νk′
                                                                              DD
                                                                                    (τ, ν) be the DD

domain basis functions associated to the xDD [l, k] and xDD [l′, k′], respectively. Furthermore, considering an

arbitrary pair of delay and Doppler shifts $(\tilde{r},\tilde{\nu})$, we have

$$\begin{split}&\int_{0}^{T}\int_{0}^{+}e^{j2\pi\tilde{\nu}(\tau-\tilde{r})}\hat{\Phi}_{\text{DD}}^{\text{v,v,v}}\left(\tau-\tilde{r},\nu-\tilde{\nu}\right)\left[\hat{\Phi}_{\text{DD}}^{\text{v,v,v}}\left(\tau,\nu\right)\right]^{*}\text{d}\text{d}\tau\\ &=e^{j2\pi\tilde{\nu}(\tau_{l}-\tilde{r})}e^{j2\pi\tilde{\nu}_{\text{v}}\left(\tau_{l}-\tilde{r}-\tilde{r}\nu_{l}\right)}A_{\tilde{\Phi}}\left(\tau_{l}-\tilde{r}-\gamma_{l},\nu_{k}-\tilde{\nu}-\nu_{k}\right).\end{split}\tag{66}$$
Proof: The proof is given in Appendix D.

■
By substituting (66) into (65), we arrive the symbol-wise DD domain input-output relation with large M and N
by

$$y_{\rm DD}\left[l,k\right]=\sum_{p=1}^{P}h_{p}\sum_{\ell^{\prime}=0}^{M-1}\sum_{b^{\prime}=0}^{N-1}e^{j2\pi\hat{\nu}_{p}(\tau_{b}-\hat{\nu}_{b})}e^{j2\pi\nu_{b^{\prime}}(\tau_{b}-\hat{\nu}_{b}-\nu_{b^{\prime}})}x_{\rm DD}\left[l^{\prime},k^{\prime}\right]A_{\hat{\bf k}}\left(\tau_{l}-\hat{\tau}_{p}-\tau_{\ell^{\prime}},\nu_{b}-\hat{\nu}_{p}-\nu_{b^{\prime}}\right).\tag{67}$$

Notice that (67) holds for general pulses/windows without any constraint on the DD orthogonality, where the umbil
guity function can be calculated based on (47). To shed the light on practical implementation, we now demonstrate the DD domain input-output relation using special pulses/windows under two specific channel conditions.

Example 1 (*Rectangular Windows*): In the case where both power normalized FWF (f) and TWT (t) are rectangular windows with bandwidth M
T and time duration NT , i.e., FWF (f) =
1
√
T
�
T /M only for f ∈
�
0, M
and TWT (t) =
1
√
NT only for t ∈ [0, NT]. According to (75) in Appendix C, (67) can be further derived by8

$$y_{\text{DD}}\left[l,k\right]=\frac{1}{MN}\sum_{p=1}^{p}h_{p}\sum_{r=0}^{M-1}\sum_{\ell=0}^{N-1}e^{2\pi\hat{\sigma}_{p}\left(\frac{\mathbf{\hat{\sigma}}_{p}}{T}-\hat{r}_{r}\right)}e^{2\pi\mathbf{\hat{\sigma}}_{p}\left(\frac{\mathbf{\hat{\sigma}}_{p}}{T}-\hat{r}_{r}\right)}x_{\text{DD}}\left[l^{\prime},k^{\prime}\right]$$ $$\sum_{n=0}^{N-1}e^{-j2\pi n\left(\frac{\mathbf{\hat{\sigma}}_{p}}{T}-\hat{\sigma}_{p}\right)T}\sum_{m=0}^{M-1}e^{j2\pi m\left(\frac{\mathbf{\hat{\sigma}}_{p}}{T}-\hat{r}_{r}\right)}\sum_{m^{\prime}=0}^{M-1}e^{j2\pi\left(\frac{\mathbf{\hat{\sigma}}_{p}}{T}-\hat{\sigma}_{p}\right)T}\text{sinc}\left(\frac{m-m^{\prime}}{T}-\left(\frac{k-k^{\prime}}{NT}-\hat{\sigma}_{p}\right)\right)\tag{68}$$
Example 2 (*Rectangular Windows with integer delay and Doppler*): In the case of integer delay and Doppler, i.e.,

˜τp =
    ˜lp
    M T, ˜νp =
              ˜kp
             NT , where 0 ≤ ˜lp ≤ M − 1 and 0 ≤ ˜kp ≤ N − 1 are integers for any 1 ≤ p ≤ P, known as the

delay and Doppler indices, (68) further reduces to

$$y_{\rm DD}\left[l,k\right]=\sum_{p=1}^{P}h_{p}\sum_{l^{\prime}=0}^{M-1}\sum_{k^{\prime}=0}^{N-1}e^{j2\pi\frac{k}{MN}\left(1-\tilde{l}_{p}\right)}e^{j2\pi\frac{k^{\prime}}{MN}\left(l-l^{\prime}-\tilde{l}_{p}\right)}x_{\rm DD}\left[l^{\prime},k^{\prime}\right]$$ $$\sum_{m=-\infty}^{\infty}\delta\left[k-k^{\prime}-\tilde{k}_{p}+mN\right]\sum_{n=-\infty}^{\infty}\delta\left[l-l^{\prime}-\tilde{l}_{p}+nM\right]$$ $$=\sum_{p=1}^{P}h_{p}e^{j2\pi\frac{k_{\rm DD}}{MN}\left(l-l_{p}\right)}\alpha_{l,l_{p},k,\tilde{l}_{p}}x_{\rm DD}\left[\left[l-l_{p}\right]_{M},\left[k-k_{p}\right]_{N}\right],\tag{69}$$
where

$$\alpha_{l,\,l_{p},\,\lambda,\,l_{p}}=\left\{\begin{array}{ll}1,&l-l_{p}\geq0\\ e^{-j2\pi\frac{l-l_{p}}{2}},&l-l_{p}<0\end{array}\right.\tag{70}$$

is a phase offset due to the DD domain quasi-periodicity [13]. In fact, the above input-output relation aligns with 
the matrix form provided in [19], [37] using rectangular pulses in the TF domain.

Remark 3: We have shown above the input-output relation using rectangular windows, where we observe a consistent input-output relation with the two-stage OTFS implementation under integer delay and Doppler when M
and N are sufficiently large. This is not unexpected, because OFDM signaling with rectangular windows can be implemented in the time domain via *sinc interpolation*. This scheme is commonly known as the discrete multi-tone
(DMT) transmission [38].

## Vi. Numerical Results

In this section, we present the numerical results on the proposed DD communications in terms of BER and pragmatic capacity. Without loss of generality, we consider M = 16 and N = 16, unless specified otherwise and the transmitted symbols are obtained from an energy-normalized QPSK constellation. Furthermore, we assume that the underspread wireless channel has P = 4 independent resolvable paths, where the delay indices and Doppler indices can have fractional values and are uniformly taking values from [0, lmax] and [−kmax/2, kmax/2], respectively, with lmax = 5 and kmax = 3. We will compare the pulse shaping using rectangular windows and RRC windows with roll-off factors β = 0.3 in the frequency domain and β = 0.1 in the time domain.

We present the BER performance of the proposed transmission in comparison with OFDM under the same channel condition in Fig. 9(a) and Fig. 9(b), where the OFDM is implemented using the DMT structure with sinc pulses (rectangular windows). To attain a good error performance, we adopt the cross domain iterative detection proposed in [36] for both DD communications and OFDM, which is shown to provide a near-optimal performance for OTFS.

We notice from Fig. 9(a) and Fig. 9(b) that the DD communications with both rectangular and RRC windows can obtain roughly the same error performance under both fractional and integer delay and Doppler case, especially in the high SNR regime. This is because the cross domain iterative detection can achieve the near-optimal performance that is dominated by the channel fading rather than the exact delay and Doppler response. Furthermore, we highlight that the application of time domain RRC windows may result in slight reduction in the effective symbol energy of few transmitted symbols due to the roll-off part as indicated by Fig. 8. However, this power loss is almost has no influence on the error performance when we choose a relatively small roll-off factor for the time domain RRC
window, e.g., β = 0.1. On the other hand, OFDM in both two cases fails to provide good BER results. Particularly, we notice that the BER curves of OFDM have a less steep slope compared to those of DD communications, which indicates that it cannot fully exploit the full channel diversity. However, we highlight that the above results are obtained from uncoded systems. A more detailed analysis between coded OTFS and OFDM appears in [11].

The pragmatic capacity performance of the considered schemes under the fractional DD case are presented in Fig. 9(c). The pragmatic capacity is characterized by the "single-letter" mutual information incorporating the effects of modulation, channel, demodulation, and equalization, which can be computed numerically by using Monte Carlo simulations. More details of pragmatic capacity can be found in [27], [28]. From the figure, we observe that the pragmatic capacities of DD communications using both rectangular and RRC windows achieve roughly the same performance, despite the fact that using rectangular window can achieve a slight rate improvement in the low-to-mid SNR regime. This observation align well with our BER curves in Fig. 9(a).

We finally examine the PSDs of the transmitted signals in Fig. 9(d), which are obtained by taking the squared values of the Fourier transform of (54). Specifically, we present the PSD corresponding to the rectangular window, and RRC windows with roll-off factors with β = 0.1 and β = 0.3, and we consider M = 16 and N = 8
here. It is not surprising to see that the PSD of transmitted signals using RRC window will exhibit a much lower OOB emission compared to the case of using rectangular windows. Particularly, we observe that the lower OOB emission comes at a price of the excess bandwidth determined by the roll-off factor, and a larger roll-off factor is beneficial for obtaining a lower OOB emission. This observation verifies the practical advantage of the proposed DD communications.

## Vii. Conclusion

In this paper, we discussed the practical implementation of DD communications based on insights from the Zak transform. We firstly presented our basis function construction and then highlighted its features in different domains.

We then presented the practical realization of the constructed basis functions based on TF-consistent windowing and filtering, and derived their ambiguity functions, where we verified the sufficient DD orthogonality can be achieved by truncated periodic signals. Finally, we derived the end-to-end system model for the proposed scheme under various shaping pulses and our conclusions were verified by our numerical results.

By substituting (31) into (24), we have

$$e^{j2\pi\nu_{1}(\tau-\tau_{1})}A_{\Phi}\left(\tau_{1}-\tau_{2},\nu_{1}-\nu_{2}\right)$$ $$=\int_{0}^{T}\int_{0}^{\phi}e^{j2\pi\nu_{2}(\tau-\tau_{2})}\phi_{00}^{\text{DD}}\left(\tau-\nu_{1},\nu-\nu_{2}\right)e^{-j2\pi\nu_{1}(\tau-\tau_{1})}\Big{(}\phi_{00}^{\text{DD}}\left(\tau-\tau_{1},\nu-\nu_{1}\right)\Big{)}^{*}\text{d}\nu\text{d}\tau$$ $$=\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{j2\pi\nu_{1}(\tau-\tau_{1})}e^{-j2\pi\nu_{1}(\tau-\tau_{1})}\varphi\left(\tau-\tau_{2}-nT,\nu-\nu_{2}-\frac{m}{T}\right)\varphi^{*}\left(\tau-\tau_{1},\nu-\nu_{1}\right)e^{-j2\pi m(\nu-\nu_{2})T}\text{d}\nu\text{d}\tau,\tag{71}$$
where (71) is derived by interchanging the variables and replacing the summation by extending the integral range.

Furthermore, by substituting ϕ (τ, ν) = δ (τ) δ (ν) into (71), we obtain

$$e^{j2\pi\nu_{2}\left(\tau_{1}-\tau_{2}\right)}A_{\Phi}\left(\tau_{1}-\tau_{2},\nu_{1}-\nu_{2}\right)=e^{j2\pi\nu_{2}\left(\tau_{1}-\tau_{2}\right)}\sum_{n=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}\delta\left(\tau_{1}-\tau_{2}-nT\right)\delta\left(\nu_{1}-\nu_{2}-\frac{m}{T}\right).\tag{72}$$

Finally, by deleting the phase term on both sides of (72), (34) can be derived.

## Appendix B Proof Of Theorem 3

Define an intermediate function Φ′
                                 T (t)
                                      ∆= Φ0,0
                                           T (t)∗FWT (t) =
                                                             � ∞
                                                               −∞ FWT (τ)Φ0,0
                                                                             T (t − τ) dτ. Then, the ambiguity

function of Φ′
             T (t) can be calculated by

−∞ −∞ FWT (τ1)Φ0,0 T (t − τ1) dτ1 AΦ′ T (τ, ν) = � ∞ � ∞ � ∞ −∞ FW∗ T (τ2) � Φ0,0 T (t − τ2 − τ) �∗ dτ2e−j2πν(t−τ)dt −∞ −∞ FWT (τ1)FW∗ T (τ2) e−j2πντ2AΦ (τ2 − τ1 + τ, ν) dτ1dτ2 = � ∞ � ∞ = T � ∞ n=−∞ � m=−∞ δ � ν − m ∞ � −∞ FWT (τ1)FW∗ T (τ1 + nT − τ) dτ1e−j2πν(τ1+nT −τ) ∞ � = T n=−∞ AFW (τ − nT, ν) m=−∞ δ � ν − m � . (73) ∞ � ∞ �

## References

[1] S. Li, W. Yuan, Z. Wei, J. Yuan, B. Bai, and G. Caire, "On the pulse shaping for delay-Doppler communications," in IEEE Globe Commun.
Conf., 2023, pp. 1–6.
[2] R. Hadani, S. Rakib, M. Tsatsanis, A. Monk, A. J. Goldsmith, A. F. Molisch, and R. Calderbank, "Orthogonal time frequency space
modulation," in *Proc. 2017 IEEE Wireless Commun. Net. Conf.*, Mar. 2017, pp. 1–6.
[3] Z. Wei, W. Yuan, S. Li, J. Yuan, G. Bharatula, R. Hadani, and L. Hanzo, "Orthogonal time-frequency space modulation: A promising
next-generation waveform," *IEEE Wireless Commun.*, vol. 28, no. 4, pp. 136–144, Aug. 2021.
[4] F. Hlawatsch and G. Matz, *Wireless Communications over Rapidly Time-Varying Channels*.
Academic Press, 2011.
[5] W. Yuan, S. Li, Z. Wei, Y. Cui, J. Jiang, H. Zhang, and P. Fan, "New delay Doppler communication paradigm in 6G era: A survey of
orthogonal time frequency space (OTFS)," *China Commun.*, vol. 20, no. 6, pp. 1–25, Jun. 2023.
[6] Z. Wei, S. Li, W. Yuan, R. Schober, and G. Caire, "Orthogonal time frequency space modulation-Part I: Fundamentals and challenges
ahead," *IEEE Commun. Lett.*, vol. 27, no. 1, pp. 4–8, Jan. 2023.
[7] S. Li, W. Yuan, Z. Wei, R. Schober, and G. Caire, "Orthogonal time frequency space modulation-Part II: Transceiver designs," IEEE
Commun. Lett., vol. 27, no. 1, pp. 9–13, Jan. 2023.
[8] W. Yuan, Z. Wei, S. Li, R. Schober, and G. Caire, "Orthogonal time frequency space modulation-Part III: ISAC and potential applications,"
IEEE Commun. Lett., vol. 27, no. 1, pp. 14–18, Jan. 2023.
[9] P. Raviteja, K. T. Phan, and Y. Hong, "Embedded pilot-aided channel estimation for OTFS in delay-Doppler channels," IEEE Trans. Veh.
Technol., vol. 68, no. 5, pp. 4906–4917, May 2019.
[10] P. Raviteja, Y. Hong, E. Viterbo, and E. Biglieri, "Effective diversity of OTFS modulation," *IEEE Wireless Commun. Lett.*, vol. 9, no. 2,
pp. 249–253, Feb. 2020.
[11] S. Li, J. Yuan, Z. Wei, B. Bai, and D. W. K. Ng, "Performance analysis of coded OTFS systems over high-mobility channels," IEEE
Trans. Wireless Commun., vol. 20, no. 9, pp. 6033–6048, Sep. 2021.
[12] M. Liu, S. Li, Z. Wei, and B. Bai, "Near optimal hybrid digital-analog beamforming for point-to-point MIMO-OTFS transmissions," in
IEEE Wireless Commun.Netw. Conf. Workshop, 2023, pp. 1–6.
[13] S. Li, J. Yuan, P. Fitzpatrick, T. Sakurai, and G. Caire, "Delay-Doppler domain Tomlinson-Harashima precoding for OTFS-based downlink
MU-MIMO transmissions: Linear complexity implementation and scaling law analysis," *IEEE Trans. Commun.*, vol. 71, no. 4, pp. 2153–
2169, Apr. 2023.
[14] S. K. Dehkordi, L. Gaudio, M. Kobayashi, G. Caire, and G. Colavolpe, "Beam-space MIMO radar for joint communication and sensing
with OTFS modulation," *IEEE Trans. Wireless Commun.*, vol. 22, no. 10, pp. 6737–6749, Oct. 2023.
[15] S. Li, W. Yuan, C. Liu, Z. Wei, J. Yuan, B. Bai, and D. W. K. Ng, "A novel ISAC transmission framework based on spatially-spread
orthogonal time frequency space modulation," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1854–1872, Jun. 2022.
[16] P. Raviteja, K. T. Phan, Y. Hong, and E. Viterbo, "Interference cancellation and iterative detection for orthogonal time frequency space
modulation," *IEEE Trans. Wireless Commun.*, vol. 17, no. 10, pp. 6501–6515, Oct. 2018.
[17] A. RezazadehReyhani, A. Farhang, M. Ji, R. R. Chen, and B. Farhang-Boroujeny, "Analysis of discrete-time MIMO OFDM-Based
orthogonal time frequency space modulation," in *Proc. 2018 IEEE Int. Conf. Commun.*, May 2018, pp. 1–6.
[18] H. Lin and J. Yuan, "Orthogonal delay-Doppler division multiplexing modulation," *IEEE Trans. Wireless Commun.*, vol. 21, no. 12, pp.
11 024–11 037, Dec. 2022.
[19] P. Raviteja, Y. Hong, E. Viterbo, and E. Biglieri, "Practical pulse-shaping waveforms for reduced-cyclic-prefix OTFS," IEEE Trans. Veh.
Technol., vol. 68, no. 1, pp. 957–961, Jan. 2019.
[20] H. Lin and J. Yuan, "On delay-Doppler plane orthogonal pulse," in *IEEE Global Comm. Conf.*, Dec. 2022, pp. 5589–5594.
[21] M. Bayat and A. Farhang, "A unified framework for pulse-shaping on delay-Doppler plane," *arXiv preprint arXiv:2311.12543*, 2023.
[22] A. J. Janssen, "The Zak transform: A signal transform for sampled time-continuous signals." *Philips J. Res.*, vol. 43, no. 1, pp. 23–69,
1988.
[23] F. Lampel, A. Avarado, and F. M. Willems, "On OTFS using the discrete Zak transform," in IEEE Int. Conf. Commun. Workshops (ICC
Workshops), 2022, pp. 729–734.
[24] S. K. Mohammed, "Derivation of OTFS modulation from first principles," *IEEE Trans. Veh. Technol.*, vol. 70, no. 8, pp. 7619–7636, Aug.
2021.
[25] S. K. Mohammed, R. Hadani, A. Chockalingam, and R. Calderbank, "OTFS–a mathematical foundation for communication and radar
sensing in the delay-Doppler domain," *IEEE BITS Inf. Theory Mag.*, vol. 2, no. 2, pp. 36–55, Nov. 2022.
[26] ——, "OTFS–predictability in the delay-Doppler domain and its value to communication and radar sensing," arXiv preprint
arXiv:2302.08705, 2023.
[27] L. Gaudio, G. Colavolpe, and G. Caire, "OTFS vs. OFDM in the presence of sparsity: A fair comparison," *IEEE Trans. Wireless Commun.*,
vol. 21, no. 6, pp. 4410–4423, Dec. 2022.
[28] A. Kavcic, X. Ma, and M. Mitzenmacher, "Binary intersymbol interference channels: Gallager codes, density evolution, and code
performance bounds," *IEEE Trans. Inf. Theory*, vol. 49, no. 7, pp. 1636–1652, Jun. 2003.
[29] H. B¨olcskei, *Gabor Expansion and Frame Theory*.
Vienna Univ. of Technol., 1994.
[30] A. Teuner and B. Hosticka, "Adaptive Gabor transformation for image processing," *IEEE Trans. Image Process.*, vol. 2, no. 1, pp. 112–117,
Jan. 1993.
[31] D. Dunn and W. Higgins, "Optimal Gabor filters for texture segmentation," *IEEE Trans. Image Process.*, vol. 4, no. 7, pp. 947–964, Jul.
1995.
[32] K. Gr¨ochenig, *Foundations of time-frequency analysis*.
Springer Science & Business Media, 2013.
[33] P. Jung and G. Wunder, "The WSSUS pulse design problem in multicarrier transmission," *IEEE Trans. Commun.*, vol. 55, no. 10, pp.
1918–1928, Oct. 2007.
[34] S. Mallat, A Wavelet Tour of Signal Processing (2. ed.).
Elsevier, 1999.
[35] H. B¨olcskei and F. Hlawatsch, "Discrete Zak transforms, polyphase transforms, and applications," *IEEE Trans. signal process.*, vol. 45,
no. 4, pp. 851–866, Apr. 1997.
[36] S. Li, W. Yuan, Z. Wei, and J. Yuan, "Cross domain iterative detection for orthogonal time frequency space modulation," IEEE Trans.
Wireless Commun., vol. 21, no. 4, pp. 2227–2242, Apr. 2022.
[37] Y. Hong, T. Thaj, and E. Viterbo, *Delay Doppler Communications: Principles and Applications*.
Elsevier, 2022.
[38] A. Sahin, I. Guvenc, and H. Arslan, "A survey on multicarrier communications: Prototype filters, lattice structures, and implementation
aspects," *IEEE Commun. Surv. Tutor.*, vol. 16, no. 3, pp. 1312–1338, Dec. 2014.