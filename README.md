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

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Write nwb file
with NWBHDF5IO('test_pointcloudseries.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_pointcloudseries.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb)
```
