import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dQ_dt(Q, t, R, X):
    return R * (X - Q/100)  # ODE：dQ/dt = XR - (Q/100)R

figure_size = (15, 8)
t = np.linspace(0, 500, 1000)

Q0_values = np.linspace(0, 100, 11)
print('Generating the graph of fixed X and R, varying Q₀');
X = float(input('Please input fixed X(g/L): '))
R = float(input('Please input fixed R(L/min): '))

plt.figure(figsize=figure_size)

for Q0 in Q0_values:
    solution = odeint(dQ_dt, Q0, t, args=(R, X))
    plt.plot(t, solution, label=f'Q₀ = {Q0:>4.1f}')

plt.xlabel('Time (minutes)')
plt.ylabel('Amount of Sugar (g)')
plt.title(f'Sugar Dynamics: Fixed X and R, Varying Q₀\nDefault X = {X} g/L, Default R = {R} L/min')
plt.legend()
plt.grid(True)
plt.savefig('Q0.png')
plt.close()

print("The plot have been generated successfully!")
print("File Name: Q0.png")