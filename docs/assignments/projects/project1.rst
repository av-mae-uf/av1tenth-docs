Project 1: Open-Loop Control (Xbox Controller Mapping)
======================================================

This next node is important to understand how the car operates and what the main operation node of the car is. Here you will be taken through the process of 
mapping keys, joysticks and triggers on your Xbox controller to a `Twist message <../../information/theoryinfo/twist.html>`_. To do this it is important to understand
how a twist works, which at this point should be covered in class. You can also look for more information in the link given earlier.

This assignment or milestone will be to map your controller to motion on your car. This will be an individual project, though you have been put into groups. This milestone has the following pertinent information.

* **Due Date:** October 7th, 2022
* **Points:** 100
* ROS 2 Topics: ``joy`` (sub), ``led_color`` (pub) and ``vehicle_command_twist`` (pub)
* ROS 2 Messages: ``Joy`` (in ``sensor_msgs``), ``Twist`` (in ``geometry_msgs``) and Int16 (in ``std_msgs``)
* A launch file to launch the ``motor_controller`` node and the ``joy_node`` node has been given but you can run the node with a normal ``ros2 run`` command.
  
To run this on your care you will need to git clone the appropriate driver package that we have created for the car. You will need to clone
this into the appropriate workspace source folder, something like ``class_ws/src``. That can be done by using the following command

.. code-block:: bash

    git clone https://github.com/av-mae-uf/av1tenth.git

Deliverables
^^^^^^^^^^^^
ROS 2 node that maps controller keys etc. to a Twist and publishes to ``vehicle_command_twist`` topic. If you want to test this live you can come in to the lab MAE-B 131 to test it out on one of the vehicles. Grading will be based on performance of the node,
if it publishes data correctly and you car functions you will get full points. You can get creative, we will leave the mappings of your car up to you. A full list of deliverables are given below

* ROS 2 Publisher Node publishing topics ``vehicle_command_twist`` and ``led_color``
* ``setup.py`` file filled out
* ``package.xml`` file filled out properly
* A launch file that launches the ``joy_node`` , ``motor_controller`` node and the controller node that you have created.
* Parameters in your launch file or ``.yaml`` file
* This is a qualitative assessment so no submissions are needed. You will need to show us your completed node running on your car by the due date.
  
.. warning:: The names of topics are important, writing the wrong name will result in a **25% point** deduction.

Joystick Mapping
^^^^^^^^^^^^^^^^
To figure out what the mappings of the controller are to the message you can ``echo`` a topic to figure out how to do this. You should be able to do this by now.
The structure of the message would be 7 sets of ``axes[#]`` and 10 sets of buttons ``buttons[#]``. It should tell you what button or axes are mapped when you press a certain button and also the number and range is.

You would ``echo`` the topic ``joy``.

.. note:: Button presses exhibit a bouncing behavior, multiple message will be sent for a single button press. Additional buttons are also available past Button[5]

To map the buttons etc. you would have to map them as such

.. code-block:: python

    Joy().buttons[#] = #something.

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

    \dot{\psi} = \dfrac{V}{R}

This will go in the the angular part of your ``Twist`` message that you will be using, while :math:`V` will go into the linear part of your message.
It'll be important to understand the limits of the radius of curvature as you can base you controllers off of them.

For more information you can check out the page on `Bicycle Kinematics <../../information/theoryinfo/cyckinem.html>`_.

Parameters
^^^^^^^^^^
You will also need to parameterize one button that functions as a stop button. Basically you need to be able to change the value of the button through your launch file or ``.yaml`` configuration file.
When we ask you need to be able to easily change the button say from a ``X`` to a ``Xbox`` button. We will ask you to show this is working. If you want to do something else instead of a simple stop button your can 
parameterize a button for your lights.

Lights Operation
^^^^^^^^^^^^^^^^

To operate the lights on board you will need an additional publisher on a timer that sends an ``Int16`` data. The topic that you will need to use is the ``led_color``
you can activate the yellow and the red colors, but the green color has been locked into being on the safe mode. To do this you need to send an integer 1 or 2 with 1 being yellow and 2 being red.
You can make these lights blink, or alternate or something creative if you'd like! You will need to have those operate in some form to get full points.
