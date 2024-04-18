# Lr-Fhss Transceiver For Direct-To-Satellite Iot Communications: Design, Implementation, And Verification

Sooyeob Jung, Seongah Jeong, Jinkyu Kang, Gyeongrae Im, Sangjae Lee, Mi-Kyung Oh, Joon Gyu Ryu, and Joonhyuk Kang Abstract—This paper proposes a long range-frequency hopping spread spectrum (LR-FHSS) transceiver design for the Direct-to- Satellite Internet of Things (DtS-IoT) communication system. The DtS-IoT system has recently attracted attention as a promising nonterrestrial network (NTN) solution to provide high-traffic and low-latency data transfer services to IoT devices in global coverage. In particular, this study provides guidelines for the overall DtS-IoT system architecture and design details that conform to the Long Range Wide-Area Network (LoRaWAN) [1]. Furthermore, we also detail various DtS-IoT use cases. Considering the multiple low-Earth orbit (LEO) satellites, we developed the LR-FHSS transceiver to improve system efficiency, which is the first attempt in real satellite communication systems using LR-FHSS. Moreover, as an extension of our previous work [2] with perfect synchronization, we applied a robust synchronization scheme against the Doppler effect and co-channel interference (CCI) caused by LEO satellite channel environments, including signal detection for the simultaneous reception of numerous frequency hopping signals and an enhanced soft-output- Viterbi-algorithm (SOVA) for the header and payload receptions. Lastly, we present proof-of-concept implementation and testbeds using an application-specific integrated circuit (ASIC) chipset and a field-programmable gate array (FPGA) that verify the performance of the proposed LR-FHSS transceiver design of DtS- IoT communication systems. The laboratory test results reveal that the proposed LR-FHSS-based framework with the robust synchronization technique can provide wide coverage, seamless The work of Sooyeob Jung was supported by Institute of Information &
communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) (No.2020-0-00843, Development of low power satellite multiple access core technology based on LEO cubesat for global IoT service).

The work of Seongah Jeong was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No.2023R1A2C2005507).

The work of Jinkyu Kang was supported by the NRF grant funded by the Korea government (MSIT) (No.2021R1F1A1050734).

The work of Joonhyuk Kang was supported by the MSIT, Korea, under the ITRC (Information Technology Research Center) support program (IITP- 2024-2020-0-01787) supervised by the IITP.

Sooyeob Jung is with the School of Electrical Engineering, Korea Advanced Institute of Science and Technology (KAIST), Daejeon 34141, and with the Satellite Communication Infra Research Section, Electronics and Telecommunications Research Institute (ETRI), Daejeon 34129, South Korea (Email: jung2816@kaist.ac.kr).

Seongah Jeong is with the School of Electronics Engineering, Kyungpook National University, Daegu 41566, South Korea (Email: seongah@knu.ac.kr).

Jinkyu Kang is with the Department of Information and Communications Engineering, Myongji University, Gyeonggi-do 17058, South Korea (Email: jkkang@mju.ac.kr).

Gyeongrae Im, Sangjae Lee, Mi-Kyung Oh, and Joon Gyu Ryu are with the Satellite Communication Infra Research Section, ETRI, Daejeon 34129, South Korea (Email: {imgrae, leestrike, ohmik, jgryurt}@etri.re.kr)
Joonhyuk Kang is with the School of Electrical Engineering, KAIST, Daejeon 34141, South Korea (Email: jhkang@ee.kaist.ac.kr).

connectivity, and high throughput communication links for the realization of future sixth-generation (6G) networks.

  Index Terms—Direct-to-Satellite Internet of Things (DtS-IoT),
low-Earth orbit (LEO) satellite, long range-frequency hopping
spread spectrum (LR-FHSS) transceiver, synchronization, detec-
tion.

## I. Introduction

Due to the rapid growth of Internet of Things (IoT), especially with the outbreak of the COVID-19 pandemic, the evolution of fifth-generation (5G) wireless communication networks has accelerated towards future sixth-generation (6G) wireless networks [3]-[6]. Future 6G networks need to meet the new requirements for global coverage and connectivity, as well as high data rates, high reliability, low latency, and energy efficiency, which have attracted attention from existing terrestrial communications. To this end, the development and integration of nonterrestrial networks (NTNs) is indispensable, which has encouraged the revolution of Direct-to- Satellite IoT (DtS-IoT) systems, so-called Internet of Remote Things [7]-[9]. Among the various types of satellites, such as geostationary-Earth orbit (GEO), medium-Earth orbit (MEO), highly-elliptical orbit (HEO) and low-Earth orbit (LEO), LEO satellites are considered the most suitable for future IoT applications due to their low latency, cost-effectiveness, and ease-of-deployment [10].

DtS-IoT offers low dependence on ground base stations as well as simplifies communications to remote areas, especially where deploying terrestrial infrastructure is challenging. To realize a scalable and energy-efficient DtS-IoT system, orthogonal frequency-division multiplexing (OFDM)-based waveforms specified in the third generation partnership project (3GPP) [11] and low-power wide area network (LPWAN) technologies [12]-[15] have been studied. This paper focuses on LPWAN technologies available in the industrial, scientific, and medical (ISM) band that can be used for any purpose without a license in most countries.

To overcome the capacity limitation of existing LPWAN
technologies, which mostly focus on terrestrial IoT communications under LEO satellite channel environments [16]-[19], Semtech [20] has proposed a long range-frequency hopping spread spectrum (LR-FHSS) transmission technology. To the best of our knowledge, there have been only a limited number of studies conducted on LR-FHSS-based LPWAN systems. The existing research [21]-[27] has shown that the LR-FHSS
provides a substantial improvement in capacity compared to other LPWAN transmission schemes, particularly for Long Range (LoRa) communications systems [13]. This demonstrates that the LR-FHSS is well-suited for global coverage of DtS-IoT transmission. Most of the previous works [21]- [25] explore performance analysis in terms of the throughput and the outage probability. This is mainly due to the limited information about the LR-FHSS physical-layer specifications in the LoRaWAN [1].

Our previous work [2] suggests an LR-FHSS transceiver structure that is compliant with the LoRaWAN specifications [1] published by LoRa Alliance and Semtech's application notes [20] as the first trial. The proposed transceiver structure is designed with the perfect synchronization assumption, whose performances are verified in terms of the miss-detection probability and packet error probability (PER). However, actual LEO satellite channel environments involve Doppler effects, symbol timing offset (STO), carrier frequency offset (CFO), phase offset, and co-channel interference (CCI), making synchronization critical for the desired performance of DtS-IoT applications. The design of LR-FHSS-compatible synchronization procedures remains a problem, calling for effective solutions that consider actual LEO satellite impairments. The design complexity of LR-FHSS-compatible synchronization is exacerbated by the fact that the LR-FHSS foresees frequency-hopping channels up to 3120, demanding a specific frequency-hopping pattern for collision avoidance. This adds stress on the optimized design of signal detection, header reception, and payload reception, where the signal detector requires a structure that can simultaneously receive up to 3120 frequency-hopping channels blindly in terms of the frequency and time domains. To approach perfect synchronization, the synchronization algorithm must be designed to overcome the following channel impairment conditions: an initial STO up to 1/4, sampling frequency offset (SFO) up to 80 ppm, CFO up to 5/6 of the symbol rate, Doppler rate up to 400 Hz/sec, and CCI up to 40 percent.

For practicality and reliability, we developed a feasible solution of design and implementation for a robust DtS-IoT communication framework based on an LR-FHSS transceiver against the LEO channel impairments that conforms to the LoRaWAN standards [1]. Specifically, we developed the Gaussian minimum shift keying (GMSK)-based LR-FHSS transceiver including a robust synchronization algorithm with a GMSK symbol mapping scheme suitable for LR-FHSS transmission [2]. Then, based on the proposed LR-FHSS transceiver design, we built a DtS-IoT framework consisting of satellite and ground integrated terminals, LEO satellite payload, and gateway, as illustrated in Fig. 1. The specific contributions of this paper are summarized as follows:

- *Overall DtS-IoT system architecture design*: The system architecture and design details for the DtS-IoT systems with the LR-FHSS transceiver are suggested with various use cases and applications. Considering the multiple satellites in orbit, a standard-compliant LR- FHSS transceiver with LoRaWAN specification [1] was designed to support the high throughput for spectral efficiency. In addition, we explore and analyze the channel impairments that should be considered for LEO satellite communications.
- Robust synchronization algorithm development against
the LEO channel impairments: A robust synchronization algorithm to withstand the LEO channel impairments was developed for LR-FHSS transmission with thousands of frequency hopping channels. Signal detection is included for the simultaneous reception of numerous frequency hopping signals and enhanced soft-output-Viterbialgorithm (SOVA) for the header and payload receptions.
In detail, the specific channel impairments such as an initial STO up to 1/4, SFO up to 80 ppm, CFO up to 5/6 of the symbol rate, Doppler rate up to 400 Hz/sec, and CCI up to 40 percent can be considered.

