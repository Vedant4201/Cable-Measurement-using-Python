import pandas as pd
import matplotlib.pyplot as plt
import math

#Defining constant values
#K = 950000 # in (N/m)
K = 75000 # in (N/m) # Choosen specifically to visualize the non-linearity in the graph
H0 = 0.07 # in (meters) # This is the maximum deflection the spring will undergo

# Created lists for the required parameters to be visualized for the estiamted spring stiffness value
deflection=[]
spring_load=[]
angle_change=[]

for i in range(1, 66): # Here, is the tension load experienced by the cable (in kN)
    del_x=(2*H0*i*1000)/(K+(2*i*1000)) #in meters 
    deflection.append(del_x) 
    F_t=K*del_x
    spring_load.append(F_t)
    theta=math.degrees(math.asin(F_t/(2*i*1000))) # Assumed the deflected cable is straight for very small deflected angle
    angle_change.append(theta)

# Created excel sheet to store the calculated values
df=pd.DataFrame({'Tension(kN)': list(range(1, 66)), 'Deflection(m)': deflection, 'Spring_Load(N)': spring_load, 'Angle_change(deg)': angle_change})
df.to_csv('Cable_Tension_measurement_calc.csv', index=False)
print('Data written to excel successfully')

df.plot(
    kind='line', 
    x='Tension(kN)', 
    y='Deflection(m)',
    xlabel='Tension (kN)',
    ylabel='Spring Deflection (m)', 
    title='Tension vs. Spring Deflection',
    color='blue',
    figsize=(8, 5),
    grid=True
)
plt.show()

df.plot(
    kind='line', 
    x='Tension(kN)', 
    y='Spring_Load(N)',
    xlabel='Tension (kN)',
    ylabel='Spring Load (N)', 
    title='Tension vs. Spring Load',
    color='red',
    figsize=(8, 5),
    grid=True
)
plt.show()

df.plot(
    kind='line', 
    x='Tension(kN)', 
    y='Angle_change(deg)',
    xlabel='Tension (kN)',
    ylabel='Cable_Angle_change (deg)', 
    title='Tension vs. Cable angle change wrt  deflection',
    color='green',
    figsize=(8, 5),
    grid=True
)
plt.show()
