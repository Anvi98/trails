# Control Designs For Critical-Continegency Responsible Grid-Following Inverters And Seamless Transitions To And From Grid-Forming Modes

Jaesang Park1,a, Alireza Askarian1,b, and Srinivasa Salapaka1,c

  Abstract— This article introduces two control frameworks:
one for Grid-Following (GFL) inverters aiding Grid-Forming
(GFM) inverters in voltage regulation during large contingency
events and optimizing power transactions under normal con-
ditions; and another for seamless transitions between grid-tied
and grid-isolated setups, managing voltage transient charac-
teristics. In microgrids, GFM inverters regulate voltage, while
GFL inverters handle power transactions. The proposed GFL
control detects abrupt load/generation changes, adjusting power
transactions using local storage to support GFM inverters
during contingencies. Additionally, a transition control ensures
smooth GFL-GFM shifts, reducing power and voltage fluctua-
tions. Simulation results validate improved voltage regulation
during contingencies and enhanced power tracking during slow
changes, alongside minimized transient overshoot.

## I. Introduction

With increasing concern for climate change, global efforts have been made in recent years to reduce carbon emissions. To mitigate the pollution from fossil-based power generation and achieve lower carbon emissions, renewable energy sources (RES) such as solar, wind, and hydro are being integrated on a large scale into the power network. These RES, often supplemented with energy storage devices like batteries, are connected to the grid through DC/AC inverters. Currently, most inverters operate in grid-following (GFL) mode, where the grid controls voltage and frequency while the inverter supplies power. However, achieving high RES penetration with GFL inverters poses challenges.

In microgrids, especially when grid-isolated, sudden large power events like load or generational changes can strain voltage regulation, resulting in significant deviations from nominal values. Similar deviations happen in grid-tied setups due to factors such as weather disturbances and uncertainties in power production, which worsen with high penetration of RES. Conventional GFL-based inverter control designs lack robustness against these deviations, leaving grid viability solely on Grid-Forming (GFM) inverters. However, if GFM inverters are overwhelmed by sudden changes, cascading failures may lead to grid instability.

One explored approach [1] is Frequency-Watt (FW) control. Here, the inverter maintains a desired power set-point within a specific frequency range. However, if the frequency exceeds this range, the inverter follows a droop curve instead of the precise set-point. While this method enhances grid stability, it struggles in weak microgrids where frequency
1
Department of Mechanical Science and Engineering, University of Illinois at Urbana-Champaign,
61801
IL, USA
ajaesang4@illinois.edu,baskaria2@illinois.edu,csalapaka@illinois.edu control is lax, resulting in erratic power injection. Moreover, when the frequency drops below the nominal value, continuous power injection attempted by the inverter control design may not be sustainable over long intervals, posing operational challenges. In contrast, [2] introduces virtual inertia, simulating synchronous machine dynamics, where the energy stored in DC link capacitors to mechanical inertia in synchronous machines, aiming to emulate traditional power generation behaviors that enhance grid stability. While it excels in steady-state active power tracking and frequency support, it mainly focuses on the active power-to-frequency response, neglecting dynamics of reactive power and voltage.

Relevant studies, such as those by [3] and [4], explore control strategies transitioning GFL and GFM modes. Here inverter control is changed from GFL to GFM based on amplitude/frequency deviations from nominal values. While suitable for grid-tied operations with occasional deviations, in weaker microgrids, operating all inverters in GFM mode might not be efficient. Our proposed control design enables inverters to switch to GFM-like voltage regulation only during rapid load or generation changes, operating as GFL inverters during gradual changes. This assists full-time GFM inverters during extreme power fluctuations while providing commanded power, like maximum power point tracking, during stable periods.

We make use of algebraic structures in our control design to enable transitions between GFL and GFM modes; thus facilitating smooth transitions of microgrids between gridtied and grid-isolated states. In the event of a main power grid anomaly, RES can disconnect and form a microgrid, preventing a complete blackout. Our transition capability ensures the grid-isolated microgrid includes a GFM inverter for regulating frequency and voltage, while allowing other GFL inverters to connect, ensuring the presence of a GFM inverter within the newly formed microgrid consistently. The proposed control retains the functional advantages and stability aspects of the control strategies developed in [4]. The main distinctive feature is that our control design enables smooth transitions while *ensuring* safe transient voltage characteristics. In contrast, the strategy in [4] does not guarantee transient characteristics during transitions. For instance, their methods may introduce sudden jumps in the controller output when switching modes, potentially causing grid instability. Using the proposed GFL inverter, we demonstrate about 44% reduction in the Rate of Change of Frequency (RoCof) during sudden load changes compared to using a conventional GFL inverter. Additionally, with the proposed smooth transition algorithm, during the transition from GFL to GFM, we demonstrate that we can achieve only 1% of overshoot in active power compared to the sudden transition and no overshoot in reactive power.

