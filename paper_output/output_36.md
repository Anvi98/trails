# Early Period Of Training Impacts Out-Of-Distribution Generalization

Chen Cecilia Liu, Iryna Gurevych Ubiquitous Knowledge Processing Lab, Department of Computer Science, Hessian Center for AI (hessian.AI), Technical University of Darmstadt

## Abstract

Prior research has found that differences in the early period of neural network training significantly impact the performance of in-distribution (ID) tasks. However, neural networks are often sensitive to out-of-distribution (OOD) data, making them less reliable in downstream applications. Yet, the impact of the early training period on OOD generalization remains understudied due to its complexity and lack of effective analytical methodologies. In this work, we investigate the relationship between learning dynamics and OOD generalization during the early period of neural network training. We utilize the trace of Fisher Information and sharpness, with a focus on gradual unfreezing (i.e. progressively unfreezing parameters during training) as the methodology for investigation. Through a series of empirical experiments, we show that 1) selecting the number of trainable parameters at different times during training, i.e. realized by gradual unfreezing - has a minuscule impact on ID results, but greatly affects the generalization to OOD data; 2) the absolute values of sharpness and trace of Fisher Information at the initial period of training are not indicative for OOD generalization, but the relative values could be; 3) the trace of Fisher Information and sharpness may be used as indicators for the removal of interventions during early period of training for better OOD generalization.

## 1 Introduction

While deep neural networks have achieved impressive results in their training tasks, they are often sensitive to distribution shifts (i.e. out-of-distribution, OOD) during inference. As in many applications of deep neural networks, the training and testing data may come from different distributions, such as training with perfect images or texts but inference with noise-corrupted data [21, 46], data obtained from different time periods [37, 58], or across different languages and domains [55, 54, 40, 34, 19], to name a few. Failure to generalize to the OOD setting degrades the models' robustness and reliability.

A plethora of research has found that differences in the early period of training have a significant impact on the in-distribution (ID) performance [17, 1, 47, 15, inter alia] for a wide range of settings.

These settings include classification, multimodal learning, training from scratch, parameter-efficient fine-tuning or even federated learning. The wide observation of such a period in machine learning applications suggests that the early period of learning is generally important for neural network training [33], which is sometimes analogous to biological processes (such as the critical learning period in animals [1, 32]). In particular, prior literature identifies that modifications (or interventions) to the optimization process are critical ways to shape the early period of training. Training techniques such as weight decay [17], learning rates [27, 47], data augmentations [17, 42] (such as with MixUp [61]) or adding noise to weights [16] impact learning dynamics early on, and can significantly improve or hamper the final task results depending on the time of application or removal. Yet, there is very limited work exploring how the early period of training impacts generalization to OOD data during testing, as well as "when"
the early period of training significantly affects the outcome of final (OOD) results. [41] found that using gradual unfreezing [24] (i.e., progressively releasing trainable parameters during training at fixed time intervals) can impact the trace of Fisher Information in the early period of training; however, the work was focused on which parameters to select for better cross-lingual transfer (where cross-lingual transfer is a form of natural OOD generalization). Besides the trace of Fisher Information, other sharpness metrics have also been used to study the generalization of network training, especially after the success of methods such as Sharpness-Aware Minimization
(SAM) [14, 36, 62], however, sharpness is less used in prior work to study the early period of training.

In this work, we delve deeper and advance our understanding of how the early period of training impacts OOD generalization through a series of empirical investigations. We first employ gradual unfreezing [24] as a method to intervene in the dynamics of the early period of training from scratch for OOD generalization and investigate how the early period of training impacts OOD generalization.

This is done in a simple and controlled setting. Next, we investigate which metrics are effective for studying the early period of training for OOD generalization. Here, we utilize Fisher Information and sharpness and show how these metrics change in the early period of training with gradual unfreezing, and examine their impact on the final solutions. After this, we focus on whether there is an optimal time (i.e. "when") to remove intervention to achieve a good trade-off between ID and OOD generalization. Along the way, we also try to answer the questions: how early does the "early period" begin and can our observations extend to other settings without gradual unfreezing or with different model architectures?

To summarize, in this paper, we show that 1) when considering the number of trainable parameters at a time, i.e. realized by gradual unfreezing - has a minuscule impact on ID results, but greatly affects the generalization on OOD data; 2) we also show that the value of sharpness and trace of Fisher Information during the initial period of training are not indicative for OOD generalization, but their relative values could be; 3) the trace of Fisher Information and sharpness may signify the removal of interventions during the early period of training.

## 2 Related Work

Early period of neural network training. Under the standard usage of the term generalization
(in-distribution, where training and testing data are assumed to be from the same distribution), prior work [17] shows that the early period of training of neural networks exhibits a "critical learning period" when trained from scratch. Regularization and interventions applied in this critical period affect final task results. [27] indicates that when learning with a lower learning rate, Fisher Information exhibits an "explosion"
which impedes generalization. Applying regularization to the trace of Fisher Information alleviates the negative impact of the high Fisher Information. [42] shows the termination of MixUp early in training and switching to standard empirical risk minimization helps with better ID generalization. [60, 16] shows that even winning "lottery tickets" emerge in the early period of training with large learning rates. The critical learning period is also found in many other settings, such as in multimodal models [32], in linear models [33], in transformers [47] and Federated learning [57]. However, prior work focuses on in-distribution generalization, ignoring the setting of OOD generalization.

[41] shows the early period of training relates to cross-lingual transfer performance in the parameterefficient fine-tuning (PEFT) setting with transformer models, connecting the early period of training with progressive parameter unfreezing and OOD generalization (as cross-lingual data are naturallyoccurring OOD data). We utilize findings in [41] and base our work on gradual unfreezing [24]. In this paper, we focus on 1) a general setup (i.e. training from scratch), and 2) the characterization of the early period of training and its relationship to OOD generalization.

Fisher Information, sharpness and generalization. Fisher Information has been studied in many prior works such as [5, 45] to investigate and improve optimization behaviour. Similarly, sharpness is another popular metric used to study optimization behaviour and its relationship to generalization.

[28] found a correlation between sharpness and the ratio of learning rate to batch size. [29, 11, 49] give theoretical guarantees on the generalization error using sharpness-related measures and conduct large empirical experiments showing that sharpness-based measures correlate with generalization. However, there have been debates on whether sharp minima (such as a high largest eigenvalue of the training Hessian, λmax) imply poor generalization [9] and demonstrate the limits of λmax in explaining in-distribution generalization [30]. Most of the current research efforts are towards analyzing the loss landscape at convergence, for in-distribution generalization. For OOD, [2] shows adaptive sharpness is not a stable measurement for OOD generalization of the final solution. However, the relationship between metrics such as Fisher Information, sharpness and OOD generalization in the early period of training is unclear.

## 3 Preliminaries 3.1 Fisher Information Matrix (Fim)

