# Gtagcn: Generalized Topology Adaptive Graph Convolutional Networks

Sukhdeep Singh2, Anuj Sharma ∗1*, Vinod Kumar Chauhan †3
1*Department of Computer Science and Applications, Panjab University, Chandigarh, India.

2Department of Computer Science, DM College (aff. to Panjab University, Chandigarh), Moga, Punjab, India.

3Department of Engineering Science, University of Oxford, Oxford, UK.

*Corresponding author(s). E-mail(s): anujs@pu.ac.in;
Contributing authors: sukha13@ymail.com; vinod.kumar@eng.ox.ac.uk;

## Abstract

Graph Neural Networks (GNN) has emerged as a popular and standard approach for learning from graph-structured data. The literature on GNN highlights the potential of this evolving research area and its widespread adoption in reallife applications. However, most of the approaches are either new in concept or derived from specific techniques. Therefore, the potential of more than one approach in hybrid form has not been studied extensively, which can be well utilized for sequenced data or static data together. We derive a hybrid approach based on two established techniques as generalized aggregation networks and topology adaptive graph convolution networks that solve our purpose to apply on both types of sequenced and static nature of data, effectively. The proposed method applies to both node and graph classification. Our empirical analysis reveals that the results are at par with literature results and better for handwritten strokes as sequenced data, where graph structures have not been explored.

Keywords: Graph Neural Networks, Deep Learning, Graph Convolutional Networks, Message Passing
∗Corresponding Author †Principal Author

## 1 Introduction

Graph Neural Networks (GNN) have emerged as a suitable choice for non-euclidean data or irregular data, where Graph Convolutional Networks (GCN) are able to work efficiently for these complex irregular data. The GCN advancements provide meaningful and valuable relationships between individuals in social networks [1] or chemical interactions [2] or recommending engines [3] or drug discovery [4, 5] and similar problems. This has resulted in the availability of graph structured data and techniques associated with GNN that could handle such datasets. This area of deep learning introduced many successful algorithms which were missing before GNN implementation.

The graphs and their rich Mathematical properties were systematically used in GNN which inherits the properties message passing among nodes, aggregation and graph kernels [6–8]. Notably, most of the GCN were either spatial or spectral in nature [9, 10], where data based on graph Fourier transformation is spectral in nature and spatial GCN consider use spatial features [3, 11]. The feature space can be systematically applied to spectral and spatial features which include feature subspaces flattening and structural principal components to expand feature space [12].

The GCN have been studied extensively in the recent past and work was mainly focused on message passing [6]. Most of the developed techniques follow recursive neighborhood aggregation, where a node aggregates messages from its neighboring nodes and updates itself. The updated nodes are permutation invariant and aggregation functions mainly include mean [11], max [13] and powermean [8]. Recent work has been carried out in the direction of permutation invariant using relational pooling where explicit labels are assigned to nodes as additional features [14]. Also, graph convolution operations multiplication by the graph adjacency matrix appeared to be a suitable choice in the previous study [15] [16]. Further, polynomials of graph adjacency matrix opened new directions to enhance GNN for time or image based signal processing systems. This has motivated us to solve the following question for GNN,
"What could be the impact of aggregation functions and polynomials of graph adjacency matrix together to sequenced or static nature of data?"
We have answered this question by combining two properties as aggregation function and polynomials of graph adjacency matrix, and tested for the pattern related problems, where time based data and static images based data were both evaluated. The time based data has been taken as online handwriting patterns [17] and scanned images are used as image data [18]. In addition, we have used other benchmarked data, which are different from handwritten pattern data.

The GNN could work for supervised and unsupervised problems both. The supervised learning includes graph kernels level and message passing for node, link, and graph level transductive tasks. The unsupervised learning includes shallow embeddings and message passing tasks as in supervised cases [19]. It has been noticed that mostly GNNs are used for supervised learning [20]. The present study is in the direction of supervised learning which include model building based on training data and its evaluation subject to test data. Most of the graph related problems are NP-hard in nature such as the evaluation of the best connection of nodes combination or the best path in the graph. The time based data has been used in sequential order that is able to reduce NP-hard complexities to an extent. For other data, we have used the graphs as provided by the sources.

In this paper, we have proposed Generalized Topology Adaptive Graph Convolutional Networks (GTAGCN) based on two successful techniques [21]. This scheme allows us to derive different variants of the proposed model. This technique focuses on the feasibility of computation for message passing task and maintaining the balance of the network. The graph filters refer to polynomials of the adjacency matrix in graph signal processing [16] and generalized aggregation functions are differentiable that help to learn better. Our main contributions are summarized as follows:

- The proposed GTAGCN combines two established techniques as generalized aggregation networks and topology adaptive GCN systematically that results in the smooth working of the proposed GTAGCN GCN.
- The results are best reported for time based data as online handwriting patterns
and at par or close to other image based data.
- The proposed GTAGCN accepts K-localized filters as happen in TAG GCN to
extract local features on a set of sizes from 1 to K receptive fields.
- In addition, generalized aggregation networks use of MLP and RELU are used in
GTAGCN.
The paper has been organized as follows. Section 2 includes related work and section 3 discusses the necessary introduction of GNN including notations. Section 4 explains the theoretical framework and proposed algorithm. Section 5 presents the results and discussion. The last section 6 concludes this paper with findings.

## 2 Notations And Basics

A graph G is defined as G = (V, E), where V = {v1, v2*, ..., v*N} and *E ⊆ V × V* are the set of vertices and edges, respectively. An edge e from node u *∈ V* to node v *∈ V* is represented as e = (u, v) *∈ E*. The nodes and edges in a graph are depicted in figure
1. An adjacency matrix is A ∈ R*|V|×|V|*.

