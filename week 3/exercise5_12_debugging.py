import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power
decibels = 10 * math.log10(ratio)
print(decibels)

"""When this program is run it gives an error stating that their is error
in line 5 but the error is actually in line 4 because the result of the 
floor division (\\) is zero.
This is to say always ceck te error very well don't always assume te 
error message is correct"""