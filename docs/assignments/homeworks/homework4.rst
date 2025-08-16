Homework 4: Coordinate Transformations
======================================

* **Due Date:** TBD
* **Points:** 30

A point has been measured in the lidar sensor coordinate system as

.. math::

   ^{lid}P_{1} = \begin{bmatrix} 2.7 \\ -1.5 \\ 23.1 \end{bmatrix} \; \text{m}

The lidar coordinate system is initially aligned with the vehicle coordinate system. Its origin is translated to the point 

.. math::

   ^{veh}P_{lid0} = \begin{bmatrix} 4.0 \\ 0.0 \\ 0.8 \end{bmatrix} \; \text{m}

It is then rotated :math:`85^\circ` about its Y axis followed by :math:`10^\circ` about its modified X axis.

The vehicle coordinate system is initially aligned with a fixed world coordinate system. Its origin is translated to the point

.. math::

   ^{F}P_{veh0} = \begin{bmatrix} 200.0 \\ 185.4 \\ 0.25 \end{bmatrix} \; \text{m}

It is then rotated :math:`75^\circ` about its Z axis.

Deliverables
^^^^^^^^^^^^

Determine the coordinates of point 1 in the fixed world coordinate system. Show your work either handwritten or through a Python script.