To investigate the training process, we first look at the Fisher Information [13]. Fisher Information reflects the local curvature and measures the amount of information with respect to network parameters, i.e. how sensitive the network predictions are to the changes in parameters. A larger Fisher Information indicates that a small change in network parameters can change the output significantly, which can be interpreted as a "sharper" loss landscape.

Let x be the inputs and y be the labels of a dataset D. Given a neural network that is parameterized by w. The Fisher Information is defined as:

$$F(w)=\mathbb{E}_{P_{x,y}}\left[\nabla_{w}\log p_{w}(\hat{y}|x)\nabla_{w}\log p_{w}(\hat{y}|x)^{T}\right].\tag{1}$$

Estimating the full Fisher Information is usually expensive, prior work shows that the trace of the Fisher Information ($\texttt{tr}(\text{F})$) correlates well with the full Fisher Information and can be used for real applications and capture signals during the learning process [1, 27, 53, inter alia]. Using the empirical data distribution $\hat{Q}(x)$:

$$\texttt{tr}(\text{F})=\mathbb{E}_{x\sim\hat{Q}(x)}\,\mathbb{E}_{\hat{y}\sim p_{w}(\hat{y}|x)}\,||\nabla_{w}\log p_{w}(\hat{y}|x)||^{2}.\tag{2}$$

## 3.2 Sharpness

Let $\mathcal{L}_{P}(w)=\frac{1}{|D|}\sum_{(x,y)\in D}\log p_{w}(y|x)$ be the loss over training datasets of a neural network parameterized by $w$, and $\delta$ be a small perturbation drawn from a noise distribution, such as a Gaussian distribution $\mathcal{N}(0,\rho^{2}diag(c^{2}))$. The definition of worst-case and average-case sharpness are [14, 36, 2, 22]:

$$S^{\rho}_{avg}=\mathbb{E}_{\delta\sim\mathcal{N}(0,\rho^{2}diag(c^{2}))}\,\mathcal{L}_{D}(w-\delta)-\mathcal{L}_{D}(w),\tag{3}$$

$$S^{\rho}_{worst}=\max_{\|\delta\|c^{-1}\|_{p}\leq\rho}\,\mathcal{L}_{D}(w-\delta)-\mathcal{L}_{D}(w),\tag{4}$$

where $\odot c^{-1}$ is element-wise multiplication.

The sharpness here refers to how rapidly the loss changes with respect to the changes in the model parameters.1 While both the Fisher Information and sharpness are used for investigating loss landscapes and generalization, they offer different views of the training process. Both Sρ
avg and Sρ
worst are studied in the prior literature for generalization. For instance, [29, 10, 36]
show that the worst-case sharpness correlates better with generalization, at convergence. While prior work believe that flatter (less sharp) minima in the loss landscape lead to better generalization in neural networks [22, 31, 26, 4], these metrics' attribution to the early period of training and how their early period trends are related to OOD generalization is understudied.

## 3.3 Gradual Unfreezing

Gradual unfreezing [24] is a simple tuning method that progressively increases the number of trainable parameters (i.e. unfreeze, layer-by-layer) of the neural network from the top to the bottom of the network with a fixed interval of training steps, k (i.e. the unfreezing time). In this paper, we used a modified formulation of gradual unfreezing [41], where we progressively unfreeze the parameters during the early period in the training top-down and for "blocks" of parameters (a block of parameters can be a single layer or several consecutive layers, in our case, we use the namespace of the parameters used in standard implementations to determine blocks). See Appendix A for details and the algorithm.

## 4 Experimental Setup

To investigate our research questions, we perform two sets of experiments. First in a controlled setup, with datasets such as CIFAR10 [35] and models such as ResNet [20] to observe patterns and validate our hypothesis. Then, we experiment with the complex setup with transformer models. We use ρ = 0.01 to calculate the sharpness (both average-case and worst-case) with 15 samples, and L2
norm for the worst-case sharpness. We normalize the tr(F) by the number of trainable parameters.

We use the Auto-PGD algorithm [8] as implemented in [2] (we refer the readers to the original papers for details) for computing worst-case sharpness, as it is a hyperparameter-free estimation method.

Controlled Setup.

In this setup, following [21], we use ResNet-18 and VGG-11 as the neural networks for this study (training from scratch). We perform experiments on classic image classification datasets and use MNIST [38], CIFAR10 [35] and CIFAR100 [35] for training. For out-of-distribution evaluation, we use the corrupted corresponding evaluation datasets, named MNIST-C [48], CIFAR10- C [21] and CIFAR-100-C [21] (results averaged across corruptions and severities). The ID evaluation sets are the original test sets respectively.

We use the SGD optimizer and the CIFAR datasets are applied with standard augmentations (i.e.

random crops and flips). We report results over 6 random seeds for MNIST (due to the high variance in OOD results), and we use 4 random seeds for other datasets. Other hyperparameters such as learning rate or weight decay are specified in Appendix B. In our experiments, the default learning rate specified in Appendix B is denoted as lrd and we also experimented with reduced learning rates which are 1/10th of the default, specified as 0.1*lrd.

Complex Setup.

We also conduct experiments using transformers. As pre-train then fine-tuning becomes a popular way to adapt general foundational models to downstream tasks, we examine the cross-lingual transfer (train with English data, test with other languages) task using parameterefficient fine-tuning (PEFT) with the LoRA [25] adapters (HuggingFace PEFT [44] implementation).

This setting is parallel to our controlled setting because: 1) only English data (i.e. ID data) is used for training and validation (other language data are for testing), this is a natural setting of OOD generalization with parallel evaluation protocol to the image tasks; 2) using LoRA adapters allows us to inject randomly initialized parameters for learning, which is analogous to our controlled setting.

We train with SQuAD [51] (English, question and answering task) and MNLI [56] (English, natural language inference task), and evaluate on XQuAD [3], MLQA [39] and XNLI [7]. We use XLM- RoBERTa [6] as the pre-trained multilingual transformer backbones and AdamW [43] as the optimizer.

We report results across 4 seeds for all experiments in this setting. Please see Appendix B for hyperparameters.

## 5 Gradual Unfreezing In The Early Period Of Training Can Improve Out-Of-Distribution Generalization

Recall from § 2, where gradual unfreezing improved OOD performance for PEFT with transformers. Here, we first validate that gradual unfreezing applied to the early period of training in our controlled setting (training from scratch) could also help OOD generalization. By examining three different datasets and two model architectures in Table 1, progressive parameter unfreezing (i.e. gradual unfreezing) does not influence ID results by a large margin (mostly minor degradation, but can also positively impact the ID results). However, gradual unfreezing has a non-negligible positive impact on the OOD results. This observation is also applicable to different learning rates, although the default (larger) learning rate empirically is better for both ID and OOD for CIFAR datasets. Here, we provide evidence that gradual unfreezing can improve OOD performance when training from scratch even if it was proposed for transfer learning [24], and validate the usability of gradual unfreezing as an intervention for our study.