- *Implementation*: The implementation details of testbeds using an application-specific integrated circuit (ASIC)
chipset and a field-programmable gate array (FPGA) are illustrated for verification. Laboratory test results reveal that the proposed LR-FHSS transceiver design can provide robustness against the Doppler effect and CCI caused by LEO satellite channel environments, enabling wide coverage, seamless connectivity and high throughput communication links for future 6G networks. In particular, DtS-IoT systems with unslotted and slotted Aloha multiple access schemes support throughputs of over 0.18 and 0.37, respectively. To the best of our knowledge, this is the first proposal for realizing an LEO satellite communication system using LR-FHSS. Moreover, by presenting the expected DtS-IoT use cases with the corresponding key performance indicators (KPIs), we can guide the readers in developing the DtS-IoT system.

The remainder of this paper is organized as follows. Section II introduces related works and suggests the proposed DtS- IoT system architecture with potential use cases. The robust synchronization algorithm for the LR-FHSS transmission is detailed in Section III. In Section IV, implementation and testbeds to integrate the system components are described, whose performances are verified via laboratory tests. Finally, conclusions and future works are summarized in Section V.

## Ii. Dts-Iot System Architecture Design

In this section, we establish the overall system architecture for DtS-IoT communication based on an LR-FHSS transceiver and the potential DtS-IoT use cases with the associated KPIs. In addition, to achieve the quality of service (QoS) of DtS-IoT communications, we explore the challenging issues that must be addressed.

## A. Previous Works

Due to the limited availability of information on the LR-
FHSS physical-layer in the LoRaWAN specifications [1], only a few studies have been conducted: [2], [21]-[27]. Most of them [21]-[24] mainly focus on throughput and outage probabilities. In particular, [21] compares the network capacity performance of LR-FHSS and LoRa under no fading channel conditions. In [22], the success probability for packet delivery is mathematically investigated under noise-free channel conditions, including path-loss and Rician fading in LR-FHSS systems. Maleki *et al.* [23] derive a closed-form expression for outage probability under realistic channel conditions, considering path-loss and Nakagami-m fading. Furthermore, [24] explores a shadowed-Rician fading model, resembling the actual satellite channel, to analyze the outage probability of device-to-device-aided LR-FHSS schemes. In [21]- [24], the suitability of LR-FHSS for DtS-IoT transmission is demonstrated, showcasing significant capacity improvements compared to LPWAN transmission schemes. Recently, several signal detection techniques have been proposed based on the LR-FHSS physical layer: [25]-[27]. Fraire *et al.* [25] developed the heuristic headerless signal detection method based on the integer linear program for extreme conditions. In [26], the interference blanking technique is suggested to increase the number of LR-FHSS signals received simultaneously. In addition, [27] proposes a new method to dynamically adjust the frequency hopping sequence and improve the reception rate of LR-FHSS by developing a reception algorithm. However, [25]-[27] only deal with signal detectors, which are part of the overall receiver, and perform algorithm verification in an imperfect LEO satellite channel environment.

In our previous work [2], a novel transceiver design is proposed for LR-FHSS-based DtS-IoT systems. The header reception is assumed to be possible via header repetition, as in the standard [1], since LR-FHSS networks can manage the collision rate among multiple end devices (EDs). Specifically, [2] proposes a transmitter structure based on the standardized physical-layer specifications of LoRaWAN [1] by modifying the preamble insertion introduced incorrectly in the existing LR-FHSS studies [21]-[24] and developing the new time-onair (TOA) calculation. Moreover, for the first time, besides commercial products, we designed the receiver structure with blind LR-FHSS that can simultaneously receive up to 3120 frequency hopping channels, which can be mixed in terms of the frequency and time domains.

B. Overall System Architecture and Potential Use Cases For end-to-end transmission, the DtS-IoT system, in general, consists of the terminal that collects data from IoT sensors and transmits it to the satellite via uplink, the LEO satellite payload that stores data transmitted from the terminal and transmits it to the gateway via downlink, and the gateway that receives data from the LEO satellite payload and processes it. The goal of the DtS-IoT system is to support seamless data delivery services with global coverage and connectivity. Currently, only high-latency services can be supported through multiple LEO satellites operating in orbit. In the near future, satellite operators such as SpaceX, Amazon, and Telesat [10] plan to support low-latency and seamless services by launching thousands of LEO satellites, installing multiple ground base stations or establishing inter-satellite links. The ultimate aim of DtS-IoT communications is to develop a waveform dedicated to LEO satellite communication that can support high throughput. LR-FHSS transmission technology has recently been proposed by Semtech [20] that has a high network capacity and collision robustness in long-range and largescale communication scenarios. In this paper, we construct a comprehensive DtS-IoT system using LR-FHSS transmission and reception, and then explain the roles and interfaces of essential components in detail.

Fig. 1 shows the overall DtS-IoT system architecture, which is composed of the satellite and ground integrated terminal, LEO satellite payload and gateway, with the LR-FHSS transmission and reception. First, the satellite and ground integrated terminals receive the data collected from the multiple IoT sensors for various use cases, such as environmental monitoring, smart grid, transport logistics, smart city, and smart terleaving N*coded* bits)
ED3
ED2
terleaving (80 bits)
ED1

ynchronizer
Viterbi 
decoding
CRC8
check
Header
SOVA
Deinter
leaving
PHDR
Payload
SOVA
Deinter
leaving
Viterbi 
decoding
CRC16
check
Payload
Payload decoder
Channel 
output

farm [28]-[31]. Through the sensor interface and monitoring and control unit (MCU) modules in the terminal, the collected data is transmitted to the LEO satellite payload from the ASIC- based LR-FHSS transmitter in the ultra high frequency (UHF) band, i.e., 940 MHz. This frequency band can be selected by considering the output power and channel occupancy time in the unlicensed band. It also includes the module for the LoRa transmission and reception to link the ground gateway and server. In the LEO satellite payload, which is composed of the user link and feeder link onboard processors (OBPs), onboard computer (OBC), and global positioning system (GPS), the data transmitted from the satellite and ground integrated terminals is demodulated by the FPGA-based LR-FHSS receiver in the user link OBP. The demodulated data is stored in the OBC, while the LEO satellite payload flies in the predetermined orbit until it can communicate with the gateway. When the connection with the gateway is possible, the stored data is transferred from the feeder link OBP to the gateway in the S-band for high-speed data transfer. For data transmission on the feeder link, the telemetry (TM) and telecommand (TC) modem, i.e., CORTEX CRT modem, can be applied between the LEO satellite payload and the gateway. In the gateway, the network management system (NMS) receives the demodulated data from the TM and TC modem via ethernet and processes it in the network protocol module. The network protocol module can receive the collected data and send and receive TM and TC messages, while sending beacon setting information. Also, the satellite and terminal management module can manage and store satellite and terminal information of the DtS-IoT. Ultimately, the IoT data stored in the gateway can be used depending on the application, e.g., to predict marine climate through machine learning-based big data analysis.

According to the utilization of collected IoT data, target use cases with their respective KPIs are summarized in Table I [28]-[31]. The requirements of the use cases are defined in the same way as the European telecommunications standards institute (ETSI) technical report (TR) 103 435 [28] in terms of data rate, power, and latency. For data rate, environmental monitoring, smart grid, transport logistics and smart farm that require simple IoT data collection can support low data rates of 1 kbps or less. However, smart cities require complex processing of data collected from various IoT terminals, requiring high data rates of up to 10 kbps. In terms of power consumption, IoT terminals equipped with portable batteries require low power in all use cases, as power is supplied at approximately 30 volts or less. Latency is not an important factor for environmental monitoring and smart farms which require long-term data collection. For example, environmental monitoring can be used to measure air quality, soil quality, ocean conditions, and animal tracking, which requires high hardware environmental resistance to factors such as temperature and humidity, fully functional GPS, and energy harvesting capabilities. Smart farms use IoT terminals for water pump control, sensors for oxygen, temperature and humidity, hydraulic valves, and level meters; therefore, their latencies must be quite relaxed, or between a few seconds and a few minutes. Conversely, the remaining use cases utilize IoT data in urgent situations of short-or mid-term, thus requiring

| Use Cases     | Data rate   | Power         |
|---------------|-------------|---------------|
| Environmental |             |               |
| monitoring    |             |               |
| ≤             |             |               |
| 1             |             |               |
| kbps          | Low         | Quite relaxed |
| Smart         |             |               |
| grid          |             |               |
| ≤             |             |               |
| 1             |             |               |
| kbps          | Low         |               |
| 100           |             |               |
| ∼             |             |               |
| 1000          |             |               |
| ms            |             |               |
| Transport     |             |               |
| logistics     |             |               |
| ≤             |             |               |
| 1             |             |               |
| kbps          | Low         |               |
| 100           |             |               |
| ∼             |             |               |
| 1000          |             |               |
| ms            |             |               |
| Smart         |             |               |
| city          |             |               |
| ≤             |             |               |
| 10            |             |               |
| kbps          | Low         |               |
| 100           |             |               |
| ∼             |             |               |
| 1000          |             |               |
| ms            |             |               |
| Smart         |             |               |
| farm          |             |               |
| ≤             |             |               |
| 1             |             |               |
| kbps          | Low         |               |
| Few seconds   |             |               |
| ∼             |             |               |
| minutes       |             |               |

