from pystac_client import Client
import matplotlib.pyplot as plt
import rioxarray as rxr
import matplotlib as plt
import numpy as np

__all__ = ['search_api', 'normalize']

def search_api(datetime, point):
    catalog = Client.open("https://earth-search.aws.element84.com/v1")
        
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        intersects=point,
        datetime=datetime,
        )

    items = search.item_collection()
    print(len(items))
    
    return items

def normalize(array): 
    array_max = array.max() 
    array_min = array.min()
    return ((array-array_min)/(array_max-array_min))

    
