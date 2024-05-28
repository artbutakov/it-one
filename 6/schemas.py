from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, field_validator


class JsonDataSchema(BaseModel):
    columns: List[str] = Field(validation_alias='Columns')
    rows: List[list] = Field(validation_alias='Rows')

    @field_validator('rows')
    @classmethod
    def check_types(cls, array):
        for index, subarray in enumerate(array):
            array[index] = [int(subarray[0]), datetime.strptime(subarray[1], '%Y-%m-%d %H:%M:%S'), str(subarray[2])]
        return array
