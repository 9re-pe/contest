#include <iostream>
using namespace std;

#define MAX 10000
#define NIL -1

struct Node {
    int parent;
    int left;
    int right;
};

void setDepth(struct Node tree[], int depth[], int nodeId, int dep = 0) {
    if (nodeId == NIL) return;

    depth[nodeId] = dep;

    setDepth(tree, depth, tree[nodeId].left, dep + 1);
    setDepth(tree, depth, tree[nodeId].right, dep + 1);
}

int setHeight(struct Node tree[], int height[], int nodeId) {
    int leftHeight = 0;
    int rightHeight = 0;
    if (tree[nodeId].left != NIL) {
        leftHeight = setHeight(tree, height, tree[nodeId].left) + 1;
    }
    if (tree[nodeId].right != NIL) {
        rightHeight = setHeight(tree, height, tree[nodeId].right) + 1;
    }
    height[nodeId] = (leftHeight > rightHeight ? leftHeight : rightHeight);

    return height[nodeId];
}

int getSibling(struct Node tree[], int nodeId) {
    if (tree[nodeId].parent == NIL) {
        // 根のとき
        return NIL;
    } else if (tree[tree[nodeId].parent].left == nodeId) {
        // 自分が左の子のとき
        return tree[tree[nodeId].parent].right;
    } else {
        // 自分が右の子のとき
        return tree[tree[nodeId].parent].left;
    }
}

void printNode(struct Node tree[], int depth[], int height[], int nodeId) {
    cout << "node " << nodeId << ": ";
    cout << "parent = " << tree[nodeId].parent << ", ";
    cout << "sibling = " << getSibling(tree, nodeId) << ", ";

    int degree = 0;
    if (tree[nodeId].left != NIL) degree++;
    if (tree[nodeId].right != NIL) degree++;
    cout << "degree = " << degree << ", ";

    cout << "depth = " << depth[nodeId] << ", ";
    cout << "height = " << height[nodeId] << ", ";

    if (tree[nodeId].parent == NIL) {
        cout << "root" << endl;
    } else if (tree[nodeId].left == NIL && tree[nodeId].right == NIL) {
        cout << "leaf" << endl;
    } else {
        cout << "internal node" << endl;
    }
}

int main() {
    struct Node tree[MAX];
    int depth[MAX];
    int height[MAX];

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) tree[i].parent = NIL;

    int me, left, right;
    for (int i = 0; i < n; i++) {
        cin >> me >> left >> right;
        tree[me].left = left;
        tree[me].right = right;
        if (left != NIL) tree[left].parent = me;
        if (right != NIL) tree[right].parent = me;
    }

    int root;
    for (int i = 0; i < n; i++) {
        if (tree[i].parent == NIL) {
            root = i;
        }
    }

    setDepth(tree, depth, root);
    setHeight(tree, height, root);

    for (int i = 0; i < n; i++) {
        printNode(tree, depth, height, i);
    }

    return 0;
}