|             | MNIST RN18   | CIFAR10 RN18   | CIFAR100 RN18   | CIFAR10 VGG11   |
|-------------|--------------|----------------|-----------------|-----------------|
| Method      | ID / OOD     | ID / OOD       | ID / OOD        | ID / OOD        |
| lr          |              |                |                 |                 |
| d           |              |                |                 |                 |
| 99.06/33.36 | 93.32/72.36  | 71.07/45.10    | 88.62/71.63     |                 |
| lr          |              |                |                 |                 |
| d           |              |                |                 |                 |
| + GU        | 98.98/       |                |                 |                 |
| 63.99       |              |                |                 |                 |
| 93.26/      |              |                |                 |                 |
| 72.95       |              |                |                 |                 |
| 71.03/      |              |                |                 |                 |
| 46.34       |              |                |                 |                 |
| 88.53/      |              |                |                 |                 |
| 72.16       |              |                |                 |                 |
| 0.1*        |              |                |                 |                 |
| lr          |              |                |                 |                 |
| d           |              |                |                 |                 |
| 99.26/58.46 | 91.66/71.14  | 69.95/44.59    | 86.93/68.41     |                 |
| 0.1*        |              |                |                 |                 |
| lr          |              |                |                 |                 |
| d           |              |                |                 |                 |
| + GU        | 99.18/       |                |                 |                 |
| 62.51       |              |                |                 |                 |
| 91.51/      |              |                |                 |                 |
| 71.26       |              |                |                 |                 |
| 70.67/      |              |                |                 |                 |
| 46.03       |              |                |                 |                 |
| 87.01/      |              |                |                 |                 |
| 69.45       |              |                |                 |                 |

## 6 Early Period Of Training Impacts Out-Of-Distribution Generalization 6.1 Evidence Of Impact On Out-Of-Distribution Generalization

[17, 1] among others show that for ID generalization, there is a "critical learning period" of the neural network. ID generalization degrades with the delaying application of regularization, as well as the removal of regularization. Using gradual unfreezing, we experimented with different unfreezing steps k (ranging from 1 to equally dividing the total training steps among the number of trainable parameter blocks) to measure its impact on both ID and OOD test results. Indeed (as in Figure 1), it is possible that withholding trainable parameters can influence the OOD generalization as early as after training on a single batch of data. The effect is especially prominent for simpler datasets like MNIST. Prolonging the unfreezing interval of parameters during training initially results in minimal change in the ID test performance with a larger learning rate, subsequently leading to quick deterioration of the ID results. The deterioration of ID results over unfreezing intervals aligns with trends observed in the early stages of training using other interventions, as reported in prior work [17, 1], while the effects on OOD results serve as evidence that the early period of training can impact OOD generalization. Gradual unfreezing casts interesting trends on the OOD generalization and shows the trade-off between ID and OOD generalizations. Before the quick deterioration of ID results, there is a short window where OOD results could be improved. As soon as the ID results start decreasing rapidly, the OOD results first increase, then rapidly decrease for CIFAR10/100 with ResNet, but not in MNIST.

There seems to be a range of k in the early period of training, such that the ID results decayed minimally, but with better OOD results, and we will examine this in more detail in § 6.4.

## 6.2 Learning Dynamics In The Early Period Of Training

Observing Figure 2, by freezing the number of trainable parameters at a time (and gradually unfreezing them), we can induce higher Fisher Information and larger Sρ
avg, Sρ
worst at the beginning of training compared to the standard training procedure, although there is an anomaly in the tr(F) of CIFAR100
with ResNet. In general, the longer we withhold parameters, the higher the level of sharpness and tr(F) we can sustain, unfreezing parameters reduce these metrics.

While there are variations between Sρ
avg, Sρ
worst and tr(F) they are all sensitive to the early period of training and interventions. Sρ
avg shows more consistent trends across datasets and architectures compared to the other two metrics. Due to the randomness in estimating Sρ
avg, Sρ
worst, and tr(F), it is also evident that a single, absolute largest value of these metrics during the early period of training may not be a consistent indication of OOD generalization (or ID generalization, in fact).

This indicates that the discussion for a high or low value of Sρ
                                                               avg, Sρ
                                                                     worst, or tr(F) during the early
period of training should be relative rather than absolute.

Empirically, our findings differed from prior work on ID generalization (such as [27]) that demon-
strates the 'explosion' of tr(F) during the early period of training (due to using a small learning rate)
is harmful. Here, a higher tr(F) induced by parameter freezing does not hurt generalization, in both
ID and OOD. When considering the trainable parameters as a variable, having initial higher sharpness
or tr(F) can be advantageous up to a certain time frame during training. More interestingly, some
sub-figures (such as Figure 2 (f) and (j)) show a rapid increase of sharpness after about 100 training
steps (see the k=750 curve). The tr(F) and sharpness transition from a transient phase to a relatively
stabilized value when withholding parameters for long. Introducing new trainable parameters induces
a quick drop in the corresponding metrics. As a result, the optimization trajectory and learning
mechanism change when manipulating the trainable parameters through unfreezing during the early
period of training (such as the network resorting to higher rank features at the initial learning period,
more details in Appendix E.1).

Overall, these results suggest that while a lower sharpness or tr(F) during the early period of
training may be good for ID generalization, when factoring in the trainable parameters (as also shown
empirically in Table 1), a lower initial sharpness or tr(F) could lead to worse OOD generalization.
This observation applies strictly to the very early period of training, and the eventual reduction of
sharpness or tr(F) after the initial period is still desirable (evident in Figure 1, Figure 2, and work
like SAM [14, 36, 52]). Importantly, while sharpness and tr(F) are effective metrics to study the
early period of training, we need to look at their relative trends for OOD generalization (in fact, also
in ID).

## 6.3 Final Solutions And Out-Of-Distribution Results

Changing the learning dynamics in the early period of training inevitably results in different final solutions. For example with CIFAR10 on ResNet, the largest eigenvalue of the Hessian (λmax, calculated on a subset of training data) of final solutions shows a negative correlation with OOD results
(see Appendix C). However, such a negative correlation is not consistent nor always statistically significant across different setups. Our results complement the findings in [2], which serve as additional evidence of the need for developing new robust metrics and further thorough investigation for OOD generalization.

## 6.4 Learning Dynamics Could Signify The Time Period To Remove Interventions

While the value of tr(F) or sharpness during the initial period of learning (or at the end of learning)
may not be indicative of good OOD generalization in general, they could signify the time to release parameters for minimal ID decay and better OOD results. When unfreezing parameters (Figure 2), we observed that in many cases, those metrics experience a "transient" period (the first 50-100 steps, characterized by rapid growth or drop of the sharpness or tr(F)), followed by a 'stabilization' phase where the rate of change in metric values slows down (unless parameters are released).

