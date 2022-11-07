Milestone 4: Creating a Speed Controller
============================================

This assignment covers working on a simple PID controller to control the speed that is coming out of your 
Joy Mapping Node that you completed in `Project 1 <../projects/project1.html>`_

* **Due Date:** November 16th, 2022
* **Points:** 20
* ROS 2 Topics: ``odometry`` (sub), ``joy`` (sub) and ``vehicle_command_angle`` (pub)
* ROS 2 Messages: ``Odometry`` (in ``nav_msgs``), ``VehCmd`` (in ``drive_interfaces/VehCmd.msg``) and ``Joy`` (in ``sensor_msgs``)

.. warning:: The message and topic names are important, not following this convention can have your car not working. Please ensure they are correct.

Deliverables
^^^^^^^^^^^^
A package ``.zip`` with your Joy Mapper and Controller Node

Odometry and Speed Basics
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``odometry`` topic outputs an ``Odometry`` message which has information on its structure `here <http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html>`_.
The value for the speed of the vehicle can be found in the ``twist.x`` section of the message. It is output in ``m/s``. You will be publishing your message
in the form of a percentage so there is some simple math involved. Using an optical tachometer the Max speed of the car was measured to be 7.3513268 m/s. The
math used is given below,

.. math::

    \dot{x}_{max} = \dfrac{N(2 \pi R)}{60} ,

where :math:`N` is the revolutions per minute (here 585 RPM), :math:`R` is the radius of the wheel (here .12 m). So now you can find out what the corresponding Odometry
throttle effort is using percentage calculations with the max velocity. 

PID Controller
^^^^^^^^^^^^^^
More info on PID Controllers can be found `here <../../information/theoryinfo/pid.html>`_. PID controllers are simple controllers that employ feedback and continuously controls
as system based on an error. The idea is to drive that error to 0 based on the Proportional (P), Integral (I) and Derivate (D) controller terms. The error
can be calculated as follows,

.. math::

    e(t) = r - y,

where :math:`e(t)` is the error w.r.t time, :math:`r` is the desired set point (value you want your system to be at) and :math:`y` is the system output (:math:`\dot{x}`).

The simplest form of a PID is multiplying your controller by a fixed or proportional gain. A form that is often given in theoretical controls classes (EML4312)

.. math::

    u = K_p e(t),

where :math:`u` is the control command given to the system and :math:`K_p` is the proportional gain.

The next term, the Integral (I) controller has the following equation,

.. math::

    u = \int_{0}^{t} K_i \, e(t) \, dt,

where :math:`K_i` is the integral gain. The integral controller in this form is not very useful to us. An alternative form is,

.. math::

    u = K_i \sum_{k=1}^{k} e_k \Delta t.

The idea is you take your old values of :math:`e_k` (the error) and you keep adding to it's self and multiplying by a fixed integral gain :math:`K_i`.
:math:`\Delta t` is just taking your current :math:`t_k` and subtracting the old one (previous iteration) :math:`t_{k-1}`, where :math:`k^th` is the current iteration.

The final term is the derivative (D) controller which multiplies a gain by the derivative or slope of your error over time. The equation of this controller would be

.. math::

    u = \dfrac{d}{dt} e(t) K_d.

where :math:`K_d` is the derivative gain. A more useful form of this controller is,

.. math::

    u = K_d \dfrac {e_k - e_{k-1} } {t_k - (t_{k-1})}

A full Proportional, Integral and Derivate (PID) controller is essentially just mashing all three controllers together and has the following equation,

.. math::
    
    u = K_p e(t) + \int_{0}^{t} K_i \, e(t) \, dt + \dfrac{d}{dt} e(t) K_d

or

.. math:: 

    u = K_p e_k + K_i \sum_{k=1}^{k} e_k \Delta t + K_d \dfrac {e_k - e_{k-1} } {t_k - (t_{k-1})}.

You do not need to use the full PID controller you can use PI or PD controllers as well or other formats. See which one works best and use that for your controller.

You will need to assign a :code:`self.var` to store your old values of integral addition errors time and error. You can get time 
using the :code:`time.monotonic()` function. You will then use the :math:`u` message as the ``vehicle_command_angle`` value.

Testing the Speed Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To easily test the speed controller, map buttons to have set speeds, ideally the buttons will set a throttle percentage of 10%, 20%, 30% etc. to test out your controller.
We will show you how to test out your controller live and also how plot the data after bagging it. You will need to publish the value set_point under VehCmd.msg to make this possible.
You can also disable the limiter in the motor_controller node to test out higher speeds, by setting a parameter in a launch file. The easiest way to test this out
will be on your cars. Come around to MAE-B 131 during `office hours or extended hours <../../assistance/contact.html>`_. We do not think we'll have time to test out
during class at the moment, but this can change.

Launch and Setup Files to Change Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have launch files to allow you to change parameters on start or you can run the following command,

.. code-block:: bash

    ros2 run motor_driver motor_controller --ros-args -p limiter:=False

But a better and easier way to do this is using launch files. To set the limiter to off set the value limiter to ``False``

:download:`Launch File <../projects/project_files/example_launch.py>`

.. note:: Your launch file should be a launch folder inside your package, something like ``package_name/launch/example_launch.py`` . Otherwise when you build the package it will fail.


There are certain things that need to be added to your ``setup.py`` file for your speed controller node which also has been given below.

:download:`Setup File <../projects/project_files/setup.py>`