## Ii. Overview Of The Conventional Gfl And Gfm Inverter A. Modeling Of Inverter Connected To A Grid

A
DC
source power (e.g., RES) is transacted with an AC power grid using an inverter. An inverter with an LC filter connected to a grid can be modeled as in Fig. 1. It converts DC
to AC using fast switching of transistors. A power converter (not shown here) takes power from the source and maintains a constant voltage Vdc at its output. The control design on the converter achieves voltage regulation by using capacitance or battery storage on the DC side. The inverter's switchaveraged model, depicted in Fig. 1, uses the modulating signal m ∈ [−1, 1] as a control parameter. This signal is actuated using pulse-width modulated (PWM) signals, which determine duty cycles governing the switching. The averaged model resembles a controlled voltage source with output voltage m Vdc
2 . However, to suppress high-frequency switching noise, an LC filter with resistance Ri, inductance Li, and capacitance Ci is employed. This filter mitigates noise in the filter current iL and the capacitor voltage Vc, which serves as the inverter's output voltage interfacing with the grid. The grid, represented as a voltage source with voltage Vg, is separated from the inverter by line impedance, modeled by line resistance Rg and inductance Lg. The output current ig from the inverter is the power transacted with the grid.

## B. Response Of Conventional Gfl To Perturbation

The main goal of a GFL is to control its output power.

Since the output power depends on the output current ig and the capacitor voltage Vc, where Vc can be measured, its goal is converted to a controlling output current ig.

Note that typically the control signal m is designed to make the inductor current iL track iL,ref, where the reference iL,ref is appropriately designed to make ig track ig,ref. In direct-quadrature (dq) coordinates, the dynamics between iL
and ig is given by the capacitor dynamics as follows [5]

$$\hat{i}_{g}^{d,q}=\hat{i}_{L}^{d,q}-C_{i}\hat{V}_{c}^{d,q}s\pm C_{i}\omega\hat{V}_{c}^{q,d}\tag{1}$$

where superscript $d$ and $q$ respectively represent the direct and quadrature components, while the hat notation denotes the s-domain signal. Additionally, $\omega$ denotes the grid voltage frequency.

Here by choosing $\hat{i}_{L,ref}^{d,q}=\hat{i}_{g,ref}^{d,q}\mp C\omega\hat{V}_{c}^{q,q}$ and designing the filter current controller with a large bandwidth, the 

coupling terms CωV d
                   c
                      and CωV q
                               c
                                  cancel out and ˆid,q
                                                  L
                                                     ≈
ˆid,q
L,ref resulting in the following dynamics given by

$$\hat{V}_{c}^{d,q}=\frac{1}{C_{i}s}(\hat{i}_{g,ref}^{d,q}-\hat{i}_{g}^{d,q})\tag{2}$$
In addition to this, the frequency of the GFL control is determined by the PLL, which takes V q c as an input:

ˆω = K*P LL*(s) 1 Cis(ˆiq g,ref −ˆiq g) + ˆω0. (3)

In this paper, we use subscript 0 to denote nominal values
and superscript − to represent amplitude of the underlying
signals. Note that by assuming that the PLL accurately
estimates the phase of the capacitance voltage, one can easily
deduce from d-q transformations that V d
                                      c ≈ ¯Vc and V q
                                                    c ≈ 0.
Also, it is easy to show that P =
                                      3
                                      2(V d
                                         c id
                                            g + V q
                                                  c iq
                                                    g) and
Q =
      3
      2(−V d
            c iq
              g + V d
                    c iq
                       g), id
                           g and iq
                                   g can be approximated
as id
   g =
          2

3V0 , id
      g,ref =
                2

3V0 P0, iq
        g = − 2

                                         3V0 Q, and iq
                                                     g,ref =
− 2

3V0 Q0. See [5] for these d-q transformation details.
From (2) and (3), we obtain

$$\hat{V}_{c}=\frac{2}{3V_{0}C_{i}s}(\hat{P}_{0}-\hat{P}),\quad\hat{\omega}=\hat{\omega}_{0}-\frac{2K_{PLL}(s)}{3V_{0}C_{i}s}(\hat{Q}_{0}-\hat{Q}).\tag{4}$$
Since the PI controller is widely used for K*P LL*(s), without loss of generality, both equations in (4) include at least one pure integrator. Therefore, they have infinite DC gain. Consequently, if there is a mismatch between the nominal output power and the actual output power, the GFL inverter cannot regulate voltage and frequency.

