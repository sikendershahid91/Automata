'''
create_machine.py 

allows users to create a FA
 
'''
from xml.dom.minidom import parse, Node
import re


def from_xml_file( filename ):

    Machines = []
    def _parse_elements(tagName, tagData):
        if tagName == "type":
            return tagData.strip()
        elif tagName == "transition" or tagName == "production":
            return [x.strip() for x in tagData.strip().split('\n')]
        else:
            return [x.strip() for x in tagData.strip().split(',') ]
        

    def _get_elements( _types ):
        return [
            {
                element.tagName: _parse_elements( element.tagName,
                                                      element.childNodes[0].data) 
                for element in _type.childNodes
                if element.nodeType == 1
            }
            
            for _type in _types
        ] 
        
    xml = parse(filename)
    Machines.extend( _get_elements(xml.getElementsByTagName('FA')) )
    Machines.extend( _get_elements(xml.getElementsByTagName('RE')) )
    Machines.extend( _get_elements(xml.getElementsByTagName('RG')) ) 

    return Machines  



class AutomataMachine:
    def __init__(self, description):
        self.Type = description['type']
        self.State = description['start-state']
        self.Accept = description['final-state']
        self.Table = {}
        
        for _state in description['state']:
            self.Table[_state] = {}
            for _alphabets in description['alphabets']:
                self.Table[_state][_alphabets] = 'Error'
            
        for _transition in description['transition']:
            aTransition = re.sub(r'[()->,]',' ',_transition).split()
            try:
                self.Table[aTransition[0]][aTransition[1]] = aTransition[2]
            except KeyError:
                print("There is a transition statement that does not make sense")
                print("Transition state: ", aTransition) 
                
