from setuptools import setup, find_packages

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    ]

# calling the setup function 
setup(name='atts',
      version='0.0.1',
      description='Train_test splitter with adversarial validation',
      long_description=long_description,
      url='https://github.com/alikula314/Auto_train_test_splitter',
      author='Muhammet Ali Kula',
      author_email='alikula3.14@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=CLASSIFIERS,
      install_requires=requirements,
      keywords='adversarial validation train-test-split data-sceince machine-learning'
      )