In addition, in (4), the nominal voltage V0 is a grid parameter that we cannot change. Moreover, Ci is chosen to be small, just enough to reject the switching noise of a transistor, to minimize the effect of Vc on ig. This makes the bandwidth of
2
3V0Cis large. Therefore, a high-frequency disturbance in output power propagates to the inverter voltage and frequency, potentially leading to grid instability.

Some literature, like [6], proposes a GFL design that considers the bandwidth between active/reactive power and voltage/frequency. However, in most conventional designs, as mentioned earlier, this bandwidth is not adequately considered. Typically, only the bandwidth of the current controller and PLL are taken into account. Consequently, the bandwidth of (4) unintentionally becomes large, as noted.

## C. Response Of Gfm To Perturbation

Unlike GFL, the goal of GFM is to control the output voltage Vc. The corresponding control designs typically accommodate uncertainties in power generation and consumption, which translate into mismatches between the commanded and actual power transactions. Since physically it is impossible to accommodate these power mismatches without compromising the voltage (amplitude and frequency) regulation, the control laws allow the amplitude and frequency to *droop* or deviate from the nominal values; however, in a controlled manner.

There are several types of droop control strategies depending on the types of output line impedance. However, even though the line impedance could vary in type, in most cases, it is inductive due to the presence of long transmission lines. Therefore, for simplicity, we assume a purely inductive line, and its droop strategy becomes the Pf − QV type of droop
[7], expressed as:

$$\hat{\omega}=\hat{\omega}_{0}+K_{P}(\hat{P}_{0}-\hat{P}),\quad\hat{V}_{ref}=\hat{V}_{0}+K_{Q}(\hat{Q}_{0}-\hat{Q}).\tag{5}$$

Here, $K_{P}(s)=k_{p}\frac{\omega_{1pf}}{s+\omega_{1pf}}$, $K_{Q}(s)=k_{q}\frac{\omega_{1pf}}{s+\omega_{1f}}$

