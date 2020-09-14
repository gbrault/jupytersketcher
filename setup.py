from distutils.core import setup
#import pysketcher  # much easier when no lib dir
__version__ = '0.2'
__author__ = 'Hans Petter Langtangen <hpl@simula.no>, Gilbert Brault <gbrault@seadev.org>'
__doc__ = 'jupyter lab sketch drawing library'
setup(name='pysketcher',
      version=__version__,
      url='',
      author=__author__,
      description='',
      license='BSD',
      long_description=__doc__,
      platforms='any',
      #package_data={'name': ['pysketcher/*.dat'],},
      packages=['pysketcher'])

