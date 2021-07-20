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

  // merge two list
  merge_to_list(list2) {
    var p = this.head;
    var q = list2.head;
    var s;
    var new_node;

    if (!p) return q;
    if (!q) return p;

    if (p && q) {
      if (p.data <= q.data) {
        s = p;
        p = p.next;
      } else {
        s = q;
        q = q.next;
      }
    }

    new_node = s;

    while (p && q) {
      if (p.data <= q.data) {
        s.next = p;
        s = p;
        p = p.next;
      } else {
        s.next = q;
        s = q;
        q = q.next;
      }
    }

    if (!p) s.next = q;
    if (!q) s.next = p;

    // console.log(new_node);
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

var llist1 = new Linkedlist();
llist1.append("1");
llist1.append("3");
llist1.append("5");
llist1.append("7");
llist1.append("9");
llist1.append("10");

var llist2 = new Linkedlist();
llist2.append("2");
llist2.append("4");
llist2.append("6");
llist2.append("8");

llist1.merge_to_list(llist2);

// llist.add_at_given("5", "4");
// llist.delete_data("2");
llist1.print();
// llist1.findMiddle();
// llist1.sumAndLength();
