#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define DUMP(x)  cout << #x << " = " << (x) << endl;
#define FOR(i, m, n) for(ll i = m; i < n; i++)
#define IFOR(i, m, n) for(ll i = n - 1; i >= m; i-- )
#define REP(i, n) FOR(i,0,n)
#define IREP(i, n) IFOR(i,0,n)
#define FOREACH(x,a) for(auto& (x) : (a) )
#define ALL(v) (v).begin(), (v).end()
#define SZ(x) ll(x.size())

template <typename _Ty>
ostream& operator << (ostream& ostr, const vector<_Ty>& v) {
    if (v.empty()) {
        ostr << "{ }";
        return ostr;
    }
    ostr << "{" << v.front();
    for (auto itr = ++v.begin(); itr != v.end(); itr++) {
        ostr << ", " << *itr;
    }
    ostr << "}";
    return ostr;
}

const ll MOD = 1e9+7;

int main(){
  string s; cin >> s;

  if ((SZ(s) % 3) == 1) {
    s = string("00") + s;
  } else if ((SZ(s) % 3) == 2) {
    s = string("0") + s;
  }

  ll n = (int)(SZ(s) / 3);

//   DUMP(s);

  vector<vector<ll>> dp(n+1, vector<ll>(13,0));
  dp[0][0] = 1;

  REP(k, n) REP(m, 13) {
      string str = s.substr(k*3, 3);
      vector<ll> d1;
      vector<ll> d2;
      vector<ll> d3;
    //   DUMP(str);

      if (str[0] == '?') {
        REP(i, 10) {
            d1.push_back(i);
        }
      } else {
        d1.push_back(str[0] - '0');
      }

      if (str[1] == '?') {
        REP(i, 10) {
            d2.push_back(i);
        }
      } else {
        d2.push_back(str[1] - '0');
      }

      if (str[2] == '?') {
        REP(i, 10) {
            d3.push_back(i);
        }
      } else {
        d3.push_back(str[2] - '0');
      }

    //   cout << str << d1 << d2 << d3 << endl;

      REP(i1, d1.size()) REP(i2, d2.size()) REP(i3, d3.size()) {
          ll num = 100 * d1[i1] + 10 * d2[i2] + d3[i3];
          dp[k + 1][(13 + num - m) % 13] += dp[k][m];
      }

      REP(i, 13) {
          dp[k + 1][i] %= MOD;
      }
  }

  cout << dp[n][5] << endl;
}
