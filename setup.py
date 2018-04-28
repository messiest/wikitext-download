from distutils.core import setup

setup(name='wikitext-downloader',
      version='1.0',
      description='Utility for downloading the WikiText datasets',
      long_description=open('README.md').read(),
      author='Chris Messier',
      license='BSD 3-Clause',
      author_email='messiercr@gmail.com',
      url='https://github.com/messiest/wikitext-downloader',
      packages=['pokegen'],
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'],
      )
