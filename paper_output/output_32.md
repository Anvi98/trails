# Hybrid Integrator-Gain System Based Integral Resonant Controllers For Negative Imaginary Systems

Kanghong Shi, Ian R. Petersen, Life Fellow, IEEE

  Abstract— We introduce a hybrid control system called a
hybrid integrator-gain system (HIGS) based integral resonant
controller (IRC) to stabilize negative imaginary (NI) systems.
A HIGS-based IRC has a similar structure to an IRC, with
the integrator replaced by a HIGS. We show that a HIGS-
based IRC is an NI system. Also, for a SISO NI system with
a minimal realization, we show there exists a HIGS-based IRC
such that their closed-loop interconnection is asymptotically
stable. Also, we propose a proportional-integral-double-integral
resonant controller (PII2RC) and a HIGS-based PII2RC and
show that both of them can be applied to asymptotically
stabilize an NI system. An example is provided to illustrate
the proposed results.
  Index Terms— hybrid integrator-gain system, integral reso-
nant control (IRC), negative imaginary (NI) system, stability,
robust control.

## I. Introduction

Negative imaginary (NI) systems theory was introduced in [1], [2] to address the robust control problem for flexible structures [3]–[5], which usually have highly resonant dynamics. Roughly speaking, a square, real-rational and proper transfer function G(s) is said to be NI if it has no strict righthalf plane poles and its frequency response G(jω) satisfies j [G(jω) − G(jω)∗] for all ω > 0 [1]. Typical examples of NI systems are mechanical systems with colocated force actuators and position sensors. NI systems theory provides an alternative approach to the passivity theory [6] when velocity measurements are unavailable. In comparison to passivity theory, which can only deal with systems with a relative degree of zero or one, an advantage of NI systems theory is that it allows systems to have relative degree zero, one, and two [7]. An NI system can be stabilized using a strictly negative imaginary (SNI) system. Under some assumptions, the positive feedback interconnection of an NI
system G(s) and an SNI system R(s) is asymptotically stable if and only if the DC loop gain of the interconnection is strictly less than unity; i.e., λmax(G(0)R(0)) < 1 (e.g., see
[8]). NI systems theory has found its applications in many fields including nano-positioning [9]–[12], control of lightly damped structures [13]–[15], and control of power systems [16].

NI systems theory was extended to nonlinear systems in [17]–[19]. A nonlinear system is said to be NI if the system is dissipative with respect to the inner product of

  This work was supported by the Australian Research Council under grant
DP230102443.
  K. Shi and I. R. Petersen are with the School of Engineering, College of
Engineering, Computing and Cybernetics, Australian National University,
Canberra, Acton, ACT 2601, Australia. kanghong.shi@anu.edu.au,
ian.petersen@anu.edu.au.

the system input and the time derivative of the system
output. Under some assumptions, a nonlinear NI system
can be asymptotically stabilized using a nonlinear output
strictly negative imaginary (OSNI) system. Such a nonlinear
extension of NI systems theory not only makes NI systems
theory applicable to a broader class of plants, but also allows
the use of more advanced controllers.
  One such controller is the hybrid integrator-gain system
(HIGS). HIGS elements were introduced in [20] to overcome
the inherent limitations of linear control systems (see e.g.,
[21]). A HIGS switches between an integrator mode and a
gain mode in order to have a sector-bounded input-output
relationship. Compared with an integrator, which has a phase
lag of 90◦, a HIGS has a similar magnitude slope but only a
38.1◦ phase lag. This 52.9◦ phase reduction can significantly
reduce time delay, and as a consequence, the overshoot; see
[22] for a concrete example; see also [23]–[26]. It is shown
in [27] that a HIGS element is a nonlinear NI system, and
can be applied as a controller to asymptotically stabilize an
NI plant. Different variants of HIGS are investigated in [28]
and [29] to provide control methods for multi-input multi-
output (MIMO) NI systems and discrete-time NI systems,
respectively. Also, as is reported in [28], a HIGS con-
troller was applied to improve the performance of a MEMS
nanopositioner in a hardware experiment. Considering the
effectiveness of HIGS-based control and the advantages of
HIGS elements over linear integral controllers, we may
naturally ask the question: rather than using a HIGS as a
standalone controller, can we replace integrators with HIGS
elements in more intricate controllers to enhance control
performance? In this paper, we investigate this problem for
a HIGS-based integral resonant controller .
  IRC was introduced in [30] to provide damping control for
flexible structures. For a system with transfer matrix G(s), an
IRC is implemented by first adding a direct feedthrough D to
the system G(s) and then applying an integrator in positive
feedback to G(s)+D. Adding such a feedthrough D changes
the pole-zero interlacing of G(s) into a zero-pole interlacing
in G(s) + D. It is shown in [2], [31] that an IRC is an SNI
system and can stabilize systems with the NI property. Since
IRC are effective in damping control and easy to implement,
they have been widely applied in the control of NI systems;
e.g., see [32]–[34].
  In this paper, we propose a HIGS-based IRC by replacing
