# A Novel Mutual Insurance Model For Hedging Against Cyber Risks In Power Systems Deploying Smart Technologies

Pikkin Lau, *Student Member, IEEE*, Lingfeng Wang, *Senior Member, IEEE,* Wei Wei, Zhaoxi Liu, Member, IEEE, and Chee-Wooi Ten, *Senior Member, IEEE* 
   
Abstract—In this paper, a novel cyber-insurance model design is 

proposed based on system risk evaluation with smart technology 
applications. The cyber insurance policy for power systems is 
tailored via cyber risk modeling, reliability impact analysis, and 
insurance premium calculation. A stochastic Epidemic Network 
Model is developed to evaluate the cyber risk by propagating 
cyberattacks among graphical vulnerabilities. Smart technologies 
deployed in risk modeling include smart monitoring and job thread 
assignment. Smart monitoring boosts the substation availability 
against cyberattacks with preventive and corrective measures. The 
job thread assignment solution reduces the execution failures by 
distributing the control and monitoring tasks to multiple threads. 
Reliability assessment is deployed to estimate load losses 
convertible to monetary losses. These monetary losses would be 
shared through a mutual insurance plan. To ensure a fair 
distribution of indemnity, a new Shapley mutual insurance 
principle is devised. Effectiveness of the proposed Shapley mutual 
insurance design is validated via case studies. The Shapley 
premium is compared with existent premium designs. It is shown 
that the Shapley premium has high indemnity levels closer to those 
of Tail Conditional Expectation premium. Meanwhile, the Shapley 
premium is nearly as affordable as the coalitional premium and 
keeps a relatively low insolvency probability.  

Index Terms—Power system reliability, cyber-insurance, power 

system security, cyber-physical systems, cyber risk modeling, 
actuarial design, tail risk. 

## Nomenclature

A. Acronym 
TGs           Transmission Grids ICTs           Information and Communications Technologies IEDs          Intelligent Electronic Devices CPSs          Cyber-Physical Systems 
SCADA     Supervisory Control And Data Acquisition IDS            Intrusion Detection System TTF           Time-To-Failure SCT           Substation Compromise Time ENM         Epidemic Network Model BN             Bayesian Network CVSS        Common Vulnerability Scoring System HMI          Human-Machine Interface WAP         Wireless Access Point 
____________________________________________ 
under awards ECCS1739485 and ECCS1739422. and Computer Science, University of Wisconsin-Milwaukee, Milwaukee, WI 53211, USA.  
W. Wei is with Department of Mathematical Sciences, University of Wisconsin-Milwaukee, Milwaukee, WI 53211, USA. 

C.-W. Ten is with Department of Electrical and Computer Engineering, 
 
 
Michigan Technological University, Houghton, MI 49931, USA. 

RTUs        Remote Terminal Units EMUs       Energy Management Units VaR          Value at Risk TCE          Tail Conditional Expectation ELC          Expected Load Curtailment EFC          Expected Faulty-Bus Count OPF          Optimal Power Flow MCS         Monte Carlo Simulation SD            Standard Deviations CoVs        Coefficients of Variation FOR          Forced Outage Rate SoI            Strengths of Interdependence 

B. Notation 
𝐶𝐶           a control center 𝑆              **              a substation 
𝑇𝑐             Substation Compromise Time 
𝑣ℎ            a network vulnerability 
𝑡𝑠             vulnerability sojourn time 𝐽1, 𝐽2, 𝐽3    numbers of assigned job threads 𝑌1, 𝑌2        durations of the task operation 
𝑈              residual time of the job thread executing the task 𝜆               failure rate of the substation CPS elements 𝜇               repair rate of the substation CPS elements  
(𝜆𝑏, 𝜇𝑏)    baseline failure and repair rates 
(𝜆𝑖, 𝜇𝑖)     smart-monitoring state failure and repair rates 
(𝜆𝑐, 𝜇𝑐)    composite smart-monitoring failure and repair rates 𝑝(𝑣ℎ)       probability of exploiting 𝑣ℎ 𝜍(𝑣ℎ)        score of the vulnerability 𝑣ℎ 
𝑝(𝑣ℎ ∧ 𝑐ℎ) probability that 𝑣ℎ is exploited by 𝑐ℎ 
𝑝(𝑐ℎ|𝑣ℎ)  conditional probability of successfully exploiting 
𝑝(𝑐ℎ)        total probability of successful exploitation on 𝑣ℎ 
ζ               set of adjacent nodes of a given graphical node 
𝑇⃑ 𝑟𝑒𝑐          epidemic recovery time vector 𝑇⃑ 𝑒𝑝𝑖          epidemic infection time vector 
𝑇𝑟𝑒𝑐          epidemic recovery time of the substation 𝑇𝑒𝑝𝑖          epidemic infection time of the substation 𝑇̂𝑐             sampled substation compromise time  
𝑇̂𝑟             sampled substation repair time 
𝔹ζ            binomial variate of the adjacent node infectivity 
𝜀               basic reproduction number 𝑐               graphical edge coupling number   
𝑍𝑒𝑝𝑖          external epidemic infection time 𝑅𝑒𝑝𝑖          external epidemic recovery time 𝑝𝑎𝑡𝑘          probability of cyberattack infection ℙ𝑣            correlated uniform variate of state sampling 
𝟏{∙}           binary indicator function  
𝑺𝒙             ****             set of substations 𝑲𝒙            ****            load curtailment vector (MW) 
∗             base indemnity of TG 𝑞 among 𝑘 TGs in S 
𝜈               ****               time step of the reliability assessment 
𝑩              ****              substation susceptance vector 
𝜽              ****              vector of the substation voltage angles (rad) 𝑮              ****              vector of the available generation (MW) 
𝑮𝒄𝒂𝒑         ****         generation capacity vector (MW) 
𝑫𝒄𝒂𝒑         ****         load capacity vector (MW) 
𝑭               ****               transmission power flow vector (MW) 
𝑭𝒄𝒂𝒑            ****            thermal limit vector of the transmission lines (MW) 
𝐸𝑁(𝑺𝒙)     enabling function of the substations 
𝟏{∙}            ****            true/false binary indicator of a conditional statement 
∗                element-wise product operator 
𝜋1              TCE Premium 𝜋2              Coalitional Premium 
𝜋3              The proposed Shapley Premium 
ℂ𝑞             Shapley value of TG 𝑞 
U               universal set including all participating TGs 
𝜀𝑞,𝑘            Shapley cost of the TG 𝑞 among 𝑘 TGs in S 
S                subset of the selected TGs  
𝛿𝑞              cumulative loss distribution  
y                number of TGs in the universal set 𝑘                number of TGs which submit their claims 
𝛤𝑞,𝑘
𝜓             indemnity of TG 𝑞 among 𝑘 TGs in S 

𝜓(∙)           scaling function of 𝛤𝑞 
𝛤𝑞,𝑘
𝜓            indemnity of TG 𝑞 
𝛤𝑞
Φ(𝜋)         probability of insolvency 

## I. Introduction

T 
HE technological transformation from the conventional power grid to smart grid has been drastically galvanized by the rapid development and deployment of ICTs. With everincreasing market values in the smart grid, the mass adoption of IEDs and other cyber-capable equipment in CPSs leads to increased network connectivity and higher operation uncertainty. Various security challenges in operations may sabotage or paralyze contemporary power grids [1]-[3]. For example, configuration change attack is a common cyber-threat where IEDs receive commands to manipulate the settings. Distance relays may receive malicious commands leading to unnecessary trips to transmission lines and disruption to substation operation. To mitigate the emerging cyber-threats, diverse cybersecurity technologies have been developed. For example, transient detection algorithms and obfuscation strategy can be developed for mitigating device risks [4] and enhancing cybersecurity [5]. To protect the SCADA systems, IDS is a promising solution against potential cyberattacks. An advanced machine learning based IDS with high accuracy was developed [6]. A reinforcement learning algorithm was tailored to obtain the stochastic strategies that minimize load curtailment subjected to coordinated attacks [7]. IDS involving supervised learning should have collected raw data preprocessed and labeled for the classification purpose. An ensemble approach was developed for the comparative feature extraction [8]. Security models are in place to evaluate and defend against the cyberattacks. A Cyber-Net model was developed to capture the cyber intrusion of switching attacks in a comprehensive power CPS including firewalls, SCADA and IEDs in a substation [9]. A data-driven stochastic game model was proposed to evaluate the cross-layer security of CPSs [10]. A matrix-based model was developed to capture the cyber-physical coupling behavior of IDS [11]. Strategic competition between defense and intrusion across the temporal state transition can be described by the Markov decision process [12]. Security metrics such as TTF are proposed to gauge the long-term risk of a network [13]. Investment in the enhancement of CPSs may be beneficial to reducing the interruption costs in the face of cyberattacks. Smart monitoring based on preventive and corrective measures was proposed for cyber network of the power system [14]. Job assignment strategy was designed to boost the reliability for vehicular clouds in [15].  
 Conventionally, technological solutions are considered the main approach to mitigate cyber risks. In this work, cyberinsurance is further devised as a promising financial instrument to hedge against the emerging cyber risks. A cyber-insurance design framework typically includes cyber risk modeling, cyberattack-induced loss estimation, and insurance premium calculation. In [16], stochastic cybersecurity insurance pricing models for graphical networks was proposed.  In [17] and [18], the potential cyber-insurance models for power systems were explored. Accounting for various cyber-intrusion scenarios, the cyber-insurance designs specific to the implications of cyberthreats on power system reliability were developed. In [17], an insurance principle was developed upon the system reliability assessment at varying intrusion tolerance capabilities of the substation SCADA servers. In [18], a Bayesian Network graphical model for integrated cybersecurity-reliability was applied to a coalitional insurance design. In this work, a new mutual cyber insurance model will be developed for power grids deploying smart technologies.  
