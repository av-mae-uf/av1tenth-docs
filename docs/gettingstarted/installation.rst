Installation
============

Before you can go ahead and start developing or use any of our packages, you will need to install certain things. 
Obviously you will need to install some sort of linux platform that ideally can install from debain packages. 

Ubuntu Installation
-------------------
You can follow the instructions at `Ubuntu Dual Boot <https://medium.com/linuxforeveryone/how-to-install-ubuntu-20-04-and-dual-boot-alongside-windows-10-323a85271a73>`_ to dual boot your computer. If you are having trouble doing this come talk to the TA's, we can help you install Ubuntu.

Common Issues
^^^^^^^^^^^^^

* Disable RST - Many manufacturers now put your storage into RAID mode instead of the standard AHCI mode. You can switch this in your BIOS, but there is a risk of bricking your windoes installation. We can install Ubuntu on a usb drive for you, you will need to have a minimum of a 128 GB drive.
* Disable Secure Boot - You can disable secure boot from your computers bios, should be under security or boot settings.
* Can't Boot into Bootable Drive - You've likely not created your bootable disk properly, if this problem persists, see the TA's, they have bootable drives available for use.



Python Installation and Additional Packages Required
-----------------------------------------------------

For some of our packages you may require certain extra packages. This section will take you through all the required packages.

Please run the following commands first before doing anything else.

.. code-block:: bash

    sudo apt update && sudo apt upgrade

First ensure pip is installed and python3 is installed. This can be done through the following commands. For ``python3``:

Python & pip
^^^^^^^^^^^^

.. code-block:: bash

    sudo apt install python3

To install ``pip``:

.. code-block:: bash

    sudo apt install python3-pip

NumPy
^^^^^
You will also need NumPy for various things. They have arrays, array operations, etc. and are useful for efficient computing. To install this you can run the command

.. code-block:: bash

    python3 -m pip install numpy

PySerial
^^^^^^^^

Once you have these two installed, we can further install a couple of other packages that we require. First we will install PySerial, this is the package that allows us to communicate serially with connected devices.

.. code-block:: bash

    python3 -m pip install pyserial

UTM Converter
^^^^^^^^^^^^^

We use a python installed UTM converter to convert from the Latitude and Longitude data we get from the GPS to UTM Easting and Northing. It can be installed by the following command.

.. code-block:: bash

    python3 -m pip install utm

Git Installation and Configuration
-----------------------------------

To install git you will need to open the terminal and enter the following commands.

.. code-block:: bash

    sudo apt install git

This command will install git from the APT tool usually installed in most linux distros by default. Once installed you will need to configure a few things. To do this run the following commands:

.. code-block:: bash

    git config --global user.name "FirstName LastName"
    git config --global user.email "email@email.com"

This should mostly setup whatever you need till the first time you push a repository to whichever Git distributor you are using. 
Then it will ask for a user name and password, generally we use GitHub which requires a Personal Access Token which you can generate
under Settings -> Developer Settings -> and Personal Access Tokens. To ensure you don't need to keep entering this on your computer you can run
the following command

.. code-block:: bash 

    git config --global credential.helper store

This will store your access token with the local git so you don't have to keep re-entering it.


Visual Studio Code Installation
-------------------------------

To install vscode you can run the following command, though sometimes you have to download it from their website and run another command which is given after.

.. code-block:: bash

    snap install code

If this does not work, go to the `Visual Studio Code website <https://code.visualstudio.com/Download>`_ and download the linux package. Then you can run the follwing command to install it.

.. code-block:: bash

    cd Downloads && sudo dpkg -i <package_name.deb>

.. note:: Please change the ``package_name.deb`` to what ever your package is named.

This should be all you need to run everything that we have provided.

ROS2 Installation and Configuration from Debian Packages
--------------------------------------------------------

These installation instructions are a direct copy from `ROS2 Foxy's installation page <https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html>`_

To install ROS2 through debian packages is quite simple, if you wish to install through binary packages or build from source you can find those instructions on the ROS2 Foxy documentation website.

.. warning:: If you install ROS2 Foxy through building from source, we will provide no support or help for any issues you run into as they can be so varied and is difficult to be informed on all of them.

Set Locale
^^^^^^^^^^

Make sure you have a locale which supports ``UTF-8``.
If you are in a minimal environment (such as a docker container), the locale may be something minimal like ``POSIX``.
We test with the following settings. However, it should be fine if you're using a different UTF-8 supported locale.

.. code-block:: bash

   locale  # check for UTF-8

   sudo apt update && sudo apt install locales
   sudo locale-gen en_US en_US.UTF-8
   sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
   export LANG=en_US.UTF-8

   locale  # verify settings

Setup Sources
^^^^^^^^^^^^^

You will need to add the ROS 2 apt repositories to your system. To do so, first authorize our GPG key with apt like this:

.. code-block:: bash

    sudo apt update && sudo apt install curl gnupg2 lsb-release
    
.. code-block:: bash

    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

And the add the repository to your sources list:

.. code-block:: bash

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Install ROS2 Packages
^^^^^^^^^^^^^^^^^^^^^

Update your APT repository cache after setting up your repositories.

.. code-block:: bash

    sudo apt update

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.

.. code-block:: bash

    sudo apt upgrade

Desktop Install (Recommended): ROS, RViz, demos, tutorials.

.. code-block:: bash

    sudo apt install ros-foxy-desktop

That's pretty much it, all base packages are now installed. We do use a certain package to comminucate with the RPLiDAR, that can be installed using the following command:

.. code-block:: bash

    sudo apt install ros-foxy-rplidar-ros

This should allow it to directly be installed into the ROS2 directory and build the package.

Configuring ROS2 to Source Everytime a Terminal is Opened
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following command sources ROS2. Though everytime you want to run any package or anything in ROS for that matter you need to run it.

.. code-block:: bash

    source /opt/ros/foxy/setup.bash

Though if you want it to be sourced everytime you open a terminal, run the following command:

.. code-block:: bash
    
    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
Installing Colcon
^^^^^^^^^^^^^^^^^

Sometimes when ROS2 is installed, it doesn't install ``colcon`` the package builder. To install this you can run the following command.

.. code-block:: bash

    sudo apt install python3-colcon-common-extensions

UDEV Rules
----------

To allow us to communicate with our USB devices easily, we have set up some UDEV rules to make sure the ports are interchanged on startup. To do this on your car you need to run the following commands

.. code-block:: bash

    sudo nano /etc/udev/rules.d/99-sensor.rules

Then you need to paste in the following rules

.. code-block:: 

    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="1456", MODE="0666", GROUP="dialout", SYMLINK+="sensor/imu"

    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="0001", MODE="0666", GROUP="dialout", SYMLINK+="sensor/lidar"

    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}==“239a”, ATTRS{idProduct}==“80cb”, MODE="0666", GROUP="dialout", SYMLINK+="sensor/encoder”


Then run the following to set them up.

.. code-block:: bash

    sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger


You will need to replug all your usb ports or just reboot your Odroid for these to work.






