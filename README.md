# ikea-warehouse
Ikea Warehouse is a Python Flask prototype with a some fun ideas.

## Requirements

- PostgreSQL database

## Installation

1. Create your virtual environment in python with venv
```
python -m venv .
```
2. Activate your virtual environment
```
cd ikea-warehouse
source bin/activate
```
3. Install requirements 
```
pip install -r requirements.txt --no-cache-dir
```
4. Run your Flask application
```
FLASK_APP=app flask run --port=9000
```

## CLI

Ikea-warehouse supports some actions via commandline interpreter:

- Create all database structure
```flask db create```
- Drop all database structure
```flask db drop```
- Download to data directory language embeddings for ML applications
```flask translate download [language (i.e. en, es)]```

## License

Ikea-warehouse is distributed under the MIT License.
