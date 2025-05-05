# Offensive Security intro

## Your First Hack
We are using Gobuster to brute-force FakeBank's website to find hidden directories and pages. Gobuster will take a list of potention page or directory anmes and try accessing a website with each of them; if the page exists, it tells you.

### 1. Open a terminal

### 2. Use GoBuster to find hidden website pages

```
gobuster -u http://fakebank.thm -w wordlist.txt dir
```
```-u``` is used to state the website we're scanning

```-w``` takes a list of words to iterate through to find hidden pages

![image](../Learning%20modules/images/gobuster1.png)

In the above image GoBuster has located 2 hidden pages:
- images (Status: 301)
- bank-transfer (Status: 200) &Larr; We will focus on this one, returning the "OK" / Successful response

### 3. "Hack" the bank

We have our hidden page, ```bank-transfer```. 

Navigate to the webpage in your browser
```http://fakebank.thm/bank-transfer```

You will be taken to an Admin Portal

![image](../Learning%20modules/images/adminportal.png)

> From this page, an attacker has authorized access and can steal money from any bank account. As an ethical hacker, you would (with permission) find vulnerabilities in their application and report them to the bank to fix them before a hacker exploits them.

Your mission is to transfer $2000 from bank account 2276 to your account (account number 8881). If your transfer was successful, you should now be able to see your new balance reflected on your account page.

![image](../Learning%20modules/images/heist.png)

![image](../Learning%20modules/images/heist2.png)

## Success!

The money is now in "your" account and the flag is displayed!

![image](../Learning%20modules/images/heist3.png)  