import pandas as pd

from cellphonedb.src.core.exceptions.EmptyResultException import EmptyResultException
from cellphonedb.src.core.methods import cpdb_statistical_analysis_simple_method


def call(meta: pd.DataFrame,
         count: pd.DataFrame,
         threads: int,
         debug_seed: int,
         result_precision: int
         ) -> (pd.DataFrame):
    winsorized = \
        cpdb_statistical_analysis_simple_method.call(meta.copy(),
                                                     count.copy(),
                                                     threads,
                                                     debug_seed,
                                                     result_precision)

    return winsorized
