
## 5G Networks Supported By Uavs, Ress, And Riss

Adam Samorzewski Poznan University of Technology Poznan, Poland adam.samorzewski@doctorate.put.poznan.pl

  Abstract— This paper presents the examination of the 5G
cellular network aware of Renewable Energy Sources (RESs)
and supported by Reconfigurable Intelligent Surfaces (RISs)
and Unmanned Aerial Vehicles working as mobile access nodes.
The investigations have been focused on the energy side of
the Radio Access Network (RAN) placed within the area of
the city of Poznan (Poland). The gain related to enabling RES
generators, i.e., photovoltaic (PV) panels, for base stations (BSs)
was presented in the form of two factors - the average number
of UAV replacements (ANUR) with a fully charged one to ensure
continuous access to mobile services for currently served user
equipment (UE) terminals, and the average reduction in energy
consumption (AREC) within the whole network.1

  Index Terms—5G, cellular networks, energy consumption,
Reconfigurable Intelligent Surfaces, Renewable Energy Sources,
Unmanned Aerial Vehicles

## I. Introduction

Nowadays, telecommunication systems are powered mainly by fossil fuels. Those systems contribute about 25% to the total value of carbon dioxide (CO2) emissions caused by the Information and Communication Technology (ICT) segment, which shows an increasing trend in energy demand from one year to another [1]. Furthermore, currently, the ICT sector is responsible for a huge part of global Green House Gas (GHG) emissions, which are maybe underestimated and could actually be even as high as 2.1 to 3.9% [2]. Hence, to deal with this issue the necessity of finding alternative sources of power that will both meet the energy demand of wireless systems (4G,
5G, and beyond) and reduce the amount of produced CO2
emissions to the atmosphere might be required. Therefore, the engagement of Renewable Energy Sources (RESs), e.g., photovoltaic (PV) panels seems to be an appropriate solution [3]. However, it is still hard to be unequivocally stated whether the use of solar cells is much more environment-friendly (in terms of entailing emissions) or not, especially taking into Adrian Kliks Poznan University of Technology, Poznan, Poland and *Lule˚a University of Technology*, Lule˚a, Sweden adrian.kliks@put.poznan.pl or adrian.kliks@ltu.se account the processes of their production and utilization. On the contrary, the way of harvesting electrical energy from solar radiation seems to be non-polluting itself and the amount of potentially generated resources can be considered to some extent as endless (excluding the need to replace/renovate PV panels after some time period) in a long-term context [4].

Within the concept of cellular systems of the 5th generation, mobile services are divided into 4 main groups: Enhanced Mobile Broadband (eMBB), Critical Communications (CC) and Ultra Reliable Low Latency Communications (URLLC), Massive Internet of Things (mIoT), and flexible network operations, where first 3 of them, in short, assume the provision of high throughput, low latency, and a big number of connected devices at the same time, respectively [5]. From the perspective of delivering the first case, there may appear a limitation related to a finite number of physical resource blocks (PRBs) per network cell. This issue might be noticed especially in urban areas, where the population is quite dense. Thus, to guarantee sufficient capacity and bit rate in a given area, the idea of deploying base stations covering regions with socalled small cells has been developed. This idea of wireless system implementation is based on the provision of RAN with low-power access nodes distributed very close to each other. However, while bringing this small cell concept to life due to obstacles such as unfavorable city architecture or money deficits for building new stationary base stations, there is a risk of signal gap appearance. One of the approaches to handle this issue, which is more and more often taken under consideration in scientific works is the employment of additional supportive equipment, e.g., Unmanned Aerial Vehicles (UAVs) as mobile base stations (MBSs). This, in turn, gives mobile network operators (MNOs) the ability to dynamically adjust the actual locations of access nodes to cover radio signal gaps and/or support existing telecommunication infrastructure in serving areas (urban or remote), where the number of simultaneously connected user terminals can also fluctuate and even exceed primary assumed capacity (e.g., due to public events) [6], [7].

Besides, the use of so-called Reconfigurable Intelligent Surfaces (RISs) to control the radio signal coverage of wireless systems has got great attention in the current literature. The RIS is a device in the form of a surface consisting of a large number of passive (or sometimes active) reflecting elements, which are able to independently cause a desired change in phase and/or amplitude of the incident radio signal. As a consequence of assuring flexible reconfiguration of signal propagation (after enabling RISs), MNOs would be able to accomplish better performance of their networks by reducing interferences and dropouts and raising the reliability, capacity, and throughput of radio links [8], [9].

Thus, in this paper, we evaluate the true performance of the UAVs working as base stations, which are equipped with both RISs (for potential future use) and RESs (for extension of the operating time). The goal of this analysis is to find the most appropriate deployment and setup of the drone base stations over a certain area while considering the transmission power, the energy consumed by UAVs for their operation, and the energy production by the RESs. We evaluate the trade-off between the additional mass needed to carry RES and RIS elements and the gains related to energy generated by RESs. Finally, we carry out simulations based on real atmospheric data to verify the true performance of such a solution.

## Ii. Scenario

