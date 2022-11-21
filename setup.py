#!/usr/bin/env python
from distutils.core import setup
import setuptools
setup(name='sgsanitizer',
      version='1.0.0',
      description="Provide an ES gamelist.xml file and it will do its best to "
                  "sanitize and remove any vulgar, casino, mahjong, or other "
                  "known unusable games from the gamelist. Primarily for arcade games",
      author='Douglas Rohde',
      packages=['sgs'],
      keywords='gamelist.xml gamelist emulationstation',
      url='https://github.com/ScienceLogic/vm2ami/archive/1.0.0.zip',
      license="MIT",
      install_requires=[
          'lxml'
      ],
      scripts=['bin/sgsanitizer']
      )