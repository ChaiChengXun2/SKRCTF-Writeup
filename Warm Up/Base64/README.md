# Base64 - Warm Up Challenge

## Basic Information
**Category:** Warm Up  
**Difficulty:** Beginner  
**Points:** 20

## Solving

The "Base64" challenge aims to familiarize you with the Base64 encoding scheme, commonly used for transferring content-based messages over the internet.

### Online Tool Solution

**Step 1: Decode Base64 Online**
1. Visit the following link to decode Base64: [CyberChef Base64 Decoder](https://cyberchef.org/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)).

2. **Step 2: Paste Base64 String**
   Copy and paste the provided Base64-encoded string into the decoder: ```U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo=```

3. **Step 3: Retrieve the Flag**
After decoding, you will find the flag

### Kali Linux CLI Solution

**Step 1: Decode Base64 Using Command Line**
1. **Open a terminal window**

2. **Step 2: Echo Base64 String**  
    Echo the Base64-encoded string to pass it through the pipeline:
    ```bash
    echo "U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo="
    ```

3. **Step 3: Pipe and Decode**  
    Pipe the output into the `base64` tool and specify the `-d` flag to decode the Base64:
    ```bash
    echo "U0tSe2I0c2U2NF80cjNfczBfczFtcDEzfQo=" | base64 -d
    ```

4. **Step 4: Retrieve the Flag**  
    After decoding, you will obtain the flag

**Challenge Completed**
