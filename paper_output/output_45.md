# Formal Definitions And Performance Comparison Of Consistency Models For Parallel File Systems

Chen Wang, *Member, IEEE,* Kathryn Mohror, *Member, IEEE,* and Marc Snir, Fellow, IEEE
Abstract—The semantics of HPC storage systems are defined by the consistency models to which they abide. Storage consistency models have been less studied than their counterparts in memory systems, with the exception of the POSIX standard and its strict consistency model. The use of POSIX consistency imposes a performance penalty that becomes more significant as the scale of parallel file systems increases and the access time to storage devices, such as node-local solid storage devices, decreases. While some efforts have been made to adopt relaxed storage consistency models, these models are often defined informally and ambiguously as by-products of a particular implementation. In this work, we establish a connection between memory consistency models and storage consistency models and revisit the key design choices of storage consistency models from a high-level perspective. Further, we propose a formal and unified framework for defining storage consistency models and a layered implementation that can be used to easily evaluate their relative performance for different I/O workloads. Finally, we conduct a comprehensive performance comparison of two relaxed consistency models on a range of commonly-seen parallel I/O workloads, such as checkpoint/restart of scientific applications and random reads of deep learning applications. We demonstrate that for certain I/O scenarios, a weaker consistency model can significantly improve the I/O performance. For instance, in small random reads that typically found in deep learning applications, session consistency achieved an 5x improvement in I/O bandwidth compared to commit consistency, even at small scales.

Index Terms—Consistency model, storage consistency, parallel file system, parallel I/O
✦

## 1 Introduction H

IGH performance computing (HPC) systems host parallel applications composed of hundreds to tens of thousands of tightly-coupled processes that typically run for hours or days. These large-scale applications that run on supercomputers often read and write large amounts of data, spending a significant fraction of their execution time performing I/O [1], [2]. However, the I/O subsystem, a core component in HPC systems, has not evolved as fast as other components such as compute and interconnect. I/O is emerging as a major bottleneck for many HPC applications. For example, it is shown that I/O can take as much as 85%
of the training time of a large-scale deep learning application [3], the majority of which is due to the random read requests to a large number of training samples. MuMMI [4], as another example, is a multi-scale simulation that models the dynamics of RAS proteins. When recording snapshots at a 0.5 ns interval, MuMMI generates over 400 million files, occupying over 1 PB of disk space for a single run, which poses a significant challenge for I/O latency and bandwidth. In order to reduce the I/O demand, compromises such as reducing snapshot frequencies have to be made. As we move beyond the exascale era, the I/O bottleneck will only be exacerbated.

A major constraint on the performance of parallel file systems (PFSs) is their strict adherence to the POSIX con-

•
Chen Wang and Kathryn Mohror are with Lawrence Livermore National
Laboratory. E-mail: {wang116, mohror1}@llnl.gov.
•
Marc Snir is with the Department of Computer Science, University of Illinois Urbana-Champaign. E-mail: snir@illinois.edu.
sistency model. A consistency model specifies a contract between a programmer and a system, wherein the system guarantees that if the programmer follows the rules, the shared data will be consistent and the results of reading, writing, or updating will be predictable. The POSIX standard [5] specifies a strong and straightforward consistency model, which requires all writes be immediately visible to all subsequent reads. While the POSIX consistency model is easy to maintain in a single-node environment, it is expensive to maintain at scale. Nevertheless, most widely deployed PFSs, including Lustre [6], GPFS [7], and BeeGFS [8], support POSIX consistency. The cost of supporting POSIX consistency is becoming increasingly unacceptable due to two key reasons: (1) the rapid growth in the scale of HPC systems, which directly increases the software overhead of maintaining POSIX consistency; (2) the emergence of new storage devices such as solid storage devices (SSDs), which greatly improves I/O latency and bandwidth and makes software overhead more significant. In recent years, many efforts have been made to develop burst buffer (BB) PFSs [9], [10], [11], [12], [13] (especially user-level systems) with relaxed consistency models, but these models were typically defined ambiguously and informally as by-products of their PFS implementations. This leads to three major issues: (1) Performance: It is challenging for system developers to evaluate and compare the effectiveness of different consistency models; (2) Correctness: It is difficult for programmers to reason about their program or check the correctness of their code; (3) Portability: A program that runs correctly under a given relaxed consistency model is not guaranteed to run correctly on a different model.

When compared to consistency models of shared memory systems (often referred to as *memory models*), storage consistency models (or *storage models* for short) have received far less attention and have not been systematically studied from a higher-level perspective. Similar terminologies and concepts are repeatedly reinvented, and lessons learned from memory models are often overlooked.

To summarize and motivate this work, here we list fundamental questions that have not been clearly answered. The first two focus on comparisons between storage and memory models. The last three focus on storage models and their performance implications.

1) What are the reasons for the lack of attention to storage
models compared to memory models?
2) What are the design choices for storage models, and
how do they relate to similar choices for memory models?
3) How do existing storage models compare and what
commonalities exist among them? Can they be defined in a unified and formal manner?
4) What are the performance implications of a storage
model?
5) What are effective methods to evaluate and compare the performance of different storage models?

This work seeks to answer these fundamental questions and develop a better understanding of storage consistency models by conducting a systematic study. Our work makes the following contributions:

- We investigate the contributing factors of the limited
attention paid to storage models. We show that recent advances in storage techniques are rapidly changing some of these factors (Section 3).
- We revisit the design choices of storage models and relate them to memory models. We highlight the different considerations between memory systems and storage systems for each design choice (Section 3).
- We propose a formal and unified framework for specifying the most widely-used family of storage models (Section 4).
- We study the performance implications of storage models. More importantly, we present a "layered" implementation that allows for effective performance comparisons between different storage models (Section 5).
- Finally, we conduct a detailed performance comparison between two storage models using a range of common HPC I/O workloads. The results highlight the significant impact storage models can have on I/O performance (Section 6).
In this work, we focus our study on storage models in
the context of parallel file systems for HPC I/O, but the concepts we develop should be generally applicable to other large-scale storage systems.

## 2 Background

This section describes example consistency models from both memory and storage domains, with the aim of introducing their similarities and differences. To prevent confusion, we use terms *store* and *load* when describing memory models and *write* and *read* when describing storage models.

## 2.1 Consistency Model: Strong Or Relaxed

Sequential consistency [14] is one of the most intuitive consistency models. It says that the result of any execution is the same as if the operations of all the processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its program. Sequential consistency is considered a strong consistency model because it guarantees operations of a processor are seen to occur in the same order by all processors. The major drawback is that it hinders optimizations that may result in reordering, e.g., store buffers and out-of-order cores.

Relaxed consistency models (weaker than sequential consistency) allow more optimizations but can be counterintuitive. Consider the well-known example shown in Table 1, where each process loads the value of the variable (x and y) stored by the other process. Intuitively, there are three possible outcomes: (r1, r2) = (0, 100), (100, 0) or (100, 100).

Sequential consistency guarantees that any execution of this program will produce one of these three results. In reality, most real hardware also allows (r1, r2) = (0, 0). For example, x86 systems from Intel uses a relaxed consistency model (often referred to as total store order [15]) that allows reordering non-conflicting store-load pairs, which violates sequential consistency. With this relaxation, store buffers can be used to buffer the expensive stores, so that loads (L12 and L22) can bypass the previous stores (L11 and L21).

| Process 1:   | Process 2:   |
|--------------|--------------|
| L            |              |
| 11           |              |
| :            | x            |
| 21           |              |
| :            | y            |
| L            |              |
| 12           |              |
| :            | r            |
| 1            |              |
| =            | y            |
| 22           |              |
| :            | r            |
| 2            |              |
| =            | x            |

The core idea behind the relaxed models is that some constraints imposed by stronger models are not necessary for the targeted program, while relaxing such constraints provides significant performance gains. The drawback, however, is that relaxing consistency semantics will likely reduce portability or programmability.

## 2.2 Relaxed Memory Models

2.2.1
Weak Ordering Weak ordering was defined by Dubois et al., [16] as follows: In a multiprocessor system, memory accesses are weakly ordered if (1) accesses to global synchronizing variables are strongly ordered, (2) no access to a synchronizing variable is issued by a processor before all previous global data accesses have been globally performed, and (3) no access to global data is issued by a processor before previous accesses to a synchronizing variable has been globally performed.

