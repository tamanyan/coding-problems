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

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v)
{
    for (int i = 0; i < (int)v.size(); ++i) {
        os << v[i];
        if (i != (int)v.size() - 1)
            os << " ";
    }
    return os;
}

vector<vector<ll>> tree;
vector<ll> ans;

void dfs(ll i, ll p) {
    FOREACH(x, tree[i]) {
        if (x != p) {
            // cout << i << x << endl;
            ans[x] += ans[i];
            // cout << ans << endl;
            dfs(x, i);
        }
    }
}

int main(){
    int N, Q;
    cin >> N >> Q;

    tree.resize(N+1);
    ans.resize(N+1);

    REP(i, N-1) {
    	ll a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    REP(i, Q) {
    	ll p, x;
        cin >> p >> x;
        ans[p] += x;
    }

    // cout << ans << endl;
    dfs(1, -1);

    for (int i = 1; i < N+1; ++i) {
        cout << ans[i] << " ";
    }
    cout << endl;
    return 0;
}
