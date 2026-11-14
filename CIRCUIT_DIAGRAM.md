# Wiring and Circuit Connections for Liberty-Bot

Before ordering any parts, I wanted to map out every single wire and pin connection so that when my father and I sit down to assemble the robot, we do not accidentally plug a power wire into the wrong pin and short-circuit the Raspberry Pi 5.

## How the Power Split Works

The most important part of this wiring setup is keeping the motor power away from the Raspberry Pi's 5V rail. A Raspberry Pi 5 uses 3.3V logic on its GPIO pins, and its 5V header pins are directly connected to the USB-C input. If I tried to run four MG90S metal-gear servos directly off the Raspberry Pi's 5V pin, the sudden burst of current when the robot raises its arm for a handshake or turns its head would cause a voltage drop on the Pi, making it freeze or restart.

To solve this cleanly, the circuit uses two separate wall adapters:
1. The official 27W USB-C power supply plugs straight into the USB-C power port on the Raspberry Pi 5. This powers the Pi, the cooling fan, the camera module, the screen, and the audio microphones.
2. A separate 5V 3A DC adapter connects directly to the green screw terminal block (labeled V+ and GND) on top of the PCA9685 servo driver board. This adapter only powers the four MG90S servo motors.

On the PCA9685 board, the logic power pin (VCC) connects to the Raspberry Pi's 3.3V pin (Pin 1), and the ground pin (GND) connects to the Raspberry Pi's Ground (Pin 6). Tying the grounds together gives both circuits a common electrical reference so the I2C data signals work reliably, while the 5V motor power stays isolated on the V+ line.

## Step-by-Step Pin Connections

### 1. Connecting the PCA9685 Servo Board to the Raspberry Pi 5 (I2C Bus)
The PCA9685 board uses the I2C protocol, which only needs four Female-to-Female DuPont jumper wires from the side header of the PCA9685 to the Raspberry Pi GPIO header:
* **PCA9685 VCC** connects to **Raspberry Pi Pin 1 (3.3V DC Power)**. This powers the small control chip on the servo board at safe 3.3V logic levels.
* **PCA9685 GND** connects to **Raspberry Pi Pin 6 (Ground)**.
* **PCA9685 SDA** connects to **Raspberry Pi Pin 3 (GPIO 2 / SDA1)**. This wire carries the I2C data packets telling the board which servo to move.
* **PCA9685 SCL** connects to **Raspberry Pi Pin 5 (GPIO 3 / SCL1)**. This wire carries the I2C clock signal.

### 2. Plugging the Four MG90S Servos into the PCA9685 Board
Each MG90S servo has a 3-wire cable: Brown (Ground), Red (5V Power), and Orange (PWM Signal). They plug straight into the 3-pin headers along the bottom of the PCA9685 board:
* **Channel 0:** Head Pan Servo (rotates the neck left and right, 0 to 180 degrees).
* **Channel 1:** Head Tilt Servo (nods the head up and down, 30 to 150 degrees so the camera cable never gets pinched).
* **Channel 2:** Left Arm Servo (moves the left arm up and down for waving or gestures).
* **Channel 3:** Right Arm Handshake Servo (raises the right arm forward when I ask the robot for a handshake).
* **Channels 4 through 15:** Left empty for now so I can plug in additional servos later when I modify the robot.

### 3. Connecting the Camera Module 3
The Raspberry Pi 5 uses smaller 22-pin MIPI camera connectors (labeled CAM/DISP 0 and CAM/DISP 1) right between the HDMI ports and the Ethernet port.
* One end of the 30cm flexible FPC ribbon cable (the wider 15-pin end) clips into the Raspberry Pi Camera Module 3 inside the robot's head.
* The other end (the narrower 22-pin end) routes down through the neck bracket and locks into the **CAM/DISP 0** port on the Raspberry Pi 5, with the metal contacts facing toward the Ethernet port.

### 4. Connecting the ReSpeaker Audio HAT and 3W Speaker
Audio input and output are handled over the I2S digital audio pins so the sound does not have static interference:
* The ReSpeaker 2-Mics HAT sits on the GPIO pins (using GPIO 18, 19, 20, and 21 for I2S audio clock and data, while passing through the I2C pins needed for the servo board).
* The 3W enclosed chamber speaker has a small white 2-pin JST plug that clicks directly into the speaker output socket on the ReSpeaker board.

### 5. Connecting the 3.5-inch IPS Eye Display
The 3.5-inch display mounts on the front chest/face plate of the robot and connects to the Raspberry Pi display interface to render the 60 FPS eye animations.

### 6. Connecting the Active Cooler Fan
The official Raspberry Pi 5 Active Cooler snaps onto the two mounting holes around the processor using spring-loaded push pins, and its 4-pin PWM fan plug connects into the dedicated small white **FAN** header located in the top-right corner of the Raspberry Pi 5 board (between the 40-pin GPIO header and the USB ports). This lets the operating system automatically speed up the fan only when the processor gets warm.

## Text Map of the Wiring

```text
[ Wall Socket 1 ] ---> 27W USB-C Adapter ---> [ Raspberry Pi 5 USB-C Port ]
[ Wall Socket 2 ] ---> 5V 3A DC Adapter  ---> [ PCA9685 V+ and GND Screw Terminals ]

[ Raspberry Pi 5 ]
   |-- FAN Header ------------> Official Active Cooler Blower Fan
   |-- CAM/DISP 0 Port -------> 30cm FPC Cable ---> Camera Module 3 (in Robot Head)
   |-- Video / SPI Display ---> 3.5-inch IPS Screen (Front Face Eyes)
   |-- I2S Audio Pins --------> ReSpeaker 2-Mics HAT ---> JST Plug ---> 3W Speaker
   |-- Pin 1 (3.3V) ----------> PCA9685 VCC
   |-- Pin 6 (GND) -----------> PCA9685 GND
   |-- Pin 3 (GPIO 2 / SDA) --> PCA9685 SDA
   |-- Pin 5 (GPIO 3 / SCL) --> PCA9685 SCL
                                   |
                                   |-- Channel 0 ---> MG90S Servo 1 (Neck Pan Left/Right)
                                   |-- Channel 1 ---> MG90S Servo 2 (Neck Tilt Up/Down)
                                   |-- Channel 2 ---> MG90S Servo 3 (Left Arm Wave)
                                   |-- Channel 3 ---> MG90S Servo 4 (Right Arm Handshake)
```
