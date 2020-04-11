from numpy import linspace

a = linspace(1, 100, 3)
print(a)
# 100 is included
# icnrement is (last_term - first_term)/(numEl-1)
# returns an array containing terms b/w 1, 100
# now lets write our linspace function











def linspace_v2(start, end, noEl):
    incr = (end-start)/(noEl-1)
    val = start
    res = []
    while val <= end:
        res.append(val)
        val += incr
    return res