from setuptools import setup, find_packages
import os
import subprocess

setup(
    name='linux-cheats-cli',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandoc>=2.4',
        'markdown>=3.4',
        'loguru>=0.7.0',
        'Pillow>=9.5.0',
        'rich>=10.0.0',
        'termcolor>=2.3.0',
    ],
    entry_points={
        'console_scripts': [
            'linux-cheats=linux_cheats_cli.main:main',
        ],
    }
)

# Make start.sh executable and run it after install
if os.path.exists('start.sh'):
    os.chmod('start.sh', 0o755)
    try:
        subprocess.run(['./start.sh'], check=True)
    except:
        print("\n✨ Installation complete! Run: ./start.sh")