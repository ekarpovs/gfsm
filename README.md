# Generic Finite State Machine (GFSM)

## It is a part of the [Image Processing Workshop](https://github.com/ekarpovs/image-processing-workshop) project. 

### It is a Python implementation of FSM concept described in [On the Implementation of Finite State Machines](https://www.jillesvangurp.com/static/on_the_implementation_of_finite_state_machines.pdf)

### A real finit state machine has to be instantiated from fsm.json file

### Additionally, working context(s) has to be created from context.json file(s)

### File system structure:

_____
    |__ /gfsm/ - The generic fsm project files
    |
    |__ /examples/ - the example of a real fsm and context descriptions
    |
    |__ /test/ - test of fsm example
    |
    |__ LICENSE - the license file
    |
    |__ README.md - this file
    |
    |__ requirements.txt - requirements
    |
    |__ setup.py - setup the package

## Local Installation

```bash
    cd gfsm
    pip install -e .
```

## Run test

```bash
    cd gfsm
    python ./test/run.py
```
