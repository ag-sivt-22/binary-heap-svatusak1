from dataclasses import dataclass
from typing import Any, Iterator

@dataclass
class Element:
    value: Any
    priority: int
 
    def __iter__(self) -> Iterator[Any | int]:
        yield self.value
        yield self.priority

class BinaryHeap:

    def __init__(self) -> None:
        self.heap: list[Element] = []
    
    def push(self, element) -> None:
        self.heap.append(element)
        self._repair_heap_bottom_up(len(self.heap)-1)

    def _repair_heap_bottom_up(self, index: int) -> None:
        if index == 0:
            return
        parent: int = (index-1)//2
        if self.heap[parent].priority > self.heap[index].priority:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._repair_heap_bottom_up(parent)

    def pop(self) -> Element:
        if len(self.heap) <= 0:
            raise Exception("heap empty")
        elif len(self.heap) == 1:
            return self.heap.pop()

        res: Element = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._repair_heap_top_down()

        return res

    def _repair_heap_top_down(self, index: int = 0) -> None:
        child: int = index * 2
        if child > len(self.heap) - 1 or len(self.heap) <= 1:
            return
        if self.heap[child].priority < self.heap[index].priority:
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            self._repair_heap_top_down(child)
            return
        if child + 1 > len(self.heap) - 1:
            return
        if self.heap[child+1].priority < self.heap[index].priority:
            self.heap[child+1], self.heap[index] = self.heap[index], self.heap[child+1]
            self._repair_heap_top_down(child+1)

    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]
        