One of the GNN fundamental components is nodes that enable network to learn structural representation. The edges are connections of nodes and share rich Mathematical properties as one-to-one, one-to-many and many-to-many relationships. The encoded features of graphs are important structure information of edges. The GNN's other component is graph convolutional layer that plays a major role in learning network from graph structure and data [22]. The node feature vector with enriched characteristics is part of the graph convolutional layer. The neighboring nodes feature vector aggregate to current node information using graph convolution operator function which is part of graph convolutional layer [23]. The convolution operators are special operators different from traditional operators and it includes learning of feature weights. This convolutional operation is performed on neighboring nodes and their associated features. This working of GNN operators uses non-linear activation functions and results feature vector passed to the next layers. This happen in an iterative mode for graph convolutional layers that help the network to learn weights which is an effective representation of graph structured data able to capture important information of graphs [24]. The activation functions are used to introduce non-linearity to layers output that further contribute in learning complex patterns of data [25]. The nodes in layers output applied by activation functions and aggregated with neighboring node features. Common activation functions are rectified linear unit (ReLU (max(0, x))), sigmoid (
1
1+e−x ), and hyperbolic tangent ( 1−e−2x
1+e−2x ) functions. Pooling and aggregation are used in GNN to reduce the dimensionality of the feature space and enable the network to handle graphs of different sizes. The pooling involves aggregating information from multiple nodes or subgraphs into a single representation [26, 27]. This mainly includes max pooling, mean pooling, or sum pooling.

The neural message passing is one of the key features of GNN which include vector messages are exchanged between nodes and update the node [6]. The message passing can be understood as follows,

$$\mathbf{h}_{u}^{(l+1)}=\text{UPDATE}^{(l)}(\mathbf{h}_{u}^{(l)},\tag{1}$$

AGREGATE${}^{(l)}(\mathbf{h}_{v}^{(l)},\forall v\in\mathcal{N}(u)))$
Here, AGGREGATE(l)(h(l)
v , ∀v *∈ N*(u)) is the aggregated message and expressed

as m(l)
     N (u). The h(l)
                 v
                    refers to vertex features. This results in final output layer as,

zu = hL
u, ∀u *∈ V*. This abstract form can be expressed as basic GNN message passing,

$$\mathbf{h}_{u}^{(l+1)}=\sigma(\mathbf{W}_{self}^{(l+1)}\mathbf{h}_{u}^{(l)}+\mathbf{W}_{neigh}^{(l+1)}\sum_{v\in\mathcal{N}(u)}\mathbf{h}_{u}^{(l)}+\mathbf{b}^{(l)})\tag{2}$$
where, W(l+1)
self , W(l+1)
neigh ∈ Rd(l)×d(l−1) are trainable parameter matrices and σ is elementwise non-linearity as *tanh* or ReLU [28]. This phenomenon can be understood with figure 2. Figure 2 presents the working of message passing for the node v1 of figure 1. The node v1 is directly connected to nodes v2 and v6. The model aggregates messages from v1 local graph neighbors as v2 and v3, and in turn, the messages coming from these neighbors (v2, v6) are based on information aggregated from their respective neighborhoods (v2 depends on v1, v3, v4, v7 and v6 depends on v5, v7, v8, v9), and so on. Therefore, figure 2 is GNN computation graph of tree structure nature and twolayer version of message passing model. One of the baselines of GNN model is GCN [11] which defines the message passing function as,

$$\mathbf{h}_{u}^{(l)}=\sigma\left(\mathbf{W}^{(l)}\sum_{v\in\mathcal{N}(u)\cup\{v\}}\frac{\mathbf{h}_{v}}{\sqrt{|\mathcal{N}(u)|}|\mathcal{N}(v)|}\right)\tag{3}$$
and the basic GCN layer is defined as,

$${\bf H}^{(l)}=\sigma\left(\hat{A}{\bf H}^{(l-1)}{\bf W}^{l}\right)\tag{4}$$
where, ˆA = D−1/2AD−1/2 and D is the diagonal degree matrix of ˆA.

## 3 Related Work

The GNN have made significant advancements in the recent past [20]. The present study presents a new GNN operator based on literature work. Selected graph convolution operators are discussed here. One of the early and popular works in this direction is Graph Convolutional Network Convolution [29] which represents working as,

$${\bf H}^{(l+1)}={\bf D}^{-\frac{1}{2}}{\bf AD}^{-\frac{1}{2}}{\bf H}^{(l)}{\bf W}^{(l)}\tag{5}$$
The other operator that follows spectral graph theory and efficient numerical schemes to design fast localized convolutional filters on graphs is Chebyshev graph convolutional [30]. It can be expressed as,

$${\bf H}^{(l+1)}=\sum_{k=0}^{K-1}\Theta_{k}^{(l)}{\bf T}_{k}(\tilde{\bf L}){\bf H}^{(l)}{\bf W}^{(l)}\tag{6}$$
where, Θ(l)
k
∈ Rd(l)×d(l+1) is the kth learnable Chebyshev filter at layer l, ˜L =
2L/λmax − IN is the normalized graph Laplacian with eigenvalues scaled to the range
[−1, 1] and L = IN −A refers to Laplacian matrix. Tk(˜L) is the kth Chebyshev polynomial of degree k evaluated at ˜L. To address and efficiently generate node embeddings in unseen data is Sample and aggregate convolutional network Convolution [31], which can be expressed as,

