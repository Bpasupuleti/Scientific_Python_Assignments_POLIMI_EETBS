import os
os.chdir("C:\Users\KRISHNA\Desktop\canopy\Assign_4") 
import Wallcalculations_balaji as FC
#Calculation for Wall

print "Stud layer"
stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]
Rtot_stud = FC.wallCalc_withParallel(stud_layer)

Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud
print "The total heat transfer coefficient on stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"

ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]
Rtot_ins = FC.wallCalc_withParallel(ins_layer)
    
Uins = 1/Rtot_ins["R total"]
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation is " + str(Uins) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"

Uwall = Ustud_tot + Uins_tot
print "Thus, the overall heat transfer coefficient of the wall is " + str(Uwall) + " (W/m^2 deg C)"

#Calculation for Door and Ceiling
door_layer = ["wood_50mm"]
Rtot_door = FC.wallCalc_withSeries(door_layer)
Udoor = 1/Rtot_door["R total"]
print "The total heat transfer coefficient on Door is " + str(Udoor) + " (W/m^2 deg C)"

ceiling_layer = ["Asphalt_Shingle_Roofing","wood_100mm","Acoustic_Tile","ConcreteBlockLightWeight_439mm"]  
Rtot_ceiling = FC.wallCalc_withSeries(ceiling_layer)

Uceiling = 1/Rtot_ceiling["R total"]
print "The total heat transfer coefficient on Ceiling is " + str(Uceiling) + " (W/m^2 deg C)"

Tht = -4.8
Tint = 20

DT = Tint-Tht

HF_wall = Uwall*DT
HF_door = Udoor*DT
HF_Ceiling = Uceiling*DT

print "Heat factor for Wall is " + str(HF_wall) + " (W/m^2)"
print "Heat factor for Door is " + str(HF_door) + " (W/m^2)"
print "Heat factor for Ceiling is " + str(HF_Ceiling) + " (W/m^2)"

A_wall = 105.8
A_door = 2.2
A_Ceiling = 200

Qwall = HF_wall*A_wall
Qdoor = HF_door*A_door
QCeiling = HF_Ceiling*A_Ceiling

print "Heating load for Wall is " + str(Qwall) + " W"
print "Heating load for Door is " + str(Qdoor) + " W"
print "Heating load for Ceiling is " + str(QCeiling) + " W"

Qtotal = Qwall+Qdoor+QCeiling
Qtotal_kW = Qtotal/1000
print "Thus, the total heating load for opaque surface (wall, door, and ceiling) is " + str(Qtotal_kW) + " kW"
