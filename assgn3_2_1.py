import netCDF4
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fig = plt.figure(figsize=(16,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])

nc = netCDF4.Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/trmm_3hourly')
rain_rate= nc.variables['rr']
rain_rate_s = rain_rate[41383,:,:]

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

m = Basemap(llcrnrlat=-50.,llcrnrlon=-179.9,\
            urcrnrlat= 50,urcrnrlon=179.9,\
            projection='mill',resolution = 'h')
            
parallels = np.arange(-60.,60.,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-180.,180.,60.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

ny = rain_rate_s.shape[0]; nx =rain_rate_s.shape[1]
lons, lats = m.makegrid(nx, ny)

x, y = m(lons, lats)
clevs = [0,0.1,0.2,0.3,0.4,0.6,0.8,1.0,1.5,1.9,2.3,2.7,3.1,3.5,3.9,4.3]

cdict = {'red': ((0., 1, 1),
                 (0.05, 1, 1),
                 (0.11, 0, 0),
                 (0.66, 1, 1),
                 (0.89, 1, 1),
                 (1, 0.5, 0.5)),
         'green': ((0., 1, 1),
                   (0.05, 1, 1),
                   (0.11, 0, 0),
                   (0.375, 1, 1),
                   (0.64, 1, 1),
                   (0.91, 0, 0),
                   (1, 0, 0)),
         'blue': ((0., 1, 1),
                  (0.05, 1, 1),
                  (0.11, 1, 1),
                  (0.34, 1, 1),
                  (0.65, 0, 0),
                  (1, 0, 0))}
                  
                
my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
cs = m.contourf(x,y,rain_rate_s,clevs,cmap= my_cmap)

m.drawcoastlines()

cbar = m.colorbar(cs,location='bottom',pad="10%")
cbar.set_label('hourly rain rate(mm/hr)')
plt.title('TRMM 3B42 V6 three_hourly merged rainfall at 21z29feb2012')

plt.show()
plt.savefig('plot_graph_TRMM2012022921z.pdf')
