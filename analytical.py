#2.6

import numpy as np
from math import factorial

N = 60
Up = 0
Down = 1
M = 10**4
macrostate = []
Counter = 0

import matplotlib.pyplot as plt
for i in range(10**5):

    microstates = [np.random.randint(Up, Down+1) for iter in range(N+1)]

    if microstates in macrostate:
        Counter += 1
    else:
        macrostate.append(microstates)

    if len(macrostate) == M:
        break
print('Failed attempts = ', Counter)
print('Number of microstates = ', len(macrostate))

from math import sqrt, pi

S = np.zeros(len(macrostate)) #spin up
NetS = np.zeros(len(macrostate)) #net spin
Al = np.zeros(len(macrostate)) #analytical solution
o_max = sqrt(2)*2**N/sqrt(pi*N)

for i in range(len(macrostate)):
    S[i] = macrostate[i].count(0)
    NetS[i] = -N + 2*S[i]
    Al[i] = o_max*np.exp(-NetS[i]**2/(2*N))


plt.title('2.6: Analytical result')
plt.plot(NetS, Al)
#plt.hist(NetS, bins=30)
plt.xlabel('Net spin S', fontsize=14)
plt.ylabel('Amount of the same net spin',fontsize=14)
plt.show()


Ent = np.zeros(len(macrostate))
k = 1.38065 * 10**-23


for i in range(len(macrostate)):
    Ent[i] = k*np.log(Al[i])

plt.plot(NetS,Ent)
plt.title('Entropy as a function of N and the net spin S',fontsize=14)
plt.xlabel('Net spin S', fontsize=14)
plt.ylabel('Entropy',fontsize=14)
plt.show()