ED3
ED2
ED1
a latency of 100 ms to 1000 ms. The smart grid uses IoT as a fault passage indicator, low voltage sensors, transformer status monitoring and alarm detection. Transport logistics uses the technology to support contents such as shipment tracking sensors, microprocessors, wireless connectivity, and minuscule identification devices. For smart cities, it supports the content such as the traffic counting detectors, inductive loop detectors for vehicle identification, highly accurate GPS and sensors for CO2, fog, and ultrasonic monitoring.

## C. Lr-Fhss Transceiver Design

Fig. 2 shows a block diagram of the LR-FHSS transmission with the LEO satellite channel model. Since the details of the LR-FHSS transmitter design, including the header and payload transmission through frequency hopping, is introduced in our previous work [2], here, we briefly summarize the major components. By applying GMSK symbol mapping suitable for LR-FHSS, the hopping blocks of 114 symbols for header fragments and 50 symbols for payload fragments are generated. In the LR-FHSS transmitter output, a total of NH +NF hopping blocks, considering the number of header replicas NH with the header duration TH and the number of payload fragments NF with the payload duration TF , are transmitted by switching frequency channels based on the hopping channel and pattern. In Fig. 2, the header and payload fragments, the outputs of

| Impairments                                             | Solutions                                 |
|---------------------------------------------------------|-------------------------------------------|
| Doppler                                                 |                                           |
| effect                                                  |                                           |
| comparison of the several Doppler candidates (11 can-   |                                           |
| didates in this paper), Doppler tracking in header SOVA |                                           |
| STO                                                     | Symbol timing estimation using a syncword |
| CFO                                                     |                                           |
| Coarse CFO estimation in signal detection, fine CFO     |                                           |
| estimation, CFO tracking in header SOVA                 |                                           |
| Phase                                                   |                                           |
| offset                                                  |                                           |
| Phase estimation, phase tracking in header SOVA         |                                           |
| CCI                                                     |                                           |
| Interleaving,                                           | convolutional encoding,                   |
| ping                                                    |                                           |
| Signal                                                  |                                           |
| detection                                               |                                           |
| Signal detection in frequency domain                    |                                           |
| Time                                                    |                                           |
| difference                                              |                                           |
| Signal detection in frequency domain                    |                                           |

three EDs, are simultaneously transferred in the frequencytime domain using frequency hopping. In LR-FHSS networks, the collision rate between the multiple EDs can be reduced by managing the spectrum used by each ED. To efficiently operate DtS-IoT communication systems, the LR-FHSS network needs to allocate a clean spectrum for EDs with a high QoS or with low transmit power. For example, supposing that ED1 transfers the LR-FHSS signal to require less transmit power and a higher QoS than ED2 and ED3, the overlapped frequency band for ED2 and ED3 as well as the clean frequency band for ED1 can be allocated.

The LR-FHSS receiver structure consisting of signal detection and decoding blocks is proposed in [2] with perfect synchronization. The design of the LR-FHSS compatible synchronization procedure remains an open problem, which is inevitable in real applications, but challenging for implementation. In this paper, we suggest a novel transceiver structure including the robust synchronization algorithm to compensate for actual LEO satellite channel effects, such as the Doppler effect, STO, CFO, phase offset, and CCI, which is explained in detail in Sec. III.

## D. Challenging Issues

In this section, we provide an overview of the challenging issues encountered during the implementation of the LR- FHSS-based DtS-IoT system, and possible solutions to these challenges are proposed in Table II.

1) Doppler Effect: In LEO satellite communications, significant and time-variant frequency shifts can occur due to the Doppler effect, depending on factors such as carrier frequency, satellite altitude, orbit, and coverage assigned to each LEO satellite [16]-[19]. The Doppler effect has a notable impact on coherent demodulation, necessitating compensation for reliable communications. As shown in Fig. 2, the Doppler effect can be emulated by considering that the Doppler rate passes through two accumulators. The output of the first accumulator represents a Doppler shift, with the Doppler rate typically affecting the narrowband around 488 Hz. This paper considers Doppler rates up to 400 Hz/sec. Initially, the Doppler effect can be estimated through performance comparison among several Doppler candidates; for instance, our framework employs 11 candidates. Subsequently, Doppler tracking is performed in the header SOVA block.

2) STO: The STO arises from the long-term instabilities of the receiver oscillator, which generates the receiver sampling clock [32]. STO can lead to inter-symbol interference (ISI), significantly degrading reception performance. To address STO in the channel model, SFO is accumulated for each sample and converted to the sampling phase, which is then applied to the LR-FHSS signal via an interpolator, as illustrated in Fig. 2. The precision of the oscillator, typically limited by its cost, is usually capped at a maximum of 10 ppm; for instance, in our architecture, up to 80 ppm is considered. For symbol timing estimation, the initial STO and SFO are estimated through cross-correlation using a syncword.

3) CFO and Phase Offset: The CFO can be attributed to various factors leading to performance degradation, including receiver oscillator instabilities and Doppler effects [32]. CFO alters the frequency of the received signal, potentially causing mismatches and resulting in inter-carrier interference (ICI). By accumulating CFO for each sample, the calculated phase component is applied to the LR-FHSS input considering the Doppler effect. In our proposed framework, we consider CFO compensation up to 5/6 of the symbol rate which can be achieved through several stages, including coarse estimation, fine estimation, and tracking. Similarly to CFO, phase offset can also be compensated for through phase estimation and tracking.

4) CCI: For DtS-IoT systems, the utilization of unslotted Aloha-based multiple access [33] is advantageous for increasing network capacity but can also lead to CCI among multiple EDs. In the channel model, CCI can be introduced alongside noise by randomly selecting the overlapping ratio of hopping blocks from different EDs within the total frame length. Depending on the coding rate, the impact of CCI may vary. In our framework, it is observed that up to 40 percent of hopping block overlaps can occur without encountering an error floor. During frequency hopping transmission, CCI can be mitigated through spectrum management of the LR-FHSS network. However, occasional collisions between LR-FHSS packets can be addressed through interleaving and convolutional encoding. Furthermore, the signal detection block is capable of detecting frequency hopping signals from multiple EDs at different output times [2].

## Iii. Robust Synchronization For Dts-Iot Communications

In this section, we propose the structure of the GMSK-based LR-FHSS receiver, as shown in Fig. 3, which is composed of the signal detector, header receiver, and payload receiver. For receiving the LR-FHSS signal, a robust synchronization algorithm that can withstand real LEO satellite channel environments is essential, whose details and performances are described in the following subsections.

## A. Signal Detector

As shown in Fig. 3, the LR-FHSS signal detector structure is composed of a channelizer, external memory, and header detector. In the signal detector, the channelizer can simultaneously receive up to NCF = 3120 LR-FHSS signals

Frequency priority signal
Chann
elizer
Header 
detector
Time priority signal
CFO 
correct
LPF
Symbol timing 
estimation
Deinterl
Header
SOVA
CRC8
eaver
External 
memory
Payload
buffer
Doppler & 
CFO correct
LPF
Timing 
correct
Deinterl
Payload
SOVA
CRC16
eaver

available in the operating channel width (OCW) of 1523 kHz by using the FFT operation with windowing. The FFT output of the channelizer is transferred to the external memory per frequency bin. The external memory is divided into the memory regions, where the data is stored in both the frequency and time axis. The FFT output corresponds to all frequency signals at one sampling point, which is referred to as the frequency priority signal. First, the frequency priority signal is stored in the corresponding memory region. In the time domain, two oversampled signals for each frequency are stored in the time order, which is called a time priority signal. After header detection, the time priority signal is stored in the corresponding memory region. To detect the header position, the frequency priority signal for each frequency is transferred to the header detector. Using the frequency priority signal, the header detector then makes a detection decision through cross-correlation. In the header detector, we can estimate the header position corresponding to the sampling point and the channel information corresponding to the frequency hopping channel. In addition, the coarse CFO can be estimated with a resolution of 976/FFT size Hz. The header position information obtained from the header detector is then transferred to external memory.

## B. Header Receiver

After detecting the LR-FHSS signal, the header receiver performs synchronization and header decoding using the frequency priority signal with the header detect information. As shown in Fig. 3, the header receiver is composed of blocks for synchronization, such as the symbol timing estimation, phase rotate, and the CFO and phase estimation, and blocks for header decoding, such as the header SOVA, deinterleaver, Viterbi decoder, CRC8 and header decoder.

1) Symbol Timing Estimation: For the symbol timing estimation, a header signal sequentially passed through the CFO correct and low-pass filter (LPF) blocks is the input. In the CFO correct block, the coarse CFO estimated by the signal detector is compensated in the header, and the noise outside

Header detect information
Payload information
CFO & Phase 
estimation
Timing 
correct
Phase 
rotate
Header 
receiver
Viterbi 
decoder
Header 
decoder
CFO & Phase 
estimation
Phase 
rotate
Dewhitener
Viterbi 
decoder

the signal band is removed in the LPF. The filtered input signal enables precise estimation of STO, which causes ISI.

