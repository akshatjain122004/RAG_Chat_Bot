# RAG — Retrieval-Augmented Generative Project

This repository contains a small Retrieval-Augmented Generation (RAG) example project.

## Project layout

- `app.py` — Main application entrypoint.
- `index.py` — Alternative runner / helper script.
- `test_app.py` — Unit tests.
- `requirements.txt` — Python dependencies.
- `docker-compose.yml` — Docker compose configuration for running services.

## Requirements

- Python 3.10+ (virtual environment recommended)
- Docker & Docker Compose (optional, for containerized runs)

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Running the app

Run the main app:

```powershell
python app.py
```

Or run `index.py` if it offers an alternate entrypoint:

```powershell
python index.py
```

## Testing

Run the unit tests with pytest:

```powershell
pip install pytest
pytest -q
```

## Docker

Start services with Docker Compose:

```powershell
docker compose up --build
```

Stop and remove containers:

```powershell
docker compose down
```

## Contributing

1. Fork the repo.
2. Create a feature branch.
3. Open a pull request with a clear description and tests.

## License

This project does not include a license file. Add one (for example, MIT) if you plan to publish or share this repository.

## Notes

- The repository currently contains a minimal example layout. Update this README to reflect actual usage details and any environment variables or secrets required by the project.