In essence, a system that follows weak ordering needs to be able to recognize synchronization operations. Concurrent accesses to shared memory can violate sequential consistency. But if all conflicting memory accesses are properly synchronized, then a weakly ordered system will deliver the same result as a system with sequential consistency. Many high-level languages require that programs be race-free, i.e., that conflicting accesses be synchronized. Consider the example in Table 2, when all operations are identified as data operations, y will not be guaranteed to return 100 because processors are free to reorder operations. However, if L12
and L21 are identified by programmers as synchronizations, then L22 is guaranteed to return the latest value of x due to the ordering imposed by the synchronizations.

Process 1:
Process 2:

$L_{11}:x=100$; $L_{21}:while(!flag)\{\}$; $L_{12}:flag=1$$L_{22}:y=x$;
2.2.2
Release Consistency Many synchronization operations occur in pairs. Release consistency [17] utilizes this information by explicitly distinguishing them as *release* and *acquire* operations, with the help from programmers. The release operation instructs the processor to make all previous memory accesses globally visible before the release completes, and the acquire operation instructs the processor not to start subsequent memory accesses before the acquire completes. In the example of Table 2, L12 is a release operation and L21 is an acquire operation. Release consistency is a further relaxation of weak ordering. It allows systems to have different implementations for release and acquire, which leads to better performance at the cost of the increased burden on programmers.

2.2.3
Entry Consistency A major issue of weak ordering and release consistency is that their synchronization operations impose order on memory operations even if they do not conflict, which may add unnecessary overhead. Consider the example in Table 3, to make sure y in L22 returns the store to x in L12, under weak ordering or release consistency, L13 and L21 need to be identified as synchronizations. However, this also prohibits reordering L11 and L13, i.e., L11 must complete before L13, which is unnecessary if no other process will ever access w. Entry consistency addresses this issue by requiring each ordinary shared data item to be associated with a *synchronization variable*. When an acquire is done on a synchronization variable, only those data guarded by that synchronization variable are made consistent. For instance, in the case of example in Table 3, we can associate w and x with two different synchronization variables, thus allowing L11 to bypass L12 and L13.

| Process 1:   | Process 2:   |
|--------------|--------------|
| L            |              |
| 11           |              |
| :            | w            |
| 21           |              |
| :            | while        |
| {}           |              |
| ;            |              |
| L            |              |
| 12           |              |
| :            | x            |
| 22           |              |
| :            | y            |

L13 : *flag* = 1

## 2.3 Relaxed Storage Models

The requirements of POSIX consistency essentially impose sequential consistency. The fundamental problem behind the performance issues stemming from POSIX consistency is that PFSs are ignorant of the application's synchronization logic and the order of I/O operations of different processes.

PFSs must make worse-case assumptions and serialize all potentially conflicting I/O operations to guarantee POSIX consistency. Alternatively, programmers can provide information on program synchronizations of conflicting I/O operations to the PFS. With this extra information, PFSs can adopt a weaker consistency model, while guaranteeing the same outcome of POSIX consistency. Wang et al., [18] have studied many such PFSs and their consistency models. Here, we briefly discuss the most commonly used models.

## 2.3.1 Commit Consistency

Commit consistency is a relaxed consistency model commonly used by recent BB PFSs such as BSCFS [19], UnifyFS [10], and SymphonyFS [13]. In commit consistency, "commit" operations are explicitly executed by processes. The commit operation conveys synchronization information. I/O updates performed by a process to a file before a commit become globally visible upon return of the commit operation. To maintain portability, PFSs adopting commit consistency may use an existing POSIX call to indicate a commit. For example, in UnifyFS [10], a commit operation is triggered by a fsync call, which applies to all updates performed by a process on a file since the previous commit. Note that finer commit granularity (e.g., committing byte ranges) is also possible, but may add additional overhead if used in a superfluous way.

## 2.3.2 Session Consistency

Commit consistency guarantees all local writes that precede the commit operation become globally visible after the commit operation. However, in many cases, data written is rarely read back by the same application, and even when this happens, usually only a subset of processes perform the reads. Thus, global visibility is not necessary. Session consistency (also known as close-to-open consistency) addresses this issue by defining a pair of synchronization operations, namely, session_close and session_open. Session consistency guarantees that writes by a process become visible to another process (not all processes) when the modified file is closed by the writing process and subsequently opened by the reading process, with the session_close happening before the session_open. The idea of session consistency is very similar to that of release consistency for memory models.

Note that we name the two operations session_open and session_close, but most existing systems adopting session consistency such as NFS [20] do not provide the separate session_open and session_close APIs. Rather, they are implied by POSIX open/close (or fopen/fclose) calls, calls that have additional effects— they apply all updates to a file.

## 2.3.3 Mpi-Io Consistency

MPI-IO [21] is a part of the MPI standard that defines both communications (message passing) and I/O operations. As the latest standard [22] states, MPI-IO provides three levels of consistency: sequential consistency among all accesses using a single file handle, sequential consistency among all accesses using file handles created from a single collective open with atomic mode enabled, and user-imposed consistency among accesses other than the above.

The first two cases are the most common cases, and sequential consistency is guaranteed without extra synchronizations. In the last case, sequential consistency can be achieved by using a *sync-barrier-sync* construct that imposes orders on the conflicting I/O accesses. Here, sync is one of MPI_File_open, MPI_File_close or MPI_File_sync that takes in the file handle and flushes the data (writer) or retrieves the latest data (reader). And barrier provides a mechanism that imposes order between the two *syncs*. In most cases, this is achieved using MPI calls. For example, *barrier* can be one of the collective communication calls such as MPI_Barrier and MPI_Allgather, or a pair of point-to-point calls such as MPI_Send plus MPI_Recv. However, *barrier* is not limited to MPI calls, it can use any mechanism that properly orders the two sync calls.

Even though MPI-IO has information on both I/O and MPI communication, it can not assume the synchronization information (i.e., *barrier*) is always available to the system as it may not use MPI calls. MPI-IO consistency is similar to session consistency, but additional optimizations are possible if ordering is imposed through MPI calls, as those are visible to the MPI library (which includes MPI-IO).

## 3 Memory Models Vs. Storage Models

In this section, we first investigate why relaxed storage consistency models have not gained enough attention and widespread adoption. Next, we analyze the key design choices for consistency models and compare the different considerations between memory systems and storage systems. Finally, we discuss the primary commonality of existing relaxed storage models, introduce the key concepts that will serve as the foundation for our formal definition of these models.

## 3.1 Why Relaxed Storage Models Are Not Widely Adopted

3.1.1
Programming Hierarchy The presence of compilers in the memory programming hierarchy (Figure 1(a)) has been an important factor in the adoption of relaxed memory models. Compilers can hide complexity and provide portability, which allows programmers to target a single memory model specified by the highlevel programming language (e.g., C++ and Java) without the knowledge of underlying consistency models provided by the CPUs. This way, a suitable consistency model can be selected for the given hardware, without worrying about programmability. For example, C++ allows specifying a different consistency model for each atomic operation; but the semantics of these models is specified by the C++ standard is unrelated to the underlying hardware.

In contrast, there is no corresponding "compiler" layer in the storage programming hierarchy and no low-level hardware-supported consistency model to map onto: Consistency protocols are implemented in software. To achieve programmability and portability, most storage systems choose to implement the same standard, POSIX. Most local file systems (e.g., ext3, ext4, and xtfs) and parallel file systems (e.g., Lustre [6] and GPFS [7]) are POSIX-compliant.

Application
I/O library
Application
DRF/HLL (e.g, C++)
POSIX I/O (e.g., C++)
Compiler
POSIX/ext4 POSIX/xfs POSIX/Others
PMEM
TSO/Intel x86 Power/IBM
Others
SSD
HDD
Memory
Storage

3.1.2
Software Overhead The POSIX consistency semantics prohibit many optimizations. This disadvantage is not so apparent in a singlenode system, in which I/O operations are serialized. But maintaining POSIX consistency in an HPC environment can be more costly, as PFSs require distributed locking mechanisms running reliably at large scale to enforce it. Nevertheless, in most scenarios, the software overhead incurred is minor compared to the slow I/O performance of HDDs. Consequently, less attention has been given to alternative consistency models. However, this is starting to change due to two reasons: the rapid increase in the scale of HPC systems, and the emergence of new, faster storage technologies, such as SSDs. The former directly increases the software overhead required to enforce the same consistency requirements. The latter makes the overhead more significant since I/O operations complete much faster.

## 3.2 Design Considerations

Here we describe several important design considerations of a consistency model and compares memory models (from the perspective of high-level programming languages) with storage models (from the perspective of parallel file systems) for each consideration.

