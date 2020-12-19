# rtsp-opencv-sink
This repository shares the sample code for receiving rtsp stream using opencv. 


# Installation

```
python3 -mpip install numpy
python3 -m pip install opencv-python
```

## additional installations
In case you get a warning: `Failed to load module "canberra-gtk-module"`, run following
```
sudo apt-get update
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module
```

# Usage
Go to project root and run 
```
python3 main.py
```
For a list of additional commans run
```
python3 main.py --help
```
To add 2000 ms delay and run a particular stream, run
```
python3 main.py --delay 2000 --address http://46.151.101.134:8082/?action=stream
```

# Dev notes
## sample streams
```
http://46.151.101.134:8082/?action=stream
```