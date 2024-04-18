# Collision Avoidance Safety Filter For An Autonomous E-Scooter Using Ultrasonic Sensors ⋆

Robin Str¨asser ∗ Marc Seidel ∗ Felix Br¨andle ∗ **David Meister** ∗
Raffaele Soloperto ∗∗ **David Hambach Ferrer** ∗∗∗ **Frank Allg¨ower** ∗
∗ University of Stuttgart, Institute for Systems Theory and Automatic Control,
70550 Stuttgart, Germany (e-mail: e-scooter@ist.uni-stuttgart.de)
∗∗ ETH Z¨urich, Automatic Control Laboratory, 8092 Z¨urich, Switzerland
∗∗∗ B.Sc. student at the University of Stuttgart, 70550 Stuttgart, Germany Abstract: In this paper, we propose a collision avoidance safety filter for autonomous electric scooters to enable safe operation of such vehicles in pedestrian areas. In particular, we employ multiple low-cost ultrasonic sensors to detect a wide range of possible obstacles in front of the e-scooter. Based on possibly faulty distance measurements, we design a filter to mitigate measurement noise and missing values as well as a gain-scheduled controller to limit the velocity commanded to the e-scooter when required due to imminent collisions. The proposed controller structure is able to prevent collisions with unknown obstacles by deploying a reduced safe velocity ensuring a sufficiently large safety distance. The collision avoidance approach is designed such that it may be easily deployed in similar applications of general micromobility vehicles. The effectiveness of our proposed safety filter is demonstrated in real-world experiments.

## 1. Introduction

Sharing systems for electric scooters (e-scooters) are well established in many cities around the globe (G¨ossling, 2020). E-scooters are a popular choice for urban mobility, particularly for short-distance commutes (Degele et al., 2018). While on-demand availability and distribution in dockless sharing systems are part of their appeal, these are also the cause of various practical challenges (Hollingsworth et al., 2019; Tuncer and Brown, 2020; G¨ossling, 2020). E-scooter related issues include cluttered sidewalks due to inconveniently parked or dropped escooters, as well as the need for additional vehicles and personnel to collect and charge the e-scooters or relocate them. To achieve high on-demand availability, suppliers often rely on non-sustainable and staff-intensive relocation of e-scooters using large vehicles. In addition, a large number of e-scooters are typically deployed to increase availability. These challenges result in high operational costs - economically (Heineke et al., 2019; Rose et al., 2020), ecologically (Cazzola and Cris, 2020; Krauss et al., 2022), and socially (Farley et al., 2020; G¨ossling, 2020; Gioldasis et al., 2021; Mehdizadeh et al., 2023). Given these observations, Wenzelburger and Allg¨ower (2020) propose the development of an autonomous escooter that can resolve or alleviate many of the described concerns about shared e-scooters. In particular, with the term *autonomous e-scooter*, we refer to a standard twowheeled e-scooter, augmented with additional features that enable the system to self-stabilize its upright position and autonomously navigate in a specified environment while avoiding unknown obstacles. By endowing e-scooters with the capability to move autonomously while not in use, cost-intensive manual redistribution or charging become obsolete. In addition, a ride with such an e-scooter is allowed to end anywhere within the region of interest, since this modified free-floating sharing system leverages the advantages of station-based sharing systems by autonomously parking an e-scooter after its ride and, thus, preventing cluttered public spaces. Moreover, their autonomy allows for optimal self-distribution according to the current or forecasted demand which improves availability and, thereby, allows to reduce the number of e-scooters necessary to cover an area of operation. Related work: As the availability and popularity of micromobility vehicles is rapidly increasing, also the proper interaction of such vehicles with their environment is of high interest, see, e.g., Li et al. (2023). Further, autonomous operation in micromobility needs to be carefully designed due to the close interaction with pedestrians and other parts of the urban environment (Christensen et al., 2021). Autonomous cars typically rely on a variety of expensive sensors (Koon, 2023), whereas micromobility vehicles are often designed with a lower budget and therefore have only a few low-cost sensors installed. Although ultrasonic sensors are known to be of low cost in installation and postprocessing compared to, e.g., LiDAR sensors or cameras, they are rarely used in micromobility for obstacle detection or collision avoidance (Manikandan and Kaliyaperumal, 2022; Guglielmi, 2023). However, ultrasonic sensors already proved useful, e.g., for the obstacle avoidance of robots (Borenstein and Koren, 1988; Yasin et al., 2020) or lateral collision avoidance of cars (Song et al., 2004). Contribution: In this paper, we focus on the development of a collision avoidance safety filter for the autonomous escooter shown in Fig. 1 using low-cost ultrasonic sensors. The main contribution of our proposed solution is the integration of a feedback design for safety stops for the autonomous e-scooter. More precisely, we propose a gainscheduled controller that limits the velocity applied to the e-scooter based on filtered distance measurements of the sensors. Here, it is crucial to design a suitable filter for the sensors to account for faulty or missing measurements. Since the e-scooter is not only driving straight but also in curves, we need to ensure that the controller is able to handle different scenarios. To this end, we incorporate three different ultrasonic sensors, where one faces straight and the other two are oriented to the sides of the e-scooter. The designed feedback solution allows to weigh the measurements of all three sensors according to the currently applied steering angle to ensure that only obstacles which block the imminent path are considered in the control decision. The proposed approach is designed to be easily transferrable to other autonomous vehicles, where the focus is the deployment in pedestrian areas with a low-cost design and, thus, low complexity requirement. Further, we aim to provide an easy-to-follow implementation and design guide for general applications.

