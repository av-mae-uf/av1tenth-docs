Project 1: Open-Loop Control (Xbox Controller Mapping)
======================================================

This next node is important to understand how the car operates and what the main operation node of the car is. Here you will be taken through the process of 
mapping keys, joysticks and triggers on your Xbox controller to a throttle effort and a steering angle. 

This assignment or milestone will be to map your controller to motion on your car. This will be a group project, though you have been put into groups. This milestone has the following pertinent information.

* **Due Date:** February 17th, 2023
* **Pseudo Code Due Date: ** February 3rd, 2023
* **Code Review Due Date: ** February 13th, 2023
* **Total Points:** 100
* ROS 2 Topics: ``joy`` (sub), ``led_color`` (pub) and ``vehicle_command_ackermann`` (pub)
* ROS 2 Messages: ``Joy`` (in ``sensor_msgs``), ``AckermannDriveStamped`` (in ``ackermann_msgs.msg``) and ``Int16`` (in ``std_msgs``)
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

* Pseudo Code/Flow Chart detailing how the code will work
* ROS 2 Publisher Node publishing topics ``vehicle_command_ackermann`` and ``led_color``
* ``setup.py`` file filled out
* ``package.xml`` file filled out properly
* A launch file that launches the ``joy_node`` , ``motor_controller`` node and the controller node that you have created. **(OPTIONAL)**
* Parameters in your launch file or ``.yaml`` file **(OPTIONAL)**
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

This will allow you take the data coming in from the ``joy`` topic and publish a Twist.

Converting Joy Data to Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``VehCmd`` message has a throttle and a steering angle that it requires to be published. The throttle effort is between 0 and 100 percent and the steering angle
will be between -45 and 45. -45 is turning to the left and 45 is right. A negative throttle effort will drive the car backwards.

.. note:: If you want to use the triggers for the throttle, note that they do not behave like the joysticks on the controller the start points and neutral points are slightly different. 

Later on you will be using a twist for consistency, the function of that can be found on the  page on `Bicycle Kinematics <../../information/theoryinfo/cyckinem.html>`_.

Lights Operation
^^^^^^^^^^^^^^^^

To operate the lights on board you will need an additional publisher on a timer that sends an ``Int16`` data. The topic that you will need to use is the ``led_color``
you can activate the yellow and the red colors, but the green color has been locked into being on the safe mode. To do this you need to send an integer 1 or 2 with 1 being yellow and 2 being red.
You can make these lights blink, or alternate or something creative if you'd like! You will need to have those operate in some form to get full points.

Parameters **(OPTIONAL)**
^^^^^^^^^^^^^^^^^^^^^^^^^
You will also need to parameterize one button that functions as a stop button. Basically you need to be able to change the value of the button through your launch file or ``.yaml`` configuration file.
When we ask you need to be able to easily change the button say from a ``X`` to a ``Xbox`` button. We will ask you to show this is working. If you want to do something else instead of a simple stop button your can 
parameterize a button for your lights.

Launch File **(OPTIONAL)**
^^^^^^^^^^^^^^^^^^^^^^^^^^

To manage parameters and easily launch nodes, a launch file can be used. A launch file can essentially allow you run multiple nodes at the same time through one terminal window,
and also allow you to change parameters in certain nodes. One parameter you might need to change is the neutral point of the car, in the case it does not drive straight. An example launch file with the motor_controller
parameters has been attached below.

:download:`Launch File <project_files/example_launch.py>`

.. note:: Your launch file should be a launch folder inside your package, something like ``package_name/launch/example_launch.py`` . Otherwise when you build the package it will fail.


There are certain things that need to be added to your ``setup.py`` file for your xbox controller mapping node which also has been given below.

:download:`Setup File <project_files/setup.py>`
