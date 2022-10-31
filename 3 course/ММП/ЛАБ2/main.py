import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import os
import random


df = pd.read_excel("C:/Users/admin/Desktop/Labs/3 course/ММП/ЛАБ2/11.xlsx")

def all_distinct():
    # Draw Plot
    plt.figure(figsize=(13,10), dpi= 80)
    plt.title('Density Plot of Time and all Transaction', fontsize=22)
    sns.distplot(df['time_per_block'], color="dodgerblue", label="All trsx", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
    plt.ylabel='Validity Сonfirmation'
    plt.xlabel='Time'
    plt.ylim(0, 0.2)
    # Decoration
    plt.legend()
    plt.show()

def per_trnsx():
    # Draw Plot
    plt.figure(figsize=(13,10), dpi= 80)
    sns.distplot(df.loc[df['transaction_count'] < 500, "time_per_block"], color="dodgerblue", label="- 500", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
    sns.distplot(df.loc[(df['transaction_count'] < 1000) & (df['transaction_count'] > 500), "time_per_block"], color="orange", label="500 - 1000", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
    sns.distplot(df.loc[(df['transaction_count'] < 2000) & (df['transaction_count'] > 1000), "time_per_block"], color="g", label="1000 - 2000", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
    sns.distplot(df.loc[df['transaction_count'] > 2000, "time_per_block"], color="deeppink", label="2000 +", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
    plt.ylim(0, 0.2)

    # Decoration
    plt.title('Density Plot of City Transaction by Count', fontsize=22)
    plt.legend()
    plt.show()

def bar_trnsx():
    x = df['transaction_count'] 
    y = df['time_per_block'] 

    fig, ax = plt.subplots()

    ax.bar(x, y,width = 40)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)    #  ширина Figure
    fig.set_figheight(6)    #  высота Figure

    plt.show()

def new(x):
    df_raw = pd.read_excel("C:/Users/admin/Desktop/Labs/3 course/ММП/ЛАБ2/12.xlsx")
    df = df_raw[['transaction_count', 'median_time','time_per_block']].groupby('median_time').apply(lambda x: x.mean())
    if x:
        df.sort_values('transaction_count', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    import matplotlib.patches as patches

    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=df.index, ymin=0, ymax=df.transaction_count, color='firebrick', alpha=0.7, linewidth=20)

    # Annotate Text
    for i, trx in enumerate(df.transaction_count):
        ax.text(i, trx+0.5, round(trx, 1), horizontalalignment='center')


    # Title, Label, Ticks and Ylim
    ax.set_title('Bar Chart for Transaction Slow Blocks', fontdict={'size':22})
    ax.set(ylabel='Transaction per block', ylim=(0, 4000))
    plt.xticks(df.index, df.median_time, rotation=60, horizontalalignment='right', fontsize=12)

    # Add patches to color the X axis labels
    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)
    
    

    # y = df['transaction_count'] 
    if x:
        ax.plot(df.sort_values(by=['transaction_count'])['time_per_block'] * 50)
    else:
        ax.plot(df['time_per_block'] * 50)

    plt.show()

if __name__ == '__main__':
    os.system('clear')
    print("Enter func ")
    term = input(">")
    match term:
        case '1':
            all_distinct()
        case '2':
            per_trnsx()
        case '3':
            bar_trnsx()
        case '4':
            new(False)
        case '5':
            new(True)
        case _:
            print("try again")