import json
import sys
import hashlib
from web3 import Web3

g_url="http://127.0.0.1:7545"
w3 =Web3(Web3.HTTPProvider(g_url))

w3.eth.default_account = w3.eth.accounts[1]
a=w3.eth.accounts[1]
#print(w3.eth.get_block('latest'))
abi= """[
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "content",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "bool",
          "name": "completed",
          "type": "bool"
        }
      ],
      "name": "Fileadded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "bool",
          "name": "allowed",
          "type": "bool"
        }
      ],
      "name": "Fileallowed",
      "type": "event"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "taskcount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "tasks",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "content",
          "type": "string"
        },
        {
          "internalType": "bool",
          "name": "allowed",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "string",
          "name": "_content",
          "type": "string"
        }
      ],
      "name": "createtask",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "allow",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "string",
          "name": "_content",
          "type": "string"
        }
      ],
      "name": "check",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ]"""
#print(abi)
abi_json=json.loads(abi)
bytecode='0x60806040526000805534801561001457600080fd5b506040805180820190915260078152666f6e6566696c6560c81b6020820152610045906001600160e01b0361004a16565b610151565b6000805460019081018083556040805160608101825282815260208082018781528284018790529386528481529190942084518155915180519293610097939085019291909101906100b6565b50604091909101516002909101805460ff191691151591909117905550565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100f757805160ff1916838001178555610124565b82800160010185558215610124579182015b82811115610124578251825591602001919060010190610109565b50610130929150610134565b5090565b61014e91905b80821115610130576000815560010161013a565b90565b6103a0806101606000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80635e24de0e146100465780638bd48089146100ee5780638d97767214610108575b600080fd5b6100ec6004803603602081101561005c57600080fd5b81019060208101813564010000000081111561007757600080fd5b82018360208201111561008957600080fd5b803590602001918460018302840111640100000000831117156100ab57600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506101af945050505050565b005b6100f661021b565b60408051918252519081900360200190f35b6101256004803603602081101561011e57600080fd5b5035610221565b604051808481526020018060200183151515158152602001828103825284818151815260200191508051906020019080838360005b8381101561017257818101518382015260200161015a565b50505050905090810190601f16801561019f5780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b60008054600190810180835560408051606081018252828152602080820187815282840187905293865284815291909420845181559151805192936101fc939085019291909101906102d0565b50604091909101516002909101805460ff191691151591909117905550565b60005481565b600160208181526000928352604092839020805481840180548651600296821615610100026000190190911695909504601f810185900485028601850190965285855290949193929091908301828280156102bd5780601f10610292576101008083540402835291602001916102bd565b820191906000526020600020905b8154815290600101906020018083116102a057829003601f168201915b5050506002909301549192505060ff1683565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061031157805160ff191683800117855561033e565b8280016001018555821561033e579182015b8281111561033e578251825591602001919060010190610323565b5061034a92915061034e565b5090565b61036891905b8082111561034a5760008155600101610354565b9056fea265627a7a723158204afc32fdc2382704ba336009ff7bc0f0f22e6e3cc84b3472e2d29599d16fc4e464736f6c63430005100032'

file_auth = w3.eth.contract(abi=abi,bytecode=bytecode)

tx_hash = file_auth.constructor().transact()

tx_res = w3.eth.waitForTransactionReceipt(tx_hash)

cont = w3.eth.contract(
    address='0xBe67E1cAa9977261953a5894B925715E5D3c5572',
    abi=abi_json
)

def create():
  print("this is create")
  md5 = hashlib.md5()
  sha1 = hashlib.sha1()
  BUF_SIZE = 65536 
  #check if not empty array 4
  if data[4]!='0':
    #path is the path from the create function 
    with open(path, 'rb') as f:
      while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            #print(data)
            md5.update(data)
            sha1.update(data)
    thi=str(md5.hexdigest())



while True:
  md5 = hashlib.md5()
  sha1 = hashlib.sha1()
  BUF_SIZE = 65536  
  with open("newfile.txt", 'rb') as f:
    while True:
          data = f.read(BUF_SIZE)
          if not data:
              break
          #print(data)
          md5.update(data)
          sha1.update(data)
  thi=str(md5.hexdigest())
  #print(md5.hexdigest())
  choose = input("what do u want to do get or post: ")
  if choose == "get":
    x=cont.functions.check(thi).call()
    print(x)
  elif choose == "put":
    cont.functions.createtask(thi).transact()
