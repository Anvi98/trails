# Information Rates Of Successive Interference Cancellation For Optical Fiber

Alex J¨ager and Gerhard Kramer, Fellow, IEEE

  Abstract—Successive interference cancellation (SIC) is used
to approach the achievable information rates (AIRs) of joint
detection and decoding for long-haul optical fiber links. The
AIRs of memoryless ring constellations are compared to those of
circularly symmetric complex Gaussian modulation for surrogate
channel models with correlated phase noise. Simulations are
performed for 1000 km of standard single-mode fiber with ideal
Raman amplification. In this setup, 32 rings and 16 SIC-
stages with Gaussian message-passing receivers achieve the AIR
peaks of previous work. The computational complexity scales in
proportion to the number of SIC-stages, where one stage has the
complexity of separate detection and decoding.

  Index Terms—Belief propagation, nonlinearity mitigation, op-
tical fiber communication, phase noise, successive interference
cancellation.

## I. Introduction

  Estimating the capacity of optical fiber is difficult be-
cause of the interactions of frequency-dependent attenuation,
dispersion, and Kerr non-linearity [1]. A standard approach
computes achievable information rates (AIRs) by simulating
transmission and having the receiver process its signal via
surrogate, or mismatched, models. The closer the surrogate
model is to the actual model, as measured by an informational
divergence, the higher the computed AIR. One, therefore, often
has a trade-off between AIR and computational complexity.
  For example, two useful surrogate models are a memoryless
additive white Gaussian noise (AWGN) channel whose covari-
ance and pseudo-covariance may depend on the channel input
amplitude [1, Sec. X.C] and an AWGN channel with correlated
phase noise with large memory [2], [3], [4]; see also [5],
[6], [7], [8]. A memoryless model suggests practical receiver
algorithms with a posteriori probability (APP) processing. The
models with memory improve the AIR, but it is less clear how
to build practical receivers. In particular, the receivers in [6],
[7], [9], [8], [10] use particle filters to compute joint detection
and decoding (JDD) rates, but it is not obvious how to convert
such structures into practical systems.
  Two classic methods to approach JDD performance combine
separate detection and decoding (SDD) with either turbo
processing or successive interference cancellation (SIC). The
former approach was applied to Wiener phase noise channels
[11], [12], [13] and fiber-optic systems [14], [15]. This method
has the disadvantage of requiring receiver iterations and a

dedicated code design to maximize the rates. We instead use
the SIC structure outlined in [1, Sec. XII] for which off-the-
shelf codes and classic multi-level coded modulation approach
capacity; see also [16], [17], [18] and recently [19], [20].
  This paper is organized as follows. Sec. II introduces nota-
tion, the channel model, and the correlated phase and additive
noise (CPAN) surrogate model of [9]. Sec. III and Sec. IV
propose SIC receivers for circularly symmetric complex Gaus-
sian (CSCG) modulation and ring constellations, respectively.
The receivers use belief propagation and approximate message
passing. For a sufficient number of SIC-stages, the receiver
achieves, and even surpasses, the AIR for JDD predicted in
[9]. Sec. V concludes the paper and suggests future work on
implementations.

## Ii. Preliminaries A. Notation

Random variables are written in uppercase, such as X, and their realizations in lowercase, such as x. Random vectors are written with bold letters, such as X, and their realizations as x. We write a(x) ∝ b(x) if there exists a constant c for which a(x) = c b(x). A Gaussian X with mean µ and variance σ2
has probability density function (pdf)

2 (x − µ)2 σ2 2πσ2 exp � −1 � . (1) N � x; µ, σ2� = 1 √
Similarly, a complex Gaussian X with mean µ, variance σ2 =
E
�
|X − µ|2�
and pseudo-variance p2 = E
�
(X − µ)2�
has pdf

NC � x; µ, σ2, p2� = 1 π � σ2 � σ2 � σ2 − |p|4 exp −1 � �� �−1 � (x − µ) (x − µ)∗ 2[(x − µ)∗, (x − µ)] � σ2 p2 � p2�∗ σ2
(2)
where ∗ denotes complex conjugation. A CSCG has p2 = 0
and therefore the pdf

σ2 � . (3) πσ2 exp � −|x − µ|2 NC � x; µ, σ2� = 1
The function

$$m\left(x\right)=\left(x+\pi\mod2\pi\right)-\pi\tag{4}$$
maps x to the interval [−π, π).

## B. System Model

  We use a standard model [1] for optical networks with
reconfigurable optical add-drop multiplexers (ROADMs). Mul-
tiple wavelength-division multiplexing (WDM) channels co-
propagate over a fiber span, and each receiver can access
only its channel of interest (COI). Co-propagating channels
disturb each other due to nonlinearities, such as cross-phase
modulation (XPM) and four-wave mixing (FWM), and the
worst-case scenario has different co-propagating signals over
the entire length of the transmission link. The continuous-time
baseband signal for n symbols and 2b interfering channels is

x(0, t) =

$$\sum_{i=1}^{n}x_{i}g(t-iT)+\sum_{\begin{subarray}{c}k=-b\\ k\neq0\end{subarray}}^{b}\sum_{i=1}^{n}b_{i}^{(k)}g(t-iT)\mathrm{e}^{\mathrm{i}\omega_{k}t}\tag{5}$$
where the xi and b(k)
i are realizations of mutually independent random variables with a common alphabet X and variance
σ2
x. All channels use root-raised cosine (RRC) pulse-shaping filters g(·) and symbol rate 1/T . We assume ∥g∥2/T = 1, so the per-channel average transmit power is Ptx = σ2
x. The central frequency of the k-th channel is ωk/2π where ω0 = 0.

Signal propagation over an optical fiber using ideal distributed Raman amplification (IDRA) is described by the nonlinear Schr¨odinger equation (NLSE) [9]

$$\frac{\partial x(z,t)}{\partial z}=-\mathrm{j}\frac{\beta_{2}}{2}\frac{\partial^{2}x(z,t)}{\partial t^{2}}+\mathrm{j}\gamma|x(z,t)|^{2}x(z,t)+n(z,t)\tag{6}$$
where β2 is the dispersion coefficient, γ the nonlinearity coefficient and n(z, t) additive noise which is usually dominated by amplified spontaneous emission (ASE). The receiver accesses its COI via a bandpass filter with bandwidth 1/T . It then performs sampling, single-channel digital backpropagation (DBP), matched filtering using RRC filters, downsampling to the symbol rate, and mean phase rotation compensation [9]
to obtain the sequence {yi}.

## C. Cpan-Model

Surrogate models based on regular perturbation (RP) [21]
simplify computation and analysis. We use the CPAN model from [9] that has a phase noise channel

$Y_{i}=X_{i}\rm{e}^{i\Theta_{i}}+N_{i}$

where the transmit symbols {Xi} are independent and iden-
tically distributed (i.i.d.). The additive noise process {Ni} is
white and CSCG with p(ni) = NC
                                 �
                                  ni; 0, σ2
                                        n
                                         �
                                          , and the phase
noise process {Θi} is a Markov chain with unit memory:

$\Theta_{i}=\mu_{\delta}\Theta_{i-1}+\sigma_{\delta}\Lambda_{i}$ (8)

where {∆i} has i.i.d. real-valued, zero-mean, unit-variance,
Gaussian ∆i. We refer to [9, Equ. (56)] and [9, Equ. (50)] on
how to choose µδ and σδ. We set the memory of the CPAN
model to 1 because, without a whitening filter, the AIR hardly
increases for larger memory. The additive and phase noise are
independent of the transmit string

$\mathbf{X}=[X_{1},X_{2},\ldots,X_{n}]$. (9)
Unlike the Wiener phase noise model [6], the variance of Θi does not increases in i, and we have

$\Theta_{i}\sim{\cal N}(0,\sigma_{\theta}^{2})$ for all $i$. (10)

## Iii. Sic For Gaussian Inputs

Consider CSCG inputs with p(xi) = NC
�
xi; 0, σ2
x
�
. SIC
bridges the gap between AIRs for memoryless surrogate models [1] and AIRs for surrogate models with memory [9], [6]; see [19, Sec. IV]. For simplicity, we describe SIC with S = 2 stages and consider even n; generalizing to any number of stages is straightforward.

The transmit vector x of dimension n is divided into two vectors a and b of dimension n/2 in the manner