3.2.1
Synchronization Synchronization is critical to a consistency model. It is used to enforce order between potential conflicting accesses. Synchronizations can be performed by explicitly invoking synchronization operations, which is common in both memory models and storage models. Alternatively, synchronizations can be specified in a declarative manner. For example, highlevel languages often provide keywords (e.g., atomic in C++ and volatile in Java) that can modify ordinary objects to impose extra ordering restrictions on relevant accesses. Such features, however, are less common in storage models.

## 3.2.2 Scope Of Synchronization Control

Both high-level programming languages and parallel file systems provide some limited control on synchronization requirements of executing code. In a high-level language such as C++ this is done at the level of variable declarations (for atomic variables) or atomic access operations (specifying the applicable memory order). The latter is seldom used. For POSIX file systems, this is done when a file is opened, e.g., with O_SYNC, O_RSYNC or O_DSYNC flags. Other scopes for such controls are feasible, in both cases. For a programming language, the scope is likely to be a static text scope; for a file system, it is likely to be a file, file range, or an I/O call.

## 3.2.3 Atomicity

Atomicity is often a required property for both memory systems and storage systems. It is key to ensure correctness for applications with conflicting accesses.

## 3.2.4 Granularity

Atomicity is supported in high-level languages with arbitrary granularity. One can specify a primitive object (e.g., int) or a large data structure to be atomic. This granularity needs not to match the granularity of memory operations in hardware; the compiler will implement them using native atomic operations or locks, depending on the granularity. Support for atomic access to larger memory objects will entail additional software overheads. Similarly, consistency is supported by memory hardware and made visible in highlevel languages at the granularity of the smallest accessible datum, namely a byte. But coherence protocols act at the granularity of a cache line (typically, 64 bytes). Finer-grain coherence units would require more hardware; coarsergrain coherence units increase the amount of coherence memory traffic and the frequency of false sharing.

File systems also support storage accesses having arbitrary lengths. POSIX does not guarantee atomicity of reads and writes; the outcome of such operations is well-defined only if conflicting operations are ordered by some means.

On the other hand, consistency is maintained at the byte level by POSIX. PFSs' units of coherence are necessarily much coarser, so that fine-grain interleaved accesses by distinct processes can generate a significant amount of coherence traffic and suffer from false sharing.

## 3.2.5 Program Text

In memory systems, compilers see the program text and thus have some information on possible executions of the program. Parallel file systems, on the other hand, have no access to the program text. A PFS is an online system that sees one storage operation at a time.

## 3.2.6 Reordering

The compiler can perform static passes to reorder memory instructions, whereas PFSs are online systems that do not have the ability to make static reorderings. PFSs can perform some limited reorderings by buffering/delaying certain storage operations.

## 3.2.7 External Information

When programming on a PFS, as discussed in Section 2.3.3, programmers sometimes use non-storage operations, e.g., through RPC and message passing, to express their synchronization logic. However, PFSs are generally unaware of synchronization operations. In contrast, memory models are simpler as they assume that all synchronization is done using memory operations.

## 3.3 Approach To Formally Define Consistency Models

The primary commonality of existing relaxed storage models is that they can guarantee sequential consistency for programs that follow certain rules. Those programs share enough information (e.g., the commit calls in commit consistency) with the system so the system can guarantee sequentially consistent execution results even with relaxed storage models. Such models are said to be in Sequential Consistency Normal Form (SCNF) [23]. SCNF was a term initially defined for memory model formalization, but it applies to storage models as well.

Sequential Consistency Normal Form: A
consistency
model
is
in
sequential
consistency
normal
form
iff it guarantees sequential consistency to a set of formally-characterized programs.
The idea of providing sequential consistency semantics to a set of formally-characterized programs was formalized by the data-race-free (DRF) memory models [23], [24]. The DRF models exploits the observation that good programming practice dictates that programs be data-race-free; a data race often suggests that there are bugs in the code. The DRF models guarantee sequential consistency for the "correct" programs (i.e., without data races) and leave the behavior of the "incorrect" programs undefined.

Unfortunately, unlike the DRF memory model, existing SCNF storage models are typically defined ambiguously and informally as by-products of their PFS implementations. In the next section, we will present a unified and formal framework to specify storage models that are in SCNF.

## 4 A Unified And Formal Framework

The SCNF storage models we consider rely on synchronization information to achieve sequential consistency. We call programs that contain adequate synchronization to enforce necessary ordering *properly-synchronized programs*, and the storage models that guarantee sequential consistency to those programs *properly-synchronized SCNF models*. All models we discussed in Section 2.3 are properly-synchronized SCNF models.

The formalization of our framework is similar to that of the Java memory model [25] (which adopts the DRF approach but with a much more complex model). Our framework does not make any assumptions about particular synchronization methods; it allows the specific storage model to define its own set of synchronization operations. The key is to define which programs are considered properlysynchronized.

## 4.1 Specifying Properly-Synchronized Scnf Models

We first define two types of storage operations: A storage operation is either a *data storage operation* or a synchronization storage operation, defined as follows.

Data Storage Operations: These are I/O operations that read or write storage, such as fread or fwrite. Data operations include the specification of the storage location (possibly as a range) to be read or written. Each data operation specifies an object called synchronization object that is associated with the requested location, such as a file handle.

Synchronization Storage Operations: These are I/O operations that may be used to impose an order on data storage operations, such as fsync, fopen, or fclose.

Synchronization operations are model-specific, where each synchronization operation includes the specification of a synchronization object.

Further, we consider here the execution of a multiprocess program, in an environment that provides well-defined mechanisms to synchronize concurrent processes, such as MPI message-passing. These mechanisms define a program order and *synchronization order* on the executed operations of the program:
Program Order (
po
−→): The program order of a process is a total order on the execution of the process' operations as specified by the program text. To keep the discussion simple, we ignore the extensions needed to deal with multithreaded processes.

Synchronization Order ( so
−→): A synchronization order is a
partial order specified between operations executed by distinct processes. This partial order is consistent with the program order, and
po
−→ ∪ so
−→ is acyclic.
A properly-synchronized SCNF model is then defined as
follows.
Happens-Before Order ( hb
−→): The happens-before order of
an execution is the transitive closure of
po
−→ ∪
so
−→.
The outcome of a parallel execution should be as if all
instructions were executed in the order specified by hb
−→.
Thus, if ow and or are, respectively, a write and a read
to the same location, and ow hb
−→ or, then or will return
the value written by ow, unless there is another store
ow′ to the same location such that ow hb
−→ ow′
hb
−→ or.
The happens-before order is defined by the semantics of the programming system used. It orders I/O operations executed by the program. It is not necessarily visible to the storage system.
Conflict: Two data storage operations *conflict* iff their access
ranges overlap, and at least one of them is a write.
Minimum Synchronization Construct (MSC): An MSC specifies a minimum sequence of synchronization storage operations required to synchronize two conflicting data operations. An MSC consists of $k$ synchronization storage operations and $k+1$ edges, where $k\geq0$:

$$MSC=\overset{r_{0}}{\longrightarrow}S_{1}\ \overset{r_{1}}{\longrightarrow}S_{2}\ \overset{r_{2}}{\longrightarrow}\ldots\ \overset{r_{k-1}}{\longrightarrow}S_{k}\ \overset{r_{k}}{\longrightarrow}$$

For each $i$, $1\leq i\leq k$ and $S_{i}\in S$, where $S$ is the set of synchronization storage operations to be defined by the specific consistency model. For each $j$, $0\leq j\leq k$ and 
rj
−→∈ {
po
−→, hb
−→}. Note here the choice of rj can not be trimmed down to just hb
−→ as some consistency models may require a synchronization operation of the MSC to be called by one of the conflicting processes, where rj =
po
−→.

Properly-Synchronized Relation (
ps
−→): Two
conflicting
data
storage
operations
X
and
Y
are
properly
synchronized, i.e., X
ps
−→ Y , iff one of the following
holds:
1) X is a read operation and X
hb
−→ Y .
2) X is a write operation, and there exists an MSC
between X and Y in the happens-before order.
Storage Race: Two data storage operations X and Y in an
execution form a *storage race* iff they conflict and they
are not properly synchronized.
Properly-Synchronized Program: A program is properly
synchronized iff for every sequentially consistent execution of the program, all storage operations can be distinguished by the system as either data or synchronization, and there are no storage races in the execution.
Properly-Synchronized SCNF System: A system is said to be a properly-synchronized SCNF system iff the result of every run of a properly-synchronized program on the system is the result of a sequentially consistent execution of the program.

