import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dQ_dt(Q, t, R, X):
    return R * (X - Q/100)  # ODE：dQ/dt = XR - (Q/100)R

figure_size = (15, 8)
t = np.linspace(0, 500, 1000)

R_values = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5]
print('Generating the graph of fixed Q₀ and X, varying R');
Q0 = float(input('Please input fixed Q₀(g): '))
X = float(input('Please input fixed X(g/L): '))

plt.figure(figsize=figure_size)    # figure size

for R in R_values:
    solution = odeint(dQ_dt, Q0, t, args=(R, X))
    plt.plot(t, solution, label=f'R = {R:>4.1f}')

plt.xlabel('Time (minutes)')
plt.ylabel('Amount of Sugar (g)')
plt.title(f'Sugar Dynamics: Fixed Q₀ and X, Varying R\nDefault Q₀ = {Q0}g, Default X = {X} g/L')
plt.legend()
plt.grid(True)
plt.savefig('R.png')
plt.close()

print("The plot have been generated successfully!")
print("File Name: R.png")