import datetime

from helpers.check import Check

class Time:
    def time_since_epoch() -> int:
        now = datetime.datetime.now(); jan_6_2023 = datetime.datetime(2023, 1, 6)
        
        time_diff_seconds = (now - jan_6_2023).total_seconds()
        time_diff_ms = int(time_diff_seconds * 1000)
        
        if Check.check41Bit(time_diff_ms) == True:
            return time_diff_ms
        else:
            return 0
        