The scenario considered in the work takes into account the
5G cellular network placed within the old market of the city of Poznan in Poland (data given in [10]), the base stations of which are UAVs located based on the real data of one of the Polish mobile operator (given in [11]) and hovering 50
m above the ground. For this study, there was assumed that the placements of the drones do not change over time. Around the city, there are 100 outdoor users distributed randomly with fixed bit rate requirements equal to 100 Mbps per each. In Fig. 1 the map presenting the above-described scenario of the wireless system has been attached.

## A. Network Design

The examined network has been designed according to the planner tool described in [12] named Green Radio Access Network Design (GRAND). This tool projects and optimizes radio access networks toward power consumption and/or human exposure by enabling the optimal number of cells of base stations with predefined locations and adjusting their transmission parameters based on the instantaneous throughput requirements of user terminals connected to the wireless system. As the input data, the GRAND tool receives the lists of available base stations and active users with their specific transmission data, and the shape files describing the considered environment (in 3D) including buildings and coverage area. The location of each user is chosen randomly within the provided simulator for every single run. In addition, in the very beginning, all transceivers of access nodes broadcast the radio signal with maximum power. After distributing users within the zone of study, the planner software selects which one of the network cells shall be enabled and with what power they shall transfer the data to reach as many active users as possible. Within this step, the GRAND tool assesses potential radio links between the system and each UE based on the bit rate requested by it as well as the maximum allowable path loss for a particular association for different transmit power configurations. Next, when the graph of accessible BS-UE relations is prepared, a mixed integer programming (MIP) solver is engaged to search for the optimal result. In order to obtain this result an objective function is formulated based on the envisioned optimization of human exposure, power consumption, or both. Afterward, all the users start exchanging data with appropriate access nodes in a continuous manner causing a fixed traffic load throughout the whole time of a single simulation run. Simultaneously, energy balance calculations for all base stations are done, which are further translated to an average number of needed battery recharging per UAV with and without RESs.

## B. Equipment

The implementation of PV panels within the GRAND tool software has been inspired by the specifications of the real device, which can be found in [13]. However, it has been assumed that used PV panels are mounted on the top of the UAV's cover in the form of thin-film solar cells. Thus, because of the insignificant impact on the total power consumption of a single mobile base station, the weight of PV panels was omitted during all calculations devoted to energy characteristics within a simulation run. In addition, those calculations have been performed for 4 various days (each starting a different season of the year) to indicate how the harvesting of energy by PV panels depends on the time of the year in Poland.

Similarly, as for solar panels, the battery systems for UAV
BSs have been also designed based on the real implementation described in [14]. The objectives of using batteries for drones are to power them in order to fulfill the energy demand as well as to store the resources produced by RES generators connected to them. The lack of electrical energy delivered by the battery cells entails a need to replace the UAV with another one but fully charged. Nevertheless, it has been posited that batteries can be completely drained, and 5% of the total energy kept in a single one is always used for flights before and after the service.

The transceivers of UAV access nodes work in accordance with the Multiple-Input-Multiple-Output (MIMO) technology using 64 active antenna elements (AAE) transmitting radio signals in the 3500 MHz frequency band. The methods of channel estimation and signal processing adopted in the software are consistent with the minimum mean-squared error (MMSE) schema. Furthermore, each of those mobile base stations has also one device of RIS type with 16 identical passive reflecting elements performing phase shifting with a 6-bit resolution of the impinging radio signal. For the following study, the impact of RISs implementation within the examined area on radio signal propagation has been neglected contrary to its influence on the energy balance of the wireless system. However, their effect on the performance of the network will be taken into consideration in future work.

## C. Energy Models

All energy models used to provide the mathematical calculation within the GRAND top (related to energy production and within the GRAND) top (related to energy production from our original by scientific literature or real implementations.

_LWA Vcc_: Due to the system design concept, it was assumed that UAV access nodes do not change their positions during the simulation. Thus, within the evaluation of energy consumption of the UAV according to assessment the utilization caused by UAV having $(P_{\rm WAV})$. Thus, assess the utilization caused by UAV having $(P_{\rm WAV})$ and $(P_{\rm WAV})$ as described to [15], we present the following formula:

$$P_{\rm UAV}\left(t\right)=\sqrt{\left(\frac{\left(m_{\rm LVW}+m_{\rm RO}\right)\cdot g\left(t,h_{\rm LVW}\right)\right)^{3}}{2\cdot\pi^{2}\cdot t\cdot\rho\left(t,h_{\rm LVW}\right)}\right)},\tag{1}$$

where $t$ is the current time step and $m_{\rm LVW}$ and $m_{\rm RO}$ are the masses of the UAV and the package that is lifted by it. In our case $m_{\rm PKO}=N_{\rm NOB}\cdot m_{\rm NOB}+N_{\rm BS}\cdot m_{\rm PV}+N_{\rm PV}\cdot m_{\rm PV}+m_{\rm PV}\cdot m_{\rm PV}$, where $m_{\rm NOB}\cdot m_{\rm NOB}$, and $m_{\rm PV}$ are the masses of $N_{\rm PV}$ and $N_{\rm PV}$ are the numbers, respectively. The parameter of $m_{\rm PV}$ is the mass of the auxiliary hardware/polyakage carried by the model of a single or age, adequately. Finally, $g$ and $\rho$ are the traditional acceleration and air density at the altitude $h_{\rm LV}$ and $g$.

