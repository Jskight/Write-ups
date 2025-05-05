# Windows Powershell

## Introduction

Ahoy there! If you’re here, you’ve either heard whispers of the marvels of PowerShell and want to discover more, or you’ve sailed over from the first room of the Command Line module—Windows Command Line. Either way, you’re about to embark on a journey to discover the marvels of this powerful shell, learning how to use it to uncover the secrets of any Windows system. Avast, then—on board!
Learning Objectives

This is the second room in the Command Line module. It is an introductory room to PowerShell, the second—only historically—command-line utility built for the Windows operating system.

   - Learn what PowerShell is and its capabilities.
   - Understand the basic structure of PowerShell’s language.
   - Learn and run some basic PowerShell commands.
   - Understand PowerShell’s many applications in the cyber security industry.

Room Prerequisites

Before approaching this room, it’s recommended that you have understood the concepts in the Windows and AD Fundamentals module and the Windows Command Line room.

**Raise the anchor, hoist the sails—it's time to set sail!**

No answer needed

---

## What is PowerShell

From the official Microsoft [page](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4): “PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework.”

PowerShell is a powerful tool from Microsoft designed for task automation and configuration management. It combines a command-line interface and a scripting language built on the .NET framework. Unlike older text-based command-line tools, PowerShell is object-oriented, which means it can handle complex data types and interact with system components more effectively. Initially exclusive to Windows, PowerShell has lately expanded to support macOS and Linux, making it a versatile option for IT professionals across different operating systems.
A Brief History of PowerShell

PowerShell was developed to overcome the limitations of existing command-line tools and scripting environments in Windows. In the early 2000s, as Windows was increasingly used in complex enterprise environments, traditional tools like `cmd.exe` and batch files fell short in automating and managing these systems. Microsoft needed a tool that could handle more sophisticated administrative tasks and interact with Windows’ modern APIs.

Jeffrey Snover, a Microsoft engineer, realised that Windows and Unix handled system operations differently—Windows used structured data and APIs, while Unix treated everything as text files. This difference made porting Unix tools to Windows impractical. Snover’s solution was to develop an **object-oriented** approach, combining scripting simplicity with the power of the .NET framework. Released in 2006, PowerShell allowed administrators to automate tasks more effectively by manipulating objects, offering deeper integration with Windows systems.

As IT environments evolved to include various operating systems, the need for a versatile automation tool grew. In 2016, Microsoft responded by releasing PowerShell Core, an open-source and cross-platform version that runs on Windows, macOS, and Linux.
The Power in PowerShell

To fully grasp the power of PowerShell, we first need to understand what an object is in this context.

In programming, an object represents an item with properties (characteristics) and methods (actions). For example, a `car` object might have properties like `Color`, `Model`, and `FuelLevel`, and methods like `Drive()`, `HonkHorn()`, and `Refuel()`.

Similarly, in PowerShell, objects are fundamental units that encapsulate data and functionality, making it easier to manage and manipulate information. An object in PowerShell can contain file names, usernames or sizes as data (properties), and carry functions (methods) such as copying a file or stopping a process.

The traditional Command Shell’s basic commands are text-based, meaning they process and output data as plain text. Instead, when a cmdlet (pronounced command-let) is run in PowerShell, it returns objects that retain their properties and methods. This allows for more powerful and flexible data manipulation since these objects do not require additional parsing of text.

We will explore more about PowerShell’s cmdlets and their capabilities in the upcoming sections.

### What do we call the advanced approach used to develop PowerShell?

**Answer**: Object-Oriented

---

## PowerShell Basics

### Connecting to the VM via SSH

*I chose to connect via the terminal on my local machine, so my instructions will vary slightly from the site instructions*

1. Make sure you're connected to tryhackme via openvpn 
2. Start the VM
3. Open the terminal

        username: captain
        password: JollyR0ger#
        IP: 10.10.15.154

4. run `ssh captain@10.10.15.154`
5. Enter the password when prompted

you should connect and get the following:

```
captain@THEBLACKPEARL C:\Users\captain>
```

### Launching PowerShell

PowerShell can be launched in several ways, depending on your needs and environment. If you are working on a Windows system from the graphical interface (GUI), these are some of the possible ways to launch it:

- Start Menu: Type `powershell` in the Windows Start Menu search bar, then click on `Windows PowerShell` or `PowerShell` from the results.

- Run Dialog: Press `Win + R` to open the Run dialog, type `powershell`, and hit `Enter`.

- File Explorer: Navigate to any folder, then type `powershell` in the address bar, and press `Enter`. This opens PowerShell in that specific directory.

- Task Manager: Open the Task Manager, go to `File > Run new task`, type `powershell`, and press `Enter`.

