from setuptools import setup, find_packages
 
setup(
    name='mywebserver',
    version='0.0.1dev',
    description='blabla',
    author='Christoph Burmeister',
    author_email='chburmeister@googlemail.com',
    url='http://christoph-burmeister.eu',
    packages=find_packages(),
    long_description="""\
      blablablabla ...
      """,
    classifiers=[
        "License :: MIT",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Webserver",
    ],
    keywords='webserver example',
    license='MIT',
    install_requires=[
        'Flask==0.11.1',
    ],
    include_package_data=True,
)
