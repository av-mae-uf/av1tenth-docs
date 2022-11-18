Milestone 5: Pose Estimator
===========================

This assignment covers working on a Pose Estimator for `Project 2 <../projects/project2.html>`_

* **Due Date:** December 2nd, 2022
* **Points:** 20
* ROS 2 Topics: ``odometry`` (sub), ``GPSData`` (sub) and ``vehicle_pose`` (pub)
* ROS 2 Messages: ``Odometry`` (in ``nav_msgs``) and ``PoseStamped`` (in ``geometry_msgs``) 

.. warning:: The message and topic names are important, not following this convention can have your car not working. Please ensure they are correct.

Deliverables
^^^^^^^^^^^^
A pdf with the plot of your pose estimator working, similar to what was done in `milestone 3 <milestone3.html>`_.

Odometry and GPSData Basics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``odometry`` topic outputs an ``Odometry`` message which has information on its structure `here <http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html>`_.
The values for the velocity, position and orientation are in ``twist.twist.linear.x``, ``pose.pose.position.x``, ``pose.pose.position.y``, ``pose.pose.orientation.z`` and ``pose.pose.orientation.w``.
You will use this data to dead reckon. To convert the orientation data to a :math:`\theta_{veh}` do the following

.. math::

    \theta_{veh} = 2*atan2(z , w) 


Dead Reckoning
^^^^^^^^^^^^^^

To dead reckon you will estimate the position based on the velocity and angular data, while updating with the GPS Data. For this you have two callbacks one that dead reckons and one that updates the GPS position.
To dead reckon you will do the following,

.. math::

    x = x + v \cos (\theta) \Delta t , \\
    y = y + v \sin (\theta) \Delta t 

where, :math:`\Delta t` is ``0.15s``. Then every time the GPSData comes in you will update your x with that. store it in a ``self.`` variable to pass it between the callbacks. Make sure the x in above is also being stored in a ``self`` variable.
You will be publishing a ``PoseStamped`` in the odometry callback, some information for that is available below

.. code-block:: python
    msgEst = PoseStamped()
    msgEst.pose.position.x = # put x here
    msgUTM.pose.position.y = # put y here
    msgUTM.pose.orientation.z = # pass in the odometry pose.pose.orientation.z
    msgUTM.pose.orientation.w =  # pass in the odometry pose.pose.orientation.z
    msgEst.header.stamp = self.get_clock().now().to_msg()

Plotting Data
^^^^^^^^^^^^^

To plot the data use the same node that was given in `milestone 3 <milestone3.html>`_, just change the subscriber topic name to the correct one, output to a txt file
import to excel and plot as normal. Use one of the bag files provided in ``ros2bag`` to do this. I've added some more for convenience.






