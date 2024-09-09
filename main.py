# To install python versions with pyenv
pyenv install <python_version>

# To create virtual venv with pyenv
pyenv virtualenv <python_version> <venv_name>

#  To display the list of python versions available to download
pyenv install --list

# To activate a python venv
pyenv activate <venv_name>
#  Example
pyenv install 3.10.0     # Install a specific Python version
pyenv virtualenv 3.10.0 myproject-env   # Create a `pyenv`-managed virtual environment
pyenv activate myproject-env  # Activate the `pyenv` virtual environment

