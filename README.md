# Fast Assignment

## Build dev environment with conda

```bash
conda env create --p ./.conda -f conda.yml
conda config --set env_prompt '({name})'
conda activate ./.conda
```

## Bring the system up

### Run via Docker Compose
```bash
docker-compose up -d --build
```

### Run locally
```bash
uvicorn app.main:app --reload --port 8000
```

You can then open the website at http://localhost:8000

## Migrate the data
```bash
alembic init -t async migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
```