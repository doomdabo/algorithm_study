#include <bits/stdc++.h>
using namespace std;
int a[1000000];
int ans[1000000];
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  stack<int> s;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = n - 1; i >= 0; i--)
  {
    while (!s.empty() && s.top() <= a[i])
      s.pop();
    //만약 스택 비어있지 않고 들어온 수가 top보다 작으면 top에 있는거 pop
    if (s.empty())
      ans[i] = -1; //더 큰수가 없다? 그럼 -1
    else
      ans[i] = s.top(); //정답 저장!
    s.push(a[i]);
  }
  for (int i = 0; i < n; i++)
  {
    cout << ans[i] << " ";
  }
}