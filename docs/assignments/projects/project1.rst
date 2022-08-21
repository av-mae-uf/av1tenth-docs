Project 1: Open-Loop Control (Xbox Controller Mapping)
======================================================

This next node is important to understand how the car operates and what the main operation node of the car is. Here you will be taken through the process of 
mapping keys, joysticks and triggers on your Xbox controller to a `Twist message <../../information/theoryinfo/twist.html>`_. To do this it is important to understand
how a twist works, which at this point should be covered in class. You can also look for more information in the link given earlier.

This assignment or milestone will be to map your controller to motion on your car. This will be an individual project, though you have been put into groups. This milestone has the following pertinent information.

* **Due Date:** September 23rd, 2022
* **Points:** 100
* ROS 2 Topics: ``joy`` (sub), ``led_color`` (pub) and ``vehicle_command`` (pub)
* ROS 2 Messages: ``Joy`` (in ``sensor_msgs``), ``Twist`` (in ``geometry_msgs``) and Int16 (in ``std_msgs``)
* A launch file to launch the ``motor_controller`` node and the ``joy_node`` node has been given but you can run the node with a normal ``ros2 run`` command.
  
Deliverables
^^^^^^^^^^^^
ROS 2 node that maps controller keys etc. to a Twist and publishes to ``vehicle_command`` topic. The names of topics are important, writing the wrong name will result in a 
**25% point** deduction. If you want to test this live you can come in to the lab MAE-B 131 to test it out on one of the vehicles. Grading will be based on performance of the node,
if it publishes data correctly and you car functions you will get full points. You can get creative, we will leave the mappings of your car up to you.

Joystick Mapping
^^^^^^^^^^^^^^^^
+-----------+--------------------------------------+-------------+-------------------------------------------------+
|Axes/Button|Controller Button, Trigger or Joystick|Range/Values | Other Info                                      |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[0]   | Left Thumbstick-Horizontal           |[-1,1]       | 0 Centered, 1 Left                              |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[1]   | Left Thumbstick-Vertical             |[-1,1]       | 0 Centered, 1 Up                                |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[2]   | Left Trigger                         |[-1,1]       | 1 when unpressed                                |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[3]   | Right Thumbstick-Horizontal          |[-1,1]       | 0 Centered, 1 Left                              |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[4]   | Right Thumbstick-Vertical            |[-1,1]       | 0 Centered, 1 Up                                |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[5]   | Right Trigger                        |[-1,1]       | 1 when unpressed                                |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[6]   | Horizontal D-Pad                     |[1],[0],[-1] | 1 pressed left, -1 pressed                      |
+           |                                      |             |                                                 |
|           |                                      |             | right, 0 not pressed                            |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| axes[7]   | Vertical D-Pad                       |[1],[0],[-1] | 1 pressed up, -1 pressed                        |
+           |                                      |             |                                                 |
|           |                                      |             | down, 0 not pressed                             |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[0]| "A"                                  |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[1]| "B"                                  |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[2]| "X"                                  |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[3]| "Y"                                  |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[4]| Left Bumper                          |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[5]| Right Bumper                         |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[6]| "Back" Button                        |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[7]| "Start" Button                       |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[8]| Xbox Button                          |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[9]| Left Thumbstick Press                |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+
| buttons[10]| Right Thumbstick Press              |[0], [1]     | 1 when pressed                                  |
+-----------+--------------------------------------+-------------+-------------------------------------------------+

.. note:: Button presses exhibit a bouncing behavior, multiple message will be sent for a single button press. Additional buttons are also available past Button[5]

To map the buttons etc. you would have to map them as such

.. code-block:: python

    Joy().buttons[1] = #something.

This will allow you take the data coming in from the ``joy`` topic and publish a Twist.

Converting Data to a Twist
^^^^^^^^^^^^^^^^^^^^^^^^^^

To convert these linear mappings to the twist you need to first understand and calculate the angular rate of the car based upon your desired motions.

To do this look at the following picture

.. figure:: ../../information/theoryinfo/images/bicyle_diagram.png
    :alt: Bicycle Model Diagram
    :width: 75%

This will be the basis of what will be input into the `Twist <../../information/theoryinfo/twist.html>`_ message that will be the main mode of conveying motion to the ``motor_controller`` `node <../../information/code/motordriver.html>`_.
To do this you will first need to input both your wheelbase and steering angle into the equation

.. math::

    R = \dfrac{L}{\tan{\delta}} \tag{1}

This is the radius of curvature that the vehicle will be traveling on. From this you can calculate the yaw rate of the vehicle which the forward
the velocity of the car in m/s. Then you can use the equation

.. math::

    \dot{\phi} = \dfrac{V}{R}

This will go in the the angular part of your ``Twist`` message that you will be using, while :math:`V` will go into the linear part of your message.
It'll be important to understand the limits of the radius of curvature as you can base you controllers off of them.

For more information you can check out the page on `Bicycle Kinematics <../../information/theoryinfo/cyckinem.html>`_.

Lights Operation
^^^^^^^^^^^^^^^^

To operate the lights on board you will need an additional publisher on a timer that sends an ``Int16`` data. The topic that you will need to use is the ``led_color``
you can activate the yellow and the red colors, but the green color has been locked into being on the safe mode. To do this you need to send an integer 1 or 2 with 1 being yellow and 2 being red.
You can make these lights blink, or alternate or something creative if you'd like! You will need to have those operate in some form to get full points.