molpy
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.com/dominiquesydow/molpy.svg?branch=master)](https://travis-ci.com/dominiquesydow/molpy)
[![codecov](https://codecov.io/gh/dominiquesydow/molpy/branch/master/graph/badge.svg)](https://codecov.io/gh/dominiquesydow/molpy/branch/master)

A novel molecule manipulation package.

This is a test package developed during a MolSSI workshop.


### Notes from workshop

#### Cookiecutter
- Package: Author name > License holder
- https://opensource.org/licenses/gpl-license 
- https://choosealicense.com/ 
#### Git
- `git checkout . (remove all changes)`
- `git log --oneline`
- `git remote -v`
- `git remote add upstream xxx`

#### Package: Testing, PEP8
- Add dependencies
  - `molpy/setup.py`
  - `molpy/devtools/conda-envs/test_env.yaml`
- `pytest -vs` (use `-s` to show also `print` statements)
- `yapf -ir *`
- Snake/camel/captial case

- https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
- https://tirkarthi.github.io/programming/2019/05/08/f-string-debugging.html
- https://gitmoji.carloscuesta.me/
- https://help.github.com/en/github/using-git/caching-your-github-password-in-git

#### Docs
- https://www.sphinx-doc.org/en/1.5/markup/code.html
- https://numpydoc.readthedocs.io/en/latest/format.html
- https://readthedocs.org/dashboard/molpy-ds/advanced/: Add tick "Install project"
- Semantic versioning: https://semver.org/ 


### Copyright

Copyright (c) 2020, Dominique Sydow


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