Intuitively speaking, the key to achieving sequential consistency is to make sure the program is storage race free (i.e., there are no conflicts or conflicts are properly synchronized). Storage race-freedom may require the use of storage synchronization operations, in addition to the synchronization constructs of the parallel programming system. The properly-synchronized SCNF model specifies a set S of storage synchronization operations and minimum synchronization constructs (MSC) to properly synchronize conflicting I/O operations.

## 4.2 Describing Existing Models

Our framework provides a formal, but simple, way to capture the specification of properly-synchronized SCNF
models, where only S and *MSC* need to be specified for a complete definition. Table 4 demonstrates how to describe the storage models discussed earlier (Section 2.3) using our framework.

4.2.1
POSIX Consistency POSIX consistency can be considered as a special properlysynchronized SCNF model. With POSIX consistency, every write is immediately visible to all subsequent reads without synchronization operations. Here and in the rest of this section, "subsequent" is defined according to the happensbefore order. Therefore, POSIX consistency has an empty set S and an MSC of hb
−→.

4.2.2
Commit Consistency For commit consistency, there is one synchronization operation, commit. A write to file f becomes visible to all subsequent reads from f upon the return of a subsequent the commit call. Most commit-based systems require that the commit is called by the process that performs the writes, by having an *MSC* of po
−→ commit hb
−→. A relaxed version may allow a process to commit for the updates of other processes, resulting an MSC of hb
−→ commit hb
−→.

4.2.3
Session Consistency Session consistency specifies two special synchronization operations, S = {session_close, session_open}. For a write to become visible to a subsequent read, a close-toopen pair has to be performed in between, thus, *MSC* =
po
−→
session_close hb
−→ session_open po
−→. The po
−→ at the beginning indicates that the session_close operation has to be performed by the writing process. Similarly, the po
−→ at the end indicates that the session_open operation must be performed by the reading process. Finally, the hb
−→ enforces that the session_close happens before the session_open.

4.2.4
MPI-IO Consistency As discussed in Section 2.3.3, MPI-IO provides three levels of consistency. For the first two cases, MPI-IO guarantees sequential consistency without requiring extra synchronizations (just like POSIX consistency). In Table 4, we show how to specify the MPI-IO consistency model for the third case. In this case, MPI_File_close synchronizes with all subsequent MPI_File_open and MPI_File_sync. MPI_File_sync synchronizes with all subsequent MPI_File_sync and MPI_File_open. Therefore, there are four possible *MSCs* that can be used to properly synchronize the conflicting accesses:

•
po
−→ MPI_File_close hb
−→ MPI_File_open
po
−→
•
po
−→ MPI_File_close hb
−→ MPI_File_sync
po
−→
•
po
−→ MPI_File_sync hb
−→ MPI_File_sync
po
−→
•
po
−→ MPI_File_sync hb
−→ MPI_File_open
po
−→
In each MSC, the hb
−→ imposes the order between the two synchronization operations, and the po
−→ enforces that the synchronization operations must be called by the conflicting processes.

## 5 An Implementation For Properly- Synchronized Scnf Systems

Now that we have formally defined properly-synchronized SCNF models, the next question is: when should we use a particular consistency model? Another question that immediately follows is: what is the performance difference? Alternatively and more simply, how much performance can we gain from using a weaker consistency model? The answers to these questions are important for both storage system developers and application programmers because they provide information to aid in understanding the tradeoff between extra programming effort and extra performance. This information helps system developers choose which consistency models to support and helps application programmers decide whether to port their codes to a storage system with weaker consistency.

To answer these questions, we need to conduct a comprehensive performance comparison between different properly-synchronized SCNF models, which requires evaluating PFSs that use those models. However, existing PFSs that adopt different consistency models also differ greatly in their implementations and optimizations. It is difficult to isolate the effect of a consistency model and ever harder to conduct a fair comparison between different consistency models.

To address this, we present a "layered" implementation that allows for an easy performance comparison of different consistency models by keeping, as much as possible, everything other than the consistency model same. An overview of our approach is depicted in Figure 2. We design and implement a "base-layer" PFS, called BaseFS, which runs on top of a system-level PFS such as GPFS or Lustre. BaseFS supports the basic functionalities of a PFS with essentially zero optimization. BaseFS buffers reads and writes using burst buffer devices, and flushes data to the underlying PFS only when explicitly instructed. BaseFS provides a very minimum consistency guarantee, but it exposes a set of flexible primitives that can be used to implement custom consistency models. On top of BaseFS, we can implement PFSs providing different consistency models using these primitives. Since these PFSs use the set of primitives and thus the same underlying implementation, we can limit the impact of other components of the PFS to a very low level. Comparing the performance of these PFSs thus can give us a good understanding of the impact of different consistency models.

In this section we describe BaseFS and two example PFSs, CommitFS and SessionFS, each adopting a different consistency model as suggested by its name.

## 5.1 Basefs

BaseFS is not designed to be a full-fledged file system. Our focus is to evaluate the performance implications of different consistency models. As a result, we consider detailed implementation choices, e.g, how to resolve a path and map it to the inode server and how to retrieve file locations given an inode as control variables in our experiments, and we need to make sure that they do not compromise the comparison when evaluating different consistency models.

Consistency Models
S
MSC
POSIX Consistency
{}
hb
−→
Commit Consistency
{commit}
hb
−→ commit hb
−→
Session Consistency
{session_close, session_open}
MPI-IO Consistency
{MPI_File_sync,
MPI_File_close,
s1 *∈ {*MPI_File_close, MPI_File_sync}
MPI_File_open}
s2 *∈ {*MPI_File_sync, MPI_File_open}

5.1.1
Primitives Modern PFSs [6], [7], [8] normally use some kind of locking mechanism to provide sequential consistency. But the lock-based design does not take advantage of the extra information available to the weaker models, like commit consistency and session consistency. Thus, instead of using locking for our BaseFS implementation, we developed a set of flexible primitives (Table 5) which are more suitable for implementing properly-synchronized SCNF models.

The BaseFS file system does not provide any implicit guarantee of consistency. Consistency must be enforced by explicit synchronization calls. The system may store multiple, possibly inconsistent, copies of parts of a file on client nodes, in addition to a (partial) copy on a storage server. In BaseFS, the write (bfs_write) writes to the local copy of the file at the calling client. The read (bfs_read) is implemented as a *read from*: The *owner* argument specifies the client process that will source the data read. The owner argument can be retrieved using the bfs_query call. The read will return the values most recently written by the owner client.

The two key synchronization primitives are bfs_attach and bfs_query. The attach call specifies a file range and the issuing client becomes the exclusive owner of those addresses in this range. One can attach only locations that were written by the local process and not flushed. Essentially, the attach call makes the local writes visible to other processes. It does not guarantee the global visibility of future writes to the same range. Whenever an update needs to be made visible to other processes, an attach call is required. An attach is not needed if the written data will not be read by other processes.

The query call specifies a file range and returns the current owners of the range. The result is returned in a list of *intervals*. Each interval contains a disjoint subrange and the last attached owner process of that subrange. A query is required to retrieve the the latest attached writes from other processes. In most HPC I/O workloads, this is rare. Typically a process reads from its own writes or from a preexisting file. As a result, the fewer conflicting storage accesses occur, the fewer attach and query calls are needed and thus the lower is the overhead.

5.1.2
Implementation Again, the top priority of BaseFS is not to achieve the best performance, but to enable effective comparisons between different consistency models. Therefore, our implementation is fairly straightforward, without complicated optimizations such as distributed servers and namespace

po
−→ session_close hb
−→ session_open
po
−→
po
−→ s1
hb
−→ s2
po
−→

partitioning. These optimizations will be equally beneficial to the PFSs built on top of BaseFS (e.g., CommitFS and SessionFS), and would not add additional value to the comparison.

As shown in Figure 2, BaseFS is implemented as a user-level BB file system with a focus on data operations. Reads and writes are directly fulfilled by the BB devices without any memory caching. A limited number of metadata operations (e.g., stat) and attributes (e.g., EOF) are supported. In BaseFS, each client process buffers its writes (bfs_write) using node-local BB devices. We assume that the BB devices are large enough to accommodate the entire storage required for a job execution (no system-initiated flushes). At a read call (bfs_read), the client reads from the buffer of the specified owner (which can be itself). If the requested range is not owned by any client, the client reads from the underlying PFS to obtain the latest flushed data.