$$\mathbf{x}=[a_{1},b_{1},a_{2},b_{2},\ldots a_{n/2},b_{n/2}].\tag{11}$$
For the receive vector y, a SIC decoder works in two stages:
1) Decode a symbol-wise using the APPs p(ai|y) for all i.
2) Decode b symbol-wise using the APPs p(bi|y, a) for all
i.
Note that the decoder receives APPs from the detector without
any inter-symbol dependencies, i.e., p(ai|y) is independent of
the ak with k ̸= i.
An AIR for the first stage with independent signaling is
$$I_{1}(\mathbf{A};\mathbf{Y})=\frac{1}{n/2}\sum_{i=1}^{n/2}h(A_{i})-h(A_{i}|\mathbf{Y})\leq I(\mathbf{A};\mathbf{Y})\tag{12}$$
where we used h(Ai|Y ) ≥ h(Ai|Y , A1, . . . , Ai−1). For the second stage, an AIR is

$$I_{2}(\mathbf{B};\mathbf{Y}|\mathbf{A})=\frac{1}{n/2}\sum_{i=1}^{n/2}h(B_{i})-h(B_{i}|\mathbf{Y},\mathbf{A})\leq I(\mathbf{B};\mathbf{Y}|\mathbf{A})\tag{13}$$

where we used $h(B_{i}|\mathbf{Y},\mathbf{A})\geq h(B_{i}|\mathbf{Y},\mathbf{A},B_{1},\ldots,B_{i-1})$. An AIR for SIC is the average of $I_{1}$ and $I_{2}$:

$$I_{\rm sic}(\mathbf{X};\mathbf{Y})=\frac{1}{2}\Big{(}I_{1}(\mathbf{A};\mathbf{Y})+I_{2}(\mathbf{B};\mathbf{Y}|\mathbf{A})\Big{)}\leq I(\mathbf{X};\mathbf{Y}).\tag{14}$$

## A. Surrogate App Based On The Cpan Model

The detector wishes to compute p(ai|y) and p(bi|y, a).

However, the true pdfs are unavailable, and we therefore use the surrogate probability

$$q(\mathbf{x},\mathbf{y},\mathbf{\theta})=p(\mathbf{x})p(\mathbf{\theta})q(\mathbf{y}|\mathbf{x},\mathbf{\theta})\tag{15}$$ $$=\prod_{i=1}^{n}p(x_{i})p(\theta_{i}|\theta_{i-1})q(y_{i}|x_{i},\theta_{i})$$
with

$$p(x_{i})=\mathcal{N}_{\mathbb{C}}\left(x_{i};0,\sigma_{x}^{2}\right)\tag{16}$$ $$p(\theta_{i}|\theta_{i-1})=\mathcal{N}\left(\theta_{i};\mu_{\theta}\theta_{i-1},\sigma_{\delta}^{2}\right)$$ (17) $$p(\theta_{1})=\mathcal{N}\left(\theta_{1};0,\sigma_{\theta}^{2}\right)$$ (18) $$q(y_{i}|x_{i},\theta_{i})=\mathcal{N}_{\mathbb{C}}\left(y_{i};x_{i}\mathrm{e}^{\mathrm{i}\theta_{i}},\sigma_{n}^{2}\right)\tag{19}$$

where we slightly abused notation for clarity.

 −→η θ′′ i −→η θi . . . . . . p(θi|θi−1) = p(θi+1|θi) θi θ′′ i ←−η θ′′ i ←−η θi θ′ i ←−η θ′ i −→η θ′ i q(yi|xi, θi) xi −→η xi ←−η xi p(xi) Note that $x$ is a function of $a$ and $b$. The surrogate model allows to approximate $p(a_{i}|\mathbf{y})$ and $p(b_{i}|\mathbf{y},\mathbf{a})$ by

$$q(a_{i}|\mathbf{y})=\frac{1}{c_{1}}\,\int_{\mathbb{R}^{n}}\,\int_{\mathcal{A}\setminus\{i\}}\,q(\mathbf{x},\mathbf{y},\mathbf{\theta})\,\mathrm{d}\mathbf{x}\mathrm{d}\mathbf{\theta}\tag{20}$$ $$q(b_{i}|\mathbf{y},\mathbf{a})=\frac{1}{c_{2}}\,\int_{\mathbb{R}^{n}}\,\int_{\mathcal{B}_{\mathbf{a}}^{\setminus\{i\}}}\,q(\mathbf{x},\mathbf{y},\mathbf{\theta})\,\mathrm{d}\mathbf{x}\mathrm{d}\mathbf{\theta}\tag{21}$$
where c1 and c2 are normalization factors and

$$\mathcal{A}^{\backslash\{i\}}=\{\mathbf{x}\in\mathbb{C}^{n}:x_{2i-1}=a_{i}\}\tag{22}$$ $$\mathcal{B}^{\backslash\{i\}}_{\mathbf{a}}=\{\mathbf{x}\in\mathbb{C}^{n}:x_{2i}=b_{i},[x_{1},x_{3},\ldots,x_{n-1}]=\mathbf{a}\}\,.\tag{23}$$
We will marginalize q(x, y, θ) in both SIC-stages, where the marginalized variables depend on the stage.

## B. Efficient Computation Of The Marginal Distributions

  The sum-product algorithm (SPA) computes the desired
marginals; see [22], [23]. To illustrate the algorithm, we use
factor graphs with directed edges carrying messages. The
message of edge e in the arrow direction is denoted −→η e(.),
and that in the opposite direction ←−η e(.). In general, messages
are densities, but for simplicity, we approximate most densities
by real-valued Gaussians. In this case, −→µ e denotes the mean
and −→
    σ 2
      e the variance of −→η e(.), and likewise for ←−η e(.).
  1) First Stage Detection: Fig. 1 depicts the branches of the
first SIC-stage.

**Upward Path:** The $X_{i}$ are circularly symmetric, i.e., we have the relation $p(x_{i})=p\left(x_{i}{\rm e}^{{\rm i}\theta}\right)$ for all $\theta$, which implies

$$\begin{split}\overleftarrow{\eta}_{\,\theta^{{}^{\prime}}_{i}}(\theta_{i})&=\frac{1}{\overleftarrow{\mathbb{C}}_{\,\theta^{{}^{\prime}}_{i}}}\int_{\mathbb{C}}p(x_{i})q(y_{i}|x_{i},\theta_{i})\,{\rm d}x_{i}\\ &=\frac{1}{\leftarrow{\mathbb{C}}_{\,\theta^{{}^{\prime}}_{i}}}\int_{\mathbb{C}}p(x^{\prime}_{i})q(y_{i}|x^{\prime}_{i})\,{\rm d}x^{\prime}_{i}\ ={\rm const}.\end{split}\tag{24}$$

where x′
      i = xiejθi. By
                    1
                   ←
                   −
                   c θ′
                     i
                      , and likewise for other messages,

we denote a constant that normalizes to a valid pdf.

Rightward Path: Using −→η θ1(θ1) = p(θ1), we obtain

$$\begin{split}\overrightarrow{\eta}_{\,\theta_{2}}(\theta_{2})&=\frac{1}{\overrightarrow{c}_{\,\theta_{2}}}\int_{\mathbb{R}}\overrightarrow{\eta}_{\,\theta_{1}}(\theta_{1})\overleftarrow{\eta}_{\,\theta_{1}^{\prime}}(\theta_{1})p(\theta_{2}|\theta_{1})\,\mathrm{d}\theta_{1}\\ &=\int_{\mathbb{R}}p(\theta_{1})p(\theta_{2}|\theta_{1})\,\mathrm{d}\theta_{1}=p(\theta_{2})\end{split}\tag{25}$$
and recursively −→η θi(θi) = p(θi) for all i.

Leftward Path: We similarly have

$$\begin{split}\overleftarrow{\eta}\,_{\theta^{\prime\prime}_{n-1}}(\theta_{n-1})&=\frac{1}{\overline{c}\,_{\theta^{\prime\prime}_{n-1}}}\,\int_{\mathbb{R}}\,\overleftarrow{\eta}\,_{\theta^{\prime}_{n}}(\theta_{n})p(\theta_{n}|\theta_{n-1})\mathrm{d}\theta_{n}\\ &=\mathrm{const.}\end{split}\tag{26}$$
and recursively ←−η θ′′
i (θi) is constant in θi.

Downward Path: We have

