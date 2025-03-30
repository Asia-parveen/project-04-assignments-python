print("This is planetary_weight_calculator.py")


MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0  

def main():

    earth_weight = float(input("Enter any weight on Earth : "))
    planet = input("Enter your choise planet: ")


    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:  
        gravity_constant = NEPTUNE_GRAVITY

    planetary_weight = round(earth_weight * gravity_constant, 2)

    
    print("The equivalent weight on", planet + ":", planetary_weight)

if __name__ == "__main__":
    main()

