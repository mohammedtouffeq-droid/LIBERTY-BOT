# 📓 Engineering Build Journal — Project LIBERTY-BOT

### Author: Mohammed Touffeq (@mohammedtouffeq-droid)
### Program: Hack Club Forge Hardware Grant

---

## Entry 1: Problem Definition, Architecture & Sourcing Decisions
**Date**: November 14, 2026  
**Status**: Architecture Finalized, BOM Verified

### The Vision
I am building **LIBERTY-BOT**, an interactive, open-source tabletop AI companion designed specifically for students and makers. Most AI interfaces today are trapped inside flat browser windows or glass smartphone screens. LIBERTY-BOT brings artificial intelligence into physical desktop reality:
* It looks at study materials and math equations through a camera with mechanical autofocus.
* It answers questions hands-free using natural speech.
* It expresses emotion physically—tilting its head curiously, nodding in agreement, and extending an arm for a physical handshake when prompted.

### Key Engineering Decisions:
1. **Compute Selection**:
   * Chose **Raspberry Pi 5 (8GB)** over smaller microcontrollers (like ESP32 or Pico) because running multimodal computer vision, neural text-to-speech, and responsive conversational logic in real-time requires full Linux OS multitasking and memory headroom.
2. **Camera Choice**:
   * Upgraded to **Raspberry Pi Camera Module 3** with autofocus. Standard fixed-focus cameras cannot focus on small printed textbook text at 15–20 cm desktop distances.
3. **Kinematics & Motor Safety**:
   * Using **MG90S metal-gear servos** instead of cheap plastic-gear servos to prevent gear stripping over long hours of movement.
   * Isolated the motor power supply using an external 5V 3A supply paired with an I2C-controlled **PCA9685 PWM driver board**. This prevents inductive current spikes from resetting the Raspberry Pi 5.
4. **Domestic Fulfillment Strategy**:
   * Sourcing the components from authorized Indian distributors (**Robu.in / Silverline Electronics**) instead of importing from overseas. This keeps delivery fast (3–4 business days), avoids courier brokerage overheads, and guarantees zero customs friction.

---

## Next Milestones:
* [x] Finalize Bill of Materials & Vendor Mapping
* [x] Design Pinout & Power Isolation Schematic
* [ ] Submit Project Proposal in Hack Club `#forge`
* [ ] Receive Component Package
* [ ] Baseplate & Bracket Mounting (Assisted by Father)
* [ ] Initial Power-on Self Test (POST) & GPIO Wiring
* [ ] Flash Raspberry Pi OS & Configure I2C / CSI Interfaces
* [ ] Deploy Core Conversational & Vision Stack (`jarvis_core` port)
