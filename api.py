# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:38:26 2021

@author: Harini
"""

pip install transformers[torch]
from transformers import pipeline
senti_pipeline=pipeline("sentiment-analysis")
senti-pipeline("i am happy")