
Simple rest application example

## Installation

Use git to clone:
```bash
git clone https://github.com/KorvinEC/test_task
```

Then, install requirements via package manager:

```bash
pip install -r requirements.txt
```

Create dababase:
```
python manage.py makemigrations 
python manage.py migrate 
```

And run project:
```
python manage.py runserver
```

## Endpoints

#### `dealers/`

* `GET` request for showing all available dealers.
* `POST / PUT` for creating a new dealer.
* `OPTIONS` to show json schema.

#### `dealers/<int:pk>`

* `GET` to show specific dealer.
* `POST / PUT` to update dealer info.
* `DELETE` to delete entity.
* `OPTIONS` to show json schema.

#### `cars/`

* `GET` request for showing all available cars.
* `POST / PUT` to create a new car.
* `OPTIONS` to show json schema.
* `?dealer=<int:pk>` to filter cars by dealer.

#### `cars/<int:pk>`

* `GET` to show specific car.
* `POST / PUT` to update car info.
* `DELETE` to delete entity.
* `OPTIONS` to show json schema.