In the symbol timing estimation block, we determine the STO using the syncword information embedded in the 114- symbol header. The STO is generated by a change in sampling phase due to accumulated SFO. Specifically, the crosscorrelation of sample timings is calculated before and after one symbol and an accurate sampling phase is obtained by comparing the magnitude squared values of the cross-correlation. This block utilizes two oversampled signal inputs and syncwordbased correlator coefficients. The estimated sampling phase is then corrected in an interpolator.

Since the GMSK signal having a constant amplitude changes only the phase component, the STO can be estimated accurately when the phase difference between the symbol intervals is sufficiently large [34]. Fig. 4(a) shows the phase change of the syncword with the full length of 32 symbols, and there is little phase change in some regions around the phase of 0◦. When all syncword symbols are used, the performance of the symbol timing estimation is degraded. Therefore, in our framework, the cross-correlation using 20 symbols in the {5,
6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24,
25, 26}-th positions among the 32 total symbols is applied, where these 20 symbols show a large phase difference, as shown in Fig. 4(b). In this study, the maximum frequency tolerance of 31 kHz implies a frequency error of about 33 ppm for a 940 MHz carrier frequency. Assuming the maximum symbol frequency error of 66 ppm between the LR-FHSS transmitter and receiver for a total of 2714 symbols, derived from 52 payload blocks and 1 header block in the case of the longest packet, the last symbol in the packet results in a timing error of approximately 0.18 symbol length. Fig. 5 shows that the standard deviation of the proposed symbol timing estimation corresponds to a sufficient performance within 0.1 symbol less than 0.18 symbol at the SNR of 5 dB; this SNR
supports the PER of 10−2 in the LR-FHSS packet transmission under AWGN [2]. In addition, it shows a performance gap of about 1 dB depending on the Doppler rate from 0 to 400 Hz/sec. This performance error indicates that symbol timing estimation using syncword is accurate; therefore, additional symbol timing tracking blocks can be omitted.

2) Phase Rotate: The phase of the GMSK signal has a contribution of ±90◦ from each symbol as a function of the previous transmitted symbol. For soft bit calculation through Trellis search [35], [36], eight Trellis states are required when transmitting binary symbols. If the phase of each symbol is accumulated and adjusted by ±90◦, the phase state by the previous symbol becomes {0◦, 180◦} for an even number of symbols and {−90◦, 90◦} for an odd number of symbols.

Finally, four Trellis states can be obtained through phase rotation. The process for the phase rotate can be expressed as,

i aiq (t − iTs), (1) ϕ (t, a) = �
where q(t) is the phase pulse, ai is the information bit of
±1, and Ts is the period of the input symbol. As shown in Fig. 6, the phase pulse becomes 90◦ after a sufficient time.

If the equation (1) is divided into the input symbols having a response of π/2 and having a response of a phase shift interval, (1) can be reformulated as,

ϕ (t, a) = 2 i=0 ai. (2) i=k−1 aiq (t − iTs) + π k−2 � k �
Here, the two symbols are used as the length of the phase transition section. The first term of the equation (2) is determined from the latest two symbols of {ak−1, ak}, and the second term is obtained by the accumulated values from the first symbol to the symbol of ak−2.

From (2), the number of Trellis states for the Viterbi detector is two for the first term and four for the second term, the total of which is eight because each of the four phases has two states. To reduce the number of Trellis states for lowcomplexity [36], by adding π
2 (k − 2) to (2), we have

φ (t, a) = ϕ (t, a) + π 2 (k − 2) = i=k−1 aiq (t − iTs) + π k � k−2 � i=0 �ai, (3)
where �ai is defined as 1 for ai = 1 and 0 for ai = −1.

By using (3), we can reduce the number of Trellis states to four. When the channel noise is independent between symbols, the operation of changing the phase of the received signal by
π
2 (k − 2) does not affect the characteristics of noise;
therefore, there is no change in reception performance due to this operation. The forward and backward Trellis searches using (3) are shown in Fig. 7, where bk is defined as

bk = k−2 � i=0 �ai and �bk = bk mod 2. (4)
When denoting the received baseband signal as rk, the path metric in each state s of the Trellis search is calculated as

λ(s) k = max t∈S � λ(t) k−1 + Re � rk · ej(k π 2 −φp(k−1)−φ(kTs,a(s)))�� , (5)
where S is the set of the previous states transitioning to state s, φp (k) is the phase of the channel estimation, and a(s) is a sequence of symbols transitioning to state s.

3) CFO & Phase Estimation: This block estimates the CFO and phase using the syncword information of the header.

First, the phase estimation φp (k) is calculated by the crosscorrelation between the filter coefficient ck and the input signal rk, which is given as φp (k) = tan−1 ��N−1
k=0 ckrk
�
, where

$\left(\tilde{b}_{k-2},a_{k-1}\right)$.

