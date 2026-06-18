#include <iostream>
#include <map>
#include <set>
#include <algorithm> // Required for std::max and std::min

int main() {
    std::ios_base::sync_with_stdio(false); // Optimize C++ standard streams for faster input/output.
    std::cin.tie(NULL); // Untie cin from cout.

    std::map<int, int> d; // Corresponds to Python's defaultdict(int)
    std::set<int> s;     // Corresponds to Python's set()

    int Q;
    std::cin >> Q;

    for (int i = 0; i < Q; ++i) {
        int type;
        std::cin >> type;

        if (type == 1) {
            int x;
            std::cin >> x;
            s.insert(x);
            d[x]++;
        } else if (type == 2) {
            int x, c;
            std::cin >> x >> c;
            
            // Check if x exists in the map
            auto it = d.find(x);
            if (it == d.end()) { // If x is not in d, continue as in Python
                continue;
            }

            int p = it->second; // Get the current count of x
            
            if (p <= c) {
                s.erase(x); // Remove x from set if its count is less than or equal to c
                d.erase(it); // Remove x from the map
            } else {
                it->second -= c; // Decrease the count of x by c
            }
        } else if (type == 3) {
            // In C++, sets are ordered, so *s.rbegin() is max and *s.begin() is min.
            std::cout << *s.rbegin() - *s.begin() << "\n";
        }
    }

    return 0;
}