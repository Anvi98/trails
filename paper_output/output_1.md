# Text Clustering With Llm Embeddings

Alina Petukhovaa,∗, Jo˜ao P. Matos-Carvalhoa,b, Nuno Fachadaa,b aLus´ofona University, COPELABS, Campo Grande, 376, Lisbon, 1700-921, Portugal bUNINOVA-CTS, Centre of Technology and Systems, Caparica, 2829-516, Portugal

## Abstract

Text clustering is an important approach for organising the growing amount of digital content, helping to structure and find hidden patterns in uncategorised data. In this research, we investigated how different textual embeddings—particularly those used in large language models (LLMs)— and clustering algorithms affect how text datasets are clustered. A series of experiments were conducted to assess how embeddings influence clustering results, the role played by dimensionality reduction through summarisation, and embedding size adjustment. Results reveal that LLM embeddings excel at capturing the nuances of structured language, while BERT leads the lightweight options in performance. In addition, we find that increasing embedding dimensionality and summarisation techniques do not uniformly improve clustering efficiency, suggesting that these strategies require careful analysis to use in real-life models. These results highlight a complex balance between the need for nuanced text representation and computational feasibility in text clustering applications. This study extends traditional text clustering frameworks by incorporating embeddings from LLMs, thereby paving the way for improved methodologies and opening new avenues for future research in various types of textual analysis. Keywords:
text clustering, large language models, text summarisation
2000 MSC: 68T50, 62H30

## 1. Introduction

Text clustering has garnered significant interest in the field of text analysis due to its potential to uncover hidden structures within large sets of unstructured textual data. With the growth of digital textual content generated through various platforms, such as social media, online news outlets, and academic publications, the ability to organise and analyse these data has become increasingly critical. Text clustering can potentially organise large volumes of unstructured data into meaningful categories, enabling efficient information retrieval and insightful thematic analysis across various domains, for example, customer feedback, academic research, and social media content. Text clustering is a preliminary step in other text analysis tasks such as topic modelling, trend analysis, and sentiment analysis. By grouping similar texts, subsequent analyses can proceed with enhanced accuracy and relevance, focusing on more homogeneous data sets with particular characteristics or themes.

As an analytical task, text clustering involves grouping text documents into clusters such that texts within the same cluster are more similar to each other than those in different clusters. It relies on the principle that text documents can be mathematically represented as vectors in a highdimensional space, also called embeddings, where dimensions correspond to the words or sentences within the documents. The axes of this space signify the various features extracted from the text, such as word frequency or contextual embeddings. Clustering algorithms exploit measures of proximity or resemblance, grouping documents that exhibit close correspondence in feature space. The research presented in this article aims to contribute to the domain of text clustering by analysing the effect of the different embeddings—including embeddings used in recently released large language models (LLMs)—and commonly used clustering algorithms on clustering results. We also perform additional experiments to evaluate the effect of dimensionality reduction with summarisation and embeddings size on clustering performance.

This paper is organised as follows. In Section 2, we describe the advancement in textual embeddings and briefly mention classical text clustering algorithms used in this domain. In Section 3, we outline the main steps and components of this study, namely the dataset selection, data preprocessing, embeddings, and clustering algorithms configuration used to assess clustering quality. In Section 4, we present the results of our study and provide a discussion of these findings. Limitations encountered during the study, along with recommendations for overcoming them, are acknowledged in Section 5. Finally, in Section 6, we synthesise the main conclusions of this research and suggest future developments.

## 2. Background

2.1. Text embeddings The landscape of text representation in natural language processing
(NLP) has undergone an impressive transformation over the past few decades. From simplistic representations to highly sophisticated embeddings, advancements in this domain have played an important role in enabling machines to process and understand human language with increasing accuracy.

One of the earliest methods of text representation that laid the groundwork for subsequent advances was Term Frequency-Inverse Document Frequency (TF-IDF). This method quantifies the importance of a word within a document relative to a corpus, accounting for term frequency and inverse document frequency [1]. While TF-IDF effectively highlighted the relevance of words, it treated each term as independent and failed to capture word context and semantic meaning [2].

Word embeddings, such as those produced by Word2Vec [3] and GloVe [4], marked a significant step forward by generating dense vector representations of words based on their contexts. These models leveraged surrounding words and large corpora to learn word relationships, successfully capturing a range of semantic and syntactic similarities. Despite their effectiveness in capturing semantic regularities, these models still provided a single static vector per word, which posed limitations in capturing polysemous words.

The arrival of BERT (Bidirectional Encoder Representations from Transformers) initiated a new phase of embedding sophistication [5]. To generate contextual embeddings, BERT employs a bidirectional transformer architecture, pre-trained on a massive corpus. This allows for a deeper understanding of word relationships by considering the full context of a word in a sentence in both directions. This revolutionised tasks like text clustering by providing richer semantic representations.

Today, LLMs like OpenAI's GPT are at the forefront of generating stateof-the-art embeddings [6]. LLMs extend the capabilities of previous models by providing an unprecedented depth and breadth of knowledge encoded in word and sentence-level embeddings. These models are trained on extensive datasets to capture a broad spectrum of human language nuances and generate embeddings that reflect a comprehensive understanding of contexts and concepts. The progression from TF-IDF to sophisticated LLM embeddings represents a transformative journey towards more nuanced and contextually aware text representation in NLP. This evolution continues to propel the field forward, expanding the possibilities for applications like text clustering, sentiment analysis, and beyond. 2.2. Text clustering algorithms Text clustering involves grouping a set of texts so that texts in the same group (referred to as a cluster) are more similar to each other than those in different clusters. This section overviews classic clustering algorithms widely used for clustering textual data.

