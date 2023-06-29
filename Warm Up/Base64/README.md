# Base64

## Basic Information
Category: Warm Up  
Difficulty: Beginner  
Points: 20  

## Solving
The idea of this challenge is to familiarise your with base64. Base64 is an encoding scheme that is generally used to trasnfer content-based messages over the Internet. Base64 can normally be identified by an ```=``` or ```==``` at the end of a string. Base64 can be solved using many tools online or on linux CLI.   

### Online Tool  
  
**Step 1:**  
Visit this link to decode base64: [CyberChef](https://cyberchef.org/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false))  

**Step 2:**   
Paste the following base64 into the decoder: ```U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo=```

**Step 3:**   
Copy the flag and complete the challenge
```SKR{b4se64_4r3_s0_s1mp13}```

**SOLVED**  

### Kali Linux CLI

**Step 1:**  
Echo the following base64 so that it could be piped
```
echo "U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo="  
```

**Step 2:**   
Pipe the output onto base64 tool and specify decode.
By default, base64 encodes any input.
```
echo "U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo=" | base64 -d 
```

**Step 3:**   
Copy the flag and complete the challenge
```SKR{b4se64_4r3_s0_s1mp13}```

**SOLVED**  
