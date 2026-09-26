type f32 = float 
"""
-> this is the previous version that I wrote without thinking about function parameters. Also the calculation is wrong, I'm using this example to show my students how NOT to do this 
"""
t = float(input("Please enter your desired seconds for orbiting the earth: "))
g = 6.67 * 10**(-11)
m = 5.97 * 10**24
r = 6371000 # in meters since g useses m**3! 
PI = 3.14159265
sidereal_day = 23.98

def calc_formula() -> f32: 
    h = (g*m*t**2 / 4 * PI**2) ** 1/3 - r
    return h 

def day_geo_func() -> f32:
    geo_day= calc_formula() * sidereal_day
    return geo_day

def ninety_func() -> f32:
    ninety = calc_formula() / sidereal_day * 90
    return ninety

def fourthyfivemin_func() -> f32:
    fourthyfivemin = calc_formula() / sidereal_day * 45
    return fourthyfivemin 

value = calc_formula()
day_value = day_geo_func()
ninety_value = ninety_func()
fourthy_value = fourthyfivemin_func()

print(f"Your altidute of your satellite is: {value} (km)")
print(f"Your altidute for once a day is {day_value} (km), for every 90min its {ninety_value} (km) and for every 45min its {fourthy_value} (km)")
