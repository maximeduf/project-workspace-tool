https://aaronlelevier.github.io/virtualenv-cheatsheet/

# install python
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.13
sudo apt-get install python3.13-dev
sudo apt-get install build-essential

# installs PIP globally
curl https://bootstrap.pypa.io/get-pip.py | python3.13

# install python virtual environment
sudo apt-get install python3.13-venv

# creates a virtualenv
python3.13 -m venv venv

# activates the virtualenv
source venv/bin/activate

# to deactive venv
deactivate
