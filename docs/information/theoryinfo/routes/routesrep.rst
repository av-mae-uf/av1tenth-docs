Route Representation and Navigation
===================================

Here we focus on how a route is defined and on how a vehicle can navigate along this route.  The route data will be defined based on information obtained from Google Earth.  The document aims to detail the following:

1.	the data format to be used to define the route
2.	the determination of the closest point on the route to the current vehicle position
3.	the determination of an instantaneous goal pose (look ahead pose)
4.	the determination of the x, y coordinate, heading angle tangent to the route, and radius of curvature at any point on the route
5.	the determination of the instantaneous steering angle based on the current goal pose and the current vehicle pose

They have all been separated into four different pages. They are given below

.. toctree::
    :maxdepth: 1
    :caption: Pages

    Definition of Series of Poses that will Define a Route <poseroute>
    Route Segment Definition <routeseg>
    Determination of Slope and Curvature for any Value of u on a Route Segment <slopecurve>
    Design of Basic Navigation System in ROS 2 <navsys>