Notice that the best range of k for overall best ID and OOD results is after the stabilization of sharpness and tr(F) (in Figure 1 and Figure 2), but not for too long. For instance in Figure 1 (b), although the OOD results improved significantly, the ID results deteriorated drastically after 800-1000 training steps (at least 1 point drop for CIFAR10/100). This observation leads to the conjecture that the best time to remove the intervention (i.e. unfreezing parameters in our case) while keeping reasonable ID results (less than 0.5 points decrease in accuracy) and achieving better OOD results must satisfy two constraints: 1) after the initial rapid change of sharpness or tr(F) (the transient phase), and 2) not too far into the stabilization phase.

The second constraint is self-evident in Figure 1, as a larger k hurts both ID and OOD results. To quickly validate the first constraint, we use MNIST to pick the earliest ending step of the transient period among three metrics (Sρ
worst, Sρ
avg and tr(F)). Then we experiment with 10 different k values each consecutively (10 steps apart) that are smaller or greater than that k value. For the smaller ks, we get 98.93/52.72 as the median ID/OOD results, for the larger ks, we get 98.91/53.54 as the median ID/OOD results, which validates the constraints. The stabilization of examined metrics indicates when to introduce new trainable parameters. Next, we use a heuristic algorithm that satisfies the above-mentioned constraints to determine the stabilization time of the three metrics (we first detect a significant change in metrics, then detect the stabilization point of the metrics, the algorithm is in Appendix D). The OOD results are then compared with with ten random k values per dataset (k ≤ 800) to determine the winning rate (i.e., the percentage of times where the value picked by the algorithm is better than a sampled value), and the results are in Table 2. Empirically, using such an algorithm is better than doing a random hyperparameter search the majority of the time. In most cases, the degradation of ID accuracy is within 0.5 points, except when using the VGG network. Nonetheless, this further validates that the stabilization of Sρ
worst, Sρ
avg and tr(F) could signify the removal of interventions (in our case gradual unfreezing) to trade some ID performance for OOD. While tr(F) shows better results, there isn't a clear winning metric for intervention removal due to: 1) metrics exhibiting high noise during training; and 2) the determined stabilization points from different metrics collide or are very close to each other. We will defer the exploration of more sophisticated algorithms for future work. However, it's worth noting the existence of an optimal time that effectively balances good ID and ODD results.

| MNIST RN18   | CIFAR10 RN18   | CIFAR100 RN18   | WR          | CIFAR10 VGG11   | WR          |
|--------------|----------------|-----------------|-------------|-----------------|-------------|
| Method       | ID / OOD       | ID / OOD        | ID / OOD    | -               | ID / OOD    |
| Standard     | 99.06/33.36    | 93.32/72.36     | 71.07/45.10 | -               | 88.62/71.63 |
| GU           |                |                 |             |                 |             |
| S            |                |                 |             |                 |             |
| ρ            |                |                 |             |                 |             |
| worst        |                |                 |             |                 |             |
| 98.78/52.48  | 93.06/72.75    | 70.68/45.19     | 60%         | 87.69/71.47     | 40%         |
| GU           |                |                 |             |                 |             |
| S            |                |                 |             |                 |             |
| ρ            |                |                 |             |                 |             |
| avg          |                |                 |             |                 |             |
| 98.78/52.48  | 93.02/72.58    | 70.67/45.35     | 60%         | 87.71/          |             |
| 72.37        |                |                 |             |                 |             |
| 100%         |                |                 |             |                 |             |
| GU           |                |                 |             |                 |             |
| tr           |                |                 |             |                 |             |
| (F)          |                |                 |             |                 |             |
| 98.91/       |                |                 |             |                 |             |
| 54.12        |                |                 |             |                 |             |
| 93.02/       |                |                 |             |                 |             |
| 73.56        |                |                 |             |                 |             |
| 70.78/       |                |                 |             |                 |             |
| 45.82        |                |                 |             |                 |             |
| 83%          | 88.40/71.86    | 60%             |             |                 |             |

## 7 Generality Of Findings On The Early Period Of Training 7.1 Higher Initial Sharpness Via Learning Rate

K=200
Using gradual unfreezing is a specific case where high sharpness at the initial learning period could benefit OOD generalizations. A critical question is: is there another way to intervene in the early period of training with higher sharpness, that also positively impacts OOD generalization? Recall that a higher learning rate typically results in lower sharpness
(and a lower learning rate results in higher sharpness, as indicated in
[27]). Based on our findings in the previous sections, we hypothesize that using a lower learning rate at the initial period of learning, then switching to a higher learning rate later (high sharpness to low sharpness), may help OOD generalization (surprisingly, this is exactly a simple form of learning rate warm-up!).

To validate, we use the CIFAR10 dataset on ResNet18 with two learning rates: we initially use 1/10th of the default learning rate, then increase the learning rate to the default value after k steps (i.e.

low-to-high, denoted as lrl2h, and the reverse is lrh2l. k is determined using random hyperparameter search). The results are in Table 3 (an example sharpness profile is in Figure 3, with more details in Appendix E.2); indeed, lrl2h can provide better OOD results (and without degrading ID results). Further, with the learning rate switching step k determined using

Method
ID/OOD
Method
ID/OOD
lrd
93.32/72.36
lrl2h
93.35/72.89
0.1*lrd
91.66/71.14
lrh2l
91.58/71.18

tr(F), Sρ
avg and Sρ
worst, the OOD results are 72.57 and 72.94 (same k for both sharpness metrics)
respectively.

## 7.2 Empirical Validations In Transformers

For our complex experimental setup (described in §4), Figure 4 shows the learning dynamics of XLM-R with MNLI in the early period, withholding trainable parameters increases the sharpness and tr(F), note that in Figure 4 (c) the Sρ
worst value is negative, withholding trainable parameters still increase the Sρ
worst during training based on Eqn. 4 (the learning dynamics for the SQuAD dataset is in Appendix E.3).

Similarly, the results using tr(F) to determine the k for unfreezing is in Table 4 (k values are in Appendix D, results with Sρ
worst / Sρ
avg are in Table 7 in the Appendix) and the winning rate is 80%.

The ID results are not sacrificed in this experimental setting, hence further pointing towards that the stabilization of sharpness and tr(F) could signify 'when' to remove intervention in the early period of training for better OOD generalization.

|             |               | XQuAD         | MLQA       | XNLI        | WR             |
|-------------|---------------|---------------|------------|-------------|----------------|
| Method      | F1- En/X-ling | EM- En/X-ling | F1- X-ling | EM- X-ling  | Acc- En/X-ling |
| Standard    | 82.96/68.72   | 71.39/52.64   | 56.27      | 40.93       | 83.17/71.84    |
| GU          |               |               |            |             |                |
| tr          |               |               |            |             |                |
| (F)         |               |               |            |             |                |
| 83.77/70.70 | 72.33/54.40   | 58.47         | 42.31      | 83.36/72.49 | 80%            |

