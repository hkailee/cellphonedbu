from setuptools import setup, find_packages

setup(
    name='CellPhoneDBu',
    author='Lee Hong Kai',
    author_email='leehongkai@gmail.com',
    version='1.1.1.2',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    exclude_package_data={'': ['tools']},
    entry_points={
        'console_scripts':
            [
                'cellphonedbu = cellphonedb.cellphonedb_cli:cli'
            ]
    },
    install_requires=[
        'click>=6.7,<6.7.99',
        'dask==1.1.4',
        'numpy==1.22.0',
        'pandas>=0.23,<0.23.99',
        'PyYAML>=3.13,<3.13.99',
        'scipy==1.2.1',
    ],
)
