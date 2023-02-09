# XWrap-Qt
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) [![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

XWrap-Qt is a script made to use Live Wallpapers on LXQt.

## Installation
- ### Installation from Source
    - First of all you need to install Python 3, pip and git:
        - On Debian-Based Distros:
            ```
            sudo apt-get install python3 python3-pip git
            ```
        - On SUSE-Based Distros:
            ```
            sudo zypper in python3 python3-pip git
            ```
        - On RedHat-Based Distros:
            ```
            sudo dnf install python3 python3-pip git
            ```
             or
            ```
            sudo yum install epel-release
            sudo yum install python3 python3-pip git
            ```
        - On Arch-Based Distros:
            ```
            sudo pacman -S python python-pip git
            ```
     - Install required Python Modules with pip:
        ```
        pip install Pillow
        ```
     - Clone the Repository and go into the folder:
        ```
        git clone https://github.com/PokeMichele/XWrap-Qt.git && cd XWrap-Qt
        ```
     - Copy the Script File in a System Folder:
        ```
        sudo cp XWrap-Qt.py /usr/local/bin
        ```
     - Launch the Script for the first time to select the GIF file and the interval (in seconds) between 2 frames:
        ```
        sudo python3 /usr/local/bin/XWrap-Qt.py
        ```
     - In the future you can edit the configuration file to change these values (you can do it with a text editor like nano)
        ```
        nano /usr/local/bin/XWrap-Qt.conf
        ```
## FAQ
- Why when I change the interval between 2 small values (like 0,0000001s and 0,0000000001) I can't see any difference in speed?
    - There isn't actually a single answer to this question. We just know that it can vary according to the Monitor Refresh Rate, the general power of your System or, maybe, it could be a PCManFM-Qt Limitation.
## Credits & License
 - XWrap-Qt is made using Python and Pillow (PIL), is based on [PCManFM-Qt](https://github.com/lxqt/pcmanfm-qt) and it's released under [GPLv2 License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

