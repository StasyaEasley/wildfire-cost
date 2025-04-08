import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def sir_model(y, t, beta, gamma):
    S,I,R=y
    dSdt = -beta *S*I
    dIdt= beta *S*I - gamma*I
    dRdt = gamma*I
    return [dSdt,dIdt,dRdt]

S0 = .99
I0 = 0.01
R0 = 0.0

initial_cond= [S0,I0,R0]

t = np.linspace(0,100,100)
beta = 0.3
gamma = 0.1

solution = odeint(sir_model, initial_cond, t, args=(beta,gamma))
S, I, R = solution.T


plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.xlabel("Time (days)")
plt.ylabel("Population Fraction")
plt.legend()
plt.title("SIR Model Simulation")
plt.show()