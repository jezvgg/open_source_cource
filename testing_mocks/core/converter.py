import io
import pickle
from core.enums import ConvertType



class Converter:
    types: dict
    



    def __init__(self):
        types = {ConvertType.JSON:"dict_to_bytesio"}

    def deconvert(self, argument: ConvertType, obj: io.BytesIO) -> dict:
        obj = obj.read()
        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")
        
        convert_function = getattr(Converter, self.types[argument])

        return convert_function(obj)


    

    def dict_to_bytesio(data_dict):
      
        byte_stream = io.BytesIO()
        pickle.dump(data_dict, byte_stream)

        byte_stream.seek(0)
        return byte_stream