The main contributions of this paper are summarized as follows: 

- 
A novel mutual cyber-insurance framework based on the Shapley value of the cooperative game is devised.  Load loss distributions are extracted from the mutual insurance participants to formulate cost values, ultimately obtaining reduced costs in the cooperative game. 
- 
An integrated reliability evaluation model considering substations deploying smart monitoring and job thread assignment technologies is developed aiming to enhance the system robustness against cyberattacks.  
- 
A state-sampling cyber epidemic model is integrated into the Bayesian Network cyber vulnerability model. This integrated model is devised considering the propagation of cyberattacks and network correlation.  
The remainder of this paper is organized as follows. Section II introduces cybersecurity in the substation CPSs coupled with the smart technologies. In Section III, the insurance principle is elaborated. Section IV presents the case studies including numerical simulations. Section V draws conclusions for this paper.  

## A. Related Work

To clarify the advancement of this work, it would be beneficial to review the most relevant work. This work continues our quest for efficient cybersecurity insurance designs, following [17] and [18]. In [17], a cyber-insurance model based on estimating the cyber risk and reliability of interdependent TGs was proposed. Reference [18] presents an alternative cyberinsurance design based on the coalitional insurance platform [19]. In this work, a new cyber-insurance framework based on Shapley cooperative game is proposed to integrate the cyberinsurance model [17] into the coalitional cyber-insurance model [18]. A prototypical epidemic spreading model [16] was used to explore the upper and lower bounds of cyberattack infection probabilities. 

The proposed cyber epidemic model inspired by [16] is conceived to further estimate the long-term infectious vulnerability risk on the graphical cyber epidemic network model coupled with power systems. While the epidemic model in [16] may be effective in estimating the upper bounds of infection probabilities in various scenarios, explicit mathematical form to evaluate the physical and monetary losses incurred in CPSs by the cyberattack needs to be further developed. The proposed epidemic network model is thus specifically tailored to the reliability-based load curtailment estimation. This study examines the effectiveness of the proposed epidemic network model considering smart technologies including smart monitoring [14] and job thread assignment [15] for improving the reliability of TGs. The results of reliability assessment are further integrated in the proposed insurance premium design. Shapley value is utilized in the proposed insurance premium design in the proposed insurance premium design as a unique solution of the cooperative game which optimizes the price of anarchy [20]-[22]. The interdependence of CPSs was addressed in [23] by creating the probability table without explicitly assigning the SoI. In this work, the SoI are directly incorporated into the state sampling process which are then reflected in load loss profiles of TGs. The comparison with the related work described above is summarized in Table I.  

 
TABLE I SUMMARY OF COMPARISON WITH RELATED WORK 
[18] 
[17] 
[19] 
[14] 
[15] 
[16] 
[23] 
 
This work 
RA 
✓ 
✓ 
✓ 
 
✓ 


CPE 
✓ 
✓ 
✓ 


✓ 
 
SM 
✓ 


✓ 


JA 
✓ 


✓ 
 
 
SCG 
✓ 


MI 
✓ 
✓ 
 
✓ 


LI 
✓ 
✓ 
✓ 


✓ 
CSM 
✓ 
✓ 
✓ 
 
 
✓ 
 
 
GCVN 
✓ 
✓ 


CEM 
✓ 


✓ 
 

* RA = Reliability Assessment, CPE = Cyber Premium Evaluation, SM = Smart Monitoring, JA = Job Assignment, SCG = Shapley Cooperative Game, MI = Mutual Insurance, LI = Loss Interdependence, CSM = Cyber-Security Metric, GCVN = Graphical Cyber Vulnerability Network, CEM = Cyber Epidemic Model 

## Ii. Proposed Epidemic Cyber-Physical System Model A Goal Of This Study Is To Gauge The Risk Of Cyberattacks On The

individual TGs to determine economical insurance pricing strategies. Fig. 1 conveys the proposed mutual insurance framework as multiple steps: (a) The power system configuration under study should be segmented according to the TGs ownership. (b) Within respective TG substations, smart monitoring and server job assignment are enforced to enhance the substation reliability subject to cyberattacks. (c) Accounting for the cyber connection across the TGs, an ENM is established to stochastically evaluate the long-term impact of cyberattacks. (d) Reliability-based optimal power flow is conducted to estimate the load loss profiles of respective TGs. (e) The insurance premium of each TG is computed based on the corresponding marginal distribution of the loss.  

## A. Epidemic Network Model

Fig. 2 illustrates the attack graph of the proposed ENM. The vulnerability 𝑣ℎ is denoted as a colored oval VUL. Each node represents a vulnerability. In the proposed ENM, two types of anomalies, ROB and DoS, are considered. ROB attack decrypts the control center's server privilege by iterating queries to a control server. DoS attack on the substation server is triggered by unauthenticated clients issuing specially crafted messages. 

The successful exploitation condition of vulnerability 𝑣ℎ occurs when the server privilege is obtained by the attacker, denoted as 
𝑐ℎ. 

Vulnerability scores are determined by CVSS comprising the base score, temporal score, and environmental score that take a wide range of attack-related factors into account, including confidentiality, integrity, availability, attack complexity, privileges required, and exploit code maturity [24]. 

In Fig. 2, the attacker may compromise the substation 𝑆𝑞,1 to start the attack on the q-th TG. Specifically, the attacker deploys anomaly DoS(1) to gain access to the server privilege user(1) of 
𝑆𝑞,1 by exploiting <0, 1>. Once 𝑆𝑞,1 is compromised, adjacent 
<1, 2> of the control center 𝐶𝐶𝑞 can be exploited in a similar manner. Vulnerabilities in cascade are exploited sequentially. In 
𝑇𝐺𝑞, the substations and the control center are laid out according to cyber connections in the attack graph. Power dispatching action is feasible along the good routes connecting healthy nodes. Then the good routes are obtained using a routing algorithm such as Depth-First Search [25]. The substations outside of the good routes indicate disconnection from power generation capacity, resulting in load curtailment in the TG. More details can be referred to [26] for cyber network modeling.    
Physically, exploiting the vulnerability means the attacker breaches the server firewall to gain the server privilege to manipulatively command the substation. According to the attack graph, all preceding and current vulnerabilities should be exploited to compromise a substation server. However, since the substations located at any point of the attack graph may be compromised, an external infection term is established in the Cyber Epidemic Model to include such a possibility. After the substation server is compromised, the attacker may send counterfeit commands to the protective relays to disconnect the major substation IED from grid operations.  
The reliability-driven approach adopted in this study is different from contingency analysis on cascading failures. A graphical S-k contingency analysis based on extended enumeration considers the cascading failure by gradually removing the overloaded lines [27]. Worst cases with divergent load flow results are recorded to estimate the substation risk indices. Differently, in the MCS based reliability evaluation procedure, each component status is determined by comparing the random number generated and the FOR of that component. Then, a reliability-based OPF is performed for the sampled state to decide if there is load loss after re-dispatching the power to minimize the overall load loss based on the current system state. Finally, the overall reliability indices can be calculated by sampling enough system states with varying failure scenarios. 

 

_Definition I:_ Substation Compromise Time

$$T_{c}=\frac{\Sigma v_{h}\epsilon\nu\,t_{s}(v_{h})p(v_{h}\wedge c_{h})}{p(c_{h})}\tag{1A}$$
Job Assignment:               

