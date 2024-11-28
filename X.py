import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dQ_dt(Q, t, R, X):
    return R * (X - Q/100)  # ODE：dQ/dt = XR - (Q/100)R

figure_size = (15, 8)
t = np.linspace(0, 500, 1000)

X_values = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5]
print('Generating the graph of fixed Q₀ and R, varying X');
Q0 = float(input('Please input fixed Q₀(g): '))
R = float(input('Please input fixed R(L/min): '))

plt.figure(figsize=figure_size)    # figure size

for X in X_values:
    solution = odeint(dQ_dt, Q0, t, args=(R, X))
    plt.plot(t, solution, label=f'X = {X:>4.1f}')

plt.xlabel('Time (minutes)')
plt.ylabel('Amount of Sugar (g)')
plt.title(f'Sugar Dynamics: Fixed Q₀ and R, Varying X\nDefault Q₀ = {Q0}g, Default R = {R} L/min')
plt.legend()
plt.grid(True)
plt.savefig('X.png')
plt.close()

print("The plot have been generated successfully!")
print("File Name: X.png")