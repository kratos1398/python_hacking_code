from hashlib import sha256
from datetime import datetime
from random import randint, uniform
 
 
def do_work(proof):
    i = proof + 1
    while not (i % 7 == 0 and i % proof == 0):
        i += 1
    return i
 
 
def print_chain(chain, block=None):
    if block is None or block > len(chain) or block < 0:
        block = -1
 
    print('This chain has {} blocks.'.format(len(chain)))
    if block == -1:
        blurb = 'the most recent block'
    else:
        blurb = 'block {}'.format(block)
 
    print('The contents of {} are as follows:'.format(blurb))
    contents = '\tID: {}\n\tTimestamp: {}\n\tPayload: {}\n\tWork: {}\n\tPrevious Hash: {}\n\tBlock Hash: {}'
    print(contents.format(chain[block]['id'],
                          str(chain[block]['timestamp']),
                          chain[block]['payload'],
                          chain[block]['work'],
                          chain[block]['prev_hash'],
                          chain[block]['hash']))
 
 
def hash_block(block):
    sha = sha256()
    sha.update(block.encode())
    return sha.hexdigest()
 
 
def next_block(work, prev_block=None, payload=None):
    # This will initialize the chain if there is no previous block
    if prev_block is None:
        index = 0
        timestamp = datetime.now()
        payload = 'Initial Block'
        prev_hash = '88B90E746B7038940A137DF88B3F9FF2651CFEA328ED5A38EC5C597AE5FB883C'
        work = randint(1975, 23897)
 
    # otherwise just return a block to add to the chain.
    else:
        if payload is None:
            payload = "No transactions"
        index = prev_block['id'] + 1
        timestamp = datetime.now()
        prev_hash = prev_block['hash']
 
    current_hash = hash_block(str(index) +
                              str(timestamp) +
                              str(payload) +
                              str(work) +
                              str(prev_hash))
 
    return {'id': index,
            'timestamp': timestamp,
            'payload': payload,
            'work': work,
            'prev_hash': prev_hash,
            'hash': current_hash
            }
 
 
def mine(block):
    last_work = block['work']
    current_work = do_work(last_work)
 
    data = {
        'from': 'network',
        'to': 'some-node-id',
        'amount': uniform(.3, 1.3)
    }
 
    return next_block(current_work, block, data)
 
 
Chain = [next_block(0)]
 
for x in range(10):
    Chain.append(mine(Chain[x]))