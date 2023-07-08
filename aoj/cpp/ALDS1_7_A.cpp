#include <iostream>
using namespace std;

#define MAX 100005
#define NIL -1

struct Node {
    int parent;
    int left;
    int right;
};

void printNode(struct Node tree[], int depth[], int nodeId) {
    cout << "node " << nodeId << ": ";
    cout << "parent = " << tree[nodeId].parent << ", ";
    cout << "depth = " << depth[nodeId] << ", ";

    // ノードタイプの出力
    if (tree[nodeId].parent == NIL) {
        // 根のとき
        cout << "root, ";
    } else if (tree[nodeId].left == NIL) {
        // 葉のとき
        cout << "leaf, ";
    } else {
        cout << "internal node, ";
    }

    // 子の出力
    cout << "[";
    for (int i = 0, child = tree[nodeId].left; child != NIL; child = tree[child].right, i++) {
        if (i) cout << ", ";
        cout << child;
    }
    cout << "]" << endl;
}

void setDepth (struct Node tree[], int depth[], int nodeId, int dep = 0) {
    depth[nodeId] = dep;
    if (tree[nodeId].right != NIL) {
        // 右端の兄弟までたどる(深さは同じ)
        setDepth(tree, depth, tree[nodeId].right, dep);
    }
    if (tree[nodeId].left != NIL) {
        // 深さを増やして子へ移る
        setDepth(tree, depth, tree[nodeId].left, dep + 1);
    }
}

int main() {
    struct Node tree[MAX];
    int depth[MAX];

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        // 先にすべてNILで初期化しておく
        tree[i].parent = tree[i].left = tree[i].right = NIL;
    }


    for (int i = 0; i < n; i++) {
        int me, k, previousChild;
        cin >> me >> k;
        for (int j = 0; j < k; j++) {
            // 今扱っている子ノード
            int child;
            cin >> child;
            if (j == 0) {
                // (1)左端の子はleftに追加
                tree[me].left = child;
            } else {
                // (2)1つ前の子ノードのrightに追加
                tree[previousChild].right = child;
            }
            // 次の子ノードの処理時に使うので保存しておく
            previousChild = child;
            // 子ノードのparentに自分を追加
            tree[child].parent = me;
        } 
    }

    // 根ノードのnodeIdを確保しておく(setDepthで使うため)
    int root;
    for (int i = 0; i < n; i++) {
        if (tree[i].parent == NIL) {
            root = i;
        }
    }

    setDepth(tree, depth, root);

    for (int i = 0; i < n; i++) printNode(tree, depth, i);

    return 0;
}
