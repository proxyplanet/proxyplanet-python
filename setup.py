from setuptools import find_packages, setup
setup(
    name="proxyplanet",
    packages=find_packages(include=["proxyplanet"]),
    version='1.2.0',
    description="Official Python Library for the ProxyPlanet 4G proxy API",
    author="Michele Lizzit @ ProxyPlanet.io",
    author_email="info@proxyplanet.io",
    url="https://github.com/proxyplanet/proxyplanet-python",
    license="GPLv3",
    install_requires=["requests"]
)