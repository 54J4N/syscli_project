from setuptools import setup, find_packages

setup(
    name='mycli_project',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil',
        'tqdm',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'mycli=mycli.main:main',
        ],
    },
)
