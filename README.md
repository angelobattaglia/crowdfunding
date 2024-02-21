# README

## How to fire this up

In Windows, it's recommended to use Powershell. In the root directory of this project:

```ps1
python -m venv .env
cd .env\scripts
.\Activate.ps1
```

Then install all of the libraries required
```ps1
pip install -r requirements.txt
pip list # to list the libraries required
```

This will run the Flask development server with debug mode enabled, allowing you to see detailed error messages and take advantage of features like automatic code reloading when changes are made

```ps1
cd app
flask run --debug
```

If you add any new module to this web app via virtual environment of this project,
just update the requirements.txt

```ps1
pip freeze > requirements.txt
```

As for the db viewer, it's recommended to use the [sqlitebrowser](https://sqlitebrowser.org/)