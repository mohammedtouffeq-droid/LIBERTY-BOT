import time

try:
    import board
    import busio
    from adafruit_pca9685 import PCA9685
    from adafruit_motor import servo
    HARDWARE_CONNECTED = True
except ImportError:
    HARDWARE_CONNECTED = False


class LibertyServos:
    def __init__(self):
        self.neck_pan_ch = 0
        self.neck_tilt_ch = 1
        self.left_arm_ch = 2
        self.right_arm_ch = 3

        self.current_angles = {
            0: 90,
            1: 90,
            2: 20,
            3: 20
        }

        if HARDWARE_CONNECTED:
            i2c = busio.I2C(board.SCL, board.SDA)
            self.pca = PCA9685(i2c)
            self.pca.frequency = 50
            self.motors = {
                0: servo.Servo(self.pca.channels[0], min_pulse=500, max_pulse=2500),
                1: servo.Servo(self.pca.channels[1], min_pulse=500, max_pulse=2500),
                2: servo.Servo(self.pca.channels[2], min_pulse=500, max_pulse=2500),
                3: servo.Servo(self.pca.channels[3], min_pulse=500, max_pulse=2500),
            }
            self.reset_posture()
        else:
            self.pca = None
            self.motors = {}

    def move_smooth(self, channel, target_angle, step_delay=0.015):
        target_angle = max(10, min(170, int(target_angle)))
        start_angle = self.current_angles.get(channel, 90)
        if start_angle == target_angle:
            return

        step = 2 if target_angle > start_angle else -2
        for angle in range(start_angle, target_angle, step):
            if HARDWARE_CONNECTED and channel in self.motors:
                self.motors[channel].angle = angle
            time.sleep(step_delay)

        if HARDWARE_CONNECTED and channel in self.motors:
            self.motors[channel].angle = target_angle
        self.current_angles[channel] = target_angle

    def reset_posture(self):
        self.move_smooth(self.neck_pan_ch, 90)
        self.move_smooth(self.neck_tilt_ch, 90)
        self.move_smooth(self.left_arm_ch, 20)
        self.move_smooth(self.right_arm_ch, 20)

    def nod_yes(self):
        for _ in range(2):
            self.move_smooth(self.neck_tilt_ch, 65, 0.01)
            self.move_smooth(self.neck_tilt_ch, 110, 0.01)
        self.move_smooth(self.neck_tilt_ch, 90, 0.01)

    def shake_no(self):
        for _ in range(2):
            self.move_smooth(self.neck_pan_ch, 60, 0.01)
            self.move_smooth(self.neck_pan_ch, 120, 0.01)
        self.move_smooth(self.neck_pan_ch, 90, 0.01)

    def offer_handshake(self):
        self.move_smooth(self.neck_tilt_ch, 80, 0.015)
        self.move_smooth(self.right_arm_ch, 115, 0.015)
        time.sleep(0.4)
        for _ in range(3):
            self.move_smooth(self.right_arm_ch, 95, 0.012)
            self.move_smooth(self.right_arm_ch, 120, 0.012)
        time.sleep(0.5)
        self.move_smooth(self.right_arm_ch, 20, 0.02)
        self.move_smooth(self.neck_tilt_ch, 90, 0.015)

    def wave_hello(self):
        self.move_smooth(self.left_arm_ch, 140, 0.015)
        for _ in range(3):
            self.move_smooth(self.left_arm_ch, 110, 0.01)
            self.move_smooth(self.left_arm_ch, 150, 0.01)
        self.move_smooth(self.left_arm_ch, 20, 0.02)

    def look_at_book(self):
        self.move_smooth(self.neck_pan_ch, 90, 0.015)
        self.move_smooth(self.neck_tilt_ch, 125, 0.02)
