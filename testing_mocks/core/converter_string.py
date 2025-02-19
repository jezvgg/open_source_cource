import io

from core.enums import ConvertStringType



class ConverterString:
    types: dict



    def __init__(self):
        types={
            ConvertStringType.INT: "str_to_int",
            ConvertStringType.FLOAT: "str_to_float",
            ConvertStringType.STR: "str_to_str"
        }  



    def __call__(self,argument: ConvertStringType, obj: str, *args, **kwds):
        return self.convert(self, argument, obj)

    

    def convert(self, argument: ConvertStringType, obj: str):
        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")
        
        convert_function = getattr(ConverterString, self.types[argument])

        return convert_function(obj)



    def str_to_int(obj: str) -> int:
        return int(obj)



    def str_to_float(obj: str) -> float:
        return float(obj)



    def str_to_srt(obj: str) -> str:
        return obj