$\hat{\omega}_{1}$\(\hat{\omega}_{1}

s+ωlpf , and kp and kq are the slope of the curve, while
ωlpf s+ωlpf is a low pass filter for power calculation.

Both dynamics given in (5) have a finite dc-gain as they have no pole at the origin. Furthermore, kp, kq, and
ωlpf are design parameters, and by changing them, we can make the frequency and voltage insensitive to high-frequency disturbances of the output power. Therefore, even if there is a mismatch in nominal and actual output power, they can regulate the frequency and the magnitude of the voltage.

Therefore, when there are GFM inverters and conventional GFL inverters in the grid, when there is a disturbance of power, conventional GFL inverters do not contribute to voltage stability, and only GFM inverters respond to power mismatches and ensure a corresponding modified setpoint. However, in a network that has many GFL inverters, substantial and sudden power mismatches can overwhelm GFM inverters, thus compromising network stability. This motivates control designs where GFL inverters are more responsive to power uncertainties.

Remark: The power-grid network robustness discussed above is also referred to as inertia in some existing literature such as [2] and [8], where intuition is developed by developing analogies with a synchronous generator used in well-studied power plants. Here, we establish this connection in the context of our analysis. In a synchronous machine, the mechanical rotor acts as an energy storage device, the energy stored in the rotor being given by E = 1
2Jω2, where J is the rotor moment of inertia, and ω is the rotating speed. Therefore, the rotor provides a mechanical means of absorbing or providing instantaneous power and prevents sudden changes in the rotating frequency of a synchronous machine. The swing equation and governor equations in (6) capture the dynamical behavior of the rotor frequency

$$J\frac{d\omega}{dt}=T_{in}-T_{out}-D\omega,\quad T_{in}=T_{0}+k_{\omega}(\omega_{0}-\omega),\tag{6}$$
where Tin is input torque comes from the governor, Tout is torque output due to electricity generation, and T0 is nominal torque. Furthermore, D represents the damping of the rotor and kω is the governor droop coefficient. Using the approximation P0 = T0ω0 and P = Toutω0, where P and P0 are, respectively, the actual and nominal output power.

Combining (6) together, as shown in [8], the dynamics of a synchronous generator can be expressed as

$$\hat{\omega}=\hat{\omega}_{0}+\frac{1/H}{s+(k_{\omega}+D)/H}(\hat{P}_{0}-\hat{P}),\tag{7}$$
where H = *J/ω*0. As shown in [9], by defining ωlpf =
(kω + D)/J and kp = 1/(kω + D), we can recover the first equation of (5). Also, as the mechanical inertia J
increases, the dynamics are less sensitive to changes in power. Therefore, inertia has an equivalent meaning in this context.

## Iii. Proposed Gfl Controller

We propose a control design in which the inverter responds to sudden and fast changes in power mismatches while being insensitive to slow changes. Here, we use our observations from the GFM droop-control design in the previous section, where we propose appropriately designing filters in the droop-control design to enable controllers that are sensitive to time constants of the load/generation perturbations. To be more specific, we will design controllers that mimic conventional GFL designs at low frequencies while mimicking the dynamics of (5) at frequencies higher than its cut-off frequency ωlpf.

## A. Power-Injecting Dynamics

The primary objective of GFL inverter is to control its output power. Designing such a controller using a droopcontrol structure requires analyzing the power-injecting dynamics. The droop equation relates output voltage amplitude and frequency to nominal and actual active/reactive power. However, these voltages and frequencies also impact active/reactive power. Illustrated in [10], this voltagefrequency-to-power relationship forms a feedback loop. Analyzing closed-loop power injection dynamics necessitates understanding power transaction dynamics. This relationship is given in the context of Fig 1, where the power transactions (P and Q) between the inverter output (specified by the output of the capacitor) and the point of coupling at the grid are given by P + jQ = ¯Vcejθc� ¯
Vcejθc− ¯
Vgejθg

                                                 ¯
                                                 Zgejϕ
                                                          �∗,
where ¯
       Zgejϕ = Rg + jω0Lg represents the line impedance.
Assuming a long transmission line, we have ϕ ≈ 90◦. By
linearizing this equation around θc − θg = 0 and ¯Vg = V0,

we obtain
         �P
           Q

�
 =
    V0
    ¯
    Zg

�0
   1
 1
   0

� � ¯Vc − ¯Vg
     V0δ

�
 . In what follows,

we assume that we have a voltage controller with a large
bandwidth and therefore ˆVc = ˆVc,ref. Now we relate ω to
δ by δ =
          � t
           0(ω − ω0)ds −
                          � t
                           0(ωg − ω0)dτ. By combining
(5) and using these relations, we derive the block diagram
of closed-loop power injecting dynamics as shown in Fig. 2.
Here, ˆd = [ ˆ¯Vg − ˆ¯V0, ˆωg − ˆω0]T and ˆp = [ ˆP, ˆQ]T respectively
represent amplitude and frequency deviations, and actual
active and reactive power components.

Since the dynamics from ˆP0 to ˆP and the dynamics from
ˆQ0 to ˆQ are decoupled, they can be expressed as two Single-
Input Single-Output (SISO) systems as

$$\hat{P}=\frac{V_{0}^{2}K_{P}}{s\bar{Z}_{g}+V_{0}^{2}K_{P}}\hat{P}_{0}+\frac{V_{0}^{2}}{s\bar{Z}_{g}+V_{0}^{2}K_{P}}(\hat{\omega}_{g}-\hat{\omega}_{0}),\tag{8}$$ $$\hat{Q}=\frac{V_{0}K_{Q}}{\bar{Z}_{g}+V_{0}K_{Q}}\hat{Q}_{0}+\frac{V_{0}}{\bar{Z}_{g}+V_{0}K_{Q}}(\hat{V}_{g}-\hat{V}_{0}).\tag{9}$$

## B. Design Of The Controller

s + ϵP s + ϵQ s + ωlpf � . (10)

  For our control design, we consider the following criteria
  1) Reference tracking: First, as discussed in the previous
section, the goal of the GFL inverter is power tracking. At the
very least, this should achieve steady-state power tracking.
In frequency domain, it is is equivalent to
                                             ˆp(j0)
                                             ˆp0(j0) ≈ I and
ˆp(j0)
d(j0) ≈ 0. To achieve this, we propose the following control
structure for [KP , KQ] =:
 ��
   kp,P +
             ki,P

� , � kp,Q + ki,Q �� � ωlpf

Note that setting ϵP = ϵQ = 0 achieves
                                            h(j0)
                                           h0(j0) = I and
h(j0)
d(j0) = 0. Additionally, by choosing ϵP , ϵQ > 0, one
can introduce robustness as a trade-off between performance.
Finally, ϵP and ϵQ will be used in transition between GFL
and GFM, a topic we will discuss later.
  2) Stability: With the controller given in (10), the losed-
loop characteristic polynomial for the system in (8) is s3 +
(ωlpf +ϵP )s2+(ωlpfϵP + V 2
                           0

Zg ωlpfkp,P )s+ V 2
             0

                                Zg ωlpf(kp,P ϵP +
ki,P ). Then, from the Routh-Hurwitz stability criterion if
ωlpf −ki,P /kp,P > 0, it is stable. Also, for the second-order
system in (9), since all the coefficients are positive, it stable
for any kp,Q, ki,Q > 0.
 3) Robustness against a high-frequency perturbation:
Finally, among the controllers that meet the reference track-
ing and stability conditions mentioned above, our objective
is to find the controller that mimics the response in (5)
for ω > ωlpf. With small ϵP , ϵQ, this can be achieved
by setting ki,P = kp and ki,Q = kq while ensuring that
ki,P /kp,P ≤ ωlpf and ki,Q/kp,Q ≤ ωlpf.

## Iv. Smooth Transition Between Gfl And Gfm

Now we consider the implementation of control schemes that achieve transitions from GFL to GFM modes or vice versa, as desired. These transitions may be motivated by various reasons - for instance, decisions to go from grid-tied to grid-isolated modes. It turns out that we can achieve this by modifying parameters ϵP and ϵQ of our control design in (10). Specifically, when ϵP *, ϵ*Q small, we obtain the GFL controller as previously designed. Conversely, selecting
ϵP = ϵQ = ϵmax for some large ϵmax mimics a GFM defined in (5), as it derives ki,P
s+ϵP ≈ 0 and ki,Q
s+ϵQ ≈ 0.

## A. Proposed Transition Strategy

1) GFL to GFM: The transition from GFL to GFM proposed in [4] is equivalent to change ϵP and ϵQ in (10) from
0 to ∞ abruptly. However, this abrupt change introduces a sudden variation in the control signal, potentially causing high-frequency perturbations in the grid and leading to grid instability. To mitigate this issue, we propose a smooth transition method that gradually ramps up ϵP and ϵQ from
0 to ϵmax.

2) GFM to GFL: On the other hand, when switching from GFM to GFL, even if we suddenly make ϵ to 0, the control signal does not experience abrupt changes. Therefore, to facilitate the transition from GFM to GFL, we use a jump from ϵmax to 0.

## B. Transition Stability

  First consider the transition stability of active power
dynamics during the transition. As shown in the previ-
ous section, if a controller satisfies the stability conditions
mentioned above, the system in (8) is stable for each
ϵP ∈ [0, ϵmax]. However, when ϵP varies, it becomes non-
autonomous system and the stability of each time instance
is not sufficient to guarantee overall stability.
  Now, let AP (ϵP ) be the state matrix of a state space model
of (8) corresponding to a given ϵP . Given that the system
is stable for each ϵP , AP (ϵP ) is Hurwitz. Next, consider
a solution to the Lyapunov equation A⊤
                                        P (ϵP )WP (ϵP ) +
WP (ϵP )AP (ϵP ) = −I. Since AP (ϵP ) is Hurwitz for each
ϵP ∈ [0, ϵmax], the eigenvalues of WP (ϵP ) are all strictly
positive. Finally, let VP (t) = x⊤
                             P (t)WP (ϵP (t))xP (t), where
xP is a state variable, be a Lyapunov candidate.
  If there exists a finite α > 0 such that VP (t) ≤ αVP (0),
then by Rayleigh Ritz theorem,

$$\|x_{P}(t)\|_{2}^{2}\leq\alpha\frac{\max_{\epsilon_{P}\in[0,\epsilon_{max}]}\bar{\lambda}(W_{P}(\epsilon_{P}))}{\min_{\epsilon_{P}\in[0,\epsilon_{max}]}\bar{\lambda}(W_{P}(\epsilon_{P}))}\|x_{P}(0)\|_{2}^{2}.\tag{11}$$

Since the eigenvalues of WP (ϵ) are strictly positive and
[0, ϵmax] is a closed interval, minϵP ∈[0,ϵmax] λ(WP (ϵP )) >
0, and the upper bound is finite. Therefore, for any ϵ > 0,
there exists δ > 0 such that if ∥x0∥ ≤ δ, ∥x(t)∥ ≤ ϵ and
therefore, the system is stable.

Proposition 1. There exists a finite α > 0 during the
transition.

  Proof 1. By taking the derivative of the Lyapunov candi-
date function and applying Rayleigh Ritz theorem, we obtain

˙VP (t) ≤ ¯λ( ˙WP (ϵP (t)) − I)∥xP (t)∥2
                                                     2 ≤ q(t)VP (t), where

|¯λ( ˙WP (ϵP (t)))|

q(t) =

minϵP ∈[0,ϵmax] λ(WP )
                      if ˙ϵP ̸= 0

−
      1