We use a single global server to handle messages from clients. These messages are generated only by the synchronization primitives, the write and read primitives do not involve the global server. The global server is multithreaded where the master thread handles all communications and the remaining threads run an identical worker routine. Each worker maintains a FIFO queue that holds client requests. When a new client request (e.g., a query request) is received, the master thread creates a new task and appends it to one worker's task queue. The worker is selected in a roundrobin manner. Once the task is completed by the specified worker, the server will send back the result to the requesting client. Next, we go through the tasks triggered by the synchronization primitives:

- **Attaching**:
When
a
client
process
invokes
a
bfs_attach* primitive, it notifies the server that
it will be responsible for reads from the specified file range. In other words, the client declares itself as the owner of the most recent update to the specified range.
The ownership is exclusive, the caller of bfs_attach*
will take over the ownership in the case when the same range has been previously attached by another process. The subsequent queries (bfs_query) to the same range will return an exclusive owner. Other clients can later use bfs_read to directly fetch the data from the owner's buffer without going through the underlying PFS.
- **Detaching**: A client detaches from a previously attached file range to relinquish ownership. After detaching, the owner does not own the range anymore and it will not be responsible for future bfs_read calls to the detached range. If the data needs to be preserved for

## Table 5: The Most Relevant Primitives Of Basefs

- bfs_file_t* bfs_open(const char* pathname)
Description: Opens the file whose pathname is the string pointed to by *pathname*, and associates a BaseFS file handle (bfs_file_t) with it. This file handle is an opaque object and can be used by subsequent I/O functions to refer to that file. The file is always opened in read-write mode.

Append mode is not supported. The file offset used to mark the current position within the file is set to the beginning of the file.

Return Value: Upon successful completion, the function returns a pointer to the BaseFS file handle; otherwise, a NULL pointer is returned.

- int bfs_close(bfs_file_t* file)
Description: Causes the file handle pointed to by *file* to be released and the associated file to be closed. Any buffered data is discarded (not flushed as in in POSIX). Whether or not the call succeeds, the file handle is disassociated from the file.

Return Value: Upon successful completion, the function returns 0; otherwise, it returns -1.

- ssize_t bfs_write(bfs_file_t* file, const void* buf, size_t size)
Description: Writes *size* bytes of data from the buffer pointed by *buf* to the specified *file*. The file-position indicator of the calling process is advanced by the number of bytes successfully written. The write becomes immediately visible to the writing process, but it is not guaranteed to be visible to other processes after the call.

Return Value: Upon successful completion, the function returns the number of bytes written; otherwise, it returns -1.

- ssize_t bfs_read(bfs_file_t* tf, void* buf, size_t size, bfs_addr_t* owner)
Description: Reads *size* bytes of data from the specified *file* to the buffer pointed to by *buf*. The file-position indicator of the calling process is advanced by the number of bytes successfully read. This function returns the most up-to-date buffered write of the specified *owner* process. The function will fail if the *owner* process does not own the specified range. If *owner* is NULL, the function will directly read from the underlying PFS.

Return Value: Upon successful completion, the function shall return the number of bytes successfully read; otherwise, it returns -1.

- int bfs_attach(bfs_file_t* file, size_t offset, size_t size)
Description: Attaches the range from offset to offset+size-1 in *file* to the calling process. This function makes the most recent buffered writes of the calling process to the specified range visible and available to all processes. Overlapping ranges that were attached by other processes shall be overwritten. The data covered by the specified range must have been written locally. It is allowed to attach partially a previous write, but attaching unwritten bytes is erroneous.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_attach_file(bfs_file_t* file)
Description: Attaches all locally buffered writes by the calling process to *file*. Overlapping ranges that were attached by other processes shall be overwritten. The function is a no-op if no buffered writes exist.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_query(bfs_file_t* file, size_t offset, size_t size, bfs_interval_t** intervals, int* num_intervals)
Description: Returns the attached subranges of *file* included in the range of [*offset, offset+size-1*]. The result is written to *intervals* and *num intervals*, where *intervals* contains a list of file ranges and the owner process of each range.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_query_file(bfs_file_t* file, bfs_interval_t** intervals, int* num_intervals)
Description: Returns all attached ranges of *file*. The result is written to *intervals* and *num intervals*, where *intervals* contains a list of file ranges and the attached process of each range.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_detach(bfs_file_t* file, size_t offset, size_t size)
Description: Detaches currently attached ranges in *file* that overlap with range of [*offset, offset+size-1*] of the *file*. The function removes the specified range from the local buffer, and makes the buffered writes covered by the range no longer visible to all processes. If the data is needed for later reads, then a bfs_flush call should be made before detaching. The function fails if the specified range was not attached before.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_detach_file(bfs_file_t* file)
Description: Detaches all ranges of *file* that are currently attached to the calling process. The function is a no-op if no attached ranges exist.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

- int bfs_flush(bfs_file_t* file, size_t offset, size_t size)
Description: Flushes the locally buffered data in the range from offset to offset+size-1 of *file* to the underlying PFS. Previously attached updates of the same range will remain available to all processes until the detach call.

Return Value: Upon successful completion, the function returns 0; otherwise, it returns -1.

- int bfs_flush_file(bfs_file_t* file)
Description: Flushes all the locally buffered data (if any) of *file*. The function is a no-op if no locally buffered data exists.

Return Value: Upon successful completion, the function returns 0; otherwise, it returns -1.

- ssize_t bfs_seek(bfs_file_t* tf, size_t offset, int whence);
Description: Sets the file-position indicator for *file*. The new position, measured in bytes from the beginning of the file, is obtained by adding offset to the position specified by *whence*. The specified point is the beginning of the file for SEEK SET, the current value of the file-position indicator for SEEK CUR, or end-of-file (EOF) for SEEK END. Reads from never written locations before the EOF are filled with zeros. Reads from locations beyond the EOF return undefined values. The function by itself is not changing the end-of-file location.

Return Value: Upon successful completion, the function returns the current file-position indicator; otherwise, it returns -1.

- ssize_t bfs_tell(bfs_file_t* file);
Description: This function obtains the current value of the file-position indicator for *file*.

Return Value: Upon successful completion, the function returns the current value of the file-position indicator for the file handle measured in bytes from the beginning of the file. Otherwise, it returns -1.

- int bfs_stat(bfs_file_t* file, struct stat* buf)
Description: This function obtains information about *file*, and writes it to the area pointed to by *buf*. Currently, BaseFS only maintains the file size attribute (i.e., st_size of struct stat), all other attributes are ignored.

Return Value: Upon successful completion, 0 is returned. Otherwise, -1 is returned.

future reads, then a bfs_flush call is required before detaching.

- **Querying**: A client issues a bfs_query call to ask the server who owns the most up-to-date data of the given range, i.e., who performed the last attach to the same range. The server will respond with a list of sub-ranges (since the queried range may cover multiple attach operations) along with their owners' information. An empty list will be returned if no one has attached locations in the range yet.

The global server maintains a per-file interval tree (noted as *global interval tree*) to keep track of the attached file ranges.

Internally, BaseFS uses an augmented self-balancing binary search tree to implement this interval tree. Each interval
(or each node of the tree) has the form of ⟨Os, Oe*, Owner*⟩, where Os and Oe are the start and end offset of a file range, and *Owner* stores the information of the most recent client who attached the range. Note that the interval tree keeps only the most recent attach and does not store any histories. A new interval is inserted upon each attach request. At the insertion time, the server checks the existing intervals to decide if they need to be split or deleted. An existing interval is split if it partially overlaps with the new interval and has a different owner; it is deleted if it is fully contained in the new interval. The server also merges intervals belonging to the same client with contiguous ranges. This reduces the number of intervals and accelerates future queries. When the server receives a detach request, it consults the interval tree and checks whether the same client still owns the entire range. It is possible that other clients has overwritten the same range and became new owners. In that case, the detach will simply be a no-op. Otherwise, the detach request succeeds (with possible splits), and the interval is removed from the tree.

Each client process also maintains a similar interval tree
(noted as *local interval tree*) for each file. It is used to keep track of locally written ranges and their mappings to the local burst buffer files. Specifically, each interval of the local interval tree has the form of ⟨Os, Oe, Bs, Be*, attached*⟩, where Os and Oe indicate the range of a write to the targeted PFS file, Bs and Be indicate where the range is buffered on the local burst buffer file, and *attached* indicates whether the write has been attached or not. At each write (bfs_write), a new interval will be inserted into the local interval tree. There will be no split because all writes are from the same client. Contiguous intervals are merged as in the global interval tree. The bfs_attach primitive is used to attach the writes to one contiguous file range, while the bfs_attach_file primitive attaches all local writes to the file. Both calls will pack and send all supplied information using a single RPC request. Moreover, both calls will check the local interval tree to make sure the same range is not attached twice, and the attached ranges were previously written by the local process.

