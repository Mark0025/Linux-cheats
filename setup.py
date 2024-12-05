from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess
import sys
import os
import time

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # First run the standard develop command
        develop.run(self)
        
        print("\n🚀 Installation complete! Starting Linux Cheats...")
        
        # Run linux-cheats command after install
        try:
            subprocess.run(
                ['linux-cheats'],
                check=True,
                stdout=None,  # Show output in terminal
                stderr=None
            )
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\nYou can start Linux Cheats anytime by running:")
            print("    linux-cheats")

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # First run the standard install command
        install.run(self)
        print("\n🚀 Running post-install setup...")
        # Then run our post-install script
        try:
            subprocess.run([sys.executable, '-m', 'linux_cheats_cli.scripts.post_install'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Post-install script error: {e}")
            print("Note: You can run 'linux-cheats' anytime to start the tool.")

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
        'python-dotenv>=1.0.0',
        'rich>=10.0.0',
        'termcolor>=2.3.0',
        'pypandoc>=1.11',
        'click>=8.0.0'
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
        ]
    },
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'linux-cheats=linux_cheats_cli.main:main',
        ],
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
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
    package_data={
        'linux_cheats_cli': [
            'scripts/*',
            'public/templates/*',
            'public/assets/css/*',
            'public/assets/images/*',
            'public/linux_cheats.txt',
            '.env'
        ]
    },
    include_package_data=True,
)