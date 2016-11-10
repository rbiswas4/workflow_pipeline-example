# workflow_pipeline-example

## Install/Setup

### Requirements 
- sims stack installed
- snsims installed
- opsimsummary installed

### Setup procedure
- choose the eups system (On my computer this is `source ${HOME}/soft/LSST_el_capitan/loadLSST.bash`
- setup lsst_sims -t $USER -t sims
- from top level directory:
    - python scripts/task_runsplit.py data/snparams.csv
    - python scripts/task_simSNgroup.py data/split_files/snpar_200.csv /Users/rbiswas/data/LSST/OpSimData/minion_1016_sqlite.db data/out_200.hdf  data/logfile.txt --summaryDir data/DoneDirs


