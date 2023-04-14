Milestone 6: Pose Estimator
===========================

This assignment covers working on a Pose Estimator for `Project 2 <../projects/project2.html>`_

* **Due Date:** April 17th, 2023
* **Psuedocode Due Date:** April 14th, 2023
* **Points:** 20
* ROS 2 Topics: ``/odometry`` (sub), ``/gps`` (sub) and ``vehicle_pose`` (pub)
* ROS 2 Messages: ``Odometry`` (in ``nav_msgs``) and ``NavSatFix`` (in ``sensor_msgs``) and `PoseStamped`` (in ``geometry_msgs``).

.. warning:: The message and topic names are important, not following this convention can have your car not working. Please ensure they are correct.

Deliverables
^^^^^^^^^^^^
A pdf with the plot of your pose estimator working, similar to what was done in `milestone 3 <milestone3.html>`_.

Odometry and GPSData Basics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``odometry`` topic outputs an ``Odometry`` message which has information on its structure `here <http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html>`_.
The values for the velocity and orientation are in ``twist.twist.linear.x``, ``pose.pose.orientation.z`` and ``pose.pose.orientation.w``.
You will use this data to dead reckon. To convert the orientation data from quaternion to a :math:`\theta_{veh}` do the following

.. math::

    \theta_{veh} = 2*atan2(z , w) 

.. code-block:: python

    theta = 2*math.atan(z,w)

To convert the GPS data from latitude and longitude to UTM coordinates you can use the python library ``utm``. You can install through

.. code-block:: bash

    pip3 install utm

Then you can call it as follows:

.. code-block:: python

    utm.from_latlon(latitude,longitude)

This will give you data in the form (Easting, Northing, Zone Number, Zone Letter). You only need Easting and Northing which Easting is x and Northing is y for the pose.

Dead Reckoning
^^^^^^^^^^^^^^

To dead reckon you will estimate the position based on the velocity and angular data, while updating with the GPS Data. For this you have two callbacks one that dead reckons and one that updates the GPS position.
To dead reckon you will do the following,

.. math::

    x = x + v \cos (\theta) \Delta t , \\
    y = y + v \sin (\theta) \Delta t 

where, :math:`\Delta t` is ``0.05s``. Then every time the GPSData comes in you will update your x with that. store it in a ``self.`` variable to pass it between the callbacks. Make sure the x in above is also being stored in a ``self`` variable.
You will be publishing a ``PoseStamped`` in the odometry callback, some information for that is available below

A Power point on Dead Reckoning is available :download:`here <milestone_files/DeadReckoning.pptx>`

.. code-block:: python
    
    msgEst = PoseStamped()
    msgEst.pose.position.x = # put x here
    msgEst.pose.position.y = # put y here
    msgEst.pose.orientation.z = # pass in the odometry pose.pose.orientation.z
    msgEst.pose.orientation.w =  # pass in the odometry pose.pose.orientation.w
    msgEst.header.stamp = self.get_clock().now().to_msg()

Plotting Data
^^^^^^^^^^^^^

You will have to go out and bag GPS data at some point to go ahead and complete this assignment. You will then need to use a CSV converter to convert it into a usable format to plot.
You will need to submit these plots along with your pose estimator to get full points. A sample node for CSV is give :download:`here <milestone_files/process_bagfile_csv.py>`






