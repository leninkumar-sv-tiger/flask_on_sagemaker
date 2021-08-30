# -*- coding: utf-8 -*-

import calendar
from datetime import datetime
from collections import namedtuple
import re
import sys
import time

import numpy as np
import pandas as pd

PY3 = sys.version_info[0] == 3
if PY3:
    string_types = str,
    text_type = str
    long_type = int
else:
    string_types = basestring,
    text_type = unicode
    long_type = long

        
def run_dataframe(data):
    print("------------------------ In Predict Function ------------------------")
    return pd.DataFrame(
                    [["a", "b"], ["x", "v"]],
                    index=["row 1", "row 2"],
                    columns=["col 1", "col 2"],
                )
