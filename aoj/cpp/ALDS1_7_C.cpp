#include <iostream>
using namespace std;

#define MAX 10000
#define NIL -1

struct Node {
    int parent;
    int left;
    int right;
};

void preParse(struct Node tree[], int nodeId) {
    if (nodeId == NIL) return;

    cout << " " << nodeId;
    preParse(tree, tree[nodeId].left); 
    preParse(tree, tree[nodeId].right); 
}

void inParse(struct Node tree[], int nodeId) {
    if (nodeId == NIL) return;

    inParse(tree, tree[nodeId].left); 
    cout << " " << nodeId;
    inParse(tree, tree[nodeId].right); 
}

void postParse(struct Node tree[], int nodeId) {
    if (nodeId == NIL) return;

    postParse(tree, tree[nodeId].left); 
    postParse(tree, tree[nodeId].right); 
    cout << " " << nodeId;
}

int main() {
    struct Node tree[MAX];

    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        tree[i].parent = NIL;
    }

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

    cout << "Preorder" << endl;
    preParse(tree, root);
    cout << endl;

    cout << "Inorder" << endl;
    inParse(tree, root);
    cout << endl;
    
    cout << "Postorder" << endl;
    postParse(tree, root);
    cout << endl;

    return 0;
}
