#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os


figures = ["BLIND", "CDR", "TI"]


def read_ranking_file(file_name, with_std=False):
    incorrect = []
    acceptable = []
    medium = []
    high = []
    with open(file_name) as input_file:
        lines = input_file.readlines()
        for line in lines[1:]:
            line = line.rstrip(os.linesep)
            if line:
                fields = line.split()
                incorrect.append(float(fields[0]))
                acceptable.append(float(fields[1]))
                medium.append(float(fields[2]))
                high.append(float(fields[3]))
    return incorrect, acceptable, medium, high


if __name__ == "__main__":

    # Read results information
    results = {}
    for figure in figures:
        result_file = os.path.join('.', "{}.list".format(figure))
        incorrect, acceptable, medium, high = read_ranking_file(result_file)
        results[figure] = {'incorrect': incorrect,
                            'acceptable': acceptable,
                            'medium': medium,
                            'high': high}

    box = plt.figure(1, figsize=(18, 6), dpi=300, facecolor='w', edgecolor='k')
    plt.rcParams.update({'font.size': 12})
    titles = {'BLIND': r'$BLIND$', 'TI': r'$TI$', 'CDR': r'$CDR$'}

    for i, figure in enumerate(figures):
        
        ax = plt.subplot(131+i)
        N = 6
        ind = np.arange(N)
        acceptable = [x * 100. for x in results[figure]['acceptable']]
        medium = [x * 100. for x in results[figure]['medium']]
        high = [x * 100. for x in results[figure]['high']]
        width = 0.7

        medium = [(x + y) for x, y in zip(medium, high)]
        acceptable = [(x + y) for x, y in zip(acceptable, medium)]

        p1 = plt.bar(ind, high, width=width, color='#559d3f', zorder=4)
        p2 = plt.bar(ind, medium, width=width, color='#b2df8a', zorder=3)
        p3 = plt.bar(ind, acceptable, width=width, color='#a6cee3', zorder=2)

        plt.ylabel('Success Rate')
        try:
            plt.title(titles[figure])
        except:
            pass
        plt.xticks(ind, ('T1', 'T5', 'T10', 'T20', 'T50', 'T100'))
        plt.ylim([0., 100.])
        plt.yticks(np.arange(0.0, 110.0, 20.0))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.yaxis.grid(which='major', color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.85, wspace=0.4, hspace=0.6)
    plt.figlegend( ['High', 'Medium', 'Acceptable'], loc = 'lower center', ncol=3, labelspacing=0.)
    plt.savefig('figure_sup_1.pdf', bbox_inches='tight')
        
