"""
The init_setup.sh file is not a standard file in Python projects. 
However, based on the naming convention and context, 
it is likely a custom script created by someone to initialize the setup
or environment for a particular project
"""

echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda create --p ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "intalling dev requirements"
pip install -r requirments_dev.txt
echo [$(date)]: "END"
