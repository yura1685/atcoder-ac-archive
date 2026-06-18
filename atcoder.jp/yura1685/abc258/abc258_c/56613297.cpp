#include <iostream>
#include <vector>
#include <string>

int main() {
    int N, Q;
    std::cin >> N >> Q;
    
    std::string S;
    std::cin >> S;

    int sta = 0;
    for (int i = 0; i < Q; ++i) {
        int t, x;
        std::cin >> t >> x;

        if (t == 1) {
            sta = (sta + x) % N;
        } else if (t == 2) {
            std::cout << S[(x - 1 - sta + N) % N] << std::endl;
        }
    }

    return 0;
}
