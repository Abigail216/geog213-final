import rioxarray as rxr

from pystac_client import Client
__all__ = ['FindBoxScene','gen_stac_asset_urls', 'reproject_and_mosaic']

def FindBoxScene(datetime, bbox):
    catalog = Client.open("https://earth-search.aws.element84.com/v1")
    
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=bbox,
        datetime=datetime, 
        query=["eo:cloud_cover<5", "s2:snow_ice_percentage<5"]
    )

    items = search.get_all_items()
    print(len(items))
    
    return items


def gen_stac_asset_urls(items, asset):
    """
    This function receives an items collection returned by a STAC API, and returns
    the urls of the requested `asset` in a list. 
    """
    urls = []
    for item in items:
        urls.append(item.assets[asset].href)
    return urls



def reproject_and_mosaic(items, band_name, epsg=5070):
   """
   Reproject and mosaic Sentinel-2 tiles for a given time period
   
   Parameters:
   items : list of STAC items from FindBoxScene
   band_name : str ('red', 'green', or 'blue')
   epsg : int (default 5070 to match CDL data)
   
   Returns:
   mosaic : reprojected and mosaicked raster
   """
   # Get URLs for the band
   urls = gen_stac_asset_urls(items, band_name)
   
   # Create reprojected datasets
   datasets = []
   for url in urls:
       ds = rxr.open_rasterio(url, lock=False, chunks=(1, 'auto', -1))
       ds_reprojected = ds.rio.reproject(f'EPSG:{epsg}')
       datasets.append(ds_reprojected.to_dataset(name=band_name))
   
   # Create mosaic
   mosaic = merge_datasets(datasets)
   
   return mosaic


