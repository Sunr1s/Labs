from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # генерируем данные 
    n = 10
    x = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
    y = np.array([74.04, 71.32, 81.87, 78.1, 80.39, 86.43, 85.76, 91.85, 93.08, 91.69])
    numb = np.arange(0,n,1)



    #линия регрессии
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    line = slope*x+intercept

    #создание кроссплота
    fig = plt.figure(figsize=(10,7))
    ax = plt.subplot(111)

    plt.scatter(x,y, s=50, c=numb)
    plt.plot(x, line, 'r', label='y={:.2f}x+{:.2f}'.format(slope,intercept))
    plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))

    plt.grid(True)
    plt.legend(fontsize=12)
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()