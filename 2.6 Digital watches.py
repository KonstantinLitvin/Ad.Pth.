__author__ = 'KonstantinLitvin'

N = int(input())

numberOfMinutes, seconds = divmod(N, 60)
numberOfHours, minutes = divmod(numberOfMinutes, 60)
numberOfDays, hours = divmod(numberOfHours, 24)

print("%d:%02d:%02d" % (hours, minutes, seconds))
