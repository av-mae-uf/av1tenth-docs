Twist Message
==============

The twist message is based on the screw interpretation of a velocity state. A screw being a 6-dimensional vector that can describe translational and rotational motion in a rather elegant form.
A screw was first defined by Robert Ball in 1900 [1]_ . As this is not a class on Screws we will not go into great detail, if you are interested in more check out the class
EML 6282 - Robot Geometry 2 taught by Dr. Crane usually in the Spring semester. Dr. Crane, Dr. Griffis and Dr. Duffy (The formers mentor) wrote a book [2]_ on screw theory if you are interested

The twist message defines a set of six variables. Usually a twist is written as 

.. math::

    \vec{T} =   \begin{bmatrix}
                \dot{x}\\
                \dot{y}\\
                \dot{z}\\
                \dot{\phi_x}\\
                \dot{\phi_y}\\
                \dot{\phi_z}\\
                \end{bmatrix}

where :math:`\dot{x}` ... is the linear velocity and :math:`\dot{\phi_x}`... is the angular velocity. In our case for our car, we will only have a :math:`\dot{x}` linear velocity and 
:math:`\dot{\phi_z}` angular velocity or yaw rate. The rest of them will be 0. In code you can define such a message as follows.

.. code-block:: python

    Twist().linear.x = linear_velocity_x
    Twist().linear.y = linear_velocity_y
    Twist().linear.z = linear_velocity_z

    Twist().angular.x = angular_velocity_x
    Twist().angular.y = angular_velocity_y
    Twist().angular.z = angular_velocity_z

The twist message is one of the most used messages for us, as it transmits motion messages between our computer and our motor controller node. In simulation this will also be the only message that one can use to convey motion.

.. [1] R. S. Ball, A Treatise on the Theory of Screws, Cambridge University Press, 1900.

.. [2] C. D. Crane III, M. Griffis and J. Duffy, Screw Theory and Its Application to Spatial Robot Manipulators, Gainesville: Cambridge University Press, 2020. 
