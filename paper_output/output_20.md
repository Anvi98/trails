# Modeling Ris From Electromagnetic Principles To Communication Systems–Part Ii: System-Level Simulation, Ray Tracing, And Measurement

Le Hao, *Student Member, IEEE,* Sravan K. R. Vuyyuru, *Member, IEEE,* Sergei A. Tretyakov, Fellow, IEEE
Artan Salihu, *Student Member, IEEE,* Markus Rupp, *Fellow, IEEE,* and Risto Valkonen, Member, IEEE,

  Abstract—In this paper, we systematically study the electro-
magnetic (EM) and communication aspects of a RIS through
EM simulations, system-level and ray-tracing simulations, and
finally measurements. We simulate a nearly perfect, lossless RIS,
and a realistic lossy anomalous reflector (AR) in different ray
tracers and analyze the large-scale fading of simple RIS-assisted
links. We also compare the results with continuous and quantized
unit cell reflection phases with one to four-bit resolutions. Finally,
we perform over-the-air communication link measurements in an
indoor setting with a manufactured sample of a wide-angle AR.
The EM, system-level, and ray-tracing simulation results show
good agreement with the measurement results. It is proved that
the introduced macroscopic model of RIS from the EM aspects
is consistent with our proposed communication models, both for
an ideal RIS and a realistic AR.

  Index Terms—Anomalous reflector, reconfigurable intelligent
surface (RIS), system-level simulator, ray tracing, 6G.

I. INTRODUCTION
R
ECONFIGURABLE Intelligent Surfaces (RIS) have attracted considerable attention in recent years. This technique is considered as an emerging technology for the next generation of wireless communications due to its potential to improve coverage and energy efficiency in wireless networks [1], [2], [3]. Unlike conventional reflectors or antennas, a RIS comprises multiple unit cells capable of dynamically altering their electromagnetic properties for different incoming waves. This enables RIS to actively control, redirect, and enhance electromagnetic waves in desired directions.

The electromagnetic (EM) perspective of the RIS-related research has been addressed in Part I of this paper. The communication aspects, discussed in this part, focus on path loss and channel modeling for RIS-aided wireless communications. To simulate and analyze large-scale wireless networks This work was supported in part by the European Union's Horizon 2020
MSCA-ITN-METAWIRELESS project, under the Marie Skłodowska-Curie grant agreement No 956256. (Corresponding author: Le Hao)
L. Hao, A. Salihu, and M. Rupp are with TU Wien, Gusshausstrasse 25,
1040 Vienna, Austria. A. Salihu is also with Christian Doppler Laboratory for Digital Twin assisted AI for sustainable Radio Access Networks, Austria.

(e-mail: {le.hao, artan.salihu, markus.rupp}@tuwien.ac.at).

S. K. R. Vuyyuru is with Nokia Bell Labs, Karakaari 7, 02610 Espoo, Finland and the Department of Electronics and Nanoengineering, School of Electrical Engineering, Aalto University, 02150 Espoo, Finland (e-mail: sravan.vuyyuru@nokia.com; sravan.vuyyuru@aalto.fi).

S. A. Tretyakov is with the Department of Electronics and Nanoengineering, School of Electrical Engineering, Aalto University, 02150 Espoo, Finland (email: sergei.tretyakov@aalto.fi).

R. Valkonen is with Nokia Bell Labs, Karakaari 7, 02610 Espoo, Finland
(e-mail: risto.valkonen@nokia-bell-labs.com).

in realistic scenarios, simulation platforms such as ray tracing and system-level simulators serve as practical tools.

Recent studies have focused on studying path-loss modeling in RIS-assisted wireless networks [4], [5], [6], [7], [8]. In [4], [5], the authors demonstrated the scaling law governing the power reflected from a RIS is influenced by various factors, such as the RIS size and the mutual distances between the RIS and the transmitter/receiver with measurements. The authors of [6] give an overview of RIS-based channel measurements and experiments, large-scale path loss models, and small-scale multipath fading channel models, as well as channel characterization issues of RIS-assisted wireless communication systems. In [7], the authors introduce a macroscopic model for evaluating the multi-mode re-radiation and diffuse scattering from a RIS. That model can be integrated with ray-based models such as ray tracing and ray launching for realistic radio propagation simulations. In addition, the authors in [8] extend the model to include metasurface scattering at the beginning or at the end of the interaction chain and perform ray tracing simulations in an indoor scenario for a lossy, phase-gradient anomalous reflector (AR). The RIS-tailored Vienna systemlevel simulator (SLS) [9] with a MATLAB ray tracer interface, as well as path loss models for system-level simulations have been introduced in [10], [11]. In [12], the authors evaluate the system performance of a RIS-assisted cellular network through system-level simulations, such as the outdoor and indoor coverage and ergodic rate with different-sized RISs and under different frequency bands.

Even though a broad range of RIS-related research activities have been done in recent years, there is still a lack of a systematic study of RIS from the EM design to communication models. The above mentioned models are based on the notion of the local reflection coefficient from different points of the RIS panels, but this field model is not necessarily efficient or even electromagnetically consistent, and in practice it is not possible to independently control the response of each individual array element. In addition, there are no works on analyzing a realistic RIS in a ray tracer or in a system-level simulator. It is essential to build connections between the theory and practice, as well as between the EM design part and the communication analysis part.

