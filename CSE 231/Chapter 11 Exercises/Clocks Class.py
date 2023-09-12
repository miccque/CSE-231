class Clock(object):
    def __init__(self, hours = 0, minutes = 0, seconds = 0):        
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds//60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes//60)) %24
    def print_clock(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds))
    def add_clocks(self, clock2):
        seconds = self.seconds + clock2.seconds
        minutes = self.minutes + clock2.minutes
        hours = self.hours + clock2.hours
        return Clock(hours, minutes, seconds)
    
my_clock = Clock(10,5,5)
my_clock.print_clock()
my_clock2 = Clock(3,8)
my_clock2.print_clock()
my_clock3 = my_clock.add_clocks(my_clock2)
my_clock3.print_clock()