$$t_{s}(v_{h})=\left\{\begin{array}{c}t_{s}(J_{1},\lambda,\mu)=\frac{1}{\lambda}\\ t_{s}(J_{2},\lambda,\mu)=\frac{1}{\lambda}+\frac{1}{2\lambda(1-p_{1})}\\ t_{s}(J_{3},\lambda,\mu)=\frac{1}{\lambda}+\frac{1}{2\lambda(1-p_{1})}+\frac{1}{3\lambda(1-p_{1})(1-p_{2})}\\ p_{1}=\Pr[Y_{1}>U]=\mu+\lambda\\ p_{2}=\Pr[\min\left\{Y_{1},Y_{2}\right\}>U]=\mu+2\lambda\end{array}\right.\tag{10}$$
Smart Monitoring: 

$$\begin{array}{c}{{(\lambda_{c},\mu_{c})=(\sum_{i=0}^{N}\lambda_{i}\,,\frac{\lambda_{c}*P u_{P}}{1-P u_{P}})}}\\ {{\left\{P_{U P b}=\frac{\mu_{b}}{\mu_{b}+\lambda_{b}}<P_{U P}=\frac{\mu_{c}}{\mu_{c}+\lambda_{c}}\right.}}\\ {{\left.\begin{array}{c}{{\mu_{b}=\mu_{0}}}\\ {{\mu_{b}\leq\mu_{i},1\leq i\leq N}}\\ {{\lambda_{b}=\sum_{i=0}^{N+M}\lambda_{i}}\end{array}\right.}}\end{array}\tag{1E}$$
{  
Epidemic Network Model:  

$p(v_{h})=\frac{\zeta(v_{h})}{10}$ (1F) $U(0.8,1)$ + $1_{(c_{h}=T)},h=1$
     𝑝(𝑐ℎ|𝑣ℎ) = {

$p(c_{h}|v_{h}\wedge(v_{1}\vee\ldots\vee v_{h-1})),n\geq h\geq2$ (1G) $p(v_{h}\wedge c_{h})=p(v_{h})*p(c_{h}|v_{h})$ (1H) $p(c_{h})=\sum_{l=1}^{n}p(v_{l}\wedge c_{h})$ (1I) **Subject to:**
 A security metric used extensively in reliability assessment is the SCT 𝑇𝑐. In *Definition 1*, 𝑇𝑐 quantifies the time taken by the attacker to bring the substation down. Considering the attack graph, 𝑇𝑐 is logically synthesized with a Bayesian Network [13]. 

The SCT 𝑇𝑐 is synthesized based on the individual sojourn times 
𝑡𝑠 of the vulnerabilities 𝑣ℎ. 𝑡𝑠 is positively correlated to 𝑇𝑐 and the overall system reliability. The smart technologies considered in this work including smart monitoring [14] and job thread assignment [15]. In the job assignment, 𝑡𝑠 corresponds to the memory thread resource in the cyber-physical elements assigned to the operational task. In smart monitoring, the CPS elements deploy preventive and corrective measures to boost substation security. The probability of exploiting vulnerability 𝑣ℎ depends on its score 𝜍(𝑣ℎ). The conditional probability 𝑝(𝑐ℎ|𝑣ℎ) can be determined by the vulnerability 𝑣ℎ  and all the preceding vulnerabilities. The total probability of successful exploitation 
𝑝(𝑐ℎ) is the summation of 𝑝(𝑣ℎ ∧ 𝑐ℎ).   

## B. Cyber Epidemic Across The Transmission Grids Definition 2: The Proposed Cyber Epidemic Model

𝑇𝑟𝑒𝑐
𝐸𝑁(𝑺𝒙) = 𝟏{ℙ𝑣≥𝑝𝑎𝑡𝑘}                     (2A) 
𝑝𝑎𝑡𝑘 =
𝑇𝑒𝑝𝑖+𝑇𝑟𝑒𝑐                               (2B) 
ℙ𝑣~𝑈(0,1)                               (2C) 
ζ = {1, … , 𝛾}                                (2D) 
𝔹ζ~𝐵𝑖𝑛(1, 𝑐)                                (2E) 
𝑇⃑ 𝑒𝑝𝑖 = [𝑇̂𝑐,1
…
𝑇̂𝑐,𝛾
𝑍𝑒𝑝𝑖]               (2F) 

𝑇⃑ 𝑟𝑒𝑐 = [𝑇̂𝑟,1
         …
            𝑇̂𝑟,𝛾
                𝑅𝑒𝑝𝑖]              (2G) 

𝑻̂𝒓 = {𝜀 ∑ 𝔹𝛤
𝛤
}                            (2H) 
𝑇𝑟𝑒𝑐 = max(𝑇⃑ 𝑟𝑒𝑐)                         (2I) 
𝑇𝑒𝑝𝑖 = 𝐸[𝑇⃑ 𝑒𝑝𝑖]                              (2J) 
The cyber epidemic model is initiated by a malicious attack described in *Definition 2*.  The cyber epidemic model that infects a vulnerability node may stochastically spread to an adjacent vulnerability node set ζ. State sequence of a specific substation is determined by the infection time vector 𝑇⃑ 𝑒𝑝𝑖 and recovery time vector 𝑇⃑ 𝑟𝑒𝑐 based on the SCTs of ζ and binomially distributed recovery times of ζ. To consider the cyber risks spreading in the large-scale network, external epidemic infection time 𝑍𝑒𝑝𝑖 and recovery time 𝑅𝑒𝑝𝑖 are respectively included in augmented 𝑇⃑ 𝑒𝑝𝑖 and 𝑇⃑ 𝑟𝑒𝑐. The intensity of the epidemic attack can be adjusted by the basic reproduction number 𝜀 and graphical edge coupling number 𝑐. The substation infection time 𝑇𝑒𝑝𝑖 and recovery time 
𝑇𝑟𝑒𝑐 are estimated by the maximum and expected values of the respective vectors. The probability of cyberattack infection 𝑝𝑎𝑡𝑘 
is calculated using 𝑇𝑒𝑝𝑖 and 𝑇𝑟𝑒𝑐. Then 𝑝𝑎𝑡𝑘 is compared with a uniform variate to determine whether the substation server is compromised by the cyberattack. The proposed Epidemic Network Model concerns a software-based cyberattack whose impacts would be reflected in the physical power system. When the substations become infected, their operations are compromised. Specifically, the physical loss due to the cyberattack is measured by load curtailment in the reliability analysis. The economic implication of the load loss on TGs is then evaluated in the insurance premium design. 

Optimization 1: Reliability-based Load Curtailment Estimation  
 
min {∑ 𝑲𝒙
𝑥
}𝜈                                (3A)  
Subject to: 

𝑩𝜽 + 𝑮 + 𝑲𝒙 = 𝑫𝒄𝒂𝒑                      ****                      (3B) 
|𝑭| ≤ 𝑭𝒄𝒂𝒑                                       (3C) 
𝟎 ≤ 𝑲𝒙 ≤ 𝑫𝒄𝒂𝒑                            (3D) 
𝟎 ≤ 𝑮 ≤ 𝐸𝑁(𝑺𝒙) ∗ 𝑮𝒄𝒂𝒑                    (3E) 
𝐸𝑁(𝑺𝒙) = 𝟏{ℙ𝑣≥𝑝𝑎𝑡𝑘}                           ****                           (3F) 
The substation state sequence 𝐸𝑁(𝑺𝒙) is sampled subject to cyber epidemic described in *Definition 2*, with binary values 1 
and 0 indicating the generation capacity 𝑮𝒄𝒂𝒑 connected to the specific substations to be either available or offline. If the substation server is infected by the cyberattack, the attacker could breach the server root privilege and send false tripping commands to the substation relays that cause generation offline. 

In *Optimization 1*, 𝐸𝑁(𝑺𝒙) ∗ 𝑮𝒄𝒂𝒑 determines the upper bounds of online capacity 𝑮 at each time step 𝜈. Together with the load capacity 𝑫𝒄𝒂𝒑 and thermal limit constraints 𝑭𝒄𝒂𝒑, the aggregate substation load loss ∑ 𝑲𝒙
𝑥
 is minimized at each time step 𝜈. The energy balance between the online generation supply and online load demand should always be maintained with load curtailment 
𝑲𝒙 being further bounded by the load capacity 𝑫𝒄𝒂𝒑.    


Fig. 3 depicts a typical process of epidemic propagation on a substation. The malicious attacker infiltrates the firewall of the control center through remote access network connected via a modem. If the Ethernet in the control center is breached, the attacker can gain access to the data storage, application server and operation of the workstation. Since WAP controls the substation operation via RTUs, the attacker may directly compromise the substation through the WAP without going through control center. Through infecting the network switch with malware, the attacker may further compromise the substation Intranet.  That is, the attacker obtains the privilege of the SCADA server, Human-Machine Interface and the WAP. If the WAP is hacked, false commands can be sent to RTUs to modify the trip settings in different relays. The breaker operating units connected to RTUs coordinate the relays to provide overcurrent protection, overvoltage protection and differential protection. By intentionally reducing the threshold value of the overcurrent relay, the circuit breakers can be falsely tripped when no physical fault condition is presented. A detailed survey further analyzed the impacts of various cyberattack scenarios in the power systems [28].   
 
In the following subsection, the cyber-physical enhancement 

## Strategies On The Substations Will Be Presented. C. Substation Cyber-Physical Enhancement

To enhance power system reliability, substation-oriented smart monitoring including SCADA systems and EMU may be worth investments. To highlight the merit of the cyber-physical smart grid with sensing and remedial equipment, reliability modeling of the smart monitoring devices performed in Fig. 4(a) shows a base case of two-state reliability model with failure rate and repair rate (𝜆𝑏, 𝜇𝑏). In Fig. 4(a), the smart monitoring reliability model has M+1 up states ( 𝑈𝑝0~𝑈𝑝𝑀 ) and N+1 
(𝐷𝑛0~𝐷𝑛𝑁 ) down states, with failure rate and repair rates 
(𝜆𝑖, 𝜇𝑖) among respective states. The smart monitoring model can be reduced to an equivalent composite two-state model with the composite failure rate and repair rate (𝜆𝑐, 𝜇𝑐) [14].  
For the substation servers, it is crucial to ensure IEDs within the substations with computing capability function normally. In typical operations of computing systems, portions of the memory are dynamically allocated to process-specific tasks. The scheduling strategies in [15] can be adapted to enable improved job thread assignment for our problem. Multiple server threads are scheduled to carry out the same task command of IEDs to heighten the computing dependability against uncertainties. 

Fig. 4(b) shows a basic 2-thread (𝐽2) fault-tolerant job thread assignment procedure assigned with a critical server task in the substation SCADA server. The procedure includes total 4 states: both threads *T1T2* carrying out single task, either thread (T1, T2) executing the same task, and the task is terminated when both threads fail F to perform the task. Similarly, Fig. 4(b) also shows a 3-thread (𝐽3) fault-tolerant job thread assignment procedure with 11 states: all 3 threads *T1T2T3* conducting single task, 2 of the threads (*T1T2, T1T3, T2T3*) carrying out the same task, within 2 selected threads one of the threads further fails (C1~C6), and the task is terminated when all 3 threads fail F to perform the task. The sojourn time of 𝐽2 and 𝐽3 are 𝑡𝑠(𝐽2, 𝜇, 𝜆) 
and 𝑡𝑠(𝐽3, 𝜇, 𝜆) , determined by the probabilities of state transition, duration of task operation, expected thread recruitment rate 𝜇 and thread residence rate 𝜆. In this study, duration of the task operation and residual time of the job thread executing the task are assumed to be exponentially distributed for simplicity. 

It will be shown in the case studies the combined application of job thread assignment and smart monitoring can achieve improved grid reliability.  

## D. Strength Of Interdependence

The SCT 𝑇𝑐 is the hypothetical effort where the individual 

substation privilege access would be obtained by the malicious attacker. Typically, SCTs of the target substations are considered mutually independent in reliability assessment. In this study, all TGs are assumed participants of the proposed mutual insurance to study Sol across the TGs. The sampled SCT vector $\widehat{\mathbf{T}}_{\mathbf{c}}$ incorporates a standard uniform variate set $\mathcal{U}$ into the SCT vector $\mathbf{T}_{\mathbf{c}}$ to produce the correlated loss pattern.

$$\widehat{\mathbf{T}}_{\mathbf{c}}=\mathbf{T}_{\mathbf{c}}*\mathcal{U}\tag{4}$$

Indirect approach is necessary to embed the correlation factor into the uniform variate. Multivariate normal variate $N_{\mathbf{c}}\!\sim\!N(\mathbf{0},\mathbf{\Sigma})$ is handy to allow specification of the correlation $r$ in the covariance matrix $\mathbf{\Sigma}$:

$$\mathbf{\Sigma}=(1+r)\mathcal{J}_{y}-I_{y}\tag{5}$$

where $y$ is the number of TGs, $\mathcal{J}_{y}$ is the all-one matrix, and $I_{y}$ is the identity matrix.

Substituting 
𝑁𝑐 = {𝑁𝑐1, . . . , 𝑁𝑐𝑦}
 into the cumulative distribution function of the standard normal distribution Φ, a set of uniform variates can be obtained: 
                                       𝒰 = Φ(𝑁𝑐)                                **                               (6) 
where 𝒰 = {𝒰𝑐1, . . . , 𝒰𝑐𝑦}  is the copula of the uniform distribution with correlation coefficient 𝑟. 

In the next section, a cyber-insurance principle for estimating the premiums of individual TGs will be introduced. 

## Iii. Proposed Insurance Premium Principle A. Fundamentals

Due to the growing adoption of ICTs in power systems, financial tools to hedge against the unforeseeable cyber-related monetary losses are emerging as an alternative or supplemental solution more recently.  
A crucial characteristic of the mutual insurance is to account for the financial impacts on economically related entities. Due to the high unpredictability of cyberattack-caused losses, power system application of the mutual insurance can be especially challenging. The intended mutual insurance premium design is tailored to TGs with a relatively small insured pool and large fluctuations in indemnities. An overview on the basics and existent work is provided before getting into the detailed insurance design. 

Definition 3: Tail Risk Measures for the loss ℒ 
  𝑉𝑎𝑅𝜛(ℒ) = inf{ℓ: 𝑃(ℒ > ℓ) ≤ 𝜛}, 𝜛 ∈ (0,1)    (7A)  
𝜋1(ℒ) =  𝑇𝐶𝐸𝜛(ℒ) = 𝐸[ℒ|ℒ > 𝑉𝑎𝑅𝜛(ℒ)]              (7B) 

Pr[ℒ >  𝑉𝑎𝑅𝜛(ℒ)] = 𝜛                   (7C)    
 𝑇𝐶𝐸𝜛(ℒ) >  𝑉𝑎𝑅𝜛(ℒ),  ∀ ℒ                 (7D) 
Pr[ℒ >  𝑇𝐶𝐸𝜛(ℒ)] ≤ 𝜛                   (7E) 
In *Definition 3*, VaR and TCE are statistical indices specifically for gauging risk percentile 𝜛. VaR is the 100𝜛% percentile of the loss ℒ. TCE is the average of the worst 100𝜛% scenarios of the loss ℒ. Given the same level of 𝜛, TCE is always larger than VaR. The relations among VaR, TCE and the loss ℒ  are described in (7). 

TCE premium design 𝜋1 [17] is a mutual insurance allocated from the insured TGs. 𝜋1 can gauge risk conservatively based on individual contributions to 𝑇𝐶𝐸𝜛(∑ ℒ𝑞
𝑞
) . In extremely catastrophic events, 𝜋1 would be beneficial. When the tail risk is small, 𝜋1 may induce heavy financial burden on the TGs if no major loss events occur.  
𝜋1 is devised with the third-party insurer operation in mind. 

When undesirably high premium quotes from 𝜋1  occur, an insurance coalition among the TGs comes into play handily. The coalitional insurance manages to scale down the premium risk loading by evenly distributing the premiums across participating entities. The coalitional premium 𝜋2 [18] is a mutual insurance based on the crowdfunding model distributing the risk affordably.  𝜋2 offers small risk loading at the cost of small loss coverage. 𝜋2  accounts for the fairness across the TGs. The commitment and the claim of 𝜋2  can be flexibly set on the participants' discretion; say, the TCE premium and the expected loss. In the following subsection, a novel Shapley premium design 𝜋3 is proposed as a middle ground between 𝜋1 and 𝜋2. 

## B. The Proposed Shapley Premium

The Shapley value [20]-[22] was introduced as a unique set of values fairly distributed across players in the cooperative games. Several basic properties should be mentioned before the premium design is presented. In a cooperative game 𝐺 = (𝑈, 𝜀) that contains a finite player universal set 𝑈 whose respective costs correspond to a subset S are 𝜀(𝑆), the Shapley value of the TG 𝑞  is defined as follows: 
∑
|𝑆|!(|𝑈|−|𝑆|−1)![𝜀(𝑆⋃{𝑞})−𝜀(𝑆)]
𝑆⊆𝑈\{𝑞}
ℂ𝑞(𝑈, 𝜀) =
|𝑈|!

         (8) 
Here a cooperative-game based Shapley value design is proposed for the power system cyber-insurance to achieve fair risk loading. The respective losses more evenly distributed in the proposed premium design than those in the coalitional insurance.  
 
Definition 4: The proposed Shapley mutual insurance principle 
𝜋3(ℒ𝑞) = ℂ𝑞(𝑈, 𝜀𝑞,𝑘)                        (9A) 
𝑦𝛿𝑞
𝑘(1 − 𝛿𝑞
𝜀𝑞,𝑘(𝑆) = 𝐶𝑘
𝑘)𝑦−𝑘 ∑
𝑞∈𝑆 𝑉𝑎𝑅𝜛(ℒ𝑞)
      (9B) 
𝑦−𝑘
𝑘−1
∗ =
𝛤𝑞,𝑘

$$\frac{y-\kappa}{y-1}\;TCE_{\varpi}\big{(}\mathcal{L}_{q}\big{)}+\frac{k-1}{y-1}\sum_{q\in U}TCE_{\varpi}(\mathcal{L}_{q})\tag{9C}$$ $$\Gamma_{q,k}^{\psi}=\psi(\Gamma_{q,k}^{*})=\Big{\{}\begin{matrix}\Gamma_{q,k}^{*},if\;\sum_{q\in S}\Gamma_{q,k}^{*}\leq\sum_{q\in U\setminus S}\mathbb{C}_{q}\\ \frac{\sum_{q\in U\setminus S}\Gamma_{q,k}^{*}}{\sum_{q\in S}\Gamma_{q,k}^{*}}\;\Gamma_{q,k}^{*},else\end{matrix}\tag{9D}$$

Shapley value $\mathbb{C}_{q}\big{(}U,\varepsilon_{q,k}\big{)}$ of the loss $\mathcal{L}_{q}$ serves as the 
Shapley premium 𝜋3, where the universal set 𝑈 includes all TGs in study. Given the subset 𝑆 including the selected TGs, Shapley cost of the q-th TG when 𝑘 TG(s) submit the claim is denoted as  
𝜀𝑞,𝑘(𝑆). The Shapley cost 𝜀𝑞,𝑘(𝑆)  handles typical risk lower than the tail risk when the cumulative loss distributions 𝛿𝑞  are smaller than  𝑉𝑎𝑅𝜛(ℒ𝑞), 𝑞 ∈ 𝑆. Since the typical risk in each TG varies with 𝑘 , the probability that the specific TGs are included in a subset 𝑆 is determined by an unfair coin-tossing model in 𝛿𝑞 . The cooperative game 𝐺  determines each ℂ𝑞(𝑈, 𝜀𝑞,𝑘) by assigning the expected values of its marginal contribution. The constraint of rationality ensures ℂ𝑞(𝑈, 𝜀𝑞,𝑘) 
that no feasible cooperation can be formed if the cooperative cost exceeds the sum of the respective costs. In other words, the Shapley cooperative game 𝐺 guarantees   

## 𝜓

Algorithm 1: Mutual Insurance for Power System Reliability  
Input: 𝐽𝑖, 𝜇, 𝜆, 𝐶𝑞, 𝑆𝑞,𝑥, 𝑣ℎ, r Output: 𝜋(ℒ𝑞), 𝜌(ℒ𝑞), 𝛤𝑞

/*Stochastic model preparation*/ 1:  FOREACH TG q 2:   FOREACH substation x  
3:   Evaluate (𝜆𝑐, 𝜇𝑐) based on Smart Monitoring. 4:   Substitute(𝜆𝑐, 𝜇𝑐) into 𝑡𝑠(𝐽𝑖) of Job Assignment.   
5:   END 
6:   Collect cyber network information (𝐶𝑞, 𝑆𝑞,𝑥, 𝑣ℎ). 
7:   FOREACH substation x 8:    By *Definition 1*,  
9:    Synthesize 𝑡𝑠(𝐽𝑖, 𝜆, 𝜇) and 𝑣ℎ in BN. 10:    Compute 𝑇𝑐 graphically using (𝐶𝑞, 𝑆𝑞,𝑥, 𝑡𝑠).   
11:   END 12: END /*Incorporate correlation in sampling*/ 
13: Synthesize 𝑻̂𝒄 via the indirect approach (4) - (6). 
14: Generate 𝐸𝑁(𝑺𝒙) by *Definition 2*. 15: Perform *Optimization 1* to obtain ℒ𝑞 in each TG q.                                  
/*Premium estimation in Section III*/ 
16: Estimate premium designs 𝜋1(ℒ𝑞), 𝜋2(ℒ𝑞), 𝜋3(ℒ𝑞).   
17: Estimate TG indemnities 𝛤𝑞
𝜓(𝜋1), 𝛤𝑞
𝜓(𝜋2), 𝛤𝑞
18: Procedure END the mutually insured individual a lower cost than its own cost. In this way, 𝜀𝑞,𝑘(𝑆) ensures that the Shapley premium 𝜋3(ℒ𝑞) is fairly allocated according to the loss ℒ𝑞 of the TG.  
∗   is the amount that each of the TGs The base indemnity 𝛤𝑞,𝑘
∗  is proportionally allocated between the self-indemnity can redeem from insurance when suffering from the loss event. 

𝛤𝑞,𝑘
term 𝑇𝐶𝐸𝜛(ℒ𝑞) and the group-indemnity term ∑
𝑞∈𝑈 𝑇𝐶𝐸𝜛(ℒ𝑞)
 
summed across all the participating TGs. The group-indemnity term weighs heavily as 𝑘 increases, and vice versa. The scaling function 𝜓(∙) ensures the budget sufficiency at various 𝑘 by scaling down 𝛤𝑞,𝑘
∗
 beyond the premium ℂ𝑞 . Denote the 
∗ ). The indemnity that the TG 𝑞 
𝜓 = 𝜓(𝛤𝑞,𝑘
indemnity at 𝑘 as 𝛤𝑞,𝑘
𝜓 = max
𝜓 .  Like can at most redeem from a loss would be 𝛤𝑞
𝑘
𝛤𝑞,𝑘
𝜋1 and 𝜋2, the formulation of 𝜋3 also incentivizes the security investment by reducing the premium payment. Besides, 𝜋3 is a mutual insurance that intends to be a financial mutual trust. Most TGs with positive risk loading provide some margin to cushion against uncertainty. In the mutual insurance, outliers struck by unexpectedly high damages would result in negative risk loading. Losses of other TGs could partially be covered by the mutual insurance premium. 

A major design goal of the insurance premium is to mitigate the risk insolvency by restraining the risk higher than the indemnity. TCE premium 𝜋1 offers good mitigation on the risk insolvency and serves as the claim term in 𝜋3. The nature of mutual insurance guarantees 𝜋3 premium package is nearly as affordable as  𝜋2. Combining the advantages of 𝜋1 and 𝜋2, the proposed 𝜋3  can substantially restrain the insolvency comparable to  𝜋1. The mutual insurance premium estimation procedure is summarized in **Algorithm 1**.         
The proposed cybersecurity mutual insurance model shown in Fig. 5 can be elaborated as follows: (1) Epidemic cyberphysical system model introduced in Section II. The cyber attacker injects the epidemic virus through Internet that penetrates the firewall of a TG. Within the TG, a control center and substations interconnected via the Local Area Network (LAN) are stochastically infected by the cyber epidemic. The proposed cyber-physical network model (*Definition 1*) accounts for the defensive capability of the TG via the hardware investment, software strategy development and its intrinsic vulnerabilities. With the above information, the substation state sequence (*Definition 2*) can be synthesized considering the SoI across the TGs. 

(2) Cyber-insurance design introduced in Section III. 

Taking the state sequence generated by the cyber epidemic, load curtailment of the respective TGs is calculated with the reliability analysis (*Optimization 1*). Using the marginal distribution of load loss statistics, the proposed Shapley premium of the individual TGs are estimated. In the following section, the proposed Shapley premium design at various SoI 
and cyber-physical defense investment will be verified in the simulated case studies.  

## Iv. Simulation Results

Case studies are performed to validate the proposed reliability assessment framework and cyber insurance model. As shown in Fig. 6, a benchmark IEEE RTS-GMLC is deployed [29]. The IEEE RTS-GMLC incorporates the increasing share of renewable energy resources such as wind and solar energies. To study the effectiveness of mutual insurance, the 3-area test system are divided into 5 TGs. The IEEE RTS-GMLC is further augmented by incorporating the epidemic cyberattack model. The cyberattack parameters of the epidemic network are assigned as follows: 𝑍𝑒𝑝𝑖 = 2000 hrs, 𝑅𝑒𝑝𝑖 = 4 hrs, 𝜀 = 2, and 
𝑐 = 0.8. 

A preliminary comparison is made on the system risk in the 

test system under various scenarios. Risk indices estimating load curtailment and fault coverage are adopted from [30]. Denote $LC$ as the load curtailment and $FC$ as the count of faulty buses at the $m$-th time step. The Expected $LC$ and $FC$ are defined as follows:

$$ELC=\frac{1}{N_{m}}\sum_{m=1}^{N_{m}}LC_{m}^{T}\tag{10}$$

$$EFC=\frac{1}{N_{m}}\sum_{m=1}^{N_{m}}FC_{m}^{T}\tag{11}$$

Parameters of the cyber-physical elements installed in the 
substations are listed in Table II. When the substation's smart monitoring is functional, the server is connected to other elements. Otherwise, the server is disconnected from other elements. Six scenarios are studied to demonstrate the effectiveness of the job assignment and smart monitoring. As shown in Table III, the deployment of job assignment and smart monitoring technologies effectively reduces the ELC and EFC. Reduced ELC and EFC indicate enhanced security and reliability of power supply. The job assignment facilitates Scenario 2 with 20% improvement from Scenario 1 in both ELC and EFC. With the smart monitoring technology enforced, Scenario 4 improves 7% on ELC and EFC over Scenario 1. In Scenarios 5 and 6, smart monitoring plus the job assignment can further improve several percent from Scenarios 2 and 3 with job assignment alone. 

 

TABLE II CYBER-PHYSICAL ELEMENT PARAMETERS 
Element 
Failure rate 
Repair rate 
Reliability 
State 
𝜆(ℎ−1) 
𝜇(ℎ−1) 
Server 
1/9200 
1/48 
0.9948 
𝐷𝑛𝑏 
(Attacked)  
Server 
1/14000 
1/48 
0.9966 
𝐷𝑛0 
Bus 
1/876000 
1/6 
0.999993 
𝐷𝑛1 
Switch 
1/45000 
1/48 
0.9989 
𝐷𝑛2 
Optical fiber 
1/500000 
1/12 
0.999976 
𝑈𝑝1 
EMU 
1/87600 
1/24 
0.9997 
𝑈𝑝2 
 
TABLE III RELIABILITY-ASSESSMENT RESULTS OF EXAMPLE SCENARIOS 
Scenarios 
ELC (p.u.) 
Improvement 
EFC 
Improvement 
1 
(𝐽1, 𝜇𝑏,𝜆𝑏) 
0.2398 
-- 
12.915 
-- 
2 
(𝐽2,𝜇𝑏, 𝜆𝑏) 
0.1852 
22.77% 
9.9233 
23.17% 
3 
(𝐽3,𝜇𝑏, 𝜆𝑏) 
0.1471 
38.66% 
7.7812 
39.75% 
4 
(𝐽1, 𝜇𝑐, 𝜆𝑐) 
0.2212 
7.66% 
11.930 
7.63% 
5 
(𝐽2, 𝜇𝑐, 𝜆𝑐) 
0.1693 
29.40% 
9.0138 
30.21% 
6 
(𝐽3, 𝜇𝑐, 𝜆𝑐) 
0.1334 
44.37% 
7.0239 
45.62% 

 
The reliability-based OPF is carried out in MCS based on the state sampling method. The sampled period is 40 years with hourly time steps. The server smart technology deployment within the substations determines the SCT. Cyberattacks that penetrate the substation servers may disturb the grid operation by sending spurious commands to disconnect generation from the grid, causing physical load losses. The load loss statistics is then converted into the monetary reliability worth to estimate the cybersecurity insurance premiums.  
To highlight the merits of the proposed Shapley premium design, two case groups are created to compare job thread assignment, smart monitoring, and correlation coefficients at varying degrees. Case Group 
1: 
Based on Scenario 
1  
(𝐽1, 𝜇𝑏, 𝜆𝑏) where in the substation only a single job thread is available without smart monitoring.  
Case Group 
2: 
Based on Scenario 
6  
(𝐽3, 𝜇𝑐, 𝜆𝑐)where the strongest job assignment and substation smart monitoring are enforced. To explore the loss characteristics in Case Group 1, Table IV summarizes the expected values, Standard Deviations, and Coefficients of Variation under various strengths of correlation 𝑟. CoV is obtained from the SD being divided by the expected value. The expected values come close to SDs, resulting in CoVs only fluctuating in a small range of [0.74 1.13]. Since a stronger 

(M$) AND COEFFICIENTS OF VARIATION OF MONETARY LOSS IN THE TGS 
𝑟 = 0 
TG1 
TG 2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
4.42 
7.10 
2.76 
3.49 
3.92 
SD 
4.83 
5.97 
2.88 
3.69 
3.29 
CoV 
1.09 
0.84 
1.05 
1.06 
0.84 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
4.60 
9.82 
3.66 
3.79 
4.02 
SD 
5.04 
10.5 
3.51 
4.29 
2.99 
CoV 
1.10 
1.07 
0.96 
1.13 
0.74 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
7.45 
12.7 
3.97 
4.74 
5.28 
SD 
5.89 
11.2 
3.34 
4.11 
4.67 
CoV 
0.79 
0.88 
0.84 
0.87 
0.88 
(M$) AND COEFFICIENTS OF VARIATION OF MONETARY LOSS IN THE TGS  
𝑟 = 0 
TG1 
TG2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
2.48 
3.96 
1.94 
1.53 
1.82 
SD 
3.30 
3.83 
2.04 
1.91 
1.91 
CoV 
1.33 
0.97 
1.05 
1.25 
1.05 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
2.79 
5.73 
2.60 
1.89 
2.69 
SD 
3.72 
6.92 
2.30 
2.46 
2.61 
CoV 
1.33 
1.21 
0.88 
1.30 
0.97 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
𝐸[ℒ𝑞] 
5.02 
7.01 
3.70 
2.19 
3.06 
SD 
4.95 
6.99 
3.51 
2.38 
3.46 
CoV 
0.99 
1.00 
0.95 
1.09 
1.13 

 correlation 𝑟 signifies the infectiousness of the epidemic model and tends to bring higher expected losses, the common cyber risk across TGs also increases. In Case Group 2, the incentive of investing on cyber-physical enhancement can be observed from Table V that expected losses are reduced substantially and reduction of SDs occurs to a lesser extent, with CoVs lying in [0.88 1.33].  
In Fig. 7, the sampled SoI among the TGs are demonstrated in the Pearson correlation matrix. The correlation is symmetric and correlation between each of the two TGs can be observed in the off-diagonal entries. Fig. 8(a) depicts the correlation matrix of the Case Group 1. When 𝑟 = 0, the SoI across the TGs are close to 0 with higher correlations between the neighboring TGs in the same areas. The correlations range around 0.45 as 𝑟 increases to 0.5. When 𝑟 = 1, the correlations across all TGs are above 0.9. The correlation matrix in Case Group 2 is as shown in Fig. 8(b). Due to reduced load losses, the correlations are in general weakened between the same pair of TGs in Case Group 1.      
Insurance premiums are designed to prepare TGs for catastrophic losses induced by probable cyberattack events. For interconnected TGs, mutual insurance accounting for respective marginal loss statistics would be a sensible option. The premium with a high-risk loading offers solid indemnity, which may however be less financially appealing to potential participants. An ideal premium design should be meticulously formulated to avoid excessive financial burdens while providing sufficient loss indemnities for the insured parties. The highly infectious nature of the cyber epidemic model dictates a heavily skewed tail risk. 

To validate the design of the proposed cyber-insurance principle, herein (a) TCE premium 𝜋1, (b) Coalitional premium 𝜋2, and (c) Shapley premium 𝜋3 of this study are compared at various degrees of correlation of the TGs. The TCE Premium is the most conservative design predominantly responsive to the tail risk, providing great redundancy at the cost of high-risk loading. On the contrary, the Coalitional Premium is the most affordable package by excluding extreme high-loss events with low probabilities. The Shapley Premium is cooperative and tailored to add further coverage against the tail risk, striking a balance between the affordability and loss coverage. To gauge the relative premium burden against the expected risk, RLC is defined as follows:  
𝜌(ℒ𝑞) = 𝜋(ℒ𝑞)/𝐸[ℒ𝑞] − 1                    (12) 
where 𝜌(ℒ𝑞) should be generally positive to gather sufficiency budget for loss coverage. While positive RLC is preferable against the unexpected extreme risk, excessively high RLC would discourage the TGs from insurance participation.  
In [17], the indemnities of 𝜋1(ℒ𝑞) are not clearly specified 

since the original design is tailored to a third-party insurer. In this paper, all premium designs are assumed to be mutual insurance. All participating entities are both insurers and insureds. For the sake of brevity, the indementies of $\pi_{1}\big{(}\mathcal{L}_{q}\big{)}$ are proportionally allocated based on $\Gamma_{q}^{\psi}(\pi_{2})$:

$$\Gamma_{q}^{\psi}(\pi_{1})=\sum_{q}\pi_{1}\big{(}\mathcal{L}_{q}\big{)}*\frac{\Gamma_{q}^{\psi}(\pi_{2})}{\sum_{q}\Gamma_{q}^{\psi}(\pi_{2})}\tag{13}$$

In Tables VI and VII, $\pi_{1}$, $\pi_{2}$, and $\pi_{3}$ are evaluated based on 
the loss statistics extracted from the two case groups with heavy tail risks. Characteristics of each design will be further elaborated numerically as follows. 

The premiums of Case Group 1 are shown in Table VI. In each TG, 𝜋1, 𝜋2, and 𝜋3 are positively correlated with the strength of correlation 𝑟. 𝜋1 has the most conservative payment schedule and can be financially burdensome. 𝜋1  may penalize the participants with heavy risk loading when extreme catastrophic events do not happen. Cost-effectiveness of 𝜋1 is unacceptably low because the maximum of 𝜌1 exceeds 3. On the flip side, 𝜋2 
is an entry-level premium design devised to be the most affordable and evenly distributed package across the TGs.  𝜋2 
offers small indemnities and the premiums collected from the TGs. 

𝑟 = 0 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
19.0 
20.3 
11.3 
12.6 
12.6 
𝜓(𝜋1)    
15.3 
18.8 
13.1 
14.1 
14.6 
𝛤𝑞
𝜌1 
3.30 
1.87 
3.11 
2.60 
2.22 
𝜋2 
4.93 
6.51 
4.35 
4.78 
5.07 
𝜓(𝜋2)  
8.74 
10.7 
7.49 
8.04 
8.36 
𝛤𝑞
𝜌2 
0.12 
-0.08 
0.58 
0.37 
0.29 
𝜋3 
4.06 
7.97 
3.25 
4.92 
5.91 
𝜓(𝜋3) 
17.0 
18.1 
10.1 
11.2 
11.3 
𝛤𝑞
𝜌3 
-0.08 
0.12 
0.18 
0.41 
0.51 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
19.9 
40.7 
12.3 
13.5 
12.8 
𝜓(𝜋1)    
19.0 
26.5 
17.7 
17.8 
18.2 
𝛤𝑞
𝜌1 
3.32 
3.14 
2.37 
2.57 
2.19 
𝜋2 
5.33 
7.37 
5.28 
5.26 
5.48 
𝜓(𝜋2)  
9.93 
13.8 
9.22 
9.31 
9.49 
𝛤𝑞
𝜌2 
0.16 
-0.25 
0.44 
0.39 
0.36 
𝜋3 
4.39 
8.26 
6.47 
5.99 
6.81 
𝜓(𝜋3) 
11.6 
23.7 
7.17 
7.85 
7.46 
𝛤𝑞
𝜌3 
-0.05 
-0.16 
0.77 
0.58 
0.69 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
20.5 
40.8 
12.5 
13.9 
17.9 
𝜓(𝜋1)    
21.8 
27.9 
17.8 
18.7 
19.3 
𝛤𝑞
𝜌1 
1.75 
2.20 
2.14 
1.94 
2.39 
𝜋2 
7.55 
9.39 
6.03 
6.40 
6.44 
𝜓(𝜋2)  
14.1 
18.1 
11.5 
12.1 
12.5 
𝛤𝑞
𝜌2 
0.01 
-0.26 
0.52 
0.35 
0.22 
𝜋3 
9.85 
10.9 
7.21 
8.28 
6.86 
𝜓(𝜋3) 
16.2 
32.2 
9.84 
11.0 
14.2 
𝛤𝑞
𝜌3 
0.32 
-0.15 
0.81 
0.75 
0.30 

## 

TABLE VII ACTUARIAL INSURANCE PREMIUMS (M$) IN CASE GROUP 2 
𝑟 = 0 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
12.1 
12.2 
7.51 
7.49 
7.60 
𝜓(𝜋1)    
9.47 
10.5 
9.11 
8.84 
9.03 
𝛤𝑞
𝜌1 
3.90 
2.08 
2.87 
3.91 
3.18 
𝜋2 
2.80 
3.77 
2.77 
2.43 
2.67 
𝜓(𝜋2)  
4.91 
5.42 
4.72 
4.58 
4.68 
𝛤𝑞
𝜌2 
0.13 
-0.05 
0.43 
0.60 
0.47 
𝜋3 
2.21 
4.51 
2.78 
0.87 
1.90 
𝜓(𝜋3) 
7.72 
7.75 
4.78 
4.77 
4.84 
𝛤𝑞
𝜌3 
-0.11 
0.14 
0.43 
-0.43 
0.04 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
13.7 
26.4 
8.00 
9.19 
8.19 
𝜓(𝜋1)    
12.5 
17.1 
12.2 
11.1 
12.4 
𝛤𝑞
𝜌1 
3.89 
3.60 
2.07 
3.87 
2.04 
𝜋2 
3.22 
4.37 
3.52 
2.89 
3.57 
𝜓(𝜋2)  
6.02 
8.23 
5.88 
5.34 
5.95 
𝛤𝑞
𝜌2 
0.15 
-0.24 
0.35 
0.53 
0.32 
𝜋3 
2.27 
4.69 
5.30 
1.32 
2.42 
𝜓(𝜋3) 
7.41 
14.3 
4.34 
4.98 
4.44 
𝛤𝑞
𝜌3 
-0.19 
-0.18 
1.04 
-0.29 
-0.10 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
𝜋1 
17.3 
26.7 
11.8 
9.95 
14.2 
𝜓(𝜋1)    
17.2 
20.0 
15.3 
13.1 
14.4 
𝛤𝑞
𝜌1 
2.45 
2.80 
2.19 
3.54 
3.64 
𝜋2 
5.18 
5.84 
4.72 
3.78 
4.08 
𝜓(𝜋2)  
9.01 
10.5 
8.02 
6.89 
7.54 
𝛤𝑞
𝜌2 
0.03 
-0.17 
0.28 
0.72 
0.33 
𝜋3 
6.24 
6.55 
6.10 
1.80 
3.11 
𝜓(𝜋3) 
10.6 
16.3 
7.20 
6.07 
8.65 
𝛤𝑞
𝜌3 
0.24 
-0.07 
0.65 
-0.18 
0.02 

 
𝜌2  of some TGs can be slightly negative with indemnities supplemented by other TGs.  However, the worse risk of 𝜋2 
beyond expected losses could barely be covered. 𝜋3 rewards TGs of relatively low risk loading with high indemnities. While 
𝜋1 provides higher indemnities than 𝜋3, 𝜋3 offers comparable affordability to the coalitional platform of 𝜋2. The proposed 𝜋3 
substantially alleviates the insolvency hazard of 𝜋2. 𝜌2 spans  

PREMIUMS IN CASE GROUPS 1, 2 
Case Group 1 
𝑟 = 0 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
7.50 
7.50 
0  
0 
0 
Φ(𝜋2) 
10.0 
17.5 
7.50 
15.0 
10.0 
Φ(𝜋3) 
7.50 
7.50 
5.00 
7.50 
5.00 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
5.00 
7.50 
0 
0 
0 
Φ(𝜋2) 
7.50 
27.5 
12.5 
17.5 
5.00 
Φ(𝜋3) 
7.50 
7.50 
12.5 
17.5 
5.00 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
0  
12.5 
0 
0 
0 
Φ(𝜋2) 
15.0 
20.0 
7.50 
10.0 
10.0 
Φ(𝜋3) 
15.0 
12.5 
10.0 
15.0 
10.0 
Case Group 2 
𝑟 = 0 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
7.50 
10.0 
0 
0 
2.50 
Φ(𝜋2) 
20.0 
25.0 
10.0 
5.00 
2.50 
Φ(𝜋3) 
7.50 
20.0 
10.0 
5.00 
2.50 
𝑟 = 0.5 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
7.50 
7.50 
0 
0 
0 
Φ(𝜋2) 
10.0 
27.5 
15.0 
7.50 
20.0 
Φ(𝜋3) 
7.50 
7.50 
15.0 
7.50 
20.0 
𝑟 = 1 
TG1 
TG2 
TG3 
TG4 
TG5 
Φ(𝜋1) 
2.50 
7.50 
0 
0 
2.50 
Φ(𝜋2) 
12.5 
25.0 
15.0 
5.00 
7.50 
Φ(𝜋3) 
10.0 
7.50 
15.0 
5.00 
5.00 

 
from -0.26 to 0.58. By contrast, 𝜌3 is dispersed in [-0.16 0.81], a typical range of risk loading. 𝜋3 offers a wider margin in risk loading than 𝜋2  to guarantee sufficient budget to cover individual risk.   
In Table VII, risk loading in Case Group 2 generally increase due to the enhanced security measure that reduces tail risk profile.  𝜌1 has a maximum close to 4 and could be too high to motivate entities to participate in. 𝜋2  is evenly distributed against average risk, with 𝜌2 lying in [-0.24 0.72]. 𝜋3 renders ideal risk loading 𝜌3  to rarely exceed 1. High capacity of indemnity and low risk loading make the proposed 𝜋3  a potentially compelling insurance model in practice.  
The probability of insolvency Φ(𝜋) is another risk measure which quantifies the capability of the insurance to mitigate the insolvency. Φ(𝜋) is defined as the probability that the loss is greater than the indemnity: 
 

$$\Phi(\pi)=\Pr[{\cal L}_{q}>\Gamma_{q}^{\Psi}(\pi)]\tag{14}$$

As shown in Table VIII, in Case Group 1, $\pi_{1}$ generally $\pi_{1}$ has the best $\pi_{1}$ and $\pi_{2}$ are all $\pi_{1}$ and $\pi_{2}$.

provides the best insolvency alleviation with lowest probabilities of insolvency. In fact, 𝜋1 is such a conversative premium design against risk that the insolvency in some cases is 0. While 𝜋3 leads to the insolvency being lower than 𝜋2 and greater than 𝜋1, 
𝜋3 has the affordability superior to 𝜋1. In Case Group 2, when the cyber risk is significantly reduced, 𝜋3  can restrain the insolvency to be about as low as that of 𝜋1.  Thus, 𝜋3 offers an economical option with relatively sufficient insolvency mitigation.  

## V. Concluding Remarks

In this paper, a mutual insurance premium principle is designed to fairly share cyber risks across the participating TGs and control the overall insolvency risk. This study is among the first endeavors to approach the cyber-insurance by estimating the insolvency. In the case studies, it is shown the smart monitoring and job thread assignment solutions can work standalone or together to boost the reliability of TGs. Reduced insolvency probability is offered by the proposed Shapley premium while remaining as affordable as the coalitional premium. More challenges may occur when real-life variables are factored in. Since any two power system servers are to some extent connectable from each other, establishing the topology of cyber node connections could be complicated. Selecting weights to prioritize the crucial edges in the cyber node graph could be essential. There are also challenges on the actuarial end. First, accurate cyber risk estimation for specific systems would rely on long-term historical data set collection. How much risk loading a premium design reserved should be sufficient against tail risk is still left to further exploration. Second, the proposed Shapley insurance scheme is designed to achieve two goals: insolvency risk control and fair distribution of indemnity. Although these goals are achieved most of the time, there are exceptions especially when some participants are struck by unexpectedly high losses due to inadequate self-protection. This shall motivate future work in designing more insurance schemes to reflect selfprotection level and thus incentivize cyber-security investment. 

## References

[1] R. V. Yohanandhan, R. M. Elavarasan, P. Manoharan and L. Mihet-Popa, 
"Cyber-Physical Power System (CPPS): A Review on Modeling, Simulation, and Analysis With Cyber Security Applications," in IEEE Access, 
vol. 
8, 
pp. 
151019-151064, 
2020, 
doi: 
10.1109/ACCESS.2020.3016826. 
[2] M. Barrett, Framework for Improving Critical Infrastructure Cybersecurity 
Version 1.1, NIST Cybersecurity Framework, 2018 [Online]. Available: https://doi.org/10.6028/NIST.CSWP.04162018. 
[3] A. Huseinović, S. Mrdović, K. Bicakci and S. Uludag, "A Survey of 
Denial-of-Service Attacks and Solutions in the Smart Grid," in IEEE Access, 
vol. 
8, 
pp. 
177447-177470, 
2020, 
doi: 
10.1109/ACCESS.2020.3026923.  
[4] J. Hong, R. F. Nuqui, A. Kondabathini, D. Ishchenko and A. Martin, 
"Cyber Attack Resilient Distance Protection and Circuit Breaker Control for Digital Substations," in IEEE Transactions on Industrial Informatics, vol. 15, no. 7, pp. 4332-4341, July 2019, doi: 10.1109/TII.2018.2884728. 
[5] H. Lin, Z. T. Kalbarczyk and R. K. Iyer, "RAINCOAT: Randomization of 
Network Communication in Power Grid Cyber Infrastructure to Mislead Attackers," in IEEE Transactions on Smart Grid, vol. 10, no. 5, pp. 4893- 4906, Sept. 2019, doi: 10.1109/TSG.2018.2870362. 
[6] T. Duan et al., "Intelligent Processing of Intrusion Detection Data," in 
IEEE 
Access, 
vol. 
8, 
pp. 
78330-78342, 
2020, 
doi: 
10.1109/ACCESS.2020.2989498. 
[7] L. Wei, A. I. Sarwat, W. Saad and S. Biswas, "Stochastic Games for Power 
Grid Protection Against Coordinated Cyber-Physical Attacks," in IEEE Transactions on Smart Grid, vol. 9, no. 2, pp. 684-694, March 2018, doi: 10.1109/TSG.2016.2561266. 
[8] A. Binbusayyis and T. Vaiyapuri, "Identifying and Benchmarking Key 
Features for Cyber Intrusion Detection: An Ensemble Approach," in IEEE Access, 
vol. 
7, 
pp. 
106495-106513, 
2019, 
doi: 
10.1109/ACCESS.2019.2929487. 
[9] K. Yamashita, C. -W. Ten, Y. Rho, L. Wang, W. Wei and A. Ginter, 
"Measuring Systemic Risk of Switching Attacks Based on Cybersecurity Technologies in Substations," in IEEE Transactions on Power Systems, vol. 
35, 
no. 
6, 
pp. 
4206-4219, 
Nov. 
2020, 
doi: 
10.1109/TPWRS.2020.2986452.  
[10] K. Huang, C. Zhou, Y. Qin and W. Tu, "A Game-Theoretic Approach to 
Cross-Layer Security Decision-Making in Industrial Cyber-Physical Systems," in IEEE Transactions on Industrial Electronics, vol. 67, no. 3, pp. 2371-2379, March 2020, doi: 10.1109/TIE.2019.2907451. 
[11] M. Li, M. Ni, Y. Xue, X. Chen and W. Ding, "Hybrid Calculation 
Architecture of Cyber Physical Power System Based on Correlative Characteristic Matrix Model," 2018 IEEE 8th Annual International Conference on CYBER Technology in Automation, Control, and Intelligent 
Systems 
(CYBER), 
2018, 
pp. 
584-588, 
doi: 
10.1109/CYBER.2018.8688204. 
[12] Y. Chen, J. Hong and C. -C. Liu, "Modeling of Intrusion and Defense for 
Assessment of Cyber Security at Power Substations," in IEEE Transactions on Smart Grid, vol. 9, no. 4, pp. 2541-2552, July 2018, doi: 10.1109/TSG.2016.2614603. 
[13] B. Cai et al., "Application of Bayesian Networks in Reliability Evaluation," 
in IEEE Transactions on Industrial Informatics, vol. 15, no. 4, pp. 2146- 2157, April 2019, doi: 10.1109/TII.2018.2858281. 
[14] B. Falahati, Y. Fu and M. J. Mousavi, "Reliability Modeling and 
Evaluation of Power Systems With Smart Monitoring," in IEEE Transactions on Smart Grid, vol. 4, no. 2, pp. 1087-1095, June 2013, doi: 10.1109/TSG.2013.2240023.  
[15] P. Ghazizadeh, R. Florin, A. G. Zadeh and S. Olariu, "Reasoning About 
Mean Time to Failure in Vehicular Clouds," in IEEE Transactions on 
Intelligent Transportation Systems, vol. 17, no. 3, pp. 751-761, March 2016, doi: 10.1109/TITS.2015.2486523.  

[16] M. Xu and L. Hua. "Cybersecurity insurance: Modeling and pricing." 
North American Actuarial Journal, vol. 23, no. 2, pp. 220-249, 2019. 
[17] P. Lau, W. Wei, L. Wang, Z. Liu and C. -W. Ten, "A Cybersecurity 
Insurance Model for Power System Reliability Considering Optimal Defense Resource Allocation," in IEEE Transactions on Smart Grid, vol. 11, no. 5, pp. 4403-4414, Sept. 2020, doi: 10.1109/TSG.2020.2992782. 
[18] P. Lau, L. Wang, Z. Liu, W. Wei and C. -W. Ten, "A Coalitional Cyber-
Insurance Design Considering Power System Reliability and Cyber Vulnerability," in IEEE Transactions on Power Systems, vol. 36, no. 6, pp. 
5512-5524, Nov. 2021, doi: 10.1109/TPWRS.2021.3078730.  
[19] I. Vakilinia and S. Sengupta, "A Coalitional Cyber-Insurance Framework 
for a Common Platform," in IEEE Transactions on Information Forensics and Security, vol. 14, no. 6, pp. 1526-1538, June 2019, doi: 10.1109/TIFS.2018.2881694.  
[20] D. Monderer, D. Samet and L. S. Shapley, "Weighted values and the core," 
International Journal of Game Theory, vol. 21, no. 1, pp. 27-39, 1992. 
[21] S. Béal, S. Ferrières, E. Rémila and P. Solal, "The proportional Shapley 
value and applications," Games and Economic Behavior, vol. 108, pp. 93- 112, 2018, https://doi.org/10.1016/j.geb.2017.08.010. 
[22] E. Algaba, V. Fragnelli and J. Sánchez-Soriano, "Handbook of the Shapley 
value," CRC Press, Boca Raton, FL, USA, 2019. 
[23] B. Falahati and Y. Fu, "Reliability Assessment of Smart Grids Considering 
Indirect Cyber-Power Interdependencies," in IEEE Transactions on Smart Grid, 
vol. 
5, 
no. 
4, 
pp. 
1677-1685, 
July 
2014, 
doi: 
10.1109/TSG.2014.2310742. 
[24] M. Schiffman, "Common Vulnerability Scoring System (CVSS)," 
[Online]. Available:  http://www.first.org/cvss/ 
[25] Y. Satotani and N. Takahashi, "Depth-First Search Algorithms for Finding 
a Generalized Moore Graph," TENCON 2018 - 2018 IEEE Region 10 Conference, 2018, pp. 0832-0837, doi: 10.1109/TENCON.2018.8650418.  
[26] C. Wang, T. Zhang, F. Luo, F. Li and Y. Liu, "Impacts of Cyber System 
on Microgrid Operational Reliability," in IEEE Transactions on Smart Grid, 
vol. 
10, 
no. 
1, 
pp. 
105-115, 
Jan. 
2019, 
doi: 
10.1109/TSG.2017.2732484.  
[27] Z. Yang, C. Ten and A. Ginter, "Extended Enumeration of Hypothesized 
Substations Outages Incorporating Overload Implication," in IEEE Transactions on Smart Grid, vol. 9, no. 6, pp. 6929-6938, Nov. 2018, doi: 10.1109/TSG.2017.2728792. 
[28] C. -W. Ten, K. Yamashita, Z. Yang, A. V. Vasilakos and A. Ginter, 
"Impact Assessment of Hypothesized Cyberattacks on Interconnected Bulk Power Systems," in IEEE Transactions on Smart Grid, vol. 9, no. 5, pp. 4405-4425, Sept. 2018, doi: 10.1109/TSG.2017.2656068.  
[29] C. Barrows et al., "The IEEE Reliability Test System: A Proposed 2019 
Update," in IEEE Transactions on Power Systems, vol. 35, no. 1, pp. 119- 127, Jan. 2020, doi: 10.1109/TPWRS.2019.2925557. 
[30] G. Cao et al., "Operational Risk Evaluation of Active Distribution 
Networks Considering Cyber Contingencies," in IEEE Transactions on Industrial Informatics, vol. 16, no. 6, pp. 3849-3861, June 2020, doi: 10.1109/TII.2019.2939346. 
 