To this end, we include a description of the hardware setup as well as the respective controller design. Outline: In Section 2, we provide an overview of the hardware setup of the autonomous e-scooter, and describe the dynamics of the e-scooter. Section 3 details the proposed collision avoidance safety filter. The derived approach is demonstrated in Section 4 by means of real-world experiments. Finally, we conclude the paper in Section 5.

## 2. System Overview

In this section, we provide an overview of the developed e-scooter prototype. We describe the system dynamics in Section 2.1, and the hardware setup in Section 2.2, where we elaborate specifically on the added components for the proposed collision avoidance safety filter.

## 2.1 System Dynamics

In the following, we describe the autonomous e-scooter to provide a better understanding of the studied prototype. A main feature of our prototype is that it balances itself

on two wheels when moving autonomously, i.e., when not being used by a human. As described in Wenzelburger and Allgower (2020), this is realized by a reaction wheel which is mounted between deck and stem in order to self-stabilize the e-scooter, see Fig. 2. Thus, from the perspective of a dynamical system, the e-scooter is described by the state vector

$$x(t):=\left[x_{\rm p}(t)\ y_{\rm p}(t)\ \psi(t)\ v(t)\ \delta(t)\ \dot{\phi}(t)\ \dot{\phi}(t)\ \omega(t)\right]^{\top},\tag{1}$$

where $x_{\rm p}(t)$, $y_{\rm p}(t)$, and $\psi(t)$ represent the position and orientation of the e-scooter, respectively, $v(t)$ is the (linear) velocity at the rear wheel, and $\delta(t)$ denotes the steering angle for some time $t\geq0$. In addition, we have three states corresponding to the roll dynamics of the e-scooter: the roll angle $\phi(t)$, its derivative $\dot{\phi}(t)$, and the motor velocity of the reaction wheel $\omega(t)$. The physical meaning of the individual components of the state vector is illustrated in Fig. 3. Further, the system is controlled with the input vector

$$u(t):=\left[v_{\rm cmd}(t)\ \delta_{\rm cmd}(t)\ \tau(t)\right]^{\top},\tag{2}$$
where vcmd(t) is the commanded velocity of the e-scooter at its rear wheel, δcmd(t) is the commanded steering angle, and τ(t) is the torque applied to the reaction wheel. Moreover, our application faces the state and input constraints
|ω(t)| ≤ ωmax, |v(t)| ≤ vmax, |δ(t)| ≤ δmax, and |τ(t)| ≤
τmax. Note that the desired velocity vcmd(t) and steering angle δcmd are processed by already implemented low-level controllers on the hardware to achieve zero tracking error in v(t) and δ(t). This step is, however, neglected in the following due to its low relevance for the proposed collision avoidance approach.

As discussed in Soloperto et al. (2021), the roll dynamics for the balancing of the e-score can be decoupled from the remaining dynamics corresponding to the e-score's longitudinal and lateral motion. More precisely, stabilization of the vertical position of the e-score is achieved by following the results in Wenzelburger and Allgower (2020) based on the inverted pendulum dynamics

$$\begin{bmatrix}\dot{\phi}(t)\\ \dot{\phi}(t)\\ \dot{\omega}(t)\end{bmatrix}=\begin{bmatrix}\dot{\phi}(t)\\ (mgz_{\mathrm{m}}\sin(\phi(t))-\tau(t))/J_{\mathrm{e}}\\ -(mgz_{\mathrm{m}}\sin(\phi(t)))/J_{\mathrm{e}}+\tau(t)/J_{\mathrm{d}}\end{bmatrix},\tag{3}$$

where $m$ is the mass of the overall system, $z_{\mathrm{m}}$ is the height of the center of mass above the ground for $\phi(t)=0$, $g=9.81\,\mathrm{m/s^{2}}$ is the gravity acceleration, and the parameters $J_{\mathrm{e}}$ and $J_{\mathrm{d}}$ denote the moments of inertia of the overall system and of the reaction wheel, respectively, both computed with respect to their rotational axes. Further, the e-score's motion can be described by a single-track model, namely the kinematic bicycle model (Kong et al., 2015), as