As mentioned above, a client can respond to read requests from other clients after an attach call. This clientto-client data transfer can be performed efficiently using RDMA. For this to work, each client process needs to spawn a separate thread to listen to the incoming bfs_read requests. This increases CPU usage but can significantly improve read performance, assuming RDMA is faster than disk I/O (i.e., reading directly from the underlying PFS).

## 5.2 Commitfs And Sessionfs

With BaseFS, we can easily implement a PosixFS, CommitFS, and SessionFS on top. Table 6 shows the APIs exposed by each along with their internal implementations using the BaseFS primitives. The primary difference in their implementations is the placement of attach and query primitives. The stronger the model, the more frequently the attach and query primitives are needed. For example, to achieve POSIX consistency, an attach call has to be invoked by each write, and a query call has to be invoked by each read. In comparison, CommitFS only performs attach at the commit time, though query is still needed ahead of every read operation.

As for SessionFS, a query is performed at the session open time, and an attach is performed at the session close time. Within a session, multiple write and read calls can be executed without any query or attach.

## 6 The Impact Of Consistency Models On I/O Performance

This section studies the impact of consistency models on I/O performance. First, we evaluate the performance of commit consistency and session consistency using benchmarks that represent common HPC I/O patterns. Then we perform two case studies to further understand the performance disparity caused by different consistency models. The first case study is of the I/O behavior of the Scalable Checkpoint/Restart (SCR) library [26], while the second case study is of the I/O behavior of the training phase of distributed deep learning applications. We note that in all cases, we only consider I/O operations and do not perform any computation or communication.

We performed all experiments on the Catalyst system located at Lawrence Livermore National Laboratory. Catalyst is a Cray CS300 system, where each compute node consists of an Intel Xeon E5-2695 with two sockets and 24 cores in total, with 128GB memory. The nodes are connected via IB QDR. The operating system is TOSS 3. Slurm is used to manage user jobs. The underlying PFS is an LLNL
customized version of Lustre, 2.10.6 2.chaos. Each compute node is equipped with an 800GB Intel 910 Series SSD, which serves as the burst buffer device. The peak sequential write bandwidth of the node-local SSD is 1GB/s, and its peak sequential read bandwidth is 2GB/s. We repeated all runs at least 10 times, and the average results are reported.

## 6.1 I/O Of Scientific Applications

From a PFS perspective, within each file, there are three common parallel I/O access patterns: (1) *Contiguous*, where multiple processes access the file in a contiguous manner
(normally without gaps); (2) *Strided*, where multiple processes access the file in an interleaved manner (often with a fixed stride); and (3) *Random*, multiple processes access the file in a random manner. The random access pattern is commonly observed in deep learning applications, where multiple processes randomly load samples to feed the neural network. On the other hand, contiguous and strided

| File System   | Storage Model         |
|---------------|-----------------------|
| PosixFS       | POSIX consistency     |
| open          | bfs_open              |
| close         | bfs_close             |
| write         | bfs_write; bfs_attach |
| read          | bfs_query; bfs_read   |
| CommitFS      | Commit consistency    |
| open          | bfs_open              |
| close         | bfs_close             |
| write         | bfs_write             |
| read          | bfs_query; bfs_read   |
| commit        | bfs_attach_file       |
| SessionFS     | Session consistency   |
| open          | bfs_open              |
| close         | bfs_close             |
| write         | bfs_write             |
| read          | bfs_read              |
| session_open  | bfs_query_file        |
| session_close | bfs_attach_file       |

access patterns are commonly used in parallel scientific applications for performing logging, checkpointing, and outputting snapshots.

We constructed synthetic workloads to simulate common HPC I/O scenarios. Each workload consists of a write phase and/or a read phase, and the read phase begins only after the write phase is complete. Additionally, all processes operate on a single shared file, resulting in an N-to-1 access pattern, where N is the total number of processes. The access pattern within the shared file for each phase (contiguous, strided, or random) can be determined at runtime. The workload can be run on either commit consistency or session consistency using the corresponding APIs provided by CommitFS or SessionFS. The other aspects of the I/O behavior are controlled by the set of parameters summarized in Table 7.

nw
Number of writing nodes. All processes of a writing node perform only writes.
nr
Number of reading nodes. All processes of a
reading node perform only reads.
n
Total number of nodes; n = nr + nw.
p
Number of processes per node. Each node runs an equal number of processes.
mw
Number of writes performed by each process. Each writing process performs the same number of writes.
mr
Number of reads performed by each process. Each reading process performs the same number of reads.
s
Access size of each I/O operation. All I/O operations have the same access size.
We used the four configurations shown in Table 8 to conduct the experiments. Each was run on up to 16 nodes with 12 processes per node. In our experiments, write nodes and read nodes did not overlap, so nw and nr always added up to n. In all runs, we set mw = mr = 10. Additionally, to understand the impact of a consistency model on scenarios with different accesses sizes, all experiments were run with two different access sizes: 8KB for small accesses and 8MB for large accesses. The file system was purged before the start of each run.

| Code name   | Write phase   | Read phase   |
|-------------|---------------|--------------|
| n           |               |              |
| w           |               |              |
| n           |               |              |
| r           |               |              |
| CN-W        | Contiguous    | N/A          |
| SN-W        | Strided       | N/A          |
| CC-R        | Contiguous    | Contiguous   |
| n           |               |              |
| 2           |               |              |
| n           |               |              |
| 2           |               |              |
| CS-R        | Contiguous    | Strided      |
| n           |               |              |
| 2           |               |              |
| n           |               |              |
| 2           |               |              |

6.1.1
Write-only workloads The first two configurations, CN-W and SN-W, are writeonly and differ only in how writes are performed by the collaborating processes. Figure 3 shows their write bandwidths. With the use of node-local SSDs as burst buffers, all writes are buffered by process-private cache files, which essentially converts the N-1 writes (contiguous or strided)
to N −N contiguous writes. Therefore, for both consistency models, the performance of CN-W and SN-W were about the same.

Since the file system is empty when the writes start, session_open became a no-op, and session_close performed the same task as commit, thus session consistency and commit consistency achieved similar bandwidths.

Finally, small writes yielded a worse performance as the small access sizes cannot saturate the bandwidth. When performing large writes, both access patterns were able to achieve the peak write bandwidth, regardless of the consistency model. This is because the overhead required by the consistency model is insignificant compared to the time needed to write to SSD.

6.1.2
Read-after-write workloads The last two configurations, CC-R and CS-R, demonstrate the impact of consistency models on the read bandwidth of workloads with different access patterns. In these configurations, half of the nodes are used for writing and the other half for reading the data back. In CC-R, writes and reads are done contiguously, so each read node reads from only one write node. In contrast, in CS-R, reads are strided, which requires each read node to receive data from multiple write nodes and may cause contention.

The results in Figure 4 demonstrate that CC-R outperforms CS-R under both consistency models and access sizes. For large reads (Figure 4a), the impact of consistency models on the bandwidth is negligible. However, for small reads (Figure 4b), session consistency achieved better performance and scalability than commit consistency. This is because commit consistency issues an RPC query every time it performs a read, and when the I/O of a read completes quickly, the software overhead becomes the I/O bottleneck, especially when many read requests are performed concurrently. In contrast, session consistency only queries once at the session open time, and the overhead is amortized over a number of reads. Lastly, we observed a high variance in the bandwidth of session consistency. To verify whether this was caused by network or system congestion, we repeated the same experiments multiple times at different times of the day and found consistent results. A further investigation (where we used a single node and excluded the communication time) showed that the SSD itself had high variance in small read performance, which we believe is due to normal wear and tear, as SSDs on Catalyst are rather old. We confirmed this hypothesis by conducting the same experiments on a newer machine (Expanse at San Diego Supercomputer Center), which showed very little variance.

## 6.2 Case Study: I/O Of Scalable Checkpoint/Restart

In this subsection, we study the I/O behavior of SCR [26] for checkpointing and restarting HACC-IO [27] using an emulator. SCR is a scalable multi-level checkpointing system that supports multiple types of checkpoints with varying costs and levels of resiliency. The slowest but most resilient level writes to the system-wide PFS, which can withstand an entire system failure. Faster checkpointing for the most common failure modes involves using node-local storage, such as RAM and SSD, and implementing cross-node redundancy schemes.

