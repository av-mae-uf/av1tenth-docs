Proportional, Integral and Derivative Controllers
=================================================

PID controllers are the most basic form of controllers out there. They are split into three categories of Proportional, Integral and Derivative.
Each category is explained under different headings, but you can have combinations of two categories such as PI or PD or PID controllers.

There are many examples of PID controllers used in the real world. A couple of them are cruise control and thermostats. 
Essentially they allow you maintain a state and compensate for external factors. The idea is to minimize :math:`e(t)` which is the error of the system.

Proportional Controller
^^^^^^^^^^^^^^^^^^^^^^^

A proportional controller multiplies your input by a fixed gain to achieve a desired output. The equation for such a controller would be

.. math::

    u = K_p e(t)\tag{1}

where

.. math::

    e(t) = r - y.

:math:`K_p` is the proportional gain, :math:`u` is the input of the system, :math:`r` is the desired set point and :math:`y` is the output of the system.

These types of controllers will tend to have poor tracking and a steady-state error as they are just multiplying our error by a fixed gain. This can further cause the system to become unstable and have large oscillations if the proportional gain is too high.

Integral Controller
^^^^^^^^^^^^^^^^^^^
An integral controller integrates the system error over time and multiplies that by an integral gain. The equation for such a controller would be

.. math::

    u = \int_{0}^{t} K_i \, e(t) \, dt. \tag{2}

Another way of writing this is

.. math::

    u = K_i \sum_{k=1}^{k} e_k \Delta t

The integral term reduces the rise time of your control response and eliminates any steady-state errors in your system. Though there is a large chance that your integral 
term will cause your control command to overshoot the set point.

Derivative Controller
^^^^^^^^^^^^^^^^^^^^^

A derivative controller multiplies a gain by the derivative or slope of your error over time. The equation of this controller would be

.. math::

    u = \dfrac{d}{dt} e(t) K_d. \tag{3}

Another way of writing this would be
 
.. math::

    u = K_d \dfrac {e_k - e_{k-1} } {t_k - (t_k-1)}

This controller helps with maintaining stability and ensures that the system settles quickly.


PID Controller
^^^^^^^^^^^^^^

As stated earlier you can use combinations of the Proportional, Integral or Derivative terms to create a controller. 
Most commonly a PI controller is used as the derivative term tends to have variable effects on the stability of the system. A full PID controller equation would look something like

.. math::
    
    u = K_p e(t) + \int_{0}^{t} K_i \, e(t) \, dt + \dfrac{d}{dt} e(t) K_d \tag{4}

or

.. math:: 

    u = K_p e_k + K_i \sum_{k=1}^{k} e_n \Delta t + K_d \dfrac {e_k - e_{k-1} } {t_k - (t_k-1)} \tag{5}

When you are working on any controllers in code, you probably want to use equation 5. You must understand how these terms work and how to implement them in code first!






