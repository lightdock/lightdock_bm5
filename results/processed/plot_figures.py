#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os


figures = ["BLIND", "TI-REC", "TI", 
           "TI-SINGLE", "TI-REC-50", "TI-50",
           "TI-RANDOM-25", "TI-REC-25", "TI-25"]

with_std = ["TI-REC-50", "TI-REC-25", "TI-50", "TI-25"]


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
                if with_std:
                    incorrect.append([float(fields[0].split(',')[0]),
                                       float(fields[0].split(',')[1])])
                    acceptable.append([float(fields[1].split(',')[0]),
                                       float(fields[1].split(',')[1])])
                    medium.append([float(fields[2].split(',')[0]),
                                       float(fields[2].split(',')[1])])
                    high.append([float(fields[3].split(',')[0]),
                                       float(fields[3].split(',')[1])])
                else:
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
        incorrect, acceptable, medium, high = read_ranking_file(result_file, figure in with_std)
        results[figure] = {'incorrect': incorrect,
                            'acceptable': acceptable,
                            'medium': medium,
                            'high': high}

    box = plt.figure(1, figsize=(16, 10), dpi=300, facecolor='w', edgecolor='k')
    plt.rcParams.update({'font.size': 12})
    titles = {'BLIND': r'$BLIND$', 'TI': r'$TI$',
              'TI-25': r'$TI_{25}$', 'TI-50': r'$TI_{50}$', 
              'TI-SINGLE':r'$TI_{SINGLE}$', 'TI-REC':r'$TI_{REC}$',
              'TI-RANDOM-25': r'$TI_{RANDOM-25}$', 'TI-REC-50':r'$TI_{REC-50}$', 
              'TI-REC-25':r'$TI_{REC-25}$'}

    for i, figure in enumerate(figures):
        
        ax = plt.subplot(331+i)
        N = 6
        ind = np.arange(N)
        if figure in with_std:
            acceptable = [x[0] * 100. for x in results[figure]['acceptable']]
            medium = [x[0] * 100. for x in results[figure]['medium']]
            high = [x[0] * 100. for x in results[figure]['high']]
        else:
            acceptable = [x * 100. for x in results[figure]['acceptable']]
            medium = [x * 100. for x in results[figure]['medium']]
            high = [x * 100. for x in results[figure]['high']]
        width = 0.7

        medium = [(x + y) for x, y in zip(medium, high)]
        acceptable = [(x + y) for x, y in zip(acceptable, medium)]

        if figure in with_std:
            std = [x[1] * 100. for x in results[figure]['high']]
            p1 = plt.bar(ind, high, yerr=std, capsize=5, width=width, ecolor='grey', color='#559d3f', zorder=-2)
            std = [x[1] * 100. for x in results[figure]['medium']]
            p2 = plt.bar(ind, medium, yerr=std, capsize=5, width=width, ecolor='grey', color='#b2df8a', zorder=-3)
            std = [x[1] * 100. for x in results[figure]['acceptable']]
            p3 = plt.bar(ind, acceptable, yerr=std, capsize=5, width=width, ecolor='grey', color='#a6cee3', zorder=-4)
        else:
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

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.6)
    plt.figlegend( ['High', 'Medium', 'Acceptable'], loc = 'lower center', ncol=3, labelspacing=0.)
    plt.savefig('figure.pdf', bbox_inches='tight')
        
