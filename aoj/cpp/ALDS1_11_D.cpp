#include <iostream>
#include <vector>
#include <stack>
using namespace std;

static const int MAX = 100000;
static const int NIL = -1;

int n;
vector<int> G[MAX];
int color[MAX];

void dfs(int r, int c) {
    // r : 始点
    // c : 始点rと連結であることを表すための色

    // スタックによる深さ優先探索
    stack<int> S;
    S.push(r);
    color[r] = c;
    while (!S.empty()) {
        int u = S.top(); S.pop();
        for (int i = 0; i < G[u].size(); i++) {
            // uと隣接する各頂点について
            int v = G[u][i];
            if (color[v] == NIL) {
                // 探索した際に色をつける
                color[v] = c;
                S.push(v);
            }
        }
    }
}

void assignColor() {
    int id = 1;

    // color[]の初期化
    for (int i = 0; i < n; i++) {
        color[i] = NIL;
    }

    // 各頂点に色を割り当て
    for (int u = 0; u < n; u++) {
        if (color[u] == NIL) {
            // 色はidを利用
            dfs(u, id++);
        }
    }
}

int main() {
    int s, t, m, q;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> s >> t;
        G[s].push_back(t);
        G[t].push_back(s);
    }

    assignColor();

    cin >> q;

    for (int i = 0; i < q; i++) {
        cin >> s >> t;
        if (color[s] == color[t]) {
            cout << "yes" << endl;
        } else {
            cout << "no" << endl;
        }
    }

    return 0;
}
