Motor Driver
=============
The motor driver node is intended to drive the main two actuators of the AV1tenth platform. This is achieved by serially communicating with the Pololu Micro Maestro Servo controller.

Serial Commands
^^^^^^^^^^^^^^^
The Pololu has a set of sepcific serial data that needs to be sent over. These commands have been packaged in to a serial class called "serial_cmds". That class is given below:

.. code-block:: python3
    
    class serial_cmds:
        def __init__(self):
            # Change according to what serial port you connected the Maestro to
            self.serial_port = '/dev/ttyACM1'
            self.serial_usb = serial.Serial(
                self.serial_port)  # Opening the serial port
            # Setting the command variable to Pololu Protocol. First command is just an arbitrary starting byte.
            self.pol_prot_cmd = chr(0xaa) + chr(0x0c)
            # Second number is device number, default is 12

        def serial_close(self):
            self.serial_usb.close()  # Closing the serial port after completion

        def cmd_out(self, cmd):
            cmd_out_byte = self.pol_prot_cmd + cmd
            self.serial_usb.write(bytes(cmd_out_byte, 'latin-1'))

        def pos_read(self, chan):

            cmd = chr(0x10) + chr(chan)
            self.cmd_out(cmd)
            lsb = ord(self.serial_usb.read())
            msb = ord(self.serial_usb.read())

            return (msb << 8)+lsb

        def set_target(self, chan, target):
            # When setting the target/acceleration/speed the first seven bits will be considered the low bits and the last 7 bits will be considered the high bits.
            #  This is shown by the target of 1500 us X 4 = 6000 which in binary is 0101110 1110000
            # Converting from microseconds to quarter microseconds for data transmission
            # target = 1500*4 # Uncomment for debugging
            lsb = int(target) & 0x7f
            msb = (int(target) >> 7) & 0x7f
            cmd = chr(0x04) + chr(chan) + chr(lsb) + chr(msb)
            self.cmd_out(cmd)

        def set_speed(self, chan, speed):
            lsb = speed & 0x7f
            msb = (speed >> 7) & 0x7f
            cmd = chr(0x07) + chr(chan) + chr(lsb) + chr(msb)
            self.cmd_out(cmd)

        def set_acc(self, chan, acc):
            lsb = acc & 0x7f
            msb = (acc >> 7) & 0x7f
            # This is the cmd byte data for the acceleration state
            cmd = chr(0x09) + chr(chan) + chr(lsb) + chr(msb)
            self.cmd_out(cmd)

The serial port is opened with a 9600 (standard) baud rate and an arbitrary byte and the device number which is 12.
You can daisy chain multiple of these servo controllers together, hence why the device number exists. That is the first part of the data that is to be sent.
Next there are different functions that sends the command, closes the serial port (self explanatory), reads position, sets a target, sets a speed, and sets the acceleration. 
The cmd_out function takes all the necessary conditions from the other functions and sends it serially to the servo controller. The rest of the functions act similarly.

To send data in a compact form the data is bit shifted 7 spaces to generate a high and low bit, ``lsb`` being lower bits and ``msb`` being high bits. Each function has a specific ``cmd`` variable that needs to be sent
to the cmd_out function. That variable defines whether you are setting the target, speed or acceleration with the first bit ``0x04``, ``0x07``, etc. and then adds in the lower and higher bits in order.
This is how the program communicates with the controller.

The target sets the position (PWM period of the signal) which is generated in quarter-microseconds. Which is 4*microseconds. The speed is the speed to achieve that target, and acceleration is the quickness to achieve that speed.
This will be true for the servo, for the drive motor the target will be speed, speed will be acceleration and the acceleration will be jerk, at least in a physical sense.

.. note:: This code will be standard, we recommend not changing it unless you are confident you understand what it does. 

ROS2, Callbacks and Logic
^^^^^^^^^^^^^^^^^^^^^^^^^
The next part of the code is the ROS2 critical code inside a ``__init__`` function. This is where you put in the subscriptions to a twist and a subscription for the warning LED's. All the ROS2 code is packaged in a ``MotorController`` class. That code is shown below.

.. code-block:: python

    def __init__(self):
        super().__init__('motor_controller')
        self.serial_ = serial_cmds()
        ##
        self.serial_.set_target(4, 3000)
        self.subscription = self.create_subscription(
            Twist, 'vehicle_command', self.cmd_send, 20)
        self.subscription  # prevent unused variable warning
        self.sub2 = self.create_subscription(
            Int16, 'led_color', self.led_cllbk, 20)
        self.sub2
        self.cmd_send
        self.lastmsg = 0

Here the serial class is called, ROS2 is initialized, and the LED's are set to off. 
Then the two subscriptions are called, one for ``vehicle_command`` topic and another for ``led_color`` topic. 
Both are self explanatory and each has a ``Twist`` and an ``Int16`` message being subscribed to it.
Next a callback for the LED subscription is defined, that is given below.

