"""Setup """

from setuptools import setup


def get_requirements():
    """Get list of requirements."""
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    # for any internal dependency we need to reformat for setuptools
    for i, requirement in enumerate(requirements):
            package_name = requirement.split("/")[-1].replace('.git', '').split("@")[0]
            requirements[i] = f'{package_name} @ {requirement}'

    return requirements


PACKAGE_NAME = 'autoplay'

setup(
    name=PACKAGE_NAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='None',
    url=f'git@github.com:nick-knudsen/{PACKAGE_NAME}.git',
    author='The Boys',
    author_email='info@beta.team',
    python_requires='>=3.8',
    install_requires=get_requirements(),
)
