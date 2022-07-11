from setuptools import find_packages, setup

setup(
    name="CarloTestPackage",
    version="0.1.0",
    description="A Minimal Template Python Package",
    url="https://github.com/Cymelo92/CarloTestPackage",
    author="Carlo Meloni",
    author_email="something.something@gmail.com",
    license="MIT",
    install_requires=["numpy", "pandas", "scipy", "matplotlib"],
    packages=find_packages(),
    zip_safe=False,
)
