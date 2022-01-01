// given a graph "check how many connected 
// component in the graph" 

/*
    1 -> 2 

         4
         |   
    5 -> 6 -> 8
         |
         7

    3

 if n = nodes, e = edges
 time : o(e)
 space : o(n)

in this graph we have 3 connected components
*/

const graph = {
    3 :[],
    4 :[6],
    6 :[4,5,7,8],
    8 :[6],
    7 :[6],
    5 :[6],
    1 :[2],
    2 :[1]
}


const graph1 = {
    0 : [8,1,5],
    1 : [0],
    5 : [0,8],
    8 : [0,5],
    2 : [3,4],
    3 : [2,4],
    4 : [3,2]
}  // -> 2

const connectedComponentsCount = (graph)=>{
    const visited = new Set()
    let count = 0 

    for (let node in graph){
       
        if(explore(graph, node, visited) === true){
            count +=1;
        }  
    }

    return count;
}

const explore = (graph, current, visited) => {
    
    // check for cycle
    if(visited.has(String(current))) return false;
    
    visited.add(String(current));

    for(let n of graph[current]){
        explore(graph, n, visited)
    }

    return true;

}

console.log(
    connectedComponentsCount(graph)
)





// let list = [4, 5, 6];

// for (let i in list) {
//    console.log(i); // "0", "1", "2",
// }

// for (let i of list) {
//    console.log(i); // "4", "5", "6"
// }

