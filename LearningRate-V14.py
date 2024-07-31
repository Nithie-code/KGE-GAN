import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] ="Times New Roman"
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
nb_k = [1, 2,3, 4, 5, 6]
MAP=  [0.528, 0.587,0.705, 0.728, 0.724, 0.722]
MRR= [0.549, 0.624,0.689, 0.724,0.716, 0.712]
nDCG  =[0.582, 0.638,0.724, 0.748, 0.740, 0.735]
xi = list(range(len(nb_k)))
fig = plt.figure()
plt.plot(xi, MAP,  marker='s', linestyle='solid', label='MAP', color='purple')
plt.plot(xi, MRR,  marker='D', linestyle='solid', label='MRR', color='red')
plt.plot(xi, nDCG,  marker='s', linestyle='solid', label='nDCG', color='blue')
plt.xlabel(' Number of  RMCs',fontsize=18)
plt.ylabel('Score',fontsize=18)
plt.xticks(xi, nb_k)
plt.legend(loc="lower left", bbox_to_anchor=(0.6,0.6))
plt.show()
fig.savefig('AAN1.pdf', bbox_inches='tight')