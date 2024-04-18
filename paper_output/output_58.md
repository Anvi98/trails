# Spectral Motion Alignment For Video Motion Transfer Using Diffusion Models

Geon Yeong Park1˚, Hyeonho Jeong2˚, Sang Wan Lee1,2,3:, Jong Chul Ye1,2:

              1Bio and Brain Engineering, KAIST
        2Kim Jae Chul Graduate School of AI, KAIST
             3Brain and Cognitive Sciences, KAIST
           ˚, :: Co-first and co-corresponding authors
{pky3436, hyeonho.jeong, sangwan, jong.ye}@kaist.ac.kr

Abstract. The evolution of diffusion models has greatly impacted video generation and understanding. Particularly, text-to-video diffusion models (VDMs) have significantly facilitated the customization of input video with target appearance, motion, etc. Despite these advances, challenges persist in accurately distilling motion information from video frames.

2
Park & Jeong et al.

While existing works leverage the consecutive frame residual as the target motion vector [16], they inherently lack global motion context and are vulnerable to frame-wise distortions. To address this, here we present Spectral Motion Alignment (SMA), a novel framework that refines and aligns motion vectors using Fourier and wavelet transforms. SMA learns motion patterns by incorporating frequency-domain regularization, facilitating the learning of whole-frame global motion dynamics, and mitigating spatial artifacts. Extensive experiments demonstrate SMA's efficacy in improving motion transfer while maintaining computational efficiency and compatibility across various video customization frameworks.

Keywords: Diffusion models · Video Motion transfer · Wavelet transform

## 1 Introduction

The progression of diffusion models [12,31] has played a pivotal role in advancing video generation and comprehension. Notably, recent advancements in textconditioned Video Diffusion Models (VDMs, [3,4,9,11,13,22,30,45]) have significantly enhanced the generation of highly realistic and superior-quality videos. Given the multifaceted nature of the video, encompassing motion dynamics, foreground object appearance, etc., several studies [16, 27, 36, 39, 41, 42, 49] aim to disentangle, modify, and compose these signals according to user intent. Additionally, various approaches specifically target to customize the motion, pose, shape, or appearance of real-world videos.

In the context of motion customization, multiple studies explore how to distill motion information from pre-trained video diffusion models. Recent research suggests that motion patterns are inherently encoded in the underlying dependencies between latent frames or epsilon noises. As noted by [49], videos with similar motion tend to exhibit similar connectivity between latent frames. Additionally, [16] utilizes residual vectors between consecutive latent frames as "motion vectors," in line with optical flow principles, where residuals in consecutive frames represent motion dynamics. Specifically, they finetune temporal attention layers of pretrained VDM to align the ground-truth image-space residuals with their predicted denoised estimates. Their work reveals that aligning these predicted and ground-truth motion vectors corresponds to aligning epsilon (noise) residuals, readily obtainable from any off-the-shelf video diffusion models.

While these efforts have made technical advances in motion distillation, the pitfalls of using latent frame residuals as motion vectors have not been fully studied. This paper focuses on the potential limitations of current motion estimation in diffusion models: (a) lack of global context information, and (b)
vulnerability to frame-wise distortions. Since frame residuals may capture local motion patterns but are blind to whole-frame motion dynamics, for better motion dynamics modeling, we have to understand the whole-frame global context information during motion distillation. Furthermore, while the frame residuals contain motion information, they may also contain inevitable disruptive variations that are unrelated to motion. These variations may include abrupt changes in the background, distortions, consecutive frame inconsistencies, or lighting condition changes.

To address these challenges, here we present Spectral Motion Alignment
(SMA), a novel Fourier and wavelet-transform-based motion vector refinement and alignment framework. This includes two primary components: First, to learn the global motion context, we propose the spectral alignment loss between predicted and ground-truth motion vectors within the wavelet domain. This facilitates the learning of multi-scale motion dynamics by leveraging rich waveletdomain representations of video considering the global frame transitions. Moreover, to mitigate the spatial artifacts and inconsistency in motion vectors, we propose 2D FFT-based motion vector refinement that aligns the amplitude and phase spectrum of ground truth and predicted motion vectors with prioritizing low-frequency components. This is because the high-frequency components in motion vectors may be associated with frame-wise non-motion-related artifacts (Figure 6). To sum up, we encourage accurate motion transfer via harmonized global and local levels of frequency-domain regularization.

Our contributions are summarized as follows:

- We introduce the Spectral Motion Alignment (SMA), a frequency-domain
motion alignment framework that learns the underlying motion dynamics of input video via frequency-based regularization. Since conventional methods mostly rely on pixel-domain motion distillation, the proposed framework is orthogonal to existing motion customization models.
- SMA imposes negligible memory and computational burdens, as most offthe-shelf VDMs can readily compute estimates of motion vectors. For instance, VMC [16] with SMA demonstrates lightweight (15GB vRAM) and rapid (< 5 minutes) training.
- We validate the advantage of SMA across diverse motion patterns and subjects, and across various video motion transfer frameworks such as Video Diffusion-based [49], Cascaded Video Diffusion-based [16], Text-to-Image Diffusion-based [38], and ControlNet-based models [7].
4
Park & Jeong et al.

## 2 Preliminaries 2.1 Diffusion Models.

Diffusion models [12,31] generate samples from the Gaussian noise through reverse denoising processes. Given a clean sample x0 " pdatapxq, the forward process is defined as a Markov chain with forward conditional densities

ppxt | xt´1q " Npxt | βtxt´1, p1 ´ βtqIq (1) ¯αx0, p1 ´ ¯αqIq, ptpxt | x0q " Npxt | ?

where xt P Rd is a noisy latent variable at time t that has the same dimension as
x0, and βt denotes an increasing sequence of noise schedule where αt :" 1 ´ βt
and ¯αt :" Πt
           i"1αi. Then, the goal of diffusion model training is to obtain a
residual denoiser ϵθ˚:

θ˚ :" argmin θ Ext"ptpxt | x0q,x0"pdatapx0q,ϵ"N p0,Iq " ∥ϵθpxt, tq ´ ϵ∥ ‰ . (2)
The reverse sampling from qpxt´1|xt, ϵθ˚pxt, tqq is then achieved by

