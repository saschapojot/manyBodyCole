import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return (x/(2*np.sinh(x/2)))**2


hbar=1.05457e-34
kB=1.38e-23

omega=1

TCritical=hbar*omega/kB

TValsAll=np.linspace(TCritical/10,TCritical*10,100)

def EinseinCv(T):
    x=omega*hbar/(kB*T)
    return F(x)


def DulongPetitCv(T):
    return 1


EinsteinCvAll=[EinseinCv(T) for T in TValsAll]
DPCvAll=[DulongPetitCv(T) for T in TValsAll]

TScaled=[T/TCritical for T in TValsAll]

# add the value at T=0
TScaled.insert(0,0)
EinsteinCvAll.insert(0,0)
DPCvAll.insert(0,1)
ftSize=16
plt.figure(figsize=(10,10))
plt.plot(TScaled,EinsteinCvAll,color="blue", label="Einstein")
plt.plot(TScaled,DPCvAll,color="red", label="Dulong-Petit")
plt.xlabel("$T/\\frac{\omega \hbar}{k_{B}}$",fontsize=ftSize)
plt.ylabel("$C_{V}/R$",fontsize=ftSize)
plt.title("Speficific heat for $\omega=1 \operatorname{ s}^{-1}$",fontsize=ftSize)
plt.xlim((0,max(TScaled)))
plt.ylim((0,1.1))
plt.legend(loc="best",fontsize=ftSize)
plt.savefig("ch2Ex2.1.png")