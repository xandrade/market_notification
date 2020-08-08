# market_notification
Stock Market Notification

# Linux (Ubuntu-20.04) through WSL 2

1. Go to the project folder, for example: `andrade@dell:/mnt/c/Users/andra$` `cd "/mnt/d/Dropbox/Python Projects/api_server"`
2. Create virtual enviroment: `andrade@dell:/mnt/d/Dropbox/Python Projects/api_server$` `python3 -m venv .venv`
3. Activte enviroment: `andrade@dell:/mnt/d/Dropbox/Python Projects/api_server$` `source .venv/bin/activate`
4. After the virtual environment is active, we are going to want to ensure that a couple of essential Python packages within the virtual environment are up to date: `(.venv) andrade@dell:/mnt/d/Dropbox/Python Projects/api_server$` `pip install -U setuptools pip`
5. Install the requirements: `(.venv) andrade@dell:/mnt/d/Dropbox/Python Projects/api_server$` `pip install quart`
6. Open VSCode `(.venv) andrade@dell:/mnt/d/Dropbox/Python Projects/api_server$` `code .`

# Docker

1. cd "/mnt/d/Dropbox/Python Projects/api_server"
2. docker build -t api-server-app .
3. docker run -dp 5000:5000 api-server-app


## Create Terminal Shortcuts
https://lifehacker.com/create-terminal-shortcuts-270799

1. `sudo vim ~/.bashrc`
2. Under the section caled `# some more ls aliases`, add:
- `alias update='sudo apt-get update -y| sudo apt-get upgrade -y'`
- `alias api_server='cd "/mnt/d/Dropbox/Python Projects/api_server" && source .venv/bin/activate'``


## Creating systemd service
1. `andrade@dell:` `cd /etc/systemd/system`
2. `sudo vim restfulapi.service`
3. Add following config
```
[Unit]
Description=RESTful API (Server) for ForeSite
After=network.target

[Service]
ExecStart=/mnt/d/Dropbox/Python Projects/api_server/app.py
Restart=Always
WorkingDirectory=/mnt/d/Dropbox/Python Projects/api_server

[Install]
WantedBy=multi-user.target
```
Vim Save And Quit The Editor Command
The procedure to save a file in vim / vi and quit the editor is as follows:

Open the terminal application in Linux or Unix
Next, open a file in vim / vi, type: vim filename
To save a file in Vim / vi, press Esc key, type `:w` and hit Enter key
One can save a file and quit vim / Vi by pressing `Esc` key, type `:x` and hit Enter key


4. `sudo systemctl enable restfulapi`






# Windows

## Preparing the enviroment
Before creating the conda enviroment, let's update conda:

`conda update --all`

Create conda enviroment:

`conda create -n api_server python=3.8`

Activating conda enviroment:

`activate api_server`

Installing requirements:

1. `conda install install quart`


To open VSCode type `code` inside the activate conda enviroment

Copy repository link and add to VSCode: Shift + Control + P -> Git: Clone -> url, select project forder (a folder called Fahud will be created). When completed, click to add project to the enviroment

# Postmaster docs

https://web.postman.co/collections/2163808-8b37fce9-eb9e-01e3-ec12-82e65b779eca?workspace=ccd6f0d5-a093-4262-88cb-c97c0dad5eda#introduction

