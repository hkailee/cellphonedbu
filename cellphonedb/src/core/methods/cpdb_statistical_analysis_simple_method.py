import pandas as pd

from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper
from cellphonedb.src.core.core_logger import core_logger


def call(meta: pd.DataFrame,
         counts: pd.DataFrame,
         threads: int = 4,
         debug_seed: int = -1,
         result_precision: int = 3
         ) -> (pd.DataFrame):
    core_logger.info(
        '[Cluster Statistical Analysis Simple] '
        'Debug-seed:{} Threads:{} Precision:{}'.format(debug_seed,
                                                        threads, 
                                                        result_precision))

    if debug_seed >= 0:
        pd.np.random.seed(debug_seed)
        core_logger.warning('Debug random seed enabled. Setted to {}'.format(debug_seed))

    core_logger.info('Running Winsorization')
    
    winsorized_counts = cpdb_statistical_analysis_helper.build_clusters(meta, counts, threads)

    return build_results(winsorized_counts, result_precision)


def build_results(winsorized_counts: pd.DataFrame,
                  result_precision: int
                  ) -> (pd.DataFrame):
    core_logger.info('Building winsorized results')

    return winsorized_counts.round(result_precision)

