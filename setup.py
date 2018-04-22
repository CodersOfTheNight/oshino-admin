#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from oshino_admin.version import get_version

install_reqs = list(parse_requirements("requirements/release.txt", session={}))
test_reqs = list(parse_requirements("requirements/test.txt", session={}))

setup(name="oshino-admin",
      version=get_version(),
      description="",
      author="zaibacu",
      author_email="zaibacu@gmail.com",
      packages=["oshino_admin"],
      install_requires=[str(ir.req) for ir in install_reqs],
      test_suite="pytest",
      tests_require=[str(tr.req) for tr in test_reqs],
      setup_requires=["pytest-runner"],
      entry_points={'console_scripts': ['oshino-admin = oshino_admin.run:main'
                                        ]
                    }
)
