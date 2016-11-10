#!/usr/bin/env python
"""
if 
"""
import os
import numpy as np
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='split a SN parameter file into files with approximately equal numbers')
parser.add_argument('paramFile', type=str, help='csv file with parameters of SN')
parser.add_argument('--numSplits', default=400, type=int, help='number of splits') 
parser.add_argument('--dirName', default='data/split_files', type=str,
                    help='directory in which the split files are kept')
args = parser.parse_args()

snParamsAll = pd.read_csv(args.paramFile).set_index('snid')
snpars = np.array_split(snParamsAll, args.numSplits)

if not os.path.exists(args.dirName):
    os.makedirs(args.dirName)
for i, snpar in enumerate(snpars):
    fname  = os.path.join(args.dirName, 'snpar_{}.csv'.format(i))
    snpar.to_csv(fname)
