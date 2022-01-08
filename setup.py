"""Setup """

from setuptools import setup


def get_requirements():
    """Get list of requirements."""
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    return requirements


PACKAGE_NAME = 'autoplay'

setup(
    name=PACKAGE_NAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Creating Better Playlists',
    url=f'git@github.com:nick-knudsen/{PACKAGE_NAME}.git',
    author='The Boys',
    python_requires='>=3.8',
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'autoplay-example = autoplay.main:main_example',
        ]
    }
)
