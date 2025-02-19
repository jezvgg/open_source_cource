import io
import csv

from core.enums import ConvertType, ConvertStringType
from core.converter_string import ConverterString


class Deconverter:
    types: dict
    



    def __init__(self):
        types = {ConvertType.CSV:"parse_csv"}

        

    def deconvert(self, argument: ConvertType, obj: io.BytesIO) -> dict:
        obj = obj.read()
        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")
        
        convert_function = getattr(Deconverter, self.types[argument])

        return convert_function(obj)





    def parse_csv(self, csv_string: str):
        data = []
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
            data.append(row_dict)

        return data
    
    def get_type(value: str):
        if value.isdidget():
            return ConvertStringType.INT
        if value.replace('.','').isdidget():
            return ConvertStringType.FLOAT
        return ConvertStringType.STR




    