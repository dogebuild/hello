from setuptools import setup, find_packages

setup(name='dogebuild-hello',
      version='0.1',
      description='A hello world plugin for dogebuild.',
      author='Kirill Sulim',
      author_email='kirillsulim@gmail.com',
      url='https://github.com/dogebuild/hello',
      packages=find_packages(include=[
          'dogebuild*',
          ]),
     )
