from setuptools import setup, find_packages

setup(
    name='grpcbigbuffer',
    version='0.0.1',

    url='https://github.com/jossemii/GRPCBigBuffer.git',
    author='Josemi Avellana',
    author_email='josemi.bnf@gmail.com',

    py_modules=[
        'grpcbigbuffer'
    ],
    install_requires=[
        'grpcio==1.56.0',
        'protobuf==4.23.3',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)