$$\begin{bmatrix}\dot{x}_{p}(t)\\ \dot{y}_{p}(t)\\ \dot{\psi}(t)\end{bmatrix}=\begin{bmatrix}v(t)\cos(\psi(t)+\delta(t))/\cos(\delta(t))\\ v(t)\sin(\psi(t)+\delta(t))/\cos(\delta(t))\\ v(t)\tan(\delta(t))/l\end{bmatrix},\tag{4}$$

where $l$ denotes the distance from the front to the rear wheel. Hence, the considered e-scoreter can be modeled and controlled via simple differential equations.

## 2.2 Hardware Setup

Here, we briefly describe the hardware setup of the autonomous e-scooter prototype, on which we deploy the proposed collision avoidance safety filter. The setup is related to the one described in Soloperto et al. (2021), but we use a different e-scooter model with additional components for the collision avoidance framework. In particular, the prototype is constructed using an *Egret Pro* escooter which is augmented by a reaction wheel in order to allow for the stabilization in the roll dynamics (see Fig. 2). The stabilization algorithm is implemented on a VESC
6 MkV motor controller, which directs a current to a Maxon EC90 flat DC motor to actuate the reaction wheel.

The controller itself is based on the approach proposed in Wenzelburger and Allg¨ower (2020) and takes as input an estimation of the roll angle. We employ a Mahony filter (Mahony et al., 2008) to compute the roll angle estimate via sensor fusion of the different measurements of the inertial measurement unit of the VESC. As shown in Fig. 2, steering is achieved by a PD4-C5918L4204-
E-08 stepper motor mounted inside the reaction wheel casing, which in turn is fixed to the deck of the e-scooter. An additional *VESC 6 MkV* motor controller is used to actuate the rear wheel for driving forward and backward. Both VESC motor controllers run at 1 kHz to enable fast and precise control of the driving velocity and roll angle. More computationally demanding operations are executed on a *Raspberry Pi 4B* at 50 Hz. Tasks on the Raspberry Pi involve, for instance, the detection of obstacles and sending the desired input signals u(t) to the motor controllers. The proposed mechanical and electronic design allows us to place most of the added components into a single casing, which encloses the reaction wheel. In addition, this configuration is beneficial since it only marginally modifies the original e-scooter, and, therefore, other off-the-shelf escooters can be easily upgraded to an autonomous version by adding our hardware and casing. Further, in order to contain the weight of the e-scooter, we make use of the power supply of its original battery to power the reaction wheel, the steering motor, as well as all the installed electronics. In the described configuration, the weight of the vehicle increases by 11.5 kg, leading to a total weight of 34 kg. To establish the proposed collision avoidance safety filter of this paper, we require additional components on the e-scooter. In particular, we employ three low-cost HC-
SR04P ultrasonic sensors to detect pedestrians and other obstacles in front of the e-scooter. As depicted in Fig. 4, one ultrasonic sensor is facing straight, and the other two are oriented to the sides of the e-scooter. We note that the chosen sensor model is a low-cost solution, which is beneficial for the deployment in a large number of e-scooters or other cost-restricted applications. On the Raspberry Pi, we execute *Python* code with the gpiozero library to measure the distance to the closest object with a frequency of 10 Hz. Each ultrasonic sensor detects objects in a 3D cone with an angle of 15◦, ranging from a minimum distance of 2 cm to a maximum distance of 400 cm, with an accuracy of 0.3 cm. In practice, however, this accuracy is hardly met since the sensors are affected by the environment, e.g., by the material of the detected object, and, thus, measurements may be faulty or missing completely. Here, the outer ultrasonic sensors are facing both sides of the e-scooter with an angle of 24◦, where each outer sensor is positioned with a distance of 37 mm to the center. The low requirements on the supplied voltage allows us to connect the ultrasonic sensors directly to the Raspberry Pi, without additional wiring to the power supply of the e-scooter. The sensors are fixed to the handlebar by a 3D- printed component which is specifically designed to ensure that the sensor rotates with the handlebar, and, hence, it is always able to detect obstacles in driving direction as well as in the relevant surrounding of the e-scooter, see Fig. 4. Based on the field of view, the height of the frontal sensor is fixed at 56 cm above the ground while the sensors on the side are fixed at 50 cm above the ground. By this, we ensure that 1) the sensors detect a wide range of obstacles and 2) there is no interference with the ground.

## 3. Collision Avoidance Safety Filter

In this section, we detail the proposed collision avoidance safety filter for keeping a safe distance from unknown obstacles. In particular, we provide an overview of the controller structure (Section 3.1), describe the employed filter for the distance measurements (Section 3.2), and detail the design of the distance controller (Section 3.3). We note that the derived collision avoidance safety filter is independent of the specific dynamics of the e-scooter presented in Section 2.1 and can be applied to other autonomous vehicles as well.

