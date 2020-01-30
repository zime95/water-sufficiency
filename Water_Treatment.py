#!/usr/bin/env python
# coding: utf-8

# # Predicting advance waste water treatment methods

# In[17]:


#Assumptions :Primary Treatment has been performed
#Inputs Parameters
print("Please note that these conceptual ideas are based on lab scale experiments")

""" Colour
    Conductivity
    COD
    Odour/Sulphide
    TDS
    pH
"""
#Proposed Advanced Methods
"""Crosflow filtration using reverse osmosis
    Photocatalytic degradation using titanium dioxide in the presence of UV light
    Oxidation of sulhide using hydrogen peroxide
"""

sans_secondary = {"colour": 100, "COD": 5000, "pH_low": 5, "pH_high": 12, "turbidity_high":10}

ltr = float(input("Please input the volume of water to be tested "))
colour = float(input("Please input the colour value in Pt/Co "))
conductivity = float(input("Please input the conductivity value in Microsiemens "))
COD = float(input("Please input the COD value in mg/L "))
Odour = input("Please input F for a foul smell or N for nomal smell ")
TDS = float(input("Please input TDS value in mg/L "))
ph_value = float(input("Please input pH value "))
turbidity = float(input("Please input turbidity value in NTU "))
"""
if turbidity < 0:
    print("Turbidity must be greater than 0", float(input(turbidity)))
"""

colour_in = colour
coagulation_dosage = 1
colour_increment = 0
hydraulic_retention_time = 30 
mixing_rate = 100
ph_value_increment = 0
ph_value_input = ph_value
n_ph_value = ph_value
pH_low = 0.1 
pH_high = 0.1
chemical_vol = 50
H2O2 = 0
turbidity_int = turbidity
settling_time = 30
N_COD = 0

print()
print("The expected results after the secodary treatment are as follows:")
print()                
while colour > sans_secondary["colour"]:
    
    coagulant= coagulation_dosage + coagulation_dosage*0.05
    colour = colour- colour*0.5
    N_colour = colour
    colour_increment +=1
    
print("The colour of the water was:", colour_in,"Pt.Co")
print()
print("After treatment, the colour if the water is:", N_colour, "Pt.Co")  
print()
print("The number of cycles colour treatment went through is:" ,colour_increment )
print()
                     

while COD > sans_secondary["COD"]:
    
        hydraulic_retention_time += 0.1
        N_COD = COD -COD*0.25
        COD = N_COD
       
print("The hydraulic retention time is:",hydraulic_retention_time, "minutes")
print()
print("The COD of the water was:", COD, "mg/L")
print()
print("After treatment, the COD is:", N_COD, "mg/L")  
print()

if Odour == "F":
    H202 = ltr*0.01
    print("The odour is unaccaptable, the amount of H2O2 added is", H2O2)
    print()
elif Odour =="N":
    print("Odour is acceptable")
    print()

while ph_value < sans_secondary["pH_low"] or ph_value > sans_secondary["pH_high"]:
    if ph_value < sans_secondary["pH_low"]:
        chemical_vol += ltr * pH_high 
        ph_value = ph_value + 0.5 * ph_value
        ph_value_increment +=1
            
    elif ph_value > sans_secondary["pH_high"]:
        chemical_vol -= ltr * pH_low 
        ph_value = ph_value - 0.5 * ph_value
        ph_value_increment +=1

print('The ph value of the water is:', n_ph_value)
print()
print("Amount of chemical used:", chemical_vol, "ml")
print()
print("The number of pH treatment cycles is:", ph_value_increment) 
print()     

while turbidity > sans_secondary["turbidity_high"]:

    settling_time =settling_time + (settling_time*0.3)
    turbidity =turbidity - turbidity * 0.4
    n_turbidity = turbidity
     
print("The settling time is:" ,settling_time, "minutes")
print()
print('The turbidy value of the water was:', turbidity_int, "NTU")
print()
print('The turbidity value after treatment:', n_turbidity, "NTU")
print()

print('All conditions for secondary water treatment are met, we are now going for advanced water treatment.' )
print()
continuing = input('Do you want to continue? Y/N: ')

if continuing == 'Y':
    print("Proceeding to tertiary phase")
    print()
    
    methods = ["Crossflow filtration using reverse osmosis", "Photocatalytic degradation using titanium dioxide in the presence of UV light"]
    sans_tertiry = {"colour": 20, "conductivity":150, "TDS": 1000, "pH_low": 6.5, "pH_high": 8, "turbidity_high":1 }
    
    N_colour_in = N_colour
    n_colour_increment = 0
    n_hydraulic_retention_time = 60
    n_ph_value_increment = 0
    n_settling_time = 60
    
    if conductivity>= sans_tertiry["conductivity"]:
        while n_turbidity > sans_tertiry["turbidity_high"]:
    
            n_settling_time =n_settling_time + (n_settling_time*0.3)
            n_turbidity =n_turbidity - n_turbidity * 0.4
        
        
        print("Perform the following method:", methods[0])
        print()
        print("The expected results for the above treatment method are as follows:")
        print()
        print("The turbidity is: ", n_turbidity)
        print()
    else:   
        while n_turbidity > sans_tertiry["turbidity_high"]:
    
            n_settling_time =n_settling_time + (n_settling_time*0.3)
            n_turbidity =n_turbidity - n_turbidity * 0.4
        
        print("Perform the following method:",methods[1])
        print()
        print("The expected results for the above treatment method are as follows:")
        print()
        print("The turbidity is:", n_turbidity)
        print()
        
    while n_ph_value < sans_tertiry["pH_low"] or n_ph_value > sans_tertiry["pH_high"]:
        if n_ph_value < sans_tertiry["pH_low"]:
            chemical_vol += ltr * pH_high 
            n_ph_value = n_ph_value + 0.5 * n_ph_value
            n_ph_value_increment +=1          
            
        elif n_ph_value > sans_tertiry["pH_high"]:
            chemical_vol -= ltr * pH_low 
            n_ph_value = n_ph_value - 0.5 * n_ph_value
            n_ph_value_increment +=1
    
    print('The ph value of the water is:', n_ph_value)
    print()
    print("Amount of chemical used:", chemical_vol, "ml")
    print()
    print("The number of pH treatment cycles is:", n_ph_value_increment)
    print()
    
    if N_colour>sans_tertiry["colour"]:
        N_colour-=N_colour*0.8
        print("The colour of the water is:",N_colour)
        print()
    
elif continuing == "N":
    print("Thank you, goodbye") 
    print()     
    
        
    
    
   

