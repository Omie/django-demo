# django-demo
a demo app for django newbies

### create and activate a virtual env
```
$ python3 -m venv /tmp/food
$ source /tmp/food/bin/activate
```

### clone the repo, install dependencies
```
$ git clone <url>
$ cd django-demo
$ pip install -r requirements.txt
```

### migrate the db and load sample data
```
$ ./manage.py migrate
$ ./manage.py loaddata fruits/fixtures/data.json
```

### check
```
open browser and navigate to http://localhost:8000/fruits/show-all/
```


