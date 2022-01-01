const edges = [
    ["i", "j"],
    ['k', "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
];

// check cycle in undirected graph

const undirectedPath = (edges, nodeA, nodeB) => {
    const graph = buildGraph(edges)
    // console.log(graph)
    return hasPath(graph, nodeA, nodeB, new Set())
}


// travel in graph
const hasPath = (graph, src, des, visited) => {
    if(des === src) return true;

    // check for cycle
    if(visited.has(src)) return false;
    visited.add(src);


    for (let n of graph[src]){
        if((hasPath(graph, n, des, visited)) === true){
            return true;
        }
    }

    return false
}



// make graph form edges
const buildGraph = (edges)=> {
    const graph = {};

    for (let edge of edges){
        const [a, b] = edge;

        if (!(a in graph))graph[a] = [];
        if (!(b in graph))graph[b] = [];

        graph[a].push(b);
        graph[b].push(a);

    }

    return graph;
    
    
}

console.log(undirectedPath(edges, "j", "n"))