from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec

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
        name='point_cloud',
        neurodata_type_inc='VectorData',
        doc='datapoints locations over time',
        dims=('time', '[x, y, z]'),
        shape=(None, 3),
        dtype='float',
        quantity='?'
    )

    PointCloudSeries.add_dataset(
        name='point_cloud_index',
        neurodata_type_inc='VectorIndex',
        doc='datapoints indices',
        dims=('index',),
        shape=(None),
        quantity='?'
    )

    PointCloudSeries.add_dataset(
        name='color',
        neurodata_type_inc='VectorData',
        doc='datapoints color',
        dims=('time', '[r, g, b]'),
        shape=(None, 3),
        dtype='float',
        quantity='?'
    )

    PointCloudSeries.add_dataset(
        name='color_index',
        neurodata_type_inc='VectorIndex',
        doc='datapoints colors indices',
        dims=('index',),
        shape=(None),
        quantity='?'
    )

    new_data_types = [PointCloudSeries]

    ns_builder.include_type('TimeSeries', namespace='core')
    ns_builder.include_type('VectorData', namespace='core')
    ns_builder.include_type('VectorIndex', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