xt´1 " 1 ?αt ´ xt ´ 1 ´ αt ?1 ´ ¯αt ϵθ˚pxt, tq ¯ ` ˜βtϵ, (3)
where ϵ " Np0, Iq and ˜βt :"
1´¯αt´1
1´¯αt βt. To accelerate sampling, DDIM [32]
further proposes another sampling method as follows:

1 ´ ¯αt´1 ´ η2 ˜βt 2ϵθ˚pxt, tq ` η ˜βtϵ, (4) xt´1 " ?¯αt´1ˆx0ptq ` b
where η P r0, 1s is a stochasticity parameter, and ˆx0ptq is the denoised estimate which can be equivalently derived using Tweedie's formula [8]:

1 ´ ¯αtϵθ˚pxt, tqq. (5) ˆx0ptq :" 1 ?¯αt pxt ´ ?
For a text-guided generation, diffusion models are often trained with the textual embedding c. Throughout this paper, we will often omit c from ϵθpxt*, t, c*q if it does not lead to notational ambiguity.

**Video Diffusion Models.** Video diffusion models [11, 13, 45] further attempt to model the video data distribution. Specifically, Let $(\mathbf{v}^{n})_{n\in\{1,\ldots,N\}}$ represents the $N$-frame input video sequence. Then, for a given $n$-th frame $\mathbf{v}^{n}\in\mathbb{R}^{d}$, let $\mathbf{v}^{1:N}\in\mathbb{R}^{N\times d}$ represents a whole video vector. Let $\mathbf{v}_{t}^{n}=\sqrt{\alpha}_{t}\mathbf{v}^{n}+\sqrt{1-\alpha_{t}}\mathbf{e}_{t}^{n}$ represents the $n$-th noisy frame latent sampled from $p_{t}(\mathbf{v}_{t}^{n}|\mathbf{v}^{n})$, where $\mathbf{e}_{t}^{1:N}\sim\mathcal{N}(0,I)$. We similarly define $(\mathbf{v}_{t}^{n})_{n\in\{1,\ldots,N\}}$, $\mathbf{v}_{t}^{1:N}$, and $\mathbf{e}^{1:N}$. The goal of video diffusion model training is then to obtain a residual denoiser $\mathbf{e}_{\theta}$ with textual condition $c$ and video input that satisfies:

$$\min_{\mathbf{v}_{t}^{0}}\mathbb{E}_{\mathbf{v}_{t}^{1:N},\mathbf{v}_{t}^{1:N},c}\big{[}\left\|\mathbf{e}_{\theta}(\mathbf{v}_{t}^{1:N},t,c)-\mathbf{e}^{1:N}\right\|\big{]},\tag{6}$$

where $\mathbf{e}_{\theta}(\mathbf{v}_{t}^{1:N},t,c),\mathbf{e}^{1:N}\in\mathbb{R}^{N\times d}$. In this work, we denote the predicted noise of $n$-th frame as $\mathbf{e}_{\theta}^{n}(\mathbf{v}_{t}^{1:N},t,c)\in\mathbb{R}^{d}$.

## 2.2 Fourier And Wavelet Analysis

Spectral analysis techniques transform time-domain or pixel-domain signals (such as video frames) into the frequency domain, revealing the frequency components and their intensities. This transformation is valuable in video understanding as it helps in identifying repetitive motion patterns and underlying structures that may not be visible in the time or pixel domain.

Fourier Transform. Let vn P RHˆW represents the n-th 2D video frame. Then, its frequency spectrum at coordinate p*a, b*q is given as follows:

H ` by W q, (7) Fvnp*a, b*q " x"0 y"0 vnpx, yqe´i2πp ax H´1 ÿ W ´1 ÿ
where vnp*x, y*q means the pixel value at coordinate p*x, y*q. The output frequency spectrum is represented as Fvnp*a, b*q " Rpa, bq`Ip*a, b*qi, where Rpa, bq, Ip*a, b*q P R
represents real and imaginary part, respectively. Then, the amplitude and phase is derived as follows:

Rp*a, b*q Rpa, bq2 ` Ipa, bq2, =Fvnp*a, b*q " arctan ´ Ip*a, b*q ¯ . (8) |Fvnp*a, b*q| " a
Here, amplitude often indicates the existence of corresponding spatial frequencies within the image, often characterized by edges, textures, patterns, etc. Phase often encodes the structural spatial relationship.

Wavelet Transform. We first provide a brief introduction to the frame theory.

Frames in signal processing are an extension of basis sets but with a relaxation that allows for redundancy. Let Ψ " rψ1 *. . . ψ*ms P Rnˆm, where tψkum k"1 is a set of functions in a Hilbert space H. Then, tψkum k"1 is called as a frame if it satisfies the following inequality:

α}f}2 ď }xf, Ψy}2 ď β}f}2, @f P H (9)
where ck :" x*f, ψ*ky is a k-th frame expansion coefficient, and *α, β* are frame bounds. The original signal f can be exactly reconstructed from expansion coefficients using the dual frame operator ˜Ψ which satisfies the so-called frame condition: ˜ΨΨ T " I.

Wavelet frames, renowned for capturing multi-resolution scale features, are among the most prevalently utilized frame representations in signal processing.

Let ψptq represent a mother wavelet that can be shifted and scaled. For a function vptq P L2pRq, the wavelet transform can be expressed as:

a CWvp*a, b*q " 1 ?α ˙ dt " xvptq, ψa,bptqy, (10) ż vptqψ˚ ˆt ´ b
which serves as an expansion coefficient. In the case of discrete wavelet transform (DWT), it uses a finite set of wavelet and scaling functions derived from a chosen wavelet family. Specifically, the mother wavelet is shifted and scaled by powers of two as follows:

ψj,kptq " 1 ? 2j ψp2´jt ´ kq. (11)
Park & Jeong et al.

Then, the DWT of a signal vrns is given by:

$${\cal W}_{\mathbf{v}}(j,k)=\langle\mathbf{v}(t),\psi_{j,k}(t)\rangle.\tag{12}$$
Then, the original signal can be recovered from inverse DWT. In practice, this discrete wavelet transform can be implemented by convolution using an appropriate choice of filter bank.

## 3 Spectral Motion Alignment

Given an input video, our main goal is to develop a novel frequency-domain motion alignment framework that (a) distills the motion patterns M ˚ of input video, and (b) transfers the motion patterns M ˚ to output video within varied contexts, e.g. Cars with motion M ˚ Ñ Tanks with motion M ˚.

Conventional motion distillation methods mostly rely on pixel-domain motion distillation objectives. However, frequency-domain analysis can further capture underlying motion patterns across a spectrum of frequency levels that mainly constitute motion. Accordingly, we propose Spectral Motion Alignment
(SMA), a novel Fourier and wavelet-transform-based motion vector refinement and alignment framework. More details follow.

## 3.1 Denoised Motion Vector Estimation

To distill the motion information, we first estimate the motion vector of the input video following [16]. The intuition is that residual vectors between consecutive frames may include information about the motion trajectories. Define the n-th frame residual vector, namely motion vector at time t ě 0 as

$$\delta\mathbf{v}_{t}^{n}:=\mathbf{v}_{t}^{n+1}-\mathbf{v}_{t}^{n},\tag{13}$$

where the epsilon residual vector $\delta\mathbf{e}_{t}^{n}$ is similarly defined. This $\delta\mathbf{v}_{t}^{n}$ can be acquired through the following diffusion kernel [16]:

$$p(\delta\mathbf{v}_{t}^{n}\mid\delta\mathbf{v}_{0}^{n})=\mathcal{N}(\delta\mathbf{v}_{t}^{n}\mid\sqrt{\bar{\alpha}_{t}}\delta\mathbf{v}_{0}^{n},2(1-\bar{\alpha}_{t})I).\tag{14}$$
Moreover, [16] shows that the ground-truth motion vector in pixel space δvn
0 can be derived as follows:

$$\delta\mathbf{v}_{0}^{n}=\frac{1}{\sqrt{\bar{\alpha}_{t}}}\left(\delta\mathbf{v}_{t}^{n}-\sqrt{1-\bar{\alpha}_{t}}\delta\mathbf{\epsilon}_{t}^{n}\right).\tag{15}$$
Similarly, one can obtain the denoised motion vector estimate δˆvn
0 by using Tweedie's formula as follows:

$$\hat{\mathbf{v}}_{0}^{1:N}(t):=\frac{1}{\sqrt{\hat{\alpha}_{t}}}\big{(}\mathbf{v}_{t}^{1:N}-\sqrt{1-\hat{\alpha}_{t}}\mathbf{\epsilon}_{\theta}(\mathbf{v}_{t}^{1:N},t)\big{)},\tag{16}$$

where $\hat{\mathbf{v}}_{0}^{1:N}(t)$ is an empirical Bayes optimal posterior expectation $\mathbb{E}[\mathbf{v}_{0}^{1:N}\,|\,\mathbf{v}_{t}^{1:N}]$.

 In the context of motion transfer, the authors in [16] finetune the temporal attention layers of VDM by aligning each motion vector $\delta\mathbf{v}_{0}^{n}$ and its denoised estimate $\delta\hat{\mathbf{v}}_{0}^{n}(t)$:

$$\min_{\delta}\mathbb{E}_{t,n,\mathbf{e}^{t,n},\mathbf{e}^{t,n+1}}\Big{[}\ell_{\text{align}}\big{(}\delta\mathbf{v}_{0}^{n},\delta\hat{\mathbf{v}}_{0}^{n}(t)\big{)}\Big{]}.\tag{17}$$

While these advancements in motion distillation mark significant progress, Figure 1, 4 and 6 indicate that [16] still has potential for further refinement.

## 3.2 Spectral Global Motion Alignment

One of the primary limitations in (17) is that it may not fully encapsulate the global motion dynamics. This is partly because [16] employs 'frame-wise' matching losses, such as ℓ2-distance. While this is effective, it may overlook the comprehensive motion dynamics by focusing solely on pairwise frame comparisons.

To mitigate these problems, we explore the use of wavelet transforms in motion distillation. In this paper, we use Haar wavelet, whose low and high pass filters are given as follows:

$$L[n]=\frac{1}{\sqrt{2}}[1\ 1],H[n]=\frac{1}{\sqrt{2}}[-1\ 1],\tag{18}$$

which is implemented using the multi-scale Haar filter bank. Then, given the
sequence of motion vectors δv0 " pδvn
                                    0qnPt1,...,N´1u and its denoised estimates
δˆv0ptq "
         `
          δˆvn
            0ptq
                ˘

                nPt1,...,N´1u, we consider (N ´ 1)-length time-dependent 1D
arrays from arbitrary spatial pixel dimension s P t1, . . . du. The corresponding
1D array of motion vector is denoted by δv0,s and δˆv0,sptq P RN´1 (Figure 2).
   Then, the frequency-matching loss between δv0 and δˆv0ptq is defined with
DWT in (12) as follows:

$$\ell_{\text{global}}(\delta\mathbf{v}_{0},\delta\hat{\mathbf{v}}_{0}(t))=\mathbb{E}_{t,s,j,k}\Big{[}\|\mathcal{W}_{\delta\mathbf{v}_{0,s}}(j,k)-\mathcal{W}_{\delta\hat{\mathbf{v}}_{0,s}(t)}(j,k)\|_{1}\Big{]}.\tag{19}$$

Considering that the wavelet transform allows multi-resolution analysis of motion vectors, it enables us to handle motions at various scales and frequencies effectively. This could be particularly beneficial for complex scenes with varying motion speeds and types, ensuring that subtle motions are captured and transferred more accurately.

## 3.3 Spectral Local Motion Refinement

Another problem in (17) is that the residuals between consecutive frames, while rich in motion information, may also encapsulate high-frequency local distortions, background noise, and other non-motion-related artifacts. Accordingly, we focus on particularly prioritizing low-to-moderate spatial frequency components. Specifically, following the amplitude and phase spectrum definition in (8), we define amplitude and phase matching loss as follows:

