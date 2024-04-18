
## Deep Active Learning: A Reality Check

Edrina Gashi
Independent Researcher
Jiankang Deng
Huawei Noah's Ark
Ismail Elezi
Huawei Noah's Ark

## Abstract

We conduct a comprehensive evaluation of state-of-theart deep active learning methods. Surprisingly, under general settings, no single-model method decisively outperforms entropy-based active learning, and some even fall short of random sampling. We delve into overlooked aspects like starting budget, budget step, and pretraining's impact, revealing their significance in achieving superior results. Additionally, we extend our evaluation to other tasks, exploring the active learning effectiveness in combination with semi-supervised learning, and object detection. Our experiments provide valuable insights and concrete recommendations for future active learning studies. By uncovering the limitations of current methods and understanding the impact of different experimental settings, we aim to inspire more efficient training of deep learning models in real-world scenarios with limited annotation budgets. This work contributes to advancing active learning's efficacy in deep learning and empowers researchers to make informed decisions when applying active learning to their tasks.

## 1. Introduction

All animals samples are equal, but some are more equal than others. [35]
Deep Learning models have achieved a remarkable feat by attaining near-human accuracy in a multitude of tasks. This prowess is attributed to their ability to harness extensive datasets, enabling them to conquer challenges like image classification [15], object detection [37], and image segmentation [6]. These accomplishments primarily reside within the domain of supervised learning, where the models rely on vast repositories of labeled data such as ImageNet [40] or MS-COCO [28]. While sourcing image data might seem straightforward, the process of meticulously annotating them is a laborious, time-consuming, and error-prone task.

This challenge becomes even more pronounced in specialized fields like medical imaging, or forensics, where data annotation necessitates expert skills and can lead to significant errors.

Recent empirical investigations [19, 31] have unveiled an intriguing aspect of deep neural models' performance –
it is not yet saturated concerning the size of the training data. The adage "more data, more accuracy" holds true, but it comes at a cost. This realization has propelled researchers to explore a semi-supervised approach [32, 34], which seeks to strike a balance between labeled and unlabeled data. However, despite these efforts, the performance of semi-supervised learning models still lags behind their fully-supervised counterparts [36]. Regardless of whether a learning scenario is fully-supervised or semi-supervised, a universal constraint persists: the annotation budget is finite. Hence, the imperative to adopt an intelligent labeling strategy - often referred to as *active learning* - becomes evident. This approach involves selectively labeling the most informative samples, a technique that has been shown to significantly enhance the performance of both fully-supervised [2,46,52] and semi-supervised [11] models.

The landscape of research in this domain is marked by a surge of recent papers proposing novel methods, each vying to establish its state-of-the-art credentials. However, a common theme emerges - these proposed methods often carry certain shortcomings. Some employ testing sets for validation, others make methodological testing errors, and unfair comparisons are not uncommon. Though such issues are not unique to active learning, analogous subfields have witnessed the emergence of works aimed at rectifying these pitfalls. For instance, in metric learning, [33] conducted an exhaustive study of various cutting-edge algorithms, revealing that the latest methods only marginally outperform classical techniques like contrastive and triplet loss in most scenarios. This scrutiny has catalyzed more meticulous research and rigorous evaluations, thereby fostering advancements in the field.

The present study embarks on a comprehensive exploration of several renowned deep active learning methods. In the experimental design, we subject these methods to uniform conditions across multiple data splits and datasets, thereby ensuring a fair comparison. Intriguingly, our findings challenge the supremacy of claimed state-of-the-art techniques. Contrary to expectations, the results reveal that, in a general setting, none of the proposed methods decisively outperform active learning based on entropy. Furthermore, some of these methods fail to consistently surpass the performance of even random sampling. This research delves further by investigating overlooked parameters such as the starting budget, budget step, and the impact of pretraining on the methods' efficacy.

To comprehensively assess the landscape, we also examine the benefits of active learning in the semi-supervised learning setting, showing that a combining these two techniques leads to better results than either of them in isolation. We then extrapolate these findings to another pertinent task - object detection. We finish this study by offering valuable insights and recommendations for future active learning endeavors, drawing parallels with the evolution of research in related subfields.

Our **contribution** is the following:

- **Thorough Evaluation of Active Learning Methods**:
We conduct an exhaustive and unbiased assessment of various cutting-edge active learning techniques. The results unveil a significant insight: in a general context, no single-model approach can outperform the *entropy*-
based strategy.
- **Expanded Experimental Scope**: Our investigation
extends beyond the mainstream by examining the behaviors of active learning methods across varying starting budgets, budget step sizes, and their performance in conjunction with pre-trained models. This broader exploration offers a more comprehensive understanding of the methods' dynamics.
- **Other modalities**: We investigate the interplay between active learning and semi-supervised learning, shedding light on their synergistic potential. Furthermore, we extend our study to the realm of object detection, showcasing the applicability of the methods in different contexts.
- **Guidelines for Future Work**: Our research does not
conclude with results; we distill our findings into actionable recommendations. These insights provide a roadmap for upcoming research endeavors in the domain of active learning, aiding researchers in charting a more effective course of exploration.
In essence, our work significantly enriches the understanding of active learning's intricacies and its potential across various dimensions, ensuring that future advancements in this field are better informed and more impactful.

## 2. Related Work

Active learning (AL) has garnered extensive attention over the past two decades. It centers on selecting uncertain samples for classifier prediction or those where independent classifiers disagree. A comprehensive survey [42] aptly delves into this issue, particularly within the context of low-level data.

The survey covers a spectrum of active learning approaches, encompassing uncertainty-based [26, 27, 30, 38, 43], SVM-based [49, 51], and query-bycommittee methods [17,44].

Deep Active Learning (DAL) has garnered substantial attention in recent years, resulting in a multitude of approaches addressing the problem from diverse angles. One notable strategy, presented in [2], involves training an ensemble of neural networks followed by the selection of samples exhibiting the highest acquisition scores. These scores are determined through acquisition functions such as entropy [45] or BALD [16].

Concurrent research [10, 22]
delves into similar territory, approximating uncertainty by leveraging Monte-Carlo dropout [9]. A comparative analysis performed in [2] sheds light on these approaches, resolutely concluding that the ensemble-based methodology yields superior results albeit with increased computational demands. An alternate Bayesian approach is presented by [50], wherein data augmentation is combined with Bayesian networks. The authors employ a variational autoencoder (VAE) [21] on real and augmented samples, selecting unlabeled samples based on the VAE's reconstruction error. An analogous strategy is outlined in [46], wherein a latent space is learned using a VAE in tandem with an adversarial network trained to distinguish between labeled and unlabeled data. The VAE and adversarial network engage in a minimax game, with the former attempting to deceive the latter into classifying all data points as labeled, while the adversarial network refines its ability to discern dissimilarities within the latent space. A divergent approach is presented in [41], wherein the active learning challenge takes the form of core-set selection. This entails the identification of a subset of points such that a model trained on this subset remains competitive when applied to the broader dataset. Another unique perspective is offered by the work of [52]. Here, the authors present a heuristic yet elegant solution: a network is trained for classification while concurrently predicting cross-entropy loss. During the sample acquisition phase, samples with the highest prediction loss are deemed the most intriguing and subsequently earmarked for labeling.

Deep Semi-Supervised Actove Learning (DSSL). constitutes a profound approach in deep learning that merges a limited set of labeled data with a substantial pool of unlabeled data during neural network training. This contrasts with active learning (AL), where the utilization of unlabeled data is typically restricted to the acquisition phase. Within semi-supervised learning (SSL), these unlabeled data play a role throughout the training process. Several methods have demonstrated exceptional outcomes [24,25,32,48] by framing semi-supervised learning as a regularization challenge.

This involves introducing an additional loss component for the unlabeled samples, effectively enhancing the learning process. Subsequent endeavors have significantly advanced SSL's performance in object classification [3–5,34,47,54]. These efforts have contributed to refining the SSL paradigm and achieving remarkable results across diverse applications.

Interestingly, despite the apparent overlap between active learning and semi-supervised learning, the fusion of these methodologies has been a relatively unexplored territory. A pioneering attempt to unify these concepts surfaced in [11]. This work employs a consistency-based semisupervised learning technique during training, establishing a connection between these two pivotal domains. The work was later extended in the domain of object detection [8] giving similar conclusions.

## 3. Representative Active Learning Works

Notation: Let D be a dataset divided into a labeled set L
and a pool of unlabeled data U. Each sample in the dataset belongs to a class y, and in total there are c classes. The Active Learning acquisition function consists of mining a subset of samples from the pool of unlabeled data U and transferring them to the labeled set L, incurring a labeling cost. For a sample x (e.g., an image), a neural network θ
generates a feature vector f and a softmax probability distribution pi, where p represents the likelihood of the sample belonging to class i. We define the labeling budget as b and typically *b <<* |L|. The training procedure is done for n active learning cycles, and in each cycle, we label *b/n* the most promising samples.

Active Learning methods: In our framework, we consider the following representative active learning works: random, entropy, variational ratio, Bayesian Active Learning (BALD), Core-Set, and Learning Loss for Active Learning (LLAL).

Random a(x) = unif() with unif() is a function returning a draw from a uniform distribution over the interval [0, 1]. Using this acquisition function is equivalent to choosing a point uniformly at random from the pool. It is the default baseline in active learning.

Entropy is an active learning method, where the classifier trained in this current iteration computes the softmax predictions of the unlabeled samples, and we choose to label the samples with the highest entropy (on the softmax predictions). The entropy of a sample is computed as:

$$H(x)=\sum_{i=1}^{c}p_{i}log(p_{i}).\tag{1}$$
Variation Ratio describes the lack of confidence of a classifier. It is computed as:

$\pi(x)=1-max(p|x)$.

BALD scores a data point based on how well the model's predictions inform us about the model parameters θ. For this, it computes the mutual information I(y|θ). The formula is given as:

$$B(x)=H(y|x)-\mathbb{E}_{p(\theta)}[H[y|x,\theta]]=\mathbb{I}(y,\theta|x).\tag{3}$$
where E represents the expectation.

LLAL divides a minibatch of size B into B/2 data pairs
(xj, xk). Then, it learns the loss prediction module by considering the difference between a pair of loss predictions, which completely makes the loss prediction module discard the overall scale changes. For each pair, the loss function of the loss prediction module is defined as:

$$L_{loss}(\hat{l},l)=max(0,1(l_{k},l_{j})\cdot(\hat{l}_{k}-\hat{l}_{j})+\xi)\tag{4}$$
where ξ is a pre-defined positive margin, and 1 is an indicator variable that takes values +1 if li *> l*j, and −1 otherwise. Then, during inference, only the learned loss Lloss is predicted, with the labeled samples being those with the highest L*loss*.

