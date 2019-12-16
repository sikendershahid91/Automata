import unittest
import src.create_machine as Machine
import inspect


class ReadInputTest(unittest.TestCase):
    def tearDown(self): print("")
    
    def test_print_output(self):
        print("[{0}]:\n".format(inspect.currentframe().f_code.co_name ))
        print(Machine.from_xml_file("input.xml"))
        
              
    def test_machine_creation(self):
        print("[{0}]:\n".format(inspect.currentframe().f_code.co_name ))
        MachineDescription = Machine.from_xml_file("input.xml")
        Machine1 = Machine.AutomataMachine(MachineDescription[0])
        print(Machine1.Table)

    def test_exception_nfa_machine_creation(self):
        print("[{0}]:\n".format(inspect.currentframe().f_code.co_name ))
        MachineDescription = Machine.from_xml_file("input.xml")
        try:
            Machine1 = Machine.AutomataMachine(MachineDescription[1])
            print(Machine1.Table)
        except ValueError:
            print("Successfully caught Error for type: ", MachineDescription[1]['type'])
