from pystac_client import Client
import matplotlib.pyplot as plt

__all__ = ['search_api']

def search_api(datetime, point)
    catalog = Client.open("https://earth-search.aws.element84.com/v1")
        
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        intersects=point,
        datetime=datetime,
        query=["eo:cloud_cover<5", "s2: snow_and_ice_percentage<5"
        )

    return search.matched()


def gen_stac_asset_urls(items, asset):
    """
    This function receives an items collection returned by a STAC API, and returns
    the urls of the requested `asset` in a list. 

    Inputs:
        items : json collection
            A STAC items collection returned by STAC API
        asset : string
            Name of an asset present in the `items` collection

    Returns:
        urls : list
            List of all usls related to the `asset`
            
    """
    
    urls = []
    for item in items:
        urls.append(item.assets[asset].href)
    
    return urls

def gen_map(band1, band2, selected_pre_image, selected_post_image):
    assets_pre = selected_pre_image.assets
    assets_post = selected_post_image.assets
    
    nir_pre_href = assets_pre[band1].href
    print(nir_pre_href)

    swir_pre_href = assets_pre[band2].href
    print(swir_pre_href)

    nir = rxr.open_rasterio(nir_pre_href)
    plt.imshow(nir[0,:,:], cmap="magma_r")
    