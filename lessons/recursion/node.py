"""Class Node."""

from __future__ import annotations

class Node:
    """My Node Class for linked lists."""

    data: int
    next: Node | None

    def __init__(self, data_inp: int, next_inp: Node | None):
        """Construct Node."""
        self.data = data_inp
        self.next = next_inp

    def __str__(self) -> str:
        """Produce a string visualization for the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """It returns the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """It returns a linked list of every element minus the head."""
        if self.next is None:
            return None
        else:
            return self.next
        return None
    
    def last(self) -> int:
        """It returns the data of the last element in the linked list"""
        node_var = self.next
        if node_var is None:
            return self.data
        else:
            while node_var is not None:
                data = node_var.data
                node_var = node_var.next
                if node_var is None:
                    return data