$$\left\{\begin{array}{l}{{}}\\ {{}}\end{array}\right.$$

maxϵP ∈[0,ϵmax] ¯λ(WP )
                  if ˙ϵP = 0

Note that during the transition $\dot{\epsilon}_{P}\neq0$, and $\bar{\lambda}(\dot{W}_{P}(\epsilon_{P}(t))-I)=\bar{\lambda}(\dot{W}_{P}(\epsilon_{P}(t)))-1\leq|\bar{\lambda}(\dot{W}_{P}(\epsilon_{P}(t)))|$. Conversely, when remaining in one mode, $\dot{\epsilon}_{P}=0$ and $\dot{W}_{P}(t)=0$ as $\dot{W}_{P}=\frac{\partial W_{P}}{\partial\epsilon_{P}}\dot{\epsilon}_{P}$. Then, $\bar{\lambda}(\dot{W}_{P}(\epsilon_{P}(t))-I)=-1$

By applying Gronwall-Bellman inequality, we obtain $V_{P}(t)\leq V_{P}(0)exp\big{(}\int_{0}^{t}q(\tau)d\tau\big{)}$, and it is bounded since

$$\int_{0}^{t}q(\tau)d\tau\leq\frac{\max_{\epsilon_{P}\in[0,\epsilon_{max}]}\|\partial W_{P}(\epsilon_{P})/\partial\epsilon_{P}\|}{\min_{\epsilon_{P}\in[0,\epsilon_{max}]}\underline{\lambda}(W_{P})}\int_{0}^{t}|\dot{\epsilon}_{P}(t)|d\tau$$ $$\leq\frac{\max_{\epsilon_{P}\in[0,\epsilon_{max}]}\|\partial W_{P}(\epsilon_{P})/\partial\epsilon_{P}\|}{\min_{\epsilon_{P}\in[0,\epsilon_{max}]}\underline{\lambda}(W_{P})}\epsilon_{max},$$
where we choose (and assume) a transition strategy where
ϵP changes monotonically with time.

## ∂Εp Proposition 2. Maxϵp ∈[0,Εmax] ��� ∂Wp (Εp )

��� is finite.

Proof 2. Since the coefficients of the characteristic polynomial (8) are affine with respect to ϵP ; therefore AP (ϵ) is also affine; that is AP (ϵP ) = AP (0) + ϵP BP for some BP .

Also
∂

0
   τ
     ���eA⊤
         P (ϵP )τeAP (ϵP )τ��� dτ,

���� ≤ 2∥BP ∥
                                   � ∞

Also $\frac{\partial}{\partial\epsilon_{P}}e^{A_{P}(\epsilon_{P})\tau}=B_{P}\tau e^{A_{P}(\epsilon_{P})\tau}$.

If we choose $\epsilon_{P}(t)$ to be a smooth function of $t$, and using $W_{P}=\left(e^{A_{P}^{\top}(\epsilon_{P})\tau}e^{A_{P}(\epsilon_{P})\tau}\right)$, we get

$$\left\|\frac{\partial W_{P}}{\partial\epsilon_{P}}\right\|\leq2\|B_{P}\|\int_{0}^{\infty}\tau\left\|e^{A_{P}^{\top}(\epsilon_{P})\tau}e^{A_{P}(\epsilon_{P})\tau}\right\|\,d\tau,$$

where since $A_{P}(\epsilon_{P})$ is Hurwitz, $\|e^{A_{P}^{\top}(\epsilon_{P})\tau}e^{A_{P}(\epsilon_{P})\tau}\|\leq\epsilon_{P}\tau$, $\epsilon_{P}$ is a smooth function of $\epsilon_{P}$.

where since AP (ϵP ) is Hurwitz, ∥eA⊤
                                   P (ϵP )τeAP (ϵP )τ∥ ≤
e−λP τ for some λP > 0. As a result, it is bounded for each
ϵP . Furthermore, since [0, ϵmax] is a closed and bounded
interval, maxϵP ∈[0,ϵmax] ∥∂WP /∂ϵP ∥ is bounded.
  For multiple transitions, if there is a time gap of at least
maxϵP ∈[0,ϵmax] ¯λ(WP )
                    maxϵP ∈[0,ϵmax] ∥∂WP (ϵP )/∂ϵP ∥

                             minϵP λ(WP )
                                                ϵmax
between the end of one transition and the start of new
transition, it ensures that VP (T) < VP (0) where T is
the time when the new transition start. Then, the same
upper bound for V (t) can be applied to the new transition,
ensuring stability.
  Similar procedures can be followed for analyzing the
transition stability of reactive power dynamics.

## V. Simulation Results

Implementation: We designed the droop controller for the proposed GFL inverter under the assumption that we have a voltage controller with a large bandwidth. To design such a controller, let us first consider the dynamics of the LC filter of the inverter in Fig. 1. In dq coordinates, the dynamics of the LC filter are given as follows:

$$L_{i}\frac{di_{L}^{d,q}}{dt}=m^{d,q}\frac{V_{dc}}{2}\pm L_{i}\omega i_{L}^{q,d}-V_{c}^{d,q}-R_{i}i_{L}^{d,q}\tag{12}$$

Based on [5], with the current controller $K_{c}$ and feedback linearizing control that cancels out the $d$ and $q$ coupling terms, the control input can be represented as follows

$$\hat{m}^{d,q}=\frac{K_{c}(\hat{i}_{L,ref}^{d,q}-\hat{i}_{L}^{d,q})\mp L_{i}\omega_{0}^{2q,q}+\hat{V}_{c}^{d,q}}{V_{dc}/2}.\tag{13}$$

Then, ˆid,q
      L
          = Tcˆid,q
                L,ref where Tc =
                                    KcGi

                             1+KcGi and Gi =
1

Lis+Ri . On top of the current control in (13), by choosing
iL,ref as

$$\hat{i}^{d,q}_{L,ref}=K_{v}(\hat{V}^{d,q}_{c,ref}-\hat{V}^{d,q}_{c})\mp C_{i}\omega_{0}\hat{V}^{q,d}_{c}+\hat{i}^{d,q}_{g},\tag{14}$$

one can achieve $\hat{V}^{d,q}_{c}=T_{v}\hat{V}^{d,q}_{c,ref}$, where $T_{v}=\frac{K_{v}T_{c}G_{v}}{1+K_{v}T_{c}G}$

                                        1+KvT cGv
and Gv =
         1

       Cis.
 In this experiment, controllers with the following structure
are utilized:

$$K_{c}=\frac{L_{i}s+R_{i}}{\tau_{c}s},\quad K_{v}=k_{p,V}+\frac{k_{i,V}}{s},\tag{15}$$
where parameters τc, kp,V , and ki,V are tuned to have enough bandwidth. Also, the conventional GFL that is used for comparison is using the same Kc.

The proposed controller and the conventional GFL were implemented and tested using the MATLAB Simscape toolbox with a step size of 0.05 s. The grid and inverter parameters used in the simulations are as follows: Ri = 0.2Ω, Li = 3.3mH, Ci = 40µF, Rg = 0.1Ω, Lg = 1.86mH.

Additionally, the nominal voltage and frequency are set to V0 = 391V and f0 = 60Hz. The chosen controller parameters are kp,P = 0.2, rad/(s · kW), ki,P = 0.1ωlpf · kp,P , kp,Q = 0.2 V/kVAR, and ki,Q = ωlpf · kp,Q.

(a) Power Tracking: First, we evaluate the active and reactive power tracking of the proposed controller with filter cutoff frequencies (ωlpf) set to 4π rad/s, 5π rad/s, and
20π rad/s. We assume that the inverter with the proposed controller is connected to a stiff grid with ωg = ω0 and Vg =
V0. As shown in Fig.3, at t = 1 second, the active power reference is changed from 10kW to 12kW, and at t = 4 second, the reactive power set point is changed from 0kVAR to 2kVAR. Similarly, at t = 7 seconds, the active power P0 changes from 12kW to 8kW, and at t = 10 seconds, the reactive power Q0 changes from 2kVAR to -1kVAR.

The proposed controller achieves steady-state tracking just as conventional GFL.

(b) Response to Fast and Slow Load Changes: For checking the frequency and voltage support of the proposed GFL, consider the case where the GFL inverter is connected to the GFM inverter, forming a weak microgrid. Initially, there is a 20kW active load and a 10kVAR reactive load, and the GFL inverter injects 10kW of active power. Throughout this scenario, P0 = 10kW and Q0 = 0*V AR*. At t = 1s,
5kW of active load and 5kVAR of reactive load are added to the grid. Then, the response is given as Fig.4
For conventional GFL, active and reactive output power converge to the reference value immediately. Then, a GFM inverter solely handles load changes and experiences a huge rate of change of frequency (RoCoF). However, with the proposed controller, in the event of a load change, the GFL inverter temporarily supplies power, resulting in smaller voltage and frequency peaks and reduced RoCoF until the grid reaches new steady-state values. When conventional GFL shows a RoCoF of 1.74 Hz/s, the proposed controllers with
ωlpf of 4π, 10π, and 20π achieve 0.89 Hz/s, 0.93 Hz/s, and
0.98 Hz/s, respectively, which represent 51.35%, 53.30%, and 56.00% of the RoCoF compared to the conventional GFL
case. Additionally, the proposed GFL controller provides damping on the voltage.

Also, to verify that the proposed controller follows the power reference point and does not react to a slow load change, we apply 5 kW and 5 kVAR of active and reactive load changes over 5 seconds in a ramp manner to a microgrid with one GFM inverter and a proposed GFL inverter with
ωlpf = 20π rad/s. As seen in Fig. 5, when the load changes slowly, most of the load change is handled by the GFM inverter, and the GFL inverter with the proposed controller maintains its power reference point.

Fig. 5: Power sharing between GFM and proposed GFL under slow load change: Blue represents the proposed GFL, Red represents GFM, and Orange represents the total load.

(c) Transition between GFM and GFL: In the same microgrid setup with a GFL inverter utilizing the proposed controller (ωlpf = 20π rad/s) and a GFM inverter, a transition between GFL and GFM is tested (Fig. 6). Initially, the proposed controller is in GFL mode. At t = 2 s, the GFL inverter transitions to GFM mode. Parameters ˙ϵ = 100
and ϵmax = 200 are chosen for smooth transition. For comparison, a sudden transition method proposed in [4] is also tested. Both methods exhibit stability, as shown in active and reactive power plots (Fig. 6). However, the smooth transition method demonstrates significantly lower overshoot and fluctuations compared to the sudden transition method. Specifically, during the transition, the sudden method results in a 4.1kW active power overshoot, whereas the proposed method shows only 41W. Similarly, the sudden method leads to a 4.4*kV AR* reactive power overshoot, while the proposed method experiences none.

Furthermore, a transition from the GFM mode to the GFL
mode is tested at t = 7 s. Here, for both methods, as explained before, ϵP and ϵQ jump from ϵmax to 0. Even though the ϵ value changes abruptly from ϵmax to 0, the transient is not significant because in GFL mode, control signals increases gradually and the transient is small.

## Vi. Conclusions

In this paper, we evaluate the robustness of conventional GFL and GFM inverters against power perturbations by analyzing their power-to-voltage responses. We observe that conventional GFL exhibits sensitivity to perturbations, whereas the droop control structure in GFM enables shaping of this sensitivity. Motivated by this, we propose a GFL control structure that is insensitive to high-frequency load perturbations and tracks low-frequency power references. Furthermore, drawing on the structural similarity between the proposed GFL controller and the GFM controller, we devise a smooth transition strategy between GFL and GFM modes. This strategy minimizes power overshoot and oscillation during the transition.

## References

[1] M. Elkhatib, J. Neely, and J. Johnson, "Evaluation of fast-frequency
support functions in high penetration isolated power systems," in 2017
IEEE 44th Photovoltaic Specialist Conference (PVSC).
IEEE, 2017,
pp. 2141–2146.
[2] Y. Qi, H. Deng, X. Liu, and Y. Tang, "Synthetic inertia control of gridconnected inverter considering the synchronization dynamics," IEEE Transactions on Power Electronics, vol. 37, no. 2, pp. 1411–1421, 2021.
[3] J. Wang and G. Saraswat, "Study of inverter control strategies on
the stability of low-inertia microgrid systems," in IECON 2022–48th Annual Conference of the IEEE Industrial Electronics Society. IEEE, 2022, pp. 1–6.
[4] S. Chakraborty, S. Patel, G. Saraswat, A. Maqsood, and M. V.
Salapaka, "Seamless transition of critical infrastructures using droop controlled grid-forming inverters," IEEE Transactions on Industrial Electronics, 2023.
[5] A. Yazdani and R. Iravani, Voltage-sourced converters in power
systems: modeling, control, and applications.
John Wiley & Sons,
2010.
[6] A. Askarian, J. Park, and S. Salapaka, "Enhanced grid following
inverter (e-gfl): A unified control framework for stiff and weak grids," IEEE Transactions on Power Electronics, 2024.
[7] Q.-C. Zhong and Y. Zeng, "Universal droop control of inverters with
different types of output impedance," *IEEE access*, vol. 4, pp. 702–
712, 2016.
[8] J. Driesen and K. Visscher, "Virtual synchronous generators," in
2008 IEEE power and energy society general meeting-conversion and
delivery of electrical energy in the 21st century.
IEEE, 2008, pp.
1–3.
[9] J. Liu, Y. Miura, and T. Ise, "Comparison of dynamic characteristics
between virtual synchronous generator and droop control in inverterbased distributed generators," IEEE Transactions on Power Electronics, vol. 31, no. 5, pp. 3600–3611, 2015.
[10] A. Askarian, J. Park, and S. Salapaka, "Control design for inverters:
Beyond steady-state droop laws," *arXiv preprint arXiv:2105.02292*,
2021.