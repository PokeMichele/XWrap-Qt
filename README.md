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
        cp Xwrap-Qt.py /usr/sbin
        ```
     - Launch the Script for the first time to select the GIF file and the interval (in seconds) between 2 frames:
        ```
        python3 /usr/sbin/XWrap-Qt.py
        ```
     - In the future you can edit the configuration file to change these values (you can do it with a text editor like nano)
        ```
        nano /usr/sbin/XWrap-Qt.conf
        ```
## FAQ
- Why when I change the interval between 2 small values (like 0,000001s and0,0001) can't see any difference in speed?
    - There isn't actually a single answer to this question. We just know that it can vary according to the Monitor Refresh Rate, the general power of your System or maybe it could be a PCManFM-Qt Limitation.
## Credits & License
 - SpineGTK is made using Python, PyQt5 and some other Python Modules, wraps [py_spec](https://github.com/rctcwyvrn/py_spec) with a GUI and it's released under [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0).

