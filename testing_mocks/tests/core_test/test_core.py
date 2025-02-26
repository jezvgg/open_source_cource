import unittest
import json

from core.converter import Converter
from core.enums import ConvertType



class TestCore(unittest.TestCase):


    def test_converter(self):
        obj = {"data":"data1"}

        result = Converter.convert(ConvertType.JSON,obj)

        assert json.loads(result) == {"data": "data1"}


    def test_deconvertor(self):
        obj =  b'"Header1","Header2"\n"value1",2'

        result = Converter.deconvert(ConvertType.CSV, obj)

        assert result == {'rows': [{'Header1': 'value1', 'Header2': 2}]}







