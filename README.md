# FastAPI assignment
This is a simple project to demonstrate the usage of FastAPI.

Features:
- [x] CRUD operations with PostgreSQL, Alembic and SQLAlchemy, Asyncio support.
- [x] FastAPI
- [x] Authentication with OAuth2 (Azure AD )
- [x] Unit tests
- [x] Docker Compose
- [x] Alembic migrations
- [x] CORS enabled
- [x] dotenv config
- [ ] CI/CD with GitHub Actions
- [ ] Dapr
- [ ] Add one more service


## Build dev environment with conda

```bash
conda env create --p ./.conda -f conda.yml
conda config --set env_prompt '({name})'
conda activate ./.conda
```

## Bring the system up
You need run data migration first to make sure the database is ready.
### Run via Docker Compose
```bash
docker-compose up -d --build
```

### Run locally
```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8000
```

You can then open the website at http://localhost:8000

## Migrate the data
```bash
alembic init -t async migrations
alembic revision --autogenerate -m "init"
alembic revision --autogenerate -m "add new tables"
alembic upgrade head
```

## Tests
```bash
python -m pytest ./tests
```