$$\dot{\eta}_{\,\theta^{\prime}_{i}}(\theta_{i})=\frac{1}{\dot{\overline{c}}_{\,\theta^{\prime}_{i}}}\dot{\eta}_{\,\theta_{i}}(\theta_{i})\dot{\overline{\eta}}_{\,\theta^{\prime\prime}_{i}}(\theta_{i})=p(\theta_{i})\tag{27}$$
and

$$\overleftarrow{\eta}_{\,x_{i}}(x_{i})=\frac{1}{\overleftarrow{C}_{\,x_{i}}}\,\int_{\mathbb{R}}\overrightarrow{\eta}_{\,\theta^{{}^{\prime}}_{i}}(\theta_{i})q(y_{i}|x_{i},\theta_{i})\mathrm{d}\theta_{i}$$ $$=\frac{1}{\overleftarrow{C}_{\,x_{i}}}\,\int_{\mathbb{R}}\mathcal{N}\left(\theta_{i};0,\sigma_{\theta}^{2}\right)\mathcal{N}_{\mathbb{C}}\left(y_{i};x_{i}\mathrm{e}^{\mathrm{i}\theta_{i}},\sigma_{n}^{2}\right)\mathrm{d}\theta_{i}.\tag{28}$$

The surrogate APP $q(x_{i}|\boldsymbol{y})$ may now be calculated using

$$f_{i}(x_{i})=\frac{1}{cf_{i}}\overrightarrow{\eta}_{\,x_{i}}(x_{i})\overleftarrow{\eta}_{\,x_{i}}(x_{i})\tag{29}$$

where cfi normalizes fi to a valid pdf.
  We approximate fi by a complex Gaussian density with
mean µfi = Efi[X], variance σ2
                            fi = Efi
                                    �
                                     |X − µfi|2�
                                                and
pseudo-variance p2
               fi = Efi
                      �
                       (X − µfi)2�
                                 . As derived in App.
A, we thus have

$$q(x_{i}|\mathbf{y})={\cal N}_{\mathbb{C}}\left(x_{i};\mu_{f_{i}},\sigma_{f_{i}}^{2},p_{f_{i}}^{2}\right)\tag{30}$$
with

$$\mu_{f_{i}}=y_{i}\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\exp\left(-\frac{\sigma_{\theta}^{2}}{2}\right)\tag{31}$$ $$\sigma_{f_{i}}^{2}=\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\left(\sigma_{n}^{2}+\left|y_{i}\right|^{2}\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\right)-\left|\mu_{f_{i}}\right|^{2}$$ (32) $$p_{f_{i}}^{2}=y_{i}^{2}\frac{\sigma_{x}^{4}}{\sigma_{y}^{4}}\exp\left(-2\sigma_{\theta}^{2}\right)-\mu_{f_{i}}^{2}\tag{33}$$

where $\sigma_{y}^{2}=\sigma_{x}^{2}+\sigma_{n}^{2}$. At this point, we are interested only in $q(x_{i}|\mathbf{y})$ for odd $i$, as these are the symbols detected in the first SIC-stage.

2) _Second Stage Detection_: In the second stage, the symbols in $\mathbf{x}$ with an odd index $i$, namely those described by $\mathbf{a}$, have been detected and decoded. Hence, branches of the form Fig. 1 and branches of the form Fig. 2 alternate. The former corresponds to the elements in $\mathbf{b}$ or those with even index of $\mathbf{x}$, respectively, and the latter to those in $\mathbf{a}$ or odd index of $\mathbf{x}$.

 $\overrightarrow{\eta}\,\theta_{i}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$$\overrightarrow{\eta}\,\theta_{i}^{\prime}$\(\overrightarrow{\eta
Upward Path: For odd i, the message passed over θ′
i is

←−η θ′ i(θi) = 1 ←−c θ′ i p(xi)q(yi|xi, θi) (34) = 1 − p(xi) πσ2n exp σ2n ←−c θ′ i � � ��yi − xiejθi��2 ∝ exp �2|yi||xi| σ2n cos � θi − (∠yi − ∠xi) �� .

This message consists of periodic repetitions of pulses, each
similar to a Gaussian with mean ∠yi − ∠xi + 2πk for k ∈ N.
As we show later on, messages on the left- and rightward
paths, i.e., −→η θi and ←−η ′′
                      θi, are Gaussians with near-zero mean
and rapidly decaying tails. As products of these messages
are passed on, we may focus on the period closest to zero
by considering m (∠yi − ∠xi) which maps ∠yi − ∠xi to the
interval [−π, π). Using the approximation cos(γ) ≈ 1 − γ2/2,
which is valid for small values of γ, we obtain

←−η θ′ i(θi) ≈ N � θi; ←− µ θ′ i, ←− σ 2 θ′ i � (35) ←− µ θ′ i = m (∠yi − ∠xi) (36) ←− σ 2 θ′ i = σ2 n 2|yi||xi|. (37) If i is even, as before, then ←−η θ′ i(θi) is constant in θi. Rightward Path: We show that all messages in the rightward path are approximately Gaussian, that is −→η θi(θi) ≈ N � θi; −→ µ θi, −→ σ 2 θi � (38) −→η θ′′ i (θi) ≈ N � θi; −→µ θ′′ i , −→σ 2 θ′′ i � . (39)

If −→η θi is Gaussian, then −→η θ′′
                                  i is either a product of Gaussians
or a product of a Gaussian and a constant, and hence Gaussian
[24]. Explicitly, the parameters of −→η θ′′
                                             i depend on i as follows.

- If i is odd, then xi was already decoded in the first stage
and is a branch of the form shown in Fig. 2. Hence −→
µ θ′′
i
is a product of Gaussians and [24]
$$\overrightarrow{\mu}_{\theta_{i}}\stackrel{{\leftarrow}}{{\sigma}}\stackrel{{2}}{{\theta}}_{i}+\overleftarrow{\mu}_{\theta_{i}}\stackrel{{\rightarrow}}{{\sigma}}\stackrel{{2}}{{\theta}}_{i}\tag{40}$$ $$\overrightarrow{\sigma}\stackrel{{2}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\sigma}}\stackrel{{2}}{{\theta}}_{i}$$ (41) $$\overrightarrow{\sigma}\stackrel{{2}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\sigma}}\stackrel{{2}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}{{\theta}}_{i}\stackrel{{\leftarrow}}\stackrel{{{\leftarrow}}}\tag
- If i is even, then xi was not decoded in the first stage
and is a branch of the form shown in Fig. 1. Hence, −→η θ′′
i

is a product of a Gaussian and a constant, and therefore
−→
µ θ′′
   i = −→
        µ θi and −→
                 σ 2
                   θ′′
                    i = −→
                         σ 2
                           θi.

If $\overrightarrow{\eta}_{\theta_{i}^{\prime\prime}-1}$ is Gaussian, then $\overrightarrow{\eta}_{\theta_{i}}$ is the marginalization over the product of a Gaussian and a conditional Gaussian. We have

$$\begin{split}\int_{\mathbb{R}}\mathcal{N}\left(\theta_{i-1};\mu,\sigma^{2}\right)&\mathcal{N}\left(\theta_{i};\mu_{\delta}\theta_{i-1},\sigma_{\delta}^{2}\right)\mathrm{d}\theta_{i-1}\\ &=\mathcal{N}\left(\theta_{i};\mu_{\delta}\mu,\mu_{\delta}^{2}\sigma^{2}+\sigma_{\delta}^{2}\right)\end{split}\tag{42}$$
from which we obtain

= N � θi; µδµ, µ2 δσ2 + σ2 δ � (42) R −→η θ′′ i−1(θi−1)p(θi|θi−1)dθi−1 −→η θi(θi) = � ≈ N � θi; µδ−→ µ θ′′ i−1, µ2 δ−→σ 2 θ′′ i−1 + σ2 δ � . (43)

With −→η θ1(θ1) = p(θ1) = N
                          �
                           θ1; 0, σ2
                                 θ
                                  �
                                    for any stage, we
arrive at (38)–(39) by induction.
Leftward Path: Denote by i′ the largest index of all symbols
decoded in earlier stages. In the second of two stages, i′ =
n−1 if n is even and i′ = n else. All branches to the right of
the i′-th branch are of the form shown in Fig. 1 and therefore
←−η θ′′
  i′(θi′) is constant in θi′. Therefore, we find that (note the
different subscripts)
                ←−η θi′ (θi′) = ←−η θ′
                             i′ (θi′)
                                                (44)

is approximately Gaussian, see (35). This is also true for i′ =
n. If ←−η θi+1 is Gaussian in θi+1, then we update

