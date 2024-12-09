# This is Equation 9.10 from the NRECA Design Guide for Rural Substations 1999
# AGW 4 is 212 kcmil

from math import sqrt
from math import log

I = float(input("What is the maximum fault current for this design (3 is common) (kV)? "))   # rms fault current (kA)
# Value Assumptions
T_m = 1084              # Maximum allowable Temperature (Fusing Temp) (degreesC)
T_a = 40                # Ambient Temperature (degreesC)
T_r = 20                # Reference Temperature for material constants (degreesC)
alpha_0 = 1             # Thermal coefficient of resistivity at 0 degrrees C (1/degrees C)
alpha_r = 0.00381       # Thermal coefficient of resistivity at reference temperature T_r (1/degrees C)
rho_r = 1.78            # Resistivity of the ground conductor at reference temperature (micro-ohms-cm)
K_0 = (1/alpha_r)-T_r   # or = 1/alpha_0 (degrees C)
t_c = 0.050             # Fault current duration (s)
TCAP = 3.42             # Thermal Capacity per unit volume (J/(cm^3 * degreesC))

A_kcmil = (I * 197.4)/sqrt((TCAP/(t_c*alpha_r*rho_r))*log((K_0+T_m)/(K_0+T_a)))
print(A_kcmil, " Minimum Area of Ground Conductor (kcmil)")
