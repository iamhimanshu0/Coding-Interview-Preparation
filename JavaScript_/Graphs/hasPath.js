// if path is exist between src node and destination node

const hasPath = (graph, src, dst) => {
    const stack = [src]

    while(stack.length > 0){
        const current = stack.pop();

        console.log(current)
        for(let neighbor of graph[current]){
            stack.push(neighbor)
        }
    }

};

const graph = {
    f : ["g","i"],
    g : ["h"],
    h : [],
    i : ["g", "k"],
    j : ["i"],
    k : []
};

/*
    f > g > h
    | /
    i > j
    |
    k
*/

console.log(hasPath(graph, "f", "j"))