$\left(1,-1\right)$$\left(1,-1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$$\left(1,+1\right)$\(\left(1,+1\right
ck = [c0, c1, · · · *, c*N−1] are the filter coefficients based on the synchronous word of the hexadecimal 0x2C0F7995.

For the CFO estimation, the result of M-point FFT operation with windowing of the length N can be written as Xm = �N−1
k=0 ckrke−j2πkm/M, from which we can derive the power spectral estimation Pm = |Xm|2. By finding the peak value of Pm in time, we can estimate the exact CFO
φf (k). The estimated CFO and phase values are transferred to the header SOVA block to compensate for the phase of the previous channel estimation φp (k − 1) in the Trellis search.

4) Header SOVA: GMSK signals allow ISI to increase frequency efficiency, and the Viterbi detector, a type of sequence detector, is often used in receivers to minimize performance degradation due to ISI. The performance and complexity of the Viterbi detector are mainly determined by the number of states in the state transition diagram represented by Trellis and the method of calculating branch metrics. Methods to minimize the number of states in Trellis have been proposed in several studies [35], [36]. First, there is a method that considers only the part with large interference between symbols and a decision feedback method that determines a part of the estimated signal using detected past symbols [35]. There is also a method that uses terms with large weights by approximating to a pulse amplitude modulation (PAM) signal [35], [36]. This paper applies the SOVA method that outputs soft decision values based on the Viterbi state transition diagram, which considers only the large interference between symbols. Here, soft decision values containing reliability information of the received signal are provided to improve error correction decoding performance. In addition, considering the characteristics of LR-FHSS frame data, we propose an enhanced SOVA scheme that performs both forward and backward Trellis searches while reflecting the tracking results of phase φp, CFO φf and Doppler rate φdr.

In the proposed framework, the header data containing LR-FHSS transmission information is demodulated with high accuracy by using the proposed SOVA method. Particularly, in the header SOVA block, both forward and backward Trellis searches are performed to cope with rapidly changing channel responses due to frequency hopping in the narrowband of 488 Hz. For two sets of the candidate Doppler rates, the forward and backward Trellis searches are utilized from the middle of the header to the last signal, e.g., here, [58:114] symbols, and from the middle [1:57] symbols of a header to the first signal, Fig. 8: Phase variations of header signal according to the Doppler rate.

respectively. As a result, the header SOVA block outputs the soft bit sequences in the forward and backward Trellis search with each Doppler rate candidate. Finally, the three soft bit sequences with the best path metrics are selected.

Fig. 8 shows the phase variations of the header signal according to the Doppler rates of {50, 100, 200, 300, 400}
Hz/sec. A phase shift of about 900◦ is required at a Doppler rate of 400 Hz/sec to make the frequency error zero at the midpoint of the header of 114 symbols. If the Doppler rate is estimated by using the syncword in the middle position of the header, the phase change of the syncword is not large at the Doppler rate of 50 Hz/sec. That is, it is difficult to improve the accuracy of the Doppler rate estimation using syncword. Therefore, the header SOVA scheme is applied with the comparison of the expected Doppler rate candidates, where the header SOVA performs the Trellis search with each Doppler rate candidate. The estimation accuracy of each Doppler rate candidate value is determined by using the bit error rate (BER)
after all header bits are demodulated. We consider 11 candidate Doppler rates of {0, ±80, ±160, ±240, ±320, ±400} Hz/sec.

For each state in the SOVA scheme, the path selection is performed based on the branch metric bmi, path metric pmi and phase of the previous channel estimation φp (k − 1) for i *∈ {*0, 1}, as shown in Fig. 9(a). First, the path metrics are calculated by sequentially compensating the branch metric and the phase of the channel estimation to the input signal. From the two paths connected by each Trellis state, the path with the smaller newly calculated path metric is selected in the path selection *path sel*. The difference between the two path metrics *pm diff* is used for soft bit calculation. To track the phase φp, CFO φf and Doppler rate φdr, the phase error of the signal *perr*i, for i *∈ {*0, 1}, is transferred to the calculator of the channel estimation, as shown in Fig. 9(b).

The *perr*i is used as an input for the tracking loop, where ua, ub and uc are the coefficients for the phase tracking of the channel estimation, CFO tracking, and Doppler rate tracking, respectively. By these definitions, we can track the phase φp, CFO φf and Doppler rate φdr as, Convolutional AWGN
Cochannel interference Symbol Header decoding CRC8
check demapping Deinter leaving fragments Convolutional AWGN
Cochannel interference Symbol 
(6)
decoding CRC8
check demapping Deinter leaving LR-FHSS 
signal


 LR-FHSS 
φdr (k) = φdr (k − 1) + uc · perri,
φds (k) = �
signal Convolutional 

Symbol Doppler Signal detector

k φdr (k),
φf (k) = φf (k − 1) + ub · perri,
φp (k) = φp (k − 1) + φds (k) + φf (k) + ua · perri, Symbol Synchronizer Acc.

Acc.

decoding demapping Deinter leaving rate timing offset Convolutional Symbol Doppler Signal detector Payload fragments Symbol Synchronizer Acc.

Acc.

decoding demapping Deinter leaving rate timing offset Payload fragments Payload decoder Payload decoder Random hopping AWGN
Cochannel interference block selection Random hopping AWGN
Cochannel interference block selection Interf. SNR


               1
               0
               1
               0
SNR

Interf. SNR



               1
               0
               1
               0
SNR

 LR-FHSS 

Interpo



signal

lator



 LR-FHSS 

Interpo

Doppler 



signal

lator



Acc.

Acc.

rate

Symbol timing offset

Doppler 

Acc.

Acc.

rate

Symbol timing offset

Synchronizer

Synchronizer

CFO

Interpo

CFO & Phase 

Header 
fragment

recovery

lator

estimation

Header
SOVA

The best
3 soft bit
sequences

CFO

Interpo

CFO & Phase 

Header 
fragment

recovery

lator

estimation

Header
SOVA

The best
3 soft bit
sequences

Forward  

Symbol 
timing 

Trellis search

estimation

Forward  

Symbol 
timing 

Backward  

Trellis search

estimation

Trellis search

11 Doppler 

rate candidates

Backward  

Doppler estimation

Trellis search

11 Doppler 

rate candidates

Doppler estimation

where φds is the Doppler shift: the cumulative value of the
Doppler rate. In the Trellis search, the bit value of the selected
state is stored as the most recent hard bit in the survival path
when a new path metric is selected. The pm diff is stored
as the most recent soft bit in the survival path of the selected
path. The hard and soft information for the previous 32 bits
are stored and updated with 32 length of the survival path. If
more than 32 signals are the input, the oldest soft bit value of
the state with the smallest path metric among the 4 states is
chosen as the output.
  Fig. 10 shows the distribution of the reception errors when
using the forward Trellis search and both forward and back-
ward Trellis searches. The error distribution is measured when
the payload of 100 bytes is sent 100 times. An issue with
the forward Trellis search method is that most errors are
concentrated in the front part of the frame, as shown in Fig.
10(a). As shown in Fig. 10(b), both forward and backward
Trellis searches distribute the errors to the entire frame, which
reduces the PER through the error correction code.
  5) Deinterleaver: The interleaver distributes bits within the
length of the header bits to effectively correct bit errors caused
by burst noise in the receiver. When reading three soft bit
sequences from the header SOVA block, the soft bit sequences
are read in the deinterleaving order to recover the original
transmission bit order as follows: {1, 18, 26, 34, 42, 50, 58,
66, 73, 2, 10, 27, 35, 43, 51, 59, 67, 74, 3, 11, 19, 36, 44, 52,
60, 68, 75, 4, 12, 20, 28, 45, 53, 61, 69, 76, 5, 13, 21, 29, 37,
54, 62, 70, 77, 6, 14, 22, 30, 38, 46, 63, 71, 78, 7, 15, 23, 31,
39, 47, 55, 72, 79, 8, 16, 24, 32, 40, 48, 56, 64, 80, 9, 17, 25,
33, 41, 49, 57, 65}.

6) Viterbi Decoder: The Viterbi decoder for header decoding with the code rate 1/2 has 64 states, and the operation in each state is performed, as shown in Fig. 11. The *llr a* and llr b are the soft bits indicating the reliability of encoded bits, the s0 and s1 are previous states transitioning to the current state s, the a0 and a1 are two coded bits output when transitioning from state s0 to state s, and the b0 and b1 are two coded bits output when transitioning from state s1 to state s. The pm[s0], pm[s1], and pm[s] are path metrics in states s0, s1, and s, respectively, and the process of finding the state transition path that maximizes path metrics is the operation of the Viterbi decoder. Among the two paths transitioned from states s0 and s1, the state transition path with the larger path metric is selected, and the data bit corresponding to the selected path is added as a new bit to the survival path register in state s. After the data bits of 40 length are input twice for demodulation of the encoding bits, the final state information is obtained with the oldest data 6 bits of the survival path register stored in the state with the largest path metric among the 64 states.

7) CRC8: The CRC8 block calculates the cyclic redundancy check (CRC) to detect the bit errors of the received header data. If the register value becomes 0 after all header bits, including the CRC of 8 bit, are entered in the CRC8 block, it is determined that there is no bit error.

8) Header Decoder: After the CRC8 check, the header decoder can obtain the payload information necessary for receiving the payload from the header data received without the error. This payload information is transferred to external memory. From the payload information, we can find the location of the entire payload stored in the external memory.

C. Payload Receiver In the payload receiver, the payload data stored in the payload buffer passes through the blocks for synchronization and payload decoding. For synchronization of the payload data, the estimation results, such as the Doppler rate, CFO and STO, obtained in the header receiver are reused to synchronize the payload.

1) Payload Buffer: In the payload buffer, the payload data to be demodulated is read with the payload information from the external memory, and is transferred to the synchronization block in units of hopping blocks. The payload information, which contains the channel/hopping sequence in the header, is used to output the payload data in units of hopping blocks. In the synchronization block, the estimation results, such as the Doppler rate, CFO and STO, obtained in the header receiver are reused to synchronize the payload. In addition, the phase rotate, CFO, and phase estimation blocks are performed the same as in the header receiver for the payload SOVA.

2) Payload SOVA: The input of the payload SOVA block is the synchronized payload data in hopping block units. To obtain the soft bits from the GMSK-based payload fragments, the Trellis search with 4 states is applied for the payload demodulation. The payload SOVA has the same role as the header SOVA. However, the length of the input signal is 50 symbols for the payload fragment, unlike the 114 symbols for the header fragment.

3) Deinterleaver: In the LR-FHSS transmitter, the input soft bits of the payload are sequentially increased by 48, and a total of n blocks are stored in memory. Conversely, the output soft bit is read from memory by adding 48 from the initial address 0. For deinterleaving, the data is read in the order of input soft bits, and is repeated until all soft bits of n blocks are read.

4) Viterbi Decoder: The code rates of 1/2, 2/3, and 5/6
are created by puncturing the convolutional code with the code rate of 1/3 as the mother code. The Viterbi decoder performs the decoding process by filling the punctured bits with 0 according to each code rate, that is, depuncturing the bits. The Viterbi decoder for the payload works the same as the Viterbi decoder for the header.

5) CRC16: To detect the payload bit errors, the CRC
calculation is performed identically to the CRC16 of the transmitter. The input bits are collected into bytes in most significant bit (MSB) order and fed into the same circuitry as the CRC16 of the transmitter. After calculating all of the payload data, the value of the shift register is compared with the received 16 bit CRC parity bit. Then, if it is the same as CRC16 parity bit, it is determined to be received without the error.

## D. Simulation Results To Validate The Proposed Lr-Fhss Transceiver Algorithm, The Per Performance Of Lr-Fhss Transmission Was Evaluated

| Parameters                            | Values   |
|---------------------------------------|----------|
| Carrier frequency                     |          |
| f                                     |          |
| c                                     |          |
| 940 MHz                               |          |
| Number of header replicas             |          |
| N                                     |          |
| H                                     |          |
| {                                     |          |
| 3, 2                                  |          |
| }                                     |          |
| Number of payload fragments           |          |
| N                                     |          |
| F                                     |          |
| {                                     |          |
| 18, 9                                 |          |
| }                                     |          |
| Header duration                       |          |
| T                                     |          |
| H                                     |          |
| 233.472 ms                            |          |
| Payload duration                      |          |
| T                                     |          |
| F                                     |          |
| 102.4 ms                              |          |
| OCW                                   | 39 kHz   |
| Grid                                  | 3.9 kHz  |
| Maximum payload size                  |          |
| L                                     |          |
| 32 bytes                              |          |
| Coding rate                           |          |
| r                                     |          |
| {                                     |          |
| 1/3, 2/3                              |          |
| }                                     |          |
| Number of channels for hopping        |          |
| N                                     |          |
| CF                                    |          |
| 80                                    |          |
| Number of channels for hopping per ED |          |
| N                                     |          |
| CF/ED                                 |          |
| 10                                    |          |
| Initial STO                           |          |
| {                                     |          |
| 0, 1/8, 1/4                           |          |
| }                                     |          |
| SFO                                   |          |
| {                                     |          |
| 0                                     |          |
| ∼                                     |          |
| 80                                    |          |
| }                                     |          |
| ppm                                   |          |
| CFO                                   |          |
| {                                     |          |
| 0                                     |          |
| ∼                                     |          |
| 5/6                                   |          |
| }                                     |          |
| Doppler rate                          |          |
| {                                     |          |
| 0                                     |          |
| ∼                                     |          |
| 400                                   |          |
| }                                     |          |
| Hz/sec                                |          |
| CCI                                   |          |
| {                                     |          |
| 0                                     |          |
| ∼                                     |          |
| 60                                    |          |
| }                                     |          |
| %                                     |          |

