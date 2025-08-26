Installing Ubuntu
=================

Here is a list of various ways to install Ubuntu. Going from most recommended to least and then to unverified methods. 

.. important::
    It is perfectly normal and understandable if you prefer not to install Ubuntu on your own. This guide is for anyone who is interested.
    Feel free to message the TA or visit TA office hours to get help installing Ubuntu.
    Instead, use this page to decide how you would like to install Ubuntu on your system with the TA or simply to learn the process.

.. note::
    Only one of your teammates needs a laptop with Ubuntu installed. However, if that teammate is absent during a class, it could set you back significantly.
    It is strongly recommended that at least two teammates have Ubuntu installed natively (either dual-booted or on a dedicated laptop).
    The remaining teammate may use a virtual machine for coding support, but virtual machines usually cannot connect to the car due to ROS 2 middleware network issues.

Before Installing
-----------------

Before installing Ubuntu, you must first download the Ubuntu ISO file. You can find the Ubuntu 22.04 ISO `here <https://releases.ubuntu.com/jammy/>`_.

- If you are using a virtual machine, you can skip ahead to the Virtual Machine section.  
- If you are installing on physical hardware, you will need to create a bootable USB drive. Tools such as `Rufus <https://rufus.ie/>`_ (Windows) or `Etcher <https://etcher.balena.io/>`_ (Windows/macOS/Linux) are commonly used.


Method 1: Wipe a Cheap Laptop and Install Ubuntu
------------------------------------------------

The simplest and most reliable way is to install Ubuntu as the only operating system on a spare laptop.  

- If you need affordable hardware, check out the `UF Surplus website <https://surplus.ufl.edu/buy-now/>`_.  
- Ubuntu is lightweight compared to Windows and runs well on older hardware. Even older laptops should handle ROS 2 Humble adequately.

Steps (High Level)
^^^^^^^^^^^^^^^^^^

1. Create a bootable USB with the Ubuntu 22.04 ISO.  
2. Boot the laptop from the USB drive.  
3. Select *Erase disk and install Ubuntu* on the Installation type page.
4. Follow the on-screen installation instructions.  

Here is a video on `how to do clean wipe install <https://www.youtube.com/watch?v=oNEwEQ0uU1Y>`_:

.. raw:: html

    <div style="text-align: center;">
      <iframe width="560" height="315" 
              src="https://www.youtube-nocookie.com/embed/oNEwEQ0uU1Y" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>


Common Issues
^^^^^^^^^^^^^
* Can't Boot into Bootable Drive - You've likely not created your bootable disk properly, if this problem persists, see the TA's, they have bootable drives available for use.

Method 2: Dual Booting on a Separate Drive
------------------------------------------

If your computer has multiple drives (for example, a second SSD or HDD), you can install Ubuntu 22.04 on one drive and keep Windows on the other.  

You only need about a 64GB drive, but 128 GB would be safe.

- This is a clean and safe option because it keeps the operating systems fully isolated.  
- During installation, choose the correct drive for Ubuntu to avoid overwriting Windows.  

In a previous semester, a student bought a high-speed USB 3.0-C drive — `such as this one <https://www.amazon.com/SAMSUNG-Type-CTM-Transfers-Compatible-Waterproof/dp/B09WB2NL8W>`_ — and used it as their Ubuntu drive. As long as you don't accidentally eject the USB, it should work fine, but do be careful!
As mentioned earlier, you only need a 64GB drive, but 128GB would be safer.

Steps (High Level)
^^^^^^^^^^^^^^^^^^

1. Create a bootable USB with the Ubuntu 22.04 ISO.  
2. Boot the laptop from the USB drive.  
3. Select *Erase disk and install Ubuntu* on the Installation type page.
4. Select the correct disk, pay attention: if it is a new drive, it should only have one partition.
5. Follow the on-screen installation instructions.  


Here are two videos on how to install Ubuntu on a separate drive. Both videos aren't perfect but follow a similar path.

`Video 1 — skip from 2:00 to 3:08 (we do not advise disabling booting off your Windows partition) <https://www.youtube.com/watch?v=KX85vZ3ANVk>`_:

.. raw:: html

    <div style="text-align: center;">
      <iframe width="560" height="315" 
              src="https://www.youtube-nocookie.com/embed/KX85vZ3ANVk" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>


`Video 2 — some parts are blurry and include clips from same-drive dual booting; the steps are fairly similar <https://www.youtube.com/watch?v=0BLFJL6UlOE>`_:

.. raw:: html

    <div style="text-align: center;">
      <iframe width="560" height="315" 
              src="https://www.youtube-nocookie.com/embed/0BLFJL6UlOE" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>