$$\mathbf{H}_{i}^{(l+1)}=\sigma\left(\mathbf{W}^{(l)}\cdot\text{CONCAT}\left(\mathbf{H}_{i}^{(l)},\text{MEAN}_{j\in\mathcal{N}^{(i)}}\{\mathbf{H}_{j}^{(l)}\}\right)\right)\tag{7}$$
The gated graph convolution [32] based on Gated Recurrent Unit includes,

$${\bf H}^{(l+1)}=\sigma\left(j(h^{k,T},{\bf H}^{(l)})\right)\tag{8}$$
The Graph Attention Network v2 Convolution (GATv2Conv) [33] is another extension of gated graph convolution using message passing, attention and update. This can be written as,

$$e_{ij}^{(l)}=\text{LeakyReLU}\left(\mathbf{a}^{(l)T}[\mathbf{W}^{(l)}\mathbf{H}_{i}^{(l)},\mathbf{W}^{(l)}\mathbf{H}_{j}^{(l)}]\right)\tag{9}$$

$$\alpha_{ij}^{(l)}=\frac{\exp(\text{LeakyReLU}(\mathbf{e}_{ij}^{(l)}))}{\sum_{k\in\mathcal{N}_{i}}\exp(\text{LeakyReLU}(\mathbf{e}_{ik}^{(l)}))}\tag{10}$$

$$\mathbf{H}_{i}^{(l+1)}=\sigma\left(\mathbf{W}^{(l)}\left(\sum_{j\in\mathcal{N}_{i}}\alpha_{ij}^{(l)}\mathbf{H}_{j}^{(l)}+\mathbf{H}_{i}^{(l)}\right)\right)\tag{11}$$
The Unified Message Passaging Model [34] includes feature and label propagation at both training and inference time.

$$v^{(l)}_{c;j}=W^{(l)}_{c;v}h^{(l)}_{j}+b^{(l)}_{c;v}\tag{12}$$

$$\hat{h}^{(l+1)}_{i}=\|\|^{C}_{c=1}\sum_{j\in N(i)}\alpha^{(l)}_{c;ij}\left(v^{(l)}_{c;j}+e_{c,ij}\right)\tag{13}$$
where, the || is the concatenation operation for C head attention. The Autoregressive Moving Average Convolution [35] was based on the autoregressive moving average as,

$${\bf H}^{(l+1)}=\sigma\left(\hat{\bf L}{\bf H}^{(l)}{\bf W}+{\bf H}^{(0)}{\bf V}\right),\tag{14}$$
where, ˆL = I − L = D−1/2AD−1/2. The Gaussian Mixture Model Convolution [36]
includes the output feature vector of each node computed as a weighted sum of the feature vectors of the Gaussian mixture components, with probability matrix P(l)
i,j. It can be expressed as,

$$\mathbf{H}^{(l+1)}=\sum_{i=1}^{M}\sum_{j=1}^{N}\mathbf{P}_{i,j}^{(l)}\cdot\sum_{k=1}^{K}\mathbf{H}_{j,k}^{(l)}\cdot\boldsymbol{\Theta}_{i,k}^{(l)}\tag{15}$$

$$\mathbf{P}_{i,j}^{(l)}=\text{softmax}\left(\frac{\exp\left(-\frac{1}{2}\cdot\left(\mathbf{x}_{i}-\mathbf{y}_{j}\right)^{T}\cdot\mathbf{A}\cdot\left(\mathbf{x}_{i}-\mathbf{y}_{j}\right)\right)}{\sum_{j^{\prime}=1}^{N}\exp\left(-\frac{1}{2}\cdot\left(\mathbf{x}_{i}-\mathbf{y}_{j^{\prime}}\right)^{T}\cdot\mathbf{A}\cdot\left(\mathbf{x}_{i}-\mathbf{y}_{j^{\prime}}\right)\right)}\right)\tag{16}$$

where, $\mathbf{P}_{i,j}^{(l)}$ is a probability matrix that assigns each node $i$ to a set of $K$ Gaussian mix
ture components centred at nodes j, H(l)
j,k is the feature vector of the k-th component centred at node j, Θ(l)
i,k is the weight matrix of the k-th component assigned to node i, xi is the feature vector of node i, yj is the feature vector of node j, A is a learnable affinity matrix that controls the similarity between nodes, and softmax is a softmax function that ensures that the weights assigned to each Gaussian mixture component sum to 1. The B-spline functions based work reported in Spline Convolution [37] which includes,

$$({\bf f}\star{\bf g})(i)=\frac{1}{{\cal N}(i)}\sum_{i=1}^{M_{m}}\sum_{j\in{\cal N}(i)}f_{l}(j)\cdot g_{l}(u(i,j))\tag{17}$$
The other advancements made as hypergraph convolution [38] is a generalization of graph convolution to hypergraphs and each node is connected to a fixed number of neighbors. It can be expressed as,

$$H^{(l+1)}=\left(D^{-\frac{1}{2}}AWB^{-1}A^{T}D^{-\frac{1}{2}}\right)H^{(l)}P\tag{18}$$
and its attention as,

$$H_{ij}=\sum_{k\in N_{i}}\frac{\exp\left(-\frac{1}{2}\|{\bf x}_{i}^{P}-{\bf x}_{j}^{P}\|^{2}\right)}{\sum_{k^{\prime}\in N_{i}}\exp\left(-\frac{1}{2}\|{\bf x}_{i}^{P}-{\bf x}_{k}^{P}\|^{2}\right)},\tag{19}$$
where ∥xP
i − xP
j ∥ denotes the Euclidean distance between the transformed feature vectors of nodes i and j. The Extended Convolution [39] operator was suitable for irregular and unstructured points cloud data. It can be expressed as,

