from setuptools import setup

setup(name='bq34z100-g1-flash',
      version='0.1',
      description='Flasher for .srec files for the TI bq34z100-g1 fuel gauge',
      url='https://github.com/nerdgilbert/bq34z100-g1-flash',
      author='Gilbert Montague',
      author_email='gilbert@openrov.com',
      license='MIT',
      packages=['argparse', 'os', 'smbus', 'sys', 'time']
      )
