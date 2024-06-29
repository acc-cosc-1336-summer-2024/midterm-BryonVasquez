#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_day_of_week 

class Test_Config(unittest.TestCase):

    def test_get_day_of_week(self): 
        assert get_day_of_week(0) == "Invalid number" 
        assert get_day_of_week(1) == "Monday" 
        assert get_day_of_week(2) == "Tuesday" 
        assert get_day_of_week(3) == "Wednesday" 
        assert get_day_of_week(8) == "Invalid number"  

        print ("All test cases passed") 



