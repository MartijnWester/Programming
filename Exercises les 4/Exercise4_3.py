lengte = int(input("Wat is je lengte in cm? "))
def lang_genoeg(lengte):
    'returns lengte'
    if lengte >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein")
lang_genoeg(lengte)