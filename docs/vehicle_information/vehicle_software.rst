Vehicle Software
----------------
Checklist:
* Install/Update Odroid Ubuntu Mate
* Install Python Modules
* Install ROS 2 and dependencies
* Add user to dialout group


Odroid Ubuntu Mate
==================
Hardkernel releases their own `customized Ubuntu Mate distributions <https://wiki.odroid.com/odroid-n2/os_images/ubuntu>`_ for their Odroid hardware.
Choose the distributions that aligns with your choice of ROS 2 version. They provide a `list of softwares for flashing the OS onto a memory device <https://wiki.odroid.com/troubleshooting/odroid_flashing_tools>`_.
The Odroid-N2+ (which is currently being used) utlizes a eMMC memory chip. You will need a special USB-A to eMMC adapter in order to flash the OS onto it.

After a fresh install, it is recommended to perform an update of the software.

.. code-block:: bash

    sudo apt update

Upgrade installed software to the latest versions.

.. code-block:: bash

    sudo apt upgrade

Git Installation
^^^^^^^^^^^^^^^^
Git is required to pull the repository that contains the ROS 2 nodes to interface with the hardware on the vehicle.

.. code-block:: bash

    sudo apt install git


Python Modules
==============
NumPy
^^^^^
You will also need NumPy for various things. They have arrays, array operations, etc. and are useful for efficient computing.

.. code-block:: bash

    pip3 install numpy

PySerial
^^^^^^^^
Install PySerial, this is the package that allows us to communicate serially with connected devices.

.. code-block:: bash

    pip3 install pyserial

UTM Converter
^^^^^^^^^^^^^
We use a python installed UTM converter to convert from the Latitude and Longitude coordinates we get from the GPS to UTM Easting and Northing coordinates.

.. code-block:: bash

    pip3 install utm

CRC
^^^
The motor carrier driver uses CRC to ensure message integrity between the nano motor carrier and the driver on the Odroid-N2+.

.. code-block:: bash

    pip3 install crc

Adafruit GPS Library
^^^^^^^^^^^^^^^^^^^^
An adafruit gps library is used to interface with the GPS module that is onboard the vehicle.

.. code-block:: bash
    
    pip3 install adafruit-circuitpython-gps


ROS 2 Installation and Configuration from Debian Packages
=========================================================
These installation instructions are a direct copy from `ROS 2 Humble's installation page <https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html>`_

Setup Sources
^^^^^^^^^^^^^
You will need to add the ROS 2 apt repositories to your system. First ensure that the Ubuntu Universe repository is enabled:

.. code-block:: bash

    sudo apt install software-properties-common
    sudo add-apt-repository universe

Install curl (if it is not already installed):

.. code-block:: bash

    sudo apt update && sudo apt install curl -y

Add the GPG key:
    
.. code-block:: bash

    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

Add the repository to your sources list:

.. code-block:: bash

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Install ROS 2 and additional packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Update your APT repository cache after setting up your repositories.

.. code-block:: bash

    sudo apt update

Base install of ROS 2 Humble:

.. code-block:: bash

    sudo apt install ros-humble-ros-base

Install Colcon:

.. code-block:: bash

    sudo apt install python3-colcon-common-extensions

Install RPLidar Driver:

.. code-block:: bash

    sudo apt install ros-humble-rplidar-ros

Install Ackermann messages:

.. code-block:: bash

    sudo apt install ros-humble-ackermann-msgs


Configuring the terminal (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want ROS 2 to be sourced everytime you open a terminal, run the following command:

.. code-block:: bash
    
    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc


UDEV Rules
==========
To allow us to communicate with our USB devices attached to the Odroid easily, we have set up some UDEV rules to make sure the ports are interchanged on startup. 
Start by running the following command to create a new rules file:

.. code-block:: bash

    sudo nano /etc/udev/rules.d/99-sensor.rules

Then you need to paste in the following rules (ctrl-shift-v):

.. code-block:: bash

    SUBSYSTEMS=="tty", KERNEL=="ttyS1" ACTION=="add", MODE="0666", GROUP="dialout", SYMLINK+="sensor/gps"

    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="8057",MODE="0666", GROUP="dialout", SYMLINK+="sensor/arduino"
    
    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="0001", MODE="0666", GROUP="dialout", SYMLINK+="sensor/lidar"

Save and exit the file. Then run the following:

.. code-block:: bash

    sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger

You will need to replug all your usb ports or reboot the Odroid for the Udev rules to take effect.


Dialout Group
=============
Add your default user to the dialout user-group in order to send data out of a serial port.

.. code-block:: bash

    sudo usermod -aG dialout USERNAME_HERE