In our emulation, we consider the most common case where SCR uses node-local storage only. We use the "Partner" redundancy scheme, where SCR writes checkpoints to local storage and also copies each checkpoint to storage local to a partner process from another failure group. This scheme requires twice the storage space, but it can withstand failures of multiple devices, so long as a device and the corresponding partner device that holds the copy do not fail simultaneously. To be specific, in our experiment, at the checkpoint phase, SCR buffers the checkpoint data in memory (local and partner) and then flushes it to the SSDs (local and partner) using a file-per-process access pattern. At the restart time, SCR reads directly from the memory buffer assuming the checkpoint data is still accessible.

The client of SCR is HACC-IO, which produces the actual checkpoint data. At each checkpoint step, HACC- IO writes out 9 arrays of the same length, each containing all particle values of a different physical variable. The total data size is determined by the number of particles, which we set to 10 million in our experiment. Furthermore, the experiment was run with one spare node, and we assumed a single-node failure. When running with n nodes, during the checkpoint phase, n − 1 nodes wrote to the node-local SSD, with a copy buffered in local memory. During the restart phase, n − 2 nodes read directly from the local memory buffer, and the spare node receives the checkpoint through MPI from the partner of the failed node.

We show the read and write bandwidths of checkpoint and restart phases in Figure 5. To better understand the read bandwidth, the result did not include the communication time for the spare node to get the checkpoint. Similar to the large-write experiments discussed earlier, SCR scaled well for checkpointing and achieved the peak bandwidth at all scales under both consistency models. In other words, the consistency model does not have a big impact on SCR's checkpointing bandwidth. However, for restarting, session consistency scaled better than commit consistency, mainly due to the low query frequency. At the restart phase, the reads were satisfied through memory buffers, and the overall read bandwidth scaled linearly with the number of nodes, which made the read time per node constant. However, under commit consistency, when more nodes were used, more query requests (one per read) were sent simultaneously to the global server, which then became the bottleneck and reduced scalability.

## 6.3 Case Study: I/O Of Distributed Deep Learning

Deep learning has thrived in recent years. However, as data sizes and system scales increase, traditional methods of feeding neural networks during training struggle to keep up with the required computation. To accelerate data ingestion rates, various methods [28], [29], [30], [31] have been proposed, such as data sharding, prestaging, and in-memory caching.

Here, we simulate the I/O of the "Preloaded" strategy that was proposed in [30] and implemented in LBANN [32]. Our simulation assigns to each process a non-overlapping subset of the training data. Before the training begins, each process loads its portion of data into its node-local SSD (hence the term Preloaded). Next, at the beginning of each epoch, each process is assigned a random subset of samples. The samples are evenly distributed to all processes so that each process performs an equal amount of work. During each epoch, each process reads the assigned samples, either locally or from other processes using MPI. It is worth noting that our benchmark is a simplified version of the Preloaded strategy that differs in two major ways: (1) we store data in node-local SSDs instead of memory, which is anyhow necessary for large datasets that do not fit in memory; and (2) we do not perform aggregations when sending samples to the same process, which places additional stress on the file system.

The average per-epoch read bandwidth is presented in Figure 6. We conducted both strong scaling and weak scaling experiments, with a mini-batch size of 1024 for strong scaling, and each process working on 32 samples per iteration for weak scaling. The sample size was set to 116KB, which is the same as the average image size of ImageNet-1K [33]. The number of processes per node was set to 4 (in real DL training, this number is usually set to match the number of GPUs per node). The results are very similar to those of small-reads experiments shown in Figure 4b, only the bandwidth is higher here thanks to the slightly larger reads (116KB vs. 8KB). In both strong scaling and weak scaling, session consistency outperformed commit consistency in terms of scalability and bandwidth, due to the less time spent on queries. Additionally, the increasing gap in bandwidth between the two consistency models with the number of nodes further emphasizes the significance of choosing an appropriate consistency model to achieve optimal performance and scalability.

## 6.4 Key Takeaways

Here, we present the key findings derived from our experiments.

- When performing large writes and reads (e.g., over one
megabyte per I/O operation), consistency models do not have a big impact on the I/O bandwidth. This is because the overhead of maintaining the consistency model (weaker or stronger) is insignificant compared to the time needed to to access the I/O device.
- When performing small writes and reads (e.g., ranging
from a few bytes to a few kilobytes), the adoption
of a stronger consistency model can noticeably hinder performance. This is attributed to the faster completion of each I/O operation, making the overhead of maintaining strong consistency a bottleneck. Moreover, the traffic required to maintain the consistency model can lead to contention, particularly when there is a high volume of small I/O operations.
- When I/O operations are directly fulfilled by memory
or fast devices like persistent memory, the choice of consistency models can significantly impact performance. This is due to a similar reason as mentioned earlier, where the faster completion of I/O operations magnifies the overhead associated with maintaining strong consistency models.
- For small random accesses (e.g., random reads of
deep learning applications), weaker consistency models demonstrate higher I/O bandwidth and improved scalability compared to stronger models. Notably, this improvement is significant even at smaller scales, indicating a promising direction for optimizing the I/O performance of deep learning applications.

## 7 Conclusion And Future Work

This work explored consistency models from the perspective of parallel file systems. We provided a high-level discussion on important aspects of storage consistency models, including their design choices and their comparison with memory models. Based on the commonalities of existing storage models, we proposed a unified and formal framework for specifying properly-synchronized SCNF models, which guarantee sequential consistency (or POSIX consistency) for programs that are properly synchronized. Additionally, we proposed a flexible design for implementing properly-synchronized SCNF models that isolates the consistency model from other file system components, making it easy to understand the impact of different consistency models on I/O performance.

We also presented a detailed performance comparison between commit consistency and session consistency. Our results indicate that session consistency is better suited for most HPC I/O workloads in terms of performance and scalability. Although this comes at the cost of slightly reduced programmability, the performance gain is potentially huge, especially for small reads such as those in deep learning applications. Overall, this work contributes to a better understanding of consistency models in parallel file systems and their impact on I/O performance.

In our future work, we will implement different relaxed storage models in existing PFSs to evaluate their performance impacts in a real-world setting. Additionally, we plan to study the consistency requirements of metadata operations for HPC applications and evaluate their performance implications.

## Acknowledgments

This work was supported by NSF SHF Collaborative grant 1763540 and was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344. LLNL- JRNL-849174-DRAFT. This material is based upon work supported by the U.S. Department of Energy, Office of Science, Office of Advanced Scientific Computing Research under the DOE Early Career Research Program.

## References

