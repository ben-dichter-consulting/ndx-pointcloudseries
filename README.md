# ndx-pointcloudseries extension for NWB:N

NWB extension of the [TimeSeries](https://pynwb.readthedocs.io/en/stable/pynwb.base.html#pynwb.base.TimeSeries) class that accommodates time-varying 3D point clouds.

[![PyPI version]()

[Python Installation](#python-installation)

[Python Usage](#python-usage)

### Python Installation
```bash
pip install git+https://github.com/ben-dichter-consulting/ndx-pointcloudseries.git
```

### Python Usage

```python
from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from ndx_pointcloudseries import PointCloudSeries
from hdmf.common.table import VectorIndex, VectorData

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

data = [[1., 1., 1.], [2., 2., 2.], [1., 2., 1.]]
data_vect = VectorData(name='points', description='desc', data=data)

indexes = [2, 3]
data_ind = VectorIndex(name='indexes', data=indexes, target=data_vect)

pcs = PointCloudSeries(
        name='PointCloudSeries',
        point_cloud=data_vect,
        point_cloud_index=data_ind,
        rate=10.
    )
nwb.add_acquisition(pcs)
print(nwb.acquisition['PointCloudSeries'])

# Write nwb file
with NWBHDF5IO('test_pointcloudseries.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_pointcloudseries.nwb', 'r') as io:
    nwb = io.read()
    print(nwb.acquisition['PointCloudSeries'])
```
