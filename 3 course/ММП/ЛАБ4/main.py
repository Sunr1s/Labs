from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def np_linereg():
     #линия регрессии
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    line = slope*x+intercept

    #создание кроссплота
    fig = plt.figure(figsize=(10,7))
    ax = plt.subplot(111)

    RSS = np.sum(np.square(line - y))
    MSE = np.mean(np.square(line - y))
    RMSE = np.sqrt(np.mean(np.square(line - y)))

    print(' residual sum of squares is : '+ str(RSS))
    print(' mean squared error is : '+ str(MSE))
    print(' root mean squared error is : '+ str(RMSE))

    plt.scatter(x,y, s=50, c=numb)
    plt.plot(x, line, 'r', label='y={:.2f}x+{:.2f}'.format(slope,intercept))
    plt.plot([], [], ' ', label='R_sq = '+'{:.2f}'.format(r_value**2))
    plt.plot([], [], ' ', label='RSS = '+'{:.2f}'.format(RSS))
    plt.plot([], [], ' ', label='MSE = '+'{:.2f}'.format(MSE))
    plt.plot([], [], ' ', label='RMSE = '+'{:.2f}'.format(RMSE))

    plt.grid(True)
    plt.legend(fontsize=12)
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def model_test(x, y):
    # adding constant
    x = sm.add_constant(x)
    
    #fit linear regression model
    model = sm.OLS(y, x).fit()
    
    #display model summary
    print(model.summary())
    
    # residual sum of squares
    print(model.ssr)

def scipi_mth(x,y):
    # Create linear regression object
    regr = LinearRegression()
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    # Train the model using the training sets
    regr.fit(x, y)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(x)

    # The coefficients
    print("Coefficients: \n", regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(y, diabetes_y_pred))

    plt.figure(figsize=(10,7))

    # Plot outputs
    plt.scatter(x, y, color="black", s =50)

    plt.plot(x, diabetes_y_pred, color="blue", linewidth=3, label='y={:.2f}x+{:.2f}'.format(float(regr.coef_),float(regr.intercept_)))

    plt.plot([], [], ' ', label='RSS = '+'{:.2f}'.format(np.sum((diabetes_y_pred - y) ** 2)))
    plt.plot([], [], ' ', label='MSE = '+'{:.2f}'.format(mean_squared_error(y, diabetes_y_pred)))
    plt.plot([], [], ' ', label='RMSE = '+'{:.2f}'.format(np.sqrt(mean_squared_error(y, diabetes_y_pred))))

    plt.grid(True)
    plt.legend(fontsize=12)
    plt.colorbar()

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks(())
    plt.yticks(())

    plt.show()


if __name__ == '__main__':

    # генерируем данные 
    n = 10
    x = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
    y = np.array([74.04, 71.32, 81.87, 78.1, 80.39, 86.43, 85.76, 91.85, 93.08, 91.69])
    numb = np.arange(0,n,1)
    
    np_linereg()

    scipi_mth(x,y)

    model_test(x, y)


   