To fill the gap, in this work, we systematically study the communication link performance of a RIS that is designed based on the EM theory of array scattering synthesis methodology [13]. We define the appropriate controllable parameters of RIS panels and next analyze the large-scale fading of the designed RIS through the Vienna SLS and with EM simulation results. Moreover, we integrate the designed RIS into a ray tracer to compare the ray tracing simulation results with the theoretical outcomes. Finally, we execute measurements using a manufactured AR prototype and compare the experimental results with theoretical analysis and ray tracing simulations. To the best knowledge of the authors, this is the first work that systematically studies a RIS from the EM design to the systemlevel and ray tracing simulations, then to model validation by prototype manufacturing and link measurements. This is also the first work on implementing a perfectly designed RIS and a realistic lossy AR to different ray tracers with the performance verified through theory.

The remainder of this paper is organized as follows. Section II introduces two methods of large-scale fading analysis and compares the results. Section III explains the RIS modeling in a ray tracer and compares the ray tracing simulation with theoretical results. In Section IV, we present experimental results for the manufactured panel and compare with ray tracing simulations. Finally, conclusions are drawn in Section V.

## Ii. Large-Scale Fading Analysis

In this section, we consider and compare two theoretical models of large-scale fading in RIS-assisted links. At this stage, we assume a far-field propagation scenario with a single line-of-sight (LOS)-path communication link. One of the studied methods is based on a theoretical estimation of the response of perfectly functioning ARs [14], incorporated in the Vienna SLS, and the other one is based on numerically simulated RIS directivity patterns.

## A. Method 1

A recently published path loss model [14], derived from an approximate electromagnetic solution for scattered fields from RIS, has been implemented in the Vienna SLS. This model is designed only for far-field propagation scenarios, and it is not applicable to near-field cases. Therefore, in this paper, we only analyze the far-field performance of RISs, and the near-field analysis is postponed to our future work. With this path loss model, the received power at the RX antenna is calculated as 
Pr = PtGt(θt, ϕt)Gr(θr, ϕr)ηeff

$$\left(\frac{S_{1}}{4\pi R_{1}R_{2}}\right)^{2}|\cos\theta^{i}\cos\theta^{r}|,\tag{1}$$

where $0<\eta_{\rm eff}\leq1$ is the RIS efficiency parameter that takes into account parasitic absorption in RIS as well as design and manufacturing imperfections. $S_{1}$ is the geometrical area of the RIS panel. The parameters $\theta^{i}$ and $\theta^{r}$ represent the incidence and reflection angles at the position of the RIS, respectively. The transmit power is indicated as $P_{t}$, while $G_{t}(\theta_{t},\phi_{t})$ and $G_{r}(\theta_{r},\phi_{r})$ represent the gains of the TX and RX antennas, respectively. $\theta_{t}$, $\phi_{t}$, $\theta_{r}$, and $\phi_{r}$ represent the elevation angle and the azimuth angle from the TX antenna to the RIS, and the elevation angle and the azimuth angle from the RX antenna to the RIS, respectively. The distance between the base station (TX) and the RIS is denoted by $R_{1}$, while the distance between the RIS and the user (RX) is denoted by $R_{2}$.

## B. Method 2

Another path loss model for a RIS-assisted link is based on the notion of RIS directivity and gain. The directivity is defined in terms of the electric field far-field pattern F(*θ, ϕ*) as [15]:

D(*θ, ϕ*) = 4πF(*θ, ϕ*) � 2π 0 � π 0 F(*θ, ϕ*) sin θdθdϕ , (2)
where F(*θ, ϕ*) is the far-zone radiation intensity pattern. The gain is calculated as

G(*θ, ϕ*) = ecdD(θ, ϕ), (3)
where ecd is the panel efficiency. If RIS losses can be neglected, we have ecd = 1.

In this work, we consider the designed RIS from Part I and calculate its gain numerically, using CST software. The RIS
gain values are found for four different modes each for five different sizes of RIS panels. The RIS gain results for the continuous load impedance design are listed in Table I. It is worth noting that each RIS model needs two gain values: Grx is the RIS gain in the direction from RIS to TX, and Gtx is the RIS gain in the direction from RIS to RX. Corresponding to our RIS designed for the normal incidence angle and four reflection angles, Grx is obtained at 0°, and Gtx is obtained at
13°, 27°, 43°, and 65°.

Once we obtain the RIS gains from CST simulations, the received power at the RX antenna through the RIS can be calculated according to Friis' formula for the links between TX and RIS and then between RIS and RX [15]:

4πR1 P1 = Gt(θt, ϕt)Grx(θrx, ϕrx) � λ �2 , (4) 4πR2 P2 = Gtx(θtx, ϕtx)Gr(θr, ϕr) � λ �2 , (5)
which gives the following path loss estimation [16]:

Pr = PtP1P2 = PtGt(θt, ϕt)Grx(θrx, ϕrx)Gtx(θtx, ϕtx)Gr(θr, ϕr)λ4 (4π)4(R1R2)2 . (6)
Here, θrx, ϕrx, θtx, and ϕtx represent the spherical angles defined from the RIS to the TX antenna, and from the RIS to the RX antenna, respectively.

## C. Comparison Between The Analytical Path Loss Model And Simulations