$$F_{p}=X{\rm Conv}(K,p,P,F)={\rm Conv}(K,{\rm MLP}(P-p)\,\times\,[{\rm MLP}(P-p),F])\tag{20}$$
MLP is a multi-layer perceptron that takes as input the maximum feature vector among the neighboring points of point i. The F is trainable convolution kernels and P refers to features. Many GNN operators were reported in the literature.

In addition to above mentioned literature work, our work is closely related to the following two techniques.

Topology Adaptive Graph Convolutional Networks (TAGCN) explores a K-localized filter for graph convolution in the vertex domain that helps to extract local features up to size K [16]. The TAGCN includes G(l)
c,f ∈ RNl×Nl denote the fth graph filter and l is l-th hidden layer. The G(l)
c,fx(l)
c is graph convolution and f-th output filter followed by ReLU function is,

$${\bf y}_{f}^{(l)}=\sum_{c=1}^{C_{l}}G_{c,f}^{(l)}x_{c}^{(l)}+b_{f}{\bf I}_{N_{l}}\tag{21}$$
where, bf is a learnable bias and INl is the ones dimension vector. The G(l)
c,f is a polynomial of ˆA which is normalized adjacency matrix of graph as ˆA = D−1/2AD−1/2.

Therefore,

$$G^{(l)}_{c,f}=\sum_{k=0}^{K}g^{(l)}_{c,f,k}A^{k}\tag{22}$$
Here, g(l)
c,f,k is the graph filter polynomial coefficients. Thus, graph convolution operation becomes, x(l+1)
f
= σ
�
y(l)
f
�
, and σ is ReLU activation function.

GENeralized Aggregation Networks (GEN) construct GCN network for mean-max aggregation functions as SoftMax and PowerMean [21]. The SoftMax aggrei∈N (v) exp(βmv,i), where, mv,u is the message set and β is u∈N (v)
exp(βmv,u)
�
gation is �
u∈N (v) mp v,u continuous variable. The PowerMean is expressed as
�
1
�1/p
, where N(v)
�
p is non-zero continuous variable. Therefore, GEN message construction is,

$$m^{(l)}_{v,u}=\mbox{ReLU}(h^{(l)}_{u}+\mbox{I}(h^{(l)}_{e_{v,u}})\cdot h^{(l)}_{e_{v,u}})+\epsilon\tag{23}$$
where, I is the indicator function and ϵ is very small positive constant. Further, message aggregation function as ζ(l)(·) could be either SoftMax or PowerMean. This study extended to message normalization which combines other features during the vertex update phase. It can be expressed as,

$$h_{v}^{(l+1)}=\text{MLP}\left(h_{v}^{(l)}+s\cdot\|h_{v}^{(l)}\|_{2}\cdot\frac{m_{v}^{(l)}}{\|m_{v}^{(l)}\|_{2}}\right),\tag{24}$$
where MLP is the multi-layer perceptron, s is the scaling factor and aggregated messages normalized to ℓ2 norm.

## 4 Gtagcn

Our approach follows the conventional way of GNN working. We have adopted a message passing scheme that iteratively updates the representations of nodes. This allows to re-look at additional structural information to refine training stages. The proposed method extracts common properties of GEN [21] and TAGCN [16], thus referred to as Generalized Topology Adaptive Graph Convolutional Networks (GTAGCN). The GTAGCN working can be expressed as,

$$H^{(l)}=\text{MLP}\left(\sum_{k=0}^{K}\text{ReLU}\left(\hat{A}^{k}H^{(l-1)}W^{l}+\epsilon\right)\right)\tag{25}$$
Here, MLP, ReLU and ϵ adopted from GEN. The iterative working of ˆAk for K filters taken from TAG. The MLP is a deterministic process for efficient computations to train the network. This helps in adjusting the weights and enables the network to learn optimal weights that leads to meaningful representations. The ReLU non-linear property helps to train network systematically. This also results in complex relationships learning of data. The ϵ is a very small constant as discussed for GEN, which helps to retain value as non-zero. As discussed, ˆAk is (D−1/2AD−1/2)k, which refers to diagonal degree matrix. As discussed in [11], the D−1/2AD−1/2 has eigenvalues and respond effectively with softmax function. Further, [16] defined recursive behaviour of ˆAk with respect to filters. This moves convolutional layers to go deeper and the output of the last layer is the projection of the first convolution layer. The use of filters increases representation capability in this process. The GTAGCN is applicable to both directed and undirected graphs as TAGCN works. The GNNs can exploit graph structures and recover hidden features which include useful information of graphs [40].

The overall working of GTAGCN in GNN can be explained in sequential steps.

The first step is initialization which assigns node or edge features to graph and prepare graph G for the propagation. The propagation iterates over a fixed number of layers and a number of layers decided subject to the nature of data or adopted deep layered architecture. Here, each layer update node representation by aggregating information from neighboring nodes or edges. This step has been explained in equation 25. The aggregated information updates node representation using a non-linear activation function. A readout function is applied after all layers are processed and results in graph level representation based on node level representations. This could be used at graph level classification. The proposed GTAGCN is applicable to both node and graph level classification. In addition, backpropagation helps to update model parameters based on difference between predicted and true labels. Recent studies suggest that GNNs are limited in their propagation operators and can be improved by incorporating trainable channel-wise weighting factors [41]. Further, alternately optimized GNNs are other possibilities for semi-supervised learning on graphs from multi-view learning perspective [42].

