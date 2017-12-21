# -*- coding:utf-8 -*-
import pandas as pd
import json


def json2pandas(file):

    columns = ["zg_id", "first_utm_content", "name", "current_app_version", "first_utm_term", "current_area",
              "current_resolution_h", "avatar", "first_channel", "first_version", "current_mccmnc","duration",
              "用户ID", "current_country", "current_os", "用户名称", "current_city", "等级", "last_visit_time",
              "current_resolution_l", "gender", "first_utm_medium", "first_utm_source", "current_device_model",
              "first_visit_time", "visit_times", "first_utm_campaign", "current_app_channel", "current_device_brand",
              "current_ov", "app_user_id", "is_anonymous"]
    df = pd.DataFrame(columns=columns)
    with open(file) as f:
        line = f.readline()
        while line:
            n = 1
            data = eval(line)
            tmp = pd.DataFrame(data, columns=data.keys(), index=range(n))
            df = df.append(tmp)
            line = f.readline()
    #df = df.set_index(df['zg_id'])
    return df