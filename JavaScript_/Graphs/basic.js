// graph = nodes + edges

/*
    a -> c
    |    |
    b <- e
    |
    d <- f
*/

// Directed graph and undirected graph

// adjacency list 

// depth first traversal (STACK)
// a,b,d,c,e

// Breadth first traversal (QUEUE)
// a,b,c


const graph = {
    a : ["b","c"],
    b : ["d"],
    c : ["e"],
    d : ["f"],
    e : [],
    f : []
};

// const graph = {
//     f : ["g","i"],
//     g : ["h"],
//     h : [],
//     i : ["g", "k"],
//     j : ["i"],
//     k : []
// };


const depthFirstPrint = (graph, source) => {
    const stack = [source];

    while (stack.length > 0){
        const current = stack.pop();
        console.log(current)
        for(let neighbor of graph[current]){
            stack.push(neighbor)
        }

    }     
   
};

const depthFirstPrintRecurssive = (graph, source) => {
     console.log(source);
     for (let neighbor of graph[source]){
         depthFirstPrintRecurssive(graph, neighbor)
     }

};

 
const breadthFirstPrint = (graph, source) =>{
    const queue = [source];

    while(queue.length > 0){
        const current = queue.shift();
        console.log(current)
        for (let neighbor of graph[current]){
            queue.push(neighbor)
        }
    }

}


breadthFirstPrint(graph, 'a')
// depthFirstPrint(graph, 'a')