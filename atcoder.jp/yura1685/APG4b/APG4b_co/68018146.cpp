#include <bits/stdc++.h>
using namespace std;

int main() {

    int n, p, N;
    cin >> n;

    if (n == 2){
        string text;
        cin >> text;
        cout << text + "!" << endl;
    }
    cin >> p >> N;
    cout << p * N << endl;
}
