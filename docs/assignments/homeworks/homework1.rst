Homework 1: Inside/Outside Polygon
==================================

This assignment introduce you to the fundamentals of python.

* **DUE DATE:** TBD
* **POINTS:** 20

Deliverables
^^^^^^^^^^^^

Write a Python function named 'is_inside' that takes two inputs

* an n by 2 numpy array which represent the x, y coordinates of a polygon
* a length 2 numpy array which represent the x, y coordinates of some point

The function will return true if the point is inside the polygon.  It will return false otherwise. 

Provide an example of calling the function for a case where:

* the point is inside the polygon
* the point is outside the polygon
* the point is on one of the sides of the polygon.

Python
^^^^^^

Installation
""""""""""""

To install Python on Windows, visit the official website:  
https://www.python.org/downloads/ and follow the installation instructions for your operating system.  

On Ubuntu, Python should already be preinstalled.  

Running a Script
""""""""""""""""

To run a Python script, open a terminal and type:

.. code-block:: bash

   python myscript.py

Replace ``myscript.py`` with the name of your file.  

.. important:: If you are on Ubuntu and receive the error ``Command 'python' not found``, try:

    .. code-block:: bash

        python3 myscript.py

.. note:: Additionally, VS Code has a play button that can quickly run your script as well.  

NumPy
^^^^^

Installation
""""""""""""

To install NumPy using ``pip`` on Windows, open a terminal and type:

.. code-block:: bash

   pip install numpy


On Ubuntu, you can also install with:

.. code-block:: bash

   sudo apt install python3-numpy


.. note::
    Alternatively for Ubuntu (but not recommended), you can run:

    .. code-block:: bash

        pip3 install numpy --break


Adding numpy to a python script
"""""""""""""""""""""""""""""""

To add numpy, enter the following to the beginning of the script:

.. code-block:: python

    import numpy as np


Here is an example code on how to use:

.. code-block:: python

   import numpy as np

   # create a 2D array representing points of a triangle
   polygon = np.array([[0, 0],
                       [2, 0],
                       [1, 2]])

   # create a point
   point = np.array([1, 1])

   print("Polygon array shape:", polygon.shape)
   print("Point array shape:", point.shape)

This should output:

.. code-block:: text

   Polygon array shape: (3, 2)
   Point array shape: (2,))

.. note:: For more information, here are some useful links:

    * https://numpy.org/
    * https://pypi.org/project/numpy/

