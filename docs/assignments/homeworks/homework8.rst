Homework 8: Plot Continuous Path Segments
=========================================

General Overview
^^^^^^^^^^^^^^^^

* **DUE DATE:** TBD
* **POINTS:** 30
* ROS 2 Topics: TODO
* `ROS 2 Messages <../../information/ros2_common_msgs.html>`_ : TODO

Deliverables
^^^^^^^^^^^^
You will submit the following:

* A text file that lists values for each path segment
    * x,y coordinates of points P0, P1, P2, P3
    * Values for w1 and w2
* An image of a plot that shown the control points of all path segments
* An image of a plot that shows the 'smooth paths' that are defined by your path segments

Task
^^^^

The input (starting point) for this assignment is your pose list file that you created in HW 7. Each line contains UTM Easting (m), UTM Northing (m), heading (deg), and an integer state value.

You will be defining path segments between each successive pair of poses. The path segment is defined by four control points and two weighting values. 
These python programs will help:

:download:`make_route_segs.zip <./homework_files/make_route_segs.zip>`