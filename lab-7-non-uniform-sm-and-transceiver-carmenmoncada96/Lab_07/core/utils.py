# Use this file to define your generic methods, e.g. for plots
import math
from .elements import plt
from .elements import csfont
import seaborn as sns
from .math_utils import *
from matplotlib.ticker import ScalarFormatter


def truncate(number, decimals=0):
    """
    Truncate or round a number to a specified number of decimal places.
    Parameters:
    - number: The number to be truncated or rounded.
    - decimals: The number of decimal places to keep (default is 0)."""
    if not isinstance(decimals, int):
        raise TypeError('The decimal number must be a integer.')
    elif decimals < 0:
        raise TypeError('The number of decimal must be a number greater than 0')
    elif decimals == 0:
        return math.trunc(number)

    # Returns:
    # The truncated or rounded number. 
    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def total_capacity_and_avg_bit_rate(bit_rate_array):
    total_cap = np.sum(bit_rate_array)
    total_capacity = truncate(total_cap / 1e9, 3)

    bit_rate_avg = np.mean(bit_rate_array)
    bit_rate_average = truncate(bit_rate_avg / 1e9, 3)
    return total_capacity, bit_rate_average


def best_metrics(lista_connection, net):
    # Selecting best snr--------------------------------------------------------------------------------------
    best_snr = []
    path_snr = []
    print('\n''\n''Best SNR found')
    for i in range(len(lista_connection)):
        if lista_connection[i].snr is None:
            print(f'For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
                  lista_connection[i].snr, 'Connection rejected because there is not path available')
        else:
            print(f'For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
                  lista_connection[i].snr)
        best_snr.append(lista_connection[i].snr)
        path_snr.append(lista_connection[i].input + '->' + lista_connection[i].output)

    # Selecting the best latency------------------------------------------------------------------------------
    best_latency = []
    path_latency = []
    print('\n''\n''Best latency found')
    for i in range(len(lista_connection)):
        if lista_connection[i].latency is None:
            print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
                  lista_connection[i].latency, 'Connection rejected because the bit rate is 0 Gbps')

        elif lista_connection[i].latency == 0:
            print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
                  lista_connection[i].latency, 'Connection rejected because there is not path available')
        else:
            print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
                  lista_connection[i].latency)

        best_latency.append(lista_connection[i].latency)
        path_latency.append(lista_connection[i].input + '->' + lista_connection[i].output)

    # Selecting bit rates-------------------------------------------------------------------------------------
    best_bit_rate = []
    path_bit_rate = []
    print('\n''\n''Best bit rate found')
    for i in range(len(lista_connection)):
        first_node = net.nodes[lista_connection[i].input]
        print('For a path between: [', lista_connection[i].input, '->', lista_connection[i].output, '] is',
              lista_connection[i].bit_rate, 'with the strategy: ', '"', first_node.transceiver, '"')
        best_bit_rate.append(lista_connection[i].bit_rate)
        path_bit_rate.append(lista_connection[i].input + '->' + lista_connection[i].output)

    return best_snr, best_latency, best_bit_rate


def plots(label, latency_array, snr_array, bit_rate_array, average_bit_rate, total_capacity):
    # Plotting the snr and latency distributions
    plt.figure(figsize=(8, 5))
    if label == 'SNR' or label == 'snr':
        # For SNRs
        # color='maroon'
        sns.histplot(snr_array, color='red', kde=False, bins=30, edgecolor='k', fill=True)
        plt.xlabel('SNR [dB]', **csfont)
        plt.ylabel('Number of Connections', **csfont)
        plt.title('SNR for 100 Connections', **csfont)
        plt.xticks(fontsize=10, fontname='Times New Roman')
        plt.yticks(fontsize=10, fontname='Times New Roman')

    else:
        # For latencies
        # color='#ff7f0e'
        sns.histplot(latency_array, color='blue', kde=False, bins=30, edgecolor='k', fill=True)
        plt.title('Latencies for 100 Connections', **csfont)
        plt.xlabel('Latency [s]', **csfont)
        plt.ylabel('Number of Connections', **csfont)
        plt.xticks(fontsize=10, fontname='Times New Roman')
        plt.yticks(fontsize=10, fontname='Times New Roman')

    # Plotting the snr and latency distributions
    plt.figure(figsize=(8, 5))
    # Bit Rates
    sns.histplot(bit_rate_array, color='orange', kde=False, bins=30, edgecolor='k', fill=True)
    plt.xlabel('Bit Rate [Gbps]', **csfont)
    plt.ylabel('Number of Connections', **csfont)
    plt.title(f'Bit Rate for 100 Connections', **csfont)
    # Create custom legend items with additional information
    legend_items = [f'Average bit rate: {average_bit_rate} Gbps',
                    f'Total capacity allocated: {total_capacity} Gbps']

    # Add the legend as a text box in the plot
    legend_text = '\n'.join(legend_items)
    plt.text(1.05, 0.5, legend_text, transform=plt.gca().transAxes, fontsize=10, va='center', ha='left',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='square,pad=0.3'))
    plt.xticks(fontsize=10, fontname='Times New Roman')
    plt.yticks(fontsize=10, fontname='Times New Roman')


    plt.tight_layout()
    plt.style.use('seaborn-paper')
    plt.show()
