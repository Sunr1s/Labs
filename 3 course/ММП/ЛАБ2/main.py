import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.patches as patches

sns.set_context("poster")  # It makes the labels, titles, etc. larger for better readability.

BASE_DIR = "C:/Users/admin/Desktop/Labs/3 course/ММП/ЛАБ2"

def load_data(file_name):
    return pd.read_excel(os.path.join(BASE_DIR, file_name))

def draw_density_plot(title, data, labels, colors):
    plt.figure(figsize=(13,10), dpi= 80)
    plt.title(title, fontsize=22)
    for label, color in zip(labels, colors):
        sns.kdeplot(data[label], color=color, label=label, linewidth=3)
    plt.legend(fontsize=20)
    plt.show()

def all_distinct(df):
    draw_density_plot(
        'Density Plot of Time and all Transaction', 
        df,
        ['time_per_block'], 
        ["dodgerblue"]
    )

def per_trnsx(df):
    labels = ['- 500', '500 - 1000', '1000 - 2000', '2000 +']
    colors = ['dodgerblue', 'orange', 'green', 'deeppink']
    data = df.loc[df['transaction_count'] < 500, "time_per_block"]
    for i in range(500, 2000, 500):
        data = pd.concat([data, df.loc[(df['transaction_count'] < i+500) & (df['transaction_count'] > i), "time_per_block"]], axis=1)
    data = pd.concat([data, df.loc[df['transaction_count'] > 2000, "time_per_block"]], axis=1)
    data.columns = labels
    draw_density_plot(
        'Density Plot of City Transaction by Count', 
        data,
        labels,
        colors
    )

def bar_trnsx(df):
    fig, ax = plt.subplots(figsize=(13,10), dpi= 80)
    ax.bar(df['transaction_count'], df['time_per_block'], width=40)
    plt.show()

def new(df, sort):
    df_raw = load_data("12.xlsx")
    df = df_raw[['transaction_count', 'median_time','time_per_block']].groupby('median_time').apply(lambda x: x.mean())
    if sort:
        df.sort_values('transaction_count', inplace=True)
    df.reset_index(inplace=True)

    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=df.index, ymin=0, ymax=df.transaction_count, color='firebrick', alpha=0.7, linewidth=20)

    # Annotate Text
    for i, trx in enumerate(df.transaction_count):
        ax.text(i, trx+0.5, round(trx, 1), horizontalalignment='center')

    ax.set_title('Bar Chart for Transaction Slow Blocks', fontsize=22)
    ax.set(ylabel='Transaction per block', ylim=(0, 4000))

    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)

    if sort:
        ax.plot(df.sort_values(by=['transaction_count'])['time_per_block'] * 50)
    else:
        ax.plot(df['time_per_block'] * 50)

    plt.show()

if __name__ == '__main__':
    os.system('clear')
    print("Enter the number corresponding to the function you want to use:\n1. all_distinct\n2. per_trnsx\n3. bar_trnsx\n4. new(False)\n5. new(True)")
    term = input(">")
    df = load_data("11.xlsx")
    functions = {
        '1': all_distinct,
        '2': per_trnsx,
        '3': bar_trnsx,
        '4': lambda df: new(df, False),
        '5': lambda df: new(df, True),
    }
    try:
        functions[term](df)
    except KeyError:
        print("Invalid input. Please try again.")
