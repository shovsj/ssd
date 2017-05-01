from setuptools import setup

setup(name='ssd',
      version='0.1',
      description='Single Shot Detector',
      url='http://github.com/tensorpro/ssd',
      packages=['ssd', 'nets', 'preprocessing', 'tf_extended'],
      install_requires=[
        'numpy',
        'tensorflow',
    ],
      zip_safe=False)
