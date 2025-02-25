import unittest
import json

from core.converter import Converter
from core.deconverter import Deconverter
from core.enums import ConvertType

class TestCore(unittest.TestCase):


    def test_converter(self):
        convert = Converter()
        obj = {"data":"data1"}
        

        result = convert.convert(ConvertType.JSON,obj)


        assert json.loads(result) == {"data": "data1"}

    def test_deconvertor(self):
        deconverter = Deconverter()
        obj =  bytes(b'"Header1","Header2"\n"value1",2')


        result = deconverter.deconvert(ConvertType.CSV,obj)

        assert result == {'rows': [{'Header1': 'value1', 'Header2': 2}]}







