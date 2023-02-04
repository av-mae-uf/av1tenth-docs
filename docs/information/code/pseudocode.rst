Pseudo Code
===========

Pseudo Code is an informal method of putting down information regarding your algorithm. We will be using it to simply put down information regarding your ROS2 nodes,
before you begin writing code. Doing this will help keep you organized when you are in groups. A general example for completing pseudo code is given below.

.. code-block:: bash

    Node 1: Publisher
    Import messages Vector 3
    Import math for cos sin pi
    import time for program time possibly

    Node Init:
        
        publisher with topic my_point_topic;  message vector 3
        timer with period 0.5
        declare a t = 0 that you can interface in the callback (this means self.t)

    Node Timer Callback
        t = 
        x = 5.0*cos(1.2*t+ pi/2)
        y = 8*sin(0.6*t)
        z = 0
        publish Vector3 message

    -------------------------------------------------------------------------------------------------------

    Node 2: Sub and Pub
    Import messages Float64MultiArray Vector3
    Import math for cos sin pi


    Node Init:
        
        subscriber with topic my_point_topic;  message Vector3
        publisher with topic my_polar_topic; message Float64MultiArray

    Node Sub Callback
        r = mag(x,y)
        stheta = y/r
        ctheta = x/r
        theta = atan2(ctheta, stheta) 
        publish Float64MultiArray message


.. note:: There is no real format to this for us, as long as it is understandable, we will accept it.
