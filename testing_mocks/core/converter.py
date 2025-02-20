import io
import json
from core.enums import ConvertType



class Converter:
    types: dict
    



    def __init__(self):
        self.types = {ConvertType.JSON:self.dict_to_bytesio}

    def convert(self, argument: ConvertType, obj: object ) -> bytearray:
        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")

        return self.types[argument](obj)


    

    def dict_to_bytesio(self, data_dict: dict):
        
        json_string = json.dumps(data_dict)
        byte_data = json_string.encode('utf-8')
        byte_array_data = bytearray(byte_data)

        return byte_array_data