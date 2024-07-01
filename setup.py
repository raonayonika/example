from setuptools import setup, find_packages

setup(
    # The name of the package
    name='example',
    # The initial release version
    version='0.1.0',
    # Automatically find and include all packages in the project
    packages=find_packages(),
    install_requires=[
        # External package dependency
        'requests',
        # Another external package dependency
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            # Command-line script entry point
            'example=example.my_project.module:main',
        ],
    },
    # Author's name
    author='Nayonika Rao',
    # Author's email
    author_email='raonayonika@gmail.com',
    # Short project description
    description='An example project to demonstrate documentation',
    # URL for the project homepage
    url='https://github.com/raonayonika/example',
    classifiers=[
        # Python version compatibility
        'Programming Language :: Python :: 3',
        # License type
        'License :: OSI Approved :: MIT License',
        # OS compatibility
        'Operating System :: OS Independent',
    ],
)