## 8 Conclusions

In this work, we investigate the early period of training and its impact on out-of-distribution generalization. We demonstrate that using gradual unfreezing to modulate the number of trainable parameters during the early period of training can affect out-of-distribution generalization in various settings, including transformers, and reveal that the number of trainable parameters at a time is an important factor that was missing in the previous literature. We observe different patterns to previous work in in-distribution generalization, where higher sharpness and tr(F) during the early period of training may be beneficial for out-of-distribution generalization. We reveal that metric values during the early period of training may not be indicative of the out-of-distribution generalization, however, they could signify "when" to remove interventions such as gradual unfreezing (or to increase the learning rate,
§7.1) for better results.

The significance of effective training and fine-tuning, along with the growing emphasis on research into techniques that involve modifying only partial parameters of the final model, such as freezing parameters (e.g. Adapters [23, 50, 25] or pruning) or network expansions [59, 12, 18] cannot be overstated. Our empirical investigations highlight the need to develop a more theoretical understanding of the early period of training and OOD generalization, as well as the creation of new theoretical metrics for better indication of OOD generalization.

## 9 Acknowledgement

This work was funded by the German Federal Ministry of Education and Research (BMBF) under the promotional reference 13N15897 (MISRIK).

## References

[1] Alessandro Achille, Matteo Rovere, and Stefano Soatto. Critical learning periods in deep
networks. In 7th International Conference on Learning Representations, ICLR 2019, New
Orleans, LA, USA, May 6-9, 2019, 2019.
[2] Maksym Andriushchenko, Francesco Croce, Maximilian Müller, Matthias Hein, and Nicolas
Flammarion. A modern look at the relationship between sharpness and generalization. In
International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu,
Hawaii, USA, volume 202 of *Proceedings of Machine Learning Research*, pages 840–902.
PMLR, 2023.
[3] Mikel Artetxe, Sebastian Ruder, and Dani Yogatama. On the cross-lingual transferability of
monolingual representations. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 4623–4637, Online, July 2020. Association for Computational
Linguistics.
[4] Junbum Cha, Sanghyuk Chun, Kyungjae Lee, Han-Cheol Cho, Seunghyun Park, Yunsung Lee,
and Sungrae Park. SWAD: domain generalization by seeking flat minima. In Advances in Neural
Information Processing Systems 34: Annual Conference on Neural Information Processing
Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual, pages 22405–22418, 2021.
[5] Pratik Chaudhari, Anna Choromanska, Stefano Soatto, Yann LeCun, Carlo Baldassi, Christian
Borgs, Jennifer T. Chayes, Levent Sagun, and Riccardo Zecchina. Entropy-SGD: Biasing gradient descent into wide valleys. In 5th International Conference on Learning Representations,
ICLR 2017, Toulon, France, April 24-26, 2017, Conference Track Proceedings. OpenReview.net,
2017.
[6] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek,
Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. Unsupervised cross-lingual representation learning at scale. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, ACL 2020, Online, July 5-10, 2020,
pages 8440–8451. Association for Computational Linguistics, 2020.
[7] Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger
Schwenk, and Veselin Stoyanov. XNLI: Evaluating cross-lingual sentence representations. In
Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,
pages 2475–2485, Brussels, Belgium, October-November 2018. Association for Computational Linguistics.
[8] Francesco Croce and Matthias Hein. Reliable evaluation of adversarial robustness with an
ensemble of diverse parameter-free attacks. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event, volume 119 of Proceedings of Machine Learning Research, pages 2206–2216. PMLR, 2020.
[9] Laurent Dinh, Razvan Pascanu, Samy Bengio, and Yoshua Bengio. Sharp minima can generalize
for deep nets. In Proceedings of the 34th International Conference on Machine Learning, ICML
2017, Sydney, NSW, Australia, 6-11 August 2017, volume 70 of Proceedings of Machine
Learning Research, pages 1019–1028. PMLR, 2017.
[10] Gintare Karolina Dziugaite, Alexandre Drouin, Brady Neal, Nitarshan Rajkumar, Ethan Caballero, Linbo Wang, Ioannis Mitliagkas, and Daniel M. Roy. In search of robust measures of generalization. In Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual, 2020.
[11] Gintare Karolina Dziugaite and Daniel M. Roy. Computing nonvacuous generalization bounds
for deep (stochastic) neural networks with many more parameters than training data.
In
Proceedings of the Thirty-Third Conference on Uncertainty in Artificial Intelligence, UAI 2017,
Sydney, Australia, August 11-15, 2017. AUAI Press, 2017.
[12] Utku Evci, Bart van Merrienboer, Thomas Unterthiner, Fabian Pedregosa, and Max Vladymyrov.
GradMax: Growing neural networks using gradient information. In The Tenth International
Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022. Open-
Review.net, 2022.
[13] Rory A. Fisher. Theory of statistical estimation. Mathematical Proceedings of the Cambridge
Philosophical Society, 22:700 - 725, 1925.
[14] Pierre Foret, Ariel Kleiner, Hossein Mobahi, and Behnam Neyshabur. Sharpness-aware minimization for efficiently improving generalization. In 9th International Conference on Learning
Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net, 2021.
[15] Stanislav Fort, Gintare Karolina Dziugaite, Mansheej Paul, Sepideh Kharaghani, Daniel M.
Roy, and Surya Ganguli. Deep learning versus kernel learning: an empirical study of loss landscape geometry and the time evolution of the neural tangent kernel. In Advances in Neural
Information Processing Systems 33: Annual Conference on Neural Information Processing
Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual, 2020.
[16] Jonathan Frankle, David J. Schwab, and Ari S. Morcos. The early phase of neural network
training. In 8th International Conference on Learning Representations, ICLR 2020, Addis
Ababa, Ethiopia, April 26-30, 2020. OpenReview.net, 2020.
[17] Aditya Golatkar, Alessandro Achille, and Stefano Soatto. Time matters in regularizing deep
networks: Weight decay and data augmentation affect early learning dynamics, matter little near convergence. In Advances in Neural Information Processing Systems 32: Annual Conference on
Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver,
BC, Canada, pages 10677–10687. Curran Associates, Inc., 2019.
[18] Xiaotao Gu, Liyuan Liu, Hongkun Yu, Jing Li, Chen Chen, and Jiawei Han. On the transformer growth for progressive BERT training. In Proceedings of the 2021 Conference of the
North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, pages 5174–5180, Online, June 2021. Association for Computational Linguistics.
[19] Ishaan Gulrajani and David Lopez-Paz. In search of lost domain generalization. In 9th
International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May
3-7, 2021. OpenReview.net, 2021.
[20] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition. In 2016 IEEE Conference on Computer Vision and Pattern Recognition, CVPR
2016, Las Vegas, NV, USA, June 27-30, 2016, pages 770–778. IEEE Computer Society, 2016.
[21] Dan Hendrycks and Thomas G. Dietterich. Benchmarking neural network robustness to common
corruptions and perturbations. In 7th International Conference on Learning Representations,
ICLR 2019, New Orleans, LA, USA, May 6-9, 2019. OpenReview.net, 2019.
[22] Sepp Hochreiter and Jürgen Schmidhuber. Flat minima. *Neural computation*, 9(1):1–42, 1997.
[23] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Laroussilhe,
Andrea Gesmundo, Mona Attariyan, and Sylvain Gelly. Parameter-efficient transfer learning
for NLP. In *Proceedings of the 36th International Conference on Machine Learning*, volume 97 of *Proceedings of Machine Learning Research*, pages 2790–2799. PMLR, 09–15 Jun 2019.
[24] Jeremy Howard and Sebastian Ruder. Universal language model fine-tuning for text classification. In Proceedings of the 56th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 328–339, Melbourne, Australia, July 2018. Association for Computational Linguistics.
[25] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In
International Conference on Learning Representations, 2022.
[26] Pavel Izmailov, Dmitrii Podoprikhin, Timur Garipov, Dmitry P. Vetrov, and Andrew Gordon
Wilson. Averaging weights leads to wider optima and better generalization. In Proceedings
of the Thirty-Fourth Conference on Uncertainty in Artificial Intelligence, UAI 2018, Monterey,
California, USA, August 6-10, 2018, pages 876–885. AUAI Press, 2018.
[27] Stanislaw Jastrzebski, Devansh Arpit, Oliver Astrand, Giancarlo B Kerg, Huan Wang, Caiming
Xiong, Richard Socher, Kyunghyun Cho, and Krzysztof J Geras. Catastrophic fisher explosion:
Early phase fisher matrix impacts generalization. In Proceedings of the 38th International
Conference on Machine Learning, volume 139 of *Proceedings of Machine Learning Research*,
pages 4772–4784. PMLR, 18–24 Jul 2021.
[28] Stanislaw Jastrzebski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua
Bengio, and Amos J. Storkey. Three factors influencing minima in SGD. *ArXiv*, abs/1711.04623, 2017.
[29] Yiding Jiang, Behnam Neyshabur, Hossein Mobahi, Dilip Krishnan, and Samy Bengio. Fantastic
generalization measures and where to find them. In 8th International Conference on Learning
Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020. OpenReview.net, 2020.
[30] Simran Kaur, Jeremy Cohen, and Zachary Chase Lipton. On the maximum hessian eigenvalue
and generalization. In Proceedings on "I Can't Believe It's Not Better! - Understanding
Deep Learning Through Empirical Falsification" at NeurIPS 2022 Workshops, volume 187 of
Proceedings of Machine Learning Research, pages 51–65. PMLR, 03 Dec 2023.
[31] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping
Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp minima.
In 5th International Conference on Learning Representations, ICLR 2017, Toulon, France, April
24-26, 2017, Conference Track Proceedings. OpenReview.net, 2017.
[32] Michael Kleinman, Alessandro Achille, and Stefano Soatto. Critical learning periods for
multisensory integration in deep networks. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-24, 2023, pages 24296–24305. IEEE, 2023.
[33] Michael Kleinman, Alessandro Achille, and Stefano Soatto. Critical learning periods emerge
even in deep linear networks. In The Twelfth International Conference on Learning Representations, 2024.
[34] Pang Wei Koh, Shiori Sagawa, Henrik Marklund, Sang Michael Xie, Marvin Zhang, Akshay
Balsubramani, Weihua Hu, Michihiro Yasunaga, Richard Lanas Phillips, Irena Gao, Tony Lee, Etienne David, Ian Stavness, Wei Guo, Berton Earnshaw, Imran S. Haque, Sara M. Beery, Jure Leskovec, Anshul Kundaje, Emma Pierson, Sergey Levine, Chelsea Finn, and Percy Liang.
WILDS: A benchmark of in-the-wild distribution shifts. In Proceedings of the 38th International
Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event, volume 139 of
Proceedings of Machine Learning Research, pages 5637–5664. PMLR, 2021.
[35] Alex Krizhevsky. Learning multiple layers of features from tiny images. 2009. [36] Jungmin Kwon, Jeongseop Kim, Hyunseo Park, and In Kwon Choi. ASAM: adaptive sharpnessaware minimization for scale-invariant learning of deep neural networks. In Proceedings of
the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual
Event, volume 139 of *Proceedings of Machine Learning Research*, pages 5905–5914. PMLR,
2021.
[37] Angeliki Lazaridou, Adhiguna Kuncoro, Elena Gribovskaya, Devang Agrawal, Adam Liska,
Tayfun Terzi, Mai Gimenez, Cyprien de Masson d'Autume, Tomás Kociský, Sebastian Ruder,
Dani Yogatama, Kris Cao, Susannah Young, and Phil Blunsom. Mind the gap: Assessing temporal generalization in neural language models. In Advances in Neural Information Processing
Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS
2021, December 6-14, 2021, virtual, pages 29348–29363, 2021.

