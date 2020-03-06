#!/usr/bin/python

import re
import os
import sys
debug = True

lines = sys.stdin.readlines()
lemma = sys.argv[1]

# INPUT:
# - lines contain a list of "%i:goal" where "%i" is the index of the goal
# - lemma contain the name of the lemma under scrutiny
# OUTPUT:
# - (on stdout) a list of ordered index separated by EOL

def debugPrint(text):
    if (debug):
        print(text)

rank = []  # list of list of goals, main list is ordered by priority
           # Higher priority is better
           # e.g. things with priority 10 will happen first,
           # things with priority 0 go close to last
           # things with no priority go very last
maxPrio = 11
for i in range(0,maxPrio):
  rank.append([])

# ---------------------- #
# ---- Reachability ---- # 
# ---------------------- #  
if 'reachable' in lemma:
  debugPrint("Applying oracle to lemma: "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if 'Add' in line: rank[10].append(num)
    elif   'TOKEN' in line: rank[9].append(num) # Tokens and counters take top priority
    elif 'COUNTER' in line: rank[9].append(num)
    elif 'Ltk' in line: rank[8].append(num)
    elif 'Pk' in line: rank[8].append(num)
    elif 'Build' in line: rank[7].append(num)

# ---------------------- #
# --- Path Integrity --- # 
# ---------------------- #  
elif 'integrity' in lemma:
  debugPrint("Applying oracle to lemma: "+lemma)
  for line in lines:
    num = line.split(':')[0]
    # Highest priority goes to event facts actually used in the lemma
    if 'Add' in line: rank[10].append(num)
    elif 'Forward' in line: rank[10].append(num)
    elif 'StartBuild' in line: rank[10].append(num)
    elif 'Complete' in line: rank[10].append(num)
    # Next priority goes to enforcing any bounds
    elif   'TOKEN' in line: rank[9].append(num)
    elif 'COUNTER' in line: rank[9].append(num)
    # Next deduce where keys came from (which may then trigger aforementioned bounds)
    elif 'Ltk' in line: rank[8].append(num)
    elif 'Pk' in line: rank[8].append(num)
    elif 'ShKey' in line: rank[8].append(num)
    elif 'SessKey' in line: rank[8].append(num)
    elif 'SegmentKey' in line: rank[8].append(num)
    # Next deduce adversary knowledge (e.g. a send rule must have happened)
    elif 'KU' in line: rank[7].append(num)
    # Next run through construction phase
    elif 'Build' in line: rank[6].append(num)

# ---------------------- #
# --- Path Symmetry  --- # 
# ---------------------- #  
elif 'symmetry' in lemma:
  debugPrint("Applying oracle to lemma: "+lemma)
  for line in lines:
    num = line.split(':')[0]
    # Highest priority goes to event facts actually used in the lemma
    if 'Add' in line: rank[10].append(num)
    elif 'Forward' in line: rank[10].append(num)
    elif 'StartBuild' in line: rank[10].append(num)
    elif 'Complete' in line: rank[10].append(num)
    # Next priority goes to enforcing any bounds
    elif   'TOKEN' in line: rank[9].append(num)
    elif 'COUNTER' in line: rank[9].append(num)
    # Next deduce where keys came from (which may then trigger aforementioned bounds)
    elif 'Ltk' in line: rank[8].append(num)
    elif 'Pk' in line: rank[8].append(num)
    elif 'ShKey' in line: rank[8].append(num)
    elif 'SessKey' in line: rank[8].append(num)
    elif 'SegmentKey' in line: rank[8].append(num)
    # Next deduce adversary knowledge (e.g. a send rule must have happened)
    elif 'KU' in line: rank[7].append(num)
    # Next run through construction phase
    elif 'Build' in line: rank[6].append(num)

else:
    debugPrint("No oracle found for this lemma")
    exit(0)

# Ordering all goals by ranking (higher first)
for listGoals in reversed(rank):
  for goal in listGoals:
    print(goal)