_LWA MRT_: Each UAV base station is equipped with a single RIS array in order to improve the efficiency of radio-signal broadening. By its reflecting fluorophore with this assumption, the reliability of the network consists of the network design, as a form of reproduction for further investigations, the examination of the wireless system (Pays) has been taken into consideration as well. Hence, referring to $h_{\rm LV}\left(t\right)=N_{\rm PKB}\cdot P_{\rm SKI}\left(t\right)_{\rm MSI}$), (2)
where NRIS,NRE are the numbers of used arrays and identical reflecting elements per single RIS, which effectively perform phase shifting on the impinging signal. Next, PPSH is the power consumption of each phase shifter, which is dependent on the bit resolution bPSH of the used type.

3) MIMO Transceiver: The model used to estimate the power consumed by radio hardware has been formulated in accordance with the work contained in [16]. The mathematical formula that evaluates the total power consumption (PMIMO)
by a single transceiver in the current time step t is as below:

$\rm{P_{\rm{Mim}}}\left(t\right)=P_{\rm{CP}}\left(t\right)+P_{\rm{PA}}\left(t\right),$
where PPA (t) = PTX(t)
µPA
is the power consumed by the power amplifier. The parameters of PTX and µPA are the transmit power and efficiency of the amplifier, respectively. Next, the PCP is the power spent by circuit components of the transceiver, which is expressed as follows:

$$P_{\rm CP}\left(t\right)=P_{\rm FX}+P_{\rm TC}\left(t\right)+P_{\rm CE}\left(t\right)+P_{\rm CD}\left(t\right)+P_{\rm BH}\left(t\right)$$ $$+P_{\rm SP}\left(t\right),\tag{4}$$
where PFIX is the fixed power consumed by a cell node. The parameter of PTC (t) = MBS (t) PCC is the power utilized by the transceiver chains in the time step t, where PCC is the power that is required to run the circuit components
(e.g. filters, I/Q mixers, etc.), and MBS is the number of presently active antenna elements of the cell. Next, PCE (t) =
3Bw
τc·ηBS KUE (t)
�
MBS (t) τp (t) + M 2
BS (t)
�
is the power needed by the channel estimators, which work according to the minimum mean-squared error (MMSE) scheme [16]. The parameters of Bw and ηBS are the channel bandwidth and computational efficiency, respectively. In addition, τp (t) =
RF · KUE (t) is the number of samples allocated for pilots per coherence block in a specific time step t, where RF is the pilot reuse factor and KUE is the current number of served users.

In turn, τc = Bc · tc is the number of samples per coherence block, where Bc and tc are the coherence bandwidth and time, respectively. Furthermore, PC/D (t) = PCOD ·TRDL (t)+PDEC ·
TRUL (t) is the total power consumed by a transceiver of the UAV BS for encoding (PCOD) and decoding (PDEC) the information transferred through uplink, in short UL, (TRUL)
and downlink, in short DL, (TRDL) connections in a particular time step t. The power model takes into account also the load-aware part of the consumption referring to the backhaul links - PBH (t) = PBT
�
TRUL (t) + TRDL (t)
�
, where PBT is the backhaul traffic power. Finally, the power required by the network cell for operations related to signal processing (e.g., UL reception and DL transmission, computation of the combining/precoding vectors) compliant with the MMSE

scheme ($P_{\text{SP}}$) is as below:

$$P_{\text{SP}}\left(t\right)=\frac{3B_{\text{W}}}{\tau_{\text{c}}\cdot\eta_{\text{BS}}}\left[M_{\text{BS}}\left(t\right)K_{\text{UE}}\left(t\right)\left(\tau_{\text{u}}\left(t\right)+\tau_{\text{d}}\left(t\right)\right)\right.\tag{5}$$ $$+\frac{\left(3M_{\text{BS}}\left(t\right)^{2}+M_{\text{BS}}\left(t\right)\right)K_{\text{UE}}\left(t\right)}{2}+\frac{M_{\text{BS}}\left(t\right)^{3}}{3}+2M_{\text{BS}}\left(t\right)$$ $$+M_{\text{BS}}\left(t\right)\tau_{\text{p}}\left(t\right)\left(\tau_{\text{p}}\left(t\right)-K_{\text{UE}}\left(t\right)\right)+M_{\text{BS}}\left(t\right)K_{\text{UE}}\left(t\right)\right],$$

where $\tau_{\text{d}}\left(t\right)$ is the number of DL data samples per coherence block in the time step $t$.

_4) PV Panel:_ There is also a need to model the energy harvesting process performed by PV panels mounted on the cover of each UAV access node. The output power of the set of PV arrays ($P_{\text{PV}}$) in a certain time step $t$ is denoted as [17]:

$$P_{\text{PV}}\left(t\right)=N_{\text{PV}}P_{\text{R,PV}}f_{\text{PV}}\cdot\frac{G_{\text{T}}\left(t\right)}{\widetilde{G}_{\text{T,STC}}}\left[1+\alpha_{\text{P}}\Big{(}T_{\text{c}}\left(t\right)-T_{\text{c,STC}}\Big{)}\right],\tag{6}$$
where NPV, PR,PV, and fPV are the total number of PV
panels allocated per network cell, and the rated power and derating factor of a single one. In addition, the first one is the multiplication of the numbers of PV panels connected in series (NPV,s) and parallel (NPV,p). Next, GT and Tc are the parameters that denote the solar radiation incident on the PV
array and its temperature. Thus, GT,STC and Tc,STC define the values of the same parameters but for standard test conditions
(STC). Finally, αP is the temperature coefficient of power dependent on the type of used PV panels. Besides, to assess the temperature of the PV cell (Tc), the formula is used [17]:

