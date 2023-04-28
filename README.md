<h1 align="center">Hi there, it is <a href="" target="_blank">Domino</a>'s source code  
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Let's start the project</h3>

[//]: # ([![Typing SVG]&#40;https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=/+//+///+////+/////+//////+///////&#41;]&#40;https://git.io/typing-svg&#41;</h3>)
[installer]: https://www.python.org/downloads/windows/

## Installation
### Windows
Install `python3.10` or later. You can use the Windows [installer][] of your choice.

### Linux
1. Install  `python3.10` or later. You can use the linux terminal for your installation.
2. Run the command `sudo apt update` in your linux terminal
3. Run the command `sudo apt install python3.10`
4. Check it with the command `python3 -version`. If you see the output like `Python 3.10`, you are done!

## Set up the project 
Create virtualenv

    python3 -m venv venv    [ Linux ]
    py -m venv venv    [ Windows ]

Enter the venv

    source venv/bin/activate    [ Linux ]
    source venv/Scripts/activate    [ Windows ]

Install required modules with requirements.txt

    (venv) pip install -r requirements.txt    [ Both Linux & Windows ]

Run the project

    python3 manage.py runserver    [ Linux ]
    py manage.py runserver    [ Windows ]