import unittest
import src.create_machine as Machine
import inspect


class ReadInputTest(unittest.TestCase):
    def test_print_output(self):
        print("[{0}]:\n".format(inspect.currentframe().f_code.co_name ))
        print(Machine.from_xml_file("input.xml"))
        
        
              
    
