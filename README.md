# Computational Physics Simulations with Python
This page covers installation, dependencies, and how to run example programs.

Should you require more information, follow the links below:

1. {Breakdown of each file}
2. {Demonstrations}
3. {Why am I building this?}

## Packages and usage
Most files use [VPython](https://vpython.org/), compatible with **Python 3.8** - **3.12** for running locally as ```.py``` files.

You may also use the [web browser version of VPython](https://vpython.org/presentation2018/noinstall.html) or run it in a Jupyter notebook. Full documentation is available [here](https://glowscript.org/docs/VPythonDocs/index.html).

To begin, clone the repository by running this in your terminal:
```bash
git clone https://github.com/Nav-da-great/Computational-Physics-Projects.git
cd Computational-Physics-Projects
```
Now, create a virtual environment in the project directory:
```bash
python -m venv .venv
```
Activate the virtual environment:
```bash
.\.venv\Scripts\activate    # Windows
source .venv/bin/activate   # macOS/Linux
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Running an example program

Run an example program (e.g. ```electromagnetism/electric_field.py```):
```bash
python .\electromagnetism\electric_field.py
```
