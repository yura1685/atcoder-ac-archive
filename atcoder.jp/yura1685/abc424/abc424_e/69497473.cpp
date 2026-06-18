// Python code to be translated
/*
from collections import defaultdict
from sortedcontainers import SortedSet
from fractions import Fraction

T = int(input())
for _ in range(T):
    N, K, X = map(int,input().split())
    A = list(map(int,input().split()))
    S = SortedSet()
    d = defaultdict(int)
    for a in A:
        f = Fraction(a,1)
        if f not in S:
            S.add(Fraction(a,1))
        d[(a,1)] += 1
    while K > 0 and S:
        f = S.pop()
        up, do = f.numerator, f.denominator
        cnt = d[(up,do)]
        if K >= cnt:
            del d[(up,do)]
            K -= cnt
            new_up, new_do = up, do
            if new_up % 2 == 0:
                new_up //= 2
            else:
                new_do *= 2
            new_f = Fraction(new_up, new_do)
            if new_f not in S:
                S.add(new_f)
            d[(new_up, new_do)] += 2*cnt
        else:
            new_up, new_do = up, do
            if new_up % 2 == 0:
                new_up //= 2
            else:
                new_do *= 2
            new_f = Fraction(new_up, new_do)
            d[(up,do)] -= K
            if new_f not in S:
                S.add(new_f)
            d[(new_up, new_do)] += 2*K
            K = 0
    
    now = [Fraction(n,d) for (n,d), _ in d.items()]
    now.sort(reverse=True)
    cnt = 0
    for f in now:
        up, do = f.numerator, f.denominator
        cnt += d[(up,do)]
        if cnt >= X:
            print(float(f))
            break
*/

#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <set>
#include <algorithm>

// PythonのFractionクラスに相当する構造体
struct Fraction {
    long long num;
    long long den;

    Fraction(long long n = 0, long long d = 1) : num(n), den(d) {
        // 分数を約分する
        long long common_divisor = std::gcd(num, den);
        num /= common_divisor;
        den /= common_divisor;
        if (den < 0) {
            num = -num;
            den = -den;
        }
    }

    bool operator<(const Fraction& other) const {
        return num * other.den < other.num * den;
    }

    bool operator>(const Fraction& other) const {
        return num * other.den > other.num * den;
    }

    bool operator==(const Fraction& other) const {
        return num == other.num && den == other.den;
    }
};

// std::mapのキーとしてFractionを使用するための比較演算子
bool operator<(const std::pair<long long, long long>& a, const std::pair<long long, long long>& b) {
    return Fraction(a.first, a.second) < Fraction(b.first, b.second);
}

void solve() {
    int N;
    long long K, X;
    std::cin >> N >> K >> X;
    
    std::vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> A[i];
    }
    
    // PythonのSortedSetに相当するstd::set
    std::set<Fraction, std::greater<Fraction>> S;
    // Pythonのdefaultdictに相当するstd::map
    std::map<std::pair<long long, long long>, long long> d;

    for (int a : A) {
        Fraction f(a, 1);
        S.insert(f);
        d[{f.num, f.den}]++;
    }

    while (K > 0 && !S.empty()) {
        Fraction f = *S.begin();
        S.erase(S.begin());

        long long up = f.num;
        long long do_ = f.den;
        long long cnt = d[{up, do_}];

        if (K >= cnt) {
            d.erase({up, do_});
            K -= cnt;

            long long new_up = up;
            long long new_do = do_;
            if (new_up % 2 == 0) {
                new_up /= 2;
            } else {
                new_do *= 2;
            }
            
            Fraction new_f(new_up, new_do);
            S.insert(new_f);
            d[{new_f.num, new_f.den}] += 2 * cnt;
        } else {
            long long new_up = up;
            long long new_do = do_;
            if (new_up % 2 == 0) {
                new_up /= 2;
            } else {
                new_do *= 2;
            }

            Fraction new_f(new_up, new_do);
            d[{up, do_}] -= K;
            S.insert(new_f);
            d[{new_f.num, new_f.den}] += 2 * K;
            K = 0;
        }
    }
    
    std::vector<Fraction> now;
    for (const auto& pair : d) {
        if (pair.second > 0) { // 本数が0より大きいものだけを対象とする
            now.push_back(Fraction(pair.first.first, pair.first.second));
        }
    }
    std::sort(now.begin(), now.end(), std::greater<Fraction>());
    
    long long current_count = 0;
    for (const auto& f : now) {
        current_count += d[{f.num, f.den}];
        if (current_count >= X) {
            std::cout.precision(15);
            std::cout << static_cast<double>(f.num) / f.den << std::endl;
            return;
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int T;
    std::cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}