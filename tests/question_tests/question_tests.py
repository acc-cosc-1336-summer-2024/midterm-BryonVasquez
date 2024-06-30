#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_person_category

class Test_Config(unittest.TestCase): 

    def test_get_person_category(self): 
        assert get_person_category(1) == "infant" 
        assert get_person_category(2) == "child" 
        assert get_person_category(14) == "teenager" 
        assert get_person_category(20) == "adult" 
        assert get_person_category(-1) == "Invalid number" 
        assert get_person_category(126) == "Invalid number" 
        print("All test cases pass") 

     