the integrator in an IRC by a HIGS element. The advantages
of a HIGS-based IRC are two-fold: 1) it utilizes the advan-
tages of a HIGS in terms of small phase lag, reduced time
delay and reduced overshoot; 2) A HIGS has two parameters

- the integrator frequency and gain value, while an integrator
only has one parameter Γ. Hence, a greater degree of freedom
in parameters is allowed in controller design using a HIGS-
based IRC. We provide a state-space model of a HIGS-based
IRC. We show that a HIGS-based IRC has the nonlinear
NI property. We also show that given a SISO NI system
with minimal realization, there exists a HIGS-based IRC
such that their closed-loop interconnection is asymptotically
stable. This is illustrated using an example.
  We also investigate proportional-integral-double-integral
resonant controllers (PII2RC) in this paper. A PII2RC is
implemented by replacing the integrator in an IRC by
a proportional-integral-double-integral controller with the
transfer function C(s) = kp + k1/s + k2/s2. We show that
a PII2RC is an SNI system and can asymptotically stabilize
an NI plant. Then, by replacing the integrators in an PII2RC
with HIGS elements, we construct a HIGS-based PII2RC. We
show that a HIGS-based PII2RC can also provide asymptotic
stabilization for NI plants.
  The rest of the paper is organized as follows: Section
II provides some preliminary results on negative imaginary
systems theory, IRC and HIGS. Section III provides a model
for the HIGS-based IRC and shows that it can be used in
the control of NI systems. Section IV introduces a PII2RC
and also gives a stability proof for the interconnection of an
NI system a PII2RC. Section V introduces the HIGS-based
PII2RC and shows that it can be applied in the stabilization
of NI systems. In Section VI, we illustrate the main results
in this paper that are given in Section III on a mass-spring
system example. The paper is concluded in Section VII.
  Notation: The notation in this paper is standard. R denotes
the field of real numbers. Rm×n denotes the space of real
matrices of dimension m × n. AT denotes the transpose of
a matrix A. A−T denotes the transpose of the inverse of A;
that is, A−T = (A−1)T = (AT )−1. λmax(A) denotes the
largest eigenvalue of a matrix A with real spectrum. ∥ · ∥
denotes the standard Euclidean norm. For a real symmetric
or complex Hermitian matrix P, P > 0 (P ≥ 0) denotes the
positive (semi-)definiteness of a matrix P and P < 0 (P ≤
0) denotes the negative (semi-)definiteness of a matrix P.
A function V : Rn → R is said to be positive definite if
V (0) = 0 and V (x) > 0 for all x ̸= 0.

## Ii. Preliminaries A. Negative Imaginary Systems

We consider systems of the form

$\dot{x}=f(x,u)$, (1a) $y=h(x)$, (1b)

where x ∈ Rn, u, y ∈ Rp are the state, input and output
of the system, respectively. Here, f : Rn × Rp → Rn is
a Lipschitz continuous function and h : Rn → Rp is a
continuously differentiable function. We assume f(0, 0) = 0
and h(0) = 0.
  Definition 1 (NI systems):
                         [17], [18] A system of the
form (1) is said to be a negative imaginary (NI) system

if there exists a positive definite continuously differentiable storage function V : Rn → R such that for any locally integrable input u and solution x to (1),
˙V (x(t)) ≤ u(t)T ˙y(t),
∀ t ≥ 0.

We provide the following conditions for a linear system to be NI. This condition is referred to as the NI lemma (see [35]).

Lemma 1 (NI lemma):
[35] Let (A, B, C, D) be a minimal state-space realization of an p × p real-rational proper transfer function matrix G(s) where A ∈ Rn×n, B ∈ Rn×p, C ∈ Rp×n, D ∈ Rp×p. Then R(s) is NI if and only if:
1. det A ̸= 0, D = DT ;
2. There exists a matrix Y = Y T > 0, Y ∈ Rn×n such that AY + Y AT ≤ 0, and B + AY CT = 0.

(2)

## B. Integral Resonant Control

The implementation of an IRC is shown in Fig. 1. Given a SISO plant with a transfer function G(s), we apply a direct feedthrough D and also an integral controller

$$C(s)=\frac{\Gamma}{s}\tag{3}$$
in positive feedback with G(s) + D. Here, we require the matrices Γ, D ∈ R to satisfy D < 0 and Γ > 0. The block diagram in Fig. 1 can be equivalently represented by the block diagram in Fig. 2, where K(s) is given as

$$K(s)=\frac{C(s)}{1-C(s)D}.\tag{4}$$

Substituting (3) in (4), we obtain the transfer function of the IRC:

$$K(s)=\frac{\Gamma}{s-\Gamma D}.\tag{5}$$
An IRC is an SNI system, and can be used in the control of NI plants (see [1], [2], [31]).

r e(s) U(s) Y (s) Y (s) G(s) C(s)

## C. Hybrid Integrator-Gain Systems

