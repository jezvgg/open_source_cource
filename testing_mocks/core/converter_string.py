import io

from core.enums import ConvertStringType



class ConverterString:
    types: dict



    def __init__(self):
        self.types={
            ConvertStringType.INT: self.str_to_int,
            ConvertStringType.FLOAT: self.str_to_float,
            ConvertStringType.STR: self.str_to_str
        }  



    def __call__(self,argument: ConvertStringType, obj: str, *args, **kwds):
        return self.convert(argument, obj)

    

    def convert(self, argument: ConvertStringType, obj: str):
        if not argument in self.types.keys():
            raise ValueError("argument not in ConverStringType")

        return self.types[argument](obj)



    def str_to_int(self,obj: str) -> int:
        return int(obj)



    def str_to_float(self,obj: str) -> float:
        return float(obj)



    def str_to_str(self,obj: str) -> str:
        return obj