The message passing is a time-consuming step as it includes aggregation and combination. Also, node representation and intermediate matrices during forward or backward passes are storage consuming. Both time and space are common challenges in deep learning problems, so part of GTAGCN as GNN technique. The GTAGCN complexity is close to TAGCN in view to see the inherited nature of GTAGCN from TAGCN [16]. Further, dealing with sparse matrices as happen in many real-life datasets, reduces both time and space complexities in practice. The empirical performance of the proposed algorithm GTAGCN has been demonstrated in the next section 5. The GTAGCN update process employed to enhance scalability that could easily accommodate graph of varying sizes. This generalizes to different graph structures and its interpretability in model decision. The MLP is an established part of deep learning working, which could easily work for complex input values. The topology aware GNNs and inference-efficient MLP gaps are bridged using different distillation speeds and differential distributed graphs [43]. As GNN enjoys the change of relationships over time for dynamic graphs, the use of ϵ avoids any zero situation. The overall combination is effective for diverse types of entities and complex system relationships. Attention mechanism applicable to relevant nodes as GTAGCN works close to techniques as GEN [21] and TAGCN [16].

## 5 Experiments

This section includes details for the datasets used, experiments setup and evaluation. We have covered sequence nature dataset as online handwriting recognition data [17]. Some of the datasets are directly available from repositories in the desired GNN form, other datasets are converted to GNN dataset form.

## 5.1 Datasets

The proposed GTAGCN technique has been implemented for GNN datasets such as cora, pubmed, citeseer, mnist, unipen and Gurmukhi HandWritten Text (GHWT)
datasets as presented in table 1. The cora, pubmed and citeseer are common datasets for GNN and are directly available in GNN form. The mnist in our experiments has been taken from the original mnist repository where 60k and 10k refer to train and test part of data. It is worth mentioning that we have not included superpixel based mnist dataset [3]. The datasets as unipen and GHWT are handwritten strokes data for digits

|            |    | Dataset   |   graphs |   nodes |   edges |   features |   classes |
|------------|----|-----------|----------|---------|---------|------------|-----------|
| citeseer [ | 44 | ]         |        1 |    3327 |    9104 |       3703 |         6 |
| cora [     | 45 | ]         |        1 |    2708 |   10556 |       1433 |         7 |
| Pubmed [   | 46 | ]         |        1 |   19717 |   88648 |        500 |         3 |
| mnist [    | 18 | ]         |    70000 |      31 |      30 |         31 |        10 |
| unipen [   | 47 | ]         |    12154 |      25 |      24 |         25 |        10 |
| GHWT [     | 17 | ]         |    33215 |      25 |      24 |         25 |        62 |

and Indic scripts Gurmukhi strokes. Therefore, we have converted mnist, unipen and indic to GNN dataset form. The datasets such as cora, pubmed and citeseer are node classification based data. The other datasets as mnist, unipen and GHWT are graph classification data. In mnist, each record is a graph and results in 60k train graphs and 10k test graphs. Similarly, for unipen and indic GNN graphs as depicted in table 1.

## 5.2 Experiment Setup

In all experiments, we use 3-layer MLP with batch normalization to map initial node representations to the desired dimensions, and 3-layer MLP without batch normalization for prediction. We have evaluated datasets using 10-cross validation using their provided data splits. The hidden dimension chosen size is 16. We apply dropout to the input of LSTM layer and chosen from {0, 0, 5}. We have chosen filter value K = 6
to analyze the effect and performance of GTAGCN. The batch size is chosen as 64 for all datasets because of memory constraints. The Aadam optimizer is used with a fixed learning rate of 0.01. The train and test split dataset has been implemented except for mnist dataset. The mnist dataset comes with 60k train and 10k test images. Therefore, we have followed the same standards. The unipen and GHWT datasets are split into 70 : 30 as train and test parts. The datasets as cora, pubmed and citeseer train and test ratio have been taken as mentioned in their repository [48]. Further, we have trained model such that validation accuracy does not increase for 100 epochs. In order to use mnist, unipen and indic datasets, their GNN representation has been done. We have used chain code feature representations for each record of these three datasets as discussed in literature [49, 50]. Further, these feature form based data converted to GNN datasets.

## 5.3 Results

The tables 2 and 3 illustrate the classification accuracy achieved by the proposed GTAGCN and baselines on the six datasets mentioned in table 1. In view to see large number of GNN methods today [20], it is complex task to run more than 50 GNN algorithms. Especially, our study is more inclined to see the working of the hybrid technique preliminarily. Therefore, we have restricted selected GNN techniques in the following tables 2 and 3. The results for all other techniques have been taken from the literature to avoid any confusion. We observe that our GTAGCN perform subject to state-of-the-art results for these datasets. We have been able to outperform results for two datasets as unipen and GHWT. In table 2, we find that our method is close to the results of other techniques. The datasets as cors, pubmed and citeseer in table 2 are for node classification. The table 3 demonstrates results for graph classification datasets as mnist, unipen and GHWT. We notice that GTAGCN outperforms for unipen and GHWT datasets.

As results depicted in table 2 for node classification datasets, we notice that GTAGCN perform at par with other popular techniques. Our results are very close to the best results for these datasets. Similarly, for graph classification results, we have achieved 99.10%, 99.16% and 92.97% recognition accuracy for mnist, unipen and GHWT datasets. The mnist best accuracy as 99.81% has been noticed using support vector machine technique as discussed in literature [51]. The GNN based Chebyshev for mnist dataset accuracy is 99.14% [52]. For unipen, [53] have achieved 98.9% accuracy, whereas we have been able to get 99.16% accuracy. The GHWT accuracy in literature is 86.60% and 87.71% for train:test split as 70 : 30 and 90 : 10. We have achieved 92.97% accuracy with 70 : 30 as train:test split.

