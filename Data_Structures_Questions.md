Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

The runtime complexity of `enqueue` is `O(1)`.

2. What is the runtime complexity of `dequeue`?

The runtime complexity of `dequeue` is `O(1)`.

3. What is the runtime complexity of `len`?

The runtime complexity for `len` is `O(1)` since we have preserved the size of the queue in a static variable.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

The runtime of `insert_after` is `O(1)` as the process of changing pointers is always constant and doesn't impact the rest of the list.

2. What is the runtime complexity of `ListNode.insert_before`?

Same answer (`O(1)`) and reasoning as the answer above.

3. What is the runtime complexity of `ListNode.delete`?

The delete runtime is `O(1)` since we're merely changing the pointers from the previous and next `Node` points, which is a constant operation.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

The runtime complexity of `add_to_head` is `O(1)`.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

The runtime complexity of `remove_from_head` is `O(1)`.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

The runtime complexity of `add_to_tail` is `O(1)`.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

The runtime complexity of `remove_from_tail` is `O(1)`.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

The runtime complexity of `move_to_front` is `O(1)`.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

The runtime complexity of `move_to_end` is `O(1)`.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The runtime complexity of `delete` is `O(1)` since we're merely changing the pointers for a select few (nearly constant) amount of `Node` points. In contrast, the `Array.splice` method is runtime complexity of `O(n)` since