## 3.1 Overview Of The Controller Structure

In order to ensure that the e-scooter is able to autonomously stabilize its upright position, we assume that the balancing algorithm proposed in Wenzelburger and Allg¨ower (2020) is active at all times. In addition, we assume that a high-level planner is available with the goal to compute the desired velocity vcmd(t) and the desired steering angle δcmd(t) based on any feasible desired state xdes(t) and the current state x(t). However, the high-level planner cannot guarantee the feasibility of the commanded path as it has no access to local environment information, possibly leading to collisions with unknown obstacles, e.g., pedestrians. The main goal of this work is to appropriately adjust the desired velocity vcmd(t) such that collisions are avoided at all times, while simultaneously allowing the e-scooter to deviate as little as possible from the desired behavior planned by the high-level planner. To this end, we propose a *distance controller* that uses the commanded velocity vcmd(t) and a later in (9) described critical distance dcrit(t)
between the e-scooter and the closest obstacle to generate a velocity vsafe(t) ≤ vcmd(t) via (10). More precisely, the safe velocity vsafe(t) limits the desired velocity vcmd(t)
under consideration of a detected obstacle to ensure a safe driving behavior of the e-scooter. Here, we emphasize that the collision avoidance is only active if the commanded velocity is non-negative, i.e., the high-level controller does not command the e-scooter to drive backwards and, thus, An overview of the general controller structure related to the driving dynamics is shown in Fig. 5. The described distance controller together with the measurement filter therefore functions as a safety filter. It can be easily integrated in other micromobility solutions as Fig. 5 demonstrates. Existing applications only require the incorporation of the proposed safety filter before applying the desired control input to the hardware.

## 3.2 Distance Measurement Filter

As described in the last section, our designed distance controller receives a critical distance dcrit(t) to the closest obstacle with respect to the e-scooter. To this end, we use filtered distance measurements d(k)
filt(t) rather than the raw measurements d(k)
meas(t) of the three ultrasonic sensors with the aim to improve the quality and accuracy of the signals and, hence, of the resulting velocity vsafe(t).

Here, k ∈ {c*, ℓ,* r} corresponds to the center, left, and right ultrasonic sensor, respectively. Then, the individual filtered distance measurements are combined to compute the critical distance dcrit(t).

_Filter design:_ First, we inspect the sample measurement of one of the ultrasonic filters shown in Fig. 6 from a real-world experiment, where the e-score is driving towards a person. We observe that the raw measurements are either rather accurate or falsely large due to missed detections, but not falsely small. Then, we leverage these observations for the filter design of each ultrasonic sensor and implement an exponential smoothing filter

$$d_{\text{hit}}^{(k)}(t)=\alpha d_{\text{mem}}^{(k)}(t)+(1-\alpha)d_{\text{hit}}^{(k)}(t-\Delta t)\tag{5}$$

with $k\in\{\text{c},\ell,\text{r}\}$ and factor $\alpha\in(0,1]$ reducing noise in the distance measurements, where

$$d_{\text{mem}}^{(k)}(t)=\min_{\tau\in[\max\{0,t-\tau_{\text{mem}}+1\},t]}d_{\text{means}}^{(k)}(\tau)\tag{6}$$ denotes the minimum of the last $\tau_{\text{mem}}\geq1$ measured distance measurements. More precisely, the introduced memory parameter $\tau_{\text{mem}}$ mitigates missed detections to ensure that the filtered distance measurements are not erroneously overestimated. The state of the filter is initialized as $d_{\text{lift}}^{(k)}(0)=0$. The introduced smoothing filter represents a delayed version of a first-order filter, where the smoothing factor $\alpha=1-e^{-\Delta t/T}$ yields the time constant

$$T=-\frac{\Delta t}{\ln(1-\alpha)}.\tag{7}$$

Here, $\ln(\cdot)$ denotes the natural logarithm and $\Delta t$ is the sampling frequency of the respective hardware, in our case $\Delta t=0.02\,\text{s}$. The time constant is chosen in dependence of whether the measured distance is increasing or decreasing. More precisely, we define

