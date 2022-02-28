import math 
import pprint


# 1. Calculation for forces on bucket
# Variables 
Fgb = 150                            #weight of bucket
lgb = 200                             #horizontal length from pin6 to CG of bucket
l7 = 100                              #horizontal length from pin6 to pin7
beta7 = math.radians(60)

# Expressions
F7 = Fgb * lgb /l7                    #force on pin7
F7y = F7 * math.cos(beta7)            #verticle vector of F7
F7x = F7 * math.sin(beta7)            #horizontal vector of F7
F6y = F7 + Fgb                        #verticle vector of F6
F6x = F7x                             #horizontal vector of F6




# 2. Calculation for forces on each pin on the dipper arm
# Variables
Fga = 300                             #weight of dipper arm
beta1 = math.radians(20)
beta3 = math.radians(35)
beta4 = math.radians(70)
beta4a = math.radians(20)
beta5 = math.radians(40)
l1 = 429
l3 = 331
l5 = 1320
l6x = 1533 * math.cos(math.radians(beta3 +10))
l6y = 1533 * math.sin(math.radians(beta3 +10))
lga = 350 * math.cos(math.radians(beta3 +10))

# Expressions
F5 = F7 * math.cos(beta4)   
F3 = F7 * math.cos(beta4a)  
F5y = F5 * math.sin(beta5)
F5x = F5 * math.cos(beta5)
F3y = F3 * math.sin(beta3)
F3x = F3 * math.cos(beta3)
F1 = -(F6y * l6x + Fga * lga - F6x * l6y - F5 * l5 - F3 * l3) / l1
F1x = F1 * math.cos(beta1)
F1y = F1 * math.sin(beta1)
F2x = F5x + F6x - F3x + F1x
F2y = F1y + F3y  +F5y - Fga - F6y


##-----------------------------Results-----------------------------------##
pprint.pprint ( [ f'F7x & F7y: {math.ceil(F7x)}, {math.ceil(F7y)}'
, f'F6x & F6y:  {math.ceil(F6x)}, {math.ceil(F6y)}',
f'F5:  {math.ceil(F5)}',
f'F3:  {math.ceil(F3)}',
f"F1: {math.ceil(F1)}",
f"F2x & F2y:  {math.ceil(F2x)}, {math.ceil(F2y)}" ])
