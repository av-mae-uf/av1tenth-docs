Milestone 3: Processing Bag Data
======================================================

This assignment covers working on processing your bag data that you collected and plotting the GPS data in a graph and in Google Earth submitting a PDF.

.. note:: We have a couple of bag files that we have created with team names in the av1tenth repo under ``bag_files`` if you weren't able to collect your bag file.

* **Due Date:** November 4th, 2022
* **Points:** 20
* ROS 2 Topics: GPSData (pub)
* ROS 2 Messages: ``PoseStamped`` ( in ``geometry_msgs``)

You can play a bag file with the following command.
  
.. code-block:: bash

    ros2 bag play -l <bag_file_name>

Deliverables
^^^^^^^^^^^^
A PDF with the two plots for GPS.

Bag File Output to a CSV File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To plot the data a file was given that is just the python file for a ROS2 Node. You will have to put this in a package and write the appropriate entry points. You should be 
able to do this now with ease. Run the converters first before running your bag file.

The two files for the GPS converter and Odometry converter is given below.

:download:`GPS Processor <milestone_files/process_GPSData_bagfile.py>`

:download:`Odometry Processor <milestone_files/process_Odom_bagfile.py>`

The GPS data is UTM data and the Odometry data is in the form of Quaternions. These two nodes will output a file that is of the format ``.txt``. You can take the values and put both into Excel with the Text Import Wizard.
You might need to set the first point of your data as the zero point so all your other Poses can be scaled to that point. This can be done by subtracting all the other points from the first
point. Your points should start with a ``0,0`` in the first row.

GPS Data to Google Earth
^^^^^^^^^^^^^^^^^^^^^^^^

So you have your data in UTM and you will need to put it into Google Earth in the form of Latitude and Longitude. You can either do this through python using the ``utm`` python
library and using the function ``utm.to_latlon``. Pertinent information for this will be that we are in Zone 17R.

You can also do this through the website `Zonum Solutions UTM to LatLong Converter <http://www.zonums.com/online/coords/cotrans.php?module=14>`_. The same information for the zone above applies here.
This can take a comma seperated list and output a comma seperated list. The python file you will have to get creative to output it correctly. 

You can now take this into Google Earth and plot these as a path. A video of how to do this is located `here <../../assistance/videos.html>`_

.. 
    Odometry to RViz
   To show your data in RViz, you can run the bag file, open RViz, add and then By Topic and you should see a message called odometry being published. You will need to change the frame to ``odom`` for this to work in RViz.
    You should now see your orientation plotted as an arrow changing continuously and overlapping.





    That's pretty much all you need to be successful in completing this milestone. If you have any problems `contact the TA's or Instructor <../../assistance/contact.html>`_.

