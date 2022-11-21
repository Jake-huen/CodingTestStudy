#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2,fma")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
 
#include "bits/stdc++.h"
#include "ext/rope"
 
using namespace std;
using namespace __gnu_cxx;
 
using ll = int_fast64_t;
using pii = pair<int, int>;
 
int n;
int ar[3001];
int pref[3001];
int dp[3001];
 
int get_segsum(int l, int r)
{
  return pref[r] - pref[l - 1];
}
 
int memo(int cur)
{
  if (cur > n) return 0;
  auto &ret = dp[cur];
  if (ret != -1e9) return ret;
  ret = 0;
  int tmp = 1e9;
 
  for (int i = cur; i <= n; i++)
  {
    tmp = min(tmp, get_segsum(cur, i) - memo(i + 1));
  }
  return ret = tmp;
}
 
void solve()
{
  cin >> n;
  int tc = 3;
  while (tc--)
  {
    for (int i = n; i >= 1; i--)
    {
      cin >> ar[i];
    }
    for (int i = 1; i <= n; i++)
    {
      pref[i] = pref[i - 1] + ar[i];
    }
 
    fill(dp, dp + 3001, -1e9);
    int res = memo(1);
    if (res < 0) cout << "A\n";
    else if (res > 0) cout << "B\n";
    else cout << "D\n";
  }
}
 
int main()
{
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
#endif
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
 
  solve();
}
