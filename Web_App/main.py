# Thin entrypoint so platforms that default to looking for "main:app"
# (like Railway) can find the app without duplicating app.py's code.
# All real logic stays in app.py — this just re-exports its `app` object.
from app import app

if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
