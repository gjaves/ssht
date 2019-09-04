#!python

from setuptools import setup

setup(name='ssht',
      version='0.1',
      description='Always use tmux with ssh.',
      url='https://github.com/gjaves/ssht',
      author='Jan (javes) Veselý',
      author_email='gjaves@gmail.com',
      license='MIT',
      scripts=['bin/ssht'],
      #packages=['funniest'],
      #zip_safe=False
      )

