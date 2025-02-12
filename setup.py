from distutils.core import setup
setup(
  name = 'ehva',         # How you named your package folder (MyLib)
  packages = ['ehva'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library used to run Python scripts from the EHVA App',   # Give a short description about your library
  author = 'EHVA inc.',                   # Type in your name
  author_email = 'info@ehva.ca',      # Type in your E-Mail
  url = 'https://github.com/EHVAAutomation/ehva-python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/EHVAAutomation/ehva-python/archive/refs/tags/v0.3.tar.gz',    # I explain this later on
  keywords = ['EHVA'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
