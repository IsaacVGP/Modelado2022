from gettext import install
from pdb import find_function
import setuptools

setuptools.setup(
    name="mpb22p1",
    version="0.0.0",
    author="Isaac",
    author_email="isaacvazquez.1iv11@gmail.com",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["numpy","pandas","matplotlib"]
)