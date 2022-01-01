/*
     5
     |   \
1 -> 0 -> 8

4 -> 2
  \/
  3

*/

const graph1 = {
    0 : [8,1,5],
    1 : [0],
    5 : [0,8],
    8 : [0,5],
    2 : [3,4],
    3 : [2,4],
    4 : [3,2]
}  

const largest = (graph) =>{
    // first traversal and get component
    
}