Here, we compare the path loss estimations obtained using both methods for a simple case of a single LOS link TX - RIS
- RX. As an example, we set Gt = Gr = 1, R1 = 17 m and R2 = 17.22 m, ηeff = 1. According to the design parameters of the RIS, the working angles are θi = 0° and θr = 13°, 27°,
43°, 65° for modes 1 to 4, respectively. The test RIS areas are S1 = 32 × 32 A, 48 × 48 A, 64 × 64 A, 80 × 80 A, and
96×96 A where A = (1.1034λ/4)2 is the area of one unit cell.

The common parameters in Eq. (6) are set the same as Eq. (1).

Grx and Gtx in Eq. (6) are the computed values from Table I

Floquet mode
Resolution
32 × 32
48 × 48
64 × 64
80 × 80
96 × 96
Gtx (dB)
Grx (dB)
Gtx (dB)
Grx (dB)
Gtx (dB)
Grx (dB)
Gtx (dB)
Grx (dB)
Gtx (dB)
Grx (dB)
Continuous
29.86
30.04
33.36
33.61
35.84
36.19
37.76
38.27
39.33
40.04
4 bit
29.86
30.03
33.35
33.61
35.84
36.19
37.76
38.26
39.32
40.03
3 bit
29.78
29.95
33.28
33.52
35.76
36.10
37.68
38.18
39.26
39.95
Mode 1
(13°)
2 bit
29.57
29.73
33.06
33.30
35.54
35.88
37.47
37.95
39.04
39.70
1 bit
27.20
27.28
30.69
30.81
33.17
33.34
35.10
35.35
36.68
37.02
Continuous
29.49
30.04
32.99
33.61
35.47
36.19
37.39
38.27
38.97
40.04
4 bit
29.45
30.01
32.95
33.58
35.43
36.16
37.36
38.23
38.93
40.00
3 bit
29.45
29.99
32.94
33.56
35.42
36.14
37.35
38.22
38.93
39.98
Mode 2
(27°)
2 bit
29.23
29.76
32.71
33.33
35.20
35.90
37.12
37.97
38.70
39.72
1 bit
26.46
27.03
29.94
30.53
32.42
33.04
34.35
35.02
35.94
36.68
Continuous
28.69
30.03
32.16
33.61
34.63
36.19
36.54
38.26
38.09
40.03
4 bit
28.51
29.87
31.99
33.44
34.45
36.01
36.36
38.09
37.92
39.84
3 bit
28.51
29.86
31.98
33.43
34.45
36.01
36.36
38.08
37.93
39.84
Mode 3
(43°)
2 bit
28.37
29.68
31.82
33.24
34.28
35.81
36.19
37.87
37.74
39.62
1 bit
24.97
26.37
28.46
29.88
30.94
32.39
32.87
34.38
34.44
36.03
Continuous
26.72
30.04
30.07
33.61
32.47
36.19
34.35
38.27
35.90
40.04
4 bit
26.65
30.00
30.01
33.57
32.41
36.15
34.29
38.22
35.84
39.98
3 bit
26.16
29.56
29.52
33.11
31.93
35.67
33.81
37.72
35.36
39.46
Mode 4
(65°)
2 bit
25.97
29.36
29.32
32.90
31.73
35.45
33.61
37.50
35.17
39.22
1 bit
22.31
25.89
25.70
29.34
28.13
31.81
30.06
33.77
31.65
35.40

with continuous loads. The results of the received power from the two methods are shown in Figs. 1(a), 1(b), 1(c), and 1(d) for modes 1 to 4, respectively.

From Fig. 1 we can observe that for all four modes, the two methods give very close results. The differences between the two methods are about 0.2 dB to 0.6 dB for mode 1, mode
2, and mode 3 when the RIS sizes change from 32 × 32 to
96 × 96. For mode 4 the difference is from 0.7 dB to 0.8 dB
with the five sizes.

This agreement is expected because Eq. (1) is valid for theoretically perfect ARs, and from Part I we saw that the RIS design with continuous loads gives a nearly perfect performance. In fact, it can be shown that for ideal ARs with continuous current distribution the considered two path loss models are equivalent. The model of (1) assumes that the RIS captures all the power that is incident on its surface and retransmits it without imperfections. This means that if we consider the same RIS as a conjugate-matched receiving antenna, its effective area Aeff is equal to the geometrical area of the panel cross-section, that is, Aeff = S1| cos θi|. Likewise, in the transmit regime, we have Aeff = S1| cos θr|. Using the general relation between the effective area and gain, valid for any linear and reciprocal antenna,

$$G=4\pi{\frac{A_{\mathrm{eff}}}{\lambda^{2}}},\eqno(7)$$
We can find the RIS gains for an ideal AR in terms of the panel area and the incidence and reflection angles:

$$G_{\rm rx}=4\pi\frac{S_{1}}{\lambda^{2}}\,|\cos\theta^{i}|\tag{8}$$

and

$$G_{\rm tx}=4\pi\frac{S_{1}}{\lambda^{2}}\,|\cos\theta^{r}|.\tag{9}$$
Substituting Eq. (8) and (9) into Eq. (6) we obtain the same equation as Eq. (1). Therefore, these two methods are equivalent if the RIS operates perfectly. The small differences between the two methods are from the RIS gain differences between CST simulation and the ideal theoretical values given by Eqs. (8) and (9), and they result from the spatial discretization of the reflecting surface.

