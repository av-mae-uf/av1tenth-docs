Odometry Publisher
==================

The odometry publisher reads data from both the `QTPy connected encoder <../sensor.html#optical-encoder>`_ 
and the `Witmotion IMU <../sensor.html#imu>`_ that is onboard. This is done serially through UART ports on the Odroid computer.

Serial Class
^^^^^^^^^^^^

To achieve this there is a class that is written just to read serial commands and send appropriate data back when needed. The class is given below.

.. code-block:: python

    class OdomSerial:

        def __init__(self, port):
            self.serial_port = port
            self.serial_usb = serial.Serial(
                self.serial_port, baudrate=9600, timeout=10)

        def serial_read(self):
            byte = self.serial_usb.read().hex()
            return byte

        def serial_close(self):
            self.serial_usb.close()

        def nine_axis(self):
            self.serial_usb.write(
                bytes((chr(0xFF)+chr(0xAA)+chr(0x24)+chr(0)+chr(0x00)), 'utf-8'))

        def six_axis(self):
            self.serial_usb.write(
                bytes((chr(0xFF)+chr(0xAA)+chr(0x24)+chr(1)+chr(0x00)), 'utf-8'))

        def serial_readline(self):
            return self.serial_usb.readline()

        def serial_in_waiting(self):
            return self.serial_usb.in_waiting

The class essentially initializes by opening a port that is passed through when calling the class. These ports are defined later.
The function ``serial_read`` reads in hexadecimal values byte by byte. This reads in the IMU data. ``serial_readline`` function reads data until the ``\n`` byte
is hit. This is how the QTPy is publishing RPM data. The ``serial_close`` function closes the serial port. The ``nine_axis`` function sets the IMU into 9-axis 
mode, which enables the magnetometer. ``six_axis`` sets into 6-axis which is based on integrating the gyroscope. The ``serial_in_waiting`` informs whether there
is data being published on the specific serial port.

Data Parsing & Publishing
^^^^^^^^^^^^^^^^^^^^^^^^^

Next we have all the ROS2 critical code for the ``OdomPub`` node. Here we can see the assignment of ports, publishers, and parameter creation.
The ports of the IMU and encoder are set first.

.. code-block:: python

    self.serial_imu = OdomSerial('/dev/ttyUSB0')
    self.serial_encoder = OdomSerial('/dev/ttyUSB1')

Then a publisher is created which is standard stuff. Next to set the algorithm type, whether we want 9-axis or 6 axis, a parameter is declared and whether you enter
1 or nothing a certain algorithm is set.

.. code-block:: python

    self.declare_parameter('set_alg', 1)
    self.alg_type = self.get_parameter('set_alg')
    if self.alg_type.value:
        self.serial_imu.nine_axis()
    else:
        self.serial_imu.six_axis()

If the parameter is 1, the algorithm is 9-axis. If the parameter is anything else, the mode is 6 axis.

Next we define a callback ``odom_callback``. This is the main odometry call back of the node. First a set of variables are assigned. Once that is done, to read the encoder data
the ``readline`` function is called.

.. code-block:: python
    
    linear_speed = self.serial_encoder.serial_readline() 

Next the data is parsed through. First we read whatever byte is being published. if the first byte corresponds to a 55 we can start reading through all the data 
as this is the start byte. Then byte of 51 will indicate acceleration output. 52 will indicate velocity output. 53 is angle output and 54 is magnetic data output.
There is bit shifting to be done to get the correct data and calculations completed that give us usable information. To understand this a foundation of 
serialization is necessary. The parsing through of this data is given below.

.. code-block:: python

    if outputs == '51' and count == 1:
        acc_output = []
        for x in range(9):
            val = self.serial_imu.serial_read()
            acc_output.append(int(val, base=16))
        y_acc = (acc_output[1] << 8 | acc_output[0])/32768*16*9.81
        x_acc = (acc_output[3] << 8 | acc_output[2])/32768*16*9.81
        z_acc = (acc_output[5] << 8 | acc_output[4])/32768*16*9.81

    elif outputs == '52' and count > 1:
        ang_vel_output = []
        for x in range(9):
            val = self.serial_imu.serial_read()
            ang_vel_output.append(int(val, base=16))
        ydot = (ang_vel_output[1] << 8 |
                ang_vel_output[0])/32768*2000
        xdot = (ang_vel_output[3] << 8 |
                ang_vel_output[2])/32768*2000
        zdot = (ang_vel_output[5] << 8 |
                ang_vel_output[4])/32768*2000
    elif outputs == '53' and count > 1:
        angle_output = []
        for x in range(9):
            val = self.serial_imu.serial_read()
            angle_output.append(int(val, base=16))
        y_angle = (angle_output[1] << 8 |
                    angle_output[0])/32768*180
        x_angle = (angle_output[3] << 8 |
                    angle_output[2])/32768*180
        z_angle = (angle_output[5] << 8 |
                    angle_output[4])/32768*180
    elif outputs == '54' and count > 1:
        mag_output = []
        for x in range(9):
            val = self.serial_imu.serial_read()
            mag_output.append(int(val, base=16))
        mag_y = ((mag_output[1] << 8) |
                    mag_output[0])
        mag_x = ((mag_output[3] << 8) |
                    mag_output[2])
        mag_z = ((angle_output[5] << 8) |
                    mag_output[4])

If you want to understand bit shifting fully you can check out this `page <https://wiki.python.org/moin/BitwiseOperators>`_. 
Next the data is published in the form of a ``Odometry`` message. You can check out the documents 
`here <http://docs.ros.org/en/diamondback/api/nav_msgs/html/msg/Odometry.html>`_. The data for the orientation is published in the
`quaternion <../theoryinfo/quaternion.html>`_ form. It is then put into the appropriate format and part of the message and then published.











