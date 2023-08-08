from time import sleep


class Pymodoro:
    def __init__(
        self,
        pomodoros: int = 1,
        pomodoro_time: int = 25,
        short_break_time: int = 5,
        long_break_time: int = 15,
    ) -> None:
        self.pomodoros = pomodoros
        self.pomodoro_time = pomodoro_time
        self.short_break_time = short_break_time
        self.long_break_time = long_break_time

        self.short_breaks = 0
        self.has_rested = True
        self.pomodoros_done = 0

        self.run()

    def start_pomodoro(self) -> None:
        self.pomodoros_done += 1
        sleep(self.pomodoro_time * 60)
        self.has_rested = False

    def start_short_break(self) -> None:
        sleep(self.short_break_time * 60)
        self.short_breaks += 1
        self.has_rested = True

    def start_long_break(self) -> None:
        self.short_breaks = 0
        sleep(self.long_break_time * 60)
        self.has_rested = True

    def run(self) -> None:
        while self.pomodoros != self.pomodoros_done:
            if self.has_rested:
                self.start_pomodoro()
            elif self.short_breaks != 3:
                self.start_short_break()
            else:
                self.start_long_break()
