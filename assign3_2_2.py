import netCDF4
import matplotlib.pyplot as plt
import pandas as pd


nc = netCDF4.Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/trmm_3hourly')

time = nc.variables['time']
rain_rate_t = nc.variables['rr'][:,320,240]

data_range = pd.date_range('1/1/1998',periods= rain_rate_t.size, freq='3H')
ts = pd.Series(rain_rate_t,index = data_range)

ts.plot(figsize=(16.0, 8.0),legend = False)
plt.title('Time series of rain rate(3 Hours) from 1998010100z to 2012022921Z for 25N120W')
plt.xlabel('Time (year)')
plt.ylabel('Rain rate (mm)')
plt.ylim(0,12)

plt.show()
plt.savefig('ts_trmm.pdf')


