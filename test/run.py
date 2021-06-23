# Usage:
#   python run.py
# 

import argparse
import json

from gfsm.fsm import FSM
from gfsm.fsm_builder.fsm_builder import FsmBuilder

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="generic fsm")
  ap.add_argument("-i", "--input", required = True,
	help = "full path to the input file(s)")
  ap.add_argument("-o", "--output", required = False,
	help = "full path to the output file(s)")
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
  return readJson('./test/fsm.json')


# Main function
def main(**kwargs): 
  fsm_conf = readConfig()
  fsm_builder = FsmBuilder(fsm_conf)
  fsm_impl = fsm_builder.build()
  # Instantiate the gfsm (create context)
  wrapper = fsm_impl['action-wrapper']
  fsm = FSM(wrapper, 'cntx_test')
  context = fsm.get_context()
  context.set_current_state(fsm_impl['first-state'])

  # Run test
  # state start
  fsm.dispatch('next')
  # state 1 
  fsm.dispatch('prev')
  fsm.dispatch('next')
  fsm.dispatch('repeat')
  fsm.dispatch('next')
  # state 2
  fsm.dispatch('prev')
  fsm.dispatch('next')
  fsm.dispatch('repeat')
  fsm.dispatch('next')
  # state 3
  fsm.dispatch('prev')
  fsm.dispatch('next')
  fsm.dispatch('repeat')
  fsm.dispatch('next')
  # state end
  fsm.dispatch('prev')



# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
