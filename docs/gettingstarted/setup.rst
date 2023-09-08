Installation
============

Ubuntu Operating System
--------------------------------------
You will need a laptop that can boot `Ubuntu 22.04 <https://releases.ubuntu.com/jammy/>`_. You can also choose to dual boot your current Windows computer,
i.e. have both Windows and Ubuntu installed on the same hard drive. It is recommended to have some knowledge of how operating systems are stored on the hard drive 
before doing this.

.. warning:: Using a Virtual Machine is not recommended. The ROS 2 middleware relies on network communications for which a Virtual Machine must be correctly configured to allow.

If you're looking for a used computer, check out the `UF Surplus website <https://surplus.ufl.edu/buy-now/>`_.

Common Issues
^^^^^^^^^^^^^
* Disable RST - Many manufacturers now put your storage into RAID mode instead of the standard AHCI mode. You can switch this in your BIOS, but there is a risk of bricking your windoes installation. We can install Ubuntu on a usb drive for you, you will need to have a minimum of a 128 GB drive.
* Disable Secure Boot - You can disable secure boot from your computers bios, should be under security or boot settings.
* Can't Boot into Bootable Drive - You've likely not created your bootable disk properly, if this problem persists, see the TA's, they have bootable drives available for use.


Python Installation and Required Packages 
-----------------------------------------------------
For some of our packages you may require certain extra packages. This section will take you through all the required packages.

Please run the following commands first before doing anything else.

.. code-block:: bash

    sudo apt update && sudo apt upgrade

First ensure python3 and pip are installed. This can be done through the following commands:

Python & pip
^^^^^^^^^^^^

.. code-block:: bash

    sudo apt install python3


.. code-block:: bash

    sudo apt install python3-pip

NumPy
^^^^^
You will also need NumPy for various things. They have arrays, array operations, etc. and are useful for efficient computing.

.. code-block:: bash

    pip3 install numpy

UTM Converter
^^^^^^^^^^^^^
We use a python installed UTM converter to convert from the Latitude and Longitude coordinates that we get from the GPS to UTM Easting and Northing coordinates.

.. code-block:: bash

    pip3 install utm


ROS 2 Installation and Configuration from Debian Packages
---------------------------------------------------------
These installation instructions are a direct copy from `ROS 2 Humble's installation page <https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html>`_

To install ROS 2 through debian packages is quite simple, if you wish to install through binary packages or build from source you can find those instructions on the ROS 2 Humble documentation website.

.. warning:: If you install ROS 2 Humble through building from source, we will provide no support or help for any issues you run into. The issues can be so varied and it is difficult to be informed on all of them.

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

Install ROS 2
^^^^^^^^^^^^^
Update your APT repository cache after setting up your repositories.

.. code-block:: bash

    sudo apt update

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.

.. code-block:: bash

    sudo apt upgrade

Desktop Install: ROS, RViz, demos, tutorials.

.. code-block:: bash

    sudo apt install ros-humble-desktop

Install Colcon.

.. code-block:: bash

    sudo apt install python3-colcon-common-extensions

Configuring the terminal (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want ROS 2 to be sourced everytime you open a terminal, run the following command:

.. code-block:: bash
    
    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