R ←−η θi+1(θi+1)p(θi+1|θi)dθi+1 ←−η θ′′ i (θi) = � . (45) θi; ←−µ θi+1 ≈ N µδ , ←−σ 2 θi+1 + σ2 δ µ2 δ � �
where the update rule depends on the index i.

Similar to the rightward path, for i ≤ i′, we have ←−η θi(θi) ≈ N � θi; ←− µ θi, ←− σ 2 θi � (46)
- If i is odd, then

$$\overleftarrow{\mu}_{\,\theta_{i}}=\frac{\overleftarrow{\mu}_{\,\theta_{i}^{\prime\prime}}\overleftarrow{\sigma}_{\,\theta_{i}^{\prime}}^{2}+\overleftarrow{\mu}_{\,\theta_{i}^{\prime}}\overleftarrow{\sigma}_{\,\theta_{i}^{\prime\prime}}^{2}}{\overleftarrow{\sigma}_{\,\theta_{i}^{\prime}}^{2}+\overleftarrow{\sigma}_{\,\theta_{i}^{\prime\prime}}^{2}}\tag{47}$$ $$\overleftarrow{\sigma}_{\,\theta_{i}}^{2}=\frac{\overleftarrow{\sigma}_{\,\theta_{i}^{\prime}}^{2}\overleftarrow{\sigma}_{\,\theta_{i}^{\prime\prime}}^{2}}{\overleftarrow{\sigma}_{\,\theta_{i}^{\prime}}^{2}+\overleftarrow{\sigma}_{\,\theta_{i}^{\prime\prime}}^{2}}.\tag{48}$$
* If $i$ is even, then $\overleftarrow{\mu}_{\,\theta_{i}}=\overleftarrow{\mu}_{\,\theta_{i}^{\prime\prime}}$ and $\overleftarrow{\sigma}_{\,\theta_{i}}^{2}=\overleftarrow{\sigma}_{\,\theta_{i}^{\prime\prime}}^{2}$.

Downward Path: As both −→η θi(θi) and ←−η θ′′
                                 i (θi) are Gaussian
in θi, their product is also Gaussian. That is, we have

$$\begin{split}\overrightarrow{\eta}_{\,\theta^{\prime}_{i}}(\theta_{i})&=\frac{1}{\overrightarrow{\epsilon}_{\,\theta^{\prime}_{i}}}\overrightarrow{\eta}_{\,\theta_{i}}(\theta_{i})\overleftarrow{\eta}_{\,\theta^{\prime\prime}_{i}}(\theta_{i})\\ &\approx\mathcal{N}\left(\theta_{i};\overrightarrow{\mu}_{\,\theta^{\prime}_{i}},\overrightarrow{\sigma}^{2}_{\,\theta^{\prime}_{i}}\right)\end{split}\tag{49}$$

with

$$\overrightarrow{\mu}_{\,\theta^{\prime}_{i}}=\frac{\overrightarrow{\mu}_{\,\theta_{i}}\overrightarrow{\sigma}^{2}_{\,\theta^{\prime\prime}}+\overrightarrow{\mu}_{\,\theta^{\prime\prime}_{i}}\overrightarrow{\sigma}^{2}_{\,\theta_{i}}}{\overrightarrow{\sigma}^{2}_{\,\theta_{i}}+\overrightarrow{\sigma}^{2}_{\,\theta^{\prime\prime}_{i}}}\tag{50}$$ $$\overrightarrow{\sigma}^{2}_{\,\theta^{\prime}_{i}}=\frac{\overrightarrow{\sigma}^{2}_{\,\theta_{i}}\overrightarrow{\sigma}^{2}_{\,\theta^{\prime\prime}_{i}}}{\overrightarrow{\sigma}^{2}_{\,\theta_{i}}+\overrightarrow{\sigma}^{2}_{\,\theta^{\prime\prime}_{i}}}.\tag{51}$$
Similar to the first stage, for even i we approximate q(xi|y, a)
by a complex Gaussian. Simulations show that using CSCGs suffices, and the mean and variance are (see App. A)

$$\mu_{f_{i}}=y_{i}\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\exp\left(-\frac{1}{2}\frac{\overrightarrow{\mu}_{\theta_{i}^{\prime}}^{2}-(\overrightarrow{\mu}_{\theta_{i}^{\prime}}-\mathrm{j}\overrightarrow{\sigma}_{\theta_{i}^{\prime}}^{2})^{2}}{\overrightarrow{\sigma}_{\theta_{i}^{\prime}}^{2}}\right)\tag{52}$$ $$\sigma_{f_{i}}^{2}=\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\left(\sigma_{n}^{2}+|y_{i}|^{2}\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}}\right)-|\mu_{f_{i}}|^{2}\,.\tag{53}$$

## C. Extension To S Sic-Stages

An extension to S stages is straightforward. The first stage can be detected as described by (30)–(33). For stage s > 1, all xi corresponding to stages s′ < s are assumed to be known.

Also, the following means and variances should be calculated beforehand for appropriate indices i:

$$\overleftarrow{\mu}_{\theta^{\prime}_{i}}=m\left(\angle_{y_{i}}-\angle_{x_{i}}\right),\quad\overleftarrow{\sigma}_{\theta^{\prime}_{i}}^{2}=\frac{\sigma_{n}^{2}}{2|y_{i}||x_{i}|}.\tag{54}$$

For Gaussian messages, we collect the mean and variance in one vector

$$\overrightarrow{\boldsymbol{\eta}}_{\theta_{i}}=\left[\overrightarrow{\mu}_{\theta_{i}},\overrightarrow{\sigma}_{\theta_{i}}^{2}\right]\tag{55}$$

and likewise for other messages. We also define the function

$$g(\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2})=\left[\frac{\mu_{1}\sigma_{2}^{2}+\mu_{2}\sigma_{1}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}},\frac{\sigma_{1}^{2}\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\right]\tag{56}$$

which describes the mean and variance of the product of
Gaussians with parameters η1 and η2.
  Algorithm 1 shows the computations for stage s. The set
Is has the symbol indices decoded in earlier stages, e.g., for
S = 2 that is I1 = ∅ and I2 = {1, 3, . . ., n − 1}. We have
−→
η θ1 = [0, σ2
          θ]. For i′ = n − S + (s − 1), which is the index
of the last symbol in x decoded prior to stage s > 1, we have

$$\overline{\eta}_{\,\theta_{i^{\prime}}}=\left[m\left(\angle_{y_{i^{\prime}}}-\angle_{x_{i^{\prime}}}\right),\frac{\sigma_{n}^{2}}{2|y_{i^{\prime}}||x_{i^{\prime}}|}\right]\tag{57}$$
and (see (45))

$$\overleftarrow{\eta}_{\,\theta^{\prime\prime}_{i^{\prime}}-1}=\left[\frac{m\left(\angle_{y_{i^{\prime}}}-\angle_{x_{i^{\prime}}}\right)}{\mu_{\delta}},\,\frac{\sigma_{n}^{2}}{2|y_{i^{\prime}}|\,|x_{i^{\prime}}|}+\sigma_{\delta}^{2}\right].\tag{58}$$

Let $\mathbf{x}^{(s)}$ be the symbols decoded in stage $s$, i.e., for two stages $\mathbf{a}=\mathbf{x}^{(1)}$ and $\mathbf{b}=\mathbf{x}^{(2)}$. For $i\in\{s,s+S,s+2S,\ldots\}$, we have

$$q(x_{i}|\mathbf{y},\mathbf{x}^{(1)},\ldots,\mathbf{x}^{(s-1)})=\mathcal{N}_{\mathbb{C}}\left(x_{i};\mu_{f_{i}},\sigma_{f_{i}}^{2}\right)\tag{59}$$

where $\mu_{f_{i}}$ and $\sigma_{f_{i}}^{2}$ can be calculated from the output of algorithm 1 and (52)-(53).

