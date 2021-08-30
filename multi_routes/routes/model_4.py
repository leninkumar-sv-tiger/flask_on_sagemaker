# -*- coding: utf-8 -*-

import calendar
from datetime import datetime
from collections import namedtuple
import re
import sys
import time
import json

import numpy as np
import pandas as pd

        
def run_dataframe(data):
    print("------------------------ In Predict Function ------------------------")
    df = pd.DataFrame(json.loads(data[0]["body"].decode("utf-8")))
    df["Source"] = "From Model 4"
    return df

