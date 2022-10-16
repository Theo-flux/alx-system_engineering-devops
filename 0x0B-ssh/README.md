# SSH

Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.
Resources

Read or watch:

1. [What is a (physical) server - text](https://alx-intranet.hbtn.io/rltoken/dkgW9lKiBRiUZHfq0MDJuw)
2. [What is a (physical) server - video](https://alx-intranet.hbtn.io/rltoken/AxFcTdcXUCsrVp01X_EbFA)
3. [SSH essentials](https://alx-intranet.hbtn.io/rltoken/ux0eM1QU9reNyG45b0erAQ)
4. [SSH Config File](https://alx-intranet.hbtn.io/rltoken/Rc9FpSy4ZaQWPlcWLinbNw)
5. [Public Key Authentication for SSH](https://alx-intranet.hbtn.io/rltoken/tOcxk5mtkedBM0WxyDZxTw)
6. [How Secure Shell Works](https://alx-intranet.hbtn.io/rltoken/j0atjRrVfZ6F810qmPfAzA)
7. [SSH Crash Course)](https://alx-intranet.hbtn.io/rltoken/FKqd8CjxExmpWGu6xGavKw)

For reference:
1. Understanding the SSH Encryption and Connection Process
2. Secure Shell Wiki
3. IETF RFC 4251 (Description of the SSH Protocol)
4. Internet Engineering Task Force
5. Request for Comments

man or help:
1. ssh
2. ssh-keygen
3. env

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

1. What is a server
2. Where servers usually live
3. What is SSH
4. How to create an SSH RSA key pair
5. How to connect to a remote host using an SSH RSA key pair
6. The advantage of using #!/usr/bin/env bash instead of /bin/bash

Copyright - Plagiarism

1. You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
2. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
3. You are not allowed to publish any content of this project.
4. Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted on Ubuntu 20.04 LTS
3. All your files should end with a new line
4. A README.md file, at the root of the folder of the project, is mandatory
5. All your Bash script files must be executable
6. The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
7. The second line of all your Bash scripts should be a comment explaining what is the script doing
