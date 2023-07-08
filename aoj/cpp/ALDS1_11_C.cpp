#include <iostream>
#include <queue>
using namespace std;

static const int N = 100;
static const int INFTY = (1<<21);

int n;
int M[N][N];
int d[N];

void bfs(int s) {
    // sは始点
    queue<int> q;
    q.push(s);
    for (int i = 0; i < n; i++) {
        // 未訪問の状態を距離無限で表す
        d[i] = INFTY;
    }
    
    // 探索
    d[s] = 0;
    int u;
    while(!q.empty()) {
        u = q.front(); q.pop();
        // uの隣接頂点を順に調べていく
        for (int v = 0; v < n; v++) {
            if (M[u][v] == 0) continue;
            if (d[v] != INFTY) continue;
            d[v] = d[u] + 1;
            q.push(v);
            d[v] = d[u] + 1;
            q.push(v);
        }
    }
    
    // 出力
    for (int i = 0; i < n; i++) {
        cout << i + 1 << " " << ((d[i] == INFTY) ? (-1) : d[i]) << endl;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < 0; i++) {
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

    bfs(0);

    return 0;
}
