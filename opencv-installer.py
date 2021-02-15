commands = ["sudo rpi-eeprom-update", "sudo rpi-eeprom-update -a", "sudo reboot", "sudo apt-get update", "sudo apt-get upgrade", "sudo apt-get install cmake gfortran",
            "sudo apt-get install libjpeg-dev libtiff-dev libgif-dev", "sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev",
            "sudo apt-get install libgtk2.0-dev libcanberra-gtk*", "sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev",
            "sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev", "sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev",
            "sudo apt-get install libjasper-dev liblapack-dev libhdf5-dev", "sudo apt-get install protobuf-compiler", "cd ~"
            "wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip", "wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip",
            "unzip opencv.zip", "unzip opencv_contrib.zip", "mv opencv-4.5.0 opencv", "mv opencv_contrib-4.5.0 opencv_contrib", "echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7" >> ~/.bashrc",
            "source ~/.bashrc", "sudo pip3 install virtualenv", "sudo pip3 install virtualenvwrapper", "echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc",
            "echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc", "source ~/.bashrc", "mkvirtualenv cv450", "pip3 install numpy", "cd ~/opencv/", "mkdir build", "cd build",
            "cmake -D CMAKE_BUILD_TYPE=RELEASE \\
        -D CMAKE_INSTALL_PREFIX=/usr/local \\
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \\
        -D ENABLE_NEON=ON \\
        -D ENABLE_VFPV3=ON \\
        -D WITH_OPENMP=ON \\
        -D BUILD_TIFF=ON \\
        -D WITH_FFMPEG=ON \\
        -D WITH_TBB=ON \\
        -D BUILD_TBB=ON \\
        -D BUILD_TESTS=OFF \\
        -D WITH_EIGEN=OFF \\
        -D WITH_V4L=ON \\
        -D WITH_LIBV4L=ON \\
        -D WITH_VTK=OFF \\
        -D WITH_QT=OFF \\
        -D OPENCV_ENABLE_NONFREE=ON \\
        -D INSTALL_C_EXAMPLES=OFF \\
        -D INSTALL_PYTHON_EXAMPLES=OFF \\
        -D BUILD_NEW_PYTHON_SUPPORT=ON \\
        -D BUILD_opencv_python3=TRUE \\
        -D OPENCV_GENERATE_PKGCONFIG=ON \\
        -D BUILD_EXAMPLES=OFF ..", "make -j4", "sudo make install", "sudo ldconfig", "make clean", "sudo apt-get update", "cd ~", "rm opencv.zip", "rm opencv_contrib.zip", "sudo reboot",
            "cd ~/.virtualenvs/cv450/lib/python3.7/site-packages", "ln -s /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so",
            "cd ~", "cd ~/opencv/build/lib/", "sudo cp cv2.so /usr/local/lib/python2.7/dist-packages/cv2/python-2.7", 
            "cd ~/opencv/build/lib/python3", "sudo cp cv2.cpython-37m-arm-linux-gnueabihf.so \ /usr/local/lib/python3.7/dist-packages/cv2/python-3.7", "cd ~/opencv",
            "sudo rm -r build", "sudo rm -rf ~/opencv", "sudo rm -rf ~/opencv_contrib"]

while (True):
    f = open("install.dat", "r")
    num = f.read()
    f.close()
    if(command[num] == "sudo reboot"):
        f = open("install.dat", "w")
        f.write(num+1)
        f.close()
        #execute command with id '3'
    elif (len(commands) - num != 0:
        f = open("install.dat", "w")
        f.write(num+1)
        f.close()
        #execute command with id 'num'
    else:
        #delete file
