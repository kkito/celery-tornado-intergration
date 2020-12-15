# way to intergate tornado and celery

## using pipenv for dependency

`pipenv install`

## start tornado server

`export PYTHONPATH=.`

`pipenv run python run.py`

## start celery

should install redis see  `celery/config.py`

`export PYTHONPATH=.`

`pipenv run celery -A celery_app worker --loglevel=info -E`


## to test 

`curl http://localhost:8888/` # works fine

`ab -c 5 -n 20 http://localhost:8888/` # may have some error `raise InvalidResponse("Protocol Error: %r" % raw)`

## current workaround

`export PYTHONPATH=.`

`pipenv run python run_fix.py`