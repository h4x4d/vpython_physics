from objects.earth import Earth


def render_logs(rocket, ticks):
    return  (f"ROCKET LAUNCH | STATUS: {rocket.status.name}\n",
             f"ROCKET INFO:"
             f"MASS: {rocket.mass} = {rocket.MASS} + {rocket.fuel_mass}\n"
             f"POS: {rocket.pos} (HEIGHT: {((rocket.pos).mag - Earth.RADIUS) / 1000}) \n"
             f"SPEED: {rocket.speed.mag} = {rocket.speed}\n"
             f"ACCELERATION: {rocket.acceleration}\n"
             f"STATUS: {rocket.status.name}\n"
             f"TIME: {ticks}")