$$T_{\rm c}\left(t\right)=\frac{T_{\rm a}\left(t,h_{\rm PV}\right)}{1+\left(T_{\rm c,NOCT}-T_{\rm a,NOCT}\right)\left(\frac{\widetilde{G}_{\rm T}(t)}{\widetilde{G}_{\rm T,NOCT}}\right)\left(\frac{\alpha_{\rm P}\mu_{\rm mg,STC}}{\tau\alpha}\right)}\tag{7}$$ $$+\frac{\left(T_{\rm c,NOCT}-T_{\rm a,NOCT}\right)\left(\frac{\widetilde{G}_{\rm T}(t)}{\widetilde{G}_{\rm T,NOCT}}\right)\left[1-\frac{\mu_{\rm mg,STC}(1-\alpha_{\rm P}T_{\rm c,STC})}{\tau\alpha}\right]}{1+\left(T_{\rm c,NOCT}-T_{\rm a,NOCT}\right)\left(\frac{\widetilde{G}_{\rm T}(t)}{\widetilde{G}_{\rm T,NOCT}}\right)\left(\frac{\alpha_{\rm P}\mu_{\rm mg,STC}}{\tau\alpha}\right)},$$

where $T_{\rm c,NOCT}$, $T_{\rm a,NOCT}$, and $\widetilde{G}_{\rm T,NOCT}$ are the nominal operating cell temperature (NOCT) of the PV panel, and the ambient temperature and solar radiation at which the NOCT is defined, respectively. Next, $\tau$, $\alpha$, and $\mu_{\rm mg,STC}$ are the solar transmittance of any cover over the PV array and its solar absorptance, and the maximum power point efficiency of the PV panel under STC. This efficiency is equal to $\mu_{\rm mg,STC}=\frac{P_{\rm b,PV}}{a_{\rm PV}\cdot b_{\rm PV}\cdot G_{\rm T,STC}}$, where 
aPV·bPV·GT,STC , where aPV and bPV are the dimensions of a single PV module. In turn, the parameter of hPV is the ground-relative altitude of the PV
panels powering a specific cell.

5) Battery System: In order to shape the energy management within the battery system (EBATT) of each UAV, inspired by [18] we propose a new model specified below:

$$E_{\text{BATT}}\left(t\right)=\begin{cases}E_{\text{BATT}}\left(t^{\prime}\right)+\Delta E_{\text{BATT},1}\left(t\right),&\text{if}\Delta E\left(t\right)>0\\ E_{\text{BATT}}\left(t^{\prime}\right)+\Delta E_{\text{BATT},2}\left(t\right),&\text{otherwise}\end{cases},\tag{8}$$
where EBATT (t′) is the energy handled by the battery system in the previous time step t′. Next, ∆EBATT,1 and ∆EBATT,2
are the energy amounts that have to be transferred from/to the battery system in the current time step t. Finally, ∆E is the energy balance, i.e., the difference between required energy and harvested one at the same moment. The parameters of
∆EBATT,1 and ∆EBATT,2 can be expressed by the formulas:

$$\Delta E_{\text{BATT},1}\left(t\right)\tag{9}$$ $$=\max\left(\Delta E\left(t\right)\cdot\mu_{\text{BATT}},E_{\text{BATT},\max}-E_{\text{BATT}}\left(t^{\prime}\right)\right),$$ $$\Delta E_{\text{BATT},2}\left(t\right)=\max\left(\frac{\Delta E\left(t\right)}{\mu_{\text{BATT}}},-E_{\text{BATT}}\left(t^{\prime}\right)\right),\tag{10}$$

where $\mu_{\text{BATT}}$ and $E_{\text{BATT},\max}$ are the efficiency of the used battery type and maximum energy the battery system is able to collect, respectively. The latter is equal to $E_{\text{BATT},\max}=N_{\text{BATT}}E_{\text{BATT},\max}^{\prime}$, where $E_{\text{BATT},\max}^{\prime}$ is the maximum energy of a single battery, and $N_{\text{BATT}}=N_{\text{BATT},\text{}}N_{\text{BATT},\text{}}$ is the total number of accumulator units in a battery system. The parameters of $N_{\text{BATT},\text{}}$ and $N_{\text{BATT},\text{}}$ are the numbers of batteries linked to each other in serial and parallel order, respectively. To evaluate the current energy balance ($\Delta E$), the formula below was engaged:

$$\Delta E\left(t\right)=\tag{11}$$ $$\left(P_{\text{PV}}\left(t\right)-\frac{P_{\text{UAV}}\left(t\right)+P_{\text{MIMO}}\left(t\right)+P_{\text{RIS}}\left(t\right)}{1-\sigma_{\text{DC}}}\right)\left(t-t^{\prime}\right),$$
where σDC is the loss factor related to DC supplying the hardware parts of the UAV device.

