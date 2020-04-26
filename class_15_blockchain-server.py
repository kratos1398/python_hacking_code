from flask import Flask
from flask import request
import json
import requests
from hashlib import sha256
from datetime import datetime
from random import randint, uniform
 
 
node = Flask(__name__) # this will be the name of the file. The node is the server
 
 
# Configuration
node_id = '72ec6501-f4a8-4da7-a00d-054c82f24e92'
mining = True
our_tx = []
peer_list = []
Chain = []
 
@node.route('/trans', methods=['POST']) # this is the only one with POST because the server needs to send data to the client
def trans():
    new_tx = request.get_json()
    our_tx.append(new_tx)
 
    print("New transaction")
    print("FROM: {}".format(new_tx['from'].encode('ascii','replace')))
    print("TO: {}".format(new_tx['to'].encode('ascii','replace')))
    print("AMOUNT: {}\n".format(new_tx['amount']))
 
    return "Transaction posted successfully.\n"
 
@node.route('/blocks', methods=['GET'])
def blocks():
    blockchain = Chain
    return json.dumps(blockchain)
 
def get_node_chains():
    chains = []
    for n in peer_list:
        chain = requests.get(n + "/blocks").content
        chain = json.loads(chain)
        chains.append(chain)
    return chains
 
def consensus():
    global Chain
    chains = get_node_chains()
    l = Chain
    for c in chains:
        if len(l) < len(c):
            l = c
    Chain = l
 
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
            'timestamp': str(timestamp),
            'payload': payload,
            'work': work,
            'prev_hash': prev_hash,
            'hash': current_hash
            }
 
 
@node.route('/mine', methods = ['GET'])
def mine():
    block = Chain[-1]
    last_work = block['work']
    current_work = do_work(last_work)
 
    data = {
        'from': 'network',
        'to': node_id,
        'amount': uniform(.3, 1.3)
    }
 
    our_tx.append(data)
    Chain.append(next_block(current_work, block, our_tx))
    our_tx.clear()
    return json.dumps(Chain[-1]) + '\n'
Chain.append(next_block(0))
node.run()
 