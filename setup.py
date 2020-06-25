import setuptools
from distutils.core import setup

with open("psychrnn/_version.py", "r") as f:
    exec(f.read())

with open("README.md", "r") as f:
    long_desc = f.read()

setup(

    name='PsychRNN',
    version=__version__,
    packages=['psychrnn', 'psychrnn.tasks', 'psychrnn.backend', 'psychrnn.backend.models'],
    license='MIT',
    long_description=long_desc,
    long_description_content_type='text/markdown',

    author="Daniel Ehrlich, Jasmine Stone, Alex Atanasov, David Brandfonbrener",
    author_email="psychrnn@gmail.com",
    description="Easy-to-use package for the modeling and analysis of neural network dynamics, directed towards cognitive neuroscientists.",
    keywords="neuroscience, modeling, analysis, neural networks",
    url="https://github.com/murraylab/PsychRNN",

)