[1]
T. Patel, S. Byna, G. K. Lockwood, and D. Tiwari, "Revisiting I/O
Behavior in Large-Scale Storage Systems: the Expected and the
Unexpected," in Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, 2019, pp.
1–13.
[2]
A. K. Paul, O. Faaland, A. Moody, E. Gonsiorowski, K. Mohror,
and A. R. Butt, "Understanding HPC Application I/O Behavior
Using System Level Statistics," in 2020 IEEE 27th International
Conference on High Performance Computing, Data, and Analytics
(HiPC).
IEEE, 2020, pp. 202–211.
[3]
N. Dryden, R. B¨ohringer, T. Ben-Nun, and T. Hoefler, "Clairvoyant
Prefetching for Distributed Machine Learning I/O," arXiv preprint arXiv:2101.08734, 2021.
[4]
F. Di Natale, H. Bhatia, T. S. Carpenter, C. Neale, S. Kokkila-
Schumacher, T. Oppelstrup, L. Stanton, X. Zhang, S. Sundram,
T. R. Scogland *et al.*, "A Massively Parallel Infrastructure for Adaptive Multiscale Simulations: Modeling RAS Initiation Pathway
for Cancer," in Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, 2019, pp.
1–16.
[5]
"IEEE Standard for Information Technology–Portable Operating
System Interface (POSIX(TM)) Base Specifications, Issue 7," IEEE
Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008), pp. 1–3951, 2018.
[6]
P. Braam, "The Lustre Storage Architecture," arXiv preprint
arXiv:1903.01955, 2019.
[7]
F. B. Schmuck and R. L. Haskin, "GPFS: A Shared-Disk File System
for Large Computing Clusters." in *FAST*, vol. 2, no. 19, 2002.
[8]
F.
Herold,
S.
Breuner,
and
J.
Heichler,
"An
Introduction
to BeeGFS," 2014. [Online]. Available: https://www.beegfs.io/
docs/whitepapers/Introduction to BeeGFS by ThinkParQ.pdf
[9]
T. Wang, K. Mohror, A. Moody, W. Yu, and K. Sato, "BurstFS: A
Distributed Burst Buffer File System for Scientific Applications,"
in The International Conference for High Performance Computing, Networking, Storage and Analysis (SC), 2015.
[10] L. L. N. Laboratory, "UnifyFS: A File System for Burst Buffers ,"
https://github.com/LLNL/UnifyFS, Mar. 2021.
[11] A. Miranda, R. Nou, and T. Cortes, "echofs: A Scheduler-Guided
Temporary Filesystem to Leverage Node-local NVMs," in 2018
30th International Symposium on Computer Architecture and High
Performance Computing (SBAC-PAD).
IEEE, 2018, pp. 225–228.
[12] O. Tatebe, S. Moriwake, and Y. Oyama, "Gfarm/BB—Gfarm File
System for Node-Local Burst Buffer," Journal of Computer Science and Technology, vol. 35, no. 1, pp. 61–71, 2020.
[13] S. Oral, S. S. Vazhkudai, F. Wang, C. Zimmer, C. Brumgard,
J. Hanley, G. Markomanolis, R. Miller, D. Leverman, S. Atchley
et al., "End-to-end I/O Portfolio for the Summit Supercomputing Ecosystem," in Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, 2019, pp.
1–14.
[14] L. Lamport, "How to Make a Multiprocessor Computer That
Correctly Executes Multiprocess Progranm," IEEE transactions on computers, vol. 28, no. 09, pp. 690–691, 1979.
[15] P. Sewell, S. Sarkar, S. Owens, F. Z. Nardelli, and M. O. Myreen,
"x86-TSO: A Rigorous and Usable Programmer's Model for x86
Multiprocessors," *Communications of the ACM*, vol. 53, no. 7, pp.
89–97, 2010.
[16] M. Dubois, C. Scheurich, and F. Briggs, "Memory Access Buffering
in Multiprocessors," *ACM SIGARCH computer architecture news*,
vol. 14, no. 2, pp. 434–442, 1986.
[17] K. Gharachorloo, D. Lenoski, J. Laudon, P. Gibbons, A. Gupta, and
J. Hennessy, "Memory Consistency and Event Ordering in Scalable Shared-Memory Multiprocessors," ACM SIGARCH Computer Architecture News, vol. 18, no. 2SI, pp. 15–26, 1990.
[18] C. Wang, K. Mohror, and M. Snir, "File System Semantics Requirements of HPC Applications," in Proceedings of the 30th International
Symposium on High-Performance Parallel and Distributed Computing
(HPDC), 2020, pp. 19–30.
[19] IBM,
"Burst
Buffer
Shared
Checkpoint
File
System,"
Apr.
2020. [Online]. Available: https://github.com/IBM/CAST/tree/ master/bscfs
[20] S. Shepler, B. Callaghan, D. Robinson, R. Thurlow, C. Beame,
M. Eisler, and D. Noveck, "RFC3530: Network File System (NFS) Version 4 Protocol," 2003.
[21] P. Corbett, D. Feitelson, S. Fineberg, Y. Hsu, B. Nitzberg, J.-P. Prost,
M. Snir, B. Traversat, and P. Wong, "Overview of the MPI-IO
Parallel I/O Interface," in IPPS'95 Workshop on Input/Output in Parallel and Distributed Systems, 1995, pp. 1–15.
[22] "MPI: A Message-Passing Interface Standard Version 4.0," https:
//www.mpi-forum.org/docs/mpi-4.0/mpi40-report.pdf, 2021.
[23] S. V. Adve, "Designing Memory Consistency Models for Shared-
Memory Multiprocessors," Ph.D. dissertation, University of Wisconsin, Madison, 1993.
[24] S. V. Adve and M. D. Hill, "Weak Ordering - a New Definition,"
ACM SIGARCH Computer Architecture News, vol. 18, no. 2SI, pp.
2–14, 1990.
[25] J. Manson, W. Pugh, and S. V. Adve, "The Java Memory Model,"
ACM SIGPLAN Notices, vol. 40, no. 1, pp. 378–391, 2005.
[26] A. Moody, G. Bronevetsky, K. Mohror, and B. R. De Supinski, "Design, Modeling, and Evaluation of a Scalable Multi-level Checkpointing System," in SC'10: Proceedings of the 2010 ACM/IEEE
International Conference for High Performance Computing, Networking,
Storage and Analysis.
IEEE, 2010, pp. 1–11.
[27] "HACC IO Kernel from the CORAL Benchmark Codes," https:
//asc.llnl.gov/coral-benchmarks#hacc, Jan 2018.
[28] Y. Oyama, N. Maruyama, N. Dryden, E. McCarthy, P. Harrington,
J. Balewski, S. Matsuoka, P. Nugent, and B. Van Essen, "The Case for Strong Scaling in Deep Learning: Training Large 3D
CNNs With Hybrid Parallelism," IEEE Transactions on Parallel and Distributed Systems, vol. 32, no. 7, pp. 1641–1652, 2020.

[29] P. Goyal, P. Doll´ar, R. Girshick, P. Noordhuis, L. Wesolowski,
A. Kyrola, A. Tulloch, Y. Jia, and K. He, "Accurate, Large
Minibatch SGD: Training ImageNet in 1 Hour," arXiv preprint arXiv:1706.02677, 2017.
[30] S. A. Jacobs, B. Van Essen, D. Hysom, J.-S. Yeom, T. Moon,
R. Anirudh, J. J. Thiagaranjan, S. Liu, P.-T. Bremer, J. Gaffney *et al.*,
"Parallelizing Training of Deep Generative Models on Massive
Scientific Datasets," in 2019 IEEE International Conference on Cluster
Computing (CLUSTER).
IEEE, 2019, pp. 1–10.
[31] S. A. Jacobs, N. Dryden, R. Pearce, and B. Van Essen, "Towards
Scalable Parallel Training of Deep Neural Networks," in Proceedings of the Machine Learning on HPC Environments, 2017, pp. 1–9.
[32] B. Van Essen, H. Kim, R. Pearce, K. Boakye, and B. Chen,
"LBANN: Livermore Big Artificial Neural Network HPC Toolkit,"
in Proceedings of the Workshop on Machine Learning in High- Performance Computing Environments, ser. MLHPC '15.
New
York, NY, USA: ACM, 2015, pp. 5:1–5:6. [Online]. Available: http://doi.acm.org/10.1145/2834892.2834897
[33] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, "Imagenet: A large-scale hierarchical image database," in 2009 IEEE conference on computer vision and pattern recognition.
Ieee, 2009, pp.
248–255.

Chen Wang is Fernbach Postdoctoral Fellow
at Lawrence Livermore National Laboratory. He
is currently working at the Center for Applied
Scientific Computing at LLNL. He received his
Ph.D in computer science from University of Illi-
nois Urbana-Champaign. His research interests
include parallel computing, I/O and communica-
tion tracing, and parallel storage systems.

                  Kathryn Mohror is a computer scientist in the
                  Parallel Systems Group in the Center for Ap-
                  plied Scientific Computing (CASC) at Lawrence
                  Livermore National Laboratory (LLNL). Kathryn
                  serves as the Deputy Director for the Labora-
                  tory Directed Research & Development (LDRD)
                  program at LLNL, Lead for the NNSA Soft-
                  ware Technologies Portfolio for the U.S. Exas-
                  cale Computing Project (ECP), and as the ASCR
                  Point of Contact for Computer Science at LLNL.
                  Kathryn's research on high-end computing sys-
tems is currently focused on I/O for extreme scale systems. Her other
research interests include scalable performance analysis and tuning,
fault tolerance, and parallel programming paradigms.

                   Marc Snir is Michael Faiman Emeritus Profes-
                   sor in the Department of Computer Science at
                   the University of Illinois Urbana-Champaign. He
                   was Director of the Mathematics and Computer
                   Science Division at the Argonne National Labo-
                   ratory from 2011 to 2016 and head of the Com-
                   puter Science Department at Illinois from 2001
                   to 2007. Until 2001 he was a senior manager
                   at the IBM T. J. Watson Research Center where
                   he led the Scalable Parallel Systems research
                   group that was responsible for major contribu-
tions to the IBM scalable parallel system and to the IBM Blue Gene
system.

