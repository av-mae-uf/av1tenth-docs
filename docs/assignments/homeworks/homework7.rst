Homework 7: Define a Path
=========================

General Overview
^^^^^^^^^^^^^^^^

* **DUE DATE:** TBD
* **POINTS:** 30
* ROS 2 Topics: TODO
* `ROS 2 Messages <../../information/ros2_common_msgs.html>`_ : TODO

Deliverables
^^^^^^^^^^^^

* Pose list text file
* JPG image of poses 

Task
^^^^

.. warning:: Double check that the files on this page are the same as the one provide on Canvas. The kml positions could have changed since the last time this page was edited.

You are given a kml formatted file that contains the latitude and longitude of a 'start/end' location and four points. The KML File is located on :download:`here <./homework_files/Reitz_Spring2024.kml>`.

You will be defining a path that will go from the 'start/end' location to each of the four points and then back to the 'start/end' location. The path will be defined by a text file that has a series of poses.

Each line of the file will have an x, y UTM coordinate, followed by the desired pose angle (measured in degrees, where East is 0 deg), followed by an integer state value (just use 1). Values are separated by a comma. A comment may be placed in your text file by having the first character on a line be the # character. A sample pose list file is available :download:`here <./homework_files/example_pose_list.txt>`.

The program :download:`kml_to_route.py <./homework_files/kml_to_route.py>` may make the task easier. Create a path in Google Earth where two successive points define a pose (the first point gives the location and that point and the next define the orientation). Save the path as a kml file. Run the program kml_to_route.py, passing the name of your kml file as a parameter followed by the name of the file that you want your pose list written to.

.. code-block:: bash

    python3 kml_to_route.py input_file.kml output_file.txt
 
Upload your pose list file and a jpg image showing the poses in your pose list file.  A python program that reads the text file and draws the set of poses is available :download:`here <./homework_files/plot_pose_list.py>`.