from setuptools import setup

setup(name='gfsm',
      version='0.1',
      description='A generic finit state machine',
      url='https://github.com/ekarpovs/gfsm',
      author='ekarpovs',
      author_email='',
      license='MIT',
      packages=['gfsm','gfsm.fsm_builder','test','examples'],
      package_data={'examples':['*']},
      zip_safe=False)