Note that our Gaussian approximate message passing algorithm uses messages that are vectors of dimension two with a mean and variance. Also, the calculations for the $\overleftarrow{\eta}_{\,\theta^{\prime}_{i}}$, $\overrightarrow{\eta}_{\,\theta^{\prime}_{i}}$, $\mu_{f_{i}}$, and $\sigma_{f_{i}}^{2}$ can be parallelized.

 Input: y, x(1), . . . , x(s−1), Is, s, S, n, i′,−→ η θ1, ←− η θ′′ i′−1, ←− η θ′ i for i ∈ Is Output: −→ η θ′ i ⊲ Rightward Path for i ← 1 to n − 1 do if i ∈ Is then −→ η θ′′ i ← g(−→ η θi, ←− η θ′ i) else−→ η θ′′ i ← −→ η θi end if −→ η θi+1 ← � µδ−→µ θ′′ i , µ2 δ−→ σ 2 θ′′ i + σ2 δ � µ2 δ end for ⊲ Leftward Path for i ← i′ − 1 to 2 do if i ∈ Is then ←− η θi ← g(←− η θ′′ i , ←− η θ′ i) else←− η θi ← ←− η θ′′ i end if ←− η θi−1′′ ← � ← − µ θi µδ , ← − σ 2 θi +σ2 δ � end for ⊲ Downward Path for l ← 0 to ⌊n/S⌋ − 1 do i ← s + lS −→ η θ′ i ← g(−→ η θi, ←− η θ′′ i ) end for

## D. Lower Bound On Mutual Information

We lower bound I1(A; Y ) by using

$$h_{q}(A_{i}|\mathbf{Y})=-\int p(\mathbf{y})\int p(a_{i}|\mathbf{y})\log q(a_{i}|\mathbf{y})\mathrm{d}a_{i}\mathrm{d}\mathbf{y}\tag{60}$$ $$=h(A_{i}|\mathbf{Y})+D\left(p(A_{i}|\mathbf{Y})||q(A_{i}|\mathbf{Y})\right)$$ $$\geq h(A_{i}|\mathbf{Y})$$
where D(·∥·) is informational divergence that is non-negative.

We thus have

$$I_{1,q}(\mathbf{A};\mathbf{Y})=\frac{1}{n/2}\sum_{i=1}^{n/2}h(A_{i})-h_{q}(A_{i}|\mathbf{Y})\leq I_{1}(\mathbf{A};\mathbf{Y}).\tag{61}$$
Likewise, we have

$$I_{2,q}(\mathbf{B};\mathbf{Y}|\mathbf{A}):=\frac{1}{n/2}\sum_{i=1}^{n/2}h(B_{i})-h_{q}(B_{i}|\mathbf{Y},\mathbf{A})\leq I_{2}(\mathbf{B};\mathbf{Y}|\mathbf{A})\tag{62}$$

with

$$\begin{split}h_{q}(B_{i}|\mathbf{Y},\mathbf{A})&=-\int\int p(\mathbf{y},\mathbf{a})\int p(b_{i}|\mathbf{y},\mathbf{a})\\ &\cdot\log q(b_{i}|\mathbf{y},\mathbf{a})\,\mathrm{d}b_{i}\mathrm{d}\mathbf{y}\mathrm{d}\mathbf{a}.\end{split}\tag{63}$$
As we use i.i.d. CSCG inputs with variance σ2
x, we have

$h(A_{i})=h(B_{i})=\log(\pi\mbox{e}\sigma_{x}^{2})$. (64)
We approximate (60) and (63) by simulating transmission of Nseq sequences {xk} and {yk} and compute

$$h_{q}(A_{i}|\mathbf{Y})\approx-\frac{1}{N_{\rm seq}}\sum_{k=1}^{N_{\rm seq}}\log q(a_{k,i}|\mathbf{y}_{k})\tag{65}$$ $$h_{q}(B_{i}|\mathbf{Y},\mathbf{A})\approx-\frac{1}{N_{\rm seq}}\sum_{k=1}^{N_{\rm seq}}\log q(b_{k,i}|\mathbf{y}_{k},\mathbf{a}_{k}).\tag{66}$$

## E. Simulation Results

  Table I lists the simulation parameters; see [9, Sec. VIII].
However, the receiver does not use a whitening filter and uses a
unit-memory surrogate channel. We use 24 sequences of 8192
symbols each for training, e.g., to obtain µδ and σ2
                                                   δ, and 120
sequences of 8192 symbols each for testing, i.e., Nseq = 120.
  We first investigate the AIRs of the CPAN channel with
noise variances that mimic those of the nonlinear fiber-optic
channel. Fig. 3 plots the variances σ2
                                     θ, σ2
                                         δ of the phase noise
process, and the variance σ2
                            n of the AWGN. These variances
increase with Ptx due to the nonlinear interference. In contrast,
the variance σ2
              ASE of the ASE is constant at approximately
2.95 · 10−7.
  Fig. 4a show the AIRs for the following benchmarking
scenarios:

1
a memoryless AWGN surrogate model,
2
a memoryless surrogate model with i.i.d. Gaussian phase noise and independent AWGN,
3
a JDD-receiver based on particle filtering [6], [9], and

 4
   a genie-aided receiver with perfect knowledge of the
   phase noise, so the AIR is I(X; Y |Θ).
The solid black curve shows the AWGN channel capacity with
ASE only, which upper bounds the CPAN channel capacity.
 The inequality (14) shows that SIC cannot outperform
JDD. SIC improves the memoryless receivers, and the mem-
oryless phase noise receiver AIR is the same as the SIC
AIR with S = 1. As Θ and X are independent, we have
I(X; Y |Θ) ≥ I(X; Y ). Thus, the genie-aided receiver with
perfect knowledge of the phase noise has larger AIRs than the
JDD receiver.
 Fig. 4a shows that SIC with 2 and 4 stages loses significant
AIR compared to JDD. To maintain a rate loss of less than 1 %,
one needs at least 8 SIC-stages. The AIR of the SIC receiver
with 64 stages is very close to the AIR of the genie-aided
receiver with perfect knowledge of the phase noise process.

| Parameter                        |
|----------------------------------|
| Fiber Length                     |
| L                                |
| 1000 km                          |
| Attenuation coefficient          |
| α                                |
| 0.2 dB km                        |
| −1                               |
| Dispersion Coefficient           |
| β                                |
| 2                                |
| −21.7 ps                         |
| 2                                |
|                                  |
| km                               |
| −1                               |
| Nonlinear coefficient            |
| γ                                |
| 1.27 W                           |
| −1                               |
|                                  |
| km                               |
| −1                               |
| Phonon occupancy factor          |
| η                                |
| 1                                |
| One-sided number of WDM channels |
| b                                |
| 2                                |

We infer that the proposed SIC receiver performs well for
CPAN models. To further improve the rates for the nonlinear
fiber-optic channel, one must improve the surrogate model,
e.g., by considering correlations in the additive noise [6].
  Studies of the dispersion-free nonlinear-fiber optic channel
show that derived models with zero dispersion have AIRs
that grow as 1

             2 log(SNR) + O(1) where SNR ∝ Ptx; see [25],
[26], [27], [28]. In contrast, the CPAN AIRs decrease with Ptx
because the additive noise variance σ2
                                     n increases with Ptx, see
Fig. 3. Both the phase and amplitude of the signal experience
distortions that increase with transmit power.
  Fig. 4b shows the AIRs for the nonlinear fiber-optic chan-
nel with a receiver that uses the CPAN surrogate model.
The solid curve again shows the capacity of the AWGN-
channel distorted by ASE only, which upper bounds the
capacity [29], [30]. We remark that the inequality in (14)
does not hold for mismatched mutual information (MI), i.e.,
1/2 (I1,q(A; Y ) + I2,q(B; Y |A)) might exceed Iq(X; Y )
based on JDD and particle filtering, as used in [9]. Second,
the AIRs of JDD are slightly smaller than those in [9], which
is mostly due to the lack of a whitening filter.
  We again see that 8 SIC-stages provide AIRs similar to those
of JDD. However, for 16 or more SIC-stages, the AIR of SIC
exceeds that of JDD. We infer that the channel description
of the SIC channel better approximates the true channel than
JDD does. The 64-stage SIC-receiver gains approximately
0.52 bits per channel use (bpcu), or 6.4 %, in rate over the
memoryless AWGN receiver.

## Iv. Sic For Ring Constellations

This section studies ring constellations. The transmit symbols have an independent amplitude $R_{i}$ and phase $\Gamma_{i}$. The amplitude is sampled from a discrete distribution in $\mathcal{R}=\{\tilde{r}_{1},\ldots,\tilde{r}_{n_{v}}\}$, and the phase is sampled from a continuous distribution in $[-\pi,\pi)$. We use the distributions

$$P(\tilde{r}_{i})=w_{i},\quad p(\gamma_{i})=\frac{1}{2\pi},\text{for}\gamma_{i}\in[-\pi,\pi).\tag{67}$$
Like CSCG inputs, ring constellations are circularly symmetric, and therefore we have (see (24))