6) Atmospheric Parameters: Finally, let us collect all auxiliary formulas used to calculate necessary atmospheric parameters. The air density (ρ) at the altitude h and in the current time step t can be calculated as follows [19]:

$$\rho\left(t,h\right)=\tag{12}$$ $$\frac{p_{\rm d}\left(t,h\right)}{R_{\rm d}\cdot\left(T_{\rm a}\left(t,h\right)+273.15\right)}+\frac{p_{\rm v}\left(t,h\right)}{R_{\rm v}\cdot\left(T_{\rm a}\left(t,h\right)+273.15\right)},$$

where $R_{\rm d}$ and $R_{\rm v}$ are the specific gas constants for dry air and water vapor, respectively. Next, $p_{\rm d}$ and $p_{\rm v}$ are the pressures of dry air and water vapor. The latter at the altitude $h$ and in the time step $t$ can be expressed by the formula [19]:

$$p_{\rm v}\left(t,h\right)=6.1078\cdot10^{\frac{7.5\cdot T_{\rm d}\left(t,h\right)}{T_{\rm a}\left(t,h\right)+257.3}},\tag{13}$$
The pressure of dry air at the same altitude and moment has been described by pd (*t, h*) = p (t, h) − pv (*t, h*), where p is the air pressure evaluated as [19]:

$$p\left(t,h\right)=p_{0}\left(t\right)\cdot e^{\frac{-g\left(h\right)\cdot M\cdot\left(h+h_{\rm T}-h_{0}\right)}{R\cdot T_{\rm a}\left(t,h\right)}}\tag{14}$$
where p0 is the air pressure at the reference level h0. It was assumed that the reference level is the sea level altitude
(h0 = 0). The parameter of hT is the absolute altitude of the terrain. Next referring to [20], the gravitational acceleration is described by g (h) = g0
r2
e
(re+h)2 , where g0 and re are the sea level acceleration and mean radius of the Earth, respectively.

Finally, the formula to calculate the ambient temperature (Ta)
at the altitude h and moment t is shown below [19]:

$$T_{\rm a}\left(t,h\right)=T_{\rm a}(t,h_{\rm WS})-0.0065\left(h+h_{\rm T}-h_{\rm WS}\right),\tag{15}$$

where $h_{\rm WS}$ is the absolute altitude, at which the measurements of weather conditions have been done (the altitude of the weather station - WS).

## Iii. Simulation Setup

The source code of the developed software was prepared in Java language. The examination of the system scenario described in Section II has been performed in the form of 10 independent simulation runs each considering 4 days of the previous year starting different seasons - vernal equinox
�
20th March 2022
�
, summer solstice
(21st June 2022), autumn equinox
�
23rd September 2022
�
, and winter solstice (21st December 2022). The parameters of users (location coordinates and traffic demand) have always been defined at the beginning of each simulation run. The assumed time step was equal to 1 minute
(4 · 24 · 60 = 5, 760 steps per simulation run), with which the weather data was updated, and then the calculations for energy production and consumption (proesumption) were carried out. The simulation setup for network and energy designs is highlighted in Tab. I and II.

| Parameter      | Sign   | Unit   |
|----------------|--------|--------|
| Value          |        |        |
| BS             | UE     |        |
| Quantity       |        |        |
| K              |        |        |
| -              |        |        |
| 8              | 100    |        |
| Movement Speed |        |        |
| v              | [      |        |
| m/s            |        |        |
| ]              |        |        |
| N/A            |        |        |
| 0              |        |        |
| Placement      | -      | -      |
| Technology         | -    | -   |
|--------------------|------|-----|
| 5                  |      |     |
| G                  | N/A  |     |
| Frequency          |      |     |
| f                  | [    |     |
| MHz                |      |     |
| ]                  | 3500 |     |
| N/A                |      |     |
| Channel Bandwidth  |      |     |
| B                  |      |     |
| w                  |      |     |
| [                  |      |     |
| MHz                |      |     |
| ]                  | 120  |     |
| N/A                |      |     |
| Used Subcarriers   |      |     |
| N                  |      |     |
| SC,u               |      |     |
| -                  |      |     |
| 320                |      |     |
| N/A                |      |     |
| Total Subcarriers  |      |     |
| N                  |      |     |
| SC,t               |      |     |
| -                  |      |     |
| 512                |      |     |
| N/A                |      |     |
| Sampling Factor    | SF   | -   |
| 1                  | .    | 536 |
| N/A                |      |     |
| Pilot Reuse Factor | RF   | -   |
| 1                  |      |     |
| N/A                |      |     |
Coherence Time
tc
[ms]
50
N/A
Coherence Bandwidth
Bc
[MHz]
1
N/A
TDD Duty Cycle DL
DDL
[%]
75
N/A
TDD Duty Cycle UL
DUL
[%]
25
N/A
Spatial Duty Cycle
S
[%]
25
N/A
Antenna Height
h
[m]
50
1.5
Antenna Elements
M
–
64
1
Antenna Gain
Ga
[dBi]
24
0
Antenna Feeder Loss
Lf
[dB]
3
0
Max. Transmit Power
PTX,max
[dBm]
42
23
| Noise Figure        | NF   |
|---------------------|------|
| [                   |      |
| dB                  |      |
| ]                   | 7    |
| N/A                 |      |
| Path Loss Model     | -    |
| 38                  | .    |
| N/A                 |      |
| Interference Margin | IM   |
| [                   |      |
| dB                  |      |
| ]                   | 2    |
| Doppler Margin      | DM   |
| [                   |      |
| dB                  |      |
| ]                   | 3    |
| N/A                 |      |
| Fade Margin         | FM   |
| [                   |      |
| dB                  |      |
| ]                   | 10   |
| N/A                 |      |
| Shadow Margin       | SM   |
| [                   |      |
| dB                  |      |
| ]                   | 10   |
| N/A                 |      |
| Implementation Loss   |   IL |
|-----------------------|------|
| [                     |      |
| dB                    |      |
| ]                     |    3 |
| N/A                   |      |
| Soft Handover Gain    |      |
| G                     |      |
| SHO                   |      |
| [                     |      |
| dB                    |      |
| ]                     |      |
| N/A                   |      |
| 0                     |      |

