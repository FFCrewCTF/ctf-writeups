# LSSO (misc, 200 points, solved by 11)

I did not actually solve this challenge during the competition.
I got hung up looking for NTFS streams (ADS) in the rarfile, when really the hostname and username were in a much simpler place.


## Challenge

> All my passwords are safely stored, or not?

Attachment: [misc200_87229453a454b44d.zip](misc200_87229453a454b44d.zip)


## Solution

The attachment contains a rar file which contains `cwallet.sso` and `ewallet.p12`. 
Some searching quickly reveals [ssoDecrypt](https://github.com/tejado/ssoDecrypt).

Install prereqs and compile in fresh ubuntu vm:
``` bash
# Install java cryptography extension (JCE) unlimited strength jurisdiction policy
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java7-unlimited-jce-policy 
# Compile ssoDecrypt
git clone https://github.com/tejado/ssoDecrypt.git
cd ssoDecrypt && javac -cp .:libs/:libs/bcprov-jdk16-145.jar ssoDecryptor.java
```

Attempt to decrypt the sso file:
``` bash
$ ./ssoDecrypt.sh cwallet.sso
PKCS12 key store mac invalid - wrong password or corrupted file.
PKCS12 key store mac invalid - wrong password, wrong LSSO secret (username + hostname) or corrupted file.
```

Because this is an LSSO, we need a username and hostname. 
``` bash
$ unrar v ekochall.rar

UNRAR 5.00 beta 8 freeware      Copyright (c) 1993-2013 Alexander Roshal

By Hugo@ekodesktop

Archive: ekochall.rar
Details: RAR 4

 Attributes      Size    Packed Ratio   Date   Time   Checksum  Name
----------- ---------  -------- ----- -------- -----  --------  ----
    ..A....      3981      3981 100%  07-10-16 23:13  21A2D217  ekochall/cwallet.sso
    ..A....      3904      3904 100%  07-10-16 23:13  0F2C4F8A  ekochall/ewallet.p12
    ...D...         0         0   0%  07-10-16 23:09  00000000  ekochall
----------- ---------  -------- ----- -------- -----  --------  ----
                 7885      7885 100%                            3
```

Rerunning with the username and hostname gets us the flag:
``` bash
$ ./ssoDecrypt.sh cwallet.sso Hugo ekodesktop
sso key: a252ece7d911fa0e
sso secret: 0e6b16ac78d6231bd237e71e0bb931c53765a6bf8f356acd
obfuscated password: 444a4f701601137b7447745039566b03
p12 password (hex): 2b416f615a571a645f442766103d2334
--------------------------------------------------------
----------------------------------------------
Credential #1: ekoparty/EKO{vPgsSHXO0LiHlZk667Xr}@ekoparty

```

Flag: EKO{vPgsSHXO0LiHlZk667Xr}
