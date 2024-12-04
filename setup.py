from setuptools import setup, find_packages

setup(
    name='udp_latency',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'udp-latency=udp_latency.udp_latency:main',
            'udp-rtt=udp_latency.udp_rtt:main',
        ],
    },
)