From [11] we conclude that when the RIS size is doubled, the received power should achieve 6 dB gain for a tuned RIS. In these four figures, the received power has about 7 dB, 5 dB,
4 dB and 3 dB differences for the RIS sizes 32×32 to 48×48, from 48 × 48 to 64 × 64 from 64 × 64 to 80 × 80, and from
80 × 80 to 96 × 96, respectively. Since the RIS size 64 × 64
is four times larger than the size 32 × 32, the received power with 64 × 64 size is 12 dB higher than for the 32 × 32-sized RIS. Similarly, the difference between 48 × 48 and 96 × 96-
sized RIS is also 12 dB, which is consistent with the power scaling law [17].

## D. Load Quantization Analysis

The RIS gain values used in Sec. II-C are from the optimization of continuous reactive loads, corresponding to the assumption that the controllable loads can have arbitrary reactive impedances. In this section, we use the RIS gain results obtained from quantized load impedances, which are summarized in Table I, to investigate the difference between different quantization resolutions. From Part I we explained that the reflection efficiency of the RIS increases when the load quantization resolution changes from 1-bit to 4-bit. This is because the unit cell loads optimization results become more efficient when we have more load impedance values (2 values for 1-bit and 16 values for 4-bit). The reflection wave is more concentrated in the desired directions and the side lobes are better suppressed, which is why the RIS gain values in the desired directions also become higher and gradually get close to the gain when using continuous loads.

In Fig. 2 we compare the received powers between the designs based on continuous and quantized load values. Figures 2(a), 2(b), 2(c), and 2(d) show the results for modes 1, 2, 3, 4, respectively. The differences between the panels of
5 different sizes are almost the same for all four modes. As expected, when the resolution increases from 1-bit to 4-bit, the differences between the continuous loads designs and the discrete loads become smaller for all four modes. It can be observed that for 1-bit resolution, the scattering losses are quite high for all four modes, while the 4-bit resolution leads to very similar results as for the continuous loads. The 3-bit resolution gives already relatively good results, i.e., 1.11 dB
for mode 4, and less than 0.4 dB loss for modes 3, 2, and 1
are good enough.

## Iii. Ray Tracing Simulations

The results in Sec. II are based on the free-space path loss model, with only one LOS path between the TX and RIS, and one LOS path between the RIS and RX. To analyze wave propagation in more realistic environments, ray tracing is a very useful method since it accounts for the effect of the environment. There are several ray tracers already in the academic and industrial use, such as the MATLAB ray tracer, the Wireless InSite from Remcom, the CloudRT from Beijing Jiaotong University, and more. However, there are still no ray tracers that would include an accurately modeled RIS module. To simulate a RIS-assisted scenario, we have to first model a RIS into the ray tracer. In this section, we first incorporate a model of the designed RIS in the Wireless InSite ray tracer and verify the simulated results against the theory. After that, we extend the simulation scenario from a simple single-input single-output (SISO) case to a multipath scenario and analyze the simulation results.

## A. Verification In A Siso Scenario

We utilize Wireless InSite to accommodate RIS functionality by modeling the RIS as two separate antennas with imported E-field data from CST. For each RIS size at each propagation mode, we have two RIS patterns, one towards the incidence direction and the other toward the realized anomalous reflection angle. Therefore, in the ray tracer, we first simulate the TX-RIS link where the RIS is used as a receiver. Next, we simulate the RIS-RX link where the RIS is used as a transmitter.

To verify the RIS modeling in the ray tracer, we set up the same SISO scenario in Wireless InSite as in Sec. II, see Fig. 3. The center frequency is 26 GHz. The TX and RX antennas are initially omnidirectional (0 dB gain). The distance between the TX and RIS is 17 m, and the distance between the RIS and RX is 17.22 m. When the RIS is used as a receiver for the TX-RIS link, the RIS pattern is toward 0°, facing the TX
antenna. When the RIS is used as a transmitter for the RIS-RX
link, the reflection pattern of the RIS is towards 13°, 27°, 43°, and 65° for modes 1, 2, 3, 4, respectively. The TX and RX
direct link is blocked by a wall, so that there is no LOS path between them. First, the reflection path number is set as 0, so that we only observe the LOS paths TX-RIS and RIS-RX. All walls, ceiling and floor in this scenario are considered as perfect absorbers, to provide a direct point of comparison with the LOS path loss models considered above.

The comparison results between the ray tracing simulation and method 1 from Sec. II-A are plotted in Fig. 4. Figures 4(a), 4(b), 4(c), and 4(d) show results for modes 1, 2, 3, 4, respectively. From the four figures we can observe that the ray tracing simulation results are very close to the theoretical results that we have obtained for method 1. The larger the RIS size, the larger the differences between the two results for all four modes. However, even the largest difference that appears for mode 4 is about 0.6 dB. The comparison results indicate that our strategy of modeling RIS in the ray tracer seems correct for the LOS link.

## B. Multi-User Scenario With Only Los Paths

