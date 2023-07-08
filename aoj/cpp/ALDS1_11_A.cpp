#include <iostream>
using namespace std;

static const int N = 100;

int main() {
    int n;
    cin >> n;

    int M[N][N];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            M[i][j] = 0;
        }
    }

    int u, k, v;
    for (int i = 0; i < n; i++) {
        cin >> u >> k;
        // 0オリジンへの変換
        u = u - 1;
        for (int j = 0; j < k; j++) {
            cin >> v;
            // 0オリジンへの変換
            v = v - 1;
            M[u][v] = 1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j) cout << " ";
            cout << M[i][j];
        }
        cout << endl;
    }

    return 0;
}
