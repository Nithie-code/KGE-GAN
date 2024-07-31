import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] ="Times New Roman"
nb_k = [0.0001, 0.0005,0.001, 0.005, 0.01, 0.05]

#MAP=   [0.716, 0.722,0.724, 0.728, 0.726, 0.725]
#nDCG12 =   [0.772, 0.774,0.775, 0.777,0.7768, 0.7759]
nDCG12 =   [0.775, 0.7760,0.7765, 0.888,0.7768, 0.7759]
nDCG14 =   [0.7624, 0.763, 0.764,0.765,0.7645, 0.7633]
#Recall =   [0.832, 0.835,0.837, 0.842,0.839, 0.837]
xi = list(range(len(nb_k)))
fig = plt.figure()
#plt.plot(xi, MAP,  marker='s', linestyle='solid', label='MAP', color='purple')
plt.plot(xi, nDCG12,  marker='D', linestyle='solid', label='DBLP-V12', color='blue')
plt.plot(xi, nDCG14,  marker='D', linestyle=(5,(10,3)), label='DBLP-V14', color='purple')
#plt.plot(xi, Recall,  marker='s', linestyle='solid', label='Recall', color='blue')
plt.xlabel('Learning rate')
plt.ylabel('nDCG')
plt.xticks(xi, nb_k)
plt.legend(loc="lower left", bbox_to_anchor=(0.6,0.6))
plt.show()
fig.savefig('LearningDDDDV12.pdf', bbox_inches='tight')