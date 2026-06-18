#include <iostream>
#include <set>
#include <string>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();  // 余分な改行文字を消去

    std::set<std::string> uniqueStrings;
    for (int i = 0; i < n; ++i) {
        std::string input;
        std::getline(std::cin, input);
        uniqueStrings.insert(input);
    }

    std::cout << uniqueStrings.size() << std::endl;

    return 0;
}
