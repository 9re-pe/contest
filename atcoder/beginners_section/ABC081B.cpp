#include <iostream>
using namespace std;
int main()
{
    int n;
    int N[200];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> N[i];

    int ans = 0;
    bool onemore = true;
    while (onemore) {
        for (int i = 0; i < n; i++) {
            int a = N[i];
            
            if (a % 2 == 0) {
                N[i] = a / 2;
                // 最後の要素までいったら操作数を1増やす
                if (i == n - 1) ans++;
            } else {
                onemore = false;
                break;
            }
        }
    }
    
    cout << ans << endl;

    return 0;
}