#!/usr/bin/env python3

import numpy as np
import os
import sys


def read_data(file_name):
    data = {'1':[],
            '5':[],
            '10':[],
            '20':[],
            '50':[],
            '100':[],
           }
    with open(file_name) as handle:
        lines = handle.readlines()
        data['1'] = [float(x) for x in lines[1].split()]
        data['5'] = [float(x) for x in lines[2].split()]
        data['10'] = [float(x) for x in lines[3].split()]
        data['20'] = [float(x) for x in lines[4].split()]
        data['50'] = [float(x) for x in lines[5].split()]
        data['100'] = [float(x) for x in lines[6].split()]
    return data


if __name__ == "__main__":

    case = sys.argv[1]
    num_runs = int(sys.argv[2])

    rankings = []
    for run in range(num_runs):
        run_file = os.path.join('.', "{}-run{}.list".format(case, run))
        data = read_data(run_file)
        rankings.append(data)

    tops = {}
    tops['1'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}
    tops['5'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}
    tops['10'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}
    tops['20'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}
    tops['50'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}
    tops['100'] = {'incorrect':[], 'acceptable':[], 'medium':[], 'high':[]}

    for run in range(num_runs):
        for top in ['1','5','10','20','50','100']:
            tops[top]['incorrect'].append(rankings[run][top][0])
            tops[top]['acceptable'].append(rankings[run][top][1])
            tops[top]['medium'].append(rankings[run][top][2])
            tops[top]['high'].append(rankings[run][top][3])

    print('#Incorrect  Acceptable  Medium  High')
    for top in ['1','5','10','20','50','100']:
        print("{:f},{:f}  {:f},{:f}  {:f},{:f}  {:f},{:f}".format(np.mean(tops[top]['incorrect']),
                                                                  np.std(tops[top]['incorrect']),
                                                                  np.mean(tops[top]['acceptable']),
                                                                  np.std(tops[top]['acceptable']),
                                                                  np.mean(tops[top]['medium']),
                                                                  np.std(tops[top]['medium']),
                                                                  np.mean(tops[top]['high']),
                                                                  np.std(tops[top]['high'])))
