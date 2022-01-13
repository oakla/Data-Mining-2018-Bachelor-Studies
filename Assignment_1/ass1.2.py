#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:55:33 2018

@author: aoakley
"""

import numpy as np
import pandas as pd

df =pd.read_excel('./Data/nanonose.xls', sheet_name='Sheet1')

print(df)

df.head()

df['A']