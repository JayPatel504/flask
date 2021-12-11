"""Division"""
from operation.calculation import Calculation

class Division(Calculation):
    """divide class"""
    def get_result(self):
        """get division result"""
        dv_of_values = self.values[0]
        try:
            for i, val in enumerate(self.values):
                if i==0:
                    continue
                dv_of_values/=val
            return round(dv_of_values,2)
        except ZeroDivisionError:
            return "Can't divide by zero"
