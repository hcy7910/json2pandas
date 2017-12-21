# -*- coding:utf-8 -*-
import pandas as pd
import json
import ast


def json2pandases(file):
    df = pd.DataFrame()
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            js = json.dumps(line)
            dt = ast.literal_eval(js)
    return df