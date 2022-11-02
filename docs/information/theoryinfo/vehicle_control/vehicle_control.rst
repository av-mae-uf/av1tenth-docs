Vehicle Controller Approaches
=============================

There are three vehicle controller approaches for path following that will be discussed and looked at in this class. 
The pure pursuit algorithm, the stanley controllerand the 3rd order curve controller. There are other vehicle controllers 
such as the Model Predictive Control (MPC) and the Linear Quadratic Regulator (LQR) that are often used in practice for path following.
 
.. note:: A `PID <../pid.html>`_ will work as well for path following but it tends to have many drawbacks to it as it is essentially just 
    minimizing a single error.

.. toctree::
    :maxdepth: 1
    :caption: Controllers

    Pure Pursuit Controllers <pure_pursuit>
    Stanley Controller <stanley>
    Third Order Curve Controller <third_order>

