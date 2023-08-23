Vehicle Software
----------------

Odroid Ubuntu Mate
==================


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