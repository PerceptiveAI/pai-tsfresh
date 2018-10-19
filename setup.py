import unittest
from setuptools import setup, find_packages


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


if __name__ == '__main__':
    setup(name='pai_tsfresh',
          version='0.1.0',
          url='https://github.com/PerceptiveAI/pai-tsfresh.git',
          description='PerceptiveAI frok for tsfresh',
          license='Private proprietary code of Perceptive AI ltd.',
          # package_dir={'': 'pai_common'},
          # packages=find_packages(where='pai_common'),
          packages=find_packages(),
          package_data={'': ['*.*']},
          install_requires=['scikit-learn==0.20.0',
                            'dask==0.19.4', 'numpy==1.15.0',
                            'pandas==0.23.4', 'requests==2.19.1',
                            'scipy==1.1.0', 'statsmodels==0.8.0',
                            'patsy==0.4.1', 'future==0.16.0',
                            'six==1.11.0', 'tqdm==4.10.0',
                            'ipaddress==1.0.18',
                            'distributed==1.18.3'],
          test_suite='setup.my_test_suite')
