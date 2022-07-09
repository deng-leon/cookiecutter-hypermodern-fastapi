"""Hello {{cookiecutter.friendly_name}}"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "{{cookiecutter.friendly_name}}"}


def main():
    uvicorn.run("{{cookiecutter.project_name}}.__main__:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
