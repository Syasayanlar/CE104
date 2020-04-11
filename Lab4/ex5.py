# Assume that one has the data in the following form
# dt = [years, days, hours, minutes, second]
# such as dt = [1, 1, 0, 0, 20] means that 1 year 1 day and 20 seconds
# also it is assumed that second or minute is less than 60 etc. 
# then write a function to compute how much seconds is the given dt value
# for example dt = [1, 1, 0, 0, 20] means that 1 year 1 day and 20 seconds is 31622420 seconds












def convert2seconds(dt):
    y = dt[0]
    d = dt[1]
    h = dt[2]
    m = dt[3]
    s = dt[4]
    sConst = 1
    mConst = sConst * 60
    hConst = mConst * 60
    dConst = hConst * 24
    yConst = dConst * 365
    
    totalSeconds = y*yConst + d*dConst + h*hConst + m*mConst\
                    + s*sConst
    return totalSeconds