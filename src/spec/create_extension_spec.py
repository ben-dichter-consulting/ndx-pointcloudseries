from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec
from pynwb.base import TimeSeries


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing time-varying 3D point clouds',
                                     name='ndx-pointcloudseries',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    PointCloudSeries = NWBGroupSpec(
        doc='type for storing time-varying 3D point clouds',
        neurodata_type_def='PointCloudSeries',
        neurodata_type_inc='TimeSeries',
        )

    PointCloudSeries.add_dataset(
        name='data',
        doc='datapoints locations over time',
        dims=('time', '[x, y, z]'),
        shape=(None, 3),
        dtype='float',
        quantity='?'
    )


# PointCloudSeries (inherits from TimeSeries)
#     data_index (VectorIndex)
#         targets data
#     data (VectorData)
#         shape: (None, 3)
#         dims: ('time', 'x,y,z')
#     color (VectorData)
#         shape: (None , 3)
#         dims: ('time', 'r,g,b')
#         quantity: '?'
#     color_index (VectorIndex) [same as data_index]
#         targets color
#         quantity: '?'

    new_data_types = [PointCloudSeries]

    ns_builder.include_type('PointCloudSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