$$\ell_{1ocal}^{A}(\delta\mathbf{v}_{0}^{n},\delta\hat{\mathbf{v}}_{0}^{n}(t))=\mathbb{E}_{t,n,a,b}\bigg{[}\omega(a,b)\|\mathcal{F}_{\delta\mathbf{v}_{0}^{n}}(a,b)|-|\mathcal{F}_{\delta\mathbf{v}_{0}^{n}}(a,b)|\|_{1}\bigg{]},\tag{20}$$ $$\ell_{local}^{P}(\delta\mathbf{v}_{0}^{n},\delta\hat{\mathbf{v}}_{0}^{n}(t))=\mathbb{E}_{t,n,a,b}\bigg{[}\omega(a,b)|\mathcal{L}\mathcal{F}_{\delta\mathbf{v}_{0}^{n}}(a,b)-\mathcal{L}\mathcal{F}_{\delta\mathbf{v}_{0}^{n}}(a)(a,b)|\|_{1}\bigg{]},$$

where the frequency domain weighting $\omega(a,b)$ is defined as

$$\omega(a,b)=\bigg{[}\big{(}\frac{H}{2}\big{)}^{2}+\big{(}\frac{W}{2}\big{)}^{2}\bigg{]}^{\delta}-\bigg{[}\big{(}a-\frac{H}{2}\big{)}^{2}+\big{(}b-\frac{W}{2}\big{)}^{2}\bigg{]}^{\delta}+1\tag{21}$$

for $0<a<H,0<b<W$, and otherwise, set to zero. This introduces a weighting [40] that prioritizes low-frequency components for $\delta>0$.

## 3.4 Inference Pipeline

To sum up, the overall spectral motion alignment framework is given as follows:

$$\min_{\theta}\mathbb{E}_{t,n,\epsilon_{1}^{n},\epsilon_{1}^{n+1}}\Big{[}\ell_{\text{align}}\big{(}\delta\mathbf{v}_{0}^{n},\delta\mathbf{\hat{v}}_{0}^{n}(t)\big{)}+\lambda_{g}\ell_{\text{global}}\big{(}\delta\mathbf{v}_{0},\delta\mathbf{\hat{v}}_{0}(t)\big{)}+\lambda_{l}\ell_{\text{local}}\big{(}\delta\mathbf{v}_{0}^{n},\delta\mathbf{\hat{v}}_{0}^{n}(t)\big{)}\Big{]},\tag{22}$$

where $\ell_{\text{local}}(\delta\mathbf{v}_{0}^{n},\delta\mathbf{\hat{v}}_{0}^{n}(t))=\ell_{\text{local}}^{1}(\delta\mathbf{v}_{0}^{n},\delta\mathbf{\hat{v}}_{0}^{n}(t))+\ell_{\text{local}}^{p}(\delta\mathbf{v}_{0}^{n},\delta\mathbf{\hat{v}}_{0}^{n}(t))$. Upon optimization, inference is performed using new text prompts to transform appearances, e.g. "a secagull is walking" $\rightarrow$ "a chicken is walking".

This Spectral Motion Alignment (SMA) is universally adaptable across various motion distillation frameworks. While diverse diffusion-based motion distillation frameworks adopt their pixel-domain motion learning objectives, the proposed frequency-domain alignment seamlessly integrates with these arbitrary objectives. Moreover, different motion distillation frameworks target specific parameters θ for fine-tuning, varying from temporal attention layers [16] to dualpath LoRAs [49]. We empirically demonstrate global compatibility of the proposed spectral motion alignment with diverse neural architectures and parameterizations. Pseudo-code is provided in the appendix.

## 4 Experiments Using T2V Diffusion Models 4.1 Experimental Setting

To assess the capability of Spectral Motion Alignment (SMA) to capture accurate motion within contemporary diffusion-based motion learning frameworks, we curated a dataset comprising 30 text-video pairs sourced from the publicly available DAVIS [24] and WebVid-10M [2] collections. This dataset is deliberately designed to cover a broad spectrum of motion types and subjects, with video lengths ranging between 8 and 16 frames. For this study, we leverage two foundational text-to-video diffusion models: Zeroscope [33], a non-cascaded VDM, and Show-1 [45], a cascaded VDM. More details are provided in appendix.

## 4.2 Baselines

MotionDirector. MotionDirector [49] pioneered the concept of motion customization within video diffusion literature. To distinctively tailor the appearance and motion of a video, [49] developed a unique dual-path framework employing Low-Rank Adaptation (LoRA, [14]). Within this architecture, spatial LoRAs are optimized using the diffusion training loss on a single, randomly chosen frame, rather than on the full video sequence. Conversely, temporal LoRAs are trained by considering all frames of the video, using an anchor frame based appearance-debiased temporal loss.

VMC. VMC [16] achieves state-of-the-art performance in motion customization through their novel epsilon residual matching objective, facilitating efficient motion distillation within cascaded video diffusion framework. In their work, they showcased the efficient of motion distillation within cascaded video diffusion models, by optimizing only keyframe generation model while freezing later modules. As VMC represents the most closely related work to ours, we conduct a two-fold validation within this baseline, including both *cascaded* and non-cascaded video diffusion scenarios.

Qualitative Comparison. Fig. 3 offers a qualitative analysis comparing MotionDirector's performance with and without the implementation of SMA. Likewise, Fig. 4 examines VMC's performance with and without SMA implementation. Specifically, videos produced using a cascaded diffusion pipeline are displayed in Fig. 4-top, whereas those generated through a non-cascaded diffusion model are shown in the bottom. Videos generated without SMA correctly capture the appearance as dictated by the target text, but fail to accurately mirror the original video's motion patterns. In contrast, SMA significantly enhances motion understanding, precisely distinguishing between dynamic and static elements in the scene. For instance, in the last example of Fig. 3, MotionDirector with SMA produces a video where only the eagle moves from right to left, whereas without SMA, the video inaccurately depicts the ground moving alongside the eagle.

Quantitative Comparison. The results of our quantitative evaluation are presented in Table 1. We employ CLIP encoders [26] for automated evaluation. To evaluate text-video alignment [10], we measure the average cosine similarity between the target text prompt and the frames generated. Regarding frame consistency, we extract CLIP image features for each frame in the output video and subsequently calculate the average cosine similarity among all frame pairs in the video. For human evaluation, we conduct a user study with 42 participants to assess three key aspects, guided by the following questions: (1) Editing Accuracy: *Is the output video accurately edited, reflecting the target text?* (2) Temporal Consistency: Is the transition between frames smooth and consistent? (3) Motion Accuracy: Is the motion of the input video accurately preserved in the output video? Tab. 1 demonstrates that SMA enhances the performance of MotionDirector and VMC across all measured metrics.

