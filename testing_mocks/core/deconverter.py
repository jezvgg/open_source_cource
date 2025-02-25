import csv

from core.enums import ConvertType, ConvertStringType
from core.converter_string import ConverterString


class Deconverter:
    types: dict
    



    def __init__(self):
        self.types = {ConvertType.CSV:self.parse_csv}

        

    def deconvert(self, argument: ConvertType, obj: bytes) -> dict:
        value = obj.decode('utf-8')
        

        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")

        return self.types[argument](value)





    def parse_csv(self, csv_string: str):
        data = {"rows": []}
        lines = csv_string.strip().split("\n")
        if not lines:
            return data

        reader = csv.reader(lines)
        header = next(reader)

        for row in reader:
            row_dict = {}
            for col_name, value in zip(header, row):
                convert = ConverterString()
                row_dict[col_name] = convert(self.get_type(value.strip()),value.strip())
            data["rows"].append(row_dict)
        print(data)
        return data
    
    def get_type(self,value: str):
        if value.isdigit():
            return ConvertStringType.INT
        if value.replace('.','').isdigit():
            return ConvertStringType.FLOAT
        return ConvertStringType.STR




    