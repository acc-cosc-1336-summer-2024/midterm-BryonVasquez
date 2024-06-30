#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_bonus_pay_amount

class Test_Config(unittest.TestCase): 

    def test_get_bonus_pay_amount(self): 
        assert get_bonus_pay_amount(-1) == 'Invalid argument' 
        assert get_bonus_pay_amount(200) == 10 
        assert get_bonus_pay_amount(600) == 36 
        assert get_bonus_pay_amount(1000) == 70 
        assert get_bonus_pay_amount(1500) == 120 
        assert get_bonus_pay_amount(2000) == 'Invalid argument'


     





