#include <iostream>
using namespace std;
int main()
{
    int a, b, c, x;
    cin >> a >> b >> c >> x;

    int ans = 0;
    int tmpi, tmpj;
    for (int i = a; i >= 0; i--) {
        // 500円のループ
        tmpi = x - 500 * i;
        if (tmpi < 0) continue;
        
        for (int j = b; j >=0; j--) {
            // 100円のループ
            tmpj = tmpi - 100 * j;
            if (tmpj < 0) continue;

            // 50円の判定
            if ((50 * c) >= tmpj // 手持ちのお金でたりる
                && tmpj % 50 == 0) { // かつぴったり払える
                    ans++;
                }
        }
    }

    cout << ans << endl;

    return 0;
}