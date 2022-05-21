ships = [["N2 Bomber", "Heavy Fighter", "Limited", 21], 
         ["J-Type 327", "Light Combat", "Unlimited", 1], 
         ["NX Cruiser", "Medium Fighter", "Limited", 18], 
         ["N1 Starfighter", "Medium Fighter", "Unlimited", 25], 
         ["Royal Cruiser", "Light Combat", "Limited", 4]]

print("{:<14} {:<14} {:<10} {:<9}".format('SHIP NAME', 'CLASS', 'DEPLOYMENT', 'IN SERVICE'))

for row in ships:
    SHIP_NAME, CLASS, DEPLOYMENT, IN_SERVICE = row
    print("{:<14} {:<14} {:<10} {:<9}".format(SHIP_NAME, CLASS, DEPLOYMENT, IN_SERVICE))