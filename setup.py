import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    VERSION = f.read()
packages = find_packages()
setup(
    name="socialmediacalendar",
    version=VERSION,
    packages=packages,
    package_data={k: ["*.csv", "*.yml"] for k in packages},
    data_files=[("", ["manifest.yml"])],
    scripts=[],
    entry_points={},
)