$$\overleftarrow{\eta}\,\theta^{\prime}_{i}(\theta_{i})=\frac{1}{\overleftarrow{C}\,\theta^{\prime}_{i}}\,\int_{\mathbb{C}}p(x_{i})q(y_{i}|x_{i},\theta_{i})\mathrm{d}x_{i}=\mathrm{const}.\tag{68}$$
Motivated by CSCG inputs, we use equidistant rings with
˜rℓ = ℓ · ∆r and probabilities wℓ that model a Rayleigh Distribution with variance σ2
x, i.e.,

$$w_{\ell}=\frac{\tilde{r}_{\ell}\exp\left(-\frac{\tilde{r}_{\ell}^{2}}{\sigma_{x}^{2}}\right)}{\sum_{m=1}^{n_{r}}\tilde{r}_{m}\exp\left(-\frac{\tilde{r}_{m}^{2}}{\sigma_{x}^{2}}\right)}.\tag{69}$$
We name this constellation unidistant Rayleigh ring (URR). The transmit power is

$$\mathrm{E}[|X|^{2}]=\sigma_{x}^{2}=\Delta r^{2}\frac{\sum_{\ell=1}^{n_{r}}\ell^{3}\exp\left(-\frac{\ell^{2}\Delta r^{2}}{\sigma_{x}^{2}}\right)}{\sum_{\ell=1}^{n_{r}}\ell\exp\left(-\frac{\ell^{2}\Delta r^{2}}{\sigma_{x}^{2}}\right)}\tag{70}$$

and we set $\sigma_{x}^{2}=P_{\mathrm{tx}}$. The $\Delta r$, which satisfies the power constraint, is found numerically.

URR constellations approximate a CSCG for large $n_{r}$. Fig. 5 shows the AIRs for memoryless AWGN channels with $\sigma_{n}^{2}=2.95\cdot10^{-7}$, which is approximately the ASE noise variance for the parameters in Table I. The horizontal line indicates the largest AIR of 2 SIC-stages in Fig. 4b, which is the peak value we attempt to reach. Observe that 32 rings are needed to prevent significant deviation from Gaussian inputs at the target AIR.

## A. Mutual Information Estimation

Suppose X has independent amplitudes R and phases Γ
that are transmitted through a channel pY |X; see Fig. 6. By
10
8
AIR [bpcu]
6
the chain rule of MI, we have

$$I(\mathbf{X};\mathbf{Y})+\underbrace{I(\mathbf{R},\mathbf{\Gamma};\mathbf{Y}|\mathbf{X})}_{=0}=I(\mathbf{R},\mathbf{\Gamma};\mathbf{Y})+\underbrace{I(\mathbf{X};\mathbf{Y}|\mathbf{R},\mathbf{\Gamma})}_{=0}\tag{71}$$

and hence $I(\mathbf{X};\mathbf{Y})=I(\mathbf{R};\mathbf{Y})+I(\mathbf{\Gamma};\mathbf{Y}|\mathbf{R})$. Consider (11) and define

$$a_{i}=r_{2i-1}\exp(\mathrm{j}\alpha_{i}),\quad b_{i}=r_{2i}\exp(\mathrm{j}\beta_{i}).\tag{72}$$

We divide only the phase noise vector into components related
to a and b because, as we will show later, the absolute value
can be detected and decoded in a memoryless fashion, hence
no SIC receiver is needed.
  AIRs for the absolute value and phase channels are

IR(R; Y ) = 1 n i=1 H(Ri) − H(Ri|Y ) n � (73) n/2 I1(α; Y |R) = 1 i=1 h(αi) − h(αi|Y , R) n/2 � n/2 I2(β; Y |R, α) = 1 i=1 h(βi) − h(βi|Y , R, α). n/2 �
The following sum is an AIR for SIC:

Isic(X; Y ) = IR(R; Y ) + 1 2 � I1(α; Y |R) + I2(β; Y |R, α) � ≤ I(X; Y ). (74) Similar to (15), consider q(r, α, β, y, θ) = q(r, γ, y, θ) = i=1 P(ri)p(γi)p(θi|θi−1)q(yi|ri, γi, θi) (75) n �

where γ describes the angles of the entries of x, and is thus
a function of α and β. The vector x is a function of r and
γ. As before, we discard dependencies for the sake of clarity.
The receiver wishes to calculate

q(ri|y) = 1 c3 r∈R\{i} q(r, γ, y, θ)dγdθ (76) Rn � � Π � q(αi|y, r) = 1 c4 Rn � � Π\{i} q(r, γ, y, θ)dγdθ (77) q(r, γ, y, θ)dγdθ (78) q(βi|y, r, α) = 1 c5 Rn � � Π\{i} α where R\{i} = {r′ ∈ Rn : r′ i = ri} (79) Π = [−π, π)n (80) Π\{i} = {γ ∈ [−π, π)n : γ2i−1 = αi} (81) Π\{i} α = {γ ∈ [−π, π)n : α(γ) = α ∧ γ2i = βi}. (82)
with α(γ) = [γ1, γ3, . . . , γn−1]. As before, we marginalize q(r, γ, y, θ), but the variables subject to marginalization depend on the SIC-stage.

_B. Computing the Marginal Distributions_

_1) Absolute Value Detection:_ The graph used to detect the amplitudes $r$ has branches shown in Fig. 7. Using

$$\int_{-\pi}^{\pi}q(y_{i}|r_{i},\gamma_{i},\theta_{i})\mathrm{d}\gamma_{i}=\frac{2}{\sigma_{n}^{2}}\exp\left(-\frac{|y_{i}|^{2}+r_{i}^{2}}{\sigma_{n}^{2}}\right)I_{0}\left(\frac{2|y_{i}|r_{i}}{\sigma_{n}^{2}}\right)\tag{83}$$

and $p(\gamma_{i})=\frac{1}{2\pi}$, one can again show that

$$\begin{split}\overleftarrow{\eta}_{\,\theta_{i}^{\prime}}(\theta_{i})&=\frac{1}{\overleftarrow{\mathrm{C}}\,\theta_{i}^{\prime}}\sum_{r_{i}^{\prime}\in\mathcal{R}}\int_{-\pi}^{\pi}p(\gamma_{i})P(r_{i})q(y_{i}|r_{i},\gamma_{i},\theta_{i})\mathrm{d}\gamma_{i}\\ &=\mathrm{const.}\end{split}\tag{84}$$

As in (27), we obtain

$$\overrightarrow{\eta}_{\,\theta_{i}^{\prime}}(\theta_{i})=p(\theta_{i})\tag{85}$$ $$\begin{split}\overleftarrow{\eta}\,r_{i}\,(r_{i})&=\frac{1}{\overleftarrow{c}\,r_{i}}\,\int_{\mathbb{R}}\overrightarrow{\eta}\,\theta_{i}^{\prime}(\theta_{i})\int_{-\pi}^{\pi}p(\gamma_{i})q(y_{i}|r_{i},\gamma_{i},\theta_{i})\mathrm{d}\gamma_{i}\mathrm{d}\theta_{i}\\ &\propto\exp\left(-\frac{r_{i}^{2}}{\sigma_{n}^{2}}\right)I_{0}\left(\frac{2|y_{i}|r_{i}}{\sigma_{n}^{2}}\right).\end{split}\tag{86}$$

With this, upon receiving $y_{i}$ one can compute

$$q(r_{i}|\mathbf{y})=\frac{P(r_{i})\overleftarrow{\eta}\,r_{i}(r_{i})}{\sum_{\vec{r}\in\mathcal{R}}P(\vec{r})\overleftarrow{\eta}\,r_{i}(\vec{r})}.\tag{87}$$

Note that the computations for different $i$ may run in parallel.

We now investigate SIC with two stages for absolute value detection. In the second stage, branches of the type shown in Fig. 7 and Fig. 8 alternate. For odd $i$, we have branches of the form shown in Fig. 8 and

$$\begin{split}\overleftarrow{\eta}\,\theta_{i}^{\prime}(\theta_{i})&=\frac{1}{\overleftarrow{c}\,\theta_{i}^{\prime}}\,\int_{-\pi}^{\pi}p(\gamma_{i})q(y_{i}|r_{i},\gamma_{i},\theta_{i})\mathrm{d}\gamma_{i}\\ &=\text{const}.\end{split}\tag{88}$$

