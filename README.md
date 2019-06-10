# CellPhoneDB Utility Tools (CellPhoneDBu)

## What is CellPhoneDBu?
CellPhoneDB Utility Tools improve input data for CellPhoneDB - a publicly available repository of curated receptors, ligands and its interactions. Subunit architecture is included for both ligands and receptors, representing heteromeric complexes accurately. This is crucial, as cell-cell communication relies on multi-subunit protein complexes that go beyond the binary representation used in most databases and studies.

Please refer to [existing repository] (https://github.com/Teichlab/cellphonedb) on how to use the program. 

Utility tools included to date:

1. Winsorizing the count data of each cluster at limit of 0.05 (upper only)
2. Log2-transforming all the count data


### Installing CellPhoneDBu
NOTE: Works with Python v3.5 or superior. If your default Python interpreter is for v2.x (you can check it with `python --version`), calls to `python`/`pip` should be substituted by `python3`/`pip3`.

We highly recommend to use a virtual env (steps 1 and 2) but you can omit.
1. Create python > 3.5 virtual-env
```shell
python -m venv your-venv
```

2. Activate virtual-env
```shell
source your-venv/bin/activate
```

3. Install cellphonedbu
```shell
pip install cellphonedbu
```

### Method optional parameters

~ **Optional Method parameters**:
- `--project-name`: Name of the project. It creates a subfolder in output folder
- `--log2-transform`: Log2-transformed all data in counts [True]
- `--result-precision`: Number of decimal digits in results [3]
- `--output-path`: Directory where the results will be allocated (the directory must exist) [out]
- `--winsorized-result-name`: Winsorized result namefile [winsorized_count.txt]
- `--verbose/--quiet`: Print or hide cellphonedb logs [verbose]

~ **Optional Method Statistical parameters**
- `--debug-seed`: Debug random seed -1 for disable it. >=0 [-1]

**Usage Examples**:

Set number of iterations and threads
```shell
cellphonedbu method winsorizer yourmetafile.txt yourcountsfile.txt --log2-transformed True
```
Set project subfolder
```shell
cellphonedbu method winsorizer yourmetafile.txt yourcountsfile.txt --project-name=new_project
```

Set output path
```shell
mkdir custom_folder
cellphonedbu method winsorizer yourmetafile.txt yourcountsfile.txt --output-path=custom_folder
```

**[DASK] (https://dask.org/) schedulers workflow (auto parallel jobs queue) is incorporated**  
![] (img/grid_search_schedule.gif)