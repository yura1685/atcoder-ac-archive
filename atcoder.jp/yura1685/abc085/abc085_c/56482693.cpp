#include <iostream>

int main() {
    int maisu, yen;
    std::cin >> maisu >> yen;
    
    for (int x = 0; x <= maisu; ++x) {
        for (int y = 0; y <= maisu - x; ++y) {
            int z = maisu - x - y;
            if (10000 * x + 5000 * y + 1000 * z == yen) {
                std::cout << x << " " << y << " " << z << std::endl;
                return 0;
            }
        }
    }
    
    std::cout << "-1 -1 -1" << std::endl;
    return 0;
}
