from setuptools import setup, find_packages

setup(
    name='example',  # The name of the package
    version='0.1.0',  # The initial release version
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=[
        'requests',  # External package dependency
        'numpy',  # Another external package dependency
    ],
    entry_points={
        'console_scripts': [
            'example=example.my_project.module:main',  # Command-line script entry point
        ],
    },
    author='Nayonika Rao',  # Author's name
    author_email='raonayonika@gmail.com',  # Author's email
    description='An example project to demonstrate documentation',  # Short project description
    url='https://github.com/raonayonika/example',  # URL for the project homepage
    classifiers=[
        'Programming Language :: Python :: 3',  # Python version compatibility
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',  # OS compatibility
    ],
)

