from functools import lru_cache
from typing import Generic, TypeVar, Hashable
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")
class LruCache(Generic[K, V]):
    
    #TODO work out the data structure
    def __init__(self, maxsize: int):
        '''
        initialization of cache
        '''
        #TODO
        
    def add(k: K, v: V):
        '''
        adds pair of key and value
        '''
        #TODO
    def clear() :
        '''
        clearing cache
        '''
    def access (k: K)->V:
        '''
        getting value by key
        raising KeyError exception if no key exists
        '''
           
        
            
        
    


