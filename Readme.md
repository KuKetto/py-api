# FastApi python example

Setting up a pyenv virtual environment is highly suggested before installing the requirements from requirements.txt

### Running the app
Application can be run via `fastapi dev ./src/main.py`

FastApi has a built-in Swagger UI which can be accessed at `http://127.0.0.1:8000/docs` to learn more [visit the official documentation](https://fastapi.tiangolo.com/#check-it)

#### Notes
requirements.txt has mypy and pylint included so the mypy and pylint vscode extensions won't need any further installation in the virtual environment

VSC may won't recognize the source directory by itself. In that case the following should be added to `.vscode/settings.json`
```json
{
    // ...
    "python.autoComplete.extraPaths": [
        "/mnt/c/Users/domon/Desktop/py-api/src"
    ]
}
```