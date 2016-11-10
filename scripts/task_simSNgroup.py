#!/usr/bin/env python
"""
simulate splits
"""
import argparse
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from snsims import EntireSimulation
import time

parser = argparse.ArgumentParser(description='Simulate the SN in params file using the Opsim pointings')
parser.add_argument('paramFile', type=str, help='parameter File for SN')
parser.add_argument('OpSimDBPath', type=str, help='absolute path to  OpSim Database')
parser.add_argument('--outfile', type=str, help='absolute path to outfile')
parser.add_argument('--logfile', type=str, help='absolute path to logfile')
args = parser.parse_args()
engine = create_engine('sqlite:///' + args.OpSimDBPath)
def simulate_SN(paramFile, pointings, outfile, logfile):
    tstart = time.time()
    print(paramFile)
    i = int(paramFile.split('_')[-1].split('.')[0])
    print(i)
    snpars = pd.read_csv(paramFile)
    snparamdf = snpars
    es = EntireSimulation(rng=np.random.RandomState(200+i), 
                          pointings=pointings, paramsDF=snparamdf)
    filename = outfile
    logfile = logfile
    snids = snparamdf.index.values
    for j, snid in enumerate(snids):
        es.writeSN(snid, filename, IDVal=0)
        if j % 50 == 0:
            print('time is {0} for {1} SN in split {2}'.format(time.time() - tstart, j, i))
            with open(logfile, 'w') as lf:
                lf.write('Written {} lightcurves'.format(i))
    tend = time.time()
    return tend - tstart

pts = pd.read_sql_query('SELECT * FROM Summary WHERE FieldID == 1427', engine)
pts.drop_duplicates(subset='obsHistID', inplace=True)
outhdf = args.outfile
logfile = args.logfile
simulate_SN(args.paramFile, pts, outhdf, logfile)
