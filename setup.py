from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='sparc.box',
      version=version,
      description="facilities to interact with GE Box api",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sparc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'boxsdk',
          'sparc.common',
          'sparc.cache'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
