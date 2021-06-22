# Usage:
#   python run.py
# 

import argparse
import json

from gfsm.fsm import FSM
from gfsm.fsm_builder.fsm_builder import FsmBuilder

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="WorkShop")
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
  first_state = fsm_impl['first-state']
  wrapper = fsm_impl['action-wrapper']
  fsm = FSM('cntx_test', first_state, wrapper)

  # Run test
  # with the context
  fsm.dispatch('to1') 
  fsm.dispatch('to2') 
  fsm.dispatch('to3') 
  fsm.dispatch('to1') 
  fsm.dispatch('tostart') 
  fsm.dispatch('toend') 




# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
