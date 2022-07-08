# English Quiz
Training English

## backend/.env
- DB_URL - str, url for db. For example, `sqlite:///db.db`
- FIRST_SUPERUSER - str, admin email
- FIRST_SUPERUSER_PASSWORD - str, admin password

## db/.env
- POSTGRES_USER - str, db admin user
- POSTGRES_PASSWORD - str, db admin pass

## Test
1. `docker-compose exec quiz-back python -m pytest --cov="."`

## Docker-compose run
1. `docker-compose up --build`
