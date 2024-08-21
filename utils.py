import json
from urllib import request, response
import logging

def format_results(results):

    results = results.json()
    
    return results