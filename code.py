type f32 = float 

user_t= float(input("Please enter your desired seconds for orbiting the earth: "))
g = 6.67 * 10**(-11)
m = 5.97 * 10**24
r = 6371000 # in meters since g useses m**3! 
PI = 3.14159265
sidereal_day = 23.98 * 3600
ninety_min_s = 90 * 60
fourtyfive_min_s = 45 * 60

def calc_formula(t: f32) -> f32: 
    h = (g*m*t**2 / (4 * PI**2)) ** (1/3) - r
    return h 

value = calc_formula(user_t)
day_value = calc_formula(sidereal_day)
ninety_value = calc_formula(ninety_min_s)
fourthy_value = calc_formula(fourtyfive_min_s)

print(f"Your altidute of your satellite is: {value} (km)")
print(f"Your altidute for once a day is {day_value} (km), for every 90min its {ninety_value} (km) and for every 45min its {fourthy_value} (km)")
