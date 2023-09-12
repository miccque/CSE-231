class Time(object):

    def __init__(self,hours=0,mins=0,secs=0):
        self.__hours = hours
        self.__mins = mins
        self.__secs = secs

    def __repr__(self):
        output = "Class Time : {:02d}:{:02d}:{:02d} ".format(self.__hours,self.__mins,self.__secs)
        return output

    def __str__(self):
        output = "{:02d}:{:02d}:{:02d} ".format(self.__hours,self.__mins,self.__secs)
        return output

    def from_str(self,clocktime):
        timeslice = clocktime.split(':')
        self.__hours = int(timeslice[0])
        self.__mins = int(timeslice[1])
        self.__secs = int(timeslice[2])




A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )