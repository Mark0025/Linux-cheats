from setuptools import setup, find_packages

setup(
    name='linux-cheats-cli',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandoc',
        'markdown',
        'loguru'
    ],
    entry_points={
        'console_scripts': [
            'linux-cheats=linux_cheats_cli.main:main',
        ],
    },
    description='A CLI tool to display Linux command cheat sheets',
    author='Mark Carpenter - The AI RE Investor',
    author_email='mark@theaireinvestor.com',
    url='https://github.com/theaireinvestor/linux-cheats-cli',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)