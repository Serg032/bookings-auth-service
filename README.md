# bookings-auth-service

## Setup (first time)

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Variables de entorno
cp env.example .env
# Edita .env con SUPABASE_URL, SUPABASE_KEY, etc.
```

## Ejecutar la API

```bash
fastapi dev src/main.py
# o
uvicorn src.main:app --reload
```

## Modo test (tabla distinta)

```bash
USERS_TABLENAME=users_atest fastapi dev src/main.py

# Con Supabase de test
USERS_TABLENAME=users_atest \
SUPABASE_URL=https://<TEST>.supabase.co \
SUPABASE_KEY=<TEST_KEY> \
fastapi dev src/main.py
```

## Tests de aceptación (Behave)

```bash
# Asegúrate de que la API esté corriendo (ver arriba)
behave
```

## Endpoints

- POST `/register` → 201 Created, devuelve `{ id, username, access_token }`
  - 409 Conflict si el usuario ya existe (`{ detail: "User already created with username <email>" }`)
- GET `/get-by-username/{username}`