under actual LEO satellite channel effects. The simulation parameters are summarized in Table III [2], [24]. The LEO satellite channel effects were considered as follows: the values for the initial STO as {0, 1/8, 1/4}, for SFO as {0, 20, 60,
80} ppm, for CFO as {0, 1/6, 3/6, 5/6}, for Doppler rate as {0, 320, 400} Hz/sec, and for CCI as {0, 4, 12, 20, 40, 60}%. The PER performance of the header with r = 1/2
and payload with r = 1/3 and 2/3 was measured under the AWGN environment, serving as a reference performance for comparing the performance degradation effects caused by the LEO satellite channel model.

Fig. 12 shows the PER performance of the LR-FHSS signal according to the initial STO and SFO, which occurs due to the long-term instabilities of the receiver oscillator. As shown in Fig. 12(a), the simulation was performed at r = 1/3 and 2/3, and the PER performance at the initial STO of 0 was identical to that in the AWGN environment. According to the initial STO, the PERs at r = 1/3 make little performance difference, while the performance difference of 1 dB at a PER
of 10−3 is observed at r = 2/3 due to the low coding gain.

Fig. 12(b) shows the PER performance of the LR-FHSS signal for the different SFOs. As SFO increases, the PER gradually rises due to the increased timing errors in the last symbol of the packet. The performance of the proposed symbol timing estimation block is verified, showing only a slight gap of 0.5 dB compared to the reference performance.

Fig. 13(a) illustrates the PER performance of the LR-
FHSS signal under different CFOs. There is no difference between the performances according to CFO and the reference performance, indicating that the CFO compensation block consisting of coarse estimation, fine estimation, and tracking blocks nearly compensates the CFO. Fig. 13(b) shows the PER performance of the LR-FHSS signal with different Doppler rates. At r = 2/3, there is little performance difference according to the Doppler rates, while, at r = 1/3, the performance difference occurs about 0.5 dB. The performance degradation at r = 1/3 may be caused by miss detection in the signal detector because the signal detector of the GMSK-based LR-FHSS are affected by the Doppler rate.

Fig. 14 illustrates the PER performance of the LR-FHSS
signal as affected by CCI. The simulation was performed by inputting the number of hopping blocks in which the CCI occurs as a percentage. At r = 1/3 and 2/3, the CCIs of {20, 40,
60}% and {4, 12, 20}% were applied, respectively. Since the impact of the CCI on PER performance is different depending on the coding rate, the different interference percentages were applied for each code rate. As a result, for r = 1/3, the error floor starts at Es/No of 8 dB under CCI conditions of 40% or more, while, for r = 2/3, the error floor starts at Es/No of 8 dB under the CCI conditions of 12% or more. This demonstrates that strong coding gain can withstand higher CCI.

## Iv. System-Level Implementation And Verification Via Laboratory Test

Using the proposed LR-FHSS transceiver design including the synchronization algorithm, we implemented the LR-FHSS transmitter testbed based on the ASIC chipset and the receiver testbed based on the FPGA, as shown in Fig. 15. To achieve the target QoS of the DtS-IoT use cases, i.e., environmental monitoring that requires data rates of less than 1 kbps, quite relaxed latency, and low power conditions, as shown in Table I, the ASIC chipset process was specially adopted for lowpower consumption and miniaturization of the terminal. The implementation of the LR-FHSS transceiver was verified via laboratory tests using multiple terminal transmissions over wired and wireless communications. Finally, the proposed DtS-IoT system including the LR-FHSS transceiver was constructed and verified through laboratory tests such as a system operation request and response.

A. Implementation of ASIC-based Transmitter and FPGA- based Receiver Testbeds The ASIC chipset for LR-FHSS transmition was built via the system on chip (SoC) process with 0.18 um and 0.6 Mgate by the foundry company SMIC. Fig. 15(a) shows the LR-FHSS transmitter testbed based on the ASIC chipset, which has the following features:

- CPU: 32-bit RISC-V (RV32I instruction set)
- Memory: RAM for chip program/data memory (32
Kbytes), ROM for chip boot memory (4 Kbytes)
- Flash controller: Serial interface (external device of
S25FL064P with 64 Mbits and 3.0 V)
- Timer: 16-bit timer with external input, watch-dog with
reset & interrupt support, real time clock

- Interface: UART (8 bits), SPI (128 bits), I2C (8 bits) - GPIO: General purpose port 0 (16 bits) - Power save mode: Deep sleep, sleep, idle - Package: 100LQFP (8mA per pin)
- Die area: 621 um x 265 um In the ASIC chipset, the internal central processing unit (CPU) reads the external sensor information through the sensor interfaces, such as the universal asynchronous receiver transmitter (UART), serial peripheral interface (SPI) and inter-integrated circuit (I2C), and stores it in the internal memory. Next, the transmission function is performed using the LR-FHSS waveform. The internal CPU of RISC-V supports the 32-bit base integer instruction set among the RV32I instruction sets. The read only memory (ROM) where the boot loader is stored and performs the function of copying the user program stored in flash to the random access memory (RAM) when the chip boots. The RAM is a space that stores user programs, and the CPU reads user programs and performs desired operations. The external flash is controlled through the quad SPI (QSPI) flash module, and the port 0 is composed of 16 bits and performs general-purpose input/output (GPIO) functions. Based on the ASIC chipset with the above features, we configured the LR-FHSS transmitter testbed including the AD9776 digital-toanalog converter (DAC), ADRF6755 modulator, flash memory and interfaces. Here, the DAC and RF modulator chips are controlled from an external CPU through the SPI interface.

Fig. 15(b) depicts the LR-FHSS receiver testbed based on FPGA. Given the constraints of terminals in terms of power consumption and size, a receiver intended for placement within the LEO satellite payload necessitates regenerative or onboard processing capabilities, for which FPGA-based implementation is suitable. The FPGA-based receiver testbed, utilizing the Xilinx Zynq-7000 SoC, incorporates components such as the AD9361 RF tuner, AD9517 clock generator, flash and DDR3 memory. The AD9361 RF tuner, equipped with integrated 12- bit DACs and analog-to-digital converters (ADCs), facilitates transmission and reception functions. DDR3 SDRAM serves as external memory for the classification and storage of up to NCF =3120 LR-FHSS signals channelized in the signal detector of the LR-FHSS receiver. Various interfaces including RS232, RS422, FPGA mezzanine card (FMC) connector, mictor connector, ethernet, and JTAG are utilized.

B. Test diagram for verification To verify the overall DtS-IoT system architecture suggested in Fig. 1, we built a test diagram, as shown in Fig. 16. This verification was carried out on the ground by establishing the DtS-IoT communication system by the development of the LEO satellite payload with an engineering model (EM) level. For the user link between the satellite and ground integrated terminals and the LEO satellite payload, the LR-FHSS transmitter sends the collected sensor data to the user link OBP of the LR-FHSS receiver in UHF band frequency, i.e., 940 MHz, supported by our self-developed LoRa antenna. In addition, the satellite and ground integrated terminal includes the module for the LoRa transmission and reception to link the ground gateway and server.

In the user link OBP, the collected sensor data received from the terminals is demodulated and stored temporarily in the DDR3 memory. The demodulated data from the multiple terminals is delivered to OBC, here SOLBrain, and stored, while the LEO satellite payload flies in the orbit until it can communicate with the gateway. In OBC, the GPS information is received at GPS receiver OEM719 with a GPS antenna of TW1322 which includes the epoch time and the location data, such as the coordinated universal time (UTC), latitude, longitude, and altitude. When the connection to the gateway is established, the stored data is transmitted from the feeder link OBP of the XLink-S to the gateway in S-band frequency with 2.4 GHz, supported by the S-band antenna of NanoCom ANT2000.

For the feeder link between the LEO satellite payload and the gateway, the feeder link OBP transmits stored data to the TM and TC modem of Cortex-CRT via the frequency up/down converter, which converts the S-band frequency to the intermediate frequency (IF) of 70 MHz. The TM and TC modem utilize the consultative committee for space data systems (CCSDS) protocol [37]. This protocol is specifically designed for communication over a space link or within a network comprising one or multiple space links. A space link refers to the communication link between a spacecraft and its associated ground system. In the gateway, the NMS receives the demodulated data from the TM and TC modem via ethernet and processes it in the network protocol module. In addition, the functions for beacon transmission management and satellite and terminal information management can be performed.

## C. Laboratory Test Results

In our laboratory tests, the performance of user link LR-
FHSS transmission was analyzed under various conditions with different transmission intervals, code rates and number of headers. The data transmission function of the CCSDS format was verified using a commercial modem of the feeder link. Finally, the entire DtS-IoT system was verified by checking the satellite network access process from the terminal.

