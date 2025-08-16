Homework 2: Creating a Simple ROS2 Node
=======================================

For this assignment, you will be creating a package containing two ROS2 nodes and a launch file.


General Overview
^^^^^^^^^^^^^^^^

* **Due Date:** TBD
* **Points:** 20
* ROS 2 Topics: ``rand_num`` (pub) and ``good_val`` (sub)
* `ROS 2 Messages <../../information/ros2_common_msgs.html>`_ : ``Int32`` in ``std_msgs``


Deliverables
^^^^^^^^^^^^

Package Name: 'yourLastName_pkg'

    Node 1:

    * node name = ``generate_random_num``
    * file name = ``generate_random_num.py``
    * executable name = ``run_node1``
    * This node will generate a random number integer value between 0 and 100 inclusive and publish it every 0.5 seconds.  The topic name is ``rand_num`` and the message type is std_msgs/Int32.
    
    Node 2:

    * node name = ``check_val``
    * file name = ``check_val.py``
    * executable name = ``run_node2``
    * This node will subscribe to the ``rand_num`` topic.  If the data received is divisible by 5 with no remainder, then publish this value on a topic named ``good_val`` using a message type std_msgs/Int32

Provide a launch file named ``my_launch.py`` in a directory named ``launch`` which is in the package directory.

Upload a zip file of your package directory.

Grading Rubric
^^^^^^^^^^^^^^

* Colcon build succeeds in compiling the package, 4 pts
* The publish/subscribe is accomplished successfully, 4 pts
* The launch file runs both nodes successfully, 4 pts
* The logic of your code makes sense and can be followed, 4 pts
* All code and config files are working and are well commented, 4 pts