## Iv. Results

The results of performed simulations have been attached within Tab. III. The first array presents the amount of energy that can be harvested by PV panels of a single UAV during

| Parameter               |   Sign | Unit   |   Value |
|-------------------------|--------|--------|---------|
| Mass of UAV             |        |        |         |
| m                       |        |        |         |
| UAV                     |        |        |         |
| [                       |        |        |         |
| kg                      |        |        |         |
| ]                       |      2 |        |         |
| Auxiliary Mass          |        |        |         |
| m                       |        |        |         |
| AUX                     |        |        |         |
| [                       |        |        |         |
| kg                      |        |        |         |
| ]                       |      0 |        |         |
| Auxiliary Power         |        |        |         |
| P                       |        |        |         |
| AUX                     |        |        |         |
| [                       |        |        |         |
| W                       |        |        |         |
| ]                       |      0 |        |         |
| Hovering Altitude       |        |        |         |
| h                       |        |        |         |
| UAV                     |        |        |         |
| [                       |        |        |         |
| m                       |        |        |         |
| ]                       |     50 |        |         |
| Single Propeller Radius |        |        |         |
| r                       |        |        |         |
| p                       |        |        |         |
| [                       |        |        |         |
| m                       |        |        |         |
| ]                       |      0 | .      |       5 |
Number of Propellers
lp
–
12
DC Loss Factor
σDC
–
0.075
Mass of MIMO Transceiver
mMIMO
[kg]
1
Fixed Power Component
PFIX
[W]
10
Local Oscillator Power
PLO
[W]
0.2
Circuit Components Power
PCC
[W]
0.4
Encoding Power
PCOD
[W]
0.1
Decoding Power
PDEC
[W]
0.8
Backhaul Traffic Power
PBT
[W]
0.25
Computational Efficiency
ηBS
[Gflops/W]
75
Amplifier Efficiency
µPA
–
0.35
Number of Transceivers
NMIMO
–
1
Mass of RIS
mRIS
[kg]
1
Phase Shifter Power
PPSH
[W]
7.8
Phase Shifter Bit Resolution
bPSH
[bits]
6
Number of Reflecting Elements
NRE
–
16
Number of RISs
NRIS
–
1
Model
Solarland SLP020-12U
Mass of PV
mPV
[kg]
0
Nominal Voltage
Vn,PV
[V]
12
Voltage at Max. Power
Vmax,PV
[V]
17.2
Current at Max. Power
Imax, PV
[A]
1.16
Rated Power
PR,PV
[W]
20
Ground-relative Altitude
hPV
[m]
50
Module Dimensions
aPV x bPV
[m]
0.576 x 0.357
1000
Solar Radiation at STC
GT,STC
800
Solar Radiation for NOCT
GT,NOCT
�
W/m2�
Temperature under STC
Tc,STC
[◦C]
25
�
W/m2�
Temperature NOCT
Tc,NOCT
[◦C]
47
Temperature Coeffi. of Power
αPV
[%/◦C]
−0.5
10
Solar Absorptance
α
–
0.3
√
10
Solar Transmittance
τ
–
0.3
√
Derating Factor
fPV
–
0.723
Number in Serial Order
NPV,s
–
1
Number in Parallel Order
NPV,p
–
5
Total Number per Net. Cell
NPV
–
5
Model
Volt Accumulator LiFePO4 12.8V 60Ah
Mass of Battery
mBATT
[kg]
5.2
Nominal Voltage
Vn,BATT
[V]
12.8
Charging Voltage
Vc,BATT
[V]
14.6
Discharging Voltage
Vd,BATT
[V]
12.8
Charging Current
Ic,BATT
[A]
30
Discharging Current
Id,BATT
[A]
60
Capacity
CBATT
[Ah]
60
Provided Energy
E′
BATT,max
[Wh]
768
Max. Depth of Discharge
DoDmax
[%]
100
| Primary State of Charge        | SoC     |
|--------------------------------|---------|
| p                              |         |
| [                              |         |
| %                              |         |
| ]                              | 95      |
| Battery's Efficiency           |         |
| µ                              |         |
| BATT                           |         |
| -                              |         |
| 0                              | .       |
| Number of Cycles               |         |
| N                              |         |
| BC                             |         |
| -                              |         |
| 2000                           |         |
| Number in Serial Order         |         |
| N                              |         |
| BATT,s                         |         |
| -                              |         |
| 1                              |         |
| Number in Parallel Order       |         |
| N                              |         |
| BATT,p                         |         |
| -                              |         |
| 1                              |         |
| Total Number per Net. Cell     |         |
| N                              |         |
| BATT                           |         |
| -                              |         |
| 1                              |         |
| Reference Altitude             |         |
| h                              |         |
| 0                              |         |
| [                              |         |
| m                              |         |
| ]                              | 0       |
| Terrain Absolute Altitude      |         |
| h                              |         |
| T                              |         |
| [                              |         |
| m                              |         |
| ]                              | 54      |
| Weather Station Absolute Alti. |         |
| h                              |         |
| WS                             |         |
| [                              |         |
| m                              |         |
| ]                              | 90      |
| Mean Radius of the Earth       |         |
| r                              |         |
| e                              |         |
| [                              |         |
| m                              |         |
| ]                              | 6371009 |
| 9                              | .       |
| Sea Level Gravitational Accel. |         |
| g                              |         |
| 0                              |         |
Air Molar Mass
mair
[kg/mol]
0.0289644
�
m/s2�
8.31432
Universal Gas Constant
Ru
Dry Air Gas Constant
Rd
[J/ (kg · K)]
287.058
� N·m
mol·K
�
Water Vapor Gas Constant
Rv
[J/ (kg · K)]
461.495

