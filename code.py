from vpython import *
type f32 = float 

user_t= float(input("Please enter your desired seconds for orbiting the earth: "))
g = 6.67 * 10**(-11)
m = 5.97 * 10**24
r = 6371000 # in meters since g useses m**3! 
PI = 3.14159265
sidereal_day = 23.98 * 3600
ninety_min_s = 90 * 60
fourtyfive_min_s = 45 * 60
r_earth = 6371000.0  # in meters

def calc_formula(t: f32) -> f32: 
    h = (g*m*t**2 / (4 * PI**2)) ** (1/3) - r
    return h 

value = calc_formula(user_t)
day_value = calc_formula(sidereal_day)
ninety_value = calc_formula(ninety_min_s)
fourthy_value = calc_formula(fourtyfive_min_s)

print(f"Your altidute of your satellite is: {value} (km)")
print(f"Your altidute for once a day is {day_value} (km), for every 90min its {ninety_value} (km) and for every 45min its {fourthy_value} (km)")


def calc_altitude(t: f32) -> f32: # not in kilometers, since VPython uses meters
    r_orbit = (g * m * t**2 / (4 * PI**2)) ** (1/3)
    h = r_orbit - r_earth
    return h

t = float(input("Please enter your desired seconds for orbiting (visualisation): "))

altitude = calc_altitude(t)
r_orbit = r_earth + altitude

print(f"Altitude: {altitude/1000:.1f} km")
print(f"Orbit radius: {r_orbit/1000:.1f} km")
print(f"Orbit period: {t:.1f} s")

scale = 1 / 1_000_000
scene.title = "Satellite Orbit Simulation"
scene.width = 900
scene.height = 600
scene.background = color.black

earth = sphere(pos=vector(0, 0, 0), radius=r_earth * scale, texture=textures.earth)
orbit_radius_scaled = r_orbit * scale
satellite = sphere(pos=vector(orbit_radius_scaled, 0, 0), radius=earth.radius * 0.08, color=color.orange, make_trail=True, trail_type="points", interval=5, retain=200)
label(pos=vector(0, -earth.radius * 1.4, 0), text=f"h = {altitude/1000:.0f} km ; t = {t:.0f} s", box=False, height=14, color=color.white)
angle = 0
omega = 2 * PI / t
dt = t / 500
speed_factor = 500 

while True:
    rate(60)
    angle += omega * dt * speed_factor
    satellite.pos = vector(orbit_radius_scaled * cos(angle), orbit_radius_scaled * sin(angle), 0)
