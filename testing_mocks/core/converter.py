import json
import csv

from core.enums import ConvertType
from core.factory_method import factorymethod



class Converter:
    '''
    Фабрика раздающая функции для конвертации документов.
    '''

    @factorymethod
    def convert(argument: ConvertType, obj: dict ) -> bytes:
        '''
        Фабричный метод, вызывается если нет подходящего обработчика.

        :param argument: Аргумент по которому будет производиться диспатчеризация
        :param obj: Объект который будет конвертироваться
        '''
        raise ValueError("argument not in ConverStringType")
    

    @convert.register(ConvertType.JSON)
    def dict_to_bytesio(_, data_dict: dict) -> bytes:
        '''
        Фабричный метод реализующий логику конвертации объекта в JSON (простая реализация)

        :param data_dict: Объект который конвертируем, обычно словарь.
        '''
        return json.dumps(data_dict).encode('utf-8')
    

    @factorymethod
    def deconvert(argument: ConvertType, obj: bytes):
        '''
        Фабричный метод, вызывается если нет подходящего обработчика.

        :param argument: Аргумент по которому будет производиться диспатчеризация
        :param obj: Объект который будет конвертироваться
        '''
        raise ValueError("argument not in ConverStringType")
    

    @deconvert.register(ConvertType.CSV)
    def parse_csv(_, csv_string: bytes):
        '''
        Функция реализующая логику разконвертации из CSV в объект.

        :param csv_string: Байтовая строка, содержащая CSV
        '''
        csv_string = csv_string.decode('utf-8')
        data = {"rows": []}
        lines = csv_string.strip().split("\n")
        if not lines:
            return data

        reader = csv.reader(lines)
        header = next(reader)

        for row in reader:
            row_dict = {}
            for col_name, value in zip(header, row):
                row_dict[col_name] = Converter.convert_type(value.strip())
            data["rows"].append(row_dict)

        return data
    

    @staticmethod
    def convert_type(value: str):
        '''
        Определение типа в строке CSV.
        
        :param value: Строка, которую нужно конвертировать.
        '''
        if value.isdigit(): return int(value)
        if value.replace('.','').isdigit(): 
            return float(value)
        return value