[38] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning
applied to document recognition. *Proc. IEEE*, 86(11):2278–2324, 1998.
[39] Patrick Lewis, Barlas Oguz, Ruty Rinott, Sebastian Riedel, and Holger Schwenk. MLQA:
Evaluating cross-lingual extractive question answering. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 7315–7330, Online, July 2020.
Association for Computational Linguistics.
[40] Chen Liu, Gregor Geigle, Robin Krebs, and Iryna Gurevych. FigMemes: A dataset for figurative
language identification in politically-opinionated memes. In Proceedings of the 2022 Conference
on Empirical Methods in Natural Language Processing, EMNLP 2022, Abu Dhabi, United Arab
Emirates, December 7-11, 2022, pages 7069–7086. Association for Computational Linguistics,
2022.
[41] Chen Cecilia Liu, Jonas Pfeiffer, Ivan Vulic, and Iryna Gurevych. Improving generalization of
adapter-based cross-lingual transfer with scheduled unfreezing. *CoRR*, abs/2301.05487, 2023.
[42] Zixuan Liu, Ziqiao Wang, Hongyu Guo, and Yongyi Mao. Over-training with mixup may hurt
generalization. In The Eleventh International Conference on Learning Representations, ICLR
2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net, 2023.
[43] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In 7th International
Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019.
OpenReview.net, 2019.
[44] Sourab Mangrulkar, Sylvain Gugger, Lysandre Debut, Younes Belkada, Sayak Paul, and
Benjamin Bossan. PEFT: state-of-the-art parameter-efficient fine-tuning methods. https:
//github.com/huggingface/peft, 2022.
[45] James Martens and Roger B. Grosse. Optimizing neural networks with kronecker-factored
approximate curvature. In Proceedings of the 32nd International Conference on Machine
Learning, ICML 2015, Lille, France, 6-11 July 2015, volume 37 of JMLR Workshop and
Conference Proceedings, pages 2408–2417. JMLR.org, 2015.
[46] Paul Michel and Graham Neubig. MTNT: A testbed for machine translation of noisy text. In
Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,
pages 543–553, Brussels, Belgium, October-November 2018. Association for Computational Linguistics.
[47] Marius Mosbach, Maksym Andriushchenko, and Dietrich Klakow. On the stability of fine-tuning
BERT: Misconceptions, explanations, and strong baselines. In 9th International Conference on
Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net,
2021.
[48] Norman Mu and Justin Gilmer. MNIST-C: A robustness benchmark for computer vision. *CoRR*,
abs/1906.02337, 2019.
[49] Behnam Neyshabur, Srinadh Bhojanapalli, David McAllester, and Nati Srebro. Exploring
generalization in deep learning. In Advances in Neural Information Processing Systems 30:
Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long
Beach, CA, USA, pages 5947–5956, 2017.
[50] Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Aishwarya Kamath, Ivan Vulic, Sebastian Ruder,
Kyunghyun Cho, and Iryna Gurevych. AdapterHub: A framework for adapting transformers. In
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing:
System Demonstrations, EMNLP 2020 - Demos, Online, November 16-20, 2020, pages 46–54.
Association for Computational Linguistics, 2020.
[51] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. SQuAD: 100,000+ questions for machine comprehension of text. In Proceedings of the 2016 Conference on Empirical
Methods in Natural Language Processing, pages 2383–2392, Austin, Texas, November 2016.
Association for Computational Linguistics.
[52] Tom Sherborne, Naomi Saphra, Pradeep Dasigi, and Hao Peng. TRAM: Bridging trust regions
and sharpness aware minimization. In The Twelfth International Conference on Learning
Representations, 2024.
[53] Yi-Lin Sung, Varun Nair, and Colin Raffel. Training neural networks with fixed sparse masks.
In Advances in Neural Information Processing Systems 34: Annual Conference on Neural
Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual, pages
24193–24205, 2021.
[54] Aarne Talman and Stergios Chatzikyriakidis. Testing the generalization power of neural network
models across NLI benchmarks. In Proceedings of the 2019 ACL Workshop BlackboxNLP:
Analyzing and Interpreting Neural Networks for NLP, pages 85–94, Florence, Italy, August
2019. Association for Computational Linguistics.
[55] Kexin Wang, Nils Reimers, and Iryna Gurevych. TSDAE: Using transformer-based sequential
denoising auto-encoderfor unsupervised sentence embedding learning. In Findings of the Association for Computational Linguistics: EMNLP 2021, pages 671–688, Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics.
[56] Adina Williams, Nikita Nangia, and Samuel R. Bowman. A broad-coverage challenge corpus
for sentence understanding through inference. In Proceedings of the 2018 Conference of the
North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, NAACL-HLT 2018, New Orleans, Louisiana, USA, June 1-6, 2018, Volume 1
(Long Papers), pages 1112–1122. Association for Computational Linguistics, 2018.
[57] Gang Yan, Hao Wang, and Jian Li. Seizing critical learning periods in federated learning. In
Thirty-Sixth AAAI Conference on Artificial Intelligence, AAAI 2022, Thirty-Fourth Conference
on Innovative Applications of Artificial Intelligence, IAAI 2022, The Twelveth Symposium on
Educational Advances in Artificial Intelligence, EAAI 2022 Virtual Event, February 22 - March
1, 2022, pages 8788–8796. AAAI Press, 2022.
[58] Huaxiu Yao, Caroline Choi, Bochuan Cao, Yoonho Lee, Pang Wei Koh, and Chelsea Finn.
Wild-Time: A benchmark of in-the-wild distribution shift over time. In Advances in Neural
Information Processing Systems 35: Annual Conference on Neural Information Processing
Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022.
[59] Jaehong Yoon, Eunho Yang, Jeongtae Lee, and Sung Ju Hwang. Lifelong learning with
dynamically expandable networks. In 6th International Conference on Learning Representations,
ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings.
OpenReview.net, 2018.
[60] Haoran You, Chaojian Li, Pengfei Xu, Yonggan Fu, Yue Wang, Xiaohan Chen, Yingyan Lin,
Zhangyang Wang, and Richard G. Baraniuk. Drawing early-bird tickets: Toward more efficient training of deep networks. In *International Conference on Learning Representations*, 2020.
[61] Hongyi Zhang, Moustapha Cissé, Yann N. Dauphin, and David Lopez-Paz. mixup: Beyond
empirical risk minimization. In 6th International Conference on Learning Representations,
ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings.
OpenReview.net, 2018.
[62] Yaowei Zheng, Richong Zhang, and Yongyi Mao. Regularizing neural networks via adversarial
model perturbation. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR
2021, virtual, June 19-25, 2021, pages 8156–8165. Computer Vision Foundation / IEEE, 2021.

