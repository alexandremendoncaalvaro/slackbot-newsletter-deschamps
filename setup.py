from setuptools import setup, setuptools

readme = ""

try:
    with open("README.md", "r") as fh:
        readme = fh.read()
except FileNotFoundError:
    readme = 'https://github.com/alexandremendoncaalvaro/slackbot-newsletter-deschamps'
    pass

setup(name='slackbot-newsletter-deschamps',
    version='0.0.4',
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
    package_dir={"": "newsletter"},
    packages=setuptools.find_packages(where="newsletter"),
    python_requires=">=3.9",
    install_requires=['python-dotenv', 'slackclient'],)