K-means is perhaps the most well-known and commonly used clustering algorithm due to its simplicity and efficiency. It partitions the dataset into k clusters by minimising the within-cluster sum of squares, i.e., variance. Each cluster is represented by the mean of its points, known as the centroid [7]. K-means is particularly effective for large datasets but depends heavily on the initialisation of centroids and the value of k, which must be known a priori.

In turn, agglomerative hierarchical clustering (AHC) builds nested clusters by merging them successively. This bottom-up approach starts with each text as a separate cluster and combines clusters based on a linkage criterion, such as the minimum or maximum distance between cluster pairs [8]. AHC is versatile and allows for discovering hierarchies in data, but it can be computationally expensive for large datasets.

Spectral clustering techniques use the eigenvalues of a similarity matrix to reduce dimensionality before applying a clustering algorithm like k-means. It is particularly adept at identifying clusters that are not necessarily spherical, as k-means assumes. Spectral clustering can also handle noise and outliers effectively [9]. However, its computational cost can be high due to the eigenvalue decomposition involved.

Fuzzy c-means is a clustering method that allows one data point to belong to more than one cluster.

This method minimises the objective function with respect to membership and centroid position; it provides soft clustering and can handle overlapping clusters [10]. Fuzzy c-means is useful when the boundaries between clusters are not clearly defined, although it is computationally more intensive than k-means.

In addition to these classic approaches, recent years have seen the rise of alternative methods for text clustering that leverage the strengths of modern embeddings and consider the unique properties of textual data. These include using deep learning models, particularly those based on autoencoders, to learn meaningful low-dimensional representations ideal for clustering [11]. Others explore graph-based clustering methods that construct a graph from text embeddings and partition this graph into clusters [12]. Ensemble clustering approaches, where multiple clustering algorithms are combined to improve the robustness and quality of the results, have also been gaining attention. These methods benefit from the diversity of the individual algorithms and can sometimes overcome the limitations of any single method [13].

The field of text clustering is rapidly expanding, and keeping up with the latest findings is crucial for advancing the state of the art. Recent papers, such as those exploring the use of transformer-based embeddings for clustering [14] or integrating external knowledge bases into the clustering process [15], represent just the tip of the iceberg in this vibrant area of research. Moreover, an emerging technique involves using summarisation to refine text clustering, positing that by condensing text into more manageable representations, we can achieve clusters of greater coherence and interpretability, a notion that is particularly advantageous when faced with large and complex datasets [16]. This work will focus on the applicability of LLM embeddings for text clustering, experimentation with summarisation as a dimensionality reduction technique, and evaluation of the impact of embedding size on clustering results.

## 3. Methods

To enhance the understanding of text data through clustering, this research compares the effectiveness of various embedding representations in improving the performance of text clustering algorithms. Our goals include identifying the most informative embeddings for text representation in clustering problems. For this purpose, we systematically experimented with multiple datasets, embeddings, and clustering methods and performed an in-depth analysis of the clustering results using different evaluation metrics.

Overall, the following steps were taken during the course of this study:

1. Selection of datasets.
2. Preprocessing of datasets, including the removal of miscellaneous characters, emails, HTML tags, etc.
3. Utilisation of various embedding computations, including LLM-related
ones, to retrieve numerical text representations.
4. Application of several clustering algorithms commonly used in text
clustering.
5. Comparison of clustering results using different external and internal
validation metrics.
The following subsections provide a comprehensive discussion of each of these steps, further detailing the employed methodologies.

3.1. Datasets We selected four datasets to cover a variety of text clustering challenges.

Table 1 shows these datasets and their characteristics. The CSTR abstracts dataset [17] is a corpus of 299 scientific abstracts from the Centre for Speech Technology Research. The homogeneous and domain-specific nature of the CSTR dataset allowed us to investigate the effectiveness of clustering techniques in discerning fine-grained topic distinctions in scholarly text related to categories such as artificial intelligence, theory, systems, and robotics. The SyskillWebert dataset [18], which includes user ratings for web pages, enabled the exploration clustering to analyse information used in recommendation systems.

The 20Newsgroups dataset [19] is a famous collection of approximately 19,000 news documents partitioned across 20 different classes. With its broad assortment of topics and noisy, unstructured text, this dataset provided a realistic scenario for evaluating the robustness of clustering algorithms under less-than-ideal conditions. To complement these, we added the MN-DS dataset [20], a diverse compilation of multimedia news articles, which provides the opportunity to explore the effectiveness of clustering algorithms in handling multi-categorical data. The dataset is organised hierarchically in two levels.

Therefore, experiments were performed independently for each level.

These datasets collectively present unique sets of characteristics such as text length variability, domain-specific vocabulary, and varying levels of class balance, creating a comprehensive testing ground for this text clustering study. 3.2. Preprocessing The motivation for preprocessing text data is to minimise noise and highlight key patterns, thereby improving the efficiency and accuracy of clustering algorithms [21].

For all datasets, a series of preprocessing steps were taken to ensure the quality and uniformity of the input data. The initial step involved removing

| Dataset               |   Size |   No. classes | Ref.   |
|-----------------------|--------|---------------|--------|
| CSTR                  |    299 |             4 | [17]   |
| SyskillWebert         |    333 |             4 | [18]   |
| 20Newsgroups dataset  |  18846 |            20 | [19]   |
| MN-DS dataset level 1 |  10917 |            17 | [20]   |
| MN-DS dataset level 2 |  10917 |           109 | [20]   |

miscellaneous items such as irrelevant metadata, HTML tags, and any extraneous content that might skew the analysis. Continuing with this methodology, we systematically eliminated invalid non-Latin characters from the dataset. These characters could arise from multilingual data sources or artefacts of data collection, such as encoding errors. Given that the employed workflow is optimised for Latin-based languages, retaining such characters could increase the dimensionality of the feature space, therefore undermining clustering performance, both in terms of computational efficiency and interpretability of the results.

