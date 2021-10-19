class Node{
  constructor(val){
    this.val =  val;
    this.left = null;
    this.right= null;
  }
  
}

const breadthFirstValue = (root) =>{
  if (root === null) return [];
  
  const values = []
  const queue = [root];
  
  
  while (queue.length > 0){
    const current = queue.shift();
    values.push(current.val);
    
    if (current.left != null) queue.push(current.left);
    if (current.right != null) queue.push(current.right);
    
    
  }
  
  return values
  
}


const a = new Node("A")
const b = new Node("B")
const c = new Node("C")
const d = new Node("D")
const e = new Node("E")
const f = new Node("F")

a.left = b;
a.right = c;
b.left = d ;
b.right = e ;
c.right = f;

// #     a
// #    /  \
// #    b  c
// #  /  \  \
// #  d  e   f

console.log(
  breadthFirstValue(a)
)