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
    
    * Each time a ``gps`` topic is read:
       
        * write the latitude and longitude to a text file named ``lat_lon_data.txt``.  Put a comma between the latitude and longitude values. 
        * Also, write the UTM position coordinates to a file named ``gps_data.txt``.  Put a comma between the values.

    * Each time an ``odometry`` topic is read:
        
        * write the ``pose.pose.orientation x,y,z,w`` values and the calculated orientation angle to a text file named ``angle_data.txt``.  
        * Recall that for our vehicle operating in the ``x,y`` plane, 
    
        .. math::
            \theta = 2*atan2(z,w)

#. Open your ``gps_data.txt`` file in Google Earth and save a jpg image of your gps data.
#. Upload the files ``gps_data.txt``, ``angle_data.txt``, and your jpg Google Earth image to Canvas.

:download:`See file print_pose_data_from_bagfile.py <homework_files/print_pose_data_from_bagfile.py>`

.. hint::
    Python's ``math`` library has a ``atan2(y,x)`` function.

.. note::
    Remember there is a list of :doc:`common ROS 2 messages <../../information/ros2_common_msgs>`. 
    Make sure to read how ``PoseStamped``, ``Odometry``, and ``NavSatFix`` work!

Task 3: Write a node named ``pose_estimator``
"""""""""""""""""""""""""""""""""""""""""""""

Write a node named ``pose_estimator`` that you will run when you play back your bag data. 

* This node will subscribe to the ``gps`` topic and the ``odometry`` topic.
    
    * Each time a ``gps`` topic is read:
        
        * store the current x and y from the latitude and longitude from the message as a ``self`` variables. 
        * More information on how to get the position can be found in the GPSData Basics section.
    
    * Each time an ``odometry`` topic is read: 
        
        * calculate the orientation angle like in Task 2,
        * store the angle, speed, z/w orientations as ``self`` variables,
        * and then dead reckon the new x/y positions using same ``self`` x,y variables. 
        * More information can be found in the Odometry and Dead Reckoning section.

* This node will publish a ``PoseStamped`` message, from ``geometry_msgs``, to the ``vehicle_pose`` topic. More information can be found in the PoseStamped section.

Upload your python file that defines this node to Canvas.

GPSData Basics
^^^^^^^^^^^^^^

To convert the GPS data from latitude and longitude to UTM coordinates you can use the python library ``utm``. You can install through

.. code-block:: bash

    pip3 install utm

Then you can call it as follows:

.. code-block:: python

    utm.from_latlon(latitude,longitude)

This will give you data in the form (Easting, Northing, Zone Number, Zone Letter). You only need Easting and Northing which Easting is x and Northing is y for the pose.

Odometry and Dead Reckoning
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``odometry`` topic outputs an ``Odometry`` message which has information on its structure `here <http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html>`_.
The values for the velocity and orientation are in ``twist.twist.linear.x``, ``pose.pose.orientation.z`` and ``pose.pose.orientation.w``.
You will use this data to dead reckon. To convert the orientation data from quaternion to a :math:`\theta_{veh}` do the following

.. math::

    \theta_{veh} = 2*atan2(z , w) 

.. code-block:: python

    theta = 2*math.atan(z,w)

To dead reckon you will estimate the position based on the velocity and angular data, while updating with the GPS Data. For this you have two callbacks one that dead reckons and one that updates the GPS position.

To dead reckon you will do the following,

.. math::

    x = x + v \cos (\theta) \Delta t , \\
    y = y + v \sin (\theta) \Delta t 

where, :math:`\Delta t` is ``0.05s``. Then every time the GPSData comes in you will update your x with that. store it in a ``self.`` variable to pass it between the callbacks. Make sure the x in above is also being stored in a ``self`` variable.

A Power point on Dead Reckoning is available :download:`here <homework_files/DeadReckoning.pptx>`

.. important::
    Both ``gps`` and ``odometry`` callback functions will update the same ``self.`` ``x`` and ``y`` variables. ``gps`` callback will simply store the current x and y based on the GPS's latitude and longitude. ``odometry`` estimates (dead reckons) the future ``x`` and ``y`` position based on the equations above. 

PoseStamped
^^^^^^^^^^^

Make a timer that publishes 20 times a second (20 Hz). In the timer callback, publish a ``PoseStamped`` message that takes the current x position, y position, z orientation, and w orientation.


Some information for that is available below:

.. code-block:: python
    
    msgEst = PoseStamped()
    msgEst.pose.position.x = # put x here
    msgEst.pose.position.y = # put y here
    msgEst.pose.orientation.z = # pass in the odometry pose.pose.orientation.z
    msgEst.pose.orientation.w =  # pass in the odometry pose.pose.orientation.w
    msgEst.header.stamp = self.get_clock().now().to_msg()

.. important:: 
    ``PoseStamped`` has both position and orientation x, y, and z member variables. Make sure to update the correct x, y, and z value when publishing!


Plotting Data (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    This was required a previous semester, but is no longer needed. Feel free to see how accurate your Dead Reckoned pose estimation is compared to the GPS values. **THIS IS NOT GRADED.**

You will have to go out and bag GPS data at some point to go ahead and complete this assignment. You will then need to use a CSV converter to convert it into a usable format to plot.
You will need to submit these plots along with your pose estimator to get full points. A sample node for CSV is give :download:`here <homework_files/process_bagfile_csv.py>`


