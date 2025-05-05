# Windows Command Line

## Introduction

Learning Objectives

The purpose of this room is to teach you how to use MS Windows Command Prompt cmd.exe, the default command-line interpreter in the Windows environment. We will learn how to use the command line to:

* Display basic system information
* Check and troubleshoot network configuration
* Manage files and folders
* Check running processes

###  What is the default command line interpreter in the Windows environment?

cmd.exe

## Basic System Information

### What is the OS version of the Windows VM?

run `ver`

Output: `Microsoft Windows [Version 10.0.20348.2655]`

**Answer**

10.0.20348.2655

### What is the hostname of the Windows VM?

run `systeminfo`

Output: 
```
user@WINSRV2022-CORE C:\Users\user> Systeminfo

Host Name:                 WINSRV2022-CORE
OS Name:                   Microsoft Windows Server 2022 Datacenter
OS Version:                10.0.20348 N/A Build 20348
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                00454-60000-00001-AA763
Original Install Date:     4/23/2024, 7:36:29 PM
System Boot Time:          5/5/2025, 5:40:19 AM
System Manufacturer:       Amazon EC2
System Model:              t3a.micro
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 23 Model 1 Stepping 2 AuthenticAMD ~2200 Mhz
BIOS Version:              Amazon EC2 1.0, 10/16/2017
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC+00:00) Dublin, Edinburgh, Lisbon, London
Total Physical Memory:     980 MB
Available Physical Memory: 302 MB
Virtual Memory: Max Size:  1,300 MB
Virtual Memory: Available: 614 MB
Virtual Memory: In Use:    686 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 4 Hotfix(s) Installed.
                           [01]: KB5041948
                           [02]: KB5041160
                           [03]: KB5032310
                           [04]: KB5041590
Network Card(s):           1 NIC(s) Installed.
                           [01]: Amazon Elastic Network Adapter
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.0.1
                                 IP address(es)
                                 [01]: 10.10.143.117
                                 [02]: fe80::e0f:d000:4448:9982
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
```


**Answer**

WINSRV2022-CORE

## Network Troubleshooting

**ipconfig** - Look up network information

**ipconfig /all** - Provides more information about the network configuration

**ping {target_name}** - Sends ICMP packet and listens for a response

```
user@WINSRV2022-CORE C:\Users\user>ping 10.10.143.117

Pinging 10.10.143.117 with 32 bytes of data:
Reply from 10.10.143.117: bytes=32 time<1ms TTL=128
Reply from 10.10.143.117: bytes=32 time<1ms TTL=128
Reply from 10.10.143.117: bytes=32 time<1ms TTL=128
Reply from 10.10.143.117: bytes=32 time<1ms TTL=128

Ping statistics for 10.10.143.117:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

**tracert {target_name}** - trace route - traces the network route traversed to reach the target, "hops."

*Due to the limitation of room's network configuration, I use the local machine in the example below, which returns 1 hop, as expected*

```
user@WINSRV2022-CORE C:\Users\user>tracert 10.10.143.117

Tracing route to WINSRV2022-CORE.eu-west-1.compute.internal [10.10.143.117]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  WINSRV2022-CORE.eu-west-1.compute.internal [10.10.143.117] 

Trace complete.
```

**nslookup target_name** - Looks up a host or domain and returns it's IP address

```
user@WINSRV2022-CORE C:\Users\user>nslookup 10.10.143.117
Server:  ip-10-0-0-2.eu-west-1.compute.internal
Address:  10.0.0.2