## 3.3. Text Embeddings For Textual Data Representation, We Compared Classical Embeddings [22,

5] and state-of-the-art LLM embeddings. Traditional TF-IDF vectors served as a baseline, providing a sparse but interpretable representation based on word importance and analysed dataset. BERT embeddings were extracted from the BERT model, which was trained as a transformer-based bidirectional encoder on BookCorpus [23] and English Wikipedia [24]. These embeddings were leveraged for deep contextual understanding, capturing the nuances in semantic meanings across the corpus. We also employed "textembedding-ada-002" [25] embeddings since they demonstrated the best results among OpenAI's embeddings on larger datasets for text search, code search, and sentence similarity tasks. Additionally, other LLM embeddings, computed for Falcon [26] and LLaMA-2-chat [27] models, were included for their respective advancements in performance and efficiency. Falcon embeddings were trained on a hybrid corpus consisting of both text documents and code, while the LLaMA-2-chat embeddings—built on the foundation of LLaMA-2 model using an optimised auto-regressive transformer—
underwent targeted fine-tuning for dialogue and question-and-answer tasks. BERT, Falcon, and LLaMA-2-chat embeddings were obtained from Hugging Face's transformers library, where Hugging Face is a company specialising in providing state-of-the-art models in the form of pipelines and making them accessible through their platform [28]. Table 2 describes the exact embeddings and configurations used.

| Embeddings   | Configuration                                          |
|--------------|--------------------------------------------------------|
| TF-IDF       |                                                        |
| min df       |                                                        |
| = 5,         |                                                        |
| max df       |                                                        |
| = 0          | .                                                      |
| max features |                                                        |
| = 8000       |                                                        |
| BERT         | huggingface.co/sentence-transformers/all-mpnet-base-v2 |
| OpenAI       | huggingface.co/Xenova/text-embedding-ada-002           |
| Falcon       | huggingface.co/tiiuae/falcon-7b                        |
| LLaMA-2      | huggingface.co/meta-llama/Llama-2-7b-chat-hf           |

3.4. Clustering algorithms The selected clustering algorithms address the diverse nature of text data, which often contains complex patterns requiring robust methods for effective grouping. Standard k-means clustering was used for its simplicity and efficiency in dealing with large datasets. K-means++ was chosen as an enhanced variant of k-means, with careful initialisation to improve convergence and cluster quality. AHC was utilised for its ability to reveal nested structures within the data. Compared to k-means, which forces each data point into a single exact cluster, Fuzzy c-means offers a more nuanced approach to text clustering by assigning probabilistic membership levels, accommodating the polysemy and subtle semantic differences typical in text.

Finally, Spectral clustering was selected for its effectiveness in identifying clusters based on the graph structure induced by the data and also since it is particularly adept at discovering clusters with non-convex shapes. We used the nearest centroid approach to map clusters and original labels for all clustering algorithms.

The selected algorithms and their respective parameters are listed in Table 3. The *scikit-learn* library [29] provided the implementations for all algorithms except for Fuzzy c-means, which was used from the scikit-fuzzy package [30].

| Algorithm     | Parameters   |
|---------------|--------------|
| k             | -means       |
| init          |              |
| = random,     |              |
| n             |              |
| init          |              |
| = 10,         |              |
| seed          |              |
| = 0           |              |
| k             | -means++     |
| init          |              |
| =             | k            |
| n             |              |
| init          |              |
| = 1,          |              |
| seed          |              |
| = 0           |              |
| AHC           |              |
| metric        |              |
| = euclidean,  |              |
| linkage       |              |
| = ward        |              |
| Fuzzy         | c            |
| init          |              |
| = None,       |              |
| m             |              |
| = 2,          |              |
| error         |              |
| = 0           | .            |
| maxiter       |              |
| = 1000        |              |
| Spectral      |              |
| assign labels |              |
| = discretize, |              |
| seed          |              |
| = 10          |              |

3.5. Evaluation metrics To comprehensively evaluate the quality of different embeddings and algorithm combinations, we used a diverse set of metrics. For external validation, since original labels were available, we used the weighted F1-score
(F1S) [31], the Adjusted Rand Index (ARI) [32], and the Homogeneity score (HS) [33]. The F1-score was computed to balance precision and recall in the presence of class imbalance. The ARI was used to access the clustering outcomes while correcting for chance grouping, and the HS was used to evaluate the degree to which each cluster is composed of data points from primarily one class. For internal validation, we leveraged the Silhouette Score (SS) [34] and the Calinski-Harabasz Index (CHI) [35], evaluating cluster coherence and separation without requiring ground truth. This multifaceted approach ensures a robust assessment, capturing both the alignment with known labels and the intrinsic structure of the generated clusters.

These metrics collectively provide a balanced view of the performance, accounting for datasets with varying characteristics and sizes. The metrics and their corresponding formulas are presented in Table 4.

Table 4: Metrics used to assess clustering results, their type (external or internal), and their respective formulas. For F1-score, C represents the number of classes, wi is the weight assigned to the i-th class, which is typically the proportion of that class within the dataset, and F1,i represents the F1-score computed for the i-th class. For ARI, RI
stands for Rand Index, Expected RI refers to the expected value of the Rand Index under random label assignment (calculated using the contingency table marginals), MaxIndex is the maximum possible value of the Rand Index. For HS, H(C|K) is the conditional entropy of the class distribution given the predicted cluster assignments, H(C) is the entropy of the class distribution. For SS, N represents the total number of data points in the dataset, and s(i) is the silhouette score for a single data point i, defined as s(i) =
b(i)−a(i)
max{a(i),b(i)} where a(i) is the average distance from the i-th data point to the others in the same cluster, b(i) is the minimum mean distance from the i-th data point to points in a different cluster, minimised over all clusters. For CHI, Tr(Bk) is the trace of the between-group dispersion matrix and measures the between-cluster dispersion, Tr(Wk) is the trace of the within-cluster dispersion matrix and quantifies the within-cluster dispersion, N refers to the number of data points, and k indicates the number of clusters. The optimal value for all these metrics is the maximum or *Max*.

