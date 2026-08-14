# NEO Observation Planner

Python scripts for NEO / NEOCP / comet observation planning

Copyright 2024-2026 Martin Junius

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


## About

This is my personal development, not necessarily usable for anyone else. This code was previously part of my astropy-workbench repository.


## Installation

Clone the repository, create an virtual environment, and activate it (Windows command line):
```
> git clone https://github.com/phtnnz/neoop.git
> cd neoop
> python -m venv venv
> .\venv\Scripts\activate.bat
```
or using PowerShell (automatically handled by VSCode)
```
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .\venv\Scripts\Activate.ps1)
```

Install the package and dependencies:
```
> pip install -e .
```

## Installed Modules

If you want to install from scratch in a new Python venv, the following modules and their dependencies are required:

| Module | Remarks |
| ------ | ------- |
| icecream   |
| requests   |
| astropy    |
| astroquery |
| astroplan  |
| matplotlib | needs 3.10 |
| tzdata     |

```
> pip install icecream requests astropy astroquery astroplan "matplotlib<3.11" tzdata
```

Please note that matplotlib < 3.11 must be installed, until this issue is fixed in astroplan:  
https://github.com/astropy/astroplan/issues/603  
https://github.com/astropy/astroplan/pull/636

## Usage

See [NEO-obs-planner](docs/NEO-obs-planner.md)
