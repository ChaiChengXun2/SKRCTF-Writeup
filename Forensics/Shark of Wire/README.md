# Shark Of Wire - Forensics Writeup

## Basic Information
**Category:** Forensics  
**Difficulty:** Easy  
**Points:** 20

## Solving

The "Shark Of Wire" challenge aims to introduce you to the Wireshark tool and its capabilities for analyzing network data.

### Step 1: Download the Network Data

Begin by downloading the provided network data file on a Linux system. You can use the following command in your terminal:

```bash
wget https://skrctf.me/files/25a0f17531dc8152380622658fde2b7e/network_data.pcap
```  

### Step 2: Open the File in Wireshark

Next, you'll need to open the downloaded network_data.pcap file in Wireshark. Use the following command in your terminal:  

```bash
wireshark network_data.pcap
```  

### Step 3: Analyze the Network Packets  

Upon opening the file in Wireshark, you'll be presented with a display of network packets, each labeled with different colors. Our objective is to identify the successful network packets, which are typically highlighted in green.

Rather than inspecting individual packets one by one, we'll focus on groups of successful packets. Observe that green packets are often grouped together. To investigate entire blocks of successful packets, click on one of the green packets, and then follow the TCP stream.

This approach allows you to analyze entire blocks of packets at once, making it more efficient.  

### Step 4: Retrieve the Flag  

As you examine the network data and follow the TCP streams of green packets, you'll eventually discover the flag:  

Flag: SKR{XXXXXXXX}

**Challenge Completed** 

