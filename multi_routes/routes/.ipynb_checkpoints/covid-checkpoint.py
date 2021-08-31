# -*- coding: utf-8 -*-

import calendar
from datetime import datetime
from collections import namedtuple
import re
import sys
import time
import json
import requests

import numpy as np
import pandas as pd

        
def run_dataframe(data):
    print("------------------------ In Predict Function ------------------------")
    model = load_model()
    response = model.predict(data)
    
    url = json.loads(data[0]["body"].decode("utf-8"))["url"]
    x = requests.get(url)
    df = pd.DataFrame(json.loads(x.text)["cases_time_series"])
    df["response"] = response
    
    return df

