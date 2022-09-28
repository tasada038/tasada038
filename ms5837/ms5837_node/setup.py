import os
from glob import glob

from setuptools import setup

package_name = 'ms5837_node'
submodules = 'ms5837_node/ms5837'

# build a list of the data files
data_files = []
data_files.append(("share/ament_index/resource_index/packages", ["resource/" + package_name]))
data_files.append(("share/" + package_name, ["package.xml"]))

def package_files(directory, data_files):
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            data_files.append(("share/" + package_name + "/" + path, glob(path + "/**/*.*", recursive=True)))
    return data_files

data_files = package_files('launch/', data_files)


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fish2',
    maintainer_email='fish2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bar30_node = ms5837_node.ms5837_node:main',
            'convert_depth_data = ms5837_node.convert_depth_data:main',
        ],
    },
)
