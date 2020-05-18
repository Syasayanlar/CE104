moments = [1e8, 1e8, 231e5, 500e5, 1200e5]
inertia = [130e6, 200e6, 500e6, 120e6, 600e6]
dist = [100, 230, 630, 330, 600]

# to calculate the stress on a section
# stress = (moment*distance)/interia 
# formula is used
# In the given data moment, inertia and distance values for
# specific sections are given
# Now write a function to compute stress values for each other

def calc_stress(moment, inertia, dist):
    stress = (moment*dist)/inertia
    return stress

stress = [0 for i in range(len(moments))]
for i in range(len(moments)):
    stress[i] = calc_stress(moments[i], inertia[i], dist[i])
    
print('Stress :', stress)


# If the names of the sections are IP_200, sect_2, sect_3, sect_4 and sect_5
# by using dictionary data type, store each sections stress


stress_dict = {}
for i in range(len(moments)):
    my_str = 'sect_'+str(i)
    stress_dict[my_str] = stress[i]
 
print('\nStress values in sections :')
for (k,v) in stress_dict.items():
    print(k, ': ', v, 'MPa')
    