Alternatively, PowerShell can be launched from a Command Prompt (`cmd.exe`) by typing `powershell`, and pressing `Enter`.

In our case, where we only have access to the target VM’s Command Prompt, this is the method we’ll use.

```
captain@THEBLACKPEARL C:\Users\captain>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\captain> 

```

After PowerShell has launched, we’re presented with a `PS` (which stands for `PowerShell`) prompt in the current working directory.

### Basic Syntax: Verb-Noun

As previously mentioned, PowerShell commands are known as `cmdlets` (pronounced `command-lets`). They are much more powerful than the traditional Windows commands and allow for more advanced data manipulation.

Cmdlets follow a consistent `Verb-Noun` naming convention. This structure makes it easy to understand what each cmdlet does. The `Verb` describes the action, and the `Noun` specifies the object on which action is performed. For example:

- `Get-Content`: Retrieves (gets) the content of a file and displays it in the console.
- `Set-Location`: Changes (sets) the current working directory.

### Basic Cmdlets

To list all available cmdlets, functions, aliases, and scripts that can be executed in the current PowerShell session, we can use Get-Command. It’s an essential tool for discovering what commands one can use.

#### How would you retrieve a list of commands that start with the verb Remove? [for the sake of this question, avoid the use of quotes (" or ') in your answer]

**Answer**

`Get-Command -Name Remove*`

#### What cmdlet has its traditional counterpart echo as an alias?

```
PS C:\Users\captain> Get-Alias

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           % -> ForEach-Object
Alias           ? -> Where-Object
Alias           ac -> Add-Content
Alias           asnp -> Add-PSSnapin
Alias           cat -> Get-Content
Alias           cd -> Set-Location
Alias           CFS -> ConvertFrom-String                          3.1.0.0    Microsoft.PowerShell.Utility
Alias           chdir -> Set-Location
Alias           clc -> Clear-Content
Alias           clear -> Clear-Host
Alias           clhy -> Clear-History
Alias           cli -> Clear-Item
Alias           clp -> Clear-ItemProperty
Alias           cls -> Clear-Host
Alias           clv -> Clear-Variable
Alias           cnsn -> Connect-PSSession
Alias           compare -> Compare-Object
Alias           copy -> Copy-Item
Alias           cp -> Copy-Item
Alias           cpi -> Copy-Item
Alias           cpp -> Copy-ItemProperty
Alias           curl -> Invoke-WebRequest
Alias           cvpa -> Convert-Path
Alias           dbp -> Disable-PSBreakpoint
Alias           del -> Remove-Item
Alias           diff -> Compare-Object
Alias           dir -> Get-ChildItem
Alias           dnsn -> Disconnect-PSSession
Alias           ebp -> Enable-PSBreakpoint
Alias           echo -> Write-Output
...
```
**Answer**

`Write-Output`

#### What is the command to retrieve some example usage for the cmdlet New-LocalUser?

We can use Get-Help cmdlet to see the help page for New-LocalUser

```
PS C:\Users\captain> Get-Help New-LocalUser

NAME
    New-LocalUser

SYNOPSIS
    Creates a local user account.


SYNTAX
    New-LocalUser [-Name] <System.String> [-AccountExpires <System.DateTime>] [-AccountNeverExpires] [-Description
    <System.String>] [-Disabled] [-FullName <System.String>] -NoPassword [-UserMayNotChangePassword] [-Confirm] [-WhatIf]        
    [<CommonParameters>]

    New-LocalUser [-Name] <System.String> [-AccountExpires <System.DateTime>] [-AccountNeverExpires] [-Description
    <System.String>] [-Disabled] [-FullName <System.String>] -Password <System.Security.SecureString> [-PasswordNeverExpires]    
    [-UserMayNotChangePassword] [-Confirm] [-WhatIf] [<CommonParameters>]


DESCRIPTION
    The `New-LocalUser` cmdlet creates a local user account. This cmdlet creates a local user account.

    > [!NOTE] > The Microsoft.PowerShell.LocalAccounts module isn't available in 32-bit PowerShell on a 64-bit > system.


RELATED LINKS
    Online Version: https://learn.microsoft.com/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershe 
    ll-5.1&WT.mc_id=ps-gethelp
    Disable-LocalUser
    Enable-LocalUser
    Get-LocalUser
    Remove-LocalUser
    Rename-LocalUser
    Set-LocalUser

REMARKS
    To see the examples, type: "get-help New-LocalUser -examples".
    For more information, type: "get-help New-LocalUser -detailed".
    For technical information, type: "get-help New-LocalUser -full".
    For online help, type: "get-help New-LocalUser -online"
```

and there we have our answer under REMARKS

**Answer**

`Get-Help New-LocalUser -examples`