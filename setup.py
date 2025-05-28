from setuptools import find_packages,setup



setup(
    name="MOCHI",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
    },
    install_requires=[
        'PyQt6'
    ],
    entry_points={
        'console_scripts': [
            'mochi = mochi.main:main',
        ],
    }
)

