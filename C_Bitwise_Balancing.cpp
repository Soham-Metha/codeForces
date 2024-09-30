#include <iostream>
#include <limits>

int main() {
    int tc;
    std::cin >> tc;
    while (tc--) {
        long long b, c, d;
        std::cin >> b >> c >> d;
        long long a = -1;
        long long mx = 2305843009213693952LL;
        for (long long i = 0; i < mx; ++i) {
            if ((i | b) + ~(i & c)  + 1== d) {
                a = i;
                break;
            }
        }
        std::cout << a << std::endl;
    }
    return 0;
}

