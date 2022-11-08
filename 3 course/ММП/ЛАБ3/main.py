import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class BC_Simulation:
    def __init__(self): 
        self.clock=0.0                      #simulation clock
        self.transaction_arrivalrate = 3.432 

        self.transactions_dispatched = 0.2941
        self.initial_mempool_transactions = 5641
        self.queue_capacity = np.Infinity
        self.mempool_size = self.initial_mempool_transactions

        self.transaction_count = 0
        self.block_count = 1

        self.mining_rate = np.arange(0.001546, 0.001650)
        self.miners_count = 2000

        self.numberoftotal_transactions = 275247

        self.block_size = 1024
        self.transaction_weight = 0.5
        self.mining_time = 600

    def add_mempool(self):
        self.mempool_size += self.mining_time  *  np.random.poisson(self.transaction_arrivalrate)
        print(int(self.mempool_size),np.random.poisson(self.transaction_arrivalrate)/10)
        return self.mempool_size

    def fork(self):
        fork = 0
        self.transaction_count = 0
        while(self.block_size > fork):
            self.transaction_count += 1
            fork += (self.transaction_weight * np.random.uniform(low=0.01,high=1.8))
        print(fork, self.transaction_count)
       
        if(self.mempool_size < self.transaction_count):
            self.mempool_size = 0
        else:
            self.mempool_size = self.mempool_size - self.transaction_count
        return self.transaction_count

    def miningpool(self):
        i = 0
        nonce = 0
        while self.miners_count > i:
            i += 1
            nonce += np.random.uniform(0.001546, 0.001650) 
        return(self.transaction_count / nonce )
    
    def join(self):
        print("ok")





s = BC_Simulation()
s.__init__()
i = 0
txs,index,time,tx_persec,mempool, unconfirmed = [], [],[],[],[],[]

while i < 144:
    mempool.append(s.add_mempool())
    txs.append(s.fork())
    time.append(s.miningpool())
    index.append(i)
    i+=1

for tx, tm in zip(txs, time) :
    tx_persec.append(tx / tm)
for tx, mp in zip(txs, mempool):
    unconfirmed.append(tx+mp)
df1 = pd.DataFrame({'Block_index': index,
                   'Transaction_in_block': txs,
                   'Time_mining': time,
                   'Txs_Per_Sec': tx_persec,
                   'Mempool': mempool,
                   'Unconfirmed': unconfirmed})
df1.to_excel("output.xlsx")    
# Draw Plot



def block_trns():
    plt.figure(figsize=(16,10), dpi= 80)
    plt.plot('Block_index', 'Transaction_in_block', data=df1, color='tab:red')

    # Decoration
    plt.ylim(50, 4000)
    xtick_location = df1.index.tolist()[::12]

    plt.xticks(ticks=xtick_location,  rotation=0, fontsize=12, horizontalalignment='center', alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.grid(axis='both', alpha=.3)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)    
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)    
    plt.gca().spines["left"].set_alpha(0.3)   
    plt.show()

def block_trns1():
    plt.figure(figsize=(16,10), dpi= 80)
    plt.plot('Block_index', 'Time_mining', data=df1, color='tab:red')

    # Decoration
    plt.ylim(500, 900)
    xtick_location = df1.index.tolist()[::12]

    plt.xticks(ticks=xtick_location,  rotation=0, fontsize=12, horizontalalignment='center', alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.grid(axis='both', alpha=.3)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)    
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)    
    plt.gca().spines["left"].set_alpha(0.3)   
    plt.show()

def block_trns2():
    plt.figure(figsize=(16,10), dpi= 80)
    plt.plot('Block_index', 'Txs_Per_Sec', data=df1, color='tab:red')

    # Decoration
    plt.ylim(3.19, 3.20)
    xtick_location = df1.index.tolist()[::12]

    plt.xticks(ticks=xtick_location,  rotation=0, fontsize=12, horizontalalignment='center', alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.grid(axis='both', alpha=.3)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)    
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)    
    plt.gca().spines["left"].set_alpha(0.3)   
    plt.show()

def block_trns3():
    x = df1['Block_index']
    y1 = df1['Mempool']
    y2 = df1['Unconfirmed']

    # Plot Line1 (Left Y Axis)
    fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
    ax1.plot(x, y1, color='tab:red')

    # Plot Line2 (Right Y Axis)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax1.plot(x, y2, color='tab:blue')

    # Decorations
    # ax1 (left Y axis)
    ax1.set_xlabel('Year', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=12)
    ax1.set_ylabel('Personal Savings Rate', color='tab:red', fontsize=20)
    ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
    ax1.grid(alpha=.4)

    # ax2 (right Y axis)
    ax2.set_ylabel("# Unemployed (1000's)", color='tab:blue', fontsize=20)
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    ax2.set_xticks(np.arange(0, len(x), 60))
    ax2.set_xticklabels(x[::60], rotation=90, fontdict={'fontsize':10})
    ax2.set_title("Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis", fontsize=22)
    fig.tight_layout()
    plt.show()

block_trns3()