$$T^{(k)}(t)=\begin{cases}T_{\text{i}}&\text{if}d_{\text{meas}}^{(k)}(t)>d_{\text{lift}}^{(k)}(t-\Delta t),\\ T_{\text{d}}&\text{if}d_{\text{meas}}^{(k)}(t)\leq d_{\text{lift}}^{(k)}(t-\Delta t),\end{cases}\tag{8}$$
where Ti > 0 for increasing measurements is significantly larger than Td > 0 for decreasing measurements. Note that the memory of size τmem introduces an additional delay for increasing measurements, which makes the filter more conservative but also more robust to missed detections. All three constants are tuning variables which depend on the used hardware and the considered velocity range of the vehicle. Using different time constants for increasing or decreasing distances resembles an important safety feature. More precisely, if an obstacle is at close range but the sensor receives no or a wrong echo due to a disturbance, then the distance measurement is erroneously large. Without filtering, no obstacle would be detected for a short period of time which would result in the e-scooter accelerating forward until the next correct measurement is taken. However, by using the above described filter parameters, we are still able to employ a safety-conscious solution. On the one hand, the proposed approach requires multiple measurements of an obstacle-free path to recover from halting due to an obstacle. On the other hand, only a few measurements indicating an obstructed path are required to indeed detect an obstacle. For the sample measurement in Fig. 6, where in many but short time intervals the measured distance dmeas(t) is falsely large due to missed detections, the filtered distance dfilt(t) ensures safe operation on the cost of a more conservative behavior with respect to the detected obstacle. More precisely, the filtered signal follows decreasing tendencies fast while it delays increasing distance measurements to account for possibly missed detections. We emphasize that the proposed filter results in an accurate and smooth distance measurement, where the resulting delay is outweighed by the obtained safety benefits of the filter. Critical distance:
Recall that we use three ultrasonic sensors to enlarge the field of view. In order to compress the information of the three sensors into a single critical distance dcrit(t), we define

$$d_{\rm crit}(t)=\min\{d_{\rm fill}^{(\rm c)}(t),d_{\rm fill}^{(\ell)}(t),d_{\rm fill}^{(\rm r)}(t)\}.\tag{9}$$

Then, the critical distance ensures safe operation of the e-scooter regardless of the desired steering angle, since it denotes always the smallest distance to an obstacle in the e-scooter's field of view, see Fig. 7.

Remark 1. The minimization in (9) is a simple approach to compress the information of the three ultrasonic sensors to a single value for the critical distance. We emphasize that more sophisticated approaches, e.g., using a weighted average of the three distances, are possible and can lead to a more accurate representation of the actual environment. In particular, the combined implementation of a weighted average and the minimum of the distances of all three sensors offers an effective way to include the steering angle in the computation of the critical distance, and, hence, allows the e-scooter to consider only relevant obstacles by ignoring obstacles which are not important for its imminent path. However, we note that the used weighting needs to be carefully chosen to ensure that the e-scooter is able to detect and react to unknown obstacles in time.

## 3.3 Controller Design

For the desired collision avoidance, the maximum distance in which the e-scooter detects obstacles and, hence, reacts to them is denoted by dmax > 0. This threshold defines when the ultrasonic sensors are no longer effective or when the e-scooter no longer needs to react to distant obstacles. Further, we require the e-scooter to decelerate and potentially stop at a predefined safe stopping distance dstop to obstacles, where 0 ≤ dstop *< d*max. The difference between the obtained critical distance dcrit(t) and the stopping distance dstop describes the remaining distance that is left for the e-scooter before reaching the stopping point, see Fig. 8. The goal of the proposed controller is to ensure collision avoidance at all times. Hence, we need to ensure that dcrit(t) > 0 for all t ≥ 0, and, if possible, even dcrit(t) ≥ dstop such that we always have a positive margin to the obstacle or even to the stopping point. In order to fulfill these objectives, we distinguish three different situations depending on the critical distance dcrit(t). Recall

that the collision avoidance is only active if the high-level controller demands the e-scooter to drive forward.

_Procedure 1_. We define the safe velocity as

$$v_{\rm safe}(t)=\min\{\beta_{\rm safe}(d_{\rm crit}(t))v_{\rm cmd}(t),v_{\rm cmd}(t)\}\tag{10}$$
with

$$\beta_{\rm safe}(d_{\rm crit}(t))=\begin{cases}1&\text{if}d_{\rm crit}(t)>d_{\rm max},\\ \frac{d_{\rm crit}(t)-d_{\rm stop}}{d_{\rm max}-d_{\rm stop}}&\text{if}d_{\rm stop}\leq d_{\rm crit}(t)\leq d_{\rm max},\\ 0&\text{if}d_{\rm crit}(t)<d_{\rm stop},\end{cases}$$

where $\beta_{\rm safe}(d_{\rm crit}(t))\in[0,1]$ and the minimization in (10) ensures that active braking of the high-level controller via negative velocities $v_{\rm cmd}(t)<0$ is not affected by the collision avoidance. Then, applying the safe velocity ensures that the e-sector is able to safely stop in front of obstacles such that collisions are avoided at all times.

The different modes of the collision avoidance scheme via the defined βsafe(dcrit(t)) in Procedure 1 are illustrated in Fig. 8 and detailed in the following, where we focus on the case of nonnegative commanded velocities.

