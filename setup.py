from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'example=example.my_project.module:main',
        ],
    },
    author='Nayonika Rao',
    author_email='raonayonika@gmail.com',
    description='An example project to demonstrate documentation ',
    url= 'https://github.com/raonayonika/example',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

