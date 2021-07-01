from setuptools import setup, setuptools
from os.path import abspath, dirname, join

setup(name='slackbot-newsletter-deschamps',
      version='1.0.1',
      url='https://github.com/alexandremendoncaalvaro/slackbot-newsletter-deschamps',
      license='MIT License',
      author='Alexandre Alvaro',
      long_description='https://github.com/alexandremendoncaalvaro/slackbot-newsletter-deschamps',
      long_description_content_type="text/markdown",
      author_email='alexandre.alvaro@hotmail.com',
      keywords='Pacote',
      description='Slackbot Tech Newsletter from e-mail',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      package_dir={"": "src"},
      py_modules=["newsletter"],
      python_requires=">=3.8",
      install_requires=['python-dotenv', 'slackclient'],)
