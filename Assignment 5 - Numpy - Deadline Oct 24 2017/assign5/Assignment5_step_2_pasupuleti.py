
import numpy as np

materials_names= np.array(["OutsideSurface_Summer", "OutsideSurface_Winter","InsideSurface","InsulationFiberGlass_90mm",
"WoodStud_90mm","WoodFiberboard", "Stucco_25mm", "WoodBevel_13x200","Gypsum_13mm"]) 

materials_Rvalues =np.array([0.044,0.030,0.12,2.45,0.63,0.23,0.037,0.14,2.52])

layerin_Stud = np.array(["OutsideSurface_Winter", "InsideSurface","WoodFiberboard","WoodBevel_13x200",
"WoodStud_90mm","Gypsum_13mm"])
RValue_myStud = np.zeros(layerin_Stud.size)

for layerName in layerin_Stud:
    RValue_myStud[layerin_Stud==layerName] = materials_Rvalues[materials_names==layerName]

Rtot_stud = RValue_myStud.sum()
U_of_Stud = 1/(Rtot_stud)

print "The total Resistance of stud is "+str(Rtot_stud) +" degC/W" 
print "The overall heat transfer coefficient for the stud wall "+str(U_of_Stud)+ " W/m^2 deg"

#For The Glass Fiber:
layerin_Fiber = np.array(["OutsideSurface_Winter", "InsideSurface","WoodBevel_13x200","WoodFiberboard",
                            "InsulationFiberGlass_90mm","Gypsum_13mm"]) # List containing layers in series 
RValue_myFiber = np.zeros(layerin_Fiber.size)

for layerName in layerin_Fiber:
    RValue_myFiber[layerin_Fiber==layerName] = materials_Rvalues[materials_names==layerName]

Rtot_Fiber = RValue_myFiber.sum()
U_of_Fiber = 1/(Rtot_Fiber)
print "The overall heat transfer coefficient for the wall with Fiber is "+str(U_of_Fiber)+ " W/m^2 degC"

A_Stud = 0.25
A_GlassFiber = 0.75
U_total = (A_GlassFiber)*(U_of_Fiber) + (A_Stud)*(U_of_Stud)
R_Total = 1/U_total 
print "The Total Resistance of the wall is "+str(R_Total)+" degC/W"
print "The Overall heat transfer coefficient,U is " +str(U_total)+ " W/degC"

Tin = 22
Tout = -2 
Q =U_total*(Tin - Tout)

Area_wall = 0.8*50*2.5
Qtot = Area_wall*Q
print "Total Heat Loss throught the buliding is "+str(Qtot)+" W"