A SISO hybrid integrator-gain system (HIGS) $\mathcal{H}$ is represented by the following differential algebraic equations [20]:

$$\mathcal{H}:\begin{cases}\dot{x}_{h}=\omega_{h}e,&\text{if}(e,u,\dot{e})\in\mathcal{F}_{1}\\ x_{h}=k_{h}e,&\text{if}(e,u,\dot{e})\in\mathcal{F}_{2}\\ u=x_{h},\end{cases}\tag{6}$$

where xh, e, u ∈ R denote the state, input, and output of
the HIGS, respectively. Here, ˙e is the time derivative of the
input e, which is assumed to be continuous and piecewise
differentiable. Also, ωh ∈ [0, ∞) and kh ∈ (0, ∞) represent
the integrator frequency and gain value, respectively. These
tunable parameters allow for desired control performance.
The sets F1 and F2 ∈ R3 determine the HIGS modes of
operation; i.e. the integrator and gain modes, respectively.
The HIGS is designed to operate under the sector constraint
(e, u, ˙e) ∈ F (see [20], [36]) where

$$\mathcal{F}=\{(e,u,\dot{e})\in\mathbb{R}^{3}\mid eu\geq\frac{1}{k_{h}}u^{2}\},\tag{7}$$
and F1 and F2 are defined as

$$\mathcal{F}_{1}=\mathcal{F}\setminus\mathcal{F}_{2};$$ $$\mathcal{F}_{2}=\{(e,u,\dot{e})\in\mathbb{R}^{3}\mid u=k_{h}e\text{and}\omega_{h}e^{2}>k_{h}e\dot{e}\}.\tag{8}$$

A HIGS of the form (6) is designed to primarily operate
in the integrator mode unless the HIGS output u is on the
boundary of the sector F, and tends to exit the sector;
i.e. (e, u, ˙e) ∈ F2. In this case, the HIGS is enforced to
operate in the gain mode. At the time instants when switching
happens, the state xh still remains continuous, as can be seen
from (6).

## Iii. Higs-Based Irc For Ni Systems

In this section, we provide the system model of a HIGS-
based IRC. Also, we show that a HIGS-based IRC has the NI property and can be applied in the control of an NI plant.

## A. Higs-Based Irc

Consider the structure of an IRC as shown in Fig. 1.

A HIGS-based IRC is constructed similarly but with the integrator C(s) in Fig. 1 replaced by a HIGS of the form
(6). The implementation of a HIGS-based IRC is shown in Fig. 3.

We aim to derive the model of the HIGS-based IRC, which takes r+y as input and gives an output u, as shown in Fig. 4.

According to the settings in Fig. 3 and Fig. 4, we have that Therefore, we have

$$e=r+y+Du;$$ $$\widetilde{e}=r+y.\tag{9}$$

$$e=\widetilde{e}+Du=\widetilde{e}+Dx_{h},\tag{10}$$

where the second equality uses (6). When the HIGS is in the integrator mode, we have that

$$\dot{x}_{h}=\omega_{h}e=\omega_{h}Dx_{h}+\omega_{h}\widetilde{e}.\tag{11}$$

When the HIGS is in the gain mode, we have that 
which implies

xh = khe = khDxh + kh�e, (12) xh = kh 1 − khD �e. (13)
Also, we reformulate the sets F, F1 and F2 to pose conditions on (�e, u, ˙�e) instead of (e, u, ˙e). Substituting (10) into
(7) and (8), we have that

