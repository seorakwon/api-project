#!/usr/bin/env python

from bottle import route, run, get, post, request
import random
from mongo1 import CollConection
import bson
from bson.json_util import dumps
from populate import db, coll
import json
import requests
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from functools import reduce
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