where we used (83). Following the same steps as before, we
recover (87). Therefore, the receiver does not use the entries
of r decoded in the first stage. We can hence use (87) to detect
all elements in r and achieve no gain using SIC.
  2) Phase Detection, First Stage: The graph is a concatena-
tion of branches of the form shown in Fig. 8. Using (83), we
again have ←−η θ′
              i(θi) = const., and −→η θ′
                                    i(θi) = p(θi). Similar
to (34), we obtain

$$q(y_{i}|r_{i},\gamma_{i},\theta_{i})\approx$$ $$\frac{1}{\sqrt{|y_{i}|r_{i}}}\mathcal{N}\left(|y_{i}|;r_{i},\frac{\sigma_{n}^{2}}{2}\right)\mathcal{N}\left(\theta_{i};m\left(\angle_{y_{i}}-\gamma_{i}\right),\frac{\sigma_{n}^{2}}{2|y_{i}|r_{i}}\right).\tag{89}$$

Using $\overrightarrow{\eta}_{\theta_{i}^{\prime}}(\theta_{i})=\mathcal{N}\left(\theta_{i};0,\sigma_{\theta}^{2}\right)$, we thus have

$$q(\gamma_{i}|\boldsymbol{y},\boldsymbol{r})=\frac{1}{c_{6}}\overrightarrow{\eta}_{\gamma_{i}}(\gamma_{i})\int_{\mathbb{R}}\overrightarrow{\eta}_{\theta_{i}^{\prime}}(\theta_{i})q(y_{i}|r_{i},\gamma_{i},\theta_{i})\mathrm{d}\theta_{i}\tag{90}$$ $$\approx\mathcal{N}\left(m\left(\angle_{y_{i}}-\gamma_{i}\right);0,\sigma_{\theta}^{2}+\frac{\sigma_{n}^{2}}{2|y_{i}|r_{i}}\right).$$

The scaling constant ensures (90) has unit integral over the
support of γi. However, as the tails decay rapidly, this constant
is larger than, but very close to 1 and may be omitted.
  3) Phase Detection, Second Stage: Branches of the form
shown in Fig. 2 for odd i and Fig. 8 for even i alternate. In
the former case, we use the approximation (35), while in the
latter case ←−η θ′
              i(θi) is constant in θi. With the same steps as
before, we obtain

$$\overrightarrow{\eta}_{\theta^{\prime}_{i}}(\theta_{i})\approx\mathcal{N}\left(\theta_{i};\overrightarrow{\mu}_{\theta^{\prime}_{i}};\overrightarrow{\sigma}_{\theta^{\prime}_{i}}^{2}\right)\tag{91}$$

where (50) and (51) give the expressions for $\overrightarrow{\mu}_{\theta^{\prime}_{i}}$ and $\overrightarrow{\sigma}_{\theta^{\prime}_{i}}^{2}$. Similar to (90), we now have

$$q(\gamma_{i}|\mathbf{y},\mathbf{r},\mathbf{\alpha})=\mathcal{N}\left(m\left(\angle_{y_{i}}-\gamma_{i}-\overrightarrow{\mu}_{\theta^{\prime}_{i}}\right);0,\overrightarrow{\sigma}_{\theta^{\prime}_{i}}^{2}+\frac{\sigma_{n}^{2}}{2|y_{i}|r_{i}}\right)\tag{92}$$

where we omitted the normalization, as discussed above.

## C. Extension To S Sic-Stages

  Extending the algorithm to S stages is straightforward. We
first decode r using (87) and the first stage of γ using (90).
For the s-th stage, we reuse algorithm 1 to obtain −→
                                                    η θ′
                                                       i =
�−→µ θ′
    i, −→σ 2
        θ′
         i

         �
           and calculate q(γi|y, r, γ(1), . . . , γ(s−1)) for i ∈
{s, s + S, s + 2S, . . .}, as indicated by (92).

## D. Lower Bound On Mutual Information

Using the same approach as in Sec. III-D, define

$$I_{R,q}(\mathbf{R};\mathbf{Y})=\frac{1}{n}\sum_{i=1}^{n}H(R_{i})-H_{q}(R_{i}|Y_{i})\tag{93}$$ $$\leq I_{R}(\mathbf{R};\mathbf{Y})$$ $$I_{1,q}(\mathbf{\alpha};\mathbf{Y}|\mathbf{R})=\frac{1}{n/2}\sum_{i=1}^{n/2}h(\alpha_{i})-h_{q}(\alpha_{i}|\mathbf{Y},\mathbf{R})$$ (94) $$\leq I_{1}(\mathbf{\alpha};\mathbf{Y}|\mathbf{R})$$ $$I_{2,q}(\mathbf{\beta};\mathbf{Y}|\mathbf{R},\mathbf{\alpha})=\frac{1}{n/2}\sum_{i=1}^{n/2}h(\beta_{i})-h_{q}(\beta_{i}|\mathbf{Y},\mathbf{R},\mathbf{\alpha})$$ (95) $$\leq I_{2}(\mathbf{\beta};\mathbf{Y}|\mathbf{R},\mathbf{\alpha}).$$
Note that

$$H(R_{i})=-\sum_{\ell=1}^{n_{r}}w_{\ell}\log w_{\ell},\quad h(\alpha_{i})=h(\beta_{i})=\log2\pi\tag{96}$$

for all $i$. The surrogate channel (differential) conditional entropies can be approximated by simulation as in Sec. III-D.

## E. Simulation Results

  Fig. 9 shows the AIRs for 2 SIC-stages. The AIRs of
CSCG modulation are plotted in dashed black for reference.
As expected from Fig. 5, the AIR increases with the number
of rings and saturates at 32 rings. Fig. 10 shows the rates as
a function of the number of SIC-stages for 32 rings. This is
similar to the results for CSCG modulation in Fig. 4.
  The phase noise variance depends on the amplitude statis-
tics. For example, M-PSK or ring constellations with one ring

cause little phase noise, whereas Gaussian modulation causes
significant phase noise [5]. Therefore, we have a tradeoff: in-
creasing the number of rings increases the amplitude channel's
rate and the phase noise variance. The left plot in Fig. 11
shows that for two SIC-stages, the AIR of the phase channel
decreases with an increasing number of rings. The right side
shows that the AIR of the amplitude channel increases by a
larger amount, and hence the overall AIR increases for an
increasing number of rings.

## V. Conclusion & Outlook

  We studied SIC-receivers to compensate for nonlinearity in
optical fiber. The receiver used the CPAN model as a surrogate
channel, and we simplified the SPA by using Gaussian mes-
sages. We proposed receiver algorithms for CSCG modulation
and ring constellations that provide AIRs comparable to those
of JDD receivers [9] for 16 or more SIC-stages. The ring
constellations perform as well as CSCG modulation for 32
or more rings. For future work, we plan to study discrete
constellations and multi-level coding with off-the-shelf codes,
as well as dual-polarization and space-division multiplexing.
Another interesting direction is to discard single-channel back-

propagation and use the proposed receiver to compensate for self-phase modulation.

           ACKNOWLEDGMENT
The authors wish to thank Daniel Plabst for inspiring discus-
sions.
 The authors acknowledge the financial support by the Fed-
eral Ministry of Education and Research of Germany in the
programme of "Souver¨an. Digital. Vernetzt.". Joint project 6G-
life, project identification number: 16KISK002.

For CSCG inputs, let

f(x) = 1 R −→η θ′(θ)q(y|x, θ)dθ (97) cf p(x) � C p(x)q(y|x, θ)dxdθ and cf = � R −→η θ′(θ) � = q(y) (98)
with q(y) = NC
�
y; 0, σ2
y
�
. Using

g(x) = x, for Ef[X] |x|2, for Ef[|X|2] x2, for Ef[X2] (99)      C g(x)f(x)dx
the second-order moments can be calculated with
�

d˜x (100) C g(˜x) p(˜x)q(y|˜x, 0) = � � R −→η θ′(θ)e−kjθdθ � �� � =:a q(y) � �� � =:b(˜x)

where ˜x = xejθ and k = 1 for Ef[X], k = 0 for Ef[|X|2],
and k = 2 for Ef[X2].
  Using −→η θ′(θ) = N
                     �
                      θ; −→µ θ′, −→σ 2
                              θ′
                                �
                                  and completing the
squares gives

−→ µ 2 θ′ − (−→µ θ′ − kj−→σ 2 θ′)2 2 −→ σ 2 θ′ � . (101) a = exp � −1
Also, b(˜x) is a CSCG

