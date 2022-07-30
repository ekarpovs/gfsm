# Usage:
#   python run.py
# 

import argparse
import json

from gfsm.fsm import FSM
from gfsm.context import Context
from gfsm.fsm_builder.fsm_builder import FsmBuilder

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="generic fsm")
  ap.add_argument("-t", "--trace", required = False,
  default=False,
	help = "print output")
  
  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type") 
  return kwargs

def readJson(ffn):
  with open(ffn, 'rt') as f:
    data = json.load(f)
  return data

# Read configuration file
def readConfig():
  return readJson('./test/fsm-cfg.json')

def readDef():
  return readJson('./test/fsm-def.json')


# Main function
def main(**kwargs): 
  fsm_conf = readConfig()
  fsm_def = readDef()
  # Create single fsm engine
  fsm_builder = FsmBuilder(fsm_conf, fsm_def)
  fsm = FSM(fsm_builder)
  # create context
  context = Context('test')
  context.current_state_name = fsm_builder.first_state_name
  # Start the fsm engine
  # fsm.start()

  # Run test  
  # state start
  fsm.dispatch('next', context)
  # state 1 
  fsm.dispatch('prev', context)
  fsm.dispatch('next', context)
  fsm.dispatch('current', context)
  fsm.dispatch('next', context)
  # state 2
  fsm.dispatch('prev', context)
  fsm.dispatch('next', context)
  fsm.dispatch('current', context)
  fsm.dispatch('next', context)
  # state 3
  fsm.dispatch('prev', context)
  fsm.dispatch('next', context)
  fsm.dispatch('current', context)
  fsm.dispatch('next', context)
  # state end
  fsm.dispatch('prev', context)



# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
