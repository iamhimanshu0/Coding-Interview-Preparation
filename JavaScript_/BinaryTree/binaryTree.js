class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BinaryTree {
  constructor(root) {
    this.root = new Node(root);
  }

  print_tree(traversal_type) {
    if (traversal_type == "pre") {
      return this.preorder_print(tree.root, "");
    } else if (traversal_type == "in") {
      return this.inorder_print(tree.root, "");
    } else if (traversal_type == "post") {
      return this.postorder_print(tree.root, "");
    }
  }

  preorder_print(start, traversal) {
    // root->left->right
    if (start) {
      traversal += start.value + "-";
      traversal = this.preorder_print(start.left, traversal);
      traversal = this.preorder_print(start.right, traversal);
    }
    return traversal;
  }

  inorder_print(start, traversal) {
    // left->root->right
    if (start) {
      traversal = this.inorder_print(start.left, traversal);
      traversal += start.value + "-";
      traversal = this.inorder_print(start.right, traversal);
    }
    return traversal;
  }

  postorder_print(start, traversal) {
    // left->right->root
    if (start) {
      traversal = this.postorder_print(start.left, traversal);
      traversal = this.postorder_print(start.right, traversal);
      traversal += start.value + "-";
    }
    return traversal;
  }
}

// #              1
// #            /   \
// #           2     3
// #          /\     /\
// #         4 5     6 7

let tree = new BinaryTree(1);
tree.root.left = new Node(2);
tree.root.right = new Node(3);
tree.root.left.left = new Node(4);
tree.root.left.right = new Node(5);
tree.root.right.left = new Node(6);
tree.root.right.right = new Node(7);

console.log(tree.print_tree("pre"));
console.log(tree.print_tree("in"));
console.log(tree.print_tree("post"));
