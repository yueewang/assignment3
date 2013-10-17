import netCDF4
from datetime import datetime
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])

nc = netCDF4.Dataset('3B42.20130530.00.7.nc')
prep= nc.variables['pcp']
prep_s = prep[0,:,:]

lon = nc.variables['longitude'][:]
lat = nc.variables['latitude'][:]


m = Basemap(llcrnrlat=-50.,llcrnrlon=-179.9,\
            urcrnrlat= 50,urcrnrlon=179.9,\
            projection='mill',resolution = 'l')
                      
parallels = np.arange(-50.,50.,15.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-180.,180.,60.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
            
ny = prep_s.shape[0]; nx =prep_s.shape[1]
lons, lats = m.makegrid(nx, ny)

x, y = m(lons, lats)
clevs = [0,1,2.5,5,7.5,10,15,20,30,40,50,70,100,150,200,250,300,400,500,600,750]
cs = m.contourf(x,y,prep_s,clevs,cmap=cm.s3pcpn)
m.drawcoastlines()

cbar = m.colorbar(cs,location='bottom',pad="10%")
cbar.set_label('mm')

plt.title('TRMM based rainfall at 2013050100z')
plt.show()
plt.savefig('plot_graph_TRMM2013050100.pdf')


