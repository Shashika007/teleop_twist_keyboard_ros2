from setuptools import setup

package_name = 'teleop_twist_keyboard_trio'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shashika',
    maintainer_email='Shashika8596@gmail.com',
    description='teleop keyboard package for ros2 foxy',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = teleop_twist_keyboard_trio.teleop_keyboard:main'
        ],
    },
)
