from fastapi import FastAPI

app = FastAPI()

database = {
    "risperss": "password123",
}


@app.get("/{username}/login")
def login(username: str, password: str = None):
    if username not in database or not password:
        # Do something
        return {"Re": "jected"}

    if password == database[username]:
        return {"Hello": "World"}
