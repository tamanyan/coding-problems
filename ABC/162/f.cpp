#include<iostream>
#include<string>
#include<vector>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<stack>
#include<list>
#include<map>
#include<deque>
#include<math.h>
using namespace std;
#define ll long long
#define FOR(i,n) for(int i = 0; i < n; i++)

int N;
ll A[202020];

ll dp[202020][2][3];

int main() {
	int i,j,k,l,r,x,y; string s;

	cin>>N;

	FOR(i,N+1) FOR(x,2) FOR(y,3) dp[i][x][y]=-1LL<<30;
	dp[0][1][0]=0;

    // FOR(j,2) {
    //     string a = dp[i][j][0] == -1LL<<30 ? "-INF" : std::to_string(dp[i][j][0]);
    //     string b = dp[i][j][1] == -1LL<<30 ? "-INF" : std::to_string(dp[i][j][1]);
    //     string c = dp[i][j][2] == -1LL<<30 ? "-INF" : std::to_string(dp[i][j][2]);
    //     cout << a << ", " << b << ", " << c << endl;
    // }

	FOR(i,N) {
		cin>>x;
		FOR(j,2) FOR(k,3) {
			// not take
			if(k+j<3) dp[i+1][1][k+j]=max(dp[i+1][1][k+j],dp[i][j][k]);
			// take
			if(j==1) dp[i+1][0][k]=max(dp[i+1][0][k],dp[i][j][k]+x);
		}
        FOR(j,2) {
            string a = dp[i+1][j][0] == -1LL<<30 ? "-INF" : std::to_string(dp[i+1][j][0]);
            string b = dp[i+1][j][1] == -1LL<<30 ? "-INF" : std::to_string(dp[i+1][j][1]);
            string c = dp[i+1][j][2] == -1LL<<30 ? "-INF" : std::to_string(dp[i+1][j][2]);
            cout << "dp" << j << " " << a << ", " << b << ", " << c << endl;
        }
	}

	if(N%2==0) cout<<max(dp[N][1][0],dp[N][0][1])<<endl;
	else cout<<max(dp[N][0][2],dp[N][1][1])<<endl;
    return 0;
}