Core-Set divides the labeled pool into k clusters, in such a way as to maximize the spread of the labeled data. It uses a complex optimization procedure based on Gurobi [13] optimizer.

All the mentioned methods, except Core-set, compute the acquisition function and then choose to label the b/n samples with the highest acquisition score. For the most part, these methods are also known as *uncertainty* methods. In the case of Core-set, it chooses the *b/n* samples that maximize the representation of the data, and it is known as a *diversity* method.

## 3.1. Flaws In The Methodology

Active Learning research is not very standardized. Different methods use different backbones and typically minimal comparison with other methods. Furthermore, most of the methods do not use a validation set, and perform experiments in only one or two datasets, usually in simple ones like CIFAR-10. Additionally, most methods show experiments in a very limited setting (e.g., very few AL cycles). LLAL [52] in particular improves the backbone to be higher-performing for low-resolution images, and achieves better results than the other methods. However, while we were able to reproduce their results, the results of entropybased AL were higher than those reported in the paper, and

|                 | CIF10   | CIF100   | CAL101   | CAL256   |
|-----------------|---------|----------|----------|----------|
| dataset size    | 50000   | 50000    | 6084     | 30607    |
| initial labeled | 1000    | 1000     | 1000     | 5000     |
| num cycles      | 20      | 20       | 5        | 10       |
| label cycle     | 1000    | 1000     | 1000     | 1000     |
| num epochs      | 200     | 200      | 200      | 200      |
| optimizer       | SGD     | SGD      | SGD      | SGD      |
| learning rate   | 0.1     | 0.1      | 0.1      | 0.1      |
| momentum        |         |          |          |          |
| 0.9             | 0.9     | 0.9      | 0.9      |          |
| scheduler       | step    | step     | step     | step     |
| scheduler step  | 160     | 160      | 160      | 160      |
| weight decay    | 5e-4    | 5e-4     | 5e-4     | 5e-4     |

actually similar to those of LLAL. Other methods like Variational Adversarial Active Learning (VAAL) [46], as can be seen from the official code, by mistake, report the results in the training set. Our experiments in the method show that it does not outperform random acquisition. The Power of Ensembles method [2], while reaching very high results, comes with a significantly higher computational cost. It also is unclear if the improvement comes from ensembles improving AL, or from the higher computational cost.

In this work, we strive for simplicity. We train all methods under the same hyperparameter configuration, seed, backbone, and training tricks. We also use a larger number of datasets, being diverse in their complexity and image resolution. Furthermore, we apply a larger number of AL cycles, to have more complete results.

## 4. Experiments 4.1. Experimental Setup

We perform our experiments in four standard classification benchmarks: CIFAR-10, CIFAR-100 [23], Caltech- 101, and Caltech-256 [12]. We keep a unified setting, where we keep the same hyperparameters for all datasets. Changing the hyperparameters for every dataset, while it can come with a slight improvement, is unrealistic in the active learning setup. Based on the dataset size, we do a different number of active learning cycles. We add 1000 images for labeling in each cycle. We train each network from scratch at every active learning cycle. We report the mean and standard deviation based on the training of five trials. For each method, we use the same initial split and random seed. We give the main hyperparameters for each dataset in Table 1. We also provide the exact numbers (mean and standard deviation) in the supplementary.

## 4.2. Main Result: Comparisons

We show the results of our experiments performed in CIFAR-10 in Figure 1a. All methods start at roughly the same point, subject to network fluctuations. We show that immediately in the second AL cycle, the entropy and LLAL acquisition functions outperform the random baseline by 1.4 percentage points (pp), respectively 1.1pp. In the third cycle, both methods outperform the random baseline by over 2.5pp. Both methods continue outperforming random by circa 3pp for the remaining of the training, with entropy having a slight advantage over LLAL, outperforming LLAL by around 1pp in the last 10 AL cycles. Interestingly, the other methods need more AL cycles to start outperforming the random baseline. For example, the random baseline outperforms BALD and Variation Ratio in the first four AL cycles, and Core-set in the first five AL cycles. After that, Core-set and BALD consistently outperform the random baseline, but always track behind LLAL and entropy, in the case of the latter, by up to 3pp. However, the Variation Ratio, after a couple of steps where it slightly outperforms the random baseline, quickly converges to the same performance and usually lags behind the entropy by 2.5 − 3pp.

We see a more interesting picture when we train in the more difficult CIFAR-100, and show its results in Figure 1b. In the first few steps, the random baseline outperforms all the acquisition functions except the Core-set. In fact, the entropy starts clearly outperforming the random baseline only after the 12th AL step, LLAL starts outperforming the random baseline only after the 14th AL step, while the performance of BALD and Variation Ratio typically is only as good as that of the random baseline. Core-set starts performing better than all the other methods, outperforming the random baseline by 1pp and entropy by 2pp in the first step. In the second step, it outperforms the random baseline by 1.5pp and entropy by almost 3pp. It continues outperforming entropy until the 13th step, after which it consistently is outperformed by entropy, finishing in the 20th step by almost 2pp worse than the entropy.

We continue our experiments in the Caltech-101 dataset, which contains images with a significantly larger resolution. We show the results in Figure 1c. In the second AL step, entropy already outperforms the random baseline by close to 5.5pp. Core-set outperforms the random baseline by 2.5pp while the other three methods reach only as good results as the random baseline. Then, on the next cycle, the entropy and Core-set outperform the random baseline by around 9pp and respectively 6pp. At this stage, the other three methods start outperforming the random baseline, in the case of LLAL by circa 2.5pp with the other two methods by around
1 − 1.5pp. At the last cycle, entropy outperforms random by over 7pp, Core-set outperforms random by around 4pp, and LLAL outperforms random by 2.2pp, with BALD and Variation Ratio improving over the baseline by around 1pp.

We now show the results in the most challenging dataset, Caltech-256 in Figure 1d. Because of the complexity of the dataset, all the methods perform around the same in the first few AL steps. Interestingly, the random baseline outperforms all the other methods in the fourth and fifth steps. After that, the entropy takes the lead and finishes the training outperforming the random by over 4pp. BALD, Coreset and Variation Ratio finish strongly, outperforming the random baseline by around 2.5pp. LLAL never manages to outperform the random baseline and finishes the training getting outperformed by random by almost 1pp.

Recommendation 1: Entropy is all you need.

To our biggest surprise, despite the rapid research in the field of active learning, entropy is arguably still the best active learning method.

While in specific scenarios, some other methods might outperform entropy, in general, entropy reaches at least competitive performances and more often than not, outperforms the other methods. Some methods such as LLAL perform nearly as well as the entropy in the dataset they were developed. However, in more challenging datasets like CIFAR-100 and Caltech-256, they fail to show much, if any, improvement over the random baseline. The Core-set, in general, shows the second-best performance after the entropy and usually performs highly in challenging datasets. BALD and Variation Ratio are shown to be very dataset-specific, and in general, tend to perform much worse than the entropy. We recommend that the practitioners use the entropy acquisition function before going to more complicated solutions. More often than not, this acquisition function is the best they can get, and it tends to perform well in most if not all, settings.

## 4.3. Ablation Study

We do a series of ablation studies, evaluating some of the design choices in active learning. We do the experiments in the CIFAR-10 dataset, using the best-found acquisition function, the entropy.

## 4.3.1 The Budget Of Each Cycle

Most AL research papers arbitrarily choose the number of samples labeled in every cycle. In this ablation study, we show the performance when the labeling budget for each cycle is small (500 samples), medium (1000 samples) and large (2000 samples). We present the results in Figure 2a.

As shown, until we label 4000 samples, the medium case works significantly better than the large and especially small cases. In particular, where we have 2000 and 3000 labeled samples, the medium case outperforms the small case by
3.5 − 4pp. After that, the performance difference between the medium and small/large diminishes, albeit the medium case shows a slightly better performance in almost all AL cycles. At the end of the training, with 20000 labeled samples, medium outperforms the other two cases by around half a percentage point.

Recommendation 2: Use a medium-sized budget for each AL cycle.

While using small-sized budgets might sound tempting, it does not perform very well in practice. This is because by choosing only the very hard samples, the network gets biased towards hard samples, thus, not performing well in the not-hard samples. This can be especially seen in the first few AL cycles. Similarly, using large budgets is equivalent to choosing a large number of easy, thus not very informative samples. We recommend that the practitioners use medium-sized acquisition budgets for each AL cycle.

## 4.3.2 To Train Vs. To Finetune

Some AL methods, in each AL cycle, continue training the network from the previous AL cycle. The intuition behind this is that the network has already shown some good performance, and by adding more data and continuing training, the performance of the network will improve. On the other hand, some other works train every network from scratch. The motivation behind it is that the networks trained on a small amount of data are potentially stuck in local minima. While adding more data will improve their performance, they might still struggle to escape the local minima, thus, it is better to train them from scratch. We perform a full training loop, in one case training the network from *scratch*, and in one training the network from the previous cycle, thus finetuning it. We perform the experiments in CIFAR-10, using the entropy acquisition function. We present the results in Figure 2b.

As we can clearly see, the networks trained from scratch tend to outperform the finetuned network. In the second and third AL cycles, the networks trained from scratch outperform the finetuned networks by an average of 4pp. The performance gain by training from scratch is lower in the next few cycles, until it completely diminishes, with both the methods performing the same.

Recommendation 3: Train networks from scratch.

We recommend the practitioners reinitialize the network at each AL cycle. This is important, especially in the first few AL cycles where the number of data is smaller. In later cycles, it does not much difference if the network is trained from scratch or it is finetuned.

## 4.3.3 The Question Of Diversity

Most of the methods we used in this work do not consider the diversity between the selected samples (except the Core-set). To consider the diversity, we adopt the heuristic of [52] where we first randomly pre-select 10000 samples to be considered, and then from them we choose the 1000
samples to be labeled, based on the acquisition score. This method probabilistically adds the concept of diversity to the model. We present the results in Figure 3a, showing that the method has a positive effect in the first few AL cycles. In particular, it improves the results by 1.5pp in the second cycle, and by a maximum of 2pp in the fourth AL cycle. After the sixth cycle, we do not see any difference between the method that uses diversity and the one that does not.

We now perform another experiment where we emulate a dataset with repetition. We duplicate each sample twice (CIFAR-10x2) and five times (CIFAR-10x5). Naturally, any method that does not consider diversity will struggle with datasets that have repetition. This is because, for every sample that has a high acquisition score, it will also select the other identical samples to label, despite that they do not contain any extra information. We present the results in Figure 3b for Cifar-10x2, and Figure 3c for Cifar-10x5 We show that the method that does not use any diversity not only suffers low results but actually performs worse than the random baseline. Further, the higher the repetition, the worse the results of the method. On the other hand, considering the diversity helps in not selecting identical samples, reaching significantly better results than the random baseline.

