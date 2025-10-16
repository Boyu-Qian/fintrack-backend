import os

class Config:
    try:
        DB_USER = os.environ["POSTGRES_USER"]
        DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
        DB_HOST = os.environ["POSTGRES_HOST"]
        DB_PORT = os.environ["POSTGRES_PORT"]
        DB_NAME = os.environ["POSTGRES_DB"]
    except KeyError as e:
        raise RuntimeError(f"Missing required environment variable: {e}")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=disable"
        )
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DTABASE_URL environment valriable is not set")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    public_key_path = os.environ.get("PUBLIC_KEY_PATH","/app/public.pem")
    if os.path.exists(public_key_path):
        with open(public_key_path, "r") as f:
            PUBLIC_KEY = f.read()
    else:
        raise RuntimeError(f"Public key file not found at {PUBLIC_KEY_PATH}")