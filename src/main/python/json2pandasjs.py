# -*- coding:utf-8 -*-
import pandas as pd
import json
import re


def json2pandasjs(file):
    df = pd.DataFrame()
    with open(file) as f:
        line = f.readline()
        while line:
            strinfo = re.compile('null')
            datare = strinfo.sub('None', line)
            data = eval(datare)
            tmp = pd.DataFrame(data=data, index=range(1))
            df = df.append(tmp)
            line = f.readline()
    df = df.set_index(df['first_visit_time'])
    df = df.sort_index(ascending=False)
    return df