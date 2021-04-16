def main_5_14():
    mass = float(input('mass = '))
    speed = float(input('speed = '))

    print('enegy = ', format(kinetic_enegy(mass, speed), '.2f'))

def kinetic_enegy(mass, speed):
    energy = 0.5 * mass * (speed ** 2)
    return energy
main_5_14()