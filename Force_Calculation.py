import math
import pprint



# Calculating Force on Bucket
# variables
alpha = math.radians(70)
weightOfBucket = 1000 #kN
length_a = 250 #horizontal
length_b = 30 #horizontal

# Torque on Bucket pivot at point 6
F7_y =  (weightOfBucket * length_a ) / length_b
F7 = F7_y / math.sin(alpha)

# Sum of Force y
F6_y = (weightOfBucket + F7_y)
# Sum of Force x
F7_x = math.cos(alpha) *F7 
F6_x = F7_x


##----------------------------------------------------------------##
# Calculating Forces on Linkage between Piston and bucket
# variables
beta = math.radians(20)
gamma = math.radians(20)

# Forces / tensions on joint 5
F5 = -(F7_x  + F7_y*math.cos(beta)) / (math.sin(gamma)*math.cos(beta)-math.cos(beta))
F3 = (F5 * math.cos(gamma) - F7_x) / math.cos(beta)
F3_x = F3* math.cos(beta) 
F3_y = F3*math.sin(beta)
F5_y = F5 * math.sin(gamma)
F5_x = F5 * math.cos(gamma)


##----------------------------------------------------------------##
# Calculating Force on Stick (main)
# variables
theta = math.radians(25)
theta_1 = theta + math.radians(31.7)
theta_2 = math.radians(15)
length_c = math.cos(theta)*1533 #horizontal 
length_d = math.sin(theta)*1533 #horizontal 
length_e = math.cos( math.radians(11.955 )+theta)* 331 #horizontal 
length_f = 350
length_g = 429
length_h = 1320
weight_stick = 1550 #kN

# Torque pivot at 2 (antiClockWise)
F1 = ( -F6_y * length_c  -F3_x * math.sqrt(331**2 - length_e**2)+  F3_y * length_e  -F6_x * length_d - weight_stick * math.cos(theta) * length_f + length_h*math.cos(theta) * F5_y + length_h*math.sin(theta) * F5_x) / -(length_g* (math.cos(theta_1)*math.sin(theta_2) + math.cos(theta_2)*math.sin(theta_1)))
# Sum of Force x
F2_x = (-F1 * math.cos(theta_2) + F5_x - F6_x - F3_x)
# Sum of Force y 
F2_y =  -F1 * math.sin(theta_2) + F5_y  - F6_y  + F3 * math.sin(beta) - weightOfBucket


##----------------------------------------------------------------##
# Results
pprint.pprint ( [ f'F7_x_y: {math.ceil(F7_x)}, {math.ceil(F7_y)}'
, f'F6_x_y:  {math.ceil(F6_x)}, {math.ceil(F6_y)}',
f'F5:  {math.ceil(F5)}',
f'F3:  {math.ceil(F3)}',
f"F1: {math.ceil(F1)}",
f"F2_x_y:  {math.ceil(F2_x)}, {math.ceil(F2_y)}" ])




