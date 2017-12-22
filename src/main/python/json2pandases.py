# -*- coding:utf-8 -*-
import pandas as pd
import re


def json2pandases(file):
    df = pd.DataFrame()
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            data = eval(line)
            yield data
        df = df.append(data)
