Homework 6: Vehicle Pose
========================


General Overview
^^^^^^^^^^^^^^^^

* **DUE DATE:** TBD
* **POINTS:** 30
* ROS 2 Topics: ``vehicle_pose`` (pub), ``gps`` (sub) and ``odometry`` (sub)
* `ROS 2 Messages <../../information/ros2_common_msgs.html>`_ : ``Odometry`` in ``nav_msgs``, ``NavSatFix`` in ``sensor_msgs`` ``PoseStamped`` in ``geometry_msgs``


Deliverables
^^^^^^^^^^^^

* ``gps_data.txt`` and ``angle_data.txt`` from Task 2
* Google Earth image from Task 2
* ``pose_estimator`` node python file from Task 3

Tasks
^^^^^

Task 1: Data Collection
"""""""""""""""""""""""

#. Place your vehicle in joystick control.  On the vehicle, launch the file ``vehicle.launch.py`` so that the nodes ``gps_node`` and ``motor_carrier_driver`` node are both running.
#. Run your vehicle outdoors, away from trees (as much as possible).  Echo the topics ``gps`` (NavSatFix message) and ``odometry`` (Odometry message) to make sure that data is being published.
#. Run for about 1 minute and bag all data.  (ros2 bag record -a)

Task 2: Plot latitude and longitude on Google Earth
"""""""""""""""""""""""""""""""""""""""""""""""""""

#. Write a node that you will run when you play back your bag data. This node will subscribe to the ``gps`` topic and the ``odometry`` topic.
    
    * Each time a ``gps`` topic is read, write the latitude and longitude to a text file named ``lat_lon_data.txt``.  Put a comma between the latitude and longitude values. Also, write the UTM position coordinates to a file named ``utm_data.txt``.  Put a comma between the values.
    * Each time an ``odometry`` topic is read, write the ``pose.pose.orientation x,y,z,w`` values and the calculated orientation angle to a text file named ``angle_data.txt``.  Recall that for our vehicle operating in the ``x,y`` plane, 
    .. math::
        \theta = 2*atan2(z,w)

#. Open your ``gps_data.txt`` file in Google Earth and save a jpg image of your gps data.
#. Upload the files ``gps_data.txt``, ``angle_data.txt``, and your jpg Google Earth image to Canvas.

There should be a given python script on the Canvas assignment page that you can use as a starting point.

.. hint::
    Python's ``math`` library has a ``atan2(y,x)`` function.

.. note::
    Remember there is a list of :doc:`common ROS 2 messages <../../information/ros2_common_msgs>`. 
    Make sure to read how ``PoseStamped``, ``Odometry``, and ``NavSatFix`` work!

Task 3: Write a node named ``pose_estimator``
"""""""""""""""""""""""""""""""""""""""""""

Write a node named ``pose_estimator`` that you will run when you play back your bag data. 

* This node will subscribe to the ``gps`` topic and the ``odometry`` topic.
* Each time a ``gps`` topic is read, get the current x and y from the latitude and longitude from the message. 
* Each time an ``odometry`` topic is read, calculate the orientation angle and store the angle, speed, z/w orientations and x/y positions. Recall that for our vehicle operating in the ``x,y`` plane, 
.. math::
    \theta = 2*atan2(z,w)
.. math::
    x' = x + v * cos(\theta) * t
.. math::
    y' = y + v * sin(\theta) * t
.. note:: 
    :math:`x'` and :math:`y'` are the next :math:`x` and :math:`y` value. :math:`v` is the velocity. :math:`t` is the time since last position, 0.05 seconds might be good enough, but feel free to experiment.

* This node will publish a ``PoseStamped`` message, from ``geometry_msgs``, to the ``vehicle_pose`` topic. Make a timer that publishes 20 times a second (20 Hz). In the timer callback, publish a ``PoseStamped`` message that takes the current x position, y position, z orientation, and w orientation.

.. note:: 
    ``PoseStamped`` has both position and orientation x, y, nad z member variables. Make sure to update the correct x, y, and z value when publishing!

.. note::
    Both ``gps`` and ``odometry`` callback functions will update the same ``x`` and ``y`` variables. ``gps`` callback will simply store the current x and y based on latitude and longitude. ``odometry`` estimates the future ``x`` and ``y`` position based on the equations above. 

Upload your python file that defines this node to Canvas.