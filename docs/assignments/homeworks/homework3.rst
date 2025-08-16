Homework 3: Open-Loop Control (Xbox Controller Mapping)
=======================================================

This next node is important to understand how the vehicle operates and what the main operation nodes of the vehicle are. Here you will be taken through the process of 
mapping joysticks and triggers on your Xbox controller to a throttle effort and a steering angle. 

This will be a group assignment were you will map your controller inputs to the motion of your vehicle.

General Overview
^^^^^^^^^^^^^^^^

* **Due Date:** TBD
* **Points:** 50
* ROS 2 Topics: ``joy`` (sub), and ``vehicle_command_ackermann`` (pub)
* `ROS 2 Messages <../../information/ros2_common_msgs.html>`_ : ``Joy`` (in ``sensor_msgs.msg``), ``AckermannDriveStamped`` (in ``ackermann_msgs.msg``)

You might be missing the ackermann_msgs package. You can install it using:

.. code-block:: bash

    sudo apt install ros-humble-ackermann-msgs

Deliverables
^^^^^^^^^^^^
* a zip file of your joystick package
* a pdf file that:
    * lists the names of your group members
    * explains how to run your node (give package name and executable name)
    * explains the mapping you used to get from the subscribed joy topic to your published Ackermann topic

The Joy Node
^^^^^^^^^^^^
Joy is a useful ROS 2 package that can be used to expose game controller inputs to the ROS 2 system. The ROS 2 output is a ``sensor_msgs/Joy`` message.

The joy node can be run with no configuration by using:

.. code-block:: bash

    ros2 run joy joy_node

A more ideal configuration for this project would be:

.. code-block:: bash

    ros2 run joy joy_node --ros-args -p sticky_buttons:=true -p autorepeat_rate:=5.0

You can ``ros2 topic echo`` the ``/joy`` topic to figure out the specific mappings from joysticks/triggers to list indices are.

.. warning:: Remember that the axes and button lists in Python are indexed from 0

You can retrieve the values of a specfic axes or button by follow the format:

.. code-block:: python

    msg.axes[n] = something. # where n is an integer.
    msg.buttons[n] = something

Mapping Joy Values to AckermannDrive Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``AckermannDriveStamped`` message has an ``AckermannDrive`` message within it. In the ``AckermannDrive`` message there are ``steering_angle`` and ``speed`` fields.
You will need to send a message whose fields satisfy:

* steering angle is between -45 and 45 degrees, were an angle of -45 degrees steers to the right and 45 degrees steers to the left. **The actual angle values need to be in radians.** 
* speed value is between -2.0 and 2.0 m/s. 
* The rest of the fields of the message do not need to be specified. 
 
It will be up to you to choose which axes from the joy message to use in order to satisfy the above specfications.

.. note:: If you want to use the triggers for the throttle, note that they do not behave like the joysticks on the controller. The start points and neutral points are slightly different. 

Launch File
^^^^^^^^^^^
You can run multiple nodes and manage their parameters by using a launch file. There is an example launch file given below:

:download:`Launch File <project_files/example.launch.py>`

.. note:: Your launch file should be in a launch folder inside your package, something like ``package_name/launch/example.launch.py`` .

You will need to modify your ``setup.py`` file so that when ``colcon build`` runs it will include the launch file. An example is given below:

:download:`Setup File <project_files/setup.py>`

SSH into Vehicle
^^^^^^^^^^^^^^^^
You must connect to the vehicle's wireless network before you can SSH into the vehicle's computer.
The SSID and password that are given on the router that is attached to vehicle (Blue TP-Link router).

From a terminal, run the following command with ``user`` replaced with the appropriate vehicle name:

.. code-block:: bash

    ssh user@192.168.0.100

You will be prompted with a security verification, you should type ``yes`` and hit return. Then enter the password.

.. hint:: Both the user and password (kinda) have been placed on the vehicle's computer.

You will need to source the vehicle workspace before running the launch file.

.. code-block:: bash

    cd vehicle_ws

.. code-block:: bash

    source install/setup.bash

Then you can launch the vehicle drivers using:

.. code-block:: bash

    ros2 launch vehicle_launch vehicle.launch.py

.. note:: If something isn't running correctly check the USB ports, you may have pulled out the wrong one. The yellow lights on the car should be on when the correct port is plugged in and the ROS 2 driver is running.