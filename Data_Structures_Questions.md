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

The runtime complexity of `insert` is worst case of `O(n)`.

2. What is the runtime complexity of `contains`?

The runtime complexity of `contains` is `O(n)`.

3. What is the runtime complexity of `get_max`?

The runtime complexity of `get_max` is `O(n)`.

## Heap

1. What is the runtime complexity of `_bubble_up`?

This private method runs in `O(log(n))` time.

2. What is the runtime complexity of `_sift_down`?

The runtime complexity of this method is `O(log(n))` in keeping with all other Binary Search-esque functionality.

3. What is the runtime complexity of `insert`?

The actual insertion of a value into the array is `O(1)`, but the bubbling up process means that this method runs in `O(log(n))` time.

4. What is the runtime complexity of `delete`?

The insertion and swap of the initial root node are `O(1)`, but the subsequent swaps of values down the tree run make this method run in `O(log(n))` time.

5. What is the runtime complexity of `get_max`?

The runtime complexity of this method is `O(1)` since we're merely looking up the first array position index's value.

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
