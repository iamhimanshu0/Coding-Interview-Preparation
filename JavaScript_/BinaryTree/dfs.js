class Node{
  constructor(val){
    this.val =  val;
    this.left = null;
    this.right= null;
  }
  
}

const depthFirstValue = (root) =>{
  
  if (root === null)return [];
  
  const result = [];
  const stack = [root];
  while(stack.length > 0){
    const current = stack.pop()
    
   result.push(current.val);
   
    if (current.left)
      stack.push(current.left)
    if (current.right)
      stack.push(current.right)
      
  
    
  }
  return result;
  
}


const depthFirstValueRecurssive = (root) =>{
  
  if(root === null) return [];
  
  const leftValues =  depthFirstValueRecurssive(root.left);
  const rightValues = depthFirstValueRecurssive(root.right);
  
  return [root.val, ...leftValues, ...rightValues]
  
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


console.log(
  depthFirstValue(a)
)