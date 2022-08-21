Pose Message
============
A pose message is often used message to define location and orientation of your robot in free space. A use for this will be using the GPS and the IMU. This can be then passed as data for a controller to reference 
in order to maintain position based on this data. To understand this message you need to first understand quaternions.

Quaternion or Orientation
^^^^^^^^^^^^^^^^^^^^^^^^^
Quaternions were first described Hamilton in 1844 [3]_  with the governing equations being 

.. math::
    
    q = w + ai + bj + ck \tag{1}

and a multiplicative property

.. math::

    i^2 = j^2 = k^2 = ijk = -1. \tag{2}

.. note:: This section will not go into great detail on what quaternions are as they are quite complex.

The main things you will need to know is how to convert euler angles (pitch, yaw and roll) to quaternion form as this is how the pose message is written. It can be written as follows

.. math::
    w = \cos{(\dfrac{\theta_x}{2})} \cos{(\dfrac{\theta_y}{2})} \cos{(\dfrac{\theta_z}{2})} + \sin{(\dfrac{\theta_x}{2})}\sin{(\dfrac{\theta_y}{2})}\sin{(\dfrac{\theta_z}{2})} \tag{3}

.. math::
     a = \sin{(\dfrac{\theta_x}{2})} \cos{(\dfrac{\theta_y}{2})} \cos{(\dfrac{\theta_z}{2})} - \cos{(\dfrac{\theta_x}{2})}\sin{(\dfrac{\theta_y}{2})}\sin{(\dfrac{\theta_z}{2})} \tag{4}

.. math::
     b = \cos{(\dfrac{\theta_x}{2})} \sin{(\dfrac{\theta_y}{2})} \cos{(\dfrac{\theta_z}{2})} + \sin{(\dfrac{\theta_x}{2})}\cos{(\dfrac{\theta_y}{2})}\sin{(\dfrac{\theta_z}{2})} \tag{5}

.. math::
     c = \cos{(\dfrac{\theta_x}{2})} \cos{(\dfrac{\theta_y}{2})} \sin{(\dfrac{\theta_z}{2})} - \sin{(\dfrac{\theta_x}{2})}\sin{(\dfrac{\theta_y}{2})}\cos{(\dfrac{\theta_z}{2})} \tag{3}

where a is the x, y is b and z is the c and :math:`\theta_x` is the roll, :math:`\theta_y` is the pitch and :math:`\theta_z` is the yaw.

Those details will go into the pose message that looks like this in code

.. code-block:: python

    Pose().orientation.x  = #details
    Pose().orientation.y  = #details
    Pose().orientation.z  = #details
    Pose().orientation.w  = #details

Point or position
^^^^^^^^^^^^^^^^^
The point part of the pose message would be the position of your vehicle in free space. to understand this say you have an arbitrary origin, this will be the location (:math:`x` ,  :math:`y` and :math:`z`) of your vehicle relative to this origin. 
In practice you will use GPS data such as latitude or longitude or UTM data in our case to detect where your vehicle is. In most of our cases we use :math:`z = 0`.
In code you can write it as

.. code-block:: python

    Pose().position.x  = #details
    Pose().position.y  = #details
    Pose().position.z  = #details

This should be all that you need to define your position and orientation in free space in ROS 2.

.. [3] W. R. Hamilton, "On Quaternions; or on a new System of Imaginaries in Algebra," The London, Edinburgh and Dublin Philosophical Magazine and Journal of Science, vol. 25, pp. 489-495, 1844. 