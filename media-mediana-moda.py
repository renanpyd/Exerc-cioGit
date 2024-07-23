# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:35:08 2023
@author: renan
"""

import statistics

ls = [10, 20, 30, 40, 40, 50]


media = statistics.mean(ls)
mediana = statistics.median(ls)
moda = statistics.mode(ls)
print("Média: ", media)
print("Mediana: ", mediana)
print("Moda: ", moda)

