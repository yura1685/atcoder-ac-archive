#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Using a struct to represent an edge for clarity
struct Edge {
    int to;
    long long weight;
};

// Global variables for the DFS function
vector<vector<Edge>> g;
vector<bool> visited;
long long max_dist;
int farthest_node;

// Depth-First Search to find the farthest node and its distance
void dfs(int u, long long current_dist) {
    visited[u] = true;

    if (current_dist > max_dist) {
        max_dist = current_dist;
        farthest_node = u;
    }

    for (const auto& edge : g[u]) {
        if (!visited[edge.to]) {
            dfs(edge.to, current_dist + edge.weight);
        }
    }
}

int main() {
    // Speed up I/O operations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    g.resize(N);
    long long total_weight_sum = 0;

    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        --a; --b; // Adjust to 0-based indexing
        g[a].push_back({b, c});
        g[b].push_back({a, c});
        total_weight_sum += c;
    }

    // This problem is about finding the diameter of a tree
    // The diameter is the longest path between any two nodes

    // Step 1: Find one end of the diameter
    visited.assign(N, false);
    max_dist = 0;
    farthest_node = 0;
    dfs(0, 0); // Start DFS from an arbitrary node (0)

    // Step 2: Find the other end of the diameter
    visited.assign(N, false);
    max_dist = 0;
    int diameter_end_node = farthest_node; // Store the first end
    dfs(diameter_end_node, 0); // Start DFS from the farthest node found in Step 1

    // The diameter is the 'max_dist' after the second DFS
    long long diameter = max_dist;

    // The total distance of all edges is C = 2 * sum(c)
    // The problem asks for C - M, where M is the diameter
    // The total distance of all edges is `2 * total_weight_sum`
    long long result = 2 * total_weight_sum - diameter;

    cout << result << endl;

    return 0;
}