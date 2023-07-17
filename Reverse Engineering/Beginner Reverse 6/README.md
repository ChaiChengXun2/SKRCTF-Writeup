# Beginner Reverse 6

## Basic Information
Category: Reverse Engineering    
Difficulty: Easy  
Points: 50  

## Solving
The concept of this challenge is to familiarise you with pointers and ASCII table.
  
**Step 1:**  
The concept is very similar to previous challenges. You have to combine your knowledge of pointers and ASCII to solve this challenge.  
```length != 17``` tells us that the password is of length 17   

```pass[0] != 'R'``` tells us that the 1st character of the password is ```R```  

```pass[1] - pass[0] != -31 || pass[1] != pass[3]``` tells us that the 2nd and 4rd characters in the password are the same value. By finding the 2nd character, we can find the 4th character. The 2nd character can be interpreted as the ASCII value of ```-31 + 82``` which is ```3``` in ASCII.  

```pass[4] != tolower(pass[0]) || pass[2] - pass[4] != 4``` tells us that the 5th character is 'r' and that the 3rd character is ```4 + 114``` which is ```v``` in ASCII.  

```pass[5] != '5' || pass[5] - pass[6] != 4``` tells us that the 6th character is ```5``` and the 7th character is ```1```  

```pass[7] != pass[0] + 28 || pass[2] - pass[8] != 47``` tells us that the 8th character is ```n``` and 9th character is ```G```  

```pass[9] != '_' || pass[12] != pass[9] || strncmp(pass+13,"Fun!",4) != 0 || strncmp(pass+10,"1s",2) != 0``` tells us that the 10th and 13th character is ```_```. It also tells us that the final 4 characters are ```Fun!``` and 11th and 12th character are reserved for ```1s```  

By combining everything together, we can find the solution.  

**Step 2:**   
Copy the flag and complete the challenge
```SKR{R3v3r51nG_1s_Fun!}```

**SOLVED**  
