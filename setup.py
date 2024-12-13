from setuptools import setup, find_packages

setup(
    name="Cinos_API",  # Package name
    version="1.0.0",  # Package version
    description="A module for managing food, drinks, and ice cream orders.",
    long_description=open("README.md").read(),  # Optional: Include your README
    long_description_content_type="text/markdown",
    author="Carlos Matos",
    author_email="your_email@example.com",
    url="https://github.com/los9806/Matos_Sprint_4_Final.git",  # GitHub or project URL
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[],  # Add dependencies here, e.g., ["numpy>=1.21.0"]
)
