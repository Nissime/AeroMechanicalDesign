import numpy as np

# ## GENERAL PARAMS
# NUM_OF_ROTORS =  #[/]
# MODEL_WEIGHT  =  #[g]
# FRAME_SIZE    =  #[mm]

# #BATTERY
# BATTERY_TYPE  = #[mah]
# BATTERY_CELLS = #[number of cells]
# BATTERY_MAX_DISCHARGE = #[%]
# #CONTROLLER
# CONTROLLER_TYPE = 
# #MOTOR
# MOTOR_MANUFACTURER = 
# MOTOR_TYEP = #kv


Platforms = {
    "mavic2zoom" : {
        "flight_time[min]" : 29.0,
        "battery[mAh]" : 3950.0,
        "weight[gr]" : 905.0,
        "diagonal_distance[mm]" : 354.0,
        "operating_current[Aa]" : 1800.0,
        "operating_voltage[v]" : 3.83,
        "energy[Wh]" : 59.29,
        "battery_weight[gr]" : 297.0},
    "mavic2pro" : {
        "flight_time[min]" : 29.0,
        "battery[mAh]" : 3950.0,
        "weight[gr]" : 907.0,
        "diagonal_distance[mm]" : 354.0,
        "operating_current[mA]" : 1800.0,
        "operating_voltage[v]" : 3.83,
        "energy[Wh]" : 59.29,
        "battery_weight[gr]" : 297.0},
    "phantom4pro" : {
        "flight_time[min]" : 28.0,
        "battery[mAh]" : 6000.0,
        "weight[gr]" : 1375.0,
        "diagonal_distance[mm]" : 350.0 ,
        "operating_current[mA]" : 1200.0,
        "operating_voltage[v]" : 7.4,
        "energy[Wh]" : 89.2,
        "battery_weight[gr]" : 460.8},
    "mavic air" : {
        "flight_time[min]" : 20.0,
        "battery[mAh]" : 2970.0,
        "weight[gr]" : 430.0,
        "diagonal_distance[mm]" : 213.0,
        "operating_current[mA]" : 750.0,
        "operating_voltage[v]" : 3.7,
        "energy[Wh]" : 27.43,
        "battery_weight[gr]" : 140.0}
}
print("here")

for x in list(Platforms):
    Platforms[x]['battery_weight_ratio']=Platforms[x]['battery_weight[gr]']/Platforms[x]['weight[gr]']*100.0
    print("battery_weight_ratio in "+x+" is: "+str(round(Platforms[x]['battery_weight_ratio']))+"%")
    
# LIST OF ALL PLATFORMS : list(Platforms)
#RETRIVE DATA : Platform[x]['battery']