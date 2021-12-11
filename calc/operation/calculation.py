"""This is our calculation base class / Abstract Class"""
class Calculation:
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self,values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)
    @classmethod
    def create(cls,values:tuple):
        """factory method"""
        return cls(values)
    @staticmethod
    def convert_args_to_list_float(values):
        """function to standardize values to list of floats"""
        return tuple(map(float,values))
