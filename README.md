# Python Package Template
This repository is a template that can be used for creating python packages. The following functionality exists.

* [x] Users can add multiple sub-packages.
* [x] Importing the installed package into other modules is simplified.
* [x] Users can create an conda environment from an environment file and automatically install the package and its dependencies.
* [x] Users can add logic to the overridden TestCase constructor and setUp and tearDown methods.

In order to use this template for your project, simply rename the different components throughout the package. This exact version
of the package can be tested with the following steps.

1. Create a conda virtual environment from the conda environment file with the below command.
```
conda env create -f my_virtual_env.yml
```
2. Activate the newly created virtual environment with the following command.
```
source activate my_virtual_env
```
If you are using a Windows computer, please use this slightly modified version of the command.
```
activate my_virtual_env
```

Now that you have created a conda environment that contains the installed package, you are now able to import the package
into other modules.

Unit tests for this package structure can be run with the below command.
```
python -m unittest discover
```

In order to use the package in other modules, please modify the following code snippet.
```python
from mypackage import mysubpackage
m = mysubpackage.MyClass(1)
m.my_method(2)
```

## License

    Copyright 2018 Michael Signorotti

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
