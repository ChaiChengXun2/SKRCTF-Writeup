# Juggling Clown

## Basic Information
Category: Web  
Difficulty: Medium  
Points: 20  

## Solving
The concept of this challenge is familiarise you with insecure PHP codes and the concept of loose and strict comparison. 
  
**Step 1:**  
Looking at the HTML source code, we can find a hidden link under the page. That hidden link provides us with the PHP code behind the web page.  

**Step 2:**  
The vulnerability with the PHP code provided is the use of ```==``` instead of ```===```. The following code compares a string with user input:  
```
if(strcmp($answer , $_GET["answer"]) == 0)
```
There are many ways to break the above string comparison. We can't modify the answer on the server (presumably a string) but we can change our inputs to stage an exploit. 

**Step 3:**   
When a string is compared with an array in strcmp, it returns NULL. Why? strcmp compares strings, when a non-string argument is given, it attempts converts that into a string, but somtimes it fails. When it fails, strcmp will return NULL. A loose comaprison between NULL and 0 always returns returns true. Hence exploiting the PHP code to spit out the flag. Use the URL format as below:  
```URL/index.php?answer[]```

**Step 4:** 
Copy the flag and complete the challenge   
```SKR{D0n't_U5e_L00s3_C0mp4ris1On_fe9cab}```

**SOLVED**  
