from setuptools import find_packages,setup



setup(
    name="MOCHI",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
    },
    install_requires=[
        'setuptools','PyQt6','numpy','pandas','scipy<=1.15.2','matplotlib','pyinstaller'
    ],
    entry_points={
        'console_scripts': [
            'mochi = mochi.main:main',
        ],
    }
)