## A Gradual Unfreezing

Following the notations and algorithm in [41], let FORWARD(∗) be the standard forward pass, and BACKWARD(∗) calculates gradients and performs updates for trainable parameters. The modified gradual unfreezing algorithm is in Algorithm 1. In our experiments, we partition the blocks by their natural namespaces, as the following:
ResNet18: The definition block follows the standard implementation of ResNet, with an input convolution layer and a batch norm group together as the additional block. The model parameters are partitioned into 5 blocks, and a classification head.

VGG11: The definition block follows the standard implementation of VGG, with 8 blocks in total.

The classification head consists of 3 linear layers with a ReLU function in between.

## Algorithm 1 Gradual Unfreezing

Require: A model's eventual trainable parameters are partitioned into blocks j ∈ {0*, . . . , L* − 1} parameterized by θj, with a task-specific classification head C, and an unfreezing interval k. A set S of the indices of parameter blocks to unfreeze.

1: Initialize C, θj for all j
2: S ← {C} 3: j ← L − 1
4: **for** i = 1 *. . .* N do 5:
Sample a data batch b ∼ D
6:
if i mod k == 0 and i ≤ kL then
7:
S ← S ∪ {θj}
8:
j ← j − 1
9:
end if
10:
FORWARD(∗)
11:
BACKWARD(S)
12: end for
XLM-RoBERTa + LoRA: The experiment follows [41]. Each parameter block consists of 2 sets of LoRA adapters added to the query and value of the backbone transformer from the same layer. The LoRA parameters are partitioned into 12 blocks, and a classification head, where the classification head and the last layer of LoRA adapters are trainable initially.

## B Hyperparameters

For all our experiments, the hyperparameters are listed in Table 5. We use the default hyperparameters for the AdamW optimizer, except for the learning rate. All other hyperparameters for the transformer experiments follow [41], and we use the HuggingFace PEFT [44] implementations of LoRA.

