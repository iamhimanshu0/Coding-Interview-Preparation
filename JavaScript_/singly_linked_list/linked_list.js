class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Linkedlist {
  constructor() {
    this.head = null;
  }

  //   append the data items
  append(data) {
    var new_node = new Node(data);
    var cur_node;
    // check if head in null
    if (this.head == null) {
      this.head = new_node;
      return;
    } else {
      cur_node = this.head;

      while (cur_node.next) {
        cur_node = cur_node.next;
      }
    }

    cur_node.next = new_node;
  }

  //   prepend the data items
  prepend(data) {
    var new_node = new Node(data);
    var cur_node = this.head;

    new_node.next = cur_node;
    this.head = new_node;
  }

  //   add at given position
  add_at_given(data, pos) {
    var new_node = new Node(data);
    var cur_node = this.head;

    while (cur_node) {
      if (cur_node.data == pos) {
        new_node.next = cur_node.next;
        cur_node.next = new_node;
        return;
      }
      cur_node = cur_node.next;
    }
  }

  //   delete at given pos
  delete_data(data) {
    var cur_node = this.head;
    var prev_node;
    while (cur_node) {
      prev_node = cur_node;
      cur_node = cur_node.next;
      if (cur_node.data == data) {
        prev_node.next = cur_node.next;
        cur_node = null;
      }
    }
  }

  //   find middle
  findMiddle() {
    var slow_node = this.head;
    var fast_node = this.head.next;

    while (fast_node && fast_node.next) {
      slow_node = slow_node.next;
      fast_node = fast_node.next.next;
    }
    console.log("Middle Node is", slow_node.data);
  }

  //   length and sum of the elemnt
  sumAndLength() {
    var cur_node = this.head;
    var count = 0;
    var sum = 0;
    while (cur_node) {
      count += 1;
      sum += Number(cur_node.data);

      cur_node = cur_node.next;
    }
    console.log(
      "The Number of Element in the Linkedlist is",
      count,
      "and the sum of the elements are",
      sum
    );
  }

  //   print the linked list
  print() {
    var cur_node = this.head;
    while (cur_node) {
      console.log(cur_node.data);
      cur_node = cur_node.next;
    }
  }
}

var llist = new Linkedlist();
llist.append("1");
llist.append("2");
llist.append("3");
llist.append("4");
llist.append("5");
llist.append("6");
// llist.add_at_given("5", "4");
// llist.delete_data("2");
llist.print();
llist.findMiddle();
llist.sumAndLength();
