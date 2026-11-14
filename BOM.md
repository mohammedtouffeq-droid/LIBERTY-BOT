# Bill of Materials (BOM) for Liberty-Bot

When my father and I sat down to figure out what we needed to build Liberty-Bot, my biggest worry was ordering the main boards and then realizing when the box arrived that we were missing a ribbon cable, a power adapter, or the right size screws to hold everything together. Because I do not have spare electronics parts lying around at home, this list has to be 100% complete from top to bottom so that we can assemble the entire robot right out of the box without getting stuck.

## Why I am ordering from Indian Suppliers (Robu.in and Silverline Electronics)

Since I live in India, importing electronics parcels from the United States or Europe through international couriers like DHL or FedEx usually causes two huge problems. First, international shipping alone costs $50 to $70, which eats up a big chunk of the grant budget just on postage. Second, Indian Customs at the airport frequently holds electronics shipments and charges heavy import duties (up to 40% or more) at the time of delivery. I cannot afford to pay surprise customs bills at my doorstep.

By ordering everything domestically from authorized Indian electronics distributors like Robu.in and Silverline Electronics (who are official Raspberry Pi resellers in India), the parts ship from warehouses inside India via local courier (BlueDart or Delhivery). It arrives in 3 to 4 days, costs almost nothing for shipping, and has zero customs duty or doorstep fees.

## Detailed Explanation of Every Part in the List

**1. Raspberry Pi 5 (8GB RAM) and Official Active Cooler**
The Raspberry Pi 5 8GB is the brain of the robot. I chose the 8GB model instead of the 4GB one because I want the robot to last for years as I keep adding heavier features to it. Handling live video frames from the camera, converting speech to text, generating voice responses, and updating the screen takes significant RAM. The official Active Cooler clips directly onto the Pi 5 board with thermal pads and a blower fan so the CPU stays cool during long study sessions.

**2. SanDisk Extreme 64GB MicroSD Card (A2 Rated)**
The operating system (Raspberry Pi OS 64-bit) and all the Python scripts live on this card. I picked an A2-rated card because cheaper memory cards are really slow at small random reads and writes, which makes Linux feel laggy when opening camera streams or audio files.

**3. Raspberry Pi Camera Module 3 (12MP with Autofocus) and 30cm Ribbon Cable**
This is the robot's eye. Unlike the old V2 camera which has a fixed lens, the Camera Module 3 has a motorized autofocus lens. When I hold my notebook or a textbook page 15cm in front of the robot and ask it to help me solve a problem, the autofocus makes the small text sharp so the AI can actually read what is written. Also, the standard cable that comes in the camera box is only 15cm long and uses the older wide connector, so I included a 30cm Raspberry Pi 5 compatible FPC camera cable. The extra length gives the neck plenty of slack to rotate left, right, up, and down without pulling on the socket.

**4. 3.5-inch IPS Display Screen**
This screen mounts on the front face of the robot to display animated digital eyes and status text. I chose an IPS panel because IPS screens have wide viewing angles, meaning I can clearly see the robot's expressions even if it is sitting at the corner of my study table.

**5. ReSpeaker 2-Mics Pi HAT and 3W Enclosed Speaker**
The Raspberry Pi 5 does not have a built-in microphone or a built-in speaker amplifier. The ReSpeaker HAT plugs into the GPIO header and gives the robot two microphones for clear voice pickup across my desk, plus an onboard audio chip and speaker connector. The 3W enclosed chamber speaker plugs straight into it so the robot can speak out loud clearly.

**6. PCA9685 16-Channel PWM Driver and 4x MG90S Metal Gear Servos**
To make the robot look at me, nod its head, wave, and raise its hand for a handshake, I am using four MG90S micro servos. I specifically picked MG90S servos with metal gears instead of cheap plastic SG90 servos so the gears do not strip or snap over time. The PCA9685 board sits between the Raspberry Pi and the servos so that motor power is kept completely separate from the Pi, and it leaves 12 extra motor channels open for future upgrades.

