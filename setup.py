#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from oshino_admin.version import get_version

setup(name="oshino-admin",
      version=get_version(),
      description="",
      author="zaibacu",
      author_email="zaibacu@gmail.com",
      packages=["oshino_admin"],
      install_requires=[
        "click==6.7",
        "requests",
        "daemonize"
      ],
      test_suite="pytest",
      tests_require=[
         "pytest",
         "coverage",
         "coveralls",
         "py"
      ],
      setup_requires=["pytest-runner"],
      entry_points={
          "console_scripts": [
              "oshino-admin = oshino_admin.run:main"
            ]
      }
)