In this section, we extend the simulation to a multi-user scenario, as shown in Fig. 5. The room size is 24 × 25 × 3
(m3) in terms of width × length × height. There is one 1 ×
1 m2 glass window on the southern wall, and a 1.3 × 2.5 m2
door on the northern wall. The material of ceiling and floor is concrete, and the material of all walls is layered drywall. In the southwest corner of the room, there is a small wooden cabinet with a height of 2 m. The direct link between the TX
and RX antennas is blocked by two inner walls in the room. The TX antenna is a horn antenna with the maximum gain of
18.5 dBi toward 0° from the RIS. To investigate how the RX
antenna location influences the received power, we place 450
test omnidirectional RX antennas at different locations in the room, shown as red cubes. The spacing between the adjacent RX antennas is 0.6 m. The RISs for mode 1 to mode 4 with five different sizes are placed at the same location in the room with their receiving beams toward the TX antenna. The farfield distances of the five RIS sizes are 1.80, 4.04, 7.19, 11.23, and 16.17 m for the sizes of 32 × 32, 48 × 48, 64 × 64, 80×80, and 96×96, respectively, according to the calculation R = 2D2/λ with D the largest dimension of the antenna.

Hence, the distance between the TX and the RIS is set to 22 m, and the distance between the RIS and the RX antenna is from 17.4 m to 22.8 m to fulfil the far-field assumption.

The RX antennas are placed at 10 arcs with the RIS location being the center point of the arcs. The angle range of the RX
antennas toward the RIS is from 10◦ to 85.4◦ from northwest to southeast in the room. The height of TX, RX, and the RIS is 1.5 m.

To investigate whether the RX antennas at different locations benefit from the RIS, we simulate the LOS path from the TX to the RIS and from the RIS to each RX antenna for all four modes. Then we take the maximum received power for each RX antenna among all four modes. In this way, the RX antennas located at 13°, 27°, 43°, and 65° should all receive strong power due to the RIS assistance. The received power for all the users at different angles and distances from the RIS is plotted in Fig. 6. Figures 6(a), 6(b), 6(c), 6(d), and 6(e)
display the results for the 32 × 32, 48 × 48, 64 × 64, 80 × 80, and 96 × 96 RIS sizes, respectively. The radius of the polar plot is the distance between the RX and the RIS. The RIS is located at point 0 in these figures. The color of these figures' curves represents the received power.

From Fig. 6 we can observe that the RXs located at
13°, 27°, 43°, and 65° receive the highest power. The RXs at other angles receive lower power because there is no strong reflection from the RIS in those angle ranges. With an increased distance between the RIS and the RX antenna, the received power is slightly reduced. However, since the distance change is not so much from 17.4 m to 22.8 m, the power reduction is not so significant. The maximum received power at the RXs increases from −92.4 dB to −74.5 dB with the RIS size increasing from 32 × 32 to 96 × 96.

To have a more detailed look at the received power at different angles, we plot the received power versus the angle results in Fig. 7. At each angle, there are multiple points representing multiple RX antennas at that angle with different distances from the RIS. From Fig. 7(a) to 7(e) are the results for 32 × 32 to 96 × 96 RIS sizes, respectively. It is obvious that the received power at the RXs forms four strong beams at the four RIS reflection directions, which is related to the RIS scattering pattern. When the RIS size increases, the scattering pattern of the RIS at each reflection angle also becomes more directive and stronger.

Next, we choose 39 RX antennas that are on the first arc at the 17.4 m distance from the RIS. The received powers at the RX antennas for five RIS sizes are plotted in Fig. 8(a). The calculated differences of received powers at different RIS reflection angles are consistent with the results for the SISO scenario in Sec. III-A. When the angle toward the RX antenna is not at one of the RIS reflection angles, the received power of these RX antennas is much lower. The differences between the five RIS sizes at those angles are also not very significant. The empirical cumulative distribution function (ECDF) results are plotted in Fig. 8(b) to compare the overall received power at all the RX antennas for the five RIS sizes.

## C. Multi-User Scenario With Multi-Path Propagation

In this section, we consider a multi-path propagation scenario. The setup is the same as in Sec. III-B, except that in this scenario we include reflection paths. It should be noted that since our RIS is designed for illumination at normal incidence and reflections into a set of four angles, it can be effectively used only for these paths and for the reciprocal ones. The RIS scattering patterns for illuminations from other directions need to be calculated separately (for RIS realized as periodical arrays, this issue is considered in [18]). For simplicity, here we consider only one LOS path for the TX-RIS link, but three reflection paths for the RIS-RX link. To investigate the difference of the received power at the RIS between the LOS path and reflection paths, we run simulations with 0, 3, and
6 reflections, and find that the difference between the LOS and 3 or 6-reflections paths is smaller than 1 dBW, which is very small. Hence, even though it is not so realistic to assume only one LOS path between the TX and the RIS, it is still reasonable to use this assumption for simulations.

The received power results versus the distances to the RX
antenna and the angles are shown in Fig. 9. In addition to the results with five RIS sizes that are shown in Figs. 9(b) - 9(f), the results without RIS are plotted in Fig. 9(a). From these figures, we notice that when there is no RIS, only some RX antennas located at the angle of 10° and in the range of [26° 41°] receive relatively high power, while many RX
antennas receive only noise. However, when including a RIS in this scenario, almost all RX antennas are covered and receive a significant amount of signal power.

