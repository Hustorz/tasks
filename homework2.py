#task1
from asyncio import graph

from fastapi import dependencies


def task1():
    users = {
        'A' : {'B', 'C', 'D', 'E', 'F'},
        'B' : {'A', 'C', 'D'},
        'C' : {'A', 'B', 'D', 'E'},
        'D' : {'B'},
        'E' : {'B', 'F'},
        'F' : {'A', 'E'}
    }
    common_friends = {}
    for i in users:
        common_friends[i] = 0
        for j in users: 
            if i != j:
                common_friends[i] += len(users[i] & users[j])

    max_common_friends = max(common_friends.values())
    for i in users:
        if common_friends[i] == max_common_friends:
            print(f'User {i} has the most common friends: {max_common_friends}')


def task2():
    def dict_deep(a,b):
        if isinstance(a,dict) and isinstance(b,dict):
            c = {}
            for key in a.keys() | b.keys():
                if key in a and key in b: 
                    c[key] = dict_deep(a[key],b[key])
                elif key in a:
                    c[key] = a[key]
                elif key in b:
                    c[key] = b[key]
            return c 
        if isinstance(a,list) and isinstance(b,list):
            return a + b
        if isinstance(a,set) and isinstance(b,set):
            return a | b
        else:
            return b
   

def task3():
    def cycl_dep(dep):
        all_cycl = []
        curr_cycl = []
        all_cycl_set = set()
        def cycl_search(vertex):
            if vertex in curr_cycl:
                index_0 = curr_cycl.index(vertex)
                cycl = curr_cycl[index_0:]+[vertex]
                cycl_set = frozenset(cycl)
                if cycl_set not in all_cycl_set:
                    all_cycl_set.add(cycl_set)

                    all_cycl.append(cycl)
                return
            curr_cycl.append(vertex)
            for neighbor in dep.get(vertex, []):
                cycl_search(neighbor)
            curr_cycl.pop()
        for vertex in dep:
            cycl_search(vertex)
        return all_cycl

    

def task4():
    def normal_data(data):
        result = {}
        all_keys = set()
        for d in data:
            all_keys = all_keys | set(d.keys())
        for key in all_keys:
            key_appears = 0
            key_values = []
            for d in data:
                if key in d:
                    key_appears += 1
                    key_values.append(d[key])
            result[key] = {'values': key_values, 'appears': key_appears, 'missing': len(data) - key_appears}
        return result

def task5():
    def reverse_index(documents):
        rev_index = {}
        for ind, text in documents.items():
            words = text.split()
            for word in words:
                if word not in rev_index:
                    rev_index[word] = []
                rev_index[word].append(ind)
        return rev_index

    def search_document(rev_index, main_words):
        unsorted_result = {}
        for word in main_words:
            if word in rev_index:
                for ind in rev_index[word]:
                    unsorted_result[ind] = unsorted_result.get(ind, 0) + 1
        sorted_result = sorted(unsorted_result.items(), key=lambda x: x[1], reverse=True)  
        documents_result = [ind for ind,count in sorted_result]
        return documents_result         
  
def task6():
    def min_structure(data):
        result = {}
        for ind, d in enumerate(data):
            new_key = tuple(sorted(d.items()))
            if new_key not in result:
                result[new_key] = (ind,)
            else:
                result[new_key] += (ind,)
        return result     

def task7():
    def comparing(a,b):
        if type(a) != type(b):
            return False
        if isinstance(a, dict):
            if len(a) != len(b):
                return False
            for (key_a, value_a), (key_b, value_b) in zip(sorted(a.items()), sorted(b.items())):
                if not comparing(value_a, value_b):
                    return False
            return True
        if isinstance(a, (list, tuple)):
            if len(a) != len(b):
                return False
            for value_a, value_b in zip(a, b):
                if not comparing(value_a, value_b):
                    return False
            return True
        if isinstance(a, set):
            if len(a) != len(b):
                return False
            for value_a, value_b in zip(sorted(a, key=repr), sorted(b, key=repr)):
                if not comparing(value_a, value_b):
                    return False
            return True    
        return True

def task8():
    def all_short_paths(data, A, B):
        paths = [(A,)]
        best_result = None
        results = []
        while paths:
            path_0 = paths.pop()
            last_vertex = path_0[-1]
            if last_vertex == B:
                
                if best_result is None:
                    shortest_length = len(path_0)
                    results.append(path_0)
                else:
                    if len(path_0) == shortest_length:
                        results.append(path_0) 

                continue
            if best_result is not None and len(path_0) >= shortest_length:
                continue
            for next_vertex in data.get(last_vertex, []):
                if next_vertex not in path_0:
                    paths.append(path_0 + (next_vertex,))
        return results         
 

            
  



