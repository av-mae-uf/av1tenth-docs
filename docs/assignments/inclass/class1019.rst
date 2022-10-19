In Class Setup October 19th, 2022
===================================

In this class we'll take you through running the GPS driver on your car and also running the odometry publisher on your car as well to bag that data for comparison

First you must update the repository that we have created with the necessary drivers.

.. code-block:: bash

    git pull

You will also need to have your Joystick Mapper available for use.

Once that has completed cloning, you can build the package.

.. warning:: You must do this in the workspace directory, not the src folder nor the av1tenth folder. This will break things.

To run the GPS driver you can run the following command:

.. code-block:: bash

    ros2 run neo6m_gps driver

To run the IMU and the Encoder driver you can run this in another terminal.

.. code-block:: bash

    ros2 run odom_data publisher

You can then set the angle offset parameter for the odometry by running the following command:

.. code-block:: bash

    ros2 param set /odom_pub z_angle_offset 23.56

Then run the motor driver and the Joy Mapper you have written.

.. code-block:: bash
    
    ros2 run motor_driver motor_controller

Then on your **laptop** bag the nodes so you can have the data stored.

.. code-block:: bash

    ros2 bag record -o deadreck_data /odometry /GPSData

.. note:: You need to have the ``joy_node`` running on your laptop.