For calculating Sρ
worst and Sρ
avg, we use L2 norm and ρ = 0.01 with 15 examples. We follow the setup in [2] and use the implementation with 2048 data points from the training data (un-augmented when calculating sharpness metrics) for all experiments. We use a batch size of 256, except for SQuAD (the batch size is 32) for calculating all the metrics. The sharpness and tr(F) are recorded every 10 batches (steps) for all datasets.

| MNIST           | CIFAR10   | CIFAR10   | CIFAR100   | SQuAD   | MNLI   |
|-----------------|-----------|-----------|------------|---------|--------|
| RN18            | RN18      | VGG11     | RN18       | XLM-R   | XLM-R  |
| optimizer       | SGD       | SGD       | SGD        | SGD     | AdamW  |
| lr scheduler    | const.    | const.    | const.     | const.  | linear |
| lr              |           |           |            |         |        |
| d               |           |           |            |         |        |
| 0.01            | 0.1       | 0.15      | 0.01       | 0.0005  | 0.0005 |
| batch size      | 128       | 128       | 128        | 128     | 32     |
| training epochs | 10        | 200       | 200        | 200     | 15     |
| weight decay    | 0.01      | 0         | 0          | 0.0005  | 0.01   |
| momentum        | 0.9       | 0         | 0          | 0.9     | -      |
| LoRA r          | -         | -         | -          | -       | 8      |
| LoRA alpha      | -         | -         | -          | -       | 8      |
| LoRA dropout    | -         | -         | -          | -       | 0.2    |

## C Properties Of The Final Solutions And Ood Results

We plot the final solution's λmax (largest eigenvalue of training data feature), Sρ
worst and Sρ
avg against the OOD test results in Figure 5 respectively.

While in general the sharpness measures and OOD have negative correlations (i.e. the smaller sharpness values the better, especially Sρ
worst has a consistent negative correlation), they are not always statistically significant (e.g., for MNIST). The learning rate has a big impact on the final solutions' sharpness. Furthermore, such as in Figure 5 (c), we can even attain slightly positive correlations. Our results complement the findings in [2], which serve as evidence pointing towards the need for developing robust new metrics and thorough investigation for OOD generalization.

## D Algorithm To Determine The Unfreeze Time

To verify our hypothesis, we use a simple algorithm with heuristic to determine the unfreezing time k, Algorithm 2 presents the flow, τ is 3 or 8 and ϵ is 0.02 (i.e. the percentage of change in the signal is within 2%). The algorithm takes t∆ ˆ
S as the input, which is the index marking the end of the rapid increase of the signal using a similar logic.

## Algorithm 2 Find Stabilization

1: **procedure** FIND_STABILIZATION_BY_MEAN( ˆ*S, t*∆ ˆ
S *, τ, ϵ*) ▷ ˆS is an array of normalized signal when only the head is trainable, t∆ ˆ
S is
the index marking the end of the rapid increasing of the signal, τ is the window for smoothing the signals, ϵ is the threshold in changes of the signal for stabilization.
2:
if t∆ ˆ
S > 0 then
3:
ˆS = ˆS[t∆ ˆ
S :]
4:
end if
5:
µ ˆ
S = moving_average( ˆ*S, τ*)
6:
∆µ ˆ
S = np.abs(np.diff(µ ˆ
S))
7:
for i, δ in enumerate(µ ˆ
S) do
8:
if δ ≤ ϵ then
9:
index = i
▷ The first time where the change is smaller than τ.
10:
break
11:
end if
12:
end for
13:
if t∆ ˆ
S > 0 then
14:
index = index + t∆ ˆ
S
15:
end if
16:
return index
17: end procedure
Using the heuristic algorithm, we determine the value k for experiments in Table 6, where we observe the determined k are very close to each other except for VGG with CIFAR10 and XLM-R with SQuAD. All the k value are shown visually in Figure 6, overlaying on top of the learning dynamics.

Metric
MNIST RN18
CIFAR10 RN18
CIFAR100 RN18
CIFAR10 VGG11
SQuAD XLM-R
MNLI XLM-R
Sρ
worst
270
230
260
960
810
780
Sρ
avg
270
270
250
1010
1090
720
tr(F)
210
260
230
250
1310
790

Table 7 shows the complete results for our complex experimental setup (described in §4). While all results are better than the standard training, empirically, tr(F) is a metric that gives a better winning rate compared to a random hyperparameter search.

|             |               | XQuAD         | MLQA       | XNLI        | WR             |
|-------------|---------------|---------------|------------|-------------|----------------|
| Method      | F1- En/X-ling | EM- En/X-ling | F1- X-ling | EM- X-ling  | Avg- En/X-ling |
| Standard    | 82.96/68.72   | 71.39/52.64   | 56.27      | 40.93       | 83.17/71.84    |
| GU          |               |               |            |             |                |
| S           |               |               |            |             |                |
| ρ           |               |               |            |             |                |
| worst       |               |               |            |             |                |
| 83.78/70.09 | 72.10/54.17   | 57.86         | 42.02      | 82.83/72.13 | 45%            |
| GU          |               |               |            |             |                |
| S           |               |               |            |             |                |
| ρ           |               |               |            |             |                |
| avg         |               |               |            |             |                |
| 83.84/70.00 | 72.12/53.69   | 58.10         | 42.03      | 83.03/72.27 | 40%            |
| GU          |               |               |            |             |                |
| tr          |               |               |            |             |                |
| (F)         |               |               |            |             |                |
| 83.77/70.70 | 72.33/54.40   | 58.47         | 42.31      | 83.36/72.49 | 80%            |

## E Additional Learning Dynamics E.1 Ranks

Figure 7 shows the evolution of feature ranks before the classification head for the first 2000 training steps. We observe standard training typically starts with a lower feature rank, as the training progresses the feature rank gradually increases. When withholding parameters from training, feature ranks are high at the initial period of learning, and as we gradually release parameters, the feature ranks reduce compared to the initial value.

## E.2 Change Learning Rate From Low To High

We provide an example of Sρ
avg during training when switching from a low learning rate to a high learning rate at k = 200 in Figure 8. From Figure 8, we can see the Sρ
avg is high initially, then quickly drops when the learning rate increases at step k. More interestingly, switching the learning rate induces similar effects as release parameters from frozen.

## E.3 Squad

In Figure 9, we present the learning dynamics for XLM-R with SQuAD in the early period of learning.

The learning dynamics show a similar trend as the SQuAD dataset, the Sρ
worst value is also negative, and withholding trainable parameters increases the Sρ
worst during training based on Eqn. 4 in our main paper.

K=200
K=200
K=200

## E.4 1/10Th Of The Default Learning Rate

Figure 10 shows the learning dynamics in the early period of training using 1/10th of the default learning rate (i.e. 0.1*lrd). The trends are similar to using the default learning rate.