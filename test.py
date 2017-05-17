# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import numpy as np
import matplotlib.pyplot as plt
import map_plotter as mp
 
# Configuration 
 
map_type = 'light-v9'

xref = 400
yref = 300

scale_config = {'offset_x':20,'offset_y':20,
                'text_offset_x':20,'text_offset_y':25,'real_length':100e3}
    
# if you want to use default parameters, uncomment            
#scale_config = {}
                
with open('api_token.txt','r') as f_token:
  api_token = f_token.readline().rstrip() # doesn't work rstrip(), probably EOF that creates trouble

# Load som test data and plot it on the map
with open('./testdata.json','r') as f:
  data = json.load(f)

lat = np.array(data['lat'])
lon = np.array(data['lon'])

# Create the map configuration
map_config = mp.get_map_config(xref,yref,lat.min(),lat.max(),lon.min(),lon.max())

# Create a matplotlib figure object with the map
fig = mp.get_figure(api_token,map_type,map_config,scale_config)
# To get rid of the scale use instead
#fig = mp.get_figure(api_token,map_type,map_config)

# This function tranforms the data so it can be plotted on fig with the regular
# matplotlib plotting functions
x,y = mp.transform_data(lat,lon,map_config)
fig.gca().plot(x,y)

plt.show()