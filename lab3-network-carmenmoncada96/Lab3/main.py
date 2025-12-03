# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from core.elements import *
from core.parameters import *
from core.elements import csfont
import seaborn as sns
import random

def main():
    # Check the parameters.py file to check the constants defined
    # such as speed of light, signal power, number of connections, etc.

    # Initialization of the Network
    net = Network(file_input)
    net.connect()
    # net.draw()
    net.weighted_paths_dataframe(signal_power)

    # Set a seed for the random number generator
    random.seed(10)

    # Creating 100 Connections
    lista_connection = []
    for i in range(connections):
        node1 = random.choice(list(net.nodes.keys()))
        node2 = random.choice(tuple(net.nodes.keys() - {node1}))
        if node1 != node2:
            lista_connection.append(Connection(node1, node2, signal_power))

    # Stream call
    label = 'snr'
    net.stream(lista_connection, signal_power, label)

    # Selecting best snr
    best_snr = []
    path_snr = []
    print('\n''\n''Best SNR found')
    for i in range(len(lista_connection)):
        print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
              lista_connection[i].snr)
        best_snr.append(lista_connection[i].snr)
        path_snr.append(lista_connection[i].input + '->' + lista_connection[i].output)

    # Selecting best
    best_latency = []
    path_latency = []
    print('\n''\n''Best latency found')
    for i in range(len(lista_connection)):
        print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
              lista_connection[i].latency)
        best_latency.append(lista_connection[i].latency)
        path_latency.append(lista_connection[i].input + '->' + lista_connection[i].output)

    # Plotting the snr and latency distributions
    snr_array = [0 if value is None else value for value in best_snr]
    snr_array = np.array(snr_array)
    latency_array = np.array(best_latency)

    plt.figure(figsize=(8, 5))
    if label == 'SNR' or label=='snr':
        # For SNRs
        #plt.hist(snr_array, color='maroon', histtype='stepfilled', bins=30, edgecolor='k')
        sns.histplot(snr_array, color='red', kde=False, bins=30, edgecolor='k', fill=True)
        plt.xlabel('SNR [dB]', **csfont)
        plt.ylabel('Number of Connections', **csfont)
        plt.title('SNR for 100 Connections', **csfont)
        plt.xticks(fontsize=10, fontname='Times New Roman')
        plt.yticks(fontsize=10, fontname='Times New Roman')
    else:
        # For latencies
        #plt.hist(latency_array*1e3, color='#ff7f0e', bins=30, histtype='stepfilled', edgecolor='k')
        sns.histplot(latency_array, color='blue', kde=False, bins=30, edgecolor='k', fill=True)
        plt.title('Latencies for 100 Connections', **csfont)
        plt.xlabel('Latency [s]', **csfont)
        plt.ylabel('Number of Connections', **csfont)
        plt.xticks(fontsize=10, fontname='Times New Roman')
        plt.yticks(fontsize=10, fontname='Times New Roman')

    plt.style.use('seaborn-paper')
    plt.show()
    plt.tight_layout()

if __name__ == '__main__':
    main()
