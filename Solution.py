import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dQ_dt(Q, t, R, X):
    return R * (X - Q/100)  # ODE：dQ/dt = XR - (Q/100)R

Q0_default = 25     # default sugar dissolved in 100L water: g
R_default = 1       # flow rate: L/min
X_default = 0.5     # inflow concentrations: g/L
figure_size = (15, 8)
t = np.linspace(0, 500, 1000)

# Program A: Effect of different inflow/outflow rates (R)
def plot_R_variation():
    Q0 = Q0_default
    X = X_default
    R_values = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5]
    
    plt.figure(figsize=figure_size)    # figure size
    
    for R in R_values:
        solution = odeint(dQ_dt, Q0, t, args=(R, X))
        plt.plot(t, solution, label=f'R = {R:>4.1f}')
    
    plt.xlabel('Time (minutes)')
    plt.ylabel('Amount of Sugar (g)')
    plt.title('Sugar Dynamics: Fixed Q₀ and X, Varying R\nDefault Q₀ = 25g, Default X = 0.5 g/L')
    plt.legend()
    plt.grid(True)
    plt.savefig('varying_R.png')
    plt.close()

# Program B: Effect of different initial sugar amounts (Q0)
def plot_Q0_variation():
    Q0_values = np.linspace(0, 100, 11)
    X = X_default
    R = R_default
    
    plt.figure(figsize=figure_size)
    
    for Q0 in Q0_values:
        solution = odeint(dQ_dt, Q0, t, args=(R, X))
        plt.plot(t, solution, label=f'Q₀ = {Q0:>4.1f}')
    
    plt.xlabel('Time (minutes)')
    plt.ylabel('Amount of Sugar (g)')
    plt.title('Sugar Dynamics: Fixed X and R, Varying Q₀\nDefault X = 0.5 g/L, Default R = 1 L/min')
    plt.legend()
    plt.grid(True)
    plt.savefig('varying_Q0.png')
    plt.close()

# Program C: Effect of different inflow concentrations (X)
def plot_X_variation():
    Q0 = Q0_default
    X_values = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5]
    R = R_default
    
    plt.figure(figsize=figure_size)
    
    for X in X_values:
        solution = odeint(dQ_dt, Q0, t, args=(R, X))
        plt.plot(t, solution, label=f'X = {X:>4.1f}')
    
    plt.xlabel('Time (minutes)')
    plt.ylabel('Amount of Sugar (g)')
    plt.title('Sugar Dynamics: Fixed Q₀ and R, Varying X\nDefault Q₀ = 25g, Default R = 1 L/min')
    plt.legend()
    plt.grid(True)
    plt.savefig('varying_X.png')
    plt.close()

if __name__ == "__main__":
    plot_R_variation()
    plot_Q0_variation()
    plot_X_variation()
    print("All plots have been generated successfully!")
    print("Including: varying_Q0.png, varying_R.png, and varying_X.png")