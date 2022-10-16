const canFinish = function(numCourses, prerequisites) {
    const graph = Array.from(Array(numCourses), () => []);
    const visited= Array.from(Array(numCourses), () => false)
    const finished = Array.from(Array(numCourses), () => false)
    let isPossible = true

    const dfs = (node) => {
        if(finished[node]) return
        visited[node] = true;
        for(let nx of graph[node]){
            if(visited[nx]){
                if(!finished[nx]){
                    isPossible = false;
                }
            }else{
                dfs(nx)
            }
        }
        finished[node] = true;
    }

    for (let [from, to] of prerequisites) {
        graph[from].push(to);
    }

    for(let arr of graph) {
        for (let i of arr) {
            dfs(i)
        }
    }
    console.log(isPossible)
};

canFinish(2, [[1,0],[0,1]]);