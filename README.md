# DOCUMENTATION


**The Python Package Index** (PyPI) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community.

## Local Installation of libraries
This is the process of installing packages or libraries in a specific directory or environment, usually associated with a particular project, rather than installing them globally on your system. This approach allows you to isolate the dependencies of different projects. Virtual Environments allow local installations by creating isolated environments.

## Folder Structures
One of the most important parts of documenting a project is the folder structure that is to be followed. It is essential to follow a structured approach in order to maintain consistency and modularity. Maintaining a constant naming convention is also essential. It is also important to keep your code modular. It is essential to package the libraries before importing them in your executable files.

A common error or mistake while importing a library in your executable file would be not mentioning the right or full path to the library module. An __init__ .py file plays a crucial role in turning a directory into a package, which allows for proper importing of modules within that directory. The presence of this file in a directory signals to Python that the directory is a package, enabling the interpreter to recognize and import its modules using the package name.

## _pip install -e_
This command installs a package which allows changes to the source code to be immediately reflected without needing to reinstall the package.It is essential for development of a project.This will also install any dependencies declared.

## setup.py:
A setup.py file makes use of setup tools to install all the required libraries/packages mentioned. This file exists at the root of your project directory.It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package.This information is used by the pip tool to install and manage Python packages from the command line.

## pyproject.toml:
The pyproject.toml file is a configuration file for Python projects, defined by PEP 518. It provides a standardized way to specify build system requirements and other project metadata.It is used by packaging tools, as well as other tools such as linters, type checkers, etc. 

example: [https://github.com/raonayonika/example]