|                     |       | Method   |   cora |   Pubmed |   Citeseer |
|---------------------|-------|----------|--------|----------|------------|
| GCN [               | 11    | ]        |  81.5  |     79   |       70.3 |
| TAGCN [             | 16    | ]        |  83.3  |          |            |
| ±                   |       |          |        |          |            |
| 0.7                 | 81.1  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.4                 | 71.4  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.5                 |       |          |        |          |            |
| GAT [               | 54    | ]        |  83    |          |            |
| ±                   |       |          |        |          |            |
| 0.7                 | 79.0  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.3                 | 72.5  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.7                 |       |          |        |          |            |
| DCNN [              | 3     | ]        |  76.8  |          |            |
| ±                   |       |          |        |          |            |
| 0.6                 | 73.0  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.5                 | -     |          |        |          |            |
| MoNet [             | 3     | ]        |  81.69 |          |            |
| ±                   |       |          |        |          |            |
| 0.5                 | 78.81 |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.4                 | -     |          |        |          |            |
| Chebyshev [         | 11    | ]        |  79.5  |     74.4 |       69.8 |
| GTAGCN (this paper) | 82.2  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.5                 | 79.1  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.4                 | 70.1  |          |        |          |            |
| ±                   |       |          |        |          |            |
| 0.5                 |       |          |        |          |            |
| Dataset   |   Accuracy (%) |
|-----------|----------------|
| mnist     |          99.1  |
| ±         |                |
| 0.7       |                |
| unipen    |          99.16 |
| ±         |                |
| 0.5       |                |
| GHWT      |          92.97 |
| ±         |                |
| 0.3       |                |

## 6 General Observations

As GNN research is in progression and further needs exploration of improvements in classification accuracy and performances. Some of the observations are listed here.

- The GNN needs data in graph structural form. This includes a systematic
understanding of data in terms of nodes, edges and respective relationships.
- GNNs use message passing process for organizing graphs in a certain form that can
be understood by machine learning algorithms. In it, every node is embedded with data about the node's location and its neighboring nodes. An AI model can find patterns and make predictions based on the embedded data.
- The GNN's ability to capture local and global features results in effective representation learning. However, data suitability for GNN working remains uncertain prior to experimentation.
- The GNN operator scalability feature could be generalized to large graphs which can
efficiently process graphs of varying sizes and handle sparsity of graph structures.
- The GNN operator's nature could be in variance to graph permutations that helps
to handle graph data regardless of any ordering.
- The GNN adaptability to new data needs transfer ability and acceptance of features
at different stages of graph networks.
- The challenge of interpretability of learned representations for graphs is complex
and its non-linear nature makes it difficult to interpret specific factors. This adds to the inner workings of GNN complex in nature and exhaustive, but the Mathematical nature of GNN overcomes these challenges.
- The GNN operators include different propagation rules for updating node or
edge representations. Also, differ in their respective aggregation mechanism for neighboring nodes. Also, respective network designs differ for message passing rules.
- GNNs are broadly classified as graph convolutional networks, recurrent graph neural networks, spatial graph convolutional networks, spectral graph convolutional networks and graph autoencoder networks.
- The GNN may face challenges for noisy or perturbed graphs. Interestingly, graphs
quality to learn representations itself work effectively on noisy data.
- The GNN overall outcome depends on theoretical and its practical implementations as theoretical foundation helps in designing complex relationships and understanding of data properties.
- The various variants of GNNs as graph convolutional network (GCN), graph recurrent network (GRN) and graph attention network (GAT) have presented great performances on several deep learning tasks.
- While deploying GNN, we should care about model interpretability for building
credibility, debugging or scientific discovery. The graph concepts that we should care, may vary from context to context. For example, with molecules we might care about the presence or absence of particular subgraphs
- The GNNs have great applications in structural as well as non - structural scenarios. The applications of GNNs can be explored as graph generation, graph mining, graph clustering, knowledge graphs, modeling real-world physical systems, molecular
fingerprints, chemical reaction prediction, protein interface prediction, biomedical engineering, combinatorial optimization, traffic networks, image classification, visual reasoning and semantic segmentation etc.
- The GNN could be applied to various tasks based on texts. It could be applied
for sentence level tasks such as text classification and word-level tasks such as sequence labeling. Further, it can be applied for other text based tasks as neural machine translation, semantic relation extraction between entities in texts, relational reasoning, event extraction, question answering and fact verification etc.
- One of the objective of present days GNN research is not making new GNN models
and architectures only, but it is mainly about "constructing graphs", more precisely, imbuing graphs with additional relations or structure that can be leveraged. So loosely it could seen as, the more graph attributes communicate the more we tend to have better GNN models.
- The GNN limitations do have a role in system performances. Common limitations
are over-smoothing, computationally expensive nature for very large graphs, sensitive to perturbations in the graph structure, changes in graph structure during training, sparsity or irregularity of data.
- Overall, the graphs are a powerful and rich structured data type that have strengths
and challenges. So we have also outlined some of the milestones that researchers have
come up with in building GNN based models that process graphs. The success of GNNs in recent years creates a great opportunity for a wide range of new problems, and it is excited to see what the future researchers will bring.

## 7 Conclusion