**7. Dual Power Supplies (27W USB-C for Pi + 5V 3A DC for Servos)**
The Raspberry Pi 5 needs a stable 5.1V 5A (27W) USB-C power adapter to run peripherals at full speed without low-voltage warnings. The second 5V 3A DC adapter plugs into the PCA9685 servo board so that moving all four motors at once never drains power from the Raspberry Pi.

**8. Mechanical Brackets, Brass Standoffs, Jumper Wires, and Baseplate**
To mount the head and arms, I included an aluminum/acrylic pan-tilt and bracket kit. To make sure my father and I have every screw and wire needed for assembly, I added a 120-piece M2.5/M3 brass standoff and screw kit, a 120-piece assortment of DuPont jumper wires (Male-to-Female, Female-to-Female, Male-to-Male), and a heavy desktop baseplate with rubber feet so the robot stands firmly on my table.

## Complete Cost Breakdown Table

| Item No. | Component Name | Why it is needed | Vendor (India) | Qty | Price (INR) | Price (USD approx.) |
|---|---|---|---|---|---|---|
| 1 | Raspberry Pi 5 (8GB RAM) | Main computer board running Linux and AI logic | Silverline / Robu.in | 1 | Rs. 8,500 | $101.20 |
| 2 | Official Raspberry Pi 5 Active Cooler | Heatsink and temperature-controlled fan | Silverline / Robu.in | 1 | Rs. 600 | $7.15 |
| 3 | SanDisk Extreme 64GB A2 MicroSD Card | Fast boot drive for Raspberry Pi OS | Robu.in | 1 | Rs. 800 | $9.50 |
| 4 | Raspberry Pi Camera Module 3 (Autofocus) | 12MP camera to focus on close-up book pages | Robu.in / Silverline | 1 | Rs. 2,500 | $29.75 |
| 5 | 30cm Pi 5 Camera FPC Ribbon Cable | Long flexible cable for the moving neck | Robu.in | 1 | Rs. 200 | $2.40 |
| 6 | 3.5-inch IPS Display Screen | Front face display for animated robot eyes | Robu.in | 1 | Rs. 2,400 | $28.55 |
| 7 | ReSpeaker 2-Mics Pi HAT | Dual microphones and audio driver board | Robu.in / Thingbits | 1 | Rs. 1,500 | $17.85 |
| 8 | 3W Chamber Stereo Speaker | Speaker for the robot's voice output | Robu.in | 1 | Rs. 400 | $4.75 |
| 9 | PCA9685 16-Channel PWM Servo Driver | I2C controller board to isolate motor power | Robu.in | 1 | Rs. 450 | $5.35 |
| 10 | MG90S Metal Gear Micro Servos (Pack of 4) | 2 servos for neck pan/tilt, 2 for left/right arms | Robu.in | 4 | Rs. 900 | $10.70 |
| 11 | Official 27W USB-C Power Supply | Main power adapter for the Raspberry Pi 5 | Silverline / Robu.in | 1 | Rs. 1,300 | $15.50 |
| 12 | 5V 3A DC Power Supply Adapter | Separate power adapter dedicated to servo motors | Robu.in | 1 | Rs. 500 | $5.95 |
| 13 | Pan-Tilt & Arm Mounting Bracket Kit | Brackets and horns to attach servos to head and arms | Robu.in | 1 | Rs. 900 | $10.70 |
| 14 | 120pc M2.5 & M3 Brass Standoff Screw Kit | Screws, nuts, and spacers to mount all boards | Robu.in | 1 | Rs. 450 | $5.35 |
| 15 | 120pc DuPont Jumper Wire Pack (M-F/F-F/M-M) | Wires for connecting GPIO pins and I2C board | Robu.in | 1 | Rs. 300 | $3.55 |
| 16 | Heavy Desktop Baseplate with Rubber Feet | Solid base so the robot stays balanced on the table | Robu.in | 1 | Rs. 400 | $4.75 |

**Total Cost in INR:** Rs. 21,400 (including taxes and domestic shipping)
**Total Cost in USD (at 1 USD = 84 INR):** ~$254.76 USD
**Remaining Buffer under $300 Grant Ceiling:** ~$45.24 USD (Rs. 3,600)