.. code-block:: python

        def led_cllbk(self, Int16):
        msg = Int16.data
        if msg is not self.lastmsg:
            if msg == 1:
                self.serial_.set_target(3, 6500)
                self.serial_.set_target(4, 3000)
            elif msg == 2:
                self.serial_.set_target(5, 6500)
                self.serial_.set_target(4, 3000)
        self.lastmsg = msg

Here the channels 3 corresponds to yello and 5 corresponds to red.
Green is the safe indicator and that correspondsto channel 4. 
As in normal subscriptions, the message data is pulled into a variable and then a conditional is used to check whether a red or yellow LED is desired. 
If the number 0 is sent, all LED's are turned off.

Next the main callback that handles the vehicle actuators is defined. This callback deals with taking your twist message and converting it into data that is
appropriate for the Pololu servo controller. First we have to assign a variable to the message, which here we call ``msg``. Thern to parse through the twist message, 
it is broken into two distinct functions inside the main class ``Twist``. Those are ``linear`` and ``angular``. Here we have the linear velocity and angular velocity
of the vehicle respectively. Their units are ``m/s`` and ``rad/s``.
 
.. code-block:: python
        
        msg = Twist
        self.linear = float(msg.linear.x)  # m/s, +ve for fwd, -ve for rev
        self.angular = float(msg.angular.z)  # rad/s, +ve for CCW rotation

Next to convert the linear velocity to a PWM signal we first conver the velocity into a throttle effort. This is based on the maximum speed the car can go.
An estimation is done to determine the max speed based on the max RPM of the wheels and the wheel size. It is determined the car can travel at

.. code-block:: python

    MAX_LINEAR_SPEED = 585*(2*pi*120e-3)/60

Which is about ``7.35 m/s``. This is defined at the beginning as a global variable. Next a throttle ratio equation is used to figure out what the ratio of linear speed to change in throttle effort is used.

.. code-block:: python

    ratio_throttle = (self.linear/MAX_LINEAR_SPEED)*3000

The 3000 multiplication at the end is to ensure there is a value between 3000 and -3000. Then the throttle effort can be calculated.

.. code-block:: python

    thrtle_eff = round(6000 + ratio_throttle)

This ensures a minimum value of 3000 quarter-microseconds or 750 microseconds and a maximum value of 9000 quarter-microseconds or 2250 microseconds. The neutral point is 6000
or 1500 microseconds. The neutral point defines when the car stops from going backward to forward. 3000 being max speed backward and 9000 being the max speed forward.

To calculate the servo angle (basically a PWM value that corresponds to an steering angle) a conditional is used. 
This is to convert the angular rate to be between -45 and 45 degrees (The maximum steering value for the car). The conditional basically ensures there is not infinite values in the radius of curvature.

.. code-block:: python

        if self.angular < 1e-2 and self.angular > -1e-2:
            rad_curv = float(1e17)
        else:
            rad_curv = float(self.linear/self.angular)
            if rad_curv < 1e-2 and rad_curv > -1e-2:
                rad_curv = 1e-10

        steer_angle = atan(WHEELBASE/float(rad_curv))*R2D  # degrees

The last equation is converting the radius of curvature back to a steering angle. This is based on the bicycle kinematic model. The kinematic of our car is slightly off,
so a supposed twist needs to be linearly multiplied to get an actual value of the radius of curvature. The simplest way to calculate radius of curvature is :math:`\dfrac {\dot{x}} {\dot{\phi}}`.


Then a ratio is defined to correlate a steering angle to a PWM signal. That is done by using:

.. code-block:: python

    ratio_steering = 3000/45

Then a PWM signal can be formed that will be between 3000 and 9000. 

.. code-block:: python

    steering_target = round(6000 - steer_angle*ratio_steering)

The channels for the drive motor and the servo steering motor are set next. They are 1 for the drive motor and 0 for the steering servo. Once this has
been completed you can serially send the appropriate commands to the servo controller.

.. code-block:: python

        self.serial_.set_speed(steering_chan, speed_steering)
        self.serial_.set_speed(drive_chan, speed_drive)
        self.serial_.set_acc(steering_chan, acc_steering)
        self.serial_.set_acc(drive_chan, acc_drive)
        self.serial_.set_target(drive_chan, thrtle_eff)
        self.serial_.set_target(steering_chan, steering_target)


Shutting Down the Node
^^^^^^^^^^^^^^^^^^^^^^

To appropriately shut down the node, a Try, Except and finally python function is used. This is to ensure that once the node is shutdown, the car will not continue to drive and to 
return the lights to a safe mode.


.. code-block:: python

     try:
        rclpy.spin(motor_controller)

    except KeyboardInterrupt:
        serial_cmds().set_target(1, 6000)
        serial_cmds().set_target(4, 6500)
        serial_cmds().set_target(3, 3000)
        serial_cmds().set_target(5, 3000)
    finally:
        motor_controller.destroy_node()
        rclpy.shutdown()
