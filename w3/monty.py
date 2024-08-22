def time_difference(time1, time2):
    s=time_to_seconds(time2)-time_to_seconds(time1)
    h=s//3600
    s%=3600
    m=s//60
    s%=60
    print(make_time_string(h,m,s))
    
    
# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)
def triangle(side1, side2, side3):
    if side1==side2 and side2==side3:
        return "Equilateral"
    if side1==side2 or side2==side3:
        return "Isosceles"
    if side1+side2<side3 and side1+side3<side2 and side2+side3<side1:
        return "Scalene"
    return "Not a triangle"