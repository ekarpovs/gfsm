# Usage:
#   python run.py
# 

import argparse
import json

from gfsm.fsm import FSM
from gfsm.fsm_builder.fsm_builder import FsmBuilder
from gfsm.context_builder.cntx_builder import ContextBuilder

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
def readFsmConfig():
  return readJson('./test/fsm.json')

def readContextConfig(config_file):
  return readJson(config_file)


# Main function
def main(**kwargs): 
  fsm_conf = readFsmConfig()
  fsm_builder = FsmBuilder(fsm_conf)
  fsm_implementation = fsm_builder.build()

  # Instantiate the gfsm
  fsm = FSM(fsm_implementation)

  # Create context builder for future usage
  cntx_builder = ContextBuilder()
  # Create test context#1 and bind it with the fsm instance
  cntx_conf = readContextConfig('./test/context1.json')
  context1 = cntx_builder.build(cntx_conf, fsm)

  # Create test context#2 and bind it with the fsm instance
  cntx_conf = readContextConfig('./test/context2.json')
  context2 = cntx_builder.build(cntx_conf, fsm)

  # Run test
  # with context#1
  fsm.dispatch('event1', context1) 
  fsm.dispatch('event2', context1) 
  fsm.dispatch('event3', context1) 

  # with context#2
  fsm.dispatch('event1', context2) 
  fsm.dispatch('event2', context2) 
  fsm.dispatch('event2', context2) 
  fsm.dispatch('event3', context2) 



# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
