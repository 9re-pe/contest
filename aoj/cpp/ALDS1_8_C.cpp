#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

struct Node {
    int key;
    struct Node *parent;
    struct Node *left;
    struct Node *right;
};

Node *root, *NIL;

Node * treeMinimux(Node *node) {
    while (node->left != NIL) {
        node = node->left;
    }

    return node;
}

Node * treeSuccessor(Node *node) {
    if (node->right != NIL) {
        return treeMinimux(node->right);
    }
    Node *y = node->parent;
    while (y != NIL && node == y->right) {
        // 親がいないか、nodeが親(y)の左の子であったら終了
        node = y;
        y = y->parent;
    }

    // 左の子の親を返す
    return y;
}

void insert(int key) {
    Node *y = NIL;
    Node *x = root;
    Node *z;

    z = (Node *)malloc(sizeof(Node));
    z->key = key;
    z->left = NIL;
    z->right = NIL;

    while (x != NIL) {
        y = x;
        if (z->key < x->key) {
            x = x->left;
        } else {
            x = x->right;
        }
    }

    z->parent = y;
    if (y == NIL) {
        root = z;
    } else if (z->key < y->key) {
        y->left = z;
    } else {
        y->right = z;
    }
}

// 見つかったとき->該当するnodeを返す
// 見つからなかったとき->NILを返す
Node * find(Node *node, int key) {
    while (node != NIL && key != node->key) {
        // 辿るものがなくなる or 見つかったとき終了
        if (key < node->key) {
            node = node->left;
        } else {
            node = node->right;
        }
    }

    return node;
}

void nodeDelete(Node *z) {
    Node *y; // 削除する対象
    Node *x; // yの子

    // 手順1
    if (z->left == NIL || z->right == NIL) {
        // case1, case2
        y = z;
    } else {
        // case3
        y = treeSuccessor(z);
    }

    // 手順2
    if (y->left != NIL) {
        // case2で右に子がいないとき
        x = y->left;
    } else {
        // case1, case2, case3
        x = y->right;
    }

    // 手順3
    // yは消えるので、xの新しい親を設定する
    if (x != NIL) {
        x->parent = y->parent;
    }
    // yは消えるので、yの親の子をxに設定する
    if (y->parent == NIL) {
        // yが根の時xを木の根とする
        root = x;
    } else {
        if (y == y->parent->left) {
            // yが左の子だったとき
            y->parent->left = x;
        } else {
            // yが右の子だったとき
            y->parent->right = x;
        }
    }

    // 手順4
    if (y != z) {
        // case3
        z->key = y->key;
    }

    free(y);
}

void inorder(Node *node) {
    if (node == NIL) return;
    inorder(node->left);
    cout << " " << node->key;
    inorder(node->right);
}

void preorder(Node *node) {
    if (node == NIL) return;
    cout << " " << node->key;
    preorder(node->left);
    preorder(node->right);
}

int main() {
    int n;
    cin >> n;
    
    string command;
    for (int i = 0; i < n; i++) {
        cin >> command;
        if (command == "insert") {
            int key;
            cin >> key;
            insert(key);
        } else if (command == "find") {
            int key;
            cin >> key;
            Node *re = find(root, key);
            if (re != NIL) {
                cout << "yes" << endl;
            } else {
                cout << "no" << endl;
            }
        } else if (command == "delete") {
            int key;
            cin >> key;
            nodeDelete(find(root, key));
        } else if (command == "print") {
            inorder(root);
            cout << endl;
            preorder(root);
            cout << endl;
        }
    }

    return 0;
}