| Automatic Metrics       | User Study                                       |
|-------------------------|--------------------------------------------------|
| Method                  | Text-Align Temp-Con Edit-Acc Temp-Con Motion-Acc |
| MotionDirector          | 0.7550                                           |
| MotionDirector w/ Ours  |                                                  |
| 0.8081                  | 0.9784                                           |
| VMC (Show-1)            | 0.8066                                           |
| VMC (Show-1) w/ Ours    |                                                  |
| 0.8193                  | 0.9776                                           |
| VMC (Zeroscope)         | 0.8223                                           |
| VMC (Zeroscope) w/ Ours |                                                  |
| 0.8425                  | 0.9578                                           |

## 5 Experiments Using T2I Video Diffusion Models 5.1 Experimental Setting

To assess the effectiveness of SMA within methodologies built on text-to-image diffusion model, we use the same text-video pairs previously assembled in Sec. 4.1. The resolution for all produced videos is standardized to 512x512. In this experiment, Stable Diffusion v1-5 [28] and ControlNet-Depth [46] are utilized.

## 5.2 Baselines

Tune-A-Video. Tune-A-Video [38] was at the forefront of image-diffusionbased video editing at a time when video diffusion models were not yet publicly accessible. It begins with transforming a pretrained T2I diffusion model to psuedo T2V model by adding temporal attention layers and expanding spatial self-attention into spatio-temporal attention. Attention projection layers within this pseudo T2V model are then fine-tuned on a specific input video, utilizing the diffusion training objective (Eq. 2).

ControlVideo. ControlVideo [48] is another one-shot-based video editing method, starting from pretrained T2I model. ControlVideo extends ControlNet [46] from image to video to incorporate structural cues obtained from the input video. Subsequently, akin to Tune-A-Video [38], attention projection layers of the backbone U-Net and ControlNet are customized on the input video.

## 5.3 Qualitative Comparison.

Fig. 5-(top) demonstrates the qualitative benefits of incorporating SMA into the Tune-A-Video method. Without SMA, Tune-A-Video often experiences flickering in foreground objects, a problem that SMA significantly reduces. Fig. 5-(*bottom*)
illustrates the qualitative improvements brought by integrating SMA with the ControlVideo framework. In ControlVideo, depth control aids in maintaining the structural integrity from the input videos to the output videos. However, it's observed that structural integrity alone doesn't ensure motion accuracy, and SMA plays a crucial role in accurately capturing motion details.

| Automatic Metrics    | User Study                                       |
|----------------------|--------------------------------------------------|
| Method               | Text-Align Temp-Con Edit-Acc Temp-Con Motion-Acc |
| Tune-A-Video         | 0.8289                                           |
| Tune-A-Video w/ Ours |                                                  |
| 0.8633               | 0.9568                                           |
| ControlVideo         | 0.8686                                           |
| ControlVideo w/ Ours |                                                  |
| 0.8781               | 0.9590                                           |

## 5.4 Quantitative Comparison.

Quantitative results are detailed in Tab. 2, following the metrics introduced in Sec. 4.2. Across both the Tune-A-Video and ControlVideo frameworks, the integration of SMA results in enhanced performance across all five evaluated metrics, notably achieving a substantial advantage in motion accuracy.

## 6 Discussion