1) User Link Verification: Fig. 17(a) and 17(b) illustrate the laboratory test environments for LR-FHSS transmission between the eight ASIC-based transmitter testbeds and single FPGA-based receiver testbed over wired communication and wireless communication, respectively. In the wired communication test, the output of eight transmitters was input to the receiver. In the wireless communication test, four transmitters spaced 8 cm apart were divided into two groups, with an interval of 45 cm between them. The distance between the center of the transmitters and the receiver was 4.7 m. Fig. 18 illustrates the spectral characteristics of the output signal from one of the LR-FHSS transmitters in a wired communication environment. The figure depicts the frequency hopping signals with an occupied bandwidth (OBW) of 488 Hz within an OCW of 1.5 MHz. The spectrum exhibits an intermittent, empty characteristic in the frequency domain during non-hopping intervals.

Fig. 19 displays the PER performance of LR-FHSS transmission at various code rates and transmission intervals, corresponding to different numbers of headers, in a laboratory test environment over wired communication. Code rates of {5/6,
2/3, 1/2, 1/3} were utilized. The packet emission interval of each transmitter was randomly selected in the short interval from 4 s to 6.56 s and in the long interval from 20 s to 32.8 s. For each transmission, the packet length increased sequentially to [10:10:100] bytes. In this simulation, the actual IoT data transmission-like environment was designed by adopting random transmission intervals and packet lengths. From these parameters, the PER was measured according to the number of headers from 1 to 4, where increasing the number of headers can improve the reception performance with low-spectral efficiency. Via simulations, we found the optimal number of header repetitions between the burden of the header repetition and reception performance. Compared to the PERs of LR-FHSS transmission with a short interval, those with a long interval are observed to be lower due to a lower packet collision rate. In both short and long intervals, as the number of headers increased, the PER decreased because of reliable header detection. At low code rates of 1/2 and 1/3, the PER reduction becomes significant, e.g., at the code rate of 1/3, the PER is slightly worse than at 1/2. This is because at the very low code rate, the number of hopping blocks may increase due to the packet length increased by encoding, leading to an increasing packet collision rate. Consequently, we conclude that less header repetition is effective at lower code rates.

Fig. 20 illustrates the PER performance of LR-FHSS transmission according to the code rate and the number of headers, considering both short and long intervals, in a laboratory test environment over wireless communication. Here, the number of headers for each code rate was adopted as (5/6,1), (2/3,2), (1/2,3), and (1/3,4): combinations defined in the LoRaWAN standard [1]. Compared to Fig. 19, to use the wired transmission link, the wireless transmission test was performed in short and long intervals. As the code rate decreases and the number of headers increases, the PER gradually decreases. However, even if four headers are used at the lowest code rate of 1/3, the PER performance of the short interval is higher than the code rate of 1/2 with three headers, which is the previous measurement condition. From these results, we estimate that using a code rate of 1/3 at short intervals can cause frequent collisions, while at long intervals, the use of a stronger code rate with increasing headers reduces the PER. Through our user link transmission test results, we demonstrate that LR- FHSS transmission supports data rates of up to 1523 kHz, which is a KPI for environmental monitoring in low-powerbased ASIC terminals.

2) Feeder Link Verification: For the feeder link transmission, as shown in Fig. 16, the S-band frequency is used between the feeder link OBP and the TM and TC modem via the frequency up/down converter, which converts the S-band frequency to the IF of 70 MHz. In addition, the symbol rate of 40 Msps and 128 ksps is used for TM downlink and TC uplink, respectively, with the modulation method of BPSK or QPSK. The data format follows the CCSDS protocol [37] of the inner format and the TM and TC protocol of the outer format. That is, the CCSDS protocol is inserted into the data part of the TM and TC protocol. After the feeder link transmission data following CCSDS and the TM and TC protocols arrives in the LEO satellite payload, the XLink protocol is applied in OBC and OBP modules. For DtS-IoT system verification, Fig. 21 shows the laboratory test environment, which is composed of the gateway, LEO satellite payload and satellite and ground integrated terminal. Here, the gateway includes the NMS, the TM and TC modem, and the frequency up/down converter.

Fig. 22 shows the results of the feeder link transmission verification for the TC uplink and TM downlink. As illustrated in Fig. 22(a) for the TC uplink, the NMS module first transmits the TM and TC protocol, which consists of the TCP-IP header, request code, command tag, TC length, data, CRC and TCP- IP postamble. Here, the CCSDS protocol consisting of a start sequence, BCH encoded data, and tail sequence is inserted into the data part of the TM and TC protocol. After the feeder link transmission data following CCSDS and TM and TC protocols arrives in the LEO satellite payload, the XLink protocol is applied in the OBC and OBP modules. The XLink protocol consists of the product key, service event, XMT, and data. The data part of the XLink protocol is included after 1 byte of CRC is excluded from the BCH encoded data of the CCSDS protocol. Finally, the user link OBP is received after the padding bits of 0x55 are excluded. For the TM downlink, the user link OBP first transmits the XLink protocol, which consists of the product key, service event, XMT, moreinfor, mask, and data with the padding, as shown in Fig. 22(b). In the feeder link OBP, the syncword is added into the mask and data with padding of the XLink protocol. This data, generated from the LEO satellite payload, is received at the NMS module by adding the header and tail as it passes through the TM and TC modem.

3) System Verification: Figs. 23(a) and 23(b) measure the throughput performance of the proposed DtS-IoT system with the unslotted and slotted Aloha multiple access schemes, respectively. The performance measurements apply the following parameters: a satellite connection time of 1200 s, number of devices 1500, packet length of 20 bytes, and beacon interval of 120 s. The maximum throughput is theoretically calculated to be 0.18 and 0.37 for the unslotted and slotted Aloha multiple access schemes, respectively [8]. In Fig. 23(a), the unslotted Aloha multiple access scheme shows a maximum throughput of 0.12 when using only one channel, and a maximum throughput of 0.38 when using three channels. Basically, more than two channels are required to satisfy the theoretical throughput of 0.18. In Fig. 23(b), the slotted Aloha multiple access scheme shows a maximum throughput of 0.24 when using only one channel, and a maximum throughput of 0.7 when using three channels, meaning more than two channels are required to satisfy the theoretical throughput of 0.37. These results demonstrate that the LR-FHSS transceiverbased DtS-IoT system enables high throughput communication link for future 6G networks.

## V. Conclusions

This paper presented the system architecture and design details for a DtS-IoT system with an LR-FHSS transceiver and its feasibility validation by implementing a testbed and conducting laboratory tests. In this study, we established high-level system architecture, target DtS-IoT use cases and associated KPIs, and provided a design overview of the LR-FHSS transceiver and DtS-IoT system. The LR-FHSS transceiver was designed by using a robust synchronization algorithm based on the GMSK symbol mapping scheme to withstand LEO satellite channel environments. In particular, it includes signal detection for the simultaneous reception of numerous frequency hopping signals and enhanced SOVA for header and payload receptions. To validate the proposed DtS-IoT system, we presented the implementation details for the transceiver testbeds using an ASIC chipset and an FPGA and the entire DtS-IoT system. The DtS-IoT system, mainly composed of the satellite and ground integrated terminal, LEO satellite payload and gateway, was constructed in a laboratory for demonstration. We demonstrated that the entire DtS-IoT
system, including to the LR-FHSS transceiver, can perform transmission on the user link and feeder link. Simultaneously with the demonstration of DtS-IoT system functionalities, a link performance assessment to check whether the LR-FHSS communication system can endure LEO satellite channel environments was conducted. The simulation tests showed that an initial STO up to 1/4, SFO up to 80 ppm, CFO up to 5/6 of the symbol rate, Doppler rate up to 400 Hz/sec, and CCI up to 40 percent can be considered. Furthermore, DtS- IoT systems with unslotted and slotted Aloha multiple access schemes were measured to support throughputs of over 0.18 and 0.37, respectively.

This study provides valuable insights into the infinite applicability of DtS-IoT systems and guides readers in implementing an LR-FHSS transceiver testbed for verification of relevant technologies; however, this study has two limitations. First, there is a lack of test results for integrated DtS-IoT system verification due to the absence of final application development for target use cases with relevant KPIs. Second, there is a significant gap between verification using actual operating LEO satellites and laboratory-level verification. For future studies, we consider the following two topics.

Development and integration of final application for environmental monitoring: We are currently developing a marine climate prediction analysis system as a final application considering use cases for environmental monitoring. To this end, we intend to collect and store marine climate data such as water temperature and waves by mounting a developed satellite and ground integrated terminal on a marine buoy. The collected data is delivered to the gateway via LEO satellite payload, processed by NMS at the gateway, and accumulated on the server. Finally, the accumulated data is used to predict future ocean climate through machine learning in a big data analysis system.

In-orbit test of the DtS-IoT system: Currently,the LEO
satellite payload of the developed DtS-IoT system has been developed at the EM level, and system verification has been performed through laboratory tests on the ground. This system verification was performed through transmission tests on each user and feeder link. Therefore, additional DtS-IoT system functional and performance testing is needed to verify that it can satisfy the relevant KPIs of the target use case. Finally, we aim to build and launch an LEO satellite payload containing the LR-FHSS receiver with a flying model (FM) level and perform an in-orbit test of the DtS-IoT system with it.

## References