kh u2}, (14) �F = {(�e, u, ˙�e) ∈ R3 | �eu ≥ 1 − khD �F2 = {(�e, u, ˙�e) ∈ R3 | u = kh 1 − khD �e and ωh�e2 > kh�e˙�e}.
(15)
To summarize, the system model of a HIGS-based IRC is given as follows:

   � H : ˙xh = ωhDxh + ωh�e, if (�e, u, ˙�e) ∈ �F1 xh = �κ�e, if (�e, u, ˙�e) ∈ �F2 u = xh, (16)  
where xh, �e, u ∈ R are the state, input and output of the HIGS-based IRC, respectively. The variable �e denotes the time derivative of the input �e and is assumed to be continuous and piecewise differentiable. The constants ωh ≥ 0, D < 0
and kh > 0 are the system parameters. Also, we denote the new gain value by

1 − khD (17) �κ := kh
since it will repeatedly occur in what follows. The HIGS-
based IRC satisfies the sector constraint (�e, u, ˙�e) ∈ �F where
(38), K(0) = − 1
D. Therefore, stability is achieved if and only if G(0)(− 1
D) < 1. That is, D < −G(0). Note that here G(0) = −CA−1B = CY CT ≥ 0, according to Lemma 1.

            V. HIGS-BASED PII2RC
 Motivated by the PII2RC proposed in Section IV, we
consider a HIGS-based PII2RC in this section. To be specific,
we consider replacing the single integrator k1/s in the
PII2RC by a single HIGS of the form (6). Also, we replace
the double integrator k2/s2 by two serial cascaded HIGS,
both of the form (6).

 The HIGS H1, H2 and H3 are of the form (6), with
different parameters. We provide the system models of H1,
H2 and H3 again in the following to distinguish different
parameters in these three HIGS:

$$\mathcal{H}_{i}:\begin{cases}\dot{x}_{hi}=\omega_{hi}e_{i},&\text{if}(e_{i},x_{hi},e_{i})\in\mathcal{F}_{i1}\\ x_{hi}=k_{hi}e_{i},&\text{if}(e_{i},x_{hi},e_{i})\in\mathcal{F}_{i2}\end{cases}\tag{40}$$
where ei ∈ R is the input, xhi ∈ R is the state and also the output of the HIGS Hi (i = 1, 2, 3), respectively. Here, ˙ei is the time derivative of the input ei, which is assumed to be continuous and piecewise differentiable. The parameters
ωhi ∈ [0, ∞) and khi ∈ (0, ∞) represent the integrator frequency and gain value of the HIGS Hi, respectively. Also, we have

$$\mathcal{F}_{i}=\{(e_{i},x_{hi},\dot{e}_{i})\in\mathbb{R}^{3}\mid e_{i}x_{hi}\geq\frac{1}{k_{hi}}x_{hi}^{2}\},\tag{41}$$

$$\mathcal{F}_{i1}=\mathcal{F}_{i}\setminus\mathcal{F}_{i2};\tag{42}$$

$$\mathcal{F}_{i2}=\{(e_{i},x_{hi},\dot{e}_{i})\in\mathbb{R}^{3}\mid x_{hi}=k_{hi}e_{i}\text{and}\omega_{hi}e_{i}^{2}>k_{hi}e_{i}e_{i}\}.\tag{43}$$

According to the setting of the system $\mathcal{H}_{h}$ in Fig. 6, we have that

$$e_{1}=e_{2}=e;\text{and}e_{3}=x_{h2}.\tag{44}$$
The integrator frequency ωh1 of the HIGS H1 corresponds to the parameter k1 of the PII2 controller �C(s) given in
(36). Also, the product of the integrator frequencies ωh2
and ωh3 corresponds to the parameter k2 in (36). Hence, for simplicity, we let

$\omega_{h2}=\omega_{h3}$, and $k_{h2}=k_{h3}$. (45)

  We prove in the following that the closed-loop inter-
connection shown in Fig. 6 is asymptotically stable. First,
we provide some preliminary results on the nonlinear NI
property of a single HIGS and two cascaded HIGS; see also
[28]. Note that the notation used in the present paper is
different from that in [28].
  Lemma 3: (see [27], [28]) A HIGS H1 of the form (40) is
a nonlinear NI system from input e1 to the output xh1 with
the storage function

$$V_{1}(x_{h1})=\frac{1}{2k_{h1}}x_{h1}^{2}$$

satisfying

$$\dot{V}(x_{h1})\leq e_{1}\dot{x}_{h1}.\tag{46}$$
Also, if ˙V (xh1) = e1 ˙xh1 then for all t ∈ [ta, tb] we have that xh1 = kh1.

Lemma 4: (see also [28]) Consider a HIGS H1 of the form (40). If ˙V (xh1) = e1 ˙xh1, then xh1 = kh1e1.

Proof: This lemma is a special single channel case of Lemma 4 in [28].

 Lemma 5: (see [28]) Consider two HIGS H2 and H3 of
the form (40) and satisfy (45). Then the serial cascade of H2
and H3 as shown in Fig. 7 is a nonlinear NI system with the
storage function

$$V_{2}(x_{h2},x_{h3})=\frac{1}{2}x_{h2}^{2}\tag{47}$$

satisfying

$$\dot{V}(x_{h2},x_{h3})\leq e_{2}\dot{x}_{h3}.\tag{48}$$
Moreover, if
˙V (xh2, xh3) = e2 ˙xh3 over a time interval
[ta, tb], where ta < tb, then for all t ∈ [ta, tb] we have that xh2 = kh2e2 and xh3 = kh2e2 = k2
h2e2.

Proof:
The proof follows directly from Theorem 5
in [28], with (45) assumed. The parameter a in Theorem
5 in [28] is allowed to take the value a =
kh3
2kh2 =
1
2, which results the storage function V2(xh2, xh3) in (47) to be positive semidefinite instead of positive definite.

$e_{2}$$\mathcal{H}_{2}$$\mathcal{H}_{2}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$$\mathcal{H}_{3}$\(

  Theorem 4: Consider the SISO minimal linear NI system
(27) with transfer function G(s). Also, consider a HIGS-
based PII2 controller Hh applied in positive feedback with
G(s)+D, as shown in Fig. 6, where D < 0 is a scalar. Here,
Hh is the parallel cascade of the HIGS H1, the serial cascade
of two HIGS H2 and H3, and also a gain kp > 0. Each HIGS

is of the form (40), where (45) is also assumed. Then there
exists a set of parameters {D, kp, ωh1, ωh2, kh1, kh2} such
that the closed-loop system shown in Fig. 6 is asymptotically
stable.
    Proof: According to Fig. 6, we have that

$$e=Cx+Du=Cx+D(x_{h1}+x_{h3}+k_{p}e)$$ $$\Longrightarrow\ e=\gamma Cx+\gamma D(x_{h1}+x_{h3}),\tag{49}$$

where

$$\gamma=\frac{1}{1-Dk_{p}}>0.\tag{50}$$
Also, we have that

u = xh1 + xh3 + kpe = kpγCx + γ(xh1 + xh3) (51)
We apple Lyapunov's direct method using the candidate Lyapunov function

W(x, xh1, xh2, xh3) = 1   x xh1 xh2 xh3 2 �xT xh1 xh2 xh3 � M   (52) where Y −1 − kpγCT C −γCT 0 −γCT −γC 1 M =   kh1 − Dγ 0 −Dγ 0 0 1 0 −γC −Dγ 0 −Dγ  . (53) 
First, we show the positive definiteness of the function W(x, xh1, xh2, xh3) by showing M > 0. Observing the third block row and block column of M, we have M > 0 if and only if

−γC 1   kh1 − Dγ −Dγ −γC −Dγ −Dγ � M =  Y −1 − kpγCT C −γCT −γCT  > 0. (54) 1 γ Y −1 − kpCT C −CT −CT
Since kp > 0 and D < 0, we have that γ > 0. Therefore,
�
M > 0 if and only if

−C 1   kh1γ − D −D −C −D −D γ � M = � M = 1   > 0 (55)
We apply Schur complement theorem in the following.

Observing that the 3, 3 block �
M33 = −D > 0, then �
M > 0
if and only if

γ Y −1 − kpCT C −CT M =� M/� M33 D −C 1 D kh1γ − D = � 1 � CT � + 1 � � C D � γ Y −1 − (kp − 1 D)CT C 0 0 1 kh1γ = � 1 � (56)
Since
1
kh1γ > 0, then we have M > 0 if and only if

$$\frac{1}{\gamma}Y^{-1}-(k_{p}-\frac{1}{D})C^{T}C>0\tag{57}$$
Substituting (50) into (57), we have that (57) holds if and only if

$Y^{-1}+\frac{1}{D}C^{T}C>0$ (58)
Using Schur complement theorem, (58) is equivalent to the positive definiteness of the matrix

$$Q=\begin{bmatrix}Y^{-1}&C^{T}\\ C&-D\end{bmatrix}\tag{59}$$
Also, considering that Y > 0, we have Q > 0 if and only if

−D − CY CT > 0. (60)
Considering that G(0) = −CA−1B = CY CT according to
(2), the condition (60) can be expressed as

D < −G(0). (61)
Therefore, the function W(x, xh1, xh2, xh3) given in (52) is positive definite if and only if (61) is satisfied. Taking the time derivative of W(x, xh1, xh2, xh3), we have

˙W(x, xh1, xh2, xh3) = xT Y −1 ˙x + 1 kh1 xh1 ˙xh1 + xh2 ˙xh2 − γ( ˙xh1 + ˙xh3)Cx − γ(xh1 + xh3)C ˙x − γD(xh1 + xh3)( ˙xh1 + ˙xh3) − kpγxT CT C ˙x = � xT Y −1 − � γ(xh1 + xh3) − kpγxT CT �� C ˙x kh1 xh1 ˙xh1 − (γCx + γD(xh1 + xh3)) ˙xh1 � + � 1 + [xh2 ˙xh2 − (γCx + γD(xh1 + xh3)) ˙xh3] = � xT Y −1 − uC � ˙x + � ˙V1(xh1) − e ˙xh1 � + � ˙V2(xh2, xh3) − e ˙xh3 � . (62) We have that � xT Y −1 − uC � ˙x = � xT AT A−T Y −1 + uBT A−T Y −1� ˙x = ˙xT (A−T Y −1) ˙x = � xT AT + uBT � A−T Y −1 ˙x = 1 2 ˙xT (A−T Y −1 + Y −1A−1) ˙x ≤ 0. (63)
Also, we have that ˙V1(xh1) − e ˙xh1 ≤ 0 and ˙V2(xh2, xh3) −
e ˙xh3 ≤ 0 according to the NI property of the H1 and the cascade of H2 and H3, as shown in Lemmas 3 and 5.

Therefore, ˙W(x, xh1, xh2, xh3) ≤ 0, which implies that the closed-loop interconnection in Fig. 6 is Lyapunov stable. We apply LaSalle's invariance principle in the following to show asymptotic stability. In the case that
˙W(x, xh1, xh2, xh3)
remains zero, we have that ˙xT (A−T Y −1 + Y −1A−1) ˙x ≡ 0,
˙V1(xh1)−e ˙xh1 ≡ 0 and ˙V2(xh2, xh3)−e ˙xh3 ≡ 0. According to Lemma 4, ˙V1(xh1) − e ˙xh1 ≡ 0 implies

$\mathbf{x}_{h1}=\mathbf{k}_{h1}\mathbf{e}$. (64)
Also, according to Lemma 5,
˙V2(xh2, xh3) − e ˙xh3 ≡ 0
implies

$$x_{h2}\equiv k_{h2}e,\tag{65}$$ $$x_{h3}\equiv k_{h2}^{2}e.\tag{66}$$

$x_{h2}\equiv k_{h2}e$ and $x_{h3}\equiv k_{h2}^{2}e$. We show that the HIGS ${\cal H}_{1}$, ${\cal H}_{2}$ and ${\cal H}_{3}$ cannot stay in the integrator mode ${\cal F}_{i1}$ by contradiction. According to (40), if $(e_{i},x_{hi},\dot{e}_{i})\in{\cal F}_{i1}$, then $\dot{x}_{hi}=\omega_{hi}e_{i}$. Since $x_{hi}=k_{hi}e_{i}$, then we have $k_{hi}\dot{e}_{i}=\omega_{hi}e_{i}$. That is,

$$\dot{e}_{i}=\frac{\omega_{hi}}{k_{hi}}e_{i},\tag{67}$$

which implies that ei diverges and so is xhi. This contradicts
the Lyapunov stability of the interconnection that is proved
above. Therefore, the HIGS H1, H2 and H3 all stay in the
gain mode Fi2. In this case, according to (43), we have that
ωhie2
    i > khiei ˙ei. That is

$$\omega_{h1}e^{2}>k_{h1}e{\dot{e}};$$
$$\omega_{h2}e^{2}>k_{h2}e{\dot{e}};$$
ωh2x2
h2 > kh2xh2 ˙xh2 =⇒ ωh2e2 > kh2e˙e, for H1, H2 and H3, respectively. Hence, we have

$$\rho e^{2}>e\dot{e},\tag{68}$$

where $\rho=\min\{\frac{\omega_{11}}{k_{h1}},\frac{\omega_{h2}}{k_{h2}}\}$. We show in the following that the condition (68) can be satisfied over time by satisfying $e\dot{e}<0$. In this case that $e\dot{e}<0$, the HIGS input $e$ converges. This implies that $x_{h1}$, $x_{h2}$ and $x_{h3}$ all converge to zero. Also, according to (49) and (51), $y$ and $u$ also converge. This is not the case of $W(x,x_{h1},x_{h2},x_{h3})\equiv0$ that is considered here. Also, we can avoid the case that (68) is satisfied by satisfying $\dot{e}\equiv0$ overtime. When $e$ is a constant, the HIGS states $x_{h1}$, $x_{h2}$ and $x_{h3}$ are all constants, according to (64), (65) and (66). Also, according to (49) and (51), we have that $y=Cx$ is a constant and also $u$ is a constant. Since the system (27) is observable, we have that $\dot{x}=0$ and the system (27) is in a steady state. Denote the constant values of $u$ and $e$ by $\overline{u}$ and $\overline{e}$, respectively, we have that

$$\overline{u}=(k_{h1}+k_{h2}^{2}+k_{p})\overline{e},\tag{69}$$
according to the system setting in Fig. 6. Also, we have that

$$\overline{e}=(G(0)+D)\overline{u}.\tag{70}$$

Therefore, by choosing suitable parameters $k_{h1}$, $k_{h2}$, and $k_{p}$ such that

$$k_{h1}+k_{h2}^{2}+k_{p}\neq\frac{1}{G(0)+D},\tag{71}$$
we can avoid the case that ˙e ≡ 0. Hence, e˙e > 0 will be satisfied eventually. In this case, since the trajectories of e and ˙e are independent of ωh1 and ωh2 when all of the HIGS are in the gain mode F2i, then we can always choose ωh1 or ωh2 to be sufficiently small such that ρe2 <
e˙e. Therefore, ˙W(x, xh1, xh2, xh3) cannot remain zero over time and W(x, xh1, xh2, xh3) will keep decreasing until W(x, xh1, xh2, xh3) = 0. This implies that the interconnection in Fig. 6 is asymptotically stable.

## Vi. Example

In this section, we apply the proposed HIGS-based IRC to stabilize a mass-spring system. As is shown in Fig. 8, the mass of the cart is $m=1kg$ and the spring constant is $k=1N/m$. The state-space model of the system is given as follows:

$$\dot{x}=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}x+\begin{bmatrix}0\\ 1\end{bmatrix}u;\tag{72}$$ $$y=\begin{bmatrix}1&0\end{bmatrix}x,$$ $$\begin{bmatrix}\end{bmatrix}\text{is the system state with}x_{1}\text{and}x_{2}\text{being its}\\ \text{id velocity,respectively.Also,}u\text{is an external}\end{bmatrix}$$
where x =
�x1
x2
displacement and velocity, respectively. Also, u is an external force input and we measure the system displacement as its output y. The system (72) has a transfer function G(s) =

$$ y$$

$$ k=1N/m$$
$$ \begin{array}{l}\underline{m=1kg\quad\vline{0.75cm}}\end{array}\begin{array}{l}\underline{u}\\ \underline{v}\end{array}$$
1
s2+1. We construct a HIGS-based IRC of the form (16) with
ωh = 0.5, kh = 20, D = −1.

(73)

Using (17), we have that �κ =
                              5
                              6. Such a �κ satisfies the
condition �κG(0) < 1. We set the initial state of the system
(72) be x1(0) = 3, x2(0) = 1. The initial state of the HIGS-
based IRC is set to be zero. We can see from Fig. 9 that the
states of the system (72) converge to the origin under the
effect of the HIGS-based IRC.

## State Trajectories Vii. Conclusion

  In this paper, we introduce a HIGS-based IRC to provide
a control approach for an NI system, with the advantages of
both HIGS and IRC utilized. A HIGS-based IRC is achieved
by replacing the integrator in an IRC by a HIGS element.
We show that a HIGS-based IRC is an NI system and can
stabilize an NI plant when applied in positive feedback. Also,
we propose a PII2RC and a HIGS-based PII2RC for the

control of NI systems. We show that both a PII2RC and a HIGS-based PII2RC can provide asymptotic stabilization for an NI system. An illustrative example is also provided.

## References

[1] A. Lanzon and I. R. Petersen, "Stability robustness of a feedback interconnection of systems with negative imaginary frequency response,"
IEEE Transactions on Automatic Control, vol. 53, no. 4, pp. 1042–
1046, 2008.
[2] I. R. Petersen and A. Lanzon, "Feedback control of negative-imaginary
systems," *IEEE Control Systems Magazine*, vol. 30, no. 5, pp. 54–72,
2010.
[3] A. Preumont, *Vibration control of active structures: an introduction*.
Springer, 2018, vol. 246.
[4] D. Halim and S. O. R. Moheimani, "Spatial resonant control of
flexible structures-application to a piezoelectric laminate beam," IEEE
Transactions on Control Systems Technology, vol. 9, no. 1, pp. 37–53,
2001.
[5] H. Pota, S. O. R. Moheimani, and M. Smith, "Resonant controllers
for smart structures," *Smart Materials and Structures*, vol. 11, no. 1,
p. 1, 2002.
[6] B. Brogliato, R. Lozano, B. Maschke, and O. Egeland, Dissipative
systems analysis and control: theory and applications.
Springer,
London, 2007, vol. 2.
[7] K. Shi, I. R. Petersen, and I. G. Vladimirov, "Necessary and sufficient
conditions for state feedback equivalence to negative imaginary systems," *IEEE Transactions on Automatic Control (Early Acess)*, 2024.
[8] A. Lanzon and H.-J. Chen, "Feedback stability of negative imaginary
systems," *IEEE Transactions on Automatic Control*, vol. 62, no. 11,
pp. 5620–5633, 2017.
[9] M. A. Mabrok, A. G. Kallapur, I. R. Petersen, and A. Lanzon, "Spectral conditions for negative imaginary systems with applications to
nanopositioning," *IEEE/ASME Transactions on Mechatronics*, vol. 19,
no. 3, pp. 895–903, 2013.
[10] S. K. Das, H. R. Pota, and I. R. Petersen, "A MIMO double resonant controller design for nanopositioners," IEEE Transactions on Nanotechnology, vol. 14, no. 2, pp. 224–237, 2014.
[11] ——, "Resonant controller design for a piezoelectric tube scanner: A
mixed negative-imaginary and small-gain approach," IEEE Transactions on Control Systems Technology, vol. 22, no. 5, pp. 1899–1906,
2014.
[12] ——, "Multivariable negative-imaginary controller design for damping and cross coupling reduction of nanopositioners: a reference
model matching approach," IEEE/ASME Transactions on Mechatronics, vol. 20, no. 6, pp. 3123–3134, 2015.
[13] C. Cai and G. Hagen, "Stability analysis for a string of coupled
stable subsystems with negative imaginary frequency response," IEEE
Transactions on Automatic Control, vol. 55, no. 8, pp. 1958–1963,
2010.
[14] M. A. Rahman, A. Al Mamun, K. Yao, and S. K. Das, "Design
and implementation of feedback resonance compensator in hard disk
drive servo system: A mixed passivity, negative-imaginary and smallgain approach in discrete time," Journal of Control, Automation and
Electrical Systems, vol. 26, no. 4, pp. 390–402, 2015.
[15] B. Bhikkaji, S. O. R. Moheimani, and I. R. Petersen, "A negative
imaginary approach to modeling and control of a collocated structure,"
IEEE/ASME Transactions on Mechatronics, vol. 17, no. 4, pp. 717–
727, 2011.
[16] Y. Chen, K. Shi, I. R. Petersen, and E. L. Ratnam, "A nonlinear
negative imaginary systems framework with actuator saturation for
control of electrical power systems," To appear in 2024 European
Control Conference, 2023.
[17] A. G. Ghallab, M. A. Mabrok, and I. R. Petersen, "Extending negative imaginary systems theory to nonlinear systems," in 2018 IEEE Conference on Decision and Control (CDC).
IEEE, 2018, pp. 2348–
2353.
[18] K. Shi, I. G. Vladimirov, and I. R. Petersen, "Robust output feedback consensus for networked identical nonlinear negative-imaginary
systems," *IFAC-PapersOnLine*, vol. 54, no. 9, pp. 239–244, 2021.
[19] K. Shi, I. R. Petersen, and I. G. Vladimirov, "Output feedback
consensus for networked heterogeneous nonlinear negative-imaginary
systems with free-body motion," IEEE Transactions on Automatic
Control, vol. 68, no. 9, pp. 5536–5543, 2023.
[20] D. A. Deenen, M. F. Heertjes, W. Heemels, and H. Nijmeijer, "Hybrid
integrator design for enhanced tracking in motion control," in 2017
American Control Conference (ACC).
IEEE, 2017, pp. 2863–2868.
[21] R. H. Middleton, "Trade-offs in linear control system design," Automatica, vol. 27, no. 2, pp. 281–292, 1991.
[22] S. Van den Eijnden, M. F. Heertjes, W. Heemels, and H. Nijmeijer,
"Hybrid integrator-gain systems: A remedy for overshoot limitations
in linear control?" *IEEE Control Systems Letters*, vol. 4, no. 4, pp.
1042–1047, 2020.
[23] D. Van Dinther, B. Sharif, S. Van den Eijnden, H. Nijmeijer,
M. F. Heertjes, and W. Heemels, "Overcoming performance limitations of linear control with hybrid integrator-gain systems," IFAC- PapersOnLine, vol. 54, no. 5, pp. 289–294, 2021.
[24] M. Heertjes, S. van Den Eijnden, and B. Sharif, "An overview on
hybrid integrator-gain systems with applications to wafer scanners," in
2023 IEEE International Conference on Mechatronics (ICM).
IEEE,
2023, pp. 1–8.
[25] D. A. Deenen, B. Sharif, S. van den Eijnden, H. Nijmeijer,
M. Heemels, and M. Heertjes, "Projection-based integrators for improved motion control: Formalization, well-posedness and stability
of hybrid integrator-gain systems," *Automatica*, vol. 133, p. 109830,
2021.
[26] S. van den Eijnden, M. Heertjes, H. Nijmeijer, and W. Heemels, "A
small-gain approach to incremental input-to-state stability analysis of
hybrid integrator-gain systems," *IEEE Control Systems Letters*, 2023.
[27] K. Shi, N. Nikooienejad, I. R. Petersen, and S. O. R. Moheimani, "A
negative imaginary approach to hybrid integrator-gain system control,"
in *2022 IEEE 61st Conference on Decision and Control (CDC)*. IEEE,
2022, pp. 1968–1973.
[28] ——, "Negative imaginary control using hybrid integrator-gain systems: Application to MEMS nanopositioner," IEEE Transactions on Control Systems Technology (Early Access), 2023.
[29] K. Shi and I. R. Petersen, "Digital control of negative imaginary
systems: a discrete-time hybrid integrator-gain system approach," To
appear in 2024 European Control Conference, 2024.
[30] S. S. Aphale, A. J. Fleming, and S. O. R. Moheimani, "Integral
resonant control of collocated smart structures," Smart materials and structures, vol. 16, no. 2, p. 439, 2007.
[31] B. Bhikkaji, S. O. R. Moheimani, and I. R. Petersen, "Multivariable
integral control of resonant structures," in 2008 47th IEEE Conference on Decision and Control.
IEEE, 2008, pp. 3743–3748.
[32] Y. Yue and Z. Song, "An integral resonant control scheme for a laser
beam stabilization system," in 2015 IEEE International Conference on Information and Automation.
IEEE, 2015, pp. 2221–2226.
[33] B. Bhikkaji and S. O. R. Moheimani, "Integral resonant control of a
piezoelectric tube actuator for fast nanoscale positioning," IEEE/ASME
Transactions on mechatronics, vol. 13, no. 5, pp. 530–537, 2008.
[34] D. Russell and S. S. Aphale, "Evaluating the performance of robust
controllers for a nanopositioning platform under loading." IFAC-
PapersOnLine, vol. 50, no. 1, pp. 10 895–10 900, 2017.
[35] J. Xiong, I. R. Petersen, and A. Lanzon, "A negative imaginary lemma
and the stability of interconnections of linear negative imaginary
systems," *IEEE Transactions on Automatic Control*, vol. 55, no. 10,
pp. 2342–2347, 2010.
[36] A. S. P., "HIGS-based skyhook damping design of a multivariable
vibration isolation system," Master's thesis, Eindhoven University of
Technology, 2020.