Mode 1: dcrit(t) *> d*max. We start with the simplest mode, where the e-scooter is far away from any obstacles. Hence, there is no need to limit the commanded velocity. Thus,
βsafe(dcrit(t)) = 1 leads to vsafe(t) = vcmd(t) ensuring that the controller does not interfere with the velocity chosen by the high-level controller. Consequently, the collision avoidance safety filter is virtually inactive.

Mode 2: dstop ≤ dcrit(t) ≤ dmax. In this case, the e-scooter is still far enough away from the detected obstacle, i.e., at least further away than the defined stopping distance dstop.

However, the sensors detect an obstacle and, therefore, a collision is imminent if the velocity is not adjusted accordingly. Thus, the objective within this distance interval is to ensure that the e-scooter decelerates such that safety can be ensured. This behavior is established through the factor βsafe(dcrit(t)) = dcrit(t)−dstop dmax−dstop
∈ [0, 1], i.e., the applied safe velocity is a simple multiplication of the commanded velocity with a linear scaling depending on the remaining distance to the stopping point.

Mode 3: dcrit(t) *< d*stop.

If the e-scooter is closer to the obstacle than the defined stopping distance dstop, it must stop abruptly to ensure safety. To this end, the safe velocity vsafe(t) is set to zero by βsafe(dcrit(t)) = 0, and, hence, the e-scooter is commanded to stop immediately. We emphasize that the proposed controller structure is a simple and intuitive way to ensure collision avoidance for autonomous vehicles relying only on low-cost ultrasonic sensors and noisy distance measurements. In particular, this design guide should also allow practitioners without expert knowledge in control theory to apply the approach. Therefore, the provided method is suitable for a wide range of applications and users. The resulting behavior of the collision avoidance safety filter can be further improved by using more sophisticated control strategies, e.g., by employing a proportional-integral-derivative controller to ensure that the e-scooter is able to retain a fixed distance to the obstacle, which is left for future work. However, already the introduced simple scheme computes a safe velocity vsafe(t) to ensure that the e-scooter is able to safely stop in front of obstacles such that collisions are avoided at all times (see Section 4 for real-world experiments).

Here, the defined stopping distance dstop is crucial for the resulting safety. It needs to be chosen carefully based on the hardware, the application, and the maximum possible velocity such that the e-scooter is able to detect and react to obstacles in time.

Remark 2. The proposed controller structure is designed to ensure that the e-scooter is able to safely stop in front of obstacles such that collisions are avoided at all times. More precisely, the collision avoidance safely stops the escooter to wait until the obstacle potentially moves away and is, therefore, no longer detected. During this time, the e-scooter may only drive backwards if commanded by the high-level controller, but not if the obstacle is closer to the e-scooter than dstop. This is crucial since the e-scooter cannot detect obstacles behind it, making collision within its blind spots possible. However, our setting can be easily extended to enable safe reverse driving by installing additional perception sensors facing the backwards direction.

## 4. Experiments

In this section, we demonstrate the effectiveness of the proposed collision avoidance safety filter by presenting three real-world experiments. For the first experiment (Section 4.1), we demonstrate the collision avoidance scheme when driving straight with a static obstacle. The second experiment illustrates the proposed framework when approaching obstacles in curves (Section 4.2). The behavior of the e-scooter with the proposed safety filter for moving obstacles is shown in the third experiment (Section 4.3). In all experiments, the e-scooter drives autonomously towards either a static or a moving obstacle, while selfbalancing its upper equilibrium. For the implementation of the proposed collision avoidance safety filter, we choose the stopping distance dstop = 0.5 m and the maximum distance dmax = 2 m below which obstacle measurements are taken into account. For filtering the distance measurements d(k)
meas(t), k ∈ {c*, ℓ,* r}, of the three ultrasonic sensors, we use the time constants Ti = 0.79 s and Td = 0.03 s for increasing and decreasing measurements, respectively. Further, all following plotted velocities are filtered with a moving average filter to remove measurement noise for better interpretability, where we use a window size of 20
samples centered around the current time step. 1

## 4.1 Driving Straight

In the first experiment, we showcase the detection of static obstacles when driving straight. To this end, the performed experiment is set up as follows. The high-level planner commands the e-scooter to drive forward with vcmd(t) = 1 m/s and δcmd(t) = 0. Then, the ultrasonic sensors detect an obstacle such that the e-scooter needs to decelerate and stop in front of the obstacle. To this end, we apply the safe velocity as described in Section 3. The resulting measured distance and velocity of the escooter together with the computed critical distance, the commanded velocity and the safe velocity are shown in Fig. 9. After 6 s of driving straight, the ultrasonic sensors detect an obstacle that is within dmax = 2 m and, thus, the collision avoidance is activated and limits the safe velocity accordingly. The designed controller is able to reduce the velocity of the e-scooter such that it stops safely at the predefined stopping distance dstop. Without our employed collision avoidance safety filter, the e-scooter would collide with the obstacle due to the high level planner not accounting for the obstacle and commanding a forward velocity vcmd(t) > 0. After the obstacle disappears from the e-scooter's path, the e-scooter accelerates again to its commanded velocity vcmd(t) and follows the commands of the high-level planner. We emphasize again that the exponentially smoothing filter is crucial for the successful implementation of the collision avoidance safety filter, as it mitigates the faulty distance measurements of the ultrasonic sensors. As seen in the plot, this comes at the cost of a small delay before acceleration.

