import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name = "hostout.overridedeploy"
setup(
    name=name,
    version="1.0.1",
    author="Anderson Leeb Inc",
    author_email="admin@andersonleeb.com",
    description="""override default deploy of hostout""",
    license="GPL",
    keywords="buildout, fabric, deploy, deployment, server, plone, django, host, hosting",
    url='https://github.com/ianderso/hostout.overridedeploy' + name,
    long_description=(
        read('README.md')
        + '\n' +
        #read('hostout', 'overridedeploy', 'README.md')
        #+ '\n' +
        read('CHANGES.txt')
        + '\n'
        ),

    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['hostout'],
    install_requires=['zc.recipe.egg',
                      'setuptools',
                      'collective.hostout>=1.0a5'],
    entry_points={'zc.buildout': ['default = hostout.overridedeploy:Recipe'],
                  'fabric': ['fabfile = hostout.overridedeploy.fabfile']
                  },
    zip_safe=False,
    )
