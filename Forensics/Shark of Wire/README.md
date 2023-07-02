# Shark Of Wire

## Basic Information
Category: Forensics    
Difficulty: Easy  
Points: 20  

## Solving
The concept of this challenge is to familiarise you with wireshark tool. 
  
**Step 1:**  
Download the image on linux by running the following command in terminal  
```
wget https://skrctf.me/files/25a0f17531dc8152380622658fde2b7e/network_data.pcap
```

**Step 2:**   
Open the pcap file in wireshark by running the following command   
```
wireshark network_data.pcap
```

**Step 3:**   
You will be greeted with network packets labelled in different colours. Our aim is to find the ones that are successful, or in other words, the ones highlighted in green.  

We won't be going through succesfully transmitted packet in the file, but groups of them. Looking at the file, we can see that green packets comes in blocks. We need to investigate each green block rather than individual packets. Click on one of the green packets and and follow the TCP stream. This way, we can investigate entire blocks rather than indivudal packets. 

**Step 4:**     
Copy the flag and complete the challenge
```SKR{0pen_Pcap_File_1n_Wir3Sh4rk}```

**SOLVED**  
