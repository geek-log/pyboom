from setuptools import setup


with open("README.md", "r") as readme_md:
    long_description = readme_md.read()

setup(name='pyboom',
      version='0.0.1',
      description='Detonador de bombas .. boom!!!',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://gitlab.com/geek.log/pyboom',
      author='constrict0r',
      author_email='constrict0r@protonmail.com',
      license='MIT',
      packages=['pyboom'],
      entry_points={
          'console_scripts': [
              'pyboom = pyboom.__main__:main'
          ]
      })
