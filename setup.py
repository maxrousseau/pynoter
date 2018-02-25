from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pynoter',
      version='0.1',
      description='Powerpoint presentations into org or tex files',
      long_description='Allows users to convert powerpoint presentations into raw text for editing in latex or org-mode',
      classifiers=['Programming Language :: Python :: 2.7', 'Topic :: Text Processing :: Markup :: LaTeX'],
      url='https://github.com/maxrousseau/pynoter',
      scripts=['bin/py-noter'],
      author='Maxime Rousseau',
      author_email='maximerousseau08@gmail.com',
      test_suite='nose.collector',
      tests_require=['nose'],
      license='MIT',
      packages=['pynoter'],
      install_requires=['python-pptx'],
      zip_safe=False)