We presented GTAGCN method which has been derived from two established techniques. We have been able to implement the proposed method to both sequence and static nature of data. The handwritten strokes in online form have been taken as sequenced data and static data as mnist images converted to a sequenced form of data. Further, established GNN datasets as core, pubmed and citeseer are experimented with the proposed GTAGCN method. The results are at par with the literature work and better in the case of sequenced data. We find that extraction of different techniques properties could be helpful to other domains' data where graph representation learning has not been explored yet.

## Competing Interests

The authors declare that they have no competing interests.

## References

[1] Easley, D., Klienberg, J. (eds.): Networks, Crowds, and Markets: Reasoning About
a Highly Connected World. Cambridge University Press, ??? (2010)
[2] Stokes, J.M., Yang, K., Swanson, K., jin, W., Cubillos-Ruiz, A., Donghia, N.M.,
MacNair, C.R., French, S., Carfrae, L.A., Bloom-Ackermann, Z.: deep learning approach to antibiotic discovery. Cell **180**(4), 688–702 (2020)
[3] Monti, F., Boscaini, D., Masci, J., Rodola, E., Svoboda, J., and, M.M.B.: Geometric deep learning on graphs and manifolds using mixture model cnns. In Conference on Computer Vision and Pattern Recognition (CVPR) (2017)
[4] Zitnik, M., Leskovec, J.: Predicting multicellular function through multi-layer
tissue networks. Bioinformatics 33(14), 190–198 (2017)
[5] Wale, M., Watson, I.A., Karypis, G.: Comparison of descriptor spaces for chemical
compound retrieval and classification. Knowledge and Information Systems 14(3),
347–375 (2008)
[6] Gilmer, J., Schoenholz, S.S., Riley, P.F., Vinyals, O., Dahl, G.E.: Neural message passing for quantum chemistry. In Proceedings of the 34th International Conference on Machine Learning (2017)
[7] Battaglia, P.W., Hamrick, J.B., Bapst, V., Sanchez-Gonzalez, A., Zambaldi, V.,
Malinowski, M., Tacchetti, A., Raposo, D., Santoro, A., Faulkner, R.: Relational inductive biases, deep learning, and graph networks. arXiv preprint arXiv:1806.01261 (2018)
[8] Xu, K., Hu, W., Leskovec, J., Jegelka, S.: How powerful are graph neural
networks? In International Conference on Learning Representations (2019)
[9] Bruna, J., Zaremba, W., Szlam, A., LeCun, Y.: Spectral networks and locally
connected networks on graphs. In Internatonal Conference on Learning Representations (ICLR) (2014)
[10] Levie, R., Monti, F., Bresson, X., Bronstein, M.M.: Cayleynets: Graph convolutional neural networks with complex rational spectral filters. arXiv preprint arXiv:1705.07664 (2017)
[11] Kipf, T.N., Welling, M.: Semi-supervised classification with graph convolutional
networks. In Internatonal Conference on Learning Representations (ICLR) (2016)
[12] Sun, J., Zhang, L., Chen, G., Xu, P., Zhang, K., Yang, Y.: Feature expansion
for graph neural networks. Proceedings of the 40th International Conference on Machine Learning **202**, 33156–33176 (2023)
[13] Hamilton, W., Ying, Z., Leskovec, J.: Inductive representation learning on large
graphs. In Advances in neural information processing systems (2017)
[14] Zhou, C., Wang, X., Zhang, M.: From relational pooling to subgraph gnns: A
universal framework for more expressive graph neural networks. Proceedings of the 40th International Conference on Machine Learning **202**, 42742–42768 (2023)
[15] Sandryhaila, A., Moura, J.M.F.: Discrete signal processing on graphs. IEEE
Transactions on Signal Processing 61(7) (2013)
[16] Du, J., Zhang, S., Wu, G., Moura, J.M.F., Kar, S.: Topology adaptive graph
convolutional networks. arxiv:1710.10370 (2018)
[17] Singh, S., Sharma, A., Chhabra, I.: A dominant points-based feature extraction approach to recognize online handwritten strokes. International Journal of Document Analysis and Recognition 20, 37–58 (2017)
[18] LeCun, Y., Cortes, C., Burges, C.J.: The mnist database of handwritten digits.
http://yann.lecun.com/exdb/mnist/ (1998)
[19] Fey, M.: On the power of message passing for learning on graph-structured data.
Dissertation - der Technischen Universit¨at Dortmund (2022)
[20] Sharma, A., Singh, S., Ratna, S.: Graph neural network operators: a review.
Multimedia Tools and Applications (2023)
[21] Li, G., Xiong, C., Thabet, A., Ghanem, B.: Deepergcn: All you need to train
deeper gcns. arXiv (2020)
[22] Li, G., M¨uller, M., Ghanem, B., Koltun, V.: Training graph neural networks with
1000 layers. In: Proceedings of the 38th International Conference on Machine Learning, vol. 139, pp. 6437–6449 (2021)
[23] Zhang, Z., Cui, P., Zhu, W.: Deep learning on graphs: A survey. IEEE Transactions on Knowledge and Data Engineering 34(1), 249–270 (2022)
[24] Scarselli, F., Gori, M., Tsoi, A.C., Hagenbuchner, M., Monfardini, G.: Computational capabilities of graph neural networks. IEEE Transactions on Neural Networks 20(1), 81–102 (2009)
[25] Nwankpa, C., Ijomah, W., Gachagan, A., Marshall, S.: Activation functions:
Comparison of trends in practice and research for deep learning. arXiv eprint 1811.03378 (2018)
[26] Jin, Y., JaJa, J.F.: Improving graph neural network with learnable permutation pooling. In: 2022 IEEE International Conference on Data Mining Workshops (ICDMW), pp. 682–689 (2022)
[27] Lai, K.-H., Zha, D., Zhou, K., Hu, X.: Policy-gnn: Aggregation optimization for
graph neural networks. In: Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pp. 461–471 (2020)
[28] Hamilton, W.L.: Graph representation learning. Synthesis Lectures on Artificial
Intelligence and Machine Learning 17(3), 1–159 (2020)
[29] Kipf, T.N., Welling, M.: Semi-supervised classification with graph convolutional
networks. In: International Conference on Learning Representations (2017)
[30] Defferrard, M., Bresson, X., Vandergheynst, P.: Convolutional neural networks on
graphs with fast localized spectral filtering. In: Advances in Neural Information Processing Systems, vol. 29 (2016)
[31] Hamilton, W.L., Ying, Z., Leskovec, J.: Inductive representation learning on large
graphs. In: Advances in Neural Information Processing Systems, pp. 1024–1034
(2017)