the whole year on average detailing each season. According to the initial expectations, the biggest amount of resources the mobile base station is able to obtain from solar radiation is the summer solstice (572.64), where the peak value of the energy production process is also the highest (91.86).

The ranking was followed by vernal and autumn equinoxes and winter solstice. Hence, there could be seen that in terms of the reduction of energy delivered by the conventional sources (i.e., from the batteries, which are charged up from the dedicated stations) the order is adequate to the aforementioned dependencies (middle array). However, due to the limitations related to the number of PV cells as well as their efficiency of power generation, the maximal achieved energy gain was equal to 5.8% (summer solstice). It is also valid to be noticed that during the winter solstice, this gain is almost none (0.18%).

Finally, the bottom array indicates the average number of UAV BS replacements, when its battery is gone. Due to weather conditions, the variety of this number can even be observed when are no RESs engaged to power up the mobile access node. The highest number of exchanged drones very noticed for summer solstice (13.93) and next for autumn equinox
(13.39), winter solstice (13.28), and vernal equinox (13.24), respectively. On the contrary, when the UAVs are supported by PV panels, summer solstice as well as vernal equinox needs the lowest average number of replacements (12.98). Taking into account the fact that during the summer the energy demand of a single UAV BS increases compared to other seasons of the year, this confirms the above-described results related to the profit when generating resources from solar radiation at this time. Thus, due to the almost zero impact of using PV arrays in winter solstice on power consumption characteristics, the number of UAV replacements is the same for both cases, i.e., with and without enabled RESs.

Total (and peak) energy obtained from PV Panels per UAV [Wh]
No RESs
PV Panels
Vernal Equinox
0 (0)
475.17 (60.57)
Summer Solstice
0 (0)
572.64 (91.86)
Autumn Equinox
0 (0)
349.56 (65.15)
Winter Solstice
0 (0)
17.67 (4.18)
Annual average
0
353.76
Average reduction in energy consumption (AREC) [%]
No RESs
PV Panels
Vernal Equinox
0
4.89
Summer Solstice
0
5.8
Autumn Equinox
0
3.56
Winter Solstice
0
0.18
Annual average
0
3.61
Avarege number of UAV replacements (ANUR)
No RESs
PV Panels
Vernal Equinox
13.24
12.98
Summer Solstice
13.93
12.98
Autumn Equinox
13.39
13.09
Winter Solstice
13.28
13.28
Annual average
13.46
13.08

## V. Conclusions

The contribution presented in this paper highlights the advantages related to the use of PV panels as power generators in cellular networks equipped with UAVs as mobile access nodes and supported by RISs. For the considered scenario, due to the weather conditions prevailing in Poland as well as the assumed configurations of UAVs and RESs, the power savings (and the resulting financial ones) are equal to the level of 3.61% per year on average in comparison to the case, in which base stations of the wireless system are supplied only from the charging stations powered by the conventional energy grid. Although RESs like PV panels are characterized by time-varying and climate-dependent harvesting processes, by appropriate management of available resources (radio and energy) using optimizing algorithms (e.g., traffic steering, resource allocation, etc.) and enabling additional equipment like RIS arrays, we are able to improve already achieved results or even ensure energy autonomy for cellular network without worsening the quality of mobile services delivered to users. However, the implementation of those algorithms as well as studies focused on the impact of RIS on radio signal propagation will be taken into consideration in future work.

ACKNOWLEDGMENT
The authors would like to thank Prof. Margot Deruyck from the Ghent University - IMEC in Belgium for supporting the following work by providing the GRAND tool. The work was realized within project no. 2021/43/B/ST7/01365 funded by National Science Center in Poland.

## References

