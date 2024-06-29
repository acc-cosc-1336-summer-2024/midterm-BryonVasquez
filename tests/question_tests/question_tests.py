#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import use_local_variable  

class Test_Config(unittest.TestCase):

    def test_use_local_variable(num): 
        num == 100 

        print(f"After function call, outside test case: num = {num}") 





