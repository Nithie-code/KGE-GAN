import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] ="Times New Roman"
nb_RMCs = [1, 2,3, 4, 5, 6,7,8]
MAP =   [0.558, 0.585,0.6268, 0.658,0.672,0.686,0.695, 0.690]
MRR =   [0.522, 0.547,0.578, 0.612,0.632,0.637,0.643, 0.652]
nDCG =   [0.595, 0.603,0.598, 0.593,0.591, 0.589, 0.600, 0.605]
xi = list(range(len(nb_RMCs)))
fig = plt.figure()
plt.plot(xi, MAP,  marker='s', linestyle='solid', label='MAP', color='purple')
plt.plot(xi, MRR,  marker='D', linestyle='solid', label='MRR', color='brown')
plt.plot(xi, nDCG ,  marker='s', linestyle='solid', label='nDCG', color='purple')
plt.xlabel('# of RMCs')
plt.ylabel('Score')
plt.xticks(xi, nb_RMCs)
plt.legend(loc="lower left", bbox_to_anchor=(0.6,0.4))
plt.show()
fig.savefig('Epoch.pdf', bbox_inches='tight')