//
//     You are given the head of a singly linked-list. The list can be represented as:
//         L0 → L1 → … → Ln - 1 → Ln
//     Reorder the list to be on the following form:
//         L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

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

  reorderList() {
    //   find middle
    var slow = this.head;
    var fast = this.head.next;

    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }

    var second = slow.next;
    slow.next = null;

    // reverse the second one
    var prev = null;
    while (second) {
      var tmp = second.next;
      second.next = prev;
      prev = second;
      second = tmp;
    }

    // merge and reorder
    var first = this.head;
    var second = prev;

    while (second) {
      var tmp1 = first.next;
      var tmp2 = second.next;
      first.next = second;
      second.next = tmp1;

      first, (second = tmp1), tmp2;
    }
  }
}

var llist = new LinkedList();

llist.append(1);
llist.append(2);
llist.append(3);
llist.append(4);
llist.reorderList();
llist.printList();
