from scipy import stats,optimize 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def f(x):
 return (x - 2) * x * (x + 2)**2

def f2(paramt):
    """The Rosenbrock function with additional arguments"""
    x, y = paramt
    return (x - 2) ** 2 * (y + 2)**2


def print_f(x, x_min, f_min):
    fig = plt.figure(figsize=(10,7))
    ax = plt.subplot(111)
    plt.scatter(x_min, f_min, c='r')
    plt.plot(x, f(x), c='k', label=r'$f(x)$')
    plt.title('f(x) = (x-2)*x*(x+2)^2')
    plt.show()

def print_f2(X,Y,Z,x_min,z_min):
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,lw=0.5,
                    cmap='viridis', edgecolor='grey', alpha = 0.8)

    ax.scatter(x_min[0], x_min[1], z_min, s=50, c='k', marker='o')

    ax.contour(X, Y, Z, zdir='z', offset=4096, cmap='coolwarm')
    ax.contour(X, Y, Z, zdir='x', offset=-6, cmap='coolwarm')
    ax.contour(X, Y, Z, zdir='y', offset=-6, cmap='coolwarm')

    ax.set(xlim=(-10,7), ylim=(-10,7), zlim=(0,4100), xlabel='X',ylabel='Y', zlabel='Z')
    ax.set_title('surface')

    plt.show()

    ax2 = plt.subplot(132)
    plt.contour(X, Y, Z, cmap='coolwarm', levels =20)
    plt.colorbar()

    ax.scatter(x_min[0], x_min[1], z_min,s=50, c='k', marker='o', label = min, linewidths=2)

    plt.show()

if __name__ == '__main__':
    x_min = optimize.minimize_scalar(f).x
    f_min = f(x_min)
    print_f(np.arange(0.0, 2.0, 0.01),x_min, f_min)
    first_guess = [0, 0]
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
    X, Y = np.meshgrid(x, y)

    x_min = optimize.minimize(f2, first_guess, method='nelder-mead').x
    Z= f2([X, Y])
    
    z_min = f2(x_min)
    print_f2(X,Y,Z,x_min, z_min)


   