Recommendation 4: Diversity matters.

We recommend that practitioners add the notion of diversity to their AL framework. While some methods based on constrained optimization [13] are computationally expensive, even simple heuristics help, especially in the early AL cycles. Diversity is important in cases of sample repetition, and in such cases, uncertainty-based AL without diversity methods reach lower performance than the random baseline.

## 4.3.4 Extension To Object Detection

We now do a small study of AL methods in object detection. We extend the same six methods for object detection, not considering the AL methods that are completely tailored for object detection. We do experiments in the PASCAL VOC07+12 dataset, using SSD object detector [29], and the training framework of [7]. We present our results in Figure 4a. In the second AL cycle, we see that all methods except Core-Set perform roughly the same. Core-Set starts very strongly, improving over the random baseline by almost 2pp. In the third cycle, all methods outperform the random baseline by at least 0.5pp with Core-set reaching the best results outperforming the random baseline by more than 1pp. In the other cycles, Core-Set, LLAL and entropy reach around the same results, all of them ending the training by at least 1pp better than the random baseline. However, BALD and Variational Ratio just slightly improved over the random baseline.

Recommendation 5: Use AL for object detection.

However, do not expect the performance improvement to be as big as in classification. From the evaluated methods entropy and Core-set seem to perform the best. From other studies, methods tailored for object detection tend to outperform our baselines [1, 7, 14, 20, 39, 53], so we recommend considering them in addition to mentioned methods.

## 4.3.5 Consistency Helps Active Learning

We combine Active Learning with consistency-based Semi- Supervised Learning (AL-SSL) and see their combined effects. For classification, we follow previous work and use [4] as the SSL algorithm of choice. We use an adaption of the method [18] for object detection. We show the results of the SSL when done without active learning (random baseline), with entropy acquisition function and with inconsistency acquisition function [11]. For the inconsistency acquisition function, we use the consistency loss as done in [8]. We provide all the implementation details in the supplementary material. We present the classification results in Figure 4c. We see that the results of all methods are significantly higher than those in the previous experiments. This is because of the effect of the semi-supervised learning, that considerably improves the results. However, we can also see the effect of Active Learning, which comes at the top of Semi-Supervised Learning. We see that both the entropy and consistency considerably improve over the random baseline, with inconsistency-based AL reaching the best results Similarly, we present the results of object detection in Figure 4b. We observe that while in the second AL
cycle, there is just a small improvement between the AL-
SSL methods, and the SSL method with random acquisition score, in the later cycles, we see a significant improvement. For example, entropy outperforms random by more than 1pp in the last three AL cycles, with a peak of 1.7pp performance improvement in the last cycle. We also observe that the performance of the entropy acquisition function and the inconsistency AL are very close to each other, with the methods performing as well as each other.

Recommendation 6: Combine SSL with AL. The results will significantly improve, and the two methodologies improve each other.

5. Conclusion In this study, we performed a fair empirical study of various Active Learning methods and ablated some of the most important parts of the models. We performed the study in a controlled setting, where we took care to minimize the possible fluctuations of the network training, hyperparameters and initial labeling set. Our most interesting finding is surprising: in general, no method tends to outperform entropy, the simplest acquisition function. We do ablations in the budget for each AL cycle, training or finetuning the network, and handling the diversity in the dataset, giving recommendations for each of them. We end our study by showing experiments that combined AL with SSL, and extensions in object detection.

## Broader Impact

Labeling data is one of the biggest pitfalls in machine learning cycles. It is an expensive process and subject to human errors. In some settings, such as autonomous driving, the majority of data is redundant, thus labeling more of it, does not come with a performance improvement. AL is one of the most promising approaches that helps practitioners in choosing to label the right data, which when fed to a network, give the best improvement. Despite many AL methods claiming to be the SOTA in the field, there are many questions with respect to the experimental setup, and thus the lessons learned from them. In this work, we shed some light on the world of AL, devising a fair setup, and training multiple AL methods in different datasets. We trained over 3, 000 networks, showing the best-performing AL method, and learning in the process some insights that we hope can help other researchers. Similar studies in SSL [34] and metric learning [33] gave a massive boost to the research in their field. We hope our study can help practitioners choose the right acquisition function and engineering practices so that not everyone needs to reinvent the wheel.

## References

[1] Hamed Habibi Aghdam, Abel Gonzalez-Garcia, Antonio M.
L´opez, and Joost van de Weijer. Active learning for deep
detection neural networks. In *ICCV*, 2019. 7
[2] William H. Beluch, Tim Genewein, Andreas N¨urnberger,
and Jan M. K¨ohler. The power of ensembles for active learning in image classification. In *CVPR*, 2018. 1, 2, 4
[3] David Berthelot, Nicholas Carlini, Ekin D. Cubuk, Alex Kurakin, Kihyuk Sohn, Han Zhang, and Colin Raffel. Remixmatch: Semi-supervised learning with distribution matching and augmentation anchoring. In *ICLR*. 3
[4] David Berthelot, Nicholas Carlini, Ian J. Goodfellow, Nicolas Papernot, Avital Oliver, and Colin Raffel. Mixmatch: A holistic approach to semi-supervised learning. In *NeurIPS*,
2019. 3, 8, 11
[5] David Berthelot, Rebecca Roelofs, Kihyuk Sohn, Nicholas
Carlini, and Alex Kurakin. Adamatch: A unified approach to semi-supervised learning and domain adaptation. *CoRR*,
abs/2106.04732, 2021. 3
[6] Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian
Schroff, and Hartwig Adam. Encoder-decoder with atrous separable convolution for semantic image segmentation. In ECCV, 2018. 1
[7] Jiwoong Choi, Ismail Elezi, Hyuk-Jae Lee, Cl´ement Farabet, and Jose M. Alvarez. Active learning for deep object detection via probabilistic modeling. In *ICCV*, 2021. 7
[8] Ismail Elezi, Zhiding Yu, Anima Anandkumar, Laura Leal-
Taixe, and Jose M. Alvarez. Not all labels are equal: Rationalizing the labeling costs for training object detection. In CVPR, 2022. 3, 8, 11
[9] Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian
approximation:
Representing model uncertainty in deep
learning. In *ICML*, 2016. 2
[10] Yarin Gal, Riashat Islam, and Zoubin Ghahramani. Deep
bayesian active learning with image data. In International Conference on Machine Learning, pages 1183–1192, 2017. 2
[11] Mingfei Gao, Zizhao Zhang, Guo Yu, Sercan ¨Omer Arik,
Larry S. Davis, and Tomas Pfister. Consistency-based semisupervised active learning: Towards minimizing labeling cost. In *ECCV*, 2020. 1, 3, 8, 11
[12] Gregory Griffin, Alex Holub, and Pietro Perona. Caltech-256
object category dataset. 2007. 4
[13] Gurobi Optimization, LLC.
Gurobi Optimizer Reference
Manual, 2023. 3, 7
[14] Elmar Haussmann, Michele Fenzi, Kashyap Chitta, Jan Ivanecky, Hanson Xu, Donna Roy, Akshita Mittel, Nicolas Koumchatzky, Clement Farabet, and Jose M Alvarez. Scalable active learning for object detection. In IV, 2020. 7
[15] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
Deep residual learning for image recognition.
In *CVPR*,
2016. 1
[16] Neil Houlsby, Ferenc Huszar, Zoubin Ghahramani, and M´at´e
Lengyel. Bayesian active learning for classification and preference learning. *CoRR*, abs/1112.5745, 2011. 2
[17] Juan Eugenio Iglesias, Ender Konukoglu, Albert Montillo,
Zhuowen Tu, and Antonio Criminisi. Combining generative
and discriminative models for semantic segmentation of CT scans via active learning. In Information Processing in Medical Imaging, 2011. 2

[18] Jisoo Jeong, Seungeui Lee, Jeesoo Kim, and Nojun Kwak.
Consistency-based semi-supervised learning for object detection. In *NeurIPS*, 2019. 8, 11
[19] Armand Joulin, Laurens van der Maaten, Allan Jabri, and
Nicolas Vasilache.
Learning visual features from large
weakly supervised data. In *ECCV*, 2016. 1
[20] Chieh-Chi Kao, Teng-Yok Lee, Pradeep Sen, and Ming-Yu
Liu. Localization-aware active learning for object detection. In *ACCV*, 2018. 7
[21] Diederik P. Kingma and Max Welling. Auto-encoding variational bayes. In International Conference on Learning Representations, 2014. 2
[22] Andreas Kirsch, Joost van Amersfoort, and Yarin Gal.
Batchbald: Efficient and diverse batch acquisition for deep
bayesian active learning. In Advances in Neural Information Processing Systems 32, pages 7024–7035, 2019. 2
[23] Alex Krizhevsky. Learning multiple layers of features from
tiny images. Technical report, 2009. 4
[24] Samuli Laine and Timo Aila. Temporal ensembling for semisupervised learning. In International Conference on Learning Representations, 2017. 3
[25] Dong-Hyun Lee.
Pseudo-label: The simple and efficient
semi-supervised learning method for deep neural networks. ICML Workshop on Challenges in Representation Learning, 2013. 3
[26] David D. Lewis and Jason Catlett.
Heterogeneous uncertainty sampling for supervised learning. In Machine Learning, Proceedings of the Eleventh International Conference, pages 148–156, 1994. 2
[27] David D. Lewis and William A. Gale. A sequential algorithm for training text classifiers.
In Proceedings of the
17th Annual International ACM-SIGIR Conference on Research and Development in Information Retrieval, pages 3– 12. ACM/Springer, 1994. 2
[28] Tsung-Yi Lin, Michael Maire, Serge J. Belongie, James
Hays, Pietro Perona, Deva Ramanan, Piotr Doll´ar, and
C. Lawrence Zitnick. Microsoft COCO: common objects in context. In *European Conference in Computer Vision*, pages 740–755, 2014. 1
[29] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C Berg. Ssd: Single shot multibox detector. In European Conference on Computer Vision (ECCV), 2016. 7
[30] Wenjie Luo, Alexander G. Schwing, and Raquel Urtasun.
Latent structured active learning. In Advances in Neural Information Processing Systems, pages 728–736, 2013. 2
[31] Dhruv Mahajan, Ross B. Girshick, Vignesh Ramanathan,
Kaiming He, Manohar Paluri, Yixuan Li, Ashwin Bharambe, and Laurens van der Maaten. Exploring the limits of weakly supervised pretraining.
In European Conference in Computer Vision, pages 185–201, 2018. 1
[32] Takeru Miyato, Shin-ichi Maeda, Masanori Koyama, and
Shin Ishii.
Virtual adversarial training: A regularization
method for supervised and semi-supervised learning. IEEE
Trans. Pattern Anal. Mach. Intell., 41(8):1979–1993, 2019.