[1] N. Sornin, M. Luis, T. Eirich, T. Kramp, and O. Hersent, "RP002-1.0.3
LoRaWAN regional parameters," LoRa Alliance Technical Committee and
others, Tech. Rep., pp. 1-94, May 2021.
[2] S. Jung, S. Jeong, J. Kang, J. Ryu, and J. Kang, "Transceiver design and
performance analysis for LR-FHSS-based Direct-to-Satellite IoT," IEEE Commun. Lett., vol.27, no. 12, pp. 3310-3314, Dec. 2023.
[3] X. Fang, W. Feng, T. Wei, Y. Chen, N. Ge, and C.-X. Wang, "5G embraces
satellites for 6G ubiquitous IoT: Basic models for integrated satellite terrestrial networks," *IEEE Internet of Things Jour.*, vol.8, no. 18, pp.
14399-14417, Sep. 2021.
[4] S. Chen, Y. Liang, S. Sun, S. Kang, W. Cheng, and M. Peng, "Vision,
requirements, and technology trend of 6G: How to tackle the challenges of system coverage, capacity, user data-rate and movement speed," IEEE
Wireless Commun., vol.27, no. 2, pp. 218-228, Apr. 2020.
[5] M. Giordani and M. Zorzi, "Non-terrestrial networks in the 6G era:
Challenges and opportunities," *IEEE Netw.*, vol.35, no. 2, pp. 244-251,
Mar. 2021.
[6] J. Kim, Y.-J. Choi, G. Noh, and H. Chung, "On the feasibility of
remote driving applications over mmWave 5G vehicular communications: implementation and demonstration," *IEEE Trans. Veh. Technol.*, vol.72, no. 2, pp. 2009-2023, Feb. 2023.
[7] J. A. Fraire, S. Cespedes, and N. Accettura, "Direct-to-satellite IoT
- a survey of the state of the art and future research perspectives: Backhauling the IoT through LEO satellites," in Proc. Int. Conf. Ad-Hoc Netw. Wireless., pp. 241-258, Sep. 2019.
[8] G. Alvarez, J. A. Fraire, K. A. Hassan, S. Cespedes, and D. Pesch,
"Uplink transmission policies for LoRa-based direct-to-satellite IoT," IEEE Access, vol. 10, pp. 72687-72701, Jul. 2022.
[9] J. A. Fraire, S. Henn, F. Dovis, R. Garello, and G. Taricco, "Sparse
satellite constellation design for LoRa-based direct-to-satellite Internet of Things," *in Proc. IEEE Global Commun. Conf.*, pp. 1-6, Dec. 2020.
[10] N. Pachler, I. del Portillo, E. F. Crawley, and B. G. Cameron, "An
updated comparison of four low earth orbit satellite constellation systems to provide global broadband," *in Proc. IEEE ICC Workshops*, pp. 1-7, Jun. 2021.
[11] 3GPP TS 36.211 v.14.3.0, "LTE; evolved universal terrestrial radio
access (E-UTRA); physical channels and modulation (Release 14)," Available from: http://www.etsi.org, 2017.
[12] U. Raza, P. Kulkarni, and M. Sooriyabandara, "Low power wide area
networks: An overview," *IEEE Commun. Surveys Tutorials*, vol. 19, no. 2, pp. 855-873, Jan. 2017.
[13] Semtech, "LoRa modem design guide: SX1272/3/6/7/8/9," Available
from: https://www.semtech.com/, July 2020.
[14] Sigfox, "Sigfox Technology," *Available from: https://www.sigfox.com/*,
Dec. 2020.
[15] IEEE Standard, "IEEE standard for local and metropolitan area
networks–part 15.4: Low-rate wireless personal area networks (LR- WPANs), amendment 5: Physical layer specifications for low energy, critical infrastructure monitoring networks," Available from: DOI: 10.1109/IEEESTD.2013.6581828, 2013.
[16] S. Jung, G. Im, D.-H. Jung, P. Kim, J. G. Ryu, and J. Kang, "Performance analysis of DSSS- and CSS-based physical layer for IoT transmission over low-Earth orbit satellites," *ETRI J.*, vol. 44, no. 4, pp. 543-559, Aug. 2022.
[17] A. A. Doroshkin, A. M. Zadorozhny, O. N. Kus, V. Y. Prokopyev, and
Y. M. Prokopyev, "Experimental study of LoRa modulation immunity to Doppler effect in cubesat radio communications," *IEEE Access*, vol. 7, pp. 75721-75731, May 2019.
[18] S. Jung, S. Jeong, J. Kang, and J. Kang, "Marine IoT systems with spaceair-sea integrated networks: Hybrid LEO and UAV edge computing," IEEE Internet of Things Jour., vol. 10, no. 23, pp. 20498-20510, Dec.
2023.
[19] B. Vucetic and J. Du, "Channel modeling and simulation in satellite
mobile communication systems," *IEEE J. Selected Areas Commun.*, vol.
10, no. 8, pp. 1209-1218, Oct. 1992.
[20] Semtech,
"Application
note:
LR-FHSS
system
performance,"
SX1261/62/ LR1110, pp. 1-28, Feb. 2022.
[21] G. Boquet, P. Tuset-Peiro, F. Adelantado, T. Watteyne, and X. Vilajosana, "LR-FHSS: overview and performance analysis," IEEE Commun.
Mag., vol. 59, no. 3, pp. 30-36, Mar. 2021.
[22] M. A. Ullah, K. Mikhaylov, and H. Alves, "Analysis and simulation
of LoRaWAN LR-FHSS for direct-to-satellite scenario," IEEE Wireless Commun. Lett., vol. 11, no. 3, pp. 548-552, Mar. 2022.
[23] A. Maleki, H. H. Nguyen, and R. Barton, "Outage probability analysis
of LR-FHSS in satellite IoT networks," *IEEE Commun. Lett.*, vol. 27, no.
3, pp. 946-950, Mar. 2023.
[24] A. Maleki, H. H. Nguyen, E. Bedeer, and R. Barton, "Outage probability
analysis of LR-FHSS and D2D-aided LR-FHSS protocols in shadowedrice fading Direct-to-Satellite IoT networks," IEEE Internet of Things Jour. Early Access, Nov. 2023.
[25] J. A. Fraire, A. Guitton, and O. Iova, "Recovering headerless frames in
LR-FHSS," *arXiv:2306.08360v1*, 2023.
[26] M. A. B. Temim, G. Ferre, and O. Seller, "An LR-FHSS receiver for a
massive IoT connectivity," Proc. IEEE Int. Symp. on Pers., Indoor and Mobile Radio Commun., pp. 1-6, Sep. 2023.
[27] F. Zhang, F. Yu, X. Zheng, L. Liu, and H. Ma, "DFH: Improving the
reliability of LR-FHSS via dynamic frequency hopping," Proc. IEEE Int. Conf. on Net. Prot., pp. 1-12, Oct. 2023.
[28] ETSI TR 103 435 v1.1.1, "System reference document (SRdoc); short
range devices (SRD); technical characteristics for ultra narrow band (UNB) SRDs operating in the UHF spectrum below 1 GHz," pp. 1-54, Feb. 2017.
[29] London Economics, "Nanosatellite telecommunications: A market study
for IoT/M2M applications," pp. 1-45, Aug. 2017.
[30] Q. Zhou, K. Zheng, L. Hou, J. Xing, and R. Xu, "Design and implementation of open LoRa for IoT," *IEEE Access*, vol. 7, pp. 100649-100657,
Jul. 2019.
[31] M. de Sanctis, E. Cianca, G. Araniti, I. Bisio, and R. Prasad, "Satellite
communications supporting Internet of Remote Things," IEEE Internet of Things Jour., vol. 3, no. 1, pp. 113-123, Feb. 2016.
[32] E. Casini, R. D. Gaudenzi, and A. Ginesi, "DVB-S2 modem algorithms
design and performance over typical satellite channels," Int. J. Satell. Commun. Network., vol. 22, no. 3, pp. 281-318, Jun. 2004.
[33] H. Zhang, X. Chu, W. Guo, and S. Wang, "Coexistence of Wi-Fi and
heterogeneous small cell networks sharing unlicensed spectrum," IEEE Commun. Mag., vol. 53, no. 3, pp. 158-164, Mar. 2015.
[34] G. M. A. Sessler, R. Abello, N. James, R. Madde, and E. Vassallo,
"GMSK demodulator implementation for ESA deep-space missions," Proceedings of the IEEE, vol. 95, no. 11, pp. 2132-2141, Nov. 2007.
[35] E. Perrins and B. Kumaraswamy, "Decision feedback detectors for
SOQPSK," *IEEE Trans. Commun.*, vol. 57, no. 8, pp. 2359-2368, Aug. 2009.
[36] N. A.-Dhahir and G. Saulnier, "A high-performance reduced-complexity
GMSK demodulator," *IEEE Trans. Commun.*, vol. 46, no. 11, pp. 1409- 1412, Nov. 1998.
[37] CCSDS 130.0-G-4, "CCSDS report: Overview of space communications
protocols," CCSDS Secretariat National Aeronautics and Space Administration, Apr. 2023.