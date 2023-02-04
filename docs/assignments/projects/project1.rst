Project 1: Open-Loop Control (Xbox Controller Mapping)
======================================================

This next node is important to understand how the car operates and what the main operation node of the car is. Here you will be taken through the process of 
mapping keys, joysticks and triggers on your Xbox controller to a throttle effort and a steering angle. 

This assignment or milestone will be to map your controller to motion on your car. This will be a group project, though you have been put into groups. This milestone has the following pertinent information.

* **Due Date:** February 17th, 2023
* **Pseudo Code Due Date:** February 13th, 2023
* **Code Review Due Date:** February 15th, 2023
* **Total Points:** 100
* ROS 2 Topics: ``joy`` (sub), ``led_color`` (pub) and ``vehicle_command_ackermann`` (pub)
* ROS 2 Messages: ``Joy`` (in ``sensor_msgs``), ``AckermannDriveStamped`` (in ``ackermann_msgs.msg``)
* A launch file to launch the car sensor and drivers stack has been installed in the car.

To launch the car the following command can be entered on **on the car**.

.. code-block:: bash

    ros2 launch vehicle_launch vehicle.launch.py
 
Grading Rubric
^^^^^^^^^^^^^^
Grading for this assignment will be based on the following rubric

+--------------------------------------------------------+---------+
| Criteria                                               | Points  |
+========================================================+=========+
| Pseudo Code/Flow Chart/Block Diagram                   | 25 Pts  |
+--------------------------------------------------------+---------+
| Code Review                                            | 25 Pts  |
+--------------------------------------------------------+---------+
| Node Performance and Code Efficacy                     | 50 Pts  |
+--------------------------------------------------------+---------+
| **Total**                                              | 100 Pts |
+--------------------------------------------------------+---------+

.. note:: If after the code review, changes that were suggested are not implemented, the latter 50% of the grade will be affected.

Deliverables
^^^^^^^^^^^^
ROS 2 node that maps controller keys etc. to a throttle effort and steering angle and published to ``vehicle_command_ackermann`` topic. If you want to test this live you can come in to the lab MAE-B 131 to test it out on one of the vehicles. Grading will be based on performance of the node,
if it publishes data correctly and you car functions you will get full points. You can get creative, we will leave the mappings of your car up to you. A full list of deliverables are given below

* Pseudo Code detailing how the code will work
* ROS 2 Publisher Node publishing topics ``vehicle_command_ackermann``
* ``setup.py`` file filled out
* ``package.xml`` file filled out properly
* A launch file that launches the ``joy_node``  node and the controller node that you have created. This will allow you set parameters
* Parameters in your launch file
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

    Joy.buttons[#] = #something.

This will allow you take the data coming in from the ``joy`` topic and publish an ``AckermannDriveStamped`` message.

Converting Joy Data to Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Start by connecting the joy stick to your computer, running ``joy_node`` and then echo the ``joy`` topic. See how the controller is being converted into data messages. Based on that selected the appropriate axes or buttons that you want.

The ``AckermannDriveStamped`` message has an ``AckermannDrive`` message that requires to be published. In the ``AckermannDrive`` message there is a ``steering_angle``and ``speed`` fields, which is what we are concerned with. 
You will need to send a message between -45 and 45, with 45 being steer to the right, and -45 being to the left. The speed value will need to be between 0 and 100. The rest are not necessary.

.. note:: If you want to use the triggers for the throttle, note that they do not behave like the joysticks on the controller the start points and neutral points are slightly different. 

Later on you may be using a twist for consistency, the function of that can be found on the  page on `Bicycle Kinematics <../../information/theoryinfo/cyckinem.html>`_.

Parameters 
^^^^^^^^^^
You will also need to parameterize one button that functions as a stop button. Basically you need to be able to change the value of the button through your launch file or ``.yaml`` configuration file.
When we ask you need to be able to easily change the button say from a ``X`` to a ``Xbox`` button. We will ask you to show this is working. 

Launch File
^^^^^^^^^^^

To manage parameters and easily launch nodes, a launch file can be used. A launch file can essentially allow you run multiple nodes at the same time through one terminal window,
and also allow you to change parameters in certain nodes. One parameter you might need to change is the neutral point of the car, in the case it does not drive straight. An example launch file with the motor_controller
parameters has been attached below.

:download:`Launch File <project_files/example_launch.py>`

.. note:: Your launch file should be a launch folder inside your package, something like ``package_name/launch/example_launch.py`` . Otherwise when you build the package it will fail.


There are certain things that need to be added to your ``setup.py`` file for your xbox controller mapping node which also has been given below.

:download:`Setup File <project_files/setup.py>`
