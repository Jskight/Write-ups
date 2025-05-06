# Photon Lockdown

## CHALLENGE DESCRIPTION

We've located the adversary's location and must now secure access to their Optical Network Terminal to disable their internet connection. Fortunately, we've obtained a copy of the device's firmware, which is suspected to contain hardcoded credentials. Can you extract the password from it?

## First steps

After downloading the Challenge file and unzipping the contents, we are presented with 3 files.

**fwu_ver**
**hw_ver**
**rootfs**

We can ignore the 2 text files. We'll investigate the **rootfs** file

> file rootfs 

output:
>rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023

## SquashFS

We can see that it is a compressed filesystem. in order to restore the filesystem we need to extract the file system from **rootfs**

We can extract the filesystem using squashfs-tools. IF it is not already installed, you can run the command below it install it.

>sudo apt install squashfs-tools

Once you've installed Squashfs you can use the unsquashfs command to restore the filesystem

>sudo unsquashfs rootfs

After extracting, navigate to the extracted filesystem using **cd**

>cd squashfs-root

## GREP

In order to find the flag, we will use the grep command to search for the expresssion **HTB**

>grep -lr HTB

We get three results

>bin/ip
>
>bin/tc
>
>etc/config_default.xml

Let's take a look at that XML file. 

>cat etc/config_default.xml

You'll notice that the output isn't very user friendly. We can use grep to search for **HTB** again, this time piping out of the **cat** on config_default.xml

>cat etc/config_default.xml | grep HTB

Output:
> Value Name="SUSER_PASSWORD" Value="HTB{N0w_Y0u_C4n_L0g1n}"
