time = [0, 20, 40, 60, 80, 100]
temp = [28.0, 48.6, 61.6, 71.2, 74.8, 75.2]

#for the a specific time (other than the ones given in matrix)
# compute temprature value by using LIENAR INTERPOLATION
# Formula for linear interpolation
# y = y_1 + (y_2 - y_1)/(x_2 - x_1) * (x - x_1)
# here x and y are time and related temprature values, respectively
# subscript 1 and 2 designates the points before and after the point we are asked to find temprature
# ex. if time is 65 then x1 = 60, x2 = 100, y1 =71.2 and y2 = 74.8

x = 50
#y = ?
#x1 = 40
#x2 = 60
#y1 = 61.6
#y2 = 71.2

c = len(time)
if x < max(time) and x > min(time):
    for i in range(c):
        if time[i] > x:
            x1 = time[i-1]
            x2 = time[i]
            y1 = temp[i-1]
            y2 = temp[i]
            break 
    y = y1 + (y2 - y1)/(x2 - x1) * (x - x1)     
    print('Value at x = ', x, ' is ', y)
else :
    print('Not a valid time value.')


