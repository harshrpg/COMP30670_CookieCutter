from setuptools import setup

setup(name="systeminfo",
      version = "0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Harsh Gupta",
      author_email="harsh.gupta@ucdconnect.ie",
      license="MIT",
      package_dir={'':'systeminfo'},
      packages=[''],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.sysinfo:get_platform_info']})