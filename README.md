TrainStalker
============

Real time display of next departures at the nearest train station (France)


Requirements
------------
# Use python3

sudo apt-get install python-software-properties
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.4-dev

mkdir -p ~/.virtualenv/trainstalker
pyvenv-3.4 ~/.virtualenv/trainstalker
. ~/.virtualenv/trainstalker/bin/activate

# Ensure pip is installed
python3.4 -m ensurepip --upgrade

```
~/.virtualenv/trainstalker/local/bin/pip install  -r requirements.txt 
```
Run script
----------
```
python3.4 trains.py
```
