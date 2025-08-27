# Computational Physics Simulations with Python
This page covers installation, dependencies, and how to run example programs.

Should you require more information, follow the links below:

1. [Repository structure](STRUCTURE.md)
2. [Demonstrations](DEMO.md)
3. [Why am I building this?](WHY.md)

## Packages and usage
Most files use [VPython](https://vpython.org/), compatible with **Python 3.8** - **3.12** for running locally as ```.py``` files.

You may also use the [web browser version of VPython](https://vpython.org/presentation2018/noinstall.html) or run it in a Jupyter notebook. Full documentation is available [here](https://glowscript.org/docs/VPythonDocs/index.html).

To begin, clone the repository by running this in your terminal:
```powershell
git clone https://github.com/Nav-da-great/Computational_Physics_Projects.git
cd Computational-Physics-Projects
```
Now, create a virtual environment in the project directory:
```powershell
python -m venv .venv
```
Activate the virtual environment:

On Windows:
```powershell
.\.venv\Scripts\activate
```
On Linux/macOS:
```bash
source .venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Running an example program

This repository spans multiple domains in physics and uses shared utility modules (e.g., ```utilities/```). To run scripts directly, you need to add the repository root to your ```PYTHONPATH```.

To run the program ```electromagnetism/electric_field.py``` for example:

#### On Linux/macOS:
```bash
PYTHONPATH=. python electromagnetism/electric_field.py
```
#### On Windows (PowerShell):
```powershell
$env:PYTHONPATH="."; python .\electromagnetism\electric_field.py
```
