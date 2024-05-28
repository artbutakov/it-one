from datetime import datetime
from random import randint

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main(documents_date: int):
    row_count = randint(2, 20)
    return {
        "Columns": ["key1", "key2", "key3"],
        "Description": "Банковское API каких-то важных документов",
        "RowCount": row_count,
        "Rows": [
            [str(randint(1, 1000)), str(datetime.fromtimestamp(documents_date)), f"value{index}"]
            for index in range(row_count)
        ]
    }


if __name__ == "__main__":
    uvicorn.run('api:app', host='localhost', port=8000, reload=True)
