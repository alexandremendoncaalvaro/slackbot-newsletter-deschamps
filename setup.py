from setuptools import setup, setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='slackbot-newsletter-deschamps',
    version='0.0.1',
    url='https://github.com/alexandremendoncaalvaro/slackbot-newsletter-deschamps',
    license='MIT License',
    author='Alexandre Alvaro',
    long_description=readme,
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
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=['python-dotenv', 'slackclient'],)
