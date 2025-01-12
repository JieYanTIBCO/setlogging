from setuptools import setup, find_packages

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="setlogging",  # The package name as it will appear on PyPI
    version="0.2.0",  # Initial version
    author="Jie Yan",  # Your name
    author_email="kiki3890528@gmail.com",  # Your contact email
    # Short description
    description="A flexible Python logging utility with JSON support and timezone awareness.",
    long_description=long_description,  # Content from README.md
    long_description_content_type="text/markdown",  # Specify markdown format
    url="https://github.com/JieYanTIBCO/setlogging",  # Your GitHub repository URL
    # Automatically find packages in the "src" directory
    packages=find_packages(where="src"),
    # Specify "src" as the root directory for packages
    package_dir={"": "src"},
    include_package_data=True,  # Include additional files from MANIFEST.in
    classifiers=[
        "Development Status :: 4 - Beta",  # Project status (Beta)
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
    install_requires=[
        # Specify runtime dependencies here, e.g.:
        # "dependency-name>=1.0.0",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],  # Development dependencies
    },
    entry_points={
        "console_scripts": [
            # If your project supports CLI, define it here:
            # "setlogging=setlogging.__main__:main",
        ],
    },
    license="MIT",  # License type
    keywords="logging json timezone python logger rotation",  # Keywords for PyPI
    project_urls={
        "Bug Tracker": "https://github.com/JieYanTIBCO/setlogging/issues",
        "Documentation": "https://github.com/JieYanTIBCO/setlogging",
        "Source Code": "https://github.com/JieYanTIBCO/setlogging",
    },
)