| Metric      | Type     | Formula   |
|-------------|----------|-----------|
| F1S         | External |           |
| i           | =1       |           |
| w           |          |           |
| i           |          |           |
| F           |          |           |
| 1           | ,i       |           |
| C           |          |           |
| �           |          |           |
| ARI         | External |           |
| RI          |          |           |
| −           |          |           |
| Expected RI |          |           |
| Max RI      |          |           |
| −           |          |           |
| Expected RI |          |           |
| HS          | External | 1         |
| −           |          |           |
|             | H        | (         |
| |           |          |           |
| K           | )        |           |
| k           |          |           |
| −           |          |           |
| 1           |          |           |
| H           | (        | C         |
| SS          | Internal |           |
| 1           |          |           |
| N           |          |           |
| �           |          |           |
| N           |          |           |
| i           | =1       |           |
|             | s        | (         |
| CHI         | Internal |           |
| Tr(         | B        |           |
| k           |          |           |
| )           |          |           |
| Tr(         | W        |           |
| k           |          |           |
| )           |          |           |
|             | ×        |           |
| N           |          |           |
| −           |          |           |
| k           |          |           |

3.6. Additional experiments This section describes additional experiments in which we performed text summarisation (3.6.1) and tested LLM embeddings obtained from larger models (i.e., models with more parameters) prior to clustering (3.6.2). The purpose is to investigate whether such representations can improve the discriminability of features within text clusters.

3.6.1. Summarisation This experiment aims to evaluate summarization as a tool for dimensionality reduction in text clustering by creating compact representations of the texts that encapsulate the semantic core without losing context. These experiments are hypothesised to streamline the clustering process, potentially leading to more coherent and interpretable clusters, even in large and complex datasets. The models used in summarisation are described in Table 5.

As an alternative approach to LLM-based models, we used the summarisation model BERT-large-uncased [5] with the implementation provided by the BERT summariser [36] to assess potential improvements in clustering achieved by utilising a lower-dimensionality model.

Embeddings Summarisation
model
Max tokens
BERT
bert-largeuncased [5]
512
OpenAI
gpt-3-5-turbo [37]
4096
Falcon
falcon-7b [38]
2048
LLaMA-2- chat
Llama-2-7b-chathf [39]
4096

For the LLaMA-2 and Falcon models, we used the Hugging Face transformers library with the parameters described in Table 6.

| Parameter name       |
|----------------------|
| temperature          |
| 0                    |
| max length           |
| 800                  |
| do sample            |
| True                 |
| top k                |
| 10                   |
| num return sequences |
| 1                    |

The following zero-shot prompt was used for generating the summarised text with LLMs:

Write a concise summary of the text. Return your responses
with maximum 5 sentences that cover the key points of the text.
{text}
SUMMARY:

3.6.2. Higher dimensionality of embeddings The original publications on LLMs underline the increase of performance with the larger model sizes in common sense topics, question answering, and code tasks [26, 27]. This experiment investigates the impact of utilising embeddings computed for higher dimensionality models on the performance of clustering algorithms in order to determine if they can capture more nuanced textual features that enhance cluster cohesion and separation. For this purpose, we used embeddings obtained for models presented in Table 7.

To visualise the different embeddings and capture their intrinsic structures, Principal Component Analysis (PCA) and t-Distributed Stochastic Neighbor Embedding (t-SNE) [40] were used. Initially, PCA was applied or preliminary dimensionality reduction while preserving variance. Then, t-SNE was used to project the data into a lower-dimensional space, emphasising the local disparities between embeddings. This sequential application of PCA and t-SNE allowed us to capture both the global and local structures within the embeddings, providing a richer visualisation of the embedding models than using PCA alone.

| Model                    | Model reference        |
|--------------------------|------------------------|
| (bp)                     |                        |
| Tokens                   |                        |
| (trl)                    |                        |
| Falcon-7b                | huggingface.co/tiiuae/ |
| falcon-7b                |                        |
| 7                        | 1.5                    |
| Falcon-40b               | huggingface.co/tiiuae/ |
| falcon-40b               |                        |
| 40                       | 1                      |
| LLaMA-2-7b               | huggingface.co/meta-   |
| llama/Llama-2-7b-chat-hf |                        |
| 7                        | 2                      |
| 13                       | 2                      |
| LLaMA-2-13b              | huggingface.co/meta-   |
| llama/Llama-2-13b-chat-  |                        |
| hf                       |                        |

## 4. Results And Discussion

Table 8 presents the clustering metrics for the "best" algorithm for the tested combinations of dataset, embedding, and clustering algorithm. By "best", we mean the algorithm with the highest F1-score value. The complete results are available as supplementary material1.

Results demonstrate that OpenAI embeddings yield superior clustering performance on structured, formal texts compared to other methods based on most metrics (column "Total" in Table 8). The combination of the kmeans algorithm and OpenAI's embeddings yielded the highest values of ARI, F1-score, and HS in most experiments. This may be attributed to OpenAI's embeddings being trained on a diverse array of Internet text, rendering them highly effective at capturing the nuances of language structures. Low values of SS and CHI for the same algorithm could indicate that, while clusters are homogeneous and aligned closely with the ground truth labels (suggesting good class separation and cluster purity), they may not be well-separated or compact as evaluated in a geometric space. This discrepancy can arise in cases where data has a high-dimensional or complex structure that the external measurements like ARI, F1S, and HS capture effectively, but when projecting into a lower-dimensional space for SS and CHI, the clusters appear to overlap or vary widely in size, leading to a lower score for these spatial coherence metrics.

In the domain of open-source models, namely Falcon, LLaMA-2, and BERT, the latter emerged as the frontrunner.

Given that BERT is designed to understand the context and potentially due to the model's lower dimensionality, these embeddings demonstrate good effectiveness in text clustering. In the comparative analysis of open-source LLM embeddings, Falcon-7b outperformed the LLaMA-2-7b across most datasets, demonstrating improved cluster quality and distinctiveness. This superiority may be attributed to Falcon-7b embeddings ability to capture better the salient linguistic features and semantic relationships within the texts since these embeddings were trained on a mixed corpus of text and code, as opposed to the LLaMA-2 embeddings, which are specialised for dialogues and Q&A contexts. Additionally, the CHI metric—measuring the dispersion ratio between and within clusters—is higher for Falcon-7b embeddings, suggesting that clusters are well separated and dense.

Experiments with the MN-DS dataset, which has an inherent label hierarchy, show that performing clustering at a higher, more abstract label level yields slightly better class separation. This outcome aligns with expectations, as it allows for the consolidation of documents into broader and more distinguishable themes. It reinforces the strategy that for datasets with multi-layered label taxonomies, clustering at higher levels can produce more cohesive and interpretable clusters that reflect the natural categorical divisions within the data. The downside is that broader categories are less specific, meaning less information is extracted for each document.

|         |          |                |                | Dataset Embed.   | Best alg.   | F1S        | ARI   | HS   | SS CHI Total   |
|---------|----------|----------------|----------------|------------------|-------------|------------|-------|------|----------------|
| DS1     | TF-IDF   | k              | -means         | 0.67             | 0.38        | 0.46       | 0.016 | 4    | 0/5            |
| BERT    | Spectral | 0.85 0.60      | 0.63           | 0.118            | 25          | 3/5        |       |      |                |
| OpenAI  | k        | -means         | 0.84           | 0.59             | 0.64        | 0.066      | 13    | 1/5  |                |
| LLaMA-2 | k        | -means         | 0.41           | 0.09             | 0.17        | 0.112      | 49    | 1/5  |                |
| Falcon  | k        | -means         | 0.74           | 0.39             | 0.48        | 0.111      | 34    | 0/5  |                |
| DS2     | TF-IDF   | Spectral       | 0.82           | 0.63             | 0.58        | 0.028      | 8     | 0/5  |                |
| BERT    | AHC      | 0.74           | 0.58           | 0.53             | 0.152       | 37         | 0/5   |      |                |
| OpenAI  | AHC      | 0.90 0.79 0.75 | 0.070          | 19               | 3/5         |            |       |      |                |
| LLaMA-2 | k        | -means         | 0.51           | 0.21             | 0.25        | 0.137      | 69    | 0/5  |                |
| Falcon  | k        | -means++       | 0.45           | 0.26             | 0.30        | 0.170      | 85    | 2/5  |                |
| DS3     | TF-IDF   | Spectral       | 0.35           | 0.13             | 0.28 -0.002 | 37         | 0/5   |      |                |
| BERT    | k        | -means         | 0.43           | 0.25             | 0.44        | 0.048      | 412   | 0/5  |                |
| OpenAI  | k        | -means         | 0.69 0.52 0.66 | 0.035            | 213         | 3/5        |       |      |                |
| LLaMA-2 | AHC      | 0.17           | 0.11           | 0.26             | 0.025       | 264        | 0/5   |      |                |
| Falcon  | k        | -means         | 0.26           | 0.15             | 0.30        | 0.071 1120 | 2/5   |      |                |
| DS4     | TF-IDF   | k              | -means         | 0.29             | 0.13        | 0.48       | 0.034 | 17   | 0/5            |
| BERT    | k        | -means         | 0.35           | 0.24             | 0.55        | 0.072      | 61    | 1/5  |                |
| OpenAI  | k        | -means         | 0.38 0.26 0.58 | 0.053            | 42          | 3/5        |       |      |                |
| LLaMA-2 | k        | -means         | 0.21           | 0.11             | 0.40        | 0.053      | 88    | 0/5  |                |
| Falcon  | k        | -means++       | 0.27           | 0.16             | 0.48        | 0.071      | 92    | 1/5  |                |
| DS5     | TF-IDF   | AHC            | 0.31           | 0.09             | 0.29        | 0.010      | 37    | 0/5  |                |
| BERT    | k        | -means++       | 0.43           | 0.27 0.42        | 0.060       | 178        | 2/5   |      |                |
| OpenAI  | Spectral | 0.45           | 0.25           | 0.41             | 0.036       | 120        | 1/5   |      |                |
| LLaMA-2 | AHC      | 0.23           | 0.10           | 0.23             | 0.031       | 263        | 0/5   |      |                |
| Falcon  | k        | -means++       | 0.28           | 0.12             | 0.25        | 0.070      | 359   | 2/5  |                |

The results of the summarisation experiment are presented in Table 9.

These results show that using summarisation as a dimensionality reduction technique does not consistently benefit all models. Clustering results for the original texts without generated summaries are higher than those with summarisation. This finding suggests that essential details necessary for accurate clustering might have been lost during the summarisation process. Alternatively, the inherent complexity and nuances of textual representation might require a more sophisticated approach to text summarisation that can maintain essential information while reducing complexity. Additionally, it is important to highlight that we observed low-quality clustering results when using the summarisation output from the smaller-sized LLaMA-2-7b and Falcon-7b models, likely due to their limited ability to capture and reproduce the complex nuances inherent in the source texts.

Results for the model size experiment, presented in Table 10, highlight the positive influence of embedding size on clustering outcomes for Falcon-7b embeddings with higher ARI, F1-score, and HS for the CSTR
and SyskillWebert datasets. This may be due to the fact that embeddings for the Falcon-40b model were created over a subset of the data used for the Falcon-7b embeddings (1.5 trillion tokens for Falcon-7b and 1 trillion tokens for Falcon-40b). Also, we anticipated comparable results from the LLaMA-7b and LLaMA-13b embeddings, as they were reportedly trained on identical datasets according to the original paper [39]. However, our observations indicate that LLaMA-13b embeddings surpass those of LLaMA-7b. Pinpointing the reasons for this discrepancy proves difficult, as the original training datasets were not made publicly available by Facebook.

Another perspective is given by Figure 1, which shows a visualisation of different sizes of LLM embeddings using PCA and t-SNE. A noticeable artefact for LLaMA-7b (Figure 1a) and Falcon-40b (Figure 1d) is the lack of coherence in document classes 1 and 2, pointing to an unclear delineation in the feature space. Conversely, when employing LLaMA-13b (Figure 1b) and Falcon-7b (Figure 1c), the classes have better separation, providing a possible explanation of the clustering results observed in Table 10. Increasing the embedding size yielded significant improvements in the results for the algorithms, aligning with existing literature that suggests larger embeddings are more capable of capturing complex patterns in the data. Since larger dimensionality comes at a higher computational cost, with implications on scalability and efficiency, it is worth investigating whether the improvements in clustering performance level off with increasing embeddings size or if they are sustainable and to what extent computational efficiency can be balanced against improved clustering.

| Dataset Embed.   | Version          | Best alg.   | F1S                 | ARI                  | HS     | SS CHI        |
|------------------|------------------|-------------|---------------------|----------------------|--------|---------------|
| DS1              | BERT             | Full        | Spectral            | 0.85 0.60 0.63 0.118 | 25     |               |
| BERT             | Summary Spectral | 0.81        | 0.50                | 0.56                 | 0.114  | 24            |
| OpenAI           | Full             | k           | -means              | 0.84 0.59 0.64 0.066 | 13     |               |
| OpenAI           | Summary          | k           | -means              | 0.81                 | 0.53   | 0.58          |
| LLaMA-           |                  |             |                     |                      |        |               |
| 2                |                  |             |                     |                      |        |               |
| Full             | k                | -means      | 0.44                | 0.12                 | 0.21   | 0.099         |
| LLaMA-           |                  |             |                     |                      |        |               |
| 2                |                  |             |                     |                      |        |               |
| Summary AHC      | 0.47 0.16 0.30   | 0.072       | 24                  |                      |        |               |
| Falcon           | Full             | k           | -means              | 0.74 0.39 0.48       | 0.111  | 34            |
| Falcon           | Summary          | k           | -means              | 0.40                 | 0.03   | 0.02          |
| DS2              | BERT             | Full        | AHC                 | 0.74                 | 0.58   | 0.53          |
| BERT             | Summary AHC      | 0.75        | 0.57                | 0.54                 | 0.089  | 22            |
| OpenAI           | Full             | AHC         | 0.9 0.79 0.75 0.070 | 19                   |        |               |
| OpenAI           | Summary Spectral | 0.79        | 0.71                | 0.64                 | 0.054  | 18            |
| LLaMA-           |                  |             |                     |                      |        |               |
| 2                |                  |             |                     |                      |        |               |
| Full             | k                | -means      | 0.51 0.21 0.25      | 0.137                | 69     |               |
| 0.25             | 0.04             | 0.06        | 0.548               | 603                  | LLaMA- |               |
| 2                |                  |             |                     |                      |        |               |
| Summary Fuzzy    |                  |             |                     |                      |        |               |
| c                | -mean            |             |                     |                      |        |               |
| Falcon           | Full             | k           | -means++            | 0.45 0.26 0.30       | 0.170  | 85            |
| 0.34             | 0.04             | 0.07        | 0.269               | 577                  | Falcon | Summary Fuzzy |
| c-mean           |                  |             |                     |                      |        |               |

Throughout our analysis, we did not discern any consistent patterns in the selection of a clustering algorithm with regard to its performance; however, we did observe that, in the majority of cases, k-means outperformed other algorithms. This suggests that, despite the absence of a one-size-fitsall solution, k-means boasts a particular robustness or suitability for the datasets and embeddings used in this study.

## 5. Limitations

Despite the insights revealed in this study, the available computational resources constrained the experiments, prohibiting us from conducting ad-

|             |            |                | Dataset Embed.   |   Best alg. |    F1S |    ARI |    HS |   SS CHI |
|-------------|------------|----------------|------------------|-------------|--------|--------|-------|----------|
| DS1         | LLaMA-2-7b | k              | -means           |       0.41  |  0.09  |   0.17 | 0.112 |       50 |
| LLaMA-2-13b | AHC        | 0.82 0.53 0.61 | 0.084            |      21     |        |        |       |          |
| Falcon-7b   | k          | -means         | 0.74 0.39 0.48   |       0.111 | 34     |        |       |          |
| Falcon-40b  | AHC        | 0.46           | 0.17             |       0.3   |  0.111 |  44    |       |          |
| DS2         | LLaMA-2-7b | k              | -means           |       0.51  |  0.21  |   0.25 | 0.137 |       69 |
| LLaMA-2-13b | k          | -means++       | 0.60 0.49 0.39   |       0.095 | 37     |        |       |          |
| Falcon-7b   | k          | -means++       | 0.45 0.26 0.30   |       0.17  | 85     |        |       |          |
| Falcon-40b  | k          | -means++ 0.40  | 0.15             |       0.13  |  0.188 | 131    |       |          |

ditional trials with summary generation and higher-dimensional models on more voluminous datasets.

Consequently, the potential benefits of summaries in large-scale text clustering have yet to be thoroughly evaluated. Summarisation might behave differently when applied at scale or with distinct prompts, potentially providing more pronounced benefits or drawbacks depending on the complexity and diversity of the text data.

Furthermore, there is a possibility that embeddings computed for extralarge models like Falcon-180b or LLaMA-70b could deliver even more substantial gains, but practical application is restrained by the significant computational demand that accompanies increased model size. This limitation potentially skews our understanding of the absolute efficacy of the embeddings computed for these models, as we can only infer performance improvements up to a specific size.

These constraints prompt essential considerations for future research.

Specifically, experiments with larger datasets and higher-dimension models would enable a more comprehensive and accurate understanding of the potentials and limitations of text clustering algorithms and their scalability in real-world applications.

## 6. Conclusions

In this study, we examined the impact that various embeddings—namely TF-IDF, BERT, OpenAI, LLaMA-2, and Falcon—and clustering algorithms have on grouping textual data. Through detailed exploration, we evaluated the efficacy of dimensionality reduction via summarisation and the role of embedding size on the clustering accuracy of various datasets. We found that OpenAI's sophisticated embeddings outperformed other embeddings. BERT's performance excelled amongst open-source alternatives, underscoring the potential of advanced models to positively affect text clustering results.

This research also revealed a trade-off between improved clustering results and the computational weight of larger embeddings. Although results indicate that an increase in model size often correlates with enhanced clustering performance, the benefits must be weighed against the practicality of available computing resources.

A key takeaway from this investigation is that summary-based dimensionality reduction does not consistently improve clustering performance, signalling that a nuanced approach is necessary when preprocessing text to avoid losing vital information. Our exploration also brings to attention the practical challenges imposed by limited computational resources, which are a significant hurdle in the widespread application of large models, especially in expansive text analysis.

These findings point towards continued research focused on developing strategies that leverage the strengths of advanced models while mitigating their computational demands.

It is also critical to expand the scope of research to include more diverse text types, which will provide a more comprehensive understanding of clustering dynamics across different contexts and inform the development of more universally applicable NLP tools.

In conclusion, our findings underscore the complex interplay between embedding types, dimensionality reduction, embedding size, and text clustering effectiveness in the context of structured, formal texts. While larger, more advanced embeddings like OpenAI's present clear advantages, researchers and practitioners must consider trade-offs in terms of cost, computational resources, and the impact of text preprocessing techniques.

## Acknowledgements

This work is supported by Funda¸c˜ao para a Ciˆencia e a Tecnologia under grants UIDB/04111/2020 (COPELABS) and UIDB/00066/2020 (Centro de Tecnologias e Sistemas).

## References

[2] J. Ramos, Using TF-IDF to determine word relevance in document queries, in: Proceedings of the First Instructional Conference on Machine Learning (ICML 2003), 2003, p. 29–48.
[3] T. Mikolov, K. Chen, G. Corrado, J. Dean, Efficient estimation of word representations in vector space (2013). arXiv:1301.3781.
[4] J. Pennington, R. Socher, C. Manning, Glove: Global vectors for word representation, in: Proceedings of the 2014 Conference on Empirical Methods in Natural
Language Processing (EMNLP), Vol. 14, 2014, pp. 1532–1543. doi:10.3115/v1/
D14-1162.
[5] J. Devlin, M. Chang, K. Lee, K. Toutanova, BERT: pre-training of deep bidirectional
transformers for language understanding, CoRR abs/1810.04805 (2018).
arXiv:
1810.04805.
URL http://arxiv.org/abs/1810.04805
[6] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, et al., Language models are few-shot learners, Advances in Neural Information Processing Systems 33 (2020).
[7] J. MacQueen, Some methods for classification and analysis of multivariate observations, in: Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1, University of California Press, Berkeley, Calif, 1967, pp. 281–297.
[8] J. H. Ward, Hierarchical grouping to optimize an objective function, Journal of the
American Statistical Association 58 (301) (1963) 236–244.
[9] A. Y. Ng, M. I. Jordan, Y. Weiss, On spectral clustering: Analysis and an algorithm,
in: Advances in Neural Information Processing Systems, Vol. 2, 2002, pp. 849–856.
[10] J. C. Bezdek, Pattern Recognition with Fuzzy Objective Function Algorithms,
Plenum Press, New York, 1981.
[11] J. Xie, R. Girshick, A. Farhadi, Unsupervised deep embedding for clustering analysis, in: International Conference on Machine Learning, 2016, pp. 478–487.
[12] L. Yang, et al., Modularity based community detection with deep learning, in: Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI),
2020, p. 2252–2258.
[13] A. Strehl, J. Ghosh, Cluster ensembles - a knowledge reuse framework for combining
multiple partitions, Journal of Machine Learning Research 3 (2002) 583–617.
[14] L. Pugachev, M. Burtsev, Short text clustering with transformers, in: INTERNA-
TIONAL CONFERENCE in Computational Linguistics and intelligent technologies,
2021, pp. 571–577. doi:10.28995/2075-7182-2021-20-571-577.
[15] X. Li, et al., Integrating semantic knowledge to tackle zero-shot text classification,
in: Proceedings of NAACL-HLT, 2019, p. 1031–1040.
[16] N. Nagwani, Summarizing large text collection using topic modeling and clustering
based on mapreduce framework, Journal of Big Data 2 (12 2015). doi:10.1186/
s40537-015-0020-5.
[17] J. Yamagishi, C. Veaux, K. MacDonald, CSTR VCTK Corpus: English multispeaker corpus for CSTR voice cloning toolkit (version 0.92) (2019). doi:10.7488/ ds/2645.
[18] M. Pazzani, Syskillwebert web page ratings (1999).
[19] T. Mitchell,
Twenty Newsgroups,
UCI Machine Learning Repository,
DOI:
https://doi.org/10.24432/C5C323 (1999).
URL http://qwone.com/~jason/20Newsgroups/
[20] A. Petukhova, N. Fachada, MN-DS: A multilabeled news dataset for news articles
hierarchical classification, Data 8 (5) (2023). doi:10.3390/data8050074. URL https://www.mdpi.com/2306-5729/8/5/74
[21] A. Petukhova, N. Fachada, TextCL: A Python package for NLP preprocessing
tasks, SoftwareX 19 (2022) 101122.
doi:https://doi.org/10.1016/j.softx.
2022.101122.
URL
https://www.sciencedirect.com/science/article/pii/
S2352711022000802
[22] W. Uther, D. Mladeni´c, M. Ciaramita, B. Berendt, A. Ko�lcz, M. Grobelnik, M. Witbrock, J. Risch, S. Bohn, S. Poteet, A. Kao, L. Quach, J. Wu, E. Keogh, R. Miikkulainen, P. Flener, U. Schmid, F. Zheng, G. Webb, S. Nijssen, TF–IDF, Springer US,
2010, Ch. TF–IDF, pp. 986–987. doi:10.1007/978-0-387-30164-8_832.
[23] Y. Zhu, R. Kiros, R. Zemel, R. Salakhutdinov, R. Urtasun, A. Torralba, S. Fidler,
Aligning books and movies: Towards story-like visual explanations by watching movies and reading books, in: The IEEE International Conference on Computer Vision (ICCV), 2015, pp. 19–27.
[24] P. Przyby�la, P. Borkowski, K. Kaczy´nski, Wikipedia complete citation corpus (Jul.
2022). doi:10.5281/zenodo.6539054. URL https://doi.org/10.5281/zenodo.6539054
[25] R. Greene, T. Sanders, L. Weng, A. Neelakantan, New and improved embedding
model, accessed: 2023-11-28 (2023).
URL https://openai.com/blog/new-and-improved-embedding-model
[26] E. Almazrouei, H. Alobeidli, A. Alshamsi, A. Cappelli, R. Cojocaru, M. Debbah,
´Etienne Goffinet, D. Hesslow, J. Launay, Q. Malartic, D. Mazzotta, B. Noune,
B. Pannier, G. Penedo, The Falcon series of open language models (2023). arXiv:
2311.16867.
[27] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov,
S. Batra, P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. C. Ferrer, M. Chen, et al.,
Llama 2: Open foundation and fine-tuned chat models (2023). arXiv:2307.09288.
[28] Hugging face (2024).
URL https://huggingface.co/
[29] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel,
M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, E. Duchesnay, Scikit-learn: Machine learning in Python, Journal of Machine Learning Research 12 (2011) 2825–2830.
[30] J. Warner, J. Sexauer, scikit fuzzy, twmeggs, alexsavio, A. Unnikrishnan, G. Castel˜ao, F. A. Pontes, T. Uelwer, pd2f, laurazh, F. Batista, alexbuy, W. V. den Broeck, W. Song, T. G. Badger, R. A. M. P´erez, J. F. Power, H. Mishra, G. O. Trullols, A. H¨orteborn, 99991, Jdwarner/scikit-fuzzy: Scikit-fuzzy version 0.4.2 (Nov. 2019).
doi:10.5281/zenodo.3541386.
URL https://doi.org/10.5281/zenodo.3541386
[31] N. Chinchor, MUC-4 evaluation metrics, in: Proceedings of the 4th Conference
on Message Understanding, MUC4 '92, Association for Computational Linguistics,
USA, 1992, p. 22–29. doi:10.3115/1072064.1072067.

URL https://doi.org/10.3115/1072064.1072067

[32] D. Steinley, Properties of the hubert-arabie adjusted rand index, Psychological
methods 9 (2004) 386–96. doi:10.1037/1082-989X.9.3.386.
[33] A. Rosenberg, J. Hirschberg, V-measure: A conditional entropy-based external cluster evaluation measure, in: J. Eisner (Ed.), Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL), Association for Computational Linguistics, Prague, Czech Republic, 2007, pp. 410–420.
URL https://aclanthology.org/D07-1043
[34] P. Rousseeuw, Silhouettes: A graphical aid to the interpretation and validation
of cluster analysis, Journal of Computational and Applied Mathematics 20 (1987)
53–65. doi:10.1016/0377-0427(87)90125-7.
[35] T. Cali´nski, H. JA, A dendrite method for cluster analysis, Communications in
Statistics - Theory and Methods 3 (1974) 1–27. doi:10.1080/03610927408827101.
[36] D. Miller, Leveraging BERT for extractive text summarization on lectures (2019).
arXiv:1906.04165.
[37] gpt-3-5-turbo (2024).
URL https://platform.openai.com/docs/models/gpt-3-5-turbo/
[38] falcon-7b (2024).
URL https://huggingface.co/tiiuae/falcon-7b/
[39] Llama-2-7b-chat-hf (2024).
URL https://huggingface.co/meta-llama/Llama-2-7b-chat-hf/
[40] L. Van der Maaten, G. Hinton, Visualizing data using t-sne., Journal of machine
learning research 9 (11) (2008).