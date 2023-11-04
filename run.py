#############################################
#
# Run
# (Sample code for CIS 500 at GVSU)
#
# Assumptions:
#   Runs begin and end on the same day 
#   (i.e., don't extend past midnight)
#
# Instance variables
#   start, end (in minutes past midnight) 
#   distance
#
# Instance methods
#   elapsed_minutes
#   elapsed_time (formatted as hours:minutes)
#   raw_pace 
#   pace (formatted in minutes:seconds)
#   __str__
#
############################################################

class Run:

    unit = "km"

    def __init__(self, distance, start_time, end_time):
        self.distance = float(distance)
        self.raw_start = Run._time_to_minutes(start_time)
        self.raw_end = Run._time_to_minutes(end_time)

    def _time_to_minutes(time):
        hours, minutes = [int(i) for i in time.split(':')]
        return hours*60 + minutes

    def elapsed_minutes(self):
        return self.raw_end - self.raw_start

    def elapsed_time(self):
        minutes = self.elapsed_minutes() % 60
        hours = self.elapsed_minutes() // 60
        return f"{hours}:{minutes:02d}"
    
    def raw_pace(self):
        return self.elapsed_minutes() / self.distance

    def pace(self):
        minutes = int(self.raw_pace())
        seconds = int((self.raw_pace() - minutes)*60)
        return f"{minutes}:{seconds:02d}/{Run.unit}"

    def __str__(self):
        return f"{self.distance} {Run.unit}s in {self.elapsed_time()}. Pace: {self.pace()}."


# Run.units = "mile"
# r = Run("8:15", "9:05", 6.12)
# print(r)