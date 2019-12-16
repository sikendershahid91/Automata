

Types of Automata and Language Generators:
-------------------------------
+ Deterministic Finite Automata
+ Nondeterministic Finite Automata
+ Regular Grammar
+ Regular Expression
+ Pushdown Automata
+ Context-Free Grammar
+ Turing Machine 



### first check test:
Make sure to have test packages, run the following:
```
pip3 install $( cat requirements.txt ) 
```

if pip3 is not installed
run:
```
sudo apt-get update && sudo apt-get install python3-pip
```

XML file as input
-------------------------------
The input.xml file allows you to create as many machines and generators you would like
to interact with. However its easier to keep things simple.

In the xml document the following is the definite structure which needs to be used.

for a Finite Automata (FA) Machine:
```
<input>
  <FA>
    <type></type>
    <state></state>
    <alphabets></alphabets>
    <transition></transition>
    <start-state></start-state>
    <final-state></final-state>
  </FA>

```

for a Regular Grammar (RG) Machine: 
```
<input>
  <RG>
    <type></type>
    <terminal></terminal>
    <non-terminal></non-terminal>
    <production></production>
    <start></start>
  </RG>
</input>
```

You can configure symbols to your choosing. They can be single character or strings. 

Following is an example of a DFA machine defined in input.xml:
```
<input>
  <!-- MACHINE ONE-->
  <FA>
    <type>DFA</type>
    <state>A,B,C</state>
    <alphabets>a,b</alphabets>
    <transition>
      (A,b)->B
      (A,a)->C
      (C,b)->B
    </transition>
    <start-state>A</start-state>
    <final-state>B</final-state>
  </FA>
</input>	
```

Following is an example of a RG defined in input.xml:
```
<input>
  <!-- GRAMMAR GENERATOR -->
  <RG>
    <type>CFG</type>
    <terminal>
      S,A,B
    </terminal>
    <non-terminal>
      a,b
    </non-terminal>
    <production>
      S->AB
      A->aA
      B->Bb
      A->a
      B->a
    </production>
    <start>
      S
    </start>
  </RG>
</input>
```