Common Issues
^^^^^^^^^^^^^
* Disable Secure Boot - You can disable secure boot from your computers bios, should be under security or boot settings.
* Can't Boot into Bootable Drive - You've likely not created your bootable disk properly, if this problem persists, see the TA's, they have bootable drives available for use.

Method 3: Dual Booting on the Same Drive as Windows
---------------------------------------------------

This is more complex than Method 2 because Ubuntu and Windows share the same disk.

- You must shrink your Windows partition using the Windows Disk Management tool to free space for Ubuntu.
- Over the years, Windows has made it harder and harder to shrink the partition, which is why this is later on the list.
- During installation, choose the *Install Ubuntu alongside Windows* option.


Steps (High Level)
^^^^^^^^^^^^^^^^^^

1. Shrink your Windows partition, leaving at least 64GB of free space.
2. Create a bootable USB with the Ubuntu 22.04 ISO.
3. Boot the laptop from the USB drive.
4. On the Installation type page, select *Something else*.
5. Select the *free space* entry after a large *ntfs* partition — this should match the space you freed earlier.
6. Select *Windows Boot Manager* as the device for boot loader installation.
7. Follow the on-screen installation instructions.

.. warning::
   If partitions are set up incorrectly, you risk losing Windows data. Make sure to back up important files before attempting this.

Here is a video on `how to dual boot Ubuntu on the same drive <https://www.youtube.com/watch?v=GXxTxBPKecQ>`_:

.. raw:: html

    <div style="text-align: center;">
      <iframe width="560" height="315" 
              src="https://www.youtube-nocookie.com/embed/GXxTxBPKecQ" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>


Common Issues
^^^^^^^^^^^^^

* Disable RST - Many manufacturers now put your storage into RAID mode instead of the standard AHCI mode. You can switch this in your BIOS, but there is a risk of bricking your Windows installation. We can install Ubuntu on a USB drive for you, you will need to have a minimum of a 128 GB drive.
* Disable Secure Boot - You can disable secure boot from your computers bios, should be under security or boot settings.
* Can't Boot into Bootable Drive - You've likely not created your bootable disk properly, if this problem persists, see the TA's, they have bootable drives available for use.

Method 4: Linux Docker Container
--------------------------------

If you are using a newer version of Ubuntu (for example, Ubuntu 24.04), ROS 2 Humble will not install directly because ROS 2 releases are OS-dependent.
However, this is more advanced than the other methods, which is why it is lower on the list.

Instead of downgrading your OS, you can create a Docker container running Ubuntu 22.04 with ROS 2 Humble.

- This method has been tested by the TA and works if you give the container the correct privileges (such as networking and hardware access).
- You may need to run Docker with flags like ``--net=host`` and pass USB devices explicitly to connect to hardware.
- The only reported issue at the moment is that sometimes the container loses access to USB devices and needs to be restarted.

TODO: add instructions

Installing Docker
^^^^^^^^^^^^^^^^^

TODO

Getting the ROS 2 Humble image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Setting up the Docker Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO: 
Here is a quick command to create the ROS 2 docker container

.. code-block:: bash

   docker run -it -d --name ros2_humble \
       --restart unless-stopped \
       --network host \
       --privileged \
       -e DISPLAY \
       -e QT_X11_NO_MITSHM=1 \
       -e ROS_DOMAIN_ID=0 \
       -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
       -v "$HOME/humble_ws:/root/humble_ws" \
       --device=/dev/input/js0 \
       --device=/dev/input/event0 \
       -w /root \
       osrf/ros:humble-desktop

Notes:

- On Linux hosts, you may need to allow X11: ``xhost +local:root`` (and later ``xhost -local:root``).
- Replace the ``--device=`` paths with the actual devices you need (e.g., USB-to-serial adapters).
- If USB devices stop working, restart the container: ``docker restart ros2_humble``.


Method 5: Virtual Machine
-------------------------

You can also install Ubuntu 22.04 inside a virtual machine (using software like VirtualBox or VMware).  

- This method is useful for teammates who only need to write and test code.  
- However, virtual machines generally cannot connect to the car due to networking limitations.  

Here is a video on `how to set up an Ubuntu VM using VirtualBox <https://www.youtube.com/watch?v=rJ9ysibH768>`_:

.. raw:: html

    <div style="text-align: center;">
      <iframe width="560" height="315" 
              src="https://www.youtube-nocookie.com/embed/rJ9ysibH768" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>


Untested Method: WSL Docker Container
-------------------------------------

Windows Subsystem for Linux (WSL) with Docker support could, in theory, run ROS 2 Humble in a container. This removes the need to dual boot or get a second laptop.

However:

- This method has **not been tested** with the car.
- Networking and USB device support in WSL are known to be limited.

If you are willing to try this method, please talk with the TA so we can flesh this section out.
