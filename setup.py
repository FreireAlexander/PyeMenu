from setuptools import setup, find_packages
with open("README.md", "r", encoding= "utf-8") as fh:
  long_description = fh.read()

setup(
    name = 'pyemenu',         # How you named your package folder (MyLib)
    packages=find_packages(),
    version = '1.0.1',      # Start with a small number and increase it with every change you make
    author = 'Freire Alexander Palomino Palma',                   # Type in your name
    author_email = 'freirealexander0214@gmail.com',      # Type in your E-Mail
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Easy and Simple kit for develop Text User Interfaces',   # Give a short description about your library
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/FreireAlexander/PyeMenu',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/FreireAlexander/PyeMenu/releases/tag/1.0.0',
    project_urls = {
        "Bug Tracker": "https://github.com/FreireAlexander/PyeMenu/issues",
    },
    #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['MENU', 'CLI', 'command line', 'TUI', 'Text User Interface'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'readchar',
        ],
    classifiers=[
      'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
      'Intended Audience :: Developers',      # Define that your audience are developers
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',   # Again, pick a license
      'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
    ],
    python_requires = ">=3.7"
)