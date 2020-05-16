#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:23:59 2020

@author: elisaluo
"""

#TODO: fix formatting of date and legend.

import pandas as pd
import matplotlib.pyplot as plt

#PARSE THE DATA!
train = pd.read_csv("train.csv")
train["date"] = pd.to_datetime(train["date"])

adj_dist = []

for i in range(0,len(train["mode"])):
    if train["mode"][i] == "bike":
        adj_dist.append(train["distance"][i]*0.5)
    elif train["mode"][i] == "run":
        adj_dist.append(train["distance"][i]*1.5)
    else:
        adj_dist.append(train["distance"][i])
        
train["adj_dist"] = adj_dist

########################################################

#GROUP BY DATE AND DISTANCE
dist_by_date = train[["date","mode","distance"]].groupby(["date","mode"]).sum()
dist_by_date = dist_by_date.unstack()
dist_by_date.plot.bar(stacked = True)

#GROUP BY DATE AND ADJUSTED DISTANCE
dist_by_date = train[["date","mode","adj_dist"]].groupby(["date","mode"]).sum()
dist_by_date = dist_by_date.unstack()
dist_by_date.plot.bar(stacked = True)


#GROUP BY DATE AND TIME_ELAPSED
agg = train[["date","mode","time_elapsed"]].groupby(['date','mode']).sum()
new = agg.unstack()
new.plot.bar(stacked = True)

########################################################
#PIE GRAPH SECTION!

#GROUP BY MODE AND TIME_ELAPSED
mode_per_time = train[["mode", "time_elapsed"]].groupby("mode").sum()
mode_per_time.plot.pie(subplots=True, figsize = (6,6))


#GROUP BY MODE AND DISTANCE!
mode_per_dist = train[["mode", "distance"]].groupby("mode").sum()
mode_per_dist.plot.pie(subplots=True, figsize = (6,6))

#MODE AND ADJUSTED DISTANCE
adj_mode_per_dist = train[["mode","adj_dist"]].groupby("mode").sum()
adj_mode_per_dist.plot.pie(subplots=True, figsize = (6,6))

    


########################################################
#TOTALS & AVERAGES SECTION!

#TOTAL MINUTES

#TOTAL DISTANCE

#AVERAGE MINUTES/DAY
