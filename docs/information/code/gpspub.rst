GPS Publisher
==============

The GPS publisher interfaces with the `GPS Module <../sensor.html#gps>`_ on top of 
the car and publishes data in the `UTM standard <https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system>`_.

The GPS Module uses a serial connection to communicate data back and forth. The data is sent and received in the form of `NMEA strings <https://www.gpsworld.com/what-exactly-is-gps-nmea-data/>`_.
There is quite a lot of detail that goes into this data format, so that will not be discussed here. A package is used to parse through the data that is sent or recieved. That package
is the `Adafruit GPS Library <https://docs.circuitpython.org/projects/gps/en/latest/index.html>`_. It essentially parses through the NMEA data and sends NMEA data when appropriate.

ROS2 and GPS Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^

First we must initialize both the GPS module and the ROS2 node. In this initialization, the serial port, the rate of publish, the types of GPS data (RMC, GGA, etc.) are setup.
The type of port can also be seleted, here we are using UART to setup the port.

.. code-block:: python

    uart = serial.Serial("/dev/ttyAML1", baudrate=9600, timeout=10)
    self.gps = adafruit_gps.GPS(uart, debug=False)
    #                               A B C D E F G H 
    self.gps.send_command(b"PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    #   A - send GLL sentences
    #   B - send RMC sentences
    #   C - send VTG sentences
    #   D - send GGA sentences
    #   E - send GSA sentences
    #   F - send GSV sentences
    #   G - send GRS sentences
    #   H - send GST sentences
    #   I - send ZDA sentences

The last command sets what type of data you want (RMC) for us. You can choose to have more data like the HDOP etc. The next important command is the rate command. Here it has been set to 5Hz

.. code-block:: python

    self.gps.send_command(b"PMTK220,200")

The number is in milliseconds. :math:`200 ms` i.e. 5Hz.

Next the ROS2 publisher is initialized, here we have a publisher that publishes at a rate of :math:`330 ms` which is about 3 Hz.

.. code-block:: python

    self.publisher_ = self.create_publisher(Pose, 'GPSData', 10)
    timer_period = 0.33
    self.timer = self.create_timer(timer_period, self.timer_callback)

Next to log the data, we have a file that the UTM data is written to for debugging. To open the file we use the following command:

.. code-block:: python

    self.fp = open('/home/cimar/lat_long.txt', 'w')

Callback and Data Parsing
^^^^^^^^^^^^^^^^^^^^^^^^^
Next we have the main and only call back of this node ``timer_callback``. The first line of code cleans out the gps serial buffer. This is to ensure we are getting current
values and not old values.

.. code-block:: python
        
    while self.gps.update():  # clean out buffer
        pass

Then we have logic to ensure that the data is updated and checked every 3 Hz. First the data is checked for a GPS fix, if there is now fix, a logger is used to print
"Waiting for fix" and then it checks for an update again until it has a fix.

.. code-block:: python

        self.current = time.monotonic()
        if self.current - self.last_print >= 0.32:
            self.last_print = self.current
            while not self.gps.has_fix:
                time.sleep(0.5)
            # Try again if we don't have a fix yet.
                self.get_logger().info('Waiting for fix')
                self.gps.update()

Then once there is a fix, immediateley the latitude and longitude data is converted into UTM Easting and Northing data. The units will be in meters.

.. code-block:: python

    utmData = utm.from_latlon(self.gps.latitude, self.gps.longitude)

A set of logic is used to set a time stamp. This is to ensure that data is consistent

.. code-block:: python

    if (self.last_time_sec != self.gps.timestamp_utc.tm_sec):        
        self.last_time_sec = self.gps.timestamp_utc.tm_sec

All the UTM data is put into seperate variables for ease of understanding instead of storing it in a list.

.. code-block:: python

    self.east = utmData[0]
    self.north = utmData[1]
    self.zoneNum = utmData[2]
    self.zoneLetter = utmData[3]

To publish this data we use a ROS2 message called a Pose. A pose holds position and orientation data. We can calculate an azimuth angle using the tracking angle from the GPS.
This is achieved by taking two points and figuring out what the angle is based upon true East.

.. code-block:: python

        msgUTM.position.x = self.east
        msgUTM.position.y = self.north
        msgUTM.position.z = 0.0
        msgUTM.orientation.z = 0.0
        msgUTM.orientation.x = 0.0
        msgUTM.orientation.y = 0.0
        msgUTM.orientation.w = 0.0

Then you publish the data. There is a couple of loggers in the node to ensure the data is being published and for ease of debugging.