[1] C.-L. I et al, ,,Energy-efficient 5G for a greener future", Nature Electronics, vol. 3, pp. 182–184, 2020.
[2] C. Freitag et al., ,,The Climate impact of ICT: A review of estimates,
trends and regulations", arXiv: 2102.02622v1.
[3] M. Deruyck et al, ,,Designing a multiple renewable energy source system
to feed the wireless access network", Elsevier Sustainable Energy, Grids and Networks, vol. 31, 2022.
[4] M. K. Abid, M. V. Kumar, V. A. Raj, and M. D. K. Dhas, ,,Environmental Impacts of the Solar Photovoltaic Systems in the Context of Globalization", Ecological Engineering & Environmental Technology, vol. 24, no. 2, pp. 231–240, 2023.
[5] 3GPP, ,,Technical Specification Group Services and System Aspects;
Release 15 Description; Summary of Rel-15 Work Items (Release 15)", TR 21.915 v15.0.0, 2019.
[6] M. Mozaffari, W. Saad, M. Bennis, Y. -H. Nam, and M. Debbah, ,,A
Tutorial on UAVs for Wireless Networks: Applications, Challenges, and Open Problems", in IEEE Communications Surveys & Tutorials, vol. 21, no. 3, pp. 2334–2360, 2019.
[7] M. Alzenad, A. El-Keyi, F. Lagum, and H. Yanikomeroglu, ,,3-D
Placement of an Unmanned Aerial Vehicle Base Station (UAV-BS) for Energy-Efficient Maximal Coverage", in IEEE Wireless Communications Letters, vol. 6, no. 4, pp. 434–437, 2017.
[8] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C.
Yuen, ,,Reconfigurable Intelligent Surfaces for Energy Efficiency in Wireless Communication", in IEEE Transactions on Wireless Communications, vol. 18, no. 8, pp. 4157–4170, 2019.
[9] M. Di Renzo et al., "Smart Radio Environments Empowered by Reconfigurable Intelligent Surfaces: How It Works, State of Research, and The Road Ahead," in IEEE Journal on Selected Areas in Communications, vol. 38, no. 11, pp. 2450–2525, 2020.
[10] System Informacji Przestrzennej (SIP), ,,Pozna´n - Model 3D", Available
at: http://sip.poznan.pl/model3d/#/legend, Accessed: 21 May 2023.
[11] BTSearch, ,,Baza danych oraz mapa lokalizacji stacji BTS / pozwole´n
UKE", Available at: http://beta.btsearch.pl, Accessed: 21 May 2023.
[12] G. Castellanos et al, ,,Multi-objective optimization of human exposure
for various 5G network topologies in Switzerland", Computer Networks, vol. 2016, 2022.
[13] Solarland,
,,Solarland
SLP020-12U
–
Specifications",
Available
at:
https://www.solar-electric.com/lib/wind-sun/SLP020-12U.pdf,
Accessed: 21 May 2023.
[14] Volt, ,,Volt Accumulator LiFePO4 12.8V 60Ah - Specifications", Available
at:
https://voltpolska.pl/index.php?controller=attachment&id attachment=320, Accessed: 21 May 2023.
[15] S. Janji, A. Samorzewski, M. Wasilewska, and A. Kliks, ,,On the
Placement and Sustainability of Drone FSO Backhaul Relays", in IEEE Wireless Communications Letters, vol. 11, no. 8, pp. 1723–1727, 2022.
[16] E. Bj¨ornson, J. Hoydis, and L. Sanguinetti, ,,Massive MIMO Networks:
Spectral, Energy, and Hardware Efficiency", Foundations and Trends®
in Signal Processing, vol. 11, no. 3–4, pp. 154–655, 2017.
[17] HOMER Pro v3.15, ,,Documentation - HOMER's Calculations",
Available
at:
https://www.homerenergy.com/products/pro/docs/3.15/
homers calculations.html, Accessed: 21 May 2023.
[18] Voltacon, ,,How long does it take to charge batteries from solar panels?",
Available at: https://voltaconsolar.com/blog/2021/04/27/how-long-doesit-take-to-charge-batteries-from-solar-panels, Accessed: 21 May 2023.
[19] Omni
Calculator,
,,Physics
Calculators",
Available
at:
https://www.omnicalculator.com/physics, Accessed: 21 May 2023.
[20] vCalc, ,,Gravity Acceleration by Altitude", Available at: https://
www.vcalc.com/wiki/KurtHeckman/Gravity+Acceleration+by+Altitude, Accessed: 21 May 2023.
[21] Visual Crossing, ,,Historical Weather Data & Weather Forecast Data",
Available at: https://www.visualcrossing.com/weather-data, Accessed: 21 May 2023.
[22] O. Arnold, F. Richter, G. P. Fettweis, and O. Blume, ,,Power Consumption Modeling of Different Base Station Types in Heterogeneous Cellular Networks", IEEE, *Future Network & Mobile Summit*, 2010.
[23] E. A. Franklin, ,,Calculations for a Grid-Connected Solar Energy
System", Available at: https://extension.arizona.edu/sites/extension.arizona.edu/files/pubs/az1782-2019.pdf, Accessed: 21 May 2023.
[24] HOMER Pro v3.15, ,,Documentation - Glossary", Available at:
https://www.homerenergy.com/products/pro/docs/3.15/glossary.html, Accessed: 21 May 2023.