[32] Li, Y., Tarlow, D., Brockschmidt, M., Zemel, R.: Gated graph sequence neural
networks. In: International Conference on Learning Representations (2016)
[33] Brody, S., Alon, U., Yahav, E.: How attentive are graph attention networks?
arXiv eprint 2105.14491 (2022)
[34] Shi, Y., Huang, Z., Feng, S., Zhong, H., Wang, W., Sun, Y.: Masked label
prediction: Unified message passing model for semi-supervised classification.
In: Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence, IJCAI-21, pp. 1548–1554 (2021)
[35] Bianchi, F.M., Grattarola, D., Livi, L., Alippi, C.: Graph neural networks with
convolutional arma filters. arXiv preprint arXiv:1901.01343 (2019)
[36] Monti, F., Boscaini, D., Masci, J., Rodola, E., Svoboda, J., Bronstein, M.M.:
Geometric deep learning on graphs and manifolds using mixture model cnns. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 5425–5434 (2017)
[37] Fey, M., Lenssen, J., Weichert, F., Muller, H.: Splinecnn: Fast geometric deep
learning with continuous b-spline kernels. In: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 869–877 (2018)
[38] Bai, S., Zhang, F., Torr, P.H.S.: Hypergraph convolution and hypergraph
attention. arXiv eprint 1901.08150 (2020)
[39] Li, Y., Bu, R., Sun, M., Wu, W., Di, X., Chen, B.: Pointcnn: Convolution on xtransformed points. In: Advances in Neural Information Processing Systems, pp. 820–830 (2018)
[40] Sato, R.: Graph neural networks can recover the hidden features solely from the
graph structure. Proceedings of the 40th International Conference on Machine Learning **202**, 30062–30079 (2023)
[41] Eliasof, M., Ruthotto, L., Treister, E.: Improving graph neural networks with
learnable propagation operators. Proceedings of the 40th International Conference on Machine Learning **202**, 9224–9245 (2023)
[42] Han, H., Liu, X., Mao, H., Torkamani, M., Shi, F., Lee, V., Tang, J.: Alternately optimized graph neural networks. Proceedings of the 40th International
Conference on Machine Learning **202**, 12411–12429 (2023)
[43] Wu, L., Lin, H., Huang, Y., Li, S.Z.: Quantifying the knowledge in gnns for
reliable distillation into mlps. Proceedings of the 40th International Conference on Machine Learning **202**, 37571–37581 (2023)
[44] Rossi, R., Ahmed, N.: The network data repository with interactive graph analytics and visualization. In: AAAI Conference on Artificial Intelligence, vol. 29, pp. 4292–4293 (2015)
[45] Prithviraj Sen, M.B.L.G.B.G. Galileo Mark Namata, Eliassi-Rad, T.: Collective
classification in network data. AI Magazine 29(3), 93–106 (2008)
[46] Galileo Mark Namata, L.G. Ben London, Huang, B.: Query-driven active surveying for collective classification. In: International Workshop on Mining and
Learning with Graphs (2012)
[47] Guyon, I., Schomaker, L., Plamondon, R., Liberman, M., Janet, S.: Unipen
project of on-line data exchange and recognizer benchmarks. In: Proceedings of the 12th IAPR International Conference on Pattern Recognition, Vol. 3 - Conference C: Signal Processing (Cat. No.94CH3440-5), vol. 2, pp. 29–33 (1994)
[48] Yang, Z., Cohen, W., Salakhudinov, R.: Revisiting semi-supervised learning
with graph embeddings. Proceedings of the 33rd International Conference on MachineLearning (2016)
[49] Bains, J.K., Singh, S., Sharma, A.: Dynamic features based stroke recognition
system for signboard images of gurmukhi text. Multimedia Tools and Applications 60, 665–689 (2021)
[50] Sharma, A.: A combined static and dynamic feature extraction technique to
recognize handwritten digits. Vietnam Journal of Computer Science 2, 133–142
(2015)
[51] Niu, X.-X., Suen, C.Y.: A novel hybrid cnn–svm classifier for recognizing
handwritten digits. Pattern Recognition 45(4), 1318–1325 (2012)
[52] Defferrard, M., Bresson, X., Vandergheynst, P.: Convolutional neural networks
on graphs with fast localized spectral filtering. Advances in Neural Information Processing Systems 29 (2016)
[53] Ratzlaff, E.H.: Methods, reports and survey for the comparison of diverse isolated character recognition results on the unipen database. Seventh International Conference on Document Analysis and Recognition, 2003. Proceedings., 623–6281 (2003)
[54] Veliˇckovi´c, P., Cucurull, G., Casanova, A., Romero, A., Li`o, P., Bengio, Y.: Graph
attention networks. International Conference on Learning Representations (2018)