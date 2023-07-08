#include <iostream>
using namespace std;

static const int MAX = 100;
static const int INFTY = (1<<21);
static const int WHITE = 0; // Tに未追加な頂点
static const int GRAY = 1;
static const int BLACK = 2; // Tに追加された頂点

int n;
int M[MAX][MAX];

int prim() {
    int u, minv;
    int d[MAX];
    int p[MAX]; // p[v]: 頂点(節点)vの親
    int color[MAX]; // color[v]: 頂点vの訪問状態

    // 各状態保存配列の初期化
    for (int i = 0; i < n; i++) {
        d[i] = INFTY;
        p[i] = -1;
        color[i] = WHITE;
    }

    // 任意の頂点を選びそれをMSTのルートとしてTに追加
    d[0] = 0;

    while (1) {
        minv = INFTY;
        u = -1;

        // 重さ最小の辺を決定(uを決定)
        for (int i = 0; i < n; i++) {
            if (d[i] < minv && color[i] != BLACK) {
                minv = d[i]; // 最小を決定するための処理
                u = i; // uを決定
            }
        }

        // V - T に頂点が残っていなかったら終了(uが-1のまま何も選ばれなかったとき)
        if (u == -1) break;

        // uをTに追加
        color[u] = BLACK;

        // 追加可能な頂点vを選択し、vをつないだ時に増える最小コストを計算
        for (int v = 0; v < n; v++) {
            if (color[v] != BLACK && M[u][v] != INFTY) {
                // 追加可能な頂点を選択
                // Tにまだ追加されていない かつ uとの辺を持っている頂点
                if (M[u][v] < d[v]) {
                    // d[v]をもっと小さくできるとき
                    d[v] = M[u][v]; // d[v]を更新
                    p[v] = u; // d[v]が成立したときにどこの頂点から来たかを保存
                    color[v] = GRAY;
                }
            }
        }
    }

    // 最小全域木の合計コストを計算
    int sum = 0;
    for (int i = 0; i < n; i++) {
        if (p[i] != -1) { // 木の根に対する例外処理
            sum += M[i][p[i]];
        }
    }

    return sum;
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int e;
            cin >> e;
            M[i][j] = (e == -1) ? INFTY : e;
        }
    }

    cout << prim() << endl;

    return 0;
}
