#2.3

import numpy as np
from math import factorial

N = 60
Up = 0
Down = 1
M = 10**4
macrostate = []
Counter = 0


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

S = np.zeros(len(macrostate)) #spin up
NetS = np.zeros(len(macrostate)) #net spin

for i in range(len(macrostate)):
    S[i] = macrostate[i].count(0)
    NetS[i] = -N + 2*S[i]

import matplotlib.pyplot as plt
import scipy.stats

x_min = -25
x_max = 25

mean = 0

std = 3.8

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y*10**4, color='coral')

plt.hist(NetS, bins=30)

plt.title('Net spin compared with the Gaussian distribution',fontsize=14)

plt.xlabel('Net spin S', fontsize=14)
plt.ylabel('Amount of the same net spin',fontsize=14)
plt.show()

Ω = np.zeros(len(macrostate))
SB = np.zeros(len(macrostate))
k = 1.38065 * 10**-23

Ωmax = factorial(N)/(factorial(N/2)*factorial(N/2))
for i in range(len(macrostate)):
    Ω[i] = Ωmax*np.exp(-S[i]**2/(2*N))
    SB[i] = k*np.log(Ω[i])

plt.plot(NetS,SB)
plt.title('Entropy as a function of N and the net spin S',fontsize=14)
plt.xlabel('Net spin S', fontsize=14)
plt.ylabel('Entropy',fontsize=14)
plt.show()