## 4.2 Driving Curves

Our second experiment incorporates a curved path of the e-scooter. More precisely, the high-level planner commands the e-scooter to drive forward with vcmd(t) = 0.8 m/s and
δcmd(t) = 0.4 rad. At the same time, the e-scooter needs to avoid any collision with occurring obstacles. Measurements of the resulting e-scooter behavior are depicted in Fig. 10. Here, we omit the measured distances to the obstacle of the individual sensors for better readability, and only show the computed critical distance. For the first 10 s of the experiment, the e-scooter drives in a circle with vcmd(t) and δcmd(t). Then, an obstacle is detected in the range of one of the three ultrasonic sensors, such that the controller adapts the velocity of the e-scooter via the computed safe velocity according to Section 3.3. Although the measured distance to the obstacle is partially faulty, the e-scooter is able to safely stop in front of the obstacle and continues its commanded path after the obstacle moves away. Notably, the e-scooter moves only forward after the obstacle passed all ultrasonic sensors as the critical distance is computed as the minimum of the three filtered distance measurements.

For the third experiment, we consider the case of moving obstacles. The setup is related to the first experiment, but the obstacle is now moving and crosses the e-scooter's path unexpectedly. More precisely, the e-scooter drives forward with vcmd(t) = 0.8 m/s and δcmd(t) = 0. The results of the experiment are shown in Fig. 11. Here, the overall behavior is similar to the experiment in Section 4.1, but the e-scooter has to react to moving obstacles which may be detected only shortly before collision. As illustrated by the measurements, the e-scooter safely stops in front of the obstacle and accelerates after the obstacle has passed the e-scooter's path. After acceleration, the deployed collision avoidance detects another obstacle and safely stops the e-scooter again. Thus, the collision avoidance safety filter allows the escooter to safely navigate in an environment with unknown obstacles, where the proposed approach can be tuned by adjusting the computation of the critical distance according to the specific application.

## 5. Conclusion And Future Work

In this work, we discussed a collision avoidance safety filter for an autonomous e-scooter based on noisy and occasionally missing distance measurements of low-cost ultrasonic sensors. This procedure is particularly useful as an additional safety-component complementing an existing driving velocity controller. The proposed safety filter proved useful to stop in front of obstacles, where the formulated collision avoidance is able to ignore obstacles not blocking the e-scooter's imminent path. Moreover, the provided hardware and software details in this design guide allow for an easy transfer of the cost-efficient solution relying on low-cost ultrasonic sensors to other autonomous vehicles in the micromobility sector. The presented approach is designed such that the tuning is intuitive without requiring an extensive background in control theory. The shown realworld experiments demonstrated the effectiveness of our approach when driving straight as well as driving curves. In future work, we aim to include additional perception sensors, e.g., a camera, to improve the detection of obstacles and to allow for more sophisticated computer vision algorithms. This will allow moving from collision avoidance to obstacle avoidance, i.e., actively evading static and moving obstacles. Note that the presented collision avoidance safety filter will still remain an important feature in this configuration to mitigate potential failures of image processing and dynamic obstacle avoidance schemes. Further, we plan to combine this feature with suitable high-level controllers such as path following algorithms to pave the way for a fully autonomous e-scooter.

## Acknowledgements

We acknowledge the support by the Stuttgart Center for Simulation Science (SimTech). R. Str¨asser, D. Meister, and M. Seidel thank the Graduate Academy of the SC SimTech for its support. F. Br¨andle thanks the International Max Planck Research School for Intelligent Systems (IMPRS- IS) for supporting him.

## References

