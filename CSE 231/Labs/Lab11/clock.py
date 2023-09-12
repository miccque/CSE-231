class Time(object):
    ''' Given hours, minutes, or seconds displays a clock time '''
    def __init__(self, hours = 0, minutes = 0, seconds = 0):        
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds//60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes//60)) % 24
    def __repr__(self):
        ''' Returns Class Time: hh:mm:ss as a string'''
        return ("Class Time: {:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds))
    def __str__(self):
        ''' Returns hh:mm:ss as a string '''
        return "{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds)
    def from_str(self, time_str):
        '''Given a string of time converts to time'''
        val_list = time_str.split(':')
        self.hours = int(val_list[0])
        self.minutes = int(val_list[1])
            self.seconds = int(val_list[2])