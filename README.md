# Wallbox - Ramiro Garbagna

## Enviroment setup
All test were created using python (pytest library). The requested packaged are listed in the requirements.txt file, just use the following command:

```sh
pip install -r requirements.txt 
```

And everything should be working.

Another neccesary thing is creating a new page in [CrudCrud](https://crudcrud.com/), get the ID and then replace it in the `main.py` file, line 3, then save it.

## Test execution

For running the tests, you must be in the main folder and run this command:

```sh
pytest -s
```