1, 3

[33] Kevin Musgrave, Serge J. Belongie, and Ser-Nam Lim. A
metric learning reality check. In *ECCV*, 2020. 1, 8
[34] Avital Oliver, Augustus Odena, Colin Raffel, Ekin Dogus
Cubuk, and Ian J. Goodfellow. Realistic evaluation of deep semi-supervised learning algorithms. In Advances in Neural
Information Processing Systems, pages 3239–3250, 2018. 1, 3, 8
[35] George Orwell. Animal farm. In *William Collins*, 1946. 1
[36] Antti Rasmus, Mathias Berglund, Mikko Honkala, Harri
Valpola, and Tapani Raiko. Semi-supervised learning with ladder networks. In Advances in Neural Information Processing Systems, pages 3546–3554, 2015. 1
[37] Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun.
Faster R-CNN: towards real-time object detection with region proposal networks. In Advances in Neural Information Processing Systems, pages 91–99, 2015. 1
[38] Dan Roth and Kevin Small. Margin-based active learning
for structured output spaces.
In European Conference on
Machine Learning, pages 413–424, 2006. 2
[39] Soumya Roy, Asim Unmesh, and Vinay P. Namboodiri.
Deep active learning for object detection. In *BMVC*, 2018. 7
[40] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael S. Bernstein, Alexander C. Berg, and Fei-Fei Li. Imagenet large scale visual recognition challenge. *International Journal of Computer Vision*,
115(3):211–252, 2015. 1
[41] Ozan Sener and Silvio Savarese. Active learning for convolutional neural networks: A core-set approach. In International Conference on Learning Representations, 2018. 2
[42] Burr Settles. *Active Learning*. Synthesis Lectures on Artificial Intelligence and Machine Learning. Morgan & Claypool Publishers, 2012. 2
[43] Burr Settles and Mark Craven. An analysis of active learning
strategies for sequence labeling tasks. In Empirical Methods in Natural Language Processing, pages 1070–1079, 2008. 2
[44] H. Sebastian Seung, Manfred Opper, and Haim Sompolinsky. Query by committee. In Conference on Computational
Learning Theory, pages 287–294, 1992. 2
[45] Claude E. Shannon. A mathematical theory of communication.
Mobile Computing and Communications Review,
5(1):3–55, 2001. 2
[46] Samarth Sinha, Sayna Ebrahimi, and Trevor Darrell. Variational adversarial active learning. *CoRR*, abs/1904.00370, 2019. 1, 2, 4
[47] Kihyuk Sohn, David Berthelot, Nicholas Carlini, Zizhao
Zhang, Han Zhang, Colin Raffel, Ekin Dogus Cubuk, Alexey Kurakin, and Chun-Liang Li. Fixmatch: Simplifying semisupervised learning with consistency and confidence.
In
NeurIPS, 2020. 3
[48] Antti Tarvainen and Harri Valpola. Mean teachers are better
role models: Weight-averaged consistency targets improve semi-supervised deep learning results. In Advances in Neural Information Processing Systems, pages 1195–1204, 2017. 3
[49] Simon Tong and Daphne Koller. Support vector machine active learning with applications to text classification. Journal of Machine Learning Research, 2:45–66, 2001. 2
[50] Toan Tran, Thanh-Toan Do, Ian D. Reid, and Gustavo
Carneiro.
Bayesian generative active deep learning.
In
ICML, 2019. 2
[51] Sudheendra Vijayanarasimhan and Kristen Grauman. Largescale live active learning: Training object detectors with crawled data and crowds. In Computer Vision and Pattern Recognition, pages 1449–1456, 2011. 2
[52] Donggeun Yoo and In So Kweon. Learning loss for active
learning. In *Computer Vision and Pattern Recognition*, pages 93–102. Computer Vision Foundation / IEEE, 2019. 1, 2, 3, 7
[53] Tianning Yuan, Fang Wan, Mengying Fu, Jianzhuang Liu,
Songcen Xu, Xiangyang Ji, and Qixiang Ye. Multiple instance active learning for object detection. In *CVPR*, 2021.
7
[54] Bowen Zhang, Yidong Wang, Wenxin Hou, Hao Wu, Jindong Wang, Manabu Okumura, and Takahiro Shinozaki. Flexmatch: Boosting semi-supervised learning with curriculum pseudo labeling. In *NeurIPS*, 2021. 3
In this supplementary material, we complement the results of the main paper. We give extra information about the consistency sections (Section 4.3.5 in the main paper), and we provide the mean and standard deviation for every experiment. We perform each experiment in a single NVIDIA V100 GPU.

## 5.1. Consistency Helps Active Learning 5.2. Image Classification

We combine Active Learning with consistency-based Semi-Supervised Learning (AL-SSL) and see their combined effects. Because the results of SSL are already quite high with 1k − 2k labeled images, we perform the experiments starting with 250 images, and double the number of labels in each cycle. For classification, we follow previous work and use MixMatch [4, 11] as the SSL algorithm of choice. We train the network for 1024 epochs, we do not make any changes to the algorithm, training procedure, or the backbone. During training, MixMatch makes two different augmentations in an image, and computes the loss function as the distance between the network's prediction We use the same loss function as inconsistency acquisition score.

## 5.2.1 Object Detection

We present the results of the SSL in object detection. As SSL method, we use that of [18]. The method feed to the network an image, and its augmented version (for example, by performing a horizontal clip), and then computes as loss function the symmetric KL divergence between the predictions of the network for both views of the image. Similar to [8], we use the same loss function as acquisition function. We train the model for 120, 000 iterations using SGD
with momentum. and we do not make any changes to the algorithm or the training procedure.

## 5.3. Detailed Results

In the paper, we provide plots for the main experiments due to the limited space. In Tables 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 we summarize the exact numbers corresponding to Figures 1a, 1b, 1c, 1d, 2a, 2b, 3a, 3b, 3c, 4a, 4b and 4c of the main paper. We provide the mean and the standard deviation for each method and AL cycle. Each experiment has been run five times.

