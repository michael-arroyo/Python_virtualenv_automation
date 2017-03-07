# Python Virtualenv Automation
## Overview
#### This project is intended to ease creating a new virtual environment for Python development. Currently the package works with Windows machines with planned Linux and OSX implementation.

## How it Works
#### The primary script, SetupEnv.py downloads virtualenv using pip, then creates a new virtual environment and installs necessary packages inside of the new environment as per requirements.txt.

## Usage
#### As a power-user call `python SetupEnv.py {name_of_env} {path/to/requirements}`
#### Defaults: Python_101 as name of env and requirements.txt 
#### This will create the env in the directory you run the script in.

#### If you do not wish for your env to be named Python_101, then pass the desired name as an argument from the command line.
#### If want to use your own custom requirements.txt then simply specify the path.