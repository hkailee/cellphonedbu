import itertools
from functools import partial
from multiprocessing.pool import Pool

import numpy as np
import pandas as pd
from scipy.stats import mstats
import sys

from cellphonedb.src.core.core_logger import core_logger


def build_clusters(meta: pd.DataFrame, counts: pd.DataFrame) -> dict:
    """
    Builds a cluster structure and calculates the means values
    """
    cluster_names = meta['cell_type'].drop_duplicates().tolist()
    clusters = {'names': cluster_names, 'counts': {}, 'means': {}}

    def mstats_winsorizer(s):
        return mstats.winsorize(s, limits=[0, 0.05])

    def WinsorizeSampleList(data):
        # quantiles = data.quantile([0.95])
        # q_05 = quantiles.loc[0.05]
        # q_95 = quantiles.loc[0.95]

        quantiles = data.quantile([0.25, 0.75])
        q_25 = quantiles.loc[0.25]
        q_75 = quantiles.loc[0.75]
        step = (q_75 - q_25) * 1.5
        # return data[(data.values >= q_05) & (data.values <= q_95)]
        return data[(data.values >= q_75 + step)]


    cluster_counts = {}
    cluster_means = {}

    for cluster_name in cluster_names:
        cells = meta[meta['cell_type'] == cluster_name].index
        cluster_count = counts.loc[:, cells]
        cluster_count.to_csv('/Volumes/Samsung_T3/SIgN/cellphonedbv/out/WinsorizeSampleList/' + \
                                                                cluster_name + '_ori.csv')
        cluster_count.apply(WinsorizeSampleList, axis=1).to_csv('/Volumes/Samsung_T3/SIgN/cellphonedbv/out/WinsorizeSampleList/' + \
                                                                cluster_name + '_top95.csv')
        winsorized_cluster_count_array = cluster_count.apply(mstats_winsorizer, axis=1)
        winsorized_cluster_count = pd.DataFrame.from_records(winsorized_cluster_count_array, \
                                        index=cluster_count.index, columns=cluster_count.columns)
        winsorized_cluster_count.to_csv('/Volumes/Samsung_T3/SIgN/cellphonedbv/out/WinsorizeSampleList/' + \
                                                                cluster_name + '_winsorized.csv')
        cluster_counts[cluster_name] = winsorized_cluster_count

    clusters['counts'] = cluster_counts
    print(clusters)
    return clusters


