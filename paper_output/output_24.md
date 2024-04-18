# Virtuoso: An Open-Source, Comprehensive And Modular Simulation Framework For Virtual Memory Research

Konstantinos Kanellopoulos1
Konstantinos Sgouras2
Onur Mutlu1
ETH Zürich1 University of Athens2

## 1 Introduction & Background

Virtual memory is a cornerstone of modern computing systems.

Introduced as one of the earliest instances of hardware-software co-design, VM facilitates programmer-transparent memory management, data sharing, process isolation and memory protection.

In light of current application trends with large data sets and irregular memory access patterns [4, 5, 14, 42, 47] and as we transition to much larger address spaces [8] (e.g., hybrid memory systems with both volatile and non-volatile memories [1, 37]) and heterogeneous memory systems [32], the overheads of virtual memory are likely to increase [39]. Research span across various solutions to reduce the overheads of virtual memory in the context of (i) improving the efficiency of the TLB subsystem [17, 22, 33, 35, 48] (e.g., software-based TLB [35] etc.), (ii) the efficiency of page table structures [30, 31, 44, 50, 55] (e.g., hash-based page tables [44, 55]), (iii)
accelerating address translation in virtualized environments [16,
25, 30, 46, 51], (iv) leveraging contiguity between virtual/physical addresses to enable offset-based address translation [22, 28, 39,
40, 56] (e.g., range-based translation [27]), (v) enabling hash-based virtual-to-physical address mapping [3, 34, 53], (vi) enabling intermediate address spaces to perform address translation only upon LLC misses [21, 45], (vii) designing efficient large page allocation techniques [9, 20, 26, 38, 56] (e.g., Transparent Huge Pages [20])
and (viii) reducing the overheads of minor page faults [43, 52].

## 2 Lack Of Comprehensive Virtual Memory Simulation Framework

Evaluating the efficiency of various virtual memory (VM) designs is crucial (i) given their significant impact on the system, including the CPU caches, the main memory, and the storage device and (ii)
given that different system architectures might benefit from various VM techniques. Such an evaluation is not straightforward, as it heavily hinges on modeling the interplay between different VM
techniques and the interactions of VM with the system architecture. To better illustrate the interplay between VM techniques, for example, the memory management policies can directly affect TLB
performance [22], contiguity-aware VM solutions significantly influence memory fragmentation [40], affecting disk accesses, while the contiguity between virtual and physical addresses is pivotal for the efficiency of prefetching [10]. As also highlighted in prior works [31, 50], the design of the page table can negatively impact main memory efficiency. With respect to system architecture, mobile devices, with their resource constraints, might benefit from lightweight VM designs that minimize energy overheads. In contrast, cloud architectures, with abundant resources, might favour VM designs that maximize throughput and scalability [7]. In contrast, commercial multi-core architectures, with multiple threads running concurrently, might favour VM designs that reduce contention and ensure efficient memory bandwidth distribution among cores.

In the face of these intricacies, assessing the merits and drawbacks of old, modern and futuristicVM proposals becomes a highlychallenging task without a comprehensive simulation tool. Modern simulators, however, struggle to keep up with the rapid VM research developments, lacking the capability to model a wide range of contemporary VM techniques and their interactions. Table 1 summarizes the VM techniques that are supported by existing simulators. For example, Sniper [19], does not include a realistic model for the page table walk latency, neither emulates nor simulates the page fault handler and does not emulate memory management.

The system call emulation mode of gem5 [18] does not include detailed TLB models (e.g., all TLBs are considered fully-associative), and neither emulates nor simulates page fault handling and large page allocation. At the same time, the full system simulation of gem5 emulates and simulates the actual OS including realistic memory management, large page allocation but at the cost of (i) high programmability effort, e.g., enabling contiguity-based translation requires modifying the kernel code in a functional manner and co-design it with the simulated hardware and (ii) high simulation time (e.g., simulating multi-programmed workloads in parallel is not supported). Given the wide range of research directions and the synergies between different VM components, our goal in this work is to provide researchers with an open-source, comprehensive and modular tool to study and evaluate various VM techniques and memory management schemes.

## 3 Our Approach: Virtuoso

To this end, we present Virtuoso, an open-source, comprehensive and modular simulation framework that models various VM designs to establish a common ground for virtual memory research.