The received power as a function of the angle is plotted in Fig. 10. Compared to the LOS scenario in Fig. 7, the received powers at the users that are not located along the RIS reflection directions have significant improvement in the multi-path scenario. For example, in the LOS scenario with the RIS size 96 × 96, the received powers at the RX antennas in the [50° 57°] range are in the range of [−109 −96] dB.

However, in the multi-path scenario, the received powers at those RX antennas are in the [−104 −83] dB range and are higher than in the LOS scenario on average. It is obvious that after multiple reflections from the walls, floor, ceiling, and cabinet, the transmitted signals have a good chance of reaching those RX antennas in blind spots.

Similarly, in Fig. 11(a) we compare the results for RIS of five sizes with 39 RX antennas at the first arc that are 17.4 m away from the RIS. Compared to the case without RIS, the scenarios with RIS lead to significant improvement of received power at these RXs, especially at the RIS reflection directions and with a larger RIS size. The ECDF results of the received power are plotted in Fig. 11(b). The curve for the case of 'No RIS' does not start from zero because many RXs receive just noise, and they are not included in this figure.

In summary, the strategy of implementing a RIS as an antenna in a ray tracer is proved to be correct, which can be also applied to other ray tracers. The ray tracing simulation results from a SISO and multi-user LOS scenario prove that the maximum received powers at the RX antennas fulfill the power scaling law [17], which is actually from the communication theory where it just considers the RIS element number and phase shifts and does not involve any EM properties of the RIS, but our RIS model is from EM perspective and modeled as a whole antenna. So far we have reached a good agreement when applying the communication theory to a realistic RIS from the EM perspective. In addition to the comparison between the scenario with multiple reflections and without reflections, we can conclude that the contributions of a RIS are highly dependent on its reflection directions, the RIS sizes, and the reflections from the environment. The user located at the RIS reflection angles can receive the maximum power, the bigger RIS size also contributes more power to the user, and reflection paths in the environment can contribute to the user coverage improvement.

## Iv. Experimental Results

In Part I we introduced a prototype of a static 48 × 48
array and measured the scattering pattern of it in an anechoic chamber. In this part we performed over-the-air measurements at 26 GHz with the same prototype in an auditorium at Nokia Bell Labs Espoo office, to test the communication link performance and our ray tracing model with the realistic AR.

## A. Indoor Measurement And Ray Tracing Settings

The measurement scenario is shown in Fig. 12. The dimensions of the auditorium are 14 × 8 × 3 (m3). The TX and RX antennas are the same horn antennas with a maximum gain of Gt = Gr = 18 dBi and a beam width of 22° at
26 GHz. The height of the TX, RX, and the AR is 1.5 m, the distance between the TX and AR is R1 = 5.5 m, and the distance between the AR and the RX is R2 = 7 m. The TX horn antenna is connected to a vector signal generator via a cable, the RX horn antenna is connected to a low noise amplifier (LNA), and then connected to a signal & spectrum analyzer via cables. The signal generator is connected to the signal & spectrum analyzer through a reference clock and Ethernet cable for synchronizing the signals. The TX cable loss is Lt = 2.5 dB, the sum of the LNA gain and the RX
cable loss is Ga = 19.9 dB. We use a 400-MHz channel bandwidth and 16 QAM modulated 5G NR wavemode for transmitted signals, and the transmitted power at the TX side is Pt = 6 dBm.

To measure the TX-AR-RX link, we use a wave absorber to block the direct link between the TX and the RX antennas. The TX and the AR are fixed and are facing each other. The RX
antenna is placed at 55◦, 60◦, ..., 85◦ of the AR, respectively, but the distance between each RX location and the AR is always 7 m. We orient the direction of the RX antenna to always face the AR at each location. In the end, we obtain 7
different received power values at the RX antenna from the 7
different locations. We denote this power as Pm in dBm.

To simulate the same measurement scenario in a ray tracer, we first create a 3D model using SketchUp and import it to a ray tracer. The top view of the model is displayed in Fig. 13(a). This 3D model replicates the real dimensions of the whole room and the objects inside it. For practical reasons, the MATLAB ray tracer suits the auditorium scenario better than alternative ray tracers. Therefore, we use the MATLAB ray tracer in this section for simulations.

We model a horn antenna in MATLAB and use it for TX and RX antennas in ray tracing simulations. The maximum gain of the horn antenna is 18 dBi. Then we use a similar way of implementing RIS as in the Wireless InSite to implement the realistic AR in the MATLAB ray tracer. The locations of the TX, RX antennas, and the AR are the same as in the measurement. Figure 13(b) shows the ray tracing of the TX-AR LOS link and the AR-RXs LOS links. We first set the reflection number as 0 to observe the received power from the AR-assisted LOS links, and compare it with the theoretical results obtained from Sec. II, since the two methods in Sec. II also considers only the LOS paths. Then we set 3
reflections in ray tracing simulations for the TX-AR and AR- RX links to include the reflection paths from the room objects and compare the results with measurement results, since the reflections cannot be ignored in a realistic environment. We denote the simulated powers at 7 locations as Pr,orig. Then, considering the cable losses and the LNA gain, we obtain PRT,orig = Pr,orig − Lt + Ga.

## B. Results Comparison Between The Theoretical Model, Ray Tracing, And Measurement

