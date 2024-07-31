import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] ="Times New Roman"
nb_epoch = [50, 100, 200,300,400,500,600,700] #13
nDCG12 =   [ 0.628,0.658,0.716,0.753,0.777,0.77899,0.776,0.775]
nDCG14 =   [0.637,0.673,0.698,0.720,0.748,0.765,0.7638,0.761988]
#Recall =   [0.595, 0.603,0.598, 0.593,0.591, 0.589]
xi = list(range(len(nb_epoch)))
fig = plt.figure()
plt.plot(xi, nDCG12,  marker='s', linestyle=(5,(10,3)), label='DBLP-V12', color='blue')
plt.plot(xi, nDCG14,  marker='D', linestyle=(5,(10,3)), label='DBLP-V14', color='purple')
#plt.plot(xi, Recall,  marker='s', linestyle='solid', label='Recall', color='purple')
plt.xlabel('Epoch')
plt.ylabel('nDCG')
plt.xticks(xi, nb_epoch)
plt.legend(loc="lower left", bbox_to_anchor=(0.6,0.4))
plt.show()
fig.savefig('Epoch12.pdf', bbox_inches='tight')