//     Given the head of a singly linked list, reverse the list, and return the reversed list.
//     Input: head = [1,2,3,4,5]
//     Output: [5,4,3,2,1]
//     https://leetcode.com/problems/reverse-linked-list/

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  append(value) {
    var new_node = new Node(value);

    if (this.head === null) {
      this.head = new_node;
      return;
    }

    var cur_node = this.head;
    while (cur_node.next) {
      cur_node = cur_node.next;
    }

    cur_node.next = new_node;
  }

  printList() {
    var cur_node = this.head;
    while (cur_node) {
      console.log(cur_node.value);
      cur_node = cur_node.next;
    }
  }

  reverse() {
    var prev = null;
    var cur_node = this.head;
    var nxt = null;

    while (cur_node) {
      nxt = cur_node.next;
      cur_node.next = prev;

      prev = cur_node;
      cur_node = nxt;
    }
    this.head = prev;
  }
}

var llist = new LinkedList();
llist.append(1);
llist.append(2);
llist.append(3);
llist.append(4);
llist.append(5);
llist.reverse();
llist.printList();
