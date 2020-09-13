import pandas as pd
import geopandas as gpd
import plotly_express as px
import matplotlib.pyplot as plt


df = pd.read_csv('data/go_track_trackspoints_edited.csv')
gdf = gpd.GeoDataFrame( df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
px.set_mapbox_access_token('pk.eyJ1Ijoic2hha2Fzb20iLCJhIjoiY2plMWg1NGFpMXZ5NjJxbjhlM2ttN3AwbiJ9.RtGYHmreKiyBfHuElgYq_w')

polygon = gpd.read_file('data/CENTERAREA.geojson')
mask = (polygon.loc[0, 'geometry'])
pip_mask_geofence = gdf.within(mask)

gdf.loc[:,'geofence'] = pip_mask_geofence
gdf['geofence'] = gdf['geofence'].replace({True: 'In', False: 'Out'})
print(gdf)
fig = px.scatter_mapbox(gdf, 
                lat='latitude_edit', lon='longitude_edit', 
                color='type', 
                size='track_id', 
                animation_frame='time', 
                animation_group='track_id',
                size_max=10, 
                zoom=12, 
                text='altitude',
                width=1200, 
                height=800)

fig.show()