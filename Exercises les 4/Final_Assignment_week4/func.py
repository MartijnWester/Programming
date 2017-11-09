def standaardprijs(afstandKM):
    if afstandKM > 0:
        if afstandKM > 50:
            return 15 + afstandKM*0.6
        else: return afstandKM*0.8
    else: return 0

def ritprijs(leeftijd, weekendrit, afstandKM):
    stnd = standaardprijs(afstandKM)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            return (stnd * 0.65)
        else: return (stnd * 0.6)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return (stnd * 0.6)
        else: return stnd