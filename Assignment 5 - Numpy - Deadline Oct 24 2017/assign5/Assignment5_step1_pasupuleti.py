import numpy as np


Resistance_names = np.array(["R1","R2","Rf","Rp1","Rp2","Rc1","Rc2","Rb"])
Resistance_types = np.array(["conv","conv","cond","cond","cond","cond","cond","cond"])
Resistance_h = np.array([10,25,None,None,None,None,None,None])
Resistance_k = np.array([None,None,0.026,0.22,0.22,0.22,0.22,0.72])
Resistance_L = np.array([None,None,0.03,0.02,0.02,0.16,0.16,0.16])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.25,0.015,0.015,0.22])
Resistances_RValues = np.array(np.zeros(8))
Resistances_RValues[Resistance_types=="cond"] = Resistance_L[Resistance_types=="cond"]/ (Resistance_k[Resistance_types=="cond"]
                                                *resistances_A[Resistance_types=="cond"])
Resistances_RValues[Resistance_types=="conv"] = 1.0 / (Resistance_h[Resistance_types=="conv"]
                                                    *resistances_A[Resistance_types=="conv"])

#series layers ["R1","Rf","Rp1","Rp2","R2"]
RLayers_series = ["R1","R2","Rf","Rp1","Rp2"]
RValues_series = Resistances_RValues[0:5]
Rtot_Series = RValues_series.sum()

#Parallel
RLayers_parallel = ["Rc1","Rc2","Rb"]
RValues_parallel =  1/Resistances_RValues[5:]
Rtot_parallel =1/ RValues_parallel.sum() 

#Total resistance
R_tot = round(Rtot_Series+Rtot_parallel,4)

Tin = 20  
Tout = -10 
A = 0.25 
Awall = 15 

#Heat transfer
Q_unit = (Tin - Tout) / R_tot 

Q_wall = round((Q_unit * (Awall/A))) 

print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The rate of heat transfer through the wall is '+str(Q_wall)+ ' W'