# %% codecell
# !pip install qutip
# %% codecell
import matplotlib.pyplot as plt
import numpy as np
import qutip
from qutip import *

# good overview:
# https://nbviewer.jupyter.org/github/jrjohansson/qutip-lectures/blob/master/Lecture-0-Introduction-to-QuTiP.ipynb
# %% codecell
# signele qobject, like a state or ket
q = Qobj([[1], [0]])

print(q,'\n')

print(q.dims)
print(q.shape)
print(q.type)
# %% codecell
# operators
sx = Qobj([[0,1],[1,0]])
sy = Qobj([[0,-1j], [1j,0]])
sz = Qobj([[1,0], [0,-1]])

nh = Qobj([[2,1j], [0,-1]])

print(sy.full())
print(abs(sy.full()))

H = 1*sz + 0.2*sy
print("\n Qubit Hamiltonian =")
H
# %% codecell
# hermitian conjugate
print(nh.full(),"\n \nhermitian conjugate:\n",nh.dag().full(),"\n")

# trace
print("trace H = ",H.tr(),", trace nh = ", nh.tr(),"\n")

# eigenstates and eigenenergies
eigensys = H.eigenstates()
print(eigensys)
eigenE1 = eigensys[0][1]
eigenS1 = eigensys[1][1]
print("\nfirst eigenenergy: ",eigenE1,"\n")
print("corresponding eigenstate:\n",eigenS1.full(),"\n")

print(H*eigenS1 == eigenE1*eigenS1)
H*eigenS1
# %% codecell
print(H*eigenS1 == eigenE1*eigenS1)
H*eigenS1
# %% codecell
# Fock state (first number of states, second occupied state)
fock(5,0)
# %% codecell
# coherent state
coh = coherent(10,1.3)

cohP = abs(coh.dag().full())[0]
print(cohP)
plt.bar(np.arange(0,10),cohP)
plt.show()

coh
# %% codecell
# density matrix of a coherent state
coherent_dm(10,2)
# %% codecell
# density matrix of a coherent state
coh = abs(coherent_dm(12,2).full())
plt.imshow(coh, origin = 'lower')
plt.show()


coh2 = displace(12,2)*fock(12)
coh2_dm = coh2*coh2.dag()
coh3 = abs(coh2_dm.full())
plt.imshow(coh3, origin = 'lower')
plt.show()

coh2_dm
# %% codecell
# squeezed vacuum
n = 16
vac = fock(n)
sq = squeeze(n,1)

# create squeezed vacuum
sVac = sq*vac
sVacP = abs(sVac.dag().full())[0]
plt.bar(np.arange(0,n),sVacP)
plt.show()

sVac_dm = sVac*sVac.dag()
sVac_dm_p = abs(sVac_dm.full())
plt.imshow(sVac_dm_p, origin = 'lower')
plt.show()
# %% codecell
# exponential, here calculate sig_x exp(i w t)
omega = 1.0
es1 = eseries(sigmax(), 1j * omega)
# %% codecell

# %% codecell

# %% codecell

# %% codecell
pl = plt.imshow(velocityMap, cmap='hot', origin = 'lower', extent = (0, 1, 0, 1))