Name:    ip-10-10-143-117.eu-west-1.compute.internal
Address:  10.10.143.117
```
**netstat** - Displays Current network connections and listening ports


*-a* -- Displays all established connections and listening ports

*-b* -- shows the program associated with each listehing port and establish connection

*-o* -- reveals the Process ID (PID) associated with the connection 

*-n* -- uses a numerical form for addresses and port numbers

```
user@WINSRV2022-CORE C:\Users\user>netstat 10.10.143.117

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.10.143.117:22       ip-10-6-47-48:61219    ESTABLISHED

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.10.143.117:22       ip-10-6-47-48:61219    ESTABLISHED

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.10.143.117:22       ip-10-6-47-48:61219    ESTABLISHED

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.10.143.117:22       ip-10-6-47-48:61219    ESTABLISHED

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.10.143.117:22       ip-10-6-47-48:61219    ESTABLISHED
^C
user@WINSRV2022-CORE C:\Users\user>netstat -abon 10.10.143.117

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING       1572
 [sshd.exe]
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       888
  RpcEptMapper
 [svchost.exe]
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
 Can not obtain ownership information
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       976
  TermService
 ...
  ```

### Which command can we use to look up the server’s physical address (MAC address)?

This answer is in the reading

**Answer**

ipconfig /all

### What is the name of the process listening on port 3389?

```
netstat -abon 10.10.143.117

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       976
  TermService
  ```

**Answer**

TermService

### What is the subnet mask?

```
user@WINSRV2022-CORE C:\Users\user>ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : WINSRV2022-CORE
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : eu-west-1.compute.internal
                                       eu-west-1.ec2-utilities.amazonaws.com

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
   Description . . . . . . . . . . . : Amazon Elastic Network Adapter
   Physical Address. . . . . . . . . : 02-6F-06-33-9E-69
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e0f:d000:4448:9982%5(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.10.143.117(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
...
```

**Answer**
255.255.0.0

## File and Disk Management

**tasklist** - lists running processes

```
user@WINSRV2022-CORE C:\Users\user>tasklist

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0        140 K
Registry                        96 Services                   0      8,856 K
smss.exe                       316 Services                   0        160 K
csrss.exe                      428 Services                   0      2,416 K
csrss.exe                      504 Console                    1      2,392 K
wininit.exe                    560 Services                   0      3,912 K
winlogon.exe                   580 Console                    1     12,240 K
services.exe                   648 Services                   0      5,668 K
lsass.exe                      672 Services                   0     13,020 K
svchost.exe                    776 Services                   0     11,332 K
fontdrvhost.exe                800 Console                    1      3,956 K
fontdrvhost.exe                804 Services                   0      1,584 K
svchost.exe                    888 Services                   0      9,764 K
svchost.exe                    976 Services                   0     13,920 K
svchost.exe                   1004 Services                   0     12,832 K
svchost.exe                    376 Services                   0      6,884 K
svchost.exe                    384 Services                   0     39,812 K
svchost.exe                    796 Services                   0     21,408 K
svchost.exe                   1028 Services                   0      8,200 K
svchost.exe                   1360 Services                   0     11,736 K
svchost.exe                   1372 Services                   0      8,872 K
svchost.exe                   1452 Services                   0     17,036 K
svchost.exe                   1468 Services                   0      3,644 K
MsMpEng.exe                   1548 Services                   0    189,060 K
sshd.exe                      1572 Services                   0      2,636 K
svchost.exe                   1728 Services                   0      3,276 K
svchost.exe                   2004 Services                   0      2,212 K
AggregatorHost.exe            2276 Services                   0      2,020 K
LogonUI.exe                   2932 Console                    1     12,856 K
conhost.exe                   2948 Console                    1     16,836 K
NisSrv.exe                    2816 Services                   0     10,596 K
amazon-ssm-agent.exe          2928 Services                   0     17,700 K
msdtc.exe                     3532 Services                   0     11,004 K
sshd.exe                      3944 Services                   0      8,300 K
sshd.exe                      3984 Services                   0      7,984 K
conhost.exe                   4000 Services                   0      5,492 K
cmd.exe                       4024 Services                   0      4,604 K
conhost.exe                   3780 Services                   0      1,340 K
tasklist.exe                  1700 Services                   0      8,812 K
WmiPrvSE.exe                  1668 Services                   0      9,112 K
```

**taskkill /PID {target PID}** - Terminates a specified task

### What command would you use to find the running processes related to notepad.exe?

**Answer**

`tasklist /FI "imagename eq notepad.exe"`

### What command can you use to kill the process with PID 1516?

**Answer**

`taskkill /PID 1516`

## Conclusion

### The command shutdown /s can shut down a system. What is the command you can use to restart a system?

```
user@WINSRV2022-CORE C:\Users\user>help shutdown
Usage: shutdown [/i | /l | /s | /sg | /r | /g | /a | /p | /h | /e | /o] [/hybrid] [/soft] [/fw] [/f]
    [/m \\computer][/t xxx][/d [p|u:]xx:yy [/c "comment"]]

    No args    Display help. This is the same as typing /?.
    /?         Display help. This is the same as not typing any options.
    /i         Display the graphical user interface (GUI).
               This must be the first option.
    /l         Log off. This cannot be used with /m or /d options.
    /s         Shutdown the computer.
    /sg        Shutdown the computer. On the next boot, if Automatic Restart Sign-On
               is enabled, automatically sign in and lock last interactive user.
               After sign in, restart any registered applications.
    /r         Full shutdown and restart the computer.
    ...
```

**Answer**

`shutdown /r`

### What command can you use to abort a scheduled system shutdown?

```
user@WINSRV2022-CORE C:\Users\user>help shutdown
Usage: shutdown [/i | /l | /s | /sg | /r | /g | /a | /p | /h | /e | /o] [/hybrid] [/soft] [/fw] [/f]
    [/m \\computer][/t xxx][/d [p|u:]xx:yy [/c "comment"]]

    No args    Display help. This is the same as typing /?.
    /?         Display help. This is the same as not typing any options.
    /i         Display the graphical user interface (GUI).
               This must be the first option.
    /l         Log off. This cannot be used with /m or /d options.
    /s         Shutdown the computer.
    /sg        Shutdown the computer. On the next boot, if Automatic Restart Sign-On
               is enabled, automatically sign in and lock last interactive user.
               After sign in, restart any registered applications.
    /r         Full shutdown and restart the computer.
    /g         Full shutdown and restart the computer. After the system is rebooted,
               if Automatic Restart Sign-On is enabled, automatically sign in and
               lock last interactive user.
               After sign in, restart any registered applications.
    /a         Abort a system shutdown.
...
```

**Answer**

`shutdown /a`