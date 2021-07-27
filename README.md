## Installation

Use git to clone:
```bash
git clone https://github.com/KorvinEC/test_task
```

Then, install requirements vie package manager [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
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
<br>
#### `dealers/<int:pk>` 
* `GET` to show specific dealer.
* `POST / PUT` to update dealer info.
* `DELETE` to delete entity.
* `OPTIONS` to show json schema.
####`cars/`
* `GET` request for showing all available cars.
* `POST / PUT` to create a new car.
* `OPTIONS` to show json schema.
* `?dealer=<int:pk>` to filter cars by dealer.
####`cars/<int:pk>`
* `GET` to show specific car.
* `POST / PUT` to update car info.
* `DELETE` to delete entity.
* `OPTIONS` to show json schema.