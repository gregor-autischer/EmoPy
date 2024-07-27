import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EmoPy",
    version="0.0.5",
    author="ThoughtWorks Arts",
    author_email="info@thoughtworksarts.io",
    description="A deep neural net toolkit for emotion analysis via Facial Expression Recognition (FER)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thoughtworksarts/EmoPy",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=3.6.3',
    install_requires=[
        'h5py==2.10.0',
        'keras==2.1.2',
        'coverage==4.5.3',
        'lasagne',
        'graphviz',
        'matplotlib',
        'pydot',
        'pytest',
        'numpy==1.17.4',
        'scipy==1.5.0',
        'tensorflow==1.13.1',
        'scikit-learn==0.19.1',
        'scikit-image==0.13.1',
        'opencv-python==4.4.0.40',
        'scikit-neuralnetwork==0.7',
    ]
)
