****PA3 Pantheon – Congestion Control Protocol Evaluation**
This repository is created for the PA3 assignment in Computer Networks. The goal of this project is to evaluate and compare different congestion control (CC) protocols using the Pantheon framework developed by Stanford.

Objective
Tested and compared the performance of three CC protocols:
TCP Vegas, TCP Cubic, TCP BBR

These were tested under different network conditions using the Mahimahi network emulator.

Test Scenarios
1. Low-Latency, High-Bandwidth Environment
Link: 50 Mbps, 10 ms RTT
Protocol tested: TCP Vegas

2. Realistic LTE Network Environment
Trace files used: ATT-LTE-driving.up and ATT-LTE-driving.down (pre-installed in Mahimahi)
Protocols tested: TCP Cubic and TCP BBR

Note on High Latency Tests
I also attempted tests with high-latency and constrained bandwidth (1 Mbps, 200 ms RTT) using TCP Vegas, LEDBAT, and Westwood. These tests failed due to tunnel connection timeouts and this limitation is mentioned in the report.

Collected Data and Metrics
For each test the following metrics were collected:

Throughput over time, Average RTT (Round-Trip Time), Packet loss rate
Each protocol’s results include:
CSV file with throughput values, CSV file with RTT and loss rate, Line chart showing throughput over time

How to Analyze New Logs
You can analyze new log files using the script analyze_logs.py. 

**Example usage:**
python3 analyze_logs.py <datalink_log> <acklink_log> <protocol_name>

This will generate:
<protocol_name>_throughput.csv
<protocol_name>_stats.csv
<protocol_name>_throughput.png