Virtuoso is built on top of sniper [19] and, as show in Table 1, extends it with (i) state-of-the-art TLB techniques and organizations,
(ii) four different page table designs from cutting-edge academic proposals, (iii) support for easily configurable Nested MMUs, required in virtualized environments(e.g., MMU with Nested TLB, Nested Walk etc.), (iv) translation techniques that exploit virtual and physical memory contiguity [2, 28] (v) support for address translation schemes that rely on intermediate address spaces [41,
45], (vi), metadata management schemes that enhance security and performance [13, 36], (vii) a complete memory management emulator that includes a reservation-based programmer-transparent large page allocator and (viii) a new simulation methodology that involves bi-directional inter-process communication between Virtuoso and software to estimate the performance of OS kernel code with a focus on the minor page fault handler. Even though Virtuoso is built on top of Sniper, it is highly-modular, avoiding the use of simulator-specific semantics. The only requirement to integrating Virtuoso in any architectural simulator, is attaching it to the simulator's memory subsystem model (e.g. interface to access the L1 data cache).

## Virtual Memory Components Supported By Existing Simulators And Virtuoso

Simulator/
Component
TLB
Subsystem
Page Table
Design
Contiguity
Schemes
Intermediate
Address Space
Hash-based
Translation
Metadata
Management
Memory
Management
Page Fault
Modelling
SimpleScalar [12]
L1 D-TLB & L1 D-ITLB
✖
✖
✖
✖
✖
✖
✖
PTLSim [15]
L1 D-TLB & L1 D-ITLB
Simplistic Walker
✖
✖
✖
✖
✖
✓
Scarab [6]
✖
✖
✖
✖
✖
✖
✖
✖
Ramulator [29]
✖
✖
✖
✖
✖
✖
✖
✖
ZSim [24]
✖
✖
✖
✖
✖
✖
✖
✖
Multi2Sim [23]
L1 D-TLB & L1 D-ITLB
✖
✖
✖
✖
✖
✖
✖
Gem5 SE [18]
2-Level TLB Hierarchy
4-level Radix-Tree Walker
✖
✖
✖
✖
✖
✖
Gem5 FS [18]
2-Level TLB Hierarchy
4-level Radix-Tree Walker
✖
✖
✖
✖
THP [20]
✓
Champsim [49]
2-Level TLB Hierarchy
4-level Radix-Tree Walker
✖
✖
✖
✖
✖
✖
Sniper [19]
2-Level TLB Hierarchy
Static PTW latency
✖
✖
✖
✖
✖
✖
Multi-page Size TLBs
(Serial probing)
Hash Table with
Open-Addressing and PTE
Clustering [31]
Configurable
TLB hierarchy
Memory-Efficient Hash
Table [55]
Offset-based
translation with
Redundant
Memory
Mappings [27]
Virtual Block
Interface with
configurable
past-LLC
translation [41]
Virtuoso
Page-size Predictors
Elastic Cuckoo
Hash Table [44]
Eager Paging to allocate
large contiguous
blocks [27]
TLB prefetching techniques
Configurable Radix

To demonstrate the versatility and utility of Virtuoso we examine four new example case studies.

- We analyze the performance, memory and cache footprint
of different page table designs under different system workloads (e.g, memory fragmentation and memory bandwidth) and different execution environments (native vs virtualized execution).
- We perform a head-to-head comparison between large-page,
intermediate address space and contiguity based schemes taking into consideration (i) address translation latency and
(ii) impact on memory fragmentation.
- We examine the performance and microarchitectural impact of Virtuoso's reservation-based large page allocator
across different fragmentation levels and compare it against Linux THP.
- We evaluate the microarchitectural impact caused by minor page faults in the presence of different page allocation policies and contiguity-aware translation approaches.

## 4 Our Contributions

In this work, we make the following contributions:

- We present Virtuoso, an open-source, comprehensive and
modularsimulatorthat models various virtual memory components and schemes to establish a common ground for
virtual memory research.
- We demonstrate the versatility and the potential of Virtuoso with four new case studies. A minimal, alpha version of the simulator is used in two recent research works [53, 54]. Virtuoso is freely open-source and can be found at https://github.com/CMU-SAFARI/Virtuoso.

Memory Management
Emulation
Memory tagging
with XMem [36]
Buddy Allocator with
pre-created memory allocation snapshots
Hybrid address
mapping with
Utopia [53]
Reservation-based
THP [11]
Bi-directional
inter-process
communication
between Virtuoso and
custom OS Software to
emulate the
functionality of PF and
simulate the
architectural events of
PF

## References