In this section, we first compare the received power results between the two methods from Sec. II, the measurement result Pm, and the ray tracing simulation result PRT,orig as shown in Fig. 14(a). It is worth noting that method 1 can only give the results at the RIS targeted direction, it cannot be used to calculate received powers at other directions that the RIS is not designed for. In our case, we only consider the received power at 65◦ with method 1 since this AR is designed for 65◦. We denote this result as Pmtd1,orig. With method 2 and ray tracing, we obtain received powers also at other angles by utilizing the respective RIS radiation patterns from CST simulations. The result from method 2 is denoted as Pmtd2,orig. From Fig. 14(a)
we observe that the ray tracing results with zero reflection are the same as from method 2, and they are very close to the theoretical result from method 1, which is consistent with our analysis in Sec. II-C and Sec. III-A. However, the ray tracing results with 3 reflections have about 1.4 dB difference compared to measurement results at 60◦ and 65◦.

To investigate whether this difference is from our ray tracing model or from the measurement system, we perform a reference measurement for the TX-RX link and compare it with theoretical results. In this reference measurement, we do not include the AR and the absorber, but let the TX and RX antennas directly face each other every time when we move the RX antenna to the 7 locations. The results from this measurement is denoted as Pm,LOS in dBm. Because it is very easy to validate this kind of LOS scenario through theory, i.e., we calculate the free space path loss between the two antennas using the equation PFS = PtGtGr
�
λ
4πR
�2 in W, where R is the distance between the TX and RX antennas. Then adding the cable losses and LNA gain, we obtain a theoretical received power Ptheory = PFS −Lt +Ga in dBW, where the PFS here is in dBW. We find the power differences between the theoretical value and the measurement results are very small: Pdiff =
Ptheory −Pm,LOS = [1.5, 1.6, 1.1, 0.7, 0.3, 1.0, 0.3] dBm for the angles of [55◦, 60◦, 65◦, 70◦, 75◦, 80◦, 85◦], respectively. This difference may be due to the system loss in our measurement setups, including alignment errors of the antennas, and is not included in the theoretical model.

Now if we take into account the Pdiff when comparing the simulations and measurement results, i.e., use this Pdiff to correct the theoretical and simulation results and obtain Pmtd1,correct = Pmtd1,orig − Pdiff, Pmtd2,correct = Pmtd2,orig − Pdiff, and PRT,correct = PRT,orig − Pdiff. The comparison with measurement results Pm is shown in Fig. 14(b). We find the measurement results at 60◦, 65◦, and 70◦ now agree very well with the ray tracing results with 3 reflections. We can thus conclude that our designed RIS works as we expected. It is also proved that our theoretical analysis for a RIS-assisted link is correct, the 3D auditorium model is accurate, the RIS implementation in Wireless InSite and in the MATLAB ray tracer is correct, the theoretical analysis and ray tracing methods work not only for a perfect RIS, but also for a realistic lossy AR.

## V. Conclusion

In Part I we studied the scattering synthesis for multimode ARs. Based on that, we designed a periodic AR that supports multiple reflection directions. By optimizing the load impedances of each unit cell, with continuous and 1 to 4-bit resolution quantized reactive loads, the AR can be configured to reflect waves toward one main direction while suppressing reflections in other directions. The designed lossless RIS can achieve almost perfect reflection efficiencies in the desired directions. The experiment with a manufactured finite reflector validated our design and reached a good agreement with CST simulation results. In this Part II, we used the designed perfect RIS and the manufactured reflector prototype to evaluate their EM properties and communication performances. We implemented both the RIS and the AR into two different ray tracers and validated the results with the theory. In addition, we investigated the quantization effect on the RIS implementation and concluded that with a 3-bit quantization resolution, the RIS can already achieve very good results. Furthermore, we analyzed the large-scale fading of RIS-assisted communication links through EM simulation, system-level, and ray tracing simulations, as well as through indoor measurements in a room using a static AR as a test vehicle. The results demonstrated that our RIS design from the EM aspects, RIS implementation in the two ray tracers, and the system-level and ray tracing simulations with the two RISs from the communication aspects, are all correct and consistent with the measurement results.

From the EM design perspective, we acknowledge that our designed multi-mode reflector is intended for reflection in discrete anomalous angles. The coverage between these angles is a topic of an extension to this work in the future. The unit cell loads of the multi-mode reflector would be made reconfigurable so that a non-perfect anomalous reflection in the gap angles would be allowed by the design, however improving the coverage between the discrete modal anomalous angles. Another possibility is to construct a multi-mode static anomalous reflector from multiple single-reflection angle subpanels, i.e., not having a RIS as a reconfigurable surface, but multiple static anomalous reflectors side-by-side to implement the same functionality as the multi-mode RIS would do.

From the communication perspective, the validated connections between the EM and communication analysis for a RIS can accelerate the RIS technology realization. For example, by passing a limited set of macroscopic RIS parameters from the EM design to the RIS-tailored Vienna system-level simulator, the simulator can deal with realistic RISs in largescale scenarios. In addition, by importing the radiation pattern of a RIS into ray tracers, one can simulate the RISs in different scenarios taking the propagation environment's effects into consideration. By using our approaches with the software, we can obtain a good estimation of the system performance with realistic RISs in realistic scenarios without the need to conduct measurements.

## Acknowledgement

The authors express gratitude to Professor Do-Hoon Kwon from the University of Massachusetts Amherst, USA, for the valuable suggestions and discussions regarding array antenna scattering synthesis for periodic reflectors.

