
def main():
    for time in range(1, 11):
        print("Растояние - ", format(falling_distance(time), '.2f'))

def falling_distance(time):
    g = 9.8
    distancee = 0.5 * g * (time ** 2)
    return distancee

main()