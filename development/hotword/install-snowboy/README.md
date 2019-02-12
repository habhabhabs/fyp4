# Compiling `snowboy` binaries for Ubnutu 18.04
---
As the official `snowboy` binaries is only up to Ubuntu 14.04 on [it's webpage,](http://docs.kitt.ai/snowboy/#introduction) and Ubuntu 14.04 LTS ending support [until April 2019,](https://wiki.ubuntu.com/Releases), it would be a viable option to build the `snowboy` libraries from Ubuntu 18.04 as it is the latest LTS version and would be supported for the next five years. 

# Guide credits to: [WorldOfPython YouTube](https://www.youtube.com/watch?v=mUEm05ZAhhI)

1."""Install Packages"""
```sudo apt-get install python-pyaudio python3-pyaudio sox libpcre3 libpcre3-dev libatlas-base-dev &&
sudo pip3 install pyaudio
```

2."""Compile a supported `swig` version (3.0.10 or above)"""
Create path `snowboy` and open it in terminal
```mkdir snowboy
cd snowboy
```

```sudo su


wget http://downloads.sourceforge.net/swig/swig-3.0.10.tar.gz &&
tar -xvzf swig-3.0.10.tar.gz &&
cd swig-3.0.10/ &&   
./configure --prefix=/usr                  \
        --without-clisp                    \
        --without-maximum-compile-warnings &&
make &&
make install &&
install -v -m755 -d /usr/share/doc/swig-3.0.10 &&
cp -v -R Doc/* /usr/share/doc/swig-3.0.10 &&
cd ..
```

3."""Compile"""
```git clone https://github.com/Kitt-AI/snowboy &&
cd snowboy/swig/Python3 && make
```
Open `/snowboy/snowboy/examples/Python3/snowboydecoder.py`
Change from `from . import snowboydetect` to `import snowboydetect`
Save it


4."""How to use""
Copy files from `/snowboy/snowboy/swig/Python3` to your project
Copy path `resources` from `/snowboy/snowboy` to your project `path`
Copy file `snowboydecoder.py` from `/snowboy/snowboy/examples/Python3` to your project `path`
Open `https://snowboy.kitt.ai/` , login & register ,create and download your voice model
Copy your voice model to project `path`
Now you can use snowboy module in python file from this `path`