## References

[1] M. Di Renzo, A. Zappone, M. Debbah, M.-S. Alouini, C. Yuen,
J. de Rosny, and S. Tretyakov, "Smart radio environments empowered
by reconfigurable intelligent surfaces: How it works, state of research,
and the road ahead," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 11, pp. 2450–2525, 2020.
[2] S. K. R. Vuyyuru, R. Valkonen, S. A. Tretyakov, and D.-H. Kwon, "Efficient synthesis of passively loaded finite arrays for tunable anomalous reflection," *arXiv preprint arXiv:2312.04441*, 2023.
[3] A. D´ıaz-Rubio and S. A. Tretyakov, "Macroscopic modeling of anomalously reflecting metasurfaces: Angular response and far-field scattering," *IEEE Trans. Antennas Propag.*, vol. 69, no. 10, pp. 6560–6571, 2021.
[4] W. Tang, M. Z. Chen, X. Chen, J. Y. Dai, Y. Han, M. Di Renzo,
Y. Zeng, S. Jin, Q. Cheng, and T. J. Cui, "Wireless communications with reconfigurable intelligent surface: Path loss modeling and experimental measurement," *IEEE Transactions on Wireless Communications*, vol. 20,
no. 1, pp. 421–439, 2021.
[5] W. Tang, X. Chen, M. Z. Chen, J. Y. Dai, Y. Han, M. D. Renzo,
S. Jin, Q. Cheng, and T. J. Cui, "Path loss modeling and measurements for reconfigurable intelligent surfaces in the millimeter-wave frequency band," *IEEE Transactions on Communications*, vol. 70, no. 9, pp. 6259–
6276, 2022.
[6] J. Huang, C.-X. Wang, Y. Sun, R. Feng, J. Huang, B. Guo, Z. Zhong, and
T. J. Cui, "Reconfigurable intelligent surfaces: Channel characterization and modeling," *Proceedings of the IEEE*, vol. 110, no. 9, pp. 1290–1311, 2022.
[7] V. Degli-Esposti, E. M. Vitucci, M. D. Renzo, and S. A. Tretyakov,
"Reradiation and scattering from a reconfigurable intelligent surface: A general macroscopic model," IEEE Transactions on Antennas and Propagation, vol. 70, no. 10, pp. 8691–8706, 2022.
[8] E. M. Vitucci, M. Fabiani, and V. Degli-Esposti, "Use of a realistic
ray-based model for the evaluation of indoor rf coverage solutions using reconfigurable intelligent surfaces," *Electronics*, vol. 12, no. 5, 2023. [Online]. Available: https://www.mdpi.com/2079-9292/12/5/1173
[9] M. K. M¨uller, F. Ademaj, T. Dittrich, A. Fastenbauer, B. R. Elbal,
A. Nabavi, L. Nagel, S. Schwarz, and M. Rupp, "Flexible multi-node simulation of cellular mobile communications: the Vienna 5G System Level Simulator," EURASIP Journal on Wireless Communications and Networking, vol. 2018, no. 1, p. 17, Sep. 2018.
[10] L. Hao, A. Fastenbauer, S. Schwarz, and M. Rupp, "Towards system
level simulation of reconfigurable intelligent surfaces," in 2022 International Symposium ELMAR, 2022, pp. 81–84.
[11] L. Hao, S. Schwarz, and M. Rupp, "The extended Vienna systemlevel simulator for reconfigurable intelligent surfaces," in 2023 Joint
European Conference on Networks and Communications & 6G Summit
(EuCNC/6G Summit), 2023, pp. 1–6.
[12] B. Sihlbom, M. I. Poulakis, and M. D. Renzo, "Reconfigurable intelligent surfaces: Performance assessment through a system-level simulator," *IEEE Wireless Communications*, pp. 1–10, 2022.
[13] S. K. R. Vuyyuru, R. Valkonen, D.-H. Kwon, and S. A. Tretyakov,
"Efficient anomalous reflector design using array antenna scattering synthesis," *IEEE Antennas Wireless Propag. Lett.*, vol. 22, no. 7, pp. 1711–1715, 2023.
[14] S. Kosulnikov, F. S. Cuesta, X. Wang, and S. A. Tretyakov, "Simple linkbudget estimation formulas for channels including anomalous reflectors," IEEE Transactions on Antennas and Propagation, vol. 71, no. 6, pp. 5276–5288, 2023.
[15] C. A. Balanis, *Antenna Theory: Analysis and Design*.
John wiley &
sons, 2015.
[16] S. W. Ellingson, "Path loss in reconfigurable intelligent surface-enabled
channels," in 2021 IEEE 32nd Annual International Symposium on Personal, Indoor and Mobile Radio Communications (PIMRC), 2021, pp. 829–835.
[17] Q. Wu and R. Zhang, "Intelligent reflecting surface enhanced wireless
network via joint active and passive beamforming," IEEE Transactions on Wireless Communications, vol. 18, no. 11, pp. 5394–5409, 2019.
[18] A. D´ıaz-Rubio and S. A. Tretyakov, "Macroscopic modeling of anomalously reflecting metasurfaces: Angular response and far-field scattering," *IEEE Transactions on Antennas and Propagation*, vol. 69, no. 10,
pp. 6560–6571, 2021.