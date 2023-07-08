#include <iostream>
using namespace std;

#define N 100
#define WHITE 0
#define GRAY 1
#define BLACK 2

int n; // 頂点の数
int M[N][N]; // 隣接行列
int color[N]; // 各頂点の訪問状態
int d[N]; // 各頂点の発見時刻
int f[N]; // 各頂点の完了時刻
int tt; // 時刻

void dfs_visit(int u) {
    // u: 現在訪問中の頂点
    // v: 次に訪問する頂点
    
    // 発見
    color[u] = GRAY;
    d[u] = ++tt; 
    for (int v = 0; v < n; v++) {
        if (M[u][v] == 0) continue; // 辺が存在しないとき
        if (color[v] == WHITE) {
            // まだvが未訪問ならvを訪問
            dfs_visit(v);
        } 
    }
    // 完了
    color[u] = BLACK;
    f[u] = ++tt;
}

void dfs() {
    //初期化
    for (int u = 0; u < n; u++) color[u] = WHITE;
    tt = 0;

    for (int u = 0; u < n; u++) {
        // 未訪問のuを始点として深さ優先探索
        if (color[u] == WHITE) dfs_visit(u);
    }

    for (int u = 0; u < n; u++) {
        cout << u + 1 << " " << d[u] << " " << f[u] << endl;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            M[i][j] = 0;
        }
    }

    int u, k, v;
    for (int i = 0; i < n; i++) {
        cin >> u >> k;
        u--;
        for (int j = 0; j < k; j++) {
            cin >> v;
            v--;
            M[u][v] = 1; 
        }
    }

    dfs();

    return 0;
}
