#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define rep(i, n) for(ll i = 0; i < (int)n; ++i)
#define FOR(i, a, b) for(ll i = a; i < (int)b; ++i)
#define vi vector<int>
#define vs vector<string>
#define vll vector<ll>

const int Inf = 1e9;
const double EPS = 1e-9;
const ll MAX = 1000000000;

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int bitCount(long bits) {
    bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555);
    bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333);
    bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f);
    bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff);
    return (bits & 0x0000ffff) + (bits >>16 & 0x0000ffff);
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    ll S;
    cin >> S;
    ll x1, x2, x3, y1, y2, y3;
    x1 = x3 = y1 = y2 = 0;

    y3;
    x2;

    cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;

    return 0;
}
