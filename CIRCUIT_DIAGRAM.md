# ⚡ Circuit Wiring & Pinout Guide — Project LIBERTY-BOT

> **Safety Architecture**: The system utilizes **Dual Isolated Power Rails**.  
> The Raspberry Pi 5 runs on the official 27W USB-C supply, while the servo motors are powered separately by an external 5V 3A DC supply via the PCA9685 driver block. Both rails share a common ground (GND) to ensure stable signal references without back-feeding inductive motor noise into the Pi's sensitive SoC.

---

## 📌 GPIO & Pinout Mapping Table

### 1. PCA9685 16-Channel PWM Servo Driver (I2C Interface)
| PCA9685 Pin | Raspberry Pi 5 Pin | Header Location | Description |
|---|---|---|---|
| **VCC (Logic)** | 3.3V Power | Pin 1 | Logic power for PCA9685 chip |
| **GND** | Ground | Pin 6 | Common reference ground |
| **SDA** | GPIO 2 (SDA1) | Pin 3 | I2C Data line |
| **SCL** | GPIO 3 (SCL1) | Pin 5 | I2C Clock line |
| **V+ (Servo Power)** | External 5V 3A (+) | Terminal Block | Isolated high-current motor power rail |
| **GND (Power)** | External 5V 3A (-) | Terminal Block | Motor power ground (tied to Pi GND) |

### 2. Servo Motor Channels (PCA9685 Header Outputs)
* **Channel 0**: Head Pan Servo (Horizontal turning - Left / Right, 180° sweep)
* **Channel 1**: Head Tilt Servo (Vertical nod - Up / Down, 90° sweep)
* **Channel 2**: Left Arm Wave Servo (Gesturing & Attention, 180° sweep)
* **Channel 3**: Right Arm Handshake Servo (Extending forward for human handshake)
* **Channels 4 to 15**: Reserved for future robotic modifications (e.g., expressive eyebrows, grippers, wheels).

### 3. Camera Module 3 (MIPI CSI Interface)
* Connected via 30cm 15-to-22 pin flexible FPC cable directly to **CAM/DISP 0** port on the Raspberry Pi 5 board.
* Supports hardware autofocus via integrated Voice Coil Motor (VCM).

### 4. ReSpeaker 2-Mics Audio HAT & Speaker
* Mounts directly onto Raspberry Pi 40-pin GPIO header.
* Shares I2S audio lines (GPIO 18, 19, 20, 21) for studio-grade low-latency microphone sampling and audio amplification.
* 3W speaker plugs into the onboard JST 2.0mm speaker output port.

### 5. 3.5-inch IPS Color Display
* Interfaces via high-speed SPI / HDMI header to drive 60 FPS animated cyber eyes.

---

## 🔌 Connection Diagram Summary

```
[ External 5V 3A DC Supply ] 
           │
           ├──(+)──> PCA9685 [V+ Power Block]
           └──(-)──> PCA9685 [GND Block] ───┐ (Common GND)
                                            │
[ Raspberry Pi 5 (8GB) ] <──────────────────┘
    ├── Pin 1 (3.3V) ──────> PCA9685 VCC
    ├── Pin 3 (SDA)  ──────> PCA9685 SDA
    ├── Pin 5 (SCL)  ──────> PCA9685 SCL
    │
    ├── CAM/DISP Port ─────> 12MP Autofocus Camera Module 3
    ├── 40-Pin Header ─────> ReSpeaker 2-Mics Audio HAT ───> 3W Speaker
    └── SPI / Video ───────> 3.5" IPS Eye Display Screen
```
