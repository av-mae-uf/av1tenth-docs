Milestone 4: PID Control Wall Following
======================================================

This assignment introduces a wall following algorithm to stay a set distance away from the wall. The controller used here is a PID controller, think 
cruise control on your car.

* **Due Date:** March 10th, 2023
* * **Pseudo Code Due Date:** March 8th, 2023
* **Points:** 20
* ROS 2 Topics: ``scan`` (sub) and ``vehicle_command_ackermann`` (pub)
* ROS 2 Messages: ``LaserScan`` in ``sensor_msgs`` (sub) and ``AckermannDriveStamped`` in ``ackermann_msgs`` (pub) 

Deliverables
^^^^^^^^^^^^
ROS 2 node with a PID controller for your vehicle steering.

* Pseudo Code for your Node. More information can be found `here <../../information/code/pseudocode.html>`_
* ROS 2 Publisher Node publishing topic ``vehicle_command_ackermann``
* ``setup.py`` file filled out
* ``package.xml`` file filled out properly
* .zip file containing entire package (We should be able to download the file and put it on a vehicle and run it without changing anything)

PID Controller
^^^^^^^^^^^^^^^^^^^^

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

.. note:: :math:`\Delta t` Can and probably should be set to a constant value of 10Hz or 0.1s.

You will need to window your integral controller, i.e. only sum up the last certain amount of error values. Usually for our case it could be around 100 to 200 values.

.. hint:: Storing the errors as a list and then summing them up will be the easiest method to achieve this. You can also use the ``pop()`` function in python to remove a certain value from a list.

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

You will need to assign a :code:`self.var` to store your old values of integral addition errors time and error. You will then use the :math:`u` message as the ``vehicle_command_angle`` value.

.. warning:: Remember that the car has actuation limits on the steering to be between -45 and 45.

.. note:: You can change the order as needed to get a certain positive or negative value.

.. hint:: Try to get the right turn to be positive and the left turn as negative. Using the ``numpy.sign()`` function should make this trivial. Just ensure you filter out ``NaN`` values with ``np.isnan()``.