We explore the impact of motion vector refinement by examining motion vectors
(δv0, δˆv0ptq) and their (amplitude, phase) spectrum in Figure 6 (t " 700). Figure
6b indicates that the original motion vector δv0 filters out appearance (e.g. background, color, etc) to some extent. However, it still faces frame-wise distortions or inconsistencies. For instance, in a specific example of this skateboarding man, non-motion-related artifacts, e.g. stair and fence patterns, background texture, etc., persist as distortions. These are characterized as high-frequency noises in the amplitude spectrum, Fig. 6a. Conversely, δˆvn
0ptq shows a reduction in highfrequency distortions while preserving essential motion information. As shown in (14), δvn t can be acquired from δvn
0 through the diffusion kernel. In this forward process, high-frequency components are perturbed more rapidly [20]. Consequently, the core motion information is consistently preserved in δvn t from coarse (t Ò) to fine (t Ó) level. Motivated by these insights, we prioritize low spatial frequency components during motion distillation to avoid overfitting to non-motion-related high-frequency distortions.

This motion vector refinement improves the overall fidelity as shown in Figure
6c. The application of VMC for motion transfer, without refinement, often fails to maintain motion patterns, introducing repetitive fence-like background distortions. Conversely, motion refinement within the frequency domain significantly improves fidelity and background detail. Moreover, global motion alignment further improves motion transfer. Specifically, while local motion alignment is generally effective, it occasionally generates "reversed" motions, i.e. an astronaut skateboarding in an upward direction. Note that this example is particularly challenging as it shows very subtle positional changes (video in project page). This highlights the limitations of conventional frameworks in identifying accurate motion from a single motion vector frame δvn
0, Figure 6b. In contrast, the proposed global motion alignment effectively mitigates these challenges, ensuring accurate learning of motion patterns. Fig. 7 further demonstrates the effectiveness of global motion alignment. Thus, our approach harmonizes both local and global motion alignment and effectively distills motion patterns while robustly reducing high-frequency distortions.

## 7 Conclusion

In this paper, we propose Spectral Motion Alignment (SMA), a novel frequencybased distillation framework for motion transfer. We explore the limitations of conventional motion estimation methods: (a) lack of global motion understanding, (b) vulnerability to spatial artifacts. By utilizing Fourier and wavelet transforms, SMA captures comprehensive motion dynamics, highlighting the significance of global motion context. We proved SMA's effectiveness and compatibility through extensive validation across different motion transfer scenarios.

Reproducibility & Ethics Statement. For reproducibility, the code and datasets will be released to the public through the project page. Video generative models may pose potential risks for misuse in creating harmful content, which necessitates political regulation.

## References

1. Bai, J., He, T., Wang, Y., Guo, J., Hu, H., Liu, Z., Bian, J.: Uniedit: A unified
tuning-free framework for video motion and appearance editing. arXiv preprint arXiv:2402.13185 (2024)
2. Bain, M., Nagrani, A., Varol, G., Zisserman, A.: Frozen in time: A joint video
and image encoder for end-to-end retrieval. In: IEEE International Conference on Computer Vision (2021)
3. Bar-Tal, O., Chefer, H., Tov, O., Herrmann, C., Paiss, R., Zada, S., Ephrat, A.,
Hur, J., Li, Y., Michaeli, T., et al.: Lumiere: A space-time diffusion model for video generation. arXiv preprint arXiv:2401.12945 (2024)
4. Blattmann, A., Rombach, R., Ling, H., Dockhorn, T., Kim, S.W., Fidler, S., Kreis,
K.: Align your latents: High-resolution video synthesis with latent diffusion models. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 22563–22575 (2023)
5. Ceylan, D., Huang, C.H.P., Mitra, N.J.: Pix2video: Video editing using image
diffusion. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 23206–23217 (2023)
6. Chen, H., Xia, M., He, Y., Zhang, Y., Cun, X., Yang, S., Xing, J., Liu, Y., Chen,
Q., Wang, X., et al.: Videocrafter1: Open diffusion models for high-quality video generation. arXiv preprint arXiv:2310.19512 (2023)
7. Chen, W., Wu, J., Xie, P., Wu, H., Li, J., Xia, X., Xiao, X., Lin, L.: Control-avideo: Controllable text-to-video generation with diffusion models. arXiv preprint arXiv:2305.13840 (2023)
8. Efron, B.: Tweedie's formula and selection bias. Journal of the American Statistical
Association **106**(496), 1602–1614 (2011)
9. Girdhar, R., Singh, M., Brown, A., Duval, Q., Azadi, S., Rambhatla, S.S., Shah,
A., Yin, X., Parikh, D., Misra, I.: Emu video: Factorizing text-to-video generation by explicit image conditioning. arXiv preprint arXiv:2311.10709 (2023)
10. Hessel, J., Holtzman, A., Forbes, M., Bras, R.L., Choi, Y.: Clipscore: A referencefree evaluation metric for image captioning. arXiv preprint arXiv:2104.08718 (2021)
11. Ho, J., Chan, W., Saharia, C., Whang, J., Gao, R., Gritsenko, A., Kingma, D.P.,
Poole, B., Norouzi, M., Fleet, D.J., et al.: Imagen video: High definition video generation with diffusion models. arXiv preprint arXiv:2210.02303 (2022)
12. Ho, J., Jain, A., Abbeel, P.: Denoising diffusion probabilistic models. Advances in
neural information processing systems 33, 6840–6851 (2020)
13. Ho, J., Salimans, T., Gritsenko, A., Chan, W., Norouzi, M., Fleet, D.J.: Video
diffusion models. arXiv:2204.03458 (2022)
14. Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L.,
Chen, W.: Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685 (2021)
15. Hu, Z., Xu, D.: Videocontrolnet: A motion-guided video-to-video translation framework by using diffusion model with controlnet. arXiv preprint arXiv:2307.14073 (2023)
16. Jeong, H., Park, G.Y., Ye, J.C.: Vmc: Video motion customization using
temporal attention adaption for text-to-video diffusion models. arXiv preprint arXiv:2312.00845 (2023)
17. Jeong, H., Ye, J.C.: Ground-a-video: Zero-shot grounded video editing using textto-image diffusion models. arXiv preprint arXiv:2310.01107 (2023)

## Park & Jeong Et Al.

18. Khachatryan, L., Movsisyan, A., Tadevosyan, V., Henschel, R., Wang, Z.,
Navasardyan, S., Shi, H.: Text2video-zero: Text-to-image diffusion models are zeroshot video generators. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 15954–15964 (2023)
19. Kim, K., Lee, H., Park, J., Kim, S., Lee, K., Kim, S., Yoo, J.: Hybrid video
diffusion models with 2d triplane and 3d wavelet representation. arXiv preprint arXiv:2402.13729 (2024)
20. Kingma, D., Gao, R.: Understanding diffusion objectives as the elbo with simple
data augmentation. Advances in Neural Information Processing Systems 36 (2024)
21. Li, Y., Liu, H., Wu, Q., Mu, F., Yang, J., Gao, J., Li, C., Lee, Y.J.: Gligen: Open-set
grounded text-to-image generation. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 22511–22521 (2023)
22. Liu, Y., Zhang, K., Li, Y., Yan, Z., Gao, C., Chen, R., Yuan, Z., Huang, Y., Sun,
H., Gao, J., et al.: Sora: A review on background, technology, limitations, and opportunities of large vision models. arXiv preprint arXiv:2402.17177 (2024)
23. Magarey, J., Kingsbury, N.: Motion estimation using a complex-valued wavelet
transform. IEEE Transactions on Signal Processing 46(4), 1069–1084 (1998)
24. Pont-Tuset, J., Perazzi, F., Caelles, S., Arbeláez, P., Sorkine-Hornung, A.,
Van Gool, L.: The 2017 davis challenge on video object segmentation. arXiv preprint arXiv:1704.00675 (2017)
25. Qi, C., Cun, X., Zhang, Y., Lei, C., Wang, X., Shan, Y., Chen, Q.: Fatezero: Fusing
attentions for zero-shot text-based video editing. arXiv preprint arXiv:2303.09535 (2023)
26. Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G.,
Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual models from natural language supervision. In: International conference on machine learning. pp. 8748–8763. PMLR (2021)
27. Ren, Y., Zhou, Y., Yang, J., Shi, J., Liu, D., Liu, F., Kwon, M., Shrivastava,
A.: Customize-a-video: One-shot motion customization of text-to-video diffusion models. arXiv preprint arXiv:2402.14780 (2024)
28. Rombach, R., Blattmann, A., Lorenz, D., Esser, P., Ommer, B.: High-resolution
image synthesis with latent diffusion models. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. pp. 10684–10695 (2022)
29. Secker, A., Taubman, D.: Highly scalable video compression using a lifting-based
3d wavelet transform with deformable mesh motion compensation. In: Proceedings. International Conference on Image Processing. vol. 3, pp. 749–752. IEEE (2002)
30. Singer, U., Polyak, A., Hayes, T., Yin, X., An, J., Zhang, S., Hu, Q., Yang, H.,
Ashual, O., Gafni, O., et al.: Make-a-video: Text-to-video generation without textvideo data. arXiv preprint arXiv:2209.14792 (2022)
31. Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S.: Deep unsupervised learning using nonequilibrium thermodynamics. In: International conference on machine learning. pp. 2256–2265. PMLR (2015)
32. Song, J., Meng, C., Ermon, S.: Denoising diffusion implicit models. arXiv preprint
arXiv:2010.02502 (2020)
33. Sterling, S.: Zeroscope (2023), https://huggingface.co/cerspense/zeroscope_
v2_576w
34. Wang, J., Yuan, H., Chen, D., Zhang, Y., Wang, X., Zhang, S.: Modelscope textto-video technical report. arXiv preprint arXiv:2308.06571 (2023)
35. Wang, Y., Chen, X., Ma, X., Zhou, S., Huang, Z., Wang, Y., Yang, C., He, Y.,
Yu, J., Yang, P., et al.: Lavie: High-quality video generation with cascaded latent diffusion models. arXiv preprint arXiv:2309.15103 (2023)
36. Wei, Y., Zhang, S., Qing, Z., Yuan, H., Liu, Z., Liu, Y., Zhang, Y., Zhou, J.,
Shan, H.: Dreamvideo: Composing your dream videos with customized subject and motion. arXiv preprint arXiv:2312.04433 (2023)
37. Williams, C., Falck, F., Deligiannidis, G., Holmes, C.C., Doucet, A., Syed, S.: A
unified framework for u-net design and analysis. Advances in Neural Information
Processing Systems 36 (2024)
38. Wu, J.Z., Ge, Y., Wang, X., Lei, S.W., Gu, Y., Shi, Y., Hsu, W., Shan, Y., Qie,
X., Shou, M.Z.: Tune-a-video: One-shot tuning of image diffusion models for textto-video generation. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 7623–7633 (2023)
39. Wu, R., Chen, L., Yang, T., Guo, C., Li, C., Zhang, X.: Lamp: Learn a motion pattern for few-shot-based video generation. arXiv preprint arXiv:2310.10769 (2023)
40. Yang, G., Liu, W., Liu, X., Gu, X., Cao, J., Li, J.: Delving into the frequency:
Temporally consistent human motion transfer in the fourier space. In: Proceedings of the 30th ACM International Conference on Multimedia. pp. 1156–1166 (2022)
41. Yang, S., Hou, L., Huang, H., Ma, C., Wan, P., Zhang, D., Chen, X., Liao, J.:
Direct-a-video: Customized video generation with user-directed camera movement and object motion. arXiv preprint arXiv:2402.03162 (2024)
42. Yatim, D., Fridman, R., Tal, O.B., Kasten, Y., Dekel, T.: Space-time diffusion
features for zero-shot text-driven motion transfer. arXiv preprint arXiv:2311.17009 (2023)
43. Ye, J.C., Han, Y., Cha, E.: Deep convolutional framelets: A general deep learning
framework for inverse problems. SIAM Journal on Imaging Sciences 11(2), 991–
1048 (2018)
44. Yoo, J., Uh, Y., Chun, S., Kang, B., Ha, J.W.: Photorealistic style transfer via
wavelet transforms. In: Proceedings of the IEEE/CVF international conference on computer vision. pp. 9036–9045 (2019)
45. Zhang, D.J., Wu, J.Z., Liu, J.W., Zhao, R., Ran, L., Gu, Y., Gao, D., Shou, M.Z.:
Show-1: Marrying pixel and latent diffusion models for text-to-video generation. arXiv preprint arXiv:2309.15818 (2023)
46. Zhang, L., Rao, A., Agrawala, M.: Adding conditional control to text-to-image
diffusion models. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 3836–3847 (2023)
47. Zhang,
Y.,
Wei,
Y.,
Jiang,
D.,
Zhang,
X.,
Zuo,
W.,
Tian,
Q.:
Controlvideo: Training-free controllable text-to-video generation. arXiv preprint
arXiv:2305.13077 (2023)
48. Zhao, M., Wang, R., Bao, F., Li, C., Zhu, J.: Controlvideo: Adding conditional
control for one shot text-to-video editing. arXiv preprint arXiv:2305.17098 (2023)
49. Zhao, R., Gu, Y., Wu, J.Z., Zhang, D.J., Liu, J., Wu, W., Keppo, J., Shou, M.Z.:
Motiondirector: Motion customization of text-to-video diffusion models. arXiv preprint arXiv:2310.08465 (2023)

## A Pseudo Training Algorithm

In our work, we adopt the notation and expressions mostly from [16] for the preliminaries section and pseudo-code, due to its relevance to our focus on denoised motion vector estimates. We interchangeably use ˆv1:N
0
ptq and ˆv0ptq in the main paper and Algorithm 1. While Algorithm 1 generalizes parameter θ, each video diffusion model incorporates specific parameters such as θTA [16] and θLoRA [49].

## Algorithm 1 Spectral Motion Alignment (Sma)

1: **Input:** N-frame input video sequence pvn
0 qnPt1*,...,N*u, training prompt P, textual
encoder ψ, Training iterations M, Video diffusion models parameterized by θ.
2: **Output:** Fine-tuned video diffusion models θ˚.
3:
4: **for** *step* " 1 to M do
5:
Sample timestep t P r0, Ts and Gaussian noise ϵ1:N
t
, where ϵn
t P Rd " Np0, Iq
6:
Prepare text embeddings c " ψpPq
7: 8:
1. Denoised motion vector estimation
9:
v1:N
t
" ?¯αtv1:N
0
` ?1 ´ ¯αtϵ1:N
t
.
10:
ˆv1:N
0
ptq "
1
?¯αt
`
v1:N
t
´ ?1 ´ ¯αtϵθpv1:N
t
, t, cq
˘
.
11: 12:
2. Global motion alignment
13:
Conduct 1D DWT for each s-th pixel in δv0, δˆv0ptq with Haar wavelet.
14:
ℓglobalpδv0, δˆv0ptqq " Et,s,j,k
"
}Wδv0,sp*j, k*q ´ Wδˆv0,sptqp*j, k*q}1
ı
.
15: 16:
3. Local motion refinement
17:
Obtain amplitude and phase spectrum for δvn
0 as |Fδvn
0 pa, bq|, =Fδvn
0 p*a, b*q.