| # labeled   |   Random |
|-------------|----------|
| 1k          |          |
| 51.78       |          |
| ±           |          |
| 0.6         |          |
| 50.74       |          |
| ±           |          |
| 1.5         |    50.74 |
| ±           |          |
| 2.3         |    51.01 |
| ±           |          |
| 1.1         |    50.34 |
| ±           |          |
| 0.3         |    50.74 |
| ±           |          |
| 0.6         |          |
| 2k          |          |
| 65.48       |          |
| ±           |          |
| 0.7         |    66.58 |
| ±           |          |
| 1.5         |          |
| 66.90       |          |
| ±           |          |
| 1.6         |          |
| 62.71       |          |
| ±           |          |
| 0.5         |    63.33 |
| ±           |          |
| 0.8         |    62.82 |
| ±           |          |
| 0.5         |          |
| 3k          |    73.69 |
| ±           |          |
| 0.9         |    76.09 |
| ±           |          |
| 1.4         |          |
| 76.14       |          |
| ±           |          |
| 1.6         |          |
| 72.42       |          |
| ±           |          |
| 0.3         |    72.06 |
| ±           |          |
| 0.6         |    71.6  |
| ±           |          |
| 0.5         |          |
| 4k          |    78.66 |
| ±           |          |
| 1.3         |    80.81 |
| ±           |          |
| 0.8         |          |
| 81.34       |          |
| ±           |          |
| 0.5         |          |
| 78.92       |          |
| ±           |          |
| 0.5         |    78.26 |
| ±           |          |
| 0.3         |    76.27 |
| ±           |          |
| 0.4         |          |
| 5k          |          |
| 81.05       |          |
| ±           |          |
| 1.0         |    82.52 |
| ±           |          |
| 0.4         |          |
| 83.59       |          |
| ±           |          |
| 0.6         |          |
| 80.88       |          |
| ±           |          |
| 0.5         |    82.65 |
| ±           |          |
| 0.6         |    80.53 |
| ±           |          |
| 0.2         |          |
| 6k          |    83.52 |
| ±           |          |
| 0.7         |    85.78 |
| ±           |          |
| 0.3         |          |
| 86.26       |          |
| ±           |          |
| 0.7         |          |
| 84.62       |          |
| ±           |          |
| 0.3         |    86.23 |
| ±           |          |
| 0.3         |    83.77 |
| ±           |          |
| 0.2         |          |
| 7k          |    85.01 |
| ±           |          |
| 1.0         |    87.36 |
| ±           |          |
| 0.4         |          |
| 87.95       |          |
| ±           |          |
| 0.3         |          |
| 86.32       |          |
| ±           |          |
| 0.1         |    87.79 |
| ±           |          |
| 0.2         |    85.43 |
| ±           |          |
| 0.4         |          |
| 8k          |    86.1  |
| ±           |          |
| 0.7         |    88.55 |
| ±           |          |
| 0.3         |          |
| 89.19       |          |
| ±           |          |
| 0.2         |          |
| 87.92       |          |
| ±           |          |
| 0.2         |    88.75 |
| ±           |          |
| 0.2         |    86.49 |
| ±           |          |
| 0.2         |          |
| 9k          |    87.15 |
| ±           |          |
| 0.7         |    89.42 |
| ±           |          |
| 0.4         |          |
| 90.16       |          |
| ±           |          |
| 0.2         |          |
| 88.87       |          |
| ±           |          |
| 0.2         |    90.11 |
| ±           |          |
| 0.1         |    87.53 |
| ±           |          |
| 0.2         |          |
| 10k         |          |
| 87.63       |          |
| ±           |          |
| 0.5         |    90.08 |
| ±           |          |
| 0.2         |          |
| 90.89       |          |
| ±           |          |
| 0.2         |          |
| 89.72       |          |
| ±           |          |
| 0.2         |    90.5  |
| ±           |          |
| 0.1         |    87.85 |
| ±           |          |
| 0.1         |          |
| 11k         |    88.51 |
| ±           |          |
| 0.6         |    90.97 |
| ±           |          |
| 0.4         |          |
| 91.65       |          |
| ±           |          |
| 0.3         |          |
| 90.81       |          |
| ±           |          |
| 0.1         |    91.53 |
| ±           |          |
| 0.1         |    89.19 |
| ±           |          |
| 0.2         |          |
| 12k         |    89.13 |
| ±           |          |
| 0.6         |    91.61 |
| ±           |          |
| 0.4         |          |
| 92.27       |          |
| ±           |          |
| 0.1         |          |
| 91.41       |          |
| ±           |          |
| 0.2         |    92.04 |
| ±           |          |
| 0.3         |    89.4  |
| ±           |          |
| 0.2         |          |
| 13k         |    89.66 |
| ±           |          |
| 0.5         |    92    |
| ±           |          |
| 0.2         |          |
| 92.76       |          |
| ±           |          |
| 0.2         |          |
| 91.75       |          |
| ±           |          |
| 0.2         |    92.21 |
| ±           |          |
| 0.2         |    89.41 |
| ±           |          |
| 0.1         |          |
| 14k         |    89.98 |
| ±           |          |
| 0.6         |    92.36 |
| ±           |          |
| 0.2         |          |
| 93.18       |          |
| ±           |          |
| 0.2         |          |
| 92.03       |          |
| ±           |          |
| 0.2         |    92.91 |
| ±           |          |
| 0.3         |    90.24 |
| ±           |          |
| 0.2         |          |
| 15k         |    90.37 |
| ±           |          |
| 0.5         |    92.63 |
| ±           |          |
| 0.2         |          |
| 93.35       |          |
| ±           |          |
| 0.2         |          |
| 92.40       |          |
| ±           |          |
| 0.2         |    93.03 |
| ±           |          |
| 0.2         |    90.17 |
| ±           |          |
| 0.1         |          |
| 16k         |    90.89 |
| ±           |          |
| 0.4         |    93.06 |
| ±           |          |
| 0.2         |          |
| 93.67       |          |
| ±           |          |
| 0.2         |          |
| 92.89       |          |
| ±           |          |
| 0.2         |    93.18 |
| ±           |          |
| 0.1         |    90.65 |
| ±           |          |
| 0.1         |          |
| 17k         |          |
| 91.06       |          |
| ±           |          |
| 0.6         |    93.31 |
| ±           |          |
| 0.2         |          |
| 93.89       |          |
| ±           |          |
| 0.1         |          |
| 93.09       |          |
| ±           |          |
| 0.2         |    93.22 |
| ±           |          |
| 0.2         |    90.92 |
| ±           |          |
| 0.2         |          |
| 18k         |    91.39 |
| ±           |          |
| 0.5         |    93.52 |
| ±           |          |
| 0.2         |          |
| 94.15       |          |
| ±           |          |
| 0.1         |          |
| 93.29       |          |
| ±           |          |
| 0.1         |    93.56 |
| ±           |          |
| 0.4         |    91.14 |
| ±           |          |
| 0.2         |          |
| 19k         |    91.6  |
| ±           |          |
| 0.4         |    93.6  |
| ±           |          |
| 0.2         |          |
| 94.36       |          |
| ±           |          |
| 0.2         |          |
| 93.45       |          |
| ±           |          |
| 0.1         |    93.55 |
| ±           |          |
| 0.1         |    91.48 |
| ±           |          |
| 0.1         |          |
| 20k         |          |
| 91.86       |          |
| ±           |          |
| 0.4         |    93.67 |
| ±           |          |
| 0.2         |          |
| 94.40       |          |
| ±           |          |
| 0.1         |          |
| 93.85       |          |
| ±           |          |
| 0.1         |    93.81 |
| ±           |          |
| 0.2         |    91.77 |
| ±           |          |
| 0.1         |          |
| # labeled   |   Random |
|-------------|----------|
| 1k          |    13.28 |
| ±           |          |
| 0.7         |    13.19 |
| ±           |          |
| 0.7         |    13.42 |
| ±           |          |
| 0.5         |    13.24 |
| ±           |          |
| 0.7         |          |
| 13.56       |          |
| ±           |          |
| 0.8         |          |
| 13.39       |          |
| ±           |          |
| 0.6         |          |
| 2k          |    20.43 |
| ±           |          |
| 0.7         |    18.69 |
| ±           |          |
| 0.7         |    19.87 |
| ±           |          |
| 0.4         |          |
| 21.24       |          |
| ±           |          |
| 0.8         |          |
| 19.73       |          |
| ±           |          |
| 0.9         |    20.32 |
| ±           |          |
| 1.3         |          |
| 3k          |    26.89 |
| ±           |          |
| 1.0         |    24.37 |
| ±           |          |
| 0.9         |    25.47 |
| ±           |          |
| 0.8         |          |
| 28.28       |          |
| ±           |          |
| 1.3         |          |
| 25.00       |          |
| ±           |          |
| 0.9         |    25.72 |
| ±           |          |
| 0.8         |          |
| 4k          |          |
| 32.88       |          |
| ±           |          |
| 1.6         |    29.57 |
| ±           |          |
| 1.3         |    31.24 |
| ±           |          |
| 1.6         |          |
| 33.87       |          |
| ±           |          |
| 0.9         |          |
| 30.28       |          |
| ±           |          |
| 1.4         |    30.38 |
| ±           |          |
| 1.1         |          |
| 5k          |    36.99 |
| ±           |          |
| 1.4         |    33.09 |
| ±           |          |
| 1.0         |    34.66 |
| ±           |          |
| 2.1         |          |
| 38.36       |          |
| ±           |          |
| 1.2         |          |
| 34.79       |          |
| ±           |          |
| 0.9         |    35.66 |
| ±           |          |
| 1.7         |          |
| 6k          |          |
| 43.45       |          |
| ±           |          |
| 1.1         |    39.9  |
| ±           |          |
| 0.7         |    43    |
| ±           |          |
| 1.6         |          |
| 45.70       |          |
| ±           |          |
| 1.3         |          |
| 41.30       |          |
| ±           |          |
| 1.3         |    41.73 |
| ±           |          |
| 1.2         |          |
| 7k          |    47.08 |
| ±           |          |
| 1.3         |    45.03 |
| ±           |          |
| 1.0         |    47.13 |
| ±           |          |
| 1.2         |          |
| 49.06       |          |
| ±           |          |
| 1.1         |          |
| 44.29       |          |
| ±           |          |
| 1.1         |    46.81 |
| ±           |          |
| 1.0         |          |
| 8k          |    50.41 |
| ±           |          |
| 1.3         |    48.65 |
| ±           |          |
| 0.7         |    50.08 |
| ±           |          |
| 1.1         |          |
| 51.51       |          |
| ±           |          |
| 0.8         |          |
| 48.01       |          |
| ±           |          |
| 1.7         |    49.58 |
| ±           |          |
| 0.9         |          |
| 9k          |    52.8  |
| ±           |          |
| 1.1         |    51.74 |
| ±           |          |
| 0.7         |    52.85 |
| ±           |          |
| 0.7         |          |
| 53.83       |          |
| ±           |          |
| 0.7         |          |
| 50.97       |          |
| ±           |          |
| 0.9         |    51.32 |
| ±           |          |
| 0.9         |          |
| 10k         |    55.09 |
| ±           |          |
| 0.8         |    54.05 |
| ±           |          |
| 0.5         |    55.68 |
| ±           |          |
| 0.7         |          |
| 55.90       |          |
| ±           |          |
| 0.9         |          |
| 54.03       |          |
| ±           |          |
| 0.7         |    54.79 |
| ±           |          |
| 0.5         |          |
| 11k         |    56.89 |
| ±           |          |
| 0.9         |    56.49 |
| ±           |          |
| 0.6         |    57.66 |
| ±           |          |
| 0.8         |          |
| 58.25       |          |
| ±           |          |
| 0.4         |          |
| 56.41       |          |
| ±           |          |
| 0.6         |    56.95 |
| ±           |          |
| 0.8         |          |
| 12k         |    58.58 |
| ±           |          |
| 0.8         |    58.51 |
| ±           |          |
| 0.6         |    59.67 |
| ±           |          |
| 0.5         |          |
| 59.93       |          |
| ±           |          |
| 0.4         |          |
| 58.61       |          |
| ±           |          |
| 0.5         |    58.56 |
| ±           |          |
| 0.4         |          |
| 13k         |    60.05 |
| ±           |          |
| 0.5         |    60.29 |
| ±           |          |
| 0.5         |          |
| 61.21       |          |
| ±           |          |
| 0.4         |          |
| 61.09       |          |
| ±           |          |
| 0.4         |    59.58 |
| ±           |          |
| 0.4         |    59.89 |
| ±           |          |
| 0.6         |          |
| 14k         |    61.3  |
| ±           |          |
| 0.6         |    61.88 |
| ±           |          |
| 0.6         |          |
| 62.80       |          |
| ±           |          |
| 0.5         |          |
| 62.33       |          |
| ±           |          |
| 0.3         |    60.38 |
| ±           |          |
| 0.6         |    60.97 |
| ±           |          |
| 0.5         |          |
| 15k         |    62.35 |
| ±           |          |
| 0.7         |    63.39 |
| ±           |          |
| 0.5         |          |
| 64.35       |          |
| ±           |          |
| 0.5         |          |
| 63.56       |          |
| ±           |          |
| 0.7         |    61.56 |
| ±           |          |
| 0.5         |    62.25 |
| ±           |          |
| 0.4         |          |
| 16k         |    63.35 |
| ±           |          |
| 0.6         |    64.32 |
| ±           |          |
| 0.4         |          |
| 65.42       |          |
| ±           |          |
| 0.1         |          |
| 64.58       |          |
| ±           |          |
| 0.4         |    62.67 |
| ±           |          |
| 0.3         |    63.26 |
| ±           |          |
| 0.5         |          |
| 17k         |    64.22 |
| ±           |          |
| 0.5         |    65.48 |
| ±           |          |
| 0.6         |          |
| 66.96       |          |
| ±           |          |
| 0.0         |          |
| 65.42       |          |
| ±           |          |
| 0.3         |    63.72 |
| ±           |          |
| 0.3         |    64.32 |
| ±           |          |
| 0.4         |          |
| 18k         |    65.21 |
| ±           |          |
| 0.6         |    66.51 |
| ±           |          |
| 0.5         |          |
| 67.58       |          |
| ±           |          |
| 0.3         |          |
| 66.36       |          |
| ±           |          |
| 0.5         |    64.83 |
| ±           |          |
| 0.4         |    65.11 |
| ±           |          |
| 0.4         |          |
| 19k         |    65.92 |
| ±           |          |
| 0.6         |    67.46 |
| ±           |          |
| 0.4         |          |
| 68.41       |          |
| ±           |          |
| 0.0         |          |
| 67.11       |          |
| ±           |          |
| 0.5         |    65.52 |
| ±           |          |
| 0.3         |    66.07 |
| ±           |          |
| 0.3         |          |
| 20k         |    66.69 |
| ±           |          |
| 0.5         |    68.18 |
| ±           |          |
| 0.4         |          |
| 69.92       |          |
| ±           |          |
| 0.8         |          |
| 68.12       |          |
| ±           |          |
| 0.4         |    66.6  |
| ±           |          |
| 0.4         |    66.5  |
| ±           |          |
| 0.4         |          |
| # labeled   |   Random |
|-------------|----------|
| 1k          |    21.35 |
| ±           |          |
| 1.6         |          |
| 21.75       |          |
| ±           |          |
| 1.7         |          |
| 20.98       |          |
| ±           |          |
| 1.4         |    20.17 |
| ±           |          |
| 1.5         |    21.52 |
| ±           |          |
| 1.6         |    21.74 |
| ±           |          |
| 1.5         |          |
| 2k          |    35.66 |
| ±           |          |
| 1.9         |    35.76 |
| ±           |          |
| 1.7         |          |
| 41.04       |          |
| ±           |          |
| 2.3         |          |
| 38.02       |          |
| ±           |          |
| 2.3         |    35.75 |
| ±           |          |
| 2.4         |    35.98 |
| ±           |          |
| 2.0         |          |
| 3k          |          |
| 47.21       |          |
| ±           |          |
| 1.6         |    49.79 |
| ±           |          |
| 1.6         |          |
| 56.49       |          |
| ±           |          |
| 0.9         |          |
| 53.09       |          |
| ±           |          |
| 2.0         |    48.43 |
| ±           |          |
| 1.6         |    48.87 |
| ±           |          |
| 1.5         |          |
| 4k          |    56.32 |
| ±           |          |
| 1.3         |    58.95 |
| ±           |          |
| 1.4         |          |
| 65.10       |          |
| ±           |          |
| 1.3         |          |
| 62.18       |          |
| ±           |          |
| 1.4         |    57.36 |
| ±           |          |
| 1.5         |    57.64 |
| ±           |          |
| 1.3         |          |
| 5k          |    62.66 |
| ±           |          |
| 0.8         |    64.88 |
| ±           |          |
| 1.2         |          |
| 69.99       |          |
| ±           |          |
| 1.0         |          |
| 66.42       |          |
| ±           |          |
| 0.8         |    63.34 |
| ±           |          |
| 0.9         |    63.46 |
| ±           |          |
| 0.9         |          |
| # labeled   |   Random |
|-------------|----------|
| 1k          |     7.06 |
| ±           |          |
| 0.5         |     6.58 |
| ±           |          |
| 0.4         |     6.69 |
| ±           |          |
| 0.8         |          |
| 7.29        |          |
| ±           |          |
| 0.7         |          |
| 6.93        |          |
| ±           |          |
| 0.5         |     7.06 |
| ±           |          |
| 0.7         |          |
| 2k          |    11.7  |
| ±           |          |
| 0.5         |    11.12 |
| ±           |          |
| 0.8         |    11.31 |
| ±           |          |
| 1.0         |    11.62 |
| ±           |          |
| 0.7         |    12.07 |
| ±           |          |
| 0.7         |          |
| 11.86       |          |
| ±           |          |
| 0.9         |          |
| 3k          |          |
| 16.80       |          |
| ±           |          |
| 0.6         |          |
| 16.07       |          |
| ±           |          |
| 1.3         |    16.44 |
| ±           |          |
| 1.0         |    15.95 |
| ±           |          |
| 0.8         |    16.78 |
| ±           |          |
| 0.7         |    16.53 |
| ±           |          |
| 0.8         |          |
| 4k          |          |
| 22.11       |          |
| ±           |          |
| 0.9         |    20.6  |
| ±           |          |
| 0.8         |    20.79 |
| ±           |          |
| 1.1         |    21.12 |
| ±           |          |
| 1.3         |          |
| 21.68       |          |
| ±           |          |
| 1.3         |          |
| 21.60       |          |
| ±           |          |
| 0.8         |          |
| 5k          |    26.05 |
| ±           |          |
| 1.2         |    24.89 |
| ±           |          |
| 1.0         |          |
| 26.45       |          |
| ±           |          |
| 0.8         |          |
| 25.19       |          |
| ±           |          |
| 1.6         |    25.58 |
| ±           |          |
| 1.5         |    25.56 |
| ±           |          |
| 0.7         |          |
| 6k          |    30.8  |
| ±           |          |
| 0.7         |    30.23 |
| ±           |          |
| 1.2         |          |
| 31.27       |          |
| ±           |          |
| 1.4         |          |
| 30.75       |          |
| ±           |          |
| 0.9         |    30.76 |
| ±           |          |
| 1.2         |    30.76 |
| ±           |          |
| 0.4         |          |
| 7k          |    35.47 |
| ±           |          |
| 0.9         |    34.56 |
| ±           |          |
| 0.8         |          |
| 35.71       |          |
| ±           |          |
| 0.5         |          |
| 34.94       |          |
| ±           |          |
| 1.1         |    34.92 |
| ±           |          |
| 0.9         |    35.02 |
| ±           |          |
| 0.4         |          |
| 8k          |    39.04 |
| ±           |          |
| 0.8         |    38.4  |
| ±           |          |
| 0.8         |          |
| 40.99       |          |
| ±           |          |
| 0.7         |          |
| 38.88       |          |
| ±           |          |
| 0.8         |    39.42 |
| ±           |          |
| 0.9         |    39.18 |
| ±           |          |
| 0.4         |          |
| 9k          |    42.32 |
| ±           |          |
| 0.7         |    41.81 |
| ±           |          |
| 1.1         |          |
| 44.30       |          |
| ±           |          |
| 1.6         |          |
| 42.65       |          |
| ±           |          |
| 1.2         |    43.39 |
| ±           |          |
| 0.9         |    42.95 |
| ±           |          |
| 0.4         |          |
| 10k         |    45.73 |
| ±           |          |
| 0.5         |    45    |
| ±           |          |
| 0.9         |          |
| 47.95       |          |
| ±           |          |
| 0.6         |          |
| 47.05       |          |
| ±           |          |
| 0.6         |    47.28 |
| ±           |          |
| 1.3         |    46.9  |
| ±           |          |
| 0.6         |          |
| #labeled   |   500 |
|------------|-------|
| 500        | 41.5  |
| ±          |       |
| 3.3        |       |
| 1k         | 50.22 |
| ±          |       |
| 2.1        |       |
| 50.74      |       |
| ±          |       |
| 2.3        |       |
| 1.5k       |       |
| 57.67      |       |
| ±          |       |
| 1.9        |       |
| 2k         | 63.28 |
| ±          |       |
| 1.5        |       |
| 66.90      |       |
| ±          |       |
| 1.6        |       |
| 65.78      |       |
| ±          |       |
| 1.8        |       |
| 2.5k       | 68.68 |
| ±          |       |
| 1.6        |       |
| 3k         | 72.75 |
| ±          |       |
| 1.5        |       |
| 76.14      |       |
| ±          |       |
| 1.6        |       |
| 3.5k       |       |
| 77.24      |       |
| ±          |       |
| 1.0        |       |
| 4k         | 80.32 |
| ±          |       |
| 0.5        |       |
| 81.3       |       |
| ±          |       |
| 0.5        |       |
| 79.60      |       |
| ±          |       |
| 0.6        |       |
| 4.5k       | 82.19 |
| ±          |       |
| 0.5        |       |
| 5k         | 83.39 |
| ±          |       |
| 0.5        |       |
| 83.59      |       |
| ±          |       |
| 0.5        |       |
| 5.5k       |       |
| 85.04      |       |
| ±          |       |
| 0.5        |       |
| 6k         |       |
| 85.88      |       |
| ±          |       |
| 0.4        |       |
| 86.26      |       |
| ±          |       |
| 0.7        |       |
| 85.70      |       |
| ±          |       |
| 0.5        |       |
| 6.5k       |       |
| 87.24      |       |
| ±          |       |
| 0.3        |       |
| 7k         | 87.65 |
| ±          |       |
| 0.2        |       |
| 87.95      |       |
| ±          |       |
| 0.2        |       |
| 7.5k       |       |
| 88.74      |       |
| ±          |       |
| 0.2        |       |
| 8k         | 89.05 |
| ±          |       |
| 0.2        |       |
| 89.19      |       |
| ±          |       |
| 0.2        |       |
| 88.53      |       |
| ±          |       |
| 0.2        |       |
| 8.5k       | 89.52 |
| ±          |       |
| 0.2        |       |
| 9k         |       |
| 89.92      |       |
| ±          |       |
| 0.2        |       |
| 90.16      |       |
| ±          |       |
| 0.2        |       |
| 9.5k       |       |
| 90.26      |       |
| ±          |       |
| 0.2        |       |
| 10k        | 90.45 |
| ±          |       |
| 0.1        |       |
| 90.89      |       |
| ±          |       |
| 0.2        |       |
| 90.42      |       |
| ±          |       |
| 0.2        |       |
| 10.5k      |       |
| 90.15      |       |
| ±          |       |
| 0.1        |       |
| 11k        | 91.27 |
| ±          |       |
| 0.1        |       |
| 91.65      |       |
| ±          |       |
| 0.2        |       |
| 11.5k      |       |
| 91.95      |       |
| ±          |       |
| 0.1        |       |
| 12k        | 92.09 |
| ±          |       |
| 0.1        |       |
| 92.27      |       |
| ±          |       |
| 0.1        |       |
| 91.91      |       |
| ±          |       |
| 0.1        |       |
| 12.5k      |       |
| 92.35      |       |
| ±          |       |
| 0.1        |       |
| 13k        | 92.5  |
| ±          |       |
| 0.1        |       |
| 92.76      |       |
| ±          |       |
| 0.2        |       |
| 13.5k      | 92.78 |
| ±          |       |
| 0.1        |       |
| 14k        |       |
| 92.65      |       |
| ±          |       |
| 0.1        |       |
| 93.18      |       |
| ±          |       |
| 0.1        |       |
| 92.76      |       |
| ±          |       |
| 0.1        |       |
| 14.5k      | 93.11 |
| ±          |       |
| 0.1        |       |
| 15k        |       |
| 93.22      |       |
| ±          |       |
| 0.1        |       |
| 93.35      |       |
| ±          |       |
| 0.2        |       |
| 15.5k      | 93.25 |
| ±          |       |
| 0.1        |       |
| 16k        | 93.42 |
| ±          |       |
| 0.1        |       |
| 93.67      |       |
| ±          |       |
| 0.1        |       |
| 93.39      |       |
| ±          |       |
| 0.1        |       |
| 16.5k      | 93.42 |
| ±          |       |
| 0.1        |       |
| 17k        | 93.45 |
| ±          |       |
| 0.1        |       |
| 93.89      |       |
| ±          |       |
| 0.1        |       |
| 17.5k      | 93.52 |
| ±          |       |
| 0.0        |       |
| 18k        | 93.82 |
| ±          |       |
| 0.0        |       |
| 94.15      |       |
| ±          |       |
| 0.0        |       |
| 93.61      |       |
| ±          |       |
| 0.0        |       |
| 18.5k      | 93.76 |
| ±          |       |
| 0.0        |       |
| 19k        | 93.82 |
| ±          |       |
| 0.0        |       |
| 94.36      |       |
| ±          |       |
| 0.1        |       |
| 19.5k      | 93.89 |
| ±          |       |
| 0.0        |       |
| 20k        | 93.98 |
| ±          |       |
| 0.0        |       |
| 94.40      |       |
| ±          |       |
| 0.0        |       |
| 93.89      |       |
| ±          |       |
| 0.0        |       |
| #labeled   |   Scratch |
|------------|-----------|
| 1k         |           |
| 50.74      |           |
| ±          |           |
| 0.3        |           |
| 50.66      |           |
| ±          |           |
| 0.9        |           |
| 2k         |           |
| 66.90      |           |
| ±          |           |
| 1.6        |           |
| 63.87      |           |
| ±          |           |
| 0.4        |           |
| 3k         |           |
| 76.14      |           |
| ±          |           |
| 1.6        |           |
| 72.33      |           |
| ±          |           |
| 0.7        |           |
| 4k         |           |
| 81.34      |           |
| ±          |           |
| 0.5        |           |
| 79.27      |           |
| ±          |           |
| 0.7        |           |
| 5k         |           |
| 83.59      |           |
| ±          |           |
| 0.5        |           |
| 82.82      |           |
| ±          |           |
| 0.3        |           |
| 6k         |           |
| 86.26      |           |
| ±          |           |
| 0.7        |           |
| 85.68      |           |
| ±          |           |
| 0.2        |           |
| 7k         |           |
| 87.95      |           |
| ±          |           |
| 0.2        |           |
| 87.46      |           |
| ±          |           |
| 0.1        |           |
| 8k         |           |
| 89.19      |           |
| ±          |           |
| 0.2        |           |
| 88.90      |           |
| ±          |           |
| 0.2        |           |
| 9k         |           |
| 90.16      |           |
| ±          |           |
| 0.2        |           |
| 89.76      |           |
| ±          |           |
| 0.3        |           |
| 10k        |           |
| 90.89      |           |
| ±          |           |
| 0.2        |           |
| 90.85      |           |
| ±          |           |
| 0.1        |           |
| 11k        |           |
| 91.65      |           |
| ±          |           |
| 0.2        |           |
| 91.43      |           |
| ±          |           |
| 0.2        |           |
| 12k        |           |
| 92.27      |           |
| ±          |           |
| 0.1        |           |
| 92.06      |           |
| ±          |           |
| 0.1        |           |
| 13k        |           |
| 92.76      |           |
| ±          |           |
| 0.2        |           |
| 92.5       |           |
| ±          |           |
| 0.1        |           |
| 14k        |           |
| 93.18      |           |
| ±          |           |
| 0.1        |           |
| 93.10      |           |
| ±          |           |
| 0.1        |           |
| 15k        |           |
| 93.35      |           |
| ±          |           |
| 0.2        |           |
| 93.26      |           |
| ±          |           |
| 0.2        |           |
| 16k        |     93.67 |
| ±          |           |
| 0.1        |           |
| 93.71      |           |
| ±          |           |
| 0.1        |           |
| 17k        |           |
| 93.89      |           |
| ±          |           |
| 0.1        |           |
| 93.77      |           |
| ±          |           |
| 0.1        |           |
| 18k        |           |
| 94.15      |           |
| ±          |           |
| 0.0        |           |
| 93.98      |           |
| ±          |           |
| 0.1        |           |
| 19k        |           |
| 94.36      |           |
| ±          |           |
| 0.1        |           |
| 94.33      |           |
| ±          |           |
| 0.2        |           |
| 20k        |           |
| 94.40      |           |
| ±          |           |
| 0.0        |     94.4  |
| ±          |           |
| 0.1        |           |
| #labeled   |   Random |
|------------|----------|
| 1k         |          |
| 51.79      |          |
| ±          |          |
| 0.7        |          |
| 50.74      |          |
| ±          |          |
| 2.3        |    51.3  |
| ±          |          |
| 2.0        |          |
| 2k         |    65.49 |
| ±          |          |
| 0.7        |          |
| 66.90      |          |
| ±          |          |
| 1.6        |          |
| 65.43      |          |
| ±          |          |
| 1.0        |          |
| 3k         |    73.7  |
| ±          |          |
| 0.9        |          |
| 76.15      |          |
| ±          |          |
| 0.5        |          |
| 75.86      |          |
| ±          |          |
| 1.6        |          |
| 4k         |          |
| 78.66      |          |
| ±          |          |
| 1.3        |          |
| 81.35      |          |
| ±          |          |
| 0.5        |          |
| 79.29      |          |
| ±          |          |
| 0.6        |          |
| 5k         |    81.06 |
| ±          |          |
| 1.0        |          |
| 83.59      |          |
| ±          |          |
| 0.6        |          |
| 82.87      |          |
| ±          |          |
| 0.2        |          |
| 6k         |          |
| 83.52      |          |
| ±          |          |
| 0.7        |          |
| 86.26      |          |
| ±          |          |
| 0.7        |          |
| 86.20      |          |
| ±          |          |
| 0.4        |          |
| 7k         |    85.02 |
| ±          |          |
| 1.0        |          |
| 87.95      |          |
| ±          |          |
| 0.3        |          |
| 87.83      |          |
| ±          |          |
| 0.3        |          |
| 8k         |    86.11 |
| ±          |          |
| 0.7        |          |
| 89.20      |          |
| ±          |          |
| 0.2        |          |
| 89.17      |          |
| ±          |          |
| 0.2        |          |
| 9k         |    87.16 |
| ±          |          |
| 0.7        |          |
| 90.16      |          |
| ±          |          |
| 0.2        |          |
| 90.20      |          |
| ±          |          |
| 0.2        |          |
| 10k        |    87.64 |
| ±          |          |
| 0.5        |          |
| 90.90      |          |
| ±          |          |
| 0.2        |          |
| 90.75      |          |
| ±          |          |
| 0.2        |          |
| 11k        |    88.51 |
| ±          |          |
| 0.6        |          |
| 91.66      |          |
| ±          |          |
| 0.3        |          |
| 91.65      |          |
| ±          |          |
| 0.1        |          |
| 12k        |    89.17 |
| ±          |          |
| 0.6        |          |
| 92.28      |          |
| ±          |          |
| 0.1        |          |
| 93.38      |          |
| ±          |          |
| 0.2        |          |
| 13k        |    89.67 |
| ±          |          |
| 0.5        |          |
| 92.77      |          |
| ±          |          |
| 0.2        |          |
| 92.78      |          |
| ±          |          |
| 0.4        |          |
| 14k        |    89.98 |
| ±          |          |
| 0.6        |          |
| 93.18      |          |
| ±          |          |
| 0.2        |          |
| 93.15      |          |
| ±          |          |
| 0.1        |          |
| 15k        |    90.37 |
| ±          |          |
| 0.5        |          |
| 93.36      |          |
| ±          |          |
| 0.2        |          |
| 93.32      |          |
| ±          |          |
| 0.3        |          |
| 16k        |    90.9  |
| ±          |          |
| 0.4        |          |
| 93.67      |          |
| ±          |          |
| 0.2        |          |
| 93.67      |          |
| ±          |          |
| 0.2        |          |
| 17k        |    91.06 |
| ±          |          |
| 0.6        |          |
| 93.89      |          |
| ±          |          |
| 0.1        |          |
| 93.97      |          |
| ±          |          |
| 0.1        |          |
| 18k        |    91.39 |
| ±          |          |
| 0.5        |          |
| 94.16      |          |
| ±          |          |
| 0.1        |          |
| 94.15      |          |
| ±          |          |
| 0.0        |          |
| 19k        |    91.6  |
| ±          |          |
| 0.4        |          |
| 94.37      |          |
| ±          |          |
| 0.2        |          |
| 94.28      |          |
| ±          |          |
| 0.1        |          |
| 20k        |    91.86 |
| ±          |          |
| 0.4        |          |
| 94.40      |          |
| ±          |          |
| 0.1        |          |
| 94.31      |          |
| ±          |          |
| 0.1        |          |
| #labeled   |   Random |
|------------|----------|
| 1k         |    49.98 |
| ±          |          |
| 1.2        |          |
| 49.98      |          |
| ±          |          |
| 1.8        |          |
| 49.98      |          |
| ±          |          |
| 1.4        |          |
| 2k         |          |
| 65.10      |          |
| ±          |          |
| 1.0        |          |
| 65.70      |          |
| ±          |          |
| 1.4        |          |
| 58.72      |          |
| ±          |          |
| 1.0        |          |
| 3k         |    70.99 |
| ±          |          |
| 1.0        |          |
| 74.00      |          |
| ±          |          |
| 0.8        |          |
| 66.45      |          |
| ±          |          |
| 0.7        |          |
| 4k         |    78.2  |
| ±          |          |
| 1.0        |          |
| 80.59      |          |
| ±          |          |
| 0.8        |          |
| 72.93      |          |
| ±          |          |
| 0.9        |          |
| 5k         |          |
| 79.19      |          |
| ±          |          |
| 0.8        |          |
| 82.79      |          |
| ±          |          |
| 0.7        |          |
| 75.63      |          |
| ±          |          |
| 0.7        |          |
| 6k         |    82.92 |
| ±          |          |
| 0.7        |          |
| 84.96      |          |
| ±          |          |
| 0.7        |          |
| 79.98      |          |
| ±          |          |
| 0.6        |          |
| 7k         |    84.88 |
| ±          |          |
| 0.8        |          |
| 87.31      |          |
| ±          |          |
| 0.5        |          |
| 81.32      |          |
| ±          |          |
| 0.6        |          |
| 8k         |    85.84 |
| ±          |          |
| 0.6        |          |
| 89.07      |          |
| ±          |          |
| 0.4        |          |
| 83.61      |          |
| ±          |          |
| 0.5        |          |
| 9k         |    87.08 |
| ±          |          |
| 0.5        |          |
| 89.66      |          |
| ±          |          |
| 0.4        |          |
| 85.04      |          |
| ±          |          |
| 0.4        |          |
| 10k        |          |
| 87.28      |          |
| ±          |          |
| 0.4        |          |
| 90.36      |          |
| ±          |          |
| 0.3        |          |
| 86.04      |          |
| ±          |          |
| 0.4        |          |
| 11k        |    88.48 |
| ±          |          |
| 0.5        |          |
| 90.87      |          |
| ±          |          |
| 0.4        |          |
| 86.79      |          |
| ±          |          |
| 0.4        |          |
| 12k        |    88.58 |
| ±          |          |
| 0.4        |          |
| 91.78      |          |
| ±          |          |
| 0.2        |          |
| 87.83      |          |
| ±          |          |
| 0.4        |          |
| 13k        |    89.26 |
| ±          |          |
| 0.4        |          |
| 92.08      |          |
| ±          |          |
| 0.3        |          |
| 88.01      |          |
| ±          |          |
| 0.4        |          |
| 14k        |    89.85 |
| ±          |          |
| 0.4        |          |
| 92.7       |          |
| ±          |          |
| 0.3        |          |
| 89.23      |          |
| ±          |          |
| 0.4        |          |
| 15k        |    89.87 |
| ±          |          |
| 0.4        |          |
| 92.9       |          |
| ±          |          |
| 0.3        |          |
| 89.27      |          |
| ±          |          |
| 0.4        |          |
| 16k        |    90.17 |
| ±          |          |
| 0.4        |          |
| 93.36      |          |
| ±          |          |
| 0.3        |          |
| 90.35      |          |
| ±          |          |
| 0.3        |          |
| 17k        |          |
| 90.69      |          |
| ±          |          |
| 0.4        |          |
| 93.56      |          |
| ±          |          |
| 0.3        |          |
| 90.47      |          |
| ±          |          |
| 0.3        |          |
| 18k        |    91.04 |
| ±          |          |
| 0.3        |          |
| 93.82      |          |
| ±          |          |
| 0.2        |          |
| 90.98      |          |
| ±          |          |
| 0.3        |          |
| 19k        |    90.99 |
| ±          |          |
| 0.3        |          |
| 93.94      |          |
| ±          |          |
| 0.2        |          |
| 91.63      |          |
| ±          |          |
| 0.3        |          |
| 20k        |          |
| 91.28      |          |
| ±          |          |
| 0.3        |          |
| 93.95      |          |
| ±          |          |
| 0.2        |          |
| 91.53      |          |
| ±          |          |
| 0.3        |          |
| #labeled   |   Random |
|------------|----------|
| 1k         |    49.82 |
| ±          |          |
| 1.1        |          |
| 49.82      |          |
| ±          |          |
| 1.2        |          |
| 49.82      |          |
| ±          |          |
| 1.3        |          |
| 2k         |    64.43 |
| ±          |          |
| 0.8        |          |
| 65.18      |          |
| ±          |          |
| 0.9        |          |
| 51.89      |          |
| ±          |          |
| 1.0        |          |
| 3k         |    72.65 |
| ±          |          |
| 0.7        |          |
| 75.21      |          |
| ±          |          |
| 0.7        |          |
| 59.43      |          |
| ±          |          |
| 0.7        |          |
| 4k         |          |
| 77.6       |          |
| ±          |          |
| 0.7        |          |
| 77.93      |          |
| ±          |          |
| 0.7        |          |
| 56.86      |          |
| ±          |          |
| 0.7        |          |
| 5k         |    81.03 |
| ±          |          |
| 0.6        |          |
| 82.76      |          |
| ±          |          |
| 0.6        |          |
| 55.78      |          |
| ±          |          |
| 0.6        |          |
| 6k         |          |
| 83.00      |          |
| ±          |          |
| 0.6        |          |
| 85.30      |          |
| ±          |          |
| 0.6        |          |
| 62.61      |          |
| ±          |          |
| 0.6        |          |
| 7k         |    84.62 |
| ±          |          |
| 0.5        |          |
| 87.13      |          |
| ±          |          |
| 0.5        |          |
| 65.42      |          |
| ±          |          |
| 0.5        |          |
| 8k         |    85.72 |
| ±          |          |
| 0.4        |          |
| 88.33      |          |
| ±          |          |
| 0.4        |          |
| 67.20      |          |
| ±          |          |
| 0.4        |          |
| 9k         |    86.42 |
| ±          |          |
| 0.4        |          |
| 89.57      |          |
| ±          |          |
| 0.4        |          |
| 73.00      |          |
| ±          |          |
| 0.4        |          |
| 10k        |    87.15 |
| ±          |          |
| 0.3        |          |
| 90.76      |          |
| ±          |          |
| 0.3        |          |
| 74.99      |          |
| ±          |          |
| 0.3        |          |
| 11k        |    88.66 |
| ±          |          |
| 0.3        |          |
| 91.12      |          |
| ±          |          |
| 0.3        |          |
| 75.89      |          |
| ±          |          |
| 0.3        |          |
| 12k        |    88.7  |
| ±          |          |
| 0.3        |          |
| 91.99      |          |
| ±          |          |
| 0.3        |          |
| 79.26      |          |
| ±          |          |
| 0.3        |          |
| 13k        |    89    |
| ±          |          |
| 0.3        |          |
| 92.36      |          |
| ±          |          |
| 0.3        |          |
| 71.82      |          |
| ±          |          |
| 0.3        |          |
| 14k        |    89.55 |
| ±          |          |
| 0.3        |          |
| 92.68      |          |
| ±          |          |
| 0.3        |          |
| 80.90      |          |
| ±          |          |
| 0.3        |          |
| 15k        |    89.74 |
| ±          |          |
| 0.3        |          |
| 92.78      |          |
| ±          |          |
| 0.3        |          |
| 82.25      |          |
| ±          |          |
| 0.3        |          |
| 16k        |    90.15 |
| ±          |          |
| 0.2        |          |
| 92.94      |          |
| ±          |          |
| 0.2        |          |
| 82.36      |          |
| ±          |          |
| 0.2        |          |
| 17k        |    90.24 |
| ±          |          |
| 0.3        |          |
| 93.02      |          |
| ±          |          |
| 0.3        |          |
| 83.78      |          |
| ±          |          |
| 0.3        |          |
| 18k        |    91.13 |
| ±          |          |
| 0.2        |          |
| 93.67      |          |
| ±          |          |
| 0.2        |          |
| 83.60      |          |
| ±          |          |
| 0.2        |          |
| 19k        |    90.91 |
| ±          |          |
| 0.2        |          |
| 93.75      |          |
| ±          |          |
| 0.2        |          |
| 83.64      |          |
| ±          |          |
| 0.2        |          |
| 20k        |    91.69 |
| ±          |          |
| 0.2        |          |
| 93.92      |          |
| ±          |          |
| 0.2        |          |
| 83.99      |          |
| ±          |          |
| 0.2        |          |
| #labeled   |   Random |
|------------|----------|
| 2k         |    60.95 |
| ±          |          |
| 0.2        |    61.23 |
| ±          |          |
| 0.6        |    60.95 |
| ±          |          |
| 0.6        |          |
| 62.36      |          |
| ±          |          |
| 0.5        |          |
| 61.23      |          |
| ±          |          |
| 0.4        |    60.89 |
| ±          |          |
| 0.5        |          |
| 3k         |    64.18 |
| ±          |          |
| 0.2        |    64.57 |
| ±          |          |
| 0.4        |    64.91 |
| ±          |          |
| 0.5        |          |
| 65.90      |          |
| ±          |          |
| 0.5        |          |
| 64.64      |          |
| ±          |          |
| 0.3        |    64.24 |
| ±          |          |
| 0.3        |          |
| 4k         |          |
| 66.39      |          |
| ±          |          |
| 0.2        |    66.94 |
| ±          |          |
| 0.2        |    66.9  |
| ±          |          |
| 0.3        |          |
| 67.63      |          |
| ±          |          |
| 0.2        |          |
| 66.92      |          |
| ±          |          |
| 0.2        |    67.12 |
| ±          |          |
| 0.2        |          |
| 5k         |    67.46 |
| ±          |          |
| 0.3        |    68.7  |
| ±          |          |
| 0.2        |          |
| 69.05      |          |
| ±          |          |
| 0.2        |          |
| 68.88      |          |
| ±          |          |
| 0.2        |    68.12 |
| ±          |          |
| 0.2        |    68.04 |
| ±          |          |
| 0.2        |          |
| 6k         |    68.58 |
| ±          |          |
| 0.4        |    69.82 |
| ±          |          |
| 0.3        |          |
| 70.35      |          |
| ±          |          |
| 0.2        |          |
| 69.74      |          |
| ±          |          |
| 0.2        |    68.95 |
| ±          |          |
| 0.2        |    68.87 |
| ±          |          |
| 0.2        |          |
| 7k         |    69.17 |
| ±          |          |
| 0.2        |    70.48 |
| ±          |          |
| 0.2        |          |
| 70.49      |          |
| ±          |          |
| 0.2        |          |
| 70.16      |          |
| ±          |          |
| 0.2        |    69.43 |
| ±          |          |
| 0.1        |    69.26 |
| ±          |          |
| 0.2        |          |
| #labeled   |   Random |
|------------|----------|
| 2k         |    63.12 |
| ±          |          |
| 0.2        |          |
| 63.18      |          |
| ±          |          |
| 0.2        |          |
| 63.15      |          |
| ±          |          |
| 0.2        |          |
| 3k         |    67.08 |
| ±          |          |
| 0.1        |          |
| 67.44      |          |
| ±          |          |
| 0.1        |          |
| 67.42      |          |
| ±          |          |
| 0.1        |          |
| 4k         |          |
| 69.44      |          |
| ±          |          |
| 0.1        |    70.22 |
| ±          |          |
| 0.1        |          |
| 70.42      |          |
| ±          |          |
| 0.1        |          |
| 5k         |    71.13 |
| ±          |          |
| 0.2        |          |
| 72.28      |          |
| ±          |          |
| 0.1        |          |
| 72.33      |          |
| ±          |          |
| 0.1        |          |
| 6k         |    72.18 |
| ±          |          |
| 0.1        |          |
| 73.56      |          |
| ±          |          |
| 0.1        |          |
| 73.28      |          |
| ±          |          |
| 0.2        |          |
| 7k         |          |
| 73.10      |          |
| ±          |          |
| 0.1        |    74.81 |
| ±          |          |
| 0.1        |          |
| 74.85      |          |
| ±          |          |
| 0.1        |          |
| #labeled   |   Random |
|------------|----------|
| 250        |    87.58 |
| ±          |          |
| 0.2        |    88.85 |
| ±          |          |
| 0.2        |          |
| 89.97      |          |
| ±          |          |
| 0.3        |          |
| 500        |    90.37 |
| ±          |          |
| 0.1        |    90.89 |
| ±          |          |
| 0.2        |          |
| 91.57      |          |
| ±          |          |
| 0.2        |          |
| 1k         |    91.76 |
| ±          |          |
| 0.1        |    92.47 |
| ±          |          |
| 0.2        |          |
| 92.87      |          |
| ±          |          |
| 0.1        |          |
| 2k         |    92.78 |
| ±          |          |
| 0.1        |    93.27 |
| ±          |          |
| 0.2        |          |
| 93.74      |          |
| ±          |          |
| 0.2        |          |
| 4k         |    93.38 |
| ±          |          |
| 0.1        |    93.97 |
| ±          |          |
| 0.1        |          |
| 94.23      |          |
| ±          |          |
| 0.1        |          |
