from leetcode.leetcode_101_200.q146_lru_cache import LRUCache

def test_lru():
    """Explanation
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1);    // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4
    """
    outputs = []

    # { set : (key, value) }
    # { get : key }
    inputs = [{'set':(1,1)}, 
             {'set':(2,2)}, 
             {'get': 1}, 
             {'set':(3,3)},   
             {'get':2}, 
             {'set':(4,4)},
             {'get': 1},
             {'get':3},
             {'get':4}
    ]
    lru = LRUCache(2)

    for input in inputs:
        if 'set' in input:
            key, value = input['set']
            lru.put(key ,value)

        if 'get' in input:
            output = lru.get(input['get'])
            outputs.append(output)

    assert outputs == [1,-1,-1,3,4] 