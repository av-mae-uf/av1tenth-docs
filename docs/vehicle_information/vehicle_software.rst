Vehicle Software
----------------

Odroid Ubuntu Mate
==================


Python Modules
==============
NumPy
^^^^^
You will also need NumPy for various things. They have arrays, array operations, etc. and are useful for efficient computing. To install this you can run the command

.. code-block:: bash

    pip3 install numpy

PySerial
^^^^^^^^

Once you have these two installed, we can further install a couple of other packages that we require. First we will install PySerial, this is the package that allows us to communicate serially with connected devices.

.. code-block:: bash

    pip3 install pyserial

UTM Converter
^^^^^^^^^^^^^

We use a python installed UTM converter to convert from the Latitude and Longitude data we get from the GPS to UTM Easting and Northing. It can be installed by the following command.

.. code-block:: bash

    pip3 install utm

CRC
^^^

The motor carrier driver uses CRC to ensure message integrity between the nano motor carrier and the driver  on the Odroid N2+.


.. code-block:: bash

    pip3 install crc

Adafruit GPS Library
^^^^^^^^^^^^^^^^^^^^

An adafruit gps library is used to interface with the gps module that is onboard the car.

.. code-block:: bash
    
    pip3 install adafruit-circuitpython-gps


ROS 2 Packages
==============

RPLidar ROS 2 Driver
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    sudo apt install ros-humble-rplidar-ros

Ackermann Messages
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    sudo apt install ros-humble-ackermann-msgs


UDEV Rules
=========================================

To allow us to communicate with our USB devices attached to the Odroid easily, we have set up some UDEV rules to make sure the ports are interchanged on startup. 
To do this on your car you need to run the following commands

.. code-block:: bash

    sudo nano /etc/udev/rules.d/99-sensor.rules

Then you need to paste in the following rules

.. code-block:: bash

    SUBSYSTEMS=="tty", KERNEL=="ttyS1" ACTION=="add", MODE="0666", GROUP="dialout", SYMLINK+="sensor/gps"

    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="8057",MODE="0666", GROUP="dialout", SYMLINK+="sensor/arduino"
    
    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="0001", MODE="0666", GROUP="dialout", SYMLINK+="sensor/lidar"


Then run the following to set them up.

.. code-block:: bash

    sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger


You will need to replug all your usb ports or just reboot your Odroid for these to work.