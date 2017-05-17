# About

This is a little Python 2.7 module to plot geographic coordinates on a map using [Matplotlib](https://matplotlib.org/). It fetches retina raster maps from [Mapbox](https://www.mapbox.com/). Before publishing any plots created with it, please consult the Mapbox [print policy](https://www.mapbox.com/help/print-policy/) and [attribution policy](https://www.mapbox.com/help/attribution/). I wrote the code for usage in my own work as a PhD student. You can probably adapt the code easily to use with other map services. The code is written in way that assumes interactive use and tries hence not to be bullet proof. Feel free to send me pull requests. The main reason to choose Mapbox as service was, that they provide retina tiles, which is really nice for use in print (scientific publications for my part). 

# Usage

## Dependcies

The module is written for being used with  [Matplotlib](https://matplotlib.org/), so you will need to have it installed alongside with [Numpy](http://www.numpy.org/). 

## Getting Started

Start by having a look at `test.py`. First you need to create a Mapbox account and [create an api token](https://www.mapbox.com/help/create-api-access-token/). Put the key in a text file `api_token.txt` in your working directory. Once you have done that, you should be able to run the script and see a map with a route from Stockholm to Gothenburg in Sweden. You can choose your preferred map style by changing the value of `map_type`. Look [here](https://www.mapbox.com/api-documentation/#styles) for documentation on different styles and [here](https://www.mapbox.com/api-documentation/#static) for documentation on the Mapbox api.

I use the abbreviations `lat` for latitude and `lon` for longitude throughout. 

There are three public functions

* `get_map_config(xref,yref,lat_min,lat_max,lon_min,lon_max)`
 computes the configuration (a dictionary) of the map plot, where `xref` and `yref` set width and hight of the plot that will be created in pixels, `lat_min` ,`lat_max`, `lon_min` ,`lon_max` specify the area that is shown. They are provided in degrees. 
* `get_figure(api_token,map_type,map_config,[scale_config])` 
creates a Matplotlib figure object with the map plotted as an image. `api_token` is your Mapbox api token, `map_type` is a string that specifies the [map style](https://www.mapbox.com/api-documentation/#styles). `map_config` is the map configuration computed with `get_map_config`. `scale_config` is an optional parameter that configures the size and position of an optional map scale in the upper left corner. It is dictionary with following optional keys. `offset_x` and `offset_y` configures the offset in pixels from the left and top respectively. With `text_offset_x`, `text_offset_y` you can control the relative position of text that shows the length of the scale. The `real_length` parameter gives the real length of the scale shown in meters. If a parameter is not provided, the script will use default values. In order to fetch the image, internet connection is required.
* `transform_data(lat,lon,map_config)` 
is used to transform the numpy arrays `lat` and `lon` with geographical coordinates into a tuple `(x,y)`, where `x` is a numpy array with x-coordinates and `y` a numpy array with y-coordinates to used for plotting the corresponding values of `lat` and `lon` on the correct position on the figure object created by `get_figure`, that was created with the same map configuration `map_config`. Now you can use all the plotting functions matplotlib provides. 

# Known quirks

* Sometimes it is necessary to adjust the `y` value by a pixel or so to get perfect alignment with the map. I don't know why that's the case. Probably some rounding issues.
* The logic how the map scale is shown is very basic and only supports kilometers. For other measurement units either fix in the code or write it properly and send me pull request.

# Other details

* The map uses Mercator projection. Note that this does not work above close to the poles. Check the [Wikipedia](https://en.wikipedia.org/w/index.php?title=Web_Mercator&oldid=767735687) article for details. 