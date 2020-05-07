# kv-storage
Key value lightweight storage

Run:
docker-composer up

Test&Linters

docker-compose run -e FLASK_ENV=testing web make test

docker-compose run -e FLASK_ENV=testing web make lint

docker-compose run -e FLASK_ENV=testing web make coverage
