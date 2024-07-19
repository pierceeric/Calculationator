# Given tau, this program calculates voltage while Charging an RC circuit

from math import e

tau = 20    # time constant
initial_voltage = 0
final_voltage = 30
calculation_duration = 5 # number of time constants to calculate
voltage_difference = final_voltage-initial_voltage

time_elapsed = 0
while time_elapsed <= (calculation_duration*tau):
    percent_charge = 1-1/(e**(time_elapsed/tau))
    value=voltage_difference*percent_charge
    print("After ",(time_elapsed/tau), "time-constants the voltage is ", value, "V.")
    time_elapsed+=tau
