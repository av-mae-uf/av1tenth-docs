In Class Setup September 26th, 2022
===================================

In this class we'll take you through setting up the car and running some of the 
software that was given to you. The main one we'll test is publishing something called
a twist.

First you must clone the repository that we have created with the necessary drivers
into a workspace of your choice, under an src folder.

.. code-block:: bash

    git clone https://github.com/av-mae-uf/av1tenth.git

If you have completed the cloning process in the previous class, update your repository, which should be done within the av1tenth folder. You can do that with the following command:

.. code-block:: bash

    git pull
    

Once that has completed cloning, you can build the package.

.. warning:: You must do this in the workspace directory, not the src folder nor the av1tenth folder. This will break things.

To build your package you must run ``colcon build``. Once the package has been built, you should see three new folders, ``build``, ``log`` and ``install``.
You can then source your workspace by running the following command.

.. code-block:: bash

    source install/setup.bash

Then you can run the ``motor_controller`` node. This node talks to the driver on the car and will control the actuators that have been installed. For more information look `here <../../information/code/motordriver.html>`_.
To run the node you enter the following command.

.. code-block:: bash
    
    ros2 run motor_driver motor_controller

You should now have a node looking for a Twist. You can then source the demo file provided to make the car run. This can be done from your workspace folder using:

.. code-block:: bash

    source src/av1tenth/driver_demo/twist

Your wheels, and the steering should move a slight bit. to stop it you can kill the node or stop the publishing.

If you'd like to do a lidar demo, you can run the launch files provided. First run the lidar in one window on the car.

.. code-block:: bash

    ros2 launch lidar_launch lidar_launch.py

Then to run rviz and see a live demo of the lidar, you would run the following launch file on your computer:

.. code-block:: bash

    ros2 launch lidar_launch lidar_rviz_launch.py


.. note:: You need to have the av1tenth package in a workspace, with the workspace sourced on your computer **NOT THE CAR** to run the rviz launch file.
    