Borenstein, J. and Koren, Y. (1988).
Obstacle avoidance with
ultrasonic sensors. *IEEE J. Robot. Autom.*, 4(2), 213–218.
Cazzola, P. and Cris, P. (2020).
Good to go? Assessing the
environmental performance of new mobility.
Technical report,
International Transport Forum - Corporate Partnership Board.
Christensen, H., Paz, D., Zhang, H., Meyer, D., Xiang, H., Han, Y.,
Liu, Y., Liang, A., Zhong, Z., and Tang, S. (2021). Autonomous vehicles for micro-mobility. *Auton. Intell. Syst.*, 1, 1–35.
Degele, J., Gorr, A., Haas, K., Kormann, D., Krauss, S., Lipinski,
P., Tenbih, M., Koppenhoefer, C., Fauser, J., and Hertweck, D. (2018).
Identifying e-scooter sharing customer segments using
clustering. In Proc. IEEE Int. Conf. Eng., Technol. & Innov.
Farley, K.X., Aizpuru, M., Wilson, J.M., Daly, C.A., Xerogeanes, J.,
Gottschalk, M.B., and Wagner, E.R. (2020). Estimated incidence of electric scooter injuries in the US from 2014 to 2019. JAMA
Network Open, 3(8), e2014500–e2014500.
Gioldasis, C., Christoforou, Z., and Seidowsky, R. (2021).
Risktaking behaviors of e-scooter users: A survey in Paris. Accident
Anal. & Prevention, 163, 106427.
G¨ossling, S. (2020). Integrating e-scooters in urban transportation:
Problems, policies, and the prospect of system change. Transp.
Res. Part D: Transport and Environ., 79, 102230.
Guglielmi, E. (2023). Modelling and simulation of a smart obstacle
detection sensor for a bike or scooter with model-based design. Ph.D. thesis, Politecnico di Torino.
G¨ossling, S. (2020). Integrating e-scooters in urban transportation:
Problems, policies, and the prospect of system change. Transp. Res. Part D: Transport and Environ., 79, 102230.
Heineke,
K.,
Kloss,
B.,
Scurtu,
D.,
and
Weig,
F.
(2019).
Micromobility's
15,000-mile
checkup.
URL
https://
www.mckinsey.com/industries/automotive-and-assembly/
our-insights/micromobilitys-15000-mile-checkup.
Accessed:
2022-11-02.
Hollingsworth, J., Copeland, B., and Johnson, J.X. (2019). Are escooters polluters? the environmental impacts of shared dockless electric scooters. *Environmental Research Letters*, 14(8), 084031.
Kong, J., Pfeiffer, M., Schildbach, G., and Borrelli, F. (2015).
Kinematic and dynamic vehicle models for autonomous driving control design. In *Proc. IEEE Intell. Vehicles Symp.*, 1094–1099.
Koon,
J.
(2023).
How
many
sensors
for
autonomous
driving?
URL https://semiengineering.com/how-many-sensorsfor-autonomous-driving. Accessed: 2024-03-15.
Krauss, K., Doll, C., and Thigpen, C. (2022). The net sustainability
impact of shared micromobility in six global cities. submitted to:
Case Studies on Transport Policy.
Li, T., Kovaceva, J., and Dozza, M. (2023).
Modeling collision
avoidance maneuvers for micromobility vehicles. *J. Saf. Res.*, 87, 232–243.
Mahony, R.E., Hamel, T., and Pflimlin, J.M. (2008).
Nonlinear
complementary filters on the special orthogonal group.
IEEE
Trans. Autom. Control, 53, 1203–1218.
Manikandan, N. and Kaliyaperumal, G. (2022). Collision avoidance
approaches for autonomous mobile robots to tackle the problem of pedestrians roaming on campus road. *Pattern Recognit. Lett.*,
160, 112–121.
Mehdizadeh, M., Nordfjaern, T., and Kl¨ockner, C.A. (2023). Drunk
or sober? number of alcohol units perceived to be safe before riding e-scooter. *Accident Anal. & Prevention*, 181, 106930.
Rose, J., Schellong, D., Schaetzberger, C., and Hill, J. (2020).
How e-scooters can win a place in urban transport.
URL
https://www.bcg.com/publications/2020/e-scooters-canwin-place-in-urban-transport. Accessed: 2022-11-02.
Soloperto, R., Wenzelburger, P., Meister, D., Scheuble, D., Breidohr, V.S., and Allg¨ower, F. (2021).
A control framework for
autonomous e-scooters. *IFAC-PapersOnLine*, 54(2), 252–258.
Song, K.T., Chen, C.H., and Huang, C.H.C. (2004).
Design and
experimental study of an ultrasonic sensor system for lateral collision avoidance at low speeds. In Proc. IEEE Intell. Vehicles Symp.
Tuncer, S. and Brown, B. (2020). E-scooters on the ground: Lessons
for redesigning urban micro-mobility.
In Proc. Conf. Human
Factors Comput. Syst.
Wenzelburger, P. and Allg¨ower, F. (2020). A first step towards an
autonomously driving e-scooter. Demonstrator Session 21st IFAC World Congress.
Yasin, J.N., Mohamed, S.A.S., Haghbayan, M.H., Heikkonen, J.,
Tenhunen, H., and Plosila, J. (2020). Low-cost ultrasonic based object detection and collision avoidance method for autonomous robots. *Int. J. Inf. Technol.*, 13(1), 97–107.