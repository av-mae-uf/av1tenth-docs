Building the AV1tenth Car
=========================


To build the 1/10th Car you will need to first have all the parts listed `here <parts.html>`_. We will not include instructions on putting the chassis together,
the Injora chassis will require the wheels and front bumber to be mounted on.

Tools Required
^^^^^^^^^^^^^^^

You will need a couple of tools and the knowledge of how to use them. The tools are listed below:

* Crimpers
* Soldering Iron & Solder
* 3D Printer
* Screw and Hex Bit Drivers
* Multimeter (Useful for checking connections)
* Wire Strippers
* Drill and Drill Bits
* Double Sided and Electrical Tape

Chassis Attachments and Build
------------------------------

Sensor Board Assembly
---------------------

Odroid Installation
--------------------

You will need to download the Linux distro called `Armbian <https://www.armbian.com/>`_. 
We are using the focal version of armbian for the Odroid N2+ which can be found `here <https://www.armbian.com/odroid-n2/>`__.

You will need to switch your board into SPI mode and boot the Odroid. You will then need some esort of ISO writer, like `balenaEtcher <https://www.balena.io/etcher/>`_.
Once you have booted into SPI mode, you will have to enter a couple of commands to make your drive into a writeable media. First, when it boots into Petitboot
you must select ``Exit To Shell`` . Then enter the following:

Check for storage devices available with the name ``mmc``

.. code-block:: bash

    ls /dev/mmc*

Then to enable write mode, enter the following:

.. code-block:: bash

    ums <name-of-storage-device>

usually this would be ``/dev/mmcblk0`` on the Odroid N2+. You should now be able to flash the image you downloaded earlier. Once you have done that and it is flashed, you should
be able to setup Armbian. Follow the `Instructions Page <../gettingstarted/installation.html>`_ to install ROS and other required packages.

 
