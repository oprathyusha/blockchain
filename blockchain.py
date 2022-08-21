import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain :
    def __init__(self) -> None:
        self.chain=list()
        genesis_block = self._create_bloock(data="genesis block!",proof=1,previous_hash="0",index=1)
        self.chain.append(genesis_block)
    
    def mine_block(self)
    
    def _create_bloock(self,data:str,proof:int,previous_hash:str,index:int) -> dict:#returns dictonery
        block = {
            "index" : index,
            "timestamp" : str(_dt.datetime.now()),
            "data":data,
            "proof" :proof,
            "previous_hash" :previous_hash,
        }
