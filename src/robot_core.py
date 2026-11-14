import datetime
from servo_controller import LibertyServos
from eye_display import RobotFace


class LibertyBot:
    def __init__(self):
        self.servos = LibertyServos()
        self.face = RobotFace()

    def handle_command(self, text):
        cleaned = text.lower().strip()

        if "handshake" in cleaned or "shake hand" in cleaned or "hath milao" in cleaned:
            self.face.set_expression("happy")
            self.servos.offer_handshake()
            self.face.set_expression("idle")
            return "Good to meet you! Let's get some work done."

        if "hello" in cleaned or "hi liberty" in cleaned:
            self.face.set_expression("happy")
            self.servos.wave_hello()
            self.face.set_expression("idle")
            return "Hey Touffeq! Ready whenever you are."

        if "time" in cleaned or "waqt" in cleaned:
            now_str = datetime.datetime.now().strftime("%I:%M %p")
            self.servos.nod_yes()
            return f"Right now it is {now_str}."

        if "look at this" in cleaned or "solve" in cleaned or "read" in cleaned:
            self.face.set_expression("thinking")
            self.servos.look_at_book()
            return "Hold your notebook steady in front of my lens so I can focus on the page."

        self.servos.nod_yes()
        return "I heard you. Let me think about that."


if __name__ == "__main__":
    bot = LibertyBot()
    print("Liberty-Bot initialized on desk.")
    while True:
        bot.face.draw_frame()
