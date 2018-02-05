from setuptools import setup, find_packages
setup(
    name="Curveball",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    test_require=['numpy', 'scipy', 'networkx'],
    author="Julien Siebert",
    author_email="siebert@cs.uni-kl.de",
    description="Several implementations of the Curveball algorithm",
    url="https://gitlab.com/siebert_tukl/curveball/",
)
