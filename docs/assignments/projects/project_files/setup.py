from setuptools import setup
from glob import glob

package_name = ''

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')), # This line for launch files
        ('share/' + package_name + '/data', glob('data/*.txt')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='John Doe',
    maintainer_email='john_doe@mail.com',
    description="This is an example setup file.",
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
