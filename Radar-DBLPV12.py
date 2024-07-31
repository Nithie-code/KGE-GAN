import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-dark-palette') #   seaborn-whitegrid #seaborn-pastel ggplot classic seaborn-v0_8-colorblind seaborn-v0_8-dark-palette

subjects=['MAP','nDCG','Recall']

CCA=[0.268, 0.309,0.698]
BNR=[0.371, 0.462,0.729]
VOPRec=[0.279, 0.377,0.712]
SCRNTR=[0.512, 0.587,0.753]
GCRGAN	=[0.582,0.647,0.775]
KGETransD=[0.590,0.651,0.760]
KGEGAN=[0.728,0.777,0.842]

angles=np.linspace(0,2*np.pi,len(subjects), endpoint=False)
print(angles)
angles=np.concatenate((angles,[angles[0]]))
print(angles)


subjects.append(subjects[0])
CCA.append(CCA[0])
BNR.append(BNR[0])
VOPRec.append(VOPRec[0])
SCRNTR.append(SCRNTR[0])
GCRGAN.append(GCRGAN[0])
KGETransD.append(KGETransD[0])
KGEGAN.append(KGEGAN[0])

#plot radar figures
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
ax.plot(angles,CCA,linewidth=2,label='CCA')
ax.fill(angles, CCA, alpha=0.25, color='Magenta')
ax.plot(angles,BNR,linewidth=2,label='BNR')
ax.fill(angles, BNR, alpha=0.25, color='Magenta') #yellow
ax.plot(angles,VOPRec,linewidth=2,label='VOPRec')
ax.fill(angles, VOPRec, alpha=0.25, color='blue') #blue
ax.plot(angles,SCRNTR,linewidth=2,label='SCR-NTR')
ax.fill(angles, SCRNTR, alpha=0.25, color='Magenta') #yellow
ax.plot(angles,GCRGAN,linewidth=2,label='GCR-GAN')
ax.fill(angles, GCRGAN, alpha=0.25, color='Magenta') #yellow
ax.plot(angles,KGETransD,linewidth=2,label='KGE-TransD')
ax.fill(angles, KGETransD, alpha=0.25, color='black')
ax.plot(angles,KGEGAN,linewidth=2,label='KGE-GAN')
ax.fill(angles,KGEGAN, alpha=0.25, color='black') #black
ax.set_thetagrids(angles * 180/np.pi, subjects)
plt.grid(True)

plt.legend(loc="lower right",fontsize='large')
#plt.gca().legend()

plt.tight_layout()
plt.savefig('Radar-DBLP-V12-KGE-GAN.pdf')
plt.show()