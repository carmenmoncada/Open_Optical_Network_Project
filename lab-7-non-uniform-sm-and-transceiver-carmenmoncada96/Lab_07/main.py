# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from core.elements import *
from core.parameters import *
from core.utils import *
import csv
import random


def main():
    # Check the parameters.py file to check the constants defined
    # such as speed of light, signal power, number of connections, etc.

    # Initialization of the Network
    net = Network(file_input)   # Check in elements.py to see the root of the file
    net.connect()
    net.switching_matrix_initial(file_input, file_name)
    # net.draw()
    net.weighted_paths_dataframe(signal_power)

    # Set a seed for the random number generator
    random.seed(1)

    # Creating 100 connections with signal_power equal to 1 and with input/output nodes
    # randomly chosen and defined in 'connectionsFile.csv'
    lista_connection = []
    for i in range(connections):
        node1 = random.choice(list(net.nodes.keys()))
        node2 = random.choice(tuple(net.nodes.keys() - {node1}))
        if node1 != node2:
            lista_connection.append(Connection(node1, node2, signal_power))

    # Specify the file name
    csv_file = csv_route_space/'lista_connection.csv'

    # Open the file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the list to the CSV file
        writer.writerow(lista_connection)

    # Stream call
    label = 'snr'
    net.stream(lista_connection, signal_power, label)
    # Calling best_metric function to get the best snr, latency and bit rate
    best_snr, best_latency, best_bit_rate = best_metrics(lista_connection, net)

    # Converting into arrays the snr, latency and bit rates
    snr_array = [-5 if value is None else value for value in best_snr]
    snr_array = np.array(snr_array)
    latency_array = np.array(best_latency)
    bit_rate_array = np.array(best_bit_rate)

    total_capacity, average_bit_rate = total_capacity_and_avg_bit_rate(bit_rate_array)
    plots(label, latency_array, snr_array, bit_rate_array, average_bit_rate, total_capacity)


if __name__ == '__main__':
    main()
