#include <iostream>
#include <algorithm>
using namespace std;

static const int N = 100;

int main() {
    int n;
    cin >> n;

    int p[N + 1];
    for (int i = 1; i <= n; i++) {
        cin >> p[i - 1] >> p[i];
    }

    int m[N + 1][N + 1];
    for (int i = 1; i <= n; i++) m[i][i] = 0;

    for (int l = 2; l <= n; l++) {
        // l は計算するオペラントの幅を表す
        for (int i = 1; i <= n - l + 1; i++) {
            // iは計算するオペラントのスタートを表す
            // jは計算するオペラントのゴールを表す
            int j = i + l - 1;
            m[i][j] = (1 << 21);
            for (int k = i; k <= j - 1; k++) {
                m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]);
            }
        }
    }

    cout << m[1][n] << endl;

    return 0;
}