[1] Chloe Alverti, Vasileios Karakostas, Nikhita Kunati, Georgios Goumas, and
Michael Swift. DaxVM: Stressing the Limits of Memory as a File Interface. In
MICRO 2022.
[2] Arkaprava Basu, Jayneel Gandhi, Jichuan Chang, Mark D. Hill, and Michael M.
Swift. Efficient Virtual Memory for Big Memory Servers. In ISCA 2013.
[3] Krishnan Gosakan, Jaehyun Han, William (Massachusetts Inst. of Technology)
Kuszmaul, Ibrahim Nael Mubarek, Nirjhar Mukherjee, Guido Tagliavini, Evan
West, Michael Bender, Abhishek Bhattacharjee, Alex Conway, Martin Farach-
Colton, Jayneel Gandhi, Rob Johnson, Sudarsun Kannan, and Donald Porter.
Mosaic Pages: Big TLB Reach with Small Pages. In ASPLOS 2023.
[4] Graph 500. Graph 500 Large-Scale Benchmarks. http://www.graph500.org/. [5] Udit Gupta, Xiaodong Wang, Maxim Naumov,Carole-JeanWu, Brandon Reagen,
David Brooks, Bradford Cottel, Kim Hazelwood, Bill Jia, Hsien-Hsin S. Lee, Andrey Malevich, Dheevatsa Mudigere, Mikhail Smelyanskiy, Liang Xiong, and
Xuan Zhang. The Architectural Implications of Facebook's DNN-based Personalized Recommendation. In arXiv 2019.
[6] Hpsresearchgroup.
"hpsresearchgroup/scarab:
Joint
hps
and
eth
repository
to
work
towards
open
sourcing
scarab
and
ramulator.".
https://github.com/hpsresearchgroup/scarab.
[7] Bongjoon Hyun, Youngeun Kwon, Yujeong Choi, John Kim, and Minsoo Rhu.
NeuMMU: Architectural Support for Efficient Address Translations in Neural
Processing Units. In ASPLOS '20.
[8] Intel
Corp.
3rd
Generation
Intel®
Xeon®
Scalable
processore.
https://www.intel.com/content/www/us/en/products/docs/processors/embedded/3rd-gen-xeon-sc
[9] Youngjin Kwon, Hangchen Yu, Simon Peter, Christopher J. Rossbach, and Emmett Witchel. Coordinated and Efficient Huge Page Management with Ingens.
In 12th USENIX Symposium on Operating Systems Design and Implementation
(OSDI 16).
[10] Georgios Vavouliotis, Gino Chacon, Lluc Alvarez, Paul V. Gratz, Daniel A.
Jiménez, and Marc Casas. Page Size Aware Cache Prefetching. In MICRO 2022.
[11] Juan Navarro, Sitaram Iyer, Peter Druschel, and Alan Cox. Practical, Transparent Operating System Support for Superpages. In OSDI.
[12] D. Ernst T. Austin, E. Larson. SimpleScalar: an infrastructure for computer system modeling. In Computer, ( Volume: 35, Issue: 2, February 2002). IEEE, 59–67.
[13] Emmett Witchel, Josh Cates, and Krste Asanović. Mondrian Memory Protection.
In ASPLOS.
[14] Piotr R Luszczek, David H Bailey, Jack J Dongarra, Jeremy Kepner, Robert F
Lucas, Rolf Rabenseifner, and Daisuke Takahashi. The HPC Challenge (HPCC)
Benchmark Suite. In SC.
[15] M.T. Yourst. PTLsim: A Cycle Accurate Full System x86-64 Microarchitectural
Simulator (IEEE International Symposium on Performance Analysis of Systems
and Software).
[16] Ravi Bhargava, Benjamin Serebrin, Francesco Spadini, and Srilatha Manne. Accelerating Two-Dimensional Page Walks for Virtualized Systems. In ASPLOS.
[17] Thomas W. Barr, Alan L. Cox, and Scott Rixner. SpecTLB: A Mechanism for
Speculative Address Translation. In ISCA.
[18] Nathan Binkert, Bradford Beckmann, Gabriel Black, Steven K. Reinhardt, Ali
Saidi, ArkapravaBasu, Joel Hestness, DerekR. Hower, Tushar Krishna, Somayeh Sardashti, Rathijit Sen, Korey Sewell, Muhammad Shoaib, Nilay Vaish, Mark D.
Hill, and David A. Wood. The gem5 Simulator. Comput. Archit. News (2011).
[19] Trevor E. Carlson, Wim Heirman, and Lieven Eeckhout. Sniper: Exploring the
Level of Abstraction for Scalable and Accurate Parallel Multi-Core Simulations.
In SC.
[20] Jonathan
Corbet.
Transparent
Huge
Pages
in
2.6.38.
https://lwn.net/inproceedingss/423584/.
[21] Arkaprava Basu, Mark D. Hill, and Michael M. Swift. Reducing Memory Reference Energy with Opportunistic Virtual Caching. In ISCA.
[22] Binh Pham, Viswanathan Vaidyanathan, Aamer Jaleel, and Abhishek Bhattacharjee. CoLT: Coalesced Large-Reach TLBs. In MICRO.
[23] Rafael Ubal, Byunghyun Jang, Perhaad Mistry, Dana Schaa, and David Kaeli.
Multi2Sim: A Simulation Framework for CPU-GPU Computing. In PACT.
[24] Daniel Sanchez and Christos Kozyrakis. ZSim: Fast and Accurate Microarchitectural Simulation of Thousand-Core Systems. In ISCA.
[25] Jayneel Gandhi, Arkaprava Basu, Mark D. Hill, and Michael M. Swift. Efficient
Memory Virtualization: Reducing Dimensionality of Nested Page Walks. In MI-
CRO.
[26] Yu Du, Miao Zhou, Bruce R Childers, Daniel Mossé, and Rami Melhem. Supporting Superpages in Non-Contiguous Physical Memory. In HPCA.
[27] Vasileios Karakostas, Jayneel Gandhi, Furkan Ayar, Adrián Cristal, Mark D. Hill,
Kathryn S. McKinley, Mario Nemirovsky, Michael M. Swift, and Osman Ünsal.
Redundant Memory Mappings for Fast Access to Large Memories. In ISCA.
[28] V. Karakostas, J. Gandhi, F. Ayar, A. Cristal, M. D. Hill, K. S. McKinley, M. Nemirovsky, M. M. Swift, and O. Ünsal. Redundant Memory Mappings for Fast
Access to Large Memories. In ISCA.
[29] Yoongu Kim, Weikun Yang, and Onur Mutlu. Ramulator: A Fast and Extensible
DRAM Simulator. In CAL.
[30] Jayneel Gandhi, Mark D. Hill, and Michael M. Swift. Agile Paging: Exceeding
the Best of Nested and Shadow Paging. In ISCA.
[31] Idan Yaniv and Dan Tsafrir. Hash, Don't Cache (the Page Table). In SIGMETRICS.
[32] Yang Li, Saugata Ghose, Jongmoo Choi, Jin Sun, Hui Wang, and Onur Mutlu.
Utility-Based Hybrid Memory Management. In CLUSTER.
[33] Yashwant Marathe, Nagendra Gulur, Jee Ho Ryoo, Shuang Song, and Lizy K.
John. CSALT: Context Switch Aware Large TLB. In MICRO.
[34] Javier Picorel, Djordje Jevdjic, and Babak Falsafi. Near-Memory Address Translation. In PACT.
[35] Jee Ho Ryoo, Nagendra Gulur, Shuang Song, and Lizy K. John. RethInking TLB
Designs in Virtualized Environments: A Very Large Part-of-Memory TLB. In
ISCA.
[36] Nandita Vijaykumar, Abhilasha Jain, Diptesh Majumdar, Kevin Hsieh, Gennady
Pekhimenko, Eiman Ebrahimi, NastaranHajinazar, Phillip B. Gibbons, and Onur Mutlu. A Case for Richer Cross-Layer Abstractions: Bridging the Semantic Gap
with Expressive Memory. In ISCA.
[37] Sihang Liu, Korakit Seemakhupt, Gennady Pekhimenko, Aasheesh Kolli, and
Samira Khan. Janus: Optimizing Memory and Storage Support for Non-Volatile
Memory Systems. In ISCA.
[38] Ashish Panwar, Sorav Bansal, and K Gopinath. Hawkeye: Efficient Fine-grained
OS Support for Huge Pages. In ASPLOS.
[39] Zi Yan, Daniel Lustig, David Nellans, and Abhishek Bhattacharjee. Translation
Ranger: Operating System Support for Contiguity-Aware TLBs. In ISCA.
[40] Chloe Alverti, Stratos Psomadakis, Vasileios Karakostas, Jayneel Gandhi, Konstantinos Nikas, Georgios Goumas, and Nectarios Koziris. Enhancing and Exploiting Contiguity for Fast Memory Virtualization. In ISCA.
[41] Nastaran Hajinazar, Pratyush Patel, Minesh Patel, Konstantinos Kanellopoulos,
Saugata Ghose, Rachata Ausavarungnirun, Geraldo F. Oliveira, Jonathan Appavoo, Vivek Seshadri, and Onur Mutlu. The Virtual Block Interface: A Flexible
Alternative to the Conventional Virtual Memory Framework. In ISCA.
[42] R. Hwang, T. Kim, Y. Kwon, and M. Rhu.
Centaur: A Chiplet-based, Hybrid Sparse-Dense Accelerator for Personalized Recommendations. In 2020
ACM/IEEE 47th Annual International Symposium on Computer Architecture
(ISCA).
[43] Gyusun Lee, Wenjing Jin, Wonsuk Song, Jeonghun Gong, Jonghyun Bae, Tae Jun
Ham, Jae W. Lee, and Jinkyu Jeong. A Case for Hardware-BasedDemand Paging.
In 2020 ACM/IEEE 47th Annual International Symposium on Computer Architecture (ISCA). 1103–1116. https://doi.org/10.1109/ISCA45697.2020.00093
[44] Dimitrios Skarlatos, Apostolos Kokolis, Tianyin Xu, and Josep Torrellas. Elastic
Cuckoo Page Tables: Rethinking Virtual Memory Translation for Parallelism. In
ASPLOS.
[45] Siddharth Gupta, Atri Bhattacharyya, Yunho Oh, Abhishek Bhattacharjee,
Babak Falsafi, and Mathias Payer. Rebooting Virtual Memory with Midgard.
In ISCA.
[46] Artemiy Margaritov, Dmitrii Ustiugov, Amna Shahab, and Boris Grot. PTEMagnet: FIne-graIned Physical Memory Reservation for Faster Page Walks in Public
Clouds. In ASPLOS.
[47] Arun Subramaniyan, Yufeng Gu, Timothy Dunn, Somnath Paul, Md. Vasimuddin, Sanchit Misra, David Blaauw, Satish Narayanasamy, and Reetuparna Das.
GenomicsBench: A Benchmark Suite for Genomics. In ISPASS.
[48] Georgios Vavouliotis, Lluc Alvarez, Vasileios Karakostas, Konstantinos Nikas,
Nectarios Koziris, Daniel A. Jiménez, and Marc Casas. Exploiting Page Table
Locality for Agile TLB Prefetching. In ISCA.
[49] Nathan Gober, Gino Chacon, Lei Wang, Paul V. Gratz, Daniel A. Jimenez, Elvira
Teran, Seth Pugsley, and Jinchun Kim. The Championship Simulator: Architectural Simulation for Education and Competition. In arXiv.
[50] Chang Hyun Park, Ilias Vougioukas, Andreas Sandberg, and David Black-
Schaffer. Every Walk's a Hit: Making Page Walks Single-Access Cache Hits.
In ASPLOS.
[51] Jovan Stojkovic, Dimitrios Skarlatos, Apostolos Kokolis, Tianyin Xu, and Josep
Torrellas. Parallel Virtualized Memory Translation with Nested Elastic Cuckoo
Page Tables. In ASPLOS.
[52] ChandrahasTirumalasetty,Chih Chieh Chou, NarasimhaReddy, Paul Gratz,and
Ayman Abouelwafa. Reducing Minor Page Fault Overheads through Enhanced
Page Walker. ACM Trans. Archit. Code Optim.
[53] Konstantinos Kanellopoulos, Rahul Bera, Kosta Stojiljkovic, Nisa Bostanci, Can
Firtina, Rachata Ausavarungnirun, Rakesh Kumar, Nastaran Hajinazar, Jisung Park, Mohammad Sadrosadati, Nandita Vijaykumar, and Onur Mutlu. Utopia: Efficient Address Translation using Hybrid Virtual-to-Physical Address Mapping. arXiv:2211.12205 [cs.AR]
[54] Konstantinos Kanellopoulos, Hong Chul Nam, F. Nisa Bostanci, Rahul Bera, Mohammad Sadrosadati, Rakesh Kumar, Davide Basilio Bartolini, and Onur Mutlu.
Victima: Drastically Increasing Address Translation Reach by Leveraging Underutilized Cache Resources. In MICRO.
[55] Jovan Stojkovic, Namrata Mantri, Dimitrios Skarlatos, Tianyin Xu, and Josep
Torrellas.
Memory-Efficient Hashed Page Tables. In 2023 IEEE International
Symposium on High-Performance Computer Architecture (HPCA). 1221–1235.
https://doi.org/10.1109/HPCA56546.2023.10071061
[56] Kaiyang Zhao, Kaiwen Xue, Ziqi Wang, Dan Schatzberg, Leon Yang, Antonis
Manousis, Johannes Weiner, Rik Van Riel, Bikash Sharma, Chunqiang Tang, and Dimitrios Skarlatos. Contiguitas: the Pursuit of Physical Memory Contiguity in
Datacenters. In ISCA.