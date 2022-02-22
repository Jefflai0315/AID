import math
import pprint

# Force on Bucket
alpha = math.radians(60)
weightOfBucket = 2000 #kN
length_a = 200 #horizontal
length_b = 100 #horizontal



# Torque on Bucket pivot at pinMain
# length_a * weightOfBucket + length_b * pin1_y = 0
pin1_y =  (weightOfBucket * length_a ) / length_b
pin1 = pin1_y / math.sin(alpha)

# Sum of Force y
# pin1_y + pinMain_y - weightOfBucket = 0
pinMain_y = -(weightOfBucket - pin1_y)

# Sum of Force x
# pin1_x - pinMain_x = 0
pin1_x = math.cos(alpha) *pin1 # making force variable possible 
pinMain_x = pin1_x

# Force on Linkage between Piston and bucket

beta = math.radians(20)
gamma = math.radians(20)

# Sum of Force x & y
# Force_L_x - Force_piston_x - pin1_x = 0
# Force_L_y - Force_piston_y - pin1_y = 0

Force_L  = (pin1_x + (pin1_y * math.sin(gamma) * math.cos(beta) ) ) / (math.cos(alpha) + math.sin(gamma)**2 * math.cos(beta))
Force_piston = (Force_L * math.cos(gamma) - pin1_x) / math.cos(beta)

# Force on Stick (main)
theta = math.radians(20)
length_c = math.sqrt( 1500**2 / (1+ (math.tan(theta))**2)) #horizontal 
length_d = math.tan(theta) * length_c #horizontal 
length_e = 200 #horizontal 
length_f = 500
length_g = 450
length_h = 1300
weight_stick = 3000 #kN
# Sum of Force x & y
# pinMain_x  - Force_piston_x - pinArm_x + Force_pistonArm_x + Force_L_x = 0
# -pinMain_y + Force_piston_y -pinArm_y + Force_pistonArm_y - Force_L_y = 0 

# Torque of arm (antiClockWise)
# pinMain_x * length c + Force_piston_y * length_e - pinMain_y * length_d - weight_stick * cos(delta) * length_f - length_g * Force_pistonArm - length_h * Force_L_y= 0
Force_pistonArm = ( pinMain_x * length_c + Force_piston* math.sin(beta) * length_e + pinMain_y * length_d - weight_stick * math.cos(theta) * length_f - length_h * Force_L * math.sin(gamma)) / length_g

pinArm_x = Force_pistonArm * math.sin(theta) + Force_L * math.cos(gamma) - pinMain_x + Force_piston * math.cos(40)
pinArm_y =  -(Force_pistonArm * math.cos(theta) - Force_L * math.cos(gamma)  + pinMain_y  - Force_piston * math.cos(40))



pprint.pprint ( [ f'pin1_x_y:, {math.ceil(pin1_x)}, {math.ceil(pin1_y)}'
, f'pinMain_x_y: , {math.ceil(pinMain_x)}, {math.ceil(pinMain_y)}',
f'Force_L:  {math.ceil(Force_L)}',
f'Force_piston:  {math.ceil(Force_piston)}',
f"Force_pistonArm: {math.ceil(Force_pistonArm)}",
f"pinArm_x_y:  {math.ceil(pinArm_x)}, {math.ceil(pinArm_y)}" ])




