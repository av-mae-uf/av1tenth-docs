Milestone 1: Creating a Simple ROS 2 Node (Pub & Sub)
=====================================================

By now you should have gone through the basics of creating a node in ROS 2 in class. Here in this sequence, you will be creating a 
ROS 2 node that outputs the quotient for a divisor of 5 but only when the remainder is equal to 0. A random number publisher will be provided to test out your code.

This assignment or milestone will be to complete a simple full ROS 2 node on your own. This milestone has the following pertinent information.

* **Due Date:** February 1st, 2023
* **Points:** 20
* ROS 2 Topics: ``rand_num`` (sub) and ``quotient`` (pub)
* ROS 2 Messages: ``Int16`` (Part of std_msgs)
* Publisher can be accessed :download:`here <../files/rand_num.zip>`

Deliverables
^^^^^^^^^^^^
ROS 2 node that publishes the quotient in the ``quotient`` topic. Grading will be based on performance of the node, if it publishes data correctly you will get full points. A full list of deliverables are given below

* ROS 2 Publisher Node publishing topic ``quotient``
* ``setup.py`` file filled out
* ``package.xml`` file filled out properly
* .zip file containing entire package (We should be able to download the file and put it into ROS 2 and run it without changing anything)
  
.. warning:: The names of topics are important, writing the wrong name will result in a **5 point** deduction of the overall grade.

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