18:
       ℓa
        localpδvn
                0 , δˆvn
                     0 ptqq " Et,n,a,b
                                    "
                                     Wpa, bq ˚ }|Fδvn
                                                    0 pa, bq| ´ |Fδˆvn
                                                                   0 ptqpa, bq|}1
                                                                              ı
                                                                               .

19:
       ℓp
        localpδvn
                0 , δˆvn
                     0 ptqq " Et,n,a,b
                                    "
                                     Wpa, bq ˚ }=Fδvn
                                                     0 pa, bq ´ =Fδˆvn
                                                                    0 ptqpa, bq}1
                                                                               ı
                                                                                .

20: 21:
4. Overall optimization

22:
       θ˚ " arg minθ Et,n,ϵn
                           t ,ϵn`1
                              t

23: end for

"
ℓSMApδv0, δˆv0ptq
                 ˘ı
                   (ℓSMA: objective in eq(22)).

## B Related Work B.1 Diffusion-Based Video Editing

There has been considerable progress in adapting the achievements of diffusionbased image editing for video generative tasks. Compared to text-conditioned image generation, creating videos based solely on text introduces the complex challenge of producing temporally consistent and natural motion. In the absence of publicly available text-to-video diffusion models, Tune-A-Video [38] was at the forefront of one-shot based video editing. It proposes to inflate image diffusion model to pseudo video diffusion model by appending temporal modules to image diffusion model [28] and reprogramming spatial self-attention to spatio-temporal self-attention. Following this adaptation, the attention modules' query projection matrices are fine-tuned on the input video. To eliminate the need for customizing model weights for every new video, various zero-shot editing methods have been developed. One approach involves guiding the generation process with attention maps, such as the injection of self-attention maps obtained from previous frames [5] or input video [25]. Another prevalent method integrates explicit structural cues, like depth or edge maps, into the reverse diffusion process. For instance, ControlNet [46] has been adapted for the video domain, facilitating the creation of structurally consistent frames in video generation [18] and translation tasks [15,47]. Furthermore, GLIGEN's [21] adaptation to the video domain by Ground- A-Video [17] demonstrates the use of both spatially-continuous depth map and spatially-discrete bounding box conditions, achieving multi-attribute editing of videos in a zero-shot manner.

The advent of open-source text-to-video diffusion models [6,33–35] has spurred research into separating, altering, and combining the appearance and motion elements of videos [1,16,27,36,41,42,49]. MotionDirector [49] and DreamVideo [36] have each suggested approaches for dividing fine-tuning processes into distinct learning phases for subject appearance and temporal motion, utilizing efficient fine-tuning methods. On the other hand, VMC [16] focuses on distilling the motion within a video by calculating the residual vectors between consecutive frames. In their work, they fine-tune temporal attention layers within cascaded video diffusion models to synchronize the ground-truth motion vector with the denoised motion vector estimate, successfully generating videos that replicate the motion pattern of an input video within diverse visual scenarios. Similarly, [42] introduces a space-time feature loss that constructs self-similarity matrices based on the differences in attention features between frames. This approach aims to minimize the discrepancy in self-similarity between the input and output videos.

## B.2 Frequency-Aware Visual Generation

Spectral analysis plays a pivotal role in the domain of visual understanding and generation, offering insights into the temporal-spatial structure of pixeldomain frames through frequency-domain signals. [23] introduced a hierarchical motion estimation algorithm employing complex discrete wavelet transforms, effectively utilizing phase differences among subbands to indicate local translations within video frames. [29] enhanced scalable video compression through motion-compensated wavelet transforms, integrating a continuous deformable mesh motion model to achieve superior compression efficiency and motion representation.

Furthermore, these spectral insights have been instrumental in refining algorithms and deepening architectural understanding, particularly within the contexts of U-Net and autoencoder frameworks. [43] provided a groundbreaking reinterpretation of deep learning architectures for image reconstruction, establishing a connection between deep learning and classical signal processing theories, including wavelets and compressed sensing. [44] developed a wavelet-based correction method, WCT2, to augment photorealism in style transfer, leveraging whitening and coloring transforms to preserve structural integrity and statistics within the VGG feature space.

In the realm of U-Net in diffusion models, [37] highlighted the rapid dominance of noise over high-frequency information in residual U-Net denoisers. Concurrently, [19] proposed the Hybrid Video Diffusion Model (HVDM), a novel architecture that captures spatiotemporal dependencies using a disentangled representation combining 2D projection and 3D convolutions with wavelet decomposition. While [19] aims to *reconstruct* input video with frequency matching loss, our approach does not aim to reconstruct input, focusing instead on learning motion dynamics through motion vectors, thereby distinguishing our method within the landscape of spectral analysis applications in motion estimation and transfer.

## C Experimental Details

For spectral global motion alignment, we mainly use Haar wavelets with the number of levels l " 3 for 8-frame videos and l " 4 for 16-frame videos. We use DWT1DForward function from the PyTorch package1. For spectral local motion refinement, we fix δ " 0.05 in frequency domain weighting ωp*a, b*q. We set λg "
0.4 and λl " 0.2 for many cases, where we recommend to fine-tune λg in a range of r0.2, 0.5s, and λg in a range of r0.1, 0.3s. We follow other configurations, e.g. optimization algorithm, learning rate, training steps, etc., from the original motion transfer frameworks.

## D Additional Results

This section provides additional qualitative comparisons of SMA across different baseline approaches. In Figure 8, we compare the efficacy of MotionDirector [49] in transferring motion, both with SMA integrated and without. Figures 9 and 10 delve into VMC's [16] capabilities in customizing motion, showcasing outcomes with SMA and without its application. Additionally, Figure 11 contrasts the ability of Tune-A-Video and ControlVideo [38] to replicate the original motion, examining the impact of incorporating SMA. All our qualitative results can be viewed on our project page in video format.