import math
import pprint

# Force on Bucket
alpha = math.radians(60)
weightOfBucket = 2000 #kN
length_a = 200 #horizontal
length_b = 100 #horizontal



# Torque on Bucket pivot at F6
# length_a * weightOfBucket + length_b * F7_y = 0
F7_y =  (weightOfBucket * length_a ) / length_b
F7 = F7_y / math.sin(alpha)

# Sum of Force y
# F7_y + F6_y - weightOfBucket = 0
F6_y = -(weightOfBucket - F7_y)

# Sum of Force x
# F7_x - F6_x = 0
F7_x = math.cos(alpha) *F7 # making force variable possible 
F6_x = F7_x

# Force on Linkage between Piston and bucket

beta = math.radians(20)
gamma = math.radians(20)

# Sum of Force x & y
# F5_x - F3_x - F7_x = 0
# F5_y - F3_y - F7_y = 0

F5  = (( (F7_y * math.cos(beta)) + F7_x * math.sin(beta) )  / ((math.sin(beta)) + math.sin(gamma) * math.cos(beta)))/math.cos(gamma)
F3 = (F5 * math.cos(gamma) - F7_x) / math.cos(beta)

# Force on Stick (main)
theta = math.radians(20)
theta_1 = theta + math.radians(20)
theta_2 = math.radians(10)
length_c = math.sqrt( 1500**2 / (1+ (math.tan(theta))**2)) #horizontal 
length_d = math.tan(theta) * length_c #horizontal 
length_e = 200 #horizontal 
length_f = 500
length_g = 450
length_h = 1300
weight_stick = 3000 #kN
# Sum of Force x & y
# F6_x  - F3_x - F2_x - F1_x - F5_x = 0
# F6_y + F3_y -F2_y - F1_y - F5_y = 0 

# Torque of arm (antiClockWise)
# -F6_y * length c + F3_y * length_e + F6_x * length_d - weight_stick * cos(delta) * length_f - length_g * cos(theta_1) * F1_y - length_g * sin(theta_1) * F1_x- length_h*cos(theta) * F5_y -length_h*sin(theta) * F5_x= 0
F1 = ( F6_y * length_c + F3* math.sin(beta) * length_e + F6_x * length_d - weight_stick * math.cos(theta) * length_f - length_h*math.cos(theta) * F5 * math.sin(gamma)- length_h*math.sin(theta) * F5 * math.cos(gamma)) / (length_g* (math.cos(theta_1)*math.sin(theta_2) + math.cos(theta_2)*math.sin(theta_1)))
F1 = -F1
F2_x = -F1 * math.cos(theta_2) - F5 * math.cos(gamma) + F6_x - F3 * math.cos(beta)
F2_y =  -F1 * math.sin(theta_2) - F5 * math.sin(gamma)  + F6_y  + F3 * math.sin(beta)
F2_x , F2_y = -(F2_x) , -(F2_y)


pprint.pprint ( [ f'F7_x_y:, {math.ceil(F7_x)}, {math.ceil(F7_y)}'
, f'F6_x_y: , {math.ceil(F6_x)}, {math.ceil(F6_y)}',
f'F5:  {math.ceil(F5)}',
f'F3:  {math.ceil(F3)}',
f"F1: {math.ceil(F1)}",
f"F2_x_y:  {math.ceil(F2_x)}, {math.ceil(F2_y)}" ])




