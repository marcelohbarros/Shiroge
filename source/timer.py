import time

# Keeps track on last synced time
class Timer:
    def __init__(self):
        self.timer = time.time_ns()

    def count(self):
        last_time = self.timer
        current_time = time.time_ns()
        self.timer = current_time
        return (current_time - last_time) / 10**9
