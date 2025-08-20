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

Grading for this assignment will be based on the following rubric

+--------------------------------------------------------+---------+
| Criteria                                               | Points  |
+========================================================+=========+
| Colcon Build succeeds in compiling the package         | 4 Pts   |
+--------------------------------------------------------+---------+
| The subscribe is accomplished successfully             | 4 Pts   |
+--------------------------------------------------------+---------+
| The logic of your code makes sense and can be followed | 4 Pts   |
+--------------------------------------------------------+---------+
|The publish is accomplished successfully                | 4 Pts   |
+--------------------------------------------------------+---------+
|All code and config files are working and well commented| 4 Pts   |
+--------------------------------------------------------+---------+
| **Total**                                              | 20 Pts  |
+--------------------------------------------------------+---------+

Quotient, Divisor, Dividend and Remainder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Hopefully this information is redundant, but it is here any way. The equation to be used is as follows

.. math::
    \dfrac{x}{y} = z

Where x is the dividend, y is the divisor and z is the quotient. That's pretty much all the info you need.

Logic
^^^^^
You will need to check whenever data comes in that the data is divisible by 5 and the remainder is 0, a useful python operator is the modulo

.. code-block:: python

    x%y

Which would return the remainder. Then you would need to use an ``if`` statement or ternary operator to check if it is 0.

Launch File
^^^^^^^^^^^
You can run multiple nodes and manage their parameters by using a launch file. There is an example launch file given below:

:download:`Launch File <../projects/project_files/example.launch.py>`

.. note:: Your launch file should be in a launch folder inside your package, something like ``package_name/launch/example.launch.py`` .

You will need to modify your ``setup.py`` file so that when ``colcon build`` runs it will include the launch file. An example is given below:

:download:`Setup File <../projects/project_files/setup.py>`
