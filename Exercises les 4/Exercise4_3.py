def lang_genoeg(lengte):
    'returns lengte'
    lengte = input("Wat is je lengte in cm? ")
    if lengte >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein")
    return lengte
