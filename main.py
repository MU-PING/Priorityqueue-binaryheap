# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:39:25 2021

@author: Mu-Ping
"""
import math

heap = [] #透過array來初始一個標兵
nodes = {}
element = ["A", "B", "C", "D","E", "F", "G", "H", "I"] 
weight = [7, 22, 12, 2, 20, 4, 8, 15, 10]        
length = len(weight)
max_min = "min"

class Node ():
    
    def __init__(self, element, weight, position):
        self.element = element   
        self.weight = weight   
        self.position = position

def Heapify(root):
    left = 2 * root         # 取得left child
    right = 2 * root + 1    # 取得right child
    index = 0               # index 用來記錄 weight 最小(最大)的 node 之 index
    
    if (left <= length):
        
        if (right > length):
            nodes = [left, root]
            
        elif (right <= length):
            nodes = [left, right, root]
            
        if(max_min=="max"):
            index = max(nodes, key=lambda i: heap[i].weight)
            
        elif(max_min=="min"):
            index = min(nodes, key=lambda i: heap[i].weight)
            
        if (index != root):                                   # 如果目前 node 的 weight 不是三者中的最小
            heap[index], heap[root] = heap[root], heap[index] # 就調換 node 與三者中 weight 最小的 node 之位置
            heap[index].position = index
            heap[root].position = root
            
            Heapify(index)                   # 調整新的 subtree 成 Min Heap

def BuildHeap():
    heap.append(Node(-1, -1, 0))
    for i in range(length):
        node = Node(element[i], weight[i], i+1)
        nodes[element[i]] = node
        heap.append(node)
        
    for i in range(math.floor(length/2), 0, -1):
        Heapify(i)
        
def ExtractOutput():   
    global length
    
    if(length==0):
        print("error: heap is empty")
        return False
    
    else:
        output = heap[1]
        heap[1] = heap[length]
        del heap[length]
        length-=1
        Heapify(1)
        return output
        
def WeightAdjust(element, weight): 
    old_weight = nodes[element].weight    
    nodes[element].weight = weight
    child_index = nodes[element].position

    if(max_min=="max"):
        if(weight >= old_weight):
            parent_index = math.floor(child_index/2)
            while (child_index > 1 and heap[parent_index].weight < heap[child_index].weight):
                heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
                heap[parent_index].position = parent_index
                heap[child_index].position = child_index
                
                child_index =  parent_index 
                parent_index = math.floor(child_index/2)
                
        elif(weight < old_weight):
            Heapify(child_index)
            
    elif(max_min=="min"):
        if(weight <= old_weight):
            parent_index = math.floor(child_index/2)
            while (child_index > 1 and heap[parent_index].weight > heap[child_index].weight):
                heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
                heap[parent_index].position = parent_index
                heap[child_index].position = child_index
                
                child_index =  parent_index 
                parent_index = math.floor(child_index/2)
                
        elif(weight > old_weight):
            Heapify(child_index)
            
def HeapInsert(element, weight):
    node = Node(element, weight, length+1)
    nodes[element] = node
    heap.append(node)
    WeightAdjust(element, weight);

def ShowHeap():
    for i in heap[1:]:
        print(i.element, i.weight, i.position)
    print("\n")
        
if __name__ == '__main__':
    
    print("Build Heap")
    BuildHeap()
    ShowHeap()
    
    print("Adjust C weight to 3")
    WeightAdjust("C", 3)
    ShowHeap()
    
    output = ExtractOutput()
    print("Output", output.element, output.weight)
    ShowHeap()
    
    print("Insert J (weight 25)")
    HeapInsert("J", 25)
    ShowHeap()
    