$$b(\tilde{x})={\cal N}_{\rm C}\left(\tilde{x};y\frac{\sigma_{x}^{2}}{\sigma_{y}^{2}},\frac{\sigma_{x}^{2}\sigma_{n}^{2}}{\sigma_{y}^{2}}\right)\tag{102}$$
and therefore

y σ2 x σ2y , for g(˜x) = ˜x σ2 x . σ2y σ2y C g(˜x)b(˜x)d˜x = �      � σ2 n + |y|2 σ2 x � , for g(˜x) = |˜x|2 y2 σ4 x σ4y , for g(˜x) = ˜x2.    
(103)
The moments of f follow directly:

−→ µ 2 θ′ − (−→µ θ′ − j−→σ 2 θ′)2 µf = y σ2 x 2 −→ σ 2 θ′ � (104) σ2y exp � −1 σ2 f = σ2 x σ2y σ2y � σ2 n + |y|2 σ2 x � − |µf|2 (105) −→ µ 2 θ′ − (−→µ θ′ − 2j−→ σ 2 θ′)2 p2 f = y2 σ4 x 2 −→ σ 2 θ′ � − µ2 f. σ4y exp � −1 (106)

## References

[1] R.-J. Essiambre, G. Kramer, P. J. Winzer, G. J. Foschini, and B. Goebel,
"Capacity Limits of Optical Fiber Networks," *J. Lightw. Technol.*,
vol. 28, no. 4, pp. 662–701, 2010.
[2] A. Mecozzi and R. Essiambre, "Nonlinear Shannon limit in pseudolinear
coherent systems," *J. Lightw. Technol.*, vol. 30, no. 12, pp. 2011–2024,
June 2012.
[3] R. Dar, M. Feder, A. Mecozzi, and M. Shtaif, "Properties of nonlinear
noise in long, dispersion-uncompensated fiber links," *Opt. Express*,
vol. 21, no. 22, pp. 25 685–25 699, Nov 2013.
[4] R. Dar, M. Shtaif, and M. Feder, "New bounds on the capacity of the
nonlinear fiber-optic channel," *Opt. Lett.*, vol. 39, no. 2, pp. 398–401,
Jan 2014.
[5] R. Dar, M. Feder, A. Mecozzi, and M. Shtaif, "Pulse Collision Picture of
Inter-Channel Nonlinear Interference in Fiber-Optic Communications,"
J. Lightw. Technol., vol. 34, no. 2, pp. 593–607, 2016.
[6] M. Secondini, E. Agrell, E. Forestieri, D. Marsella, and M. R. Camara,
"Nonlinearity Mitigation in WDM Systems: Models, Strategies, and
Achievable Rates," *J. Lightw. Technol.*, vol. 37, no. 10, pp. 2270–2283,
2019.
[7] M. Secondini, S. Civelli, E. Forestieri, and L. Z. Khan, "New lower
bounds on the capacity of optical fiber channels via optimized shaping
and detection," *J. Lightw. Technol.*, vol. 40, no. 10, pp. 3197–3209, 2022.
[8] F. J. Garc´ıa-G´omez and G. Kramer, "Mismatched models to lower
bound the capacity of dual-polarization optical fiber channels," J. Lightw. Technol., vol. 39, no. 11, pp. 3390–3399, 2021.
[9] ——, "Mismatched Models to Lower Bound the Capacity of Optical
Fiber Channels," *J. Lightw. Technol.*, vol. 38, no. 24, pp. 6779–6787,
2020.
[10] J. Dauwels and H.-A. Loeliger, "Computation of information rates by
particle methods," *IEEE Trans. Inf. Theory*, vol. 54, no. 1, pp. 406–409,
2008.
[11] ——, "Phase estimation by message passing," in IEEE Int. Conf.
Commun., vol. 1, 2004, pp. 523–527 Vol.1.
[12] G. Colavolpe, A. Barbieri, and G. Caire, "Algorithms for Iterative
Decoding in the Presence of Strong Phase Noise," IEEE J. Selected Areas Commun., vol. 23, no. 9, pp. 1748–1757, 2005.
[13] S. Shayovitz and D. Raphaeli, "Message passing algorithms for phase
noise tracking using Tikhonov mixtures," *IEEE Trans. Commun.*, vol. 64,
no. 1, pp. 387–401, 2016.
[14] M. P. Yankov, T. Fehenberger, L. Barletta, and N. Hanik, "Lowcomplexity tracking of laser and nonlinear phase noise in WDM optical
fiber systems," *J. Lightw. Technol.*, vol. 33, no. 23, pp. 4975–4984, 2015.
[15] A. F. Alfredsson, E. Agrell, and H. Wymeersch, "Iterative detection and
phase-noise compensation for coded multichannel optical transmission,"
IEEE Trans. Commun., vol. 67, no. 8, pp. 5532–5543, 2019.
[16] U. Wachsmann, R. F. Fischer, and J. B. Huber, "Multilevel codes:
Theoretical concepts and practical design rules," IEEE Trans. Inf. Theory, vol. 45, no. 5, pp. 1361–1391, 1999.
[17] H. Pfister, J. Soriaga, and P. Siegel, "On the achievable information rates
of finite state ISI channels," in *IEEE Global Telecommun. Conf.*, vol. 5,
2001, pp. 2992–2996 vol.5.
[18] J. B. Soriaga, H. D. Pfister, and P. H. Siegel, "Determining and
approaching achievable rates of binary intersymbol interference channels
using multistage decoding," *IEEE Trans. Inf. Theory*, vol. 53, no. 4, pp.
1416–1429, 2007.
[19] T. Prinz, D. Plabst, T. Wiegart, S. Calabr`o, N. Hanik, and G. Kramer,
"Successive Interference Cancellation for Bandlimited Channels with
Direct Detection," *IEEE Trans. Commun.*, vol. 72, no. 3, pp. 1330–1340,
2024.
[20] D.
Plabst,
T.
Prinz,
F.
Diedolo,
T.
Wiegart,
G.
B¨ocherer,
N.
Hanik,
and
G.
Kramer,
"Neural
network
equalizers
and
successive interference cancellation for bandlimited channels with
a nonlinearity," *IEEE Trans. Commun., submitted*, 2024. [Online].
Available: https://arxiv.org/abs/2401.09217
[21] A. Mecozzi and R.-J. Essiambre, "Nonlinear shannon limit in pseudolinear coherent systems," *J. Lightw. Technol.*, vol. 30, no. 12, pp. 2011–
2024, 2012.
[22] F. Kschischang, B. Frey, and H.-A. Loeliger, "Factor graphs and the
sum-product algorithm," *IEEE Trans. Inf. Theory*, vol. 47, no. 2, pp.
498–519, 2001.
[23] H.-A. Loeliger, "An introduction to factor graphs," IEEE Signal Proc.
Mag., vol. 21, no. 1, pp. 28–41, 2004.
[24] P. Bromiley, "Products and convolutions of Gaussian probability density
functions," University of Manchester, Tech. Rep., 2014.
[25] K. S. Turitsyn, S. A. Derevyanko, I. V. Yurkevich, and S. K. Turitsyn, "Information capacity of optical fiber channels with zero average
dispersion," *Phys. Rev. Lett.*, vol. 91, p. 203901, 2003.
[26] M. I. Yousefi and F. R. Kschischang, "On the per-sample capacity of
nondispersive optical fibers," *IEEE Trans. Inf. Theory*, vol. 57, no. 11,
pp. 7522–7541, 2011.
[27] G. Kramer, "Autocorrelation function for dispersion-free fiber channels
with distributed amplification," *IEEE Trans. Inf. Theory*, vol. 64, no. 7,
pp. 5131–5155, 2018.
[28] C. H¨ager and E. Agrell, "Data-driven estimation of capacity upper
bounds," *IEEE Commun. Lett.*, vol. 26, no. 12, pp. 2939–2943, 2022.
[29] G. Kramer, M. I. Yousefi, and F. R. Kschischang, "Upper bound on the
capacity of a cascade of nonlinear and noisy channels," in IEEE Inf.
Theory Workshop, 2015, pp. 1–4.
[30] M. I. Yousefi, G. Kramer, and F. R. Kschischang, "Upper bound on the
capacity of the nonlinear schr¨odinger channel," in IEEE Can. Workshop Inf. Theory, 2015, pp. 22–26.