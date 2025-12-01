Troubleshooting
===============

If you have any issues, this page might be able to help you solve some common issues that you may face.

SSH Troubleshooting
^^^^^^^^^^^^^^^^^^^

The vehicles each contain a ``TP-Link N300 Travel Router`` to provide a local intranet network for SSH access and ROS communication.

All cars use the same IP address: ``192.168.0.100``.  
This means every car can be SSH'd into using the same command structure.

Connecting to the Vehicle
-------------------------

1. Connect to the car’s Wi-Fi network.  
   The login credentials are printed on the TP-Link device.

2. Once connected, open a terminal and enter:

   .. code-block:: bash

      ssh <vehicle-user>@192.168.0.100

Most vehicle usernames match the car’s name in lowercase (e.g. ``duffy``, ``tlustty``, ``snider``).

Handling SSH Host Key Errors
----------------------------

If you encounter a warning similar to the following:

.. code-block:: bash

   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
   Someone could be eavesdropping on you right now (man-in-the-middle attack)!
   It is also possible that a host key has just been changed.
   The fingerprint for the RSA key sent by the remote host is
   <fingerprint_here>.
   Please contact your system administrator.
   Add correct host key in /home/<user>/.ssh/known_hosts to get rid of this message.
   Offending ECDSA key in /home/<user>/.ssh/known_hosts:<line_number>
     remove with:
     ssh-keygen -f "/home/<user>/.ssh/known_hosts" -R "<ip_address>"
   Host key for <ip_address> has changed and you have requested strict checking.
   Host key verification failed.

This occurs when the router or computer has changed SSH keys, and your machine still has outdated keys stored in ``known_hosts``.

To fix the issue, remove the stale key by running:

.. code-block:: bash

   ssh-keygen -f "/home/$USER/.ssh/known_hosts" -R "192.168.0.100"

After running the command, retry the SSH connection:

.. code-block:: bash

   ssh <vehicle-user>@192.168.0.100
