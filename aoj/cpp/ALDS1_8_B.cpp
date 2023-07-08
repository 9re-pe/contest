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
        } else if (command == "print") {
            inorder(root);
            cout << endl;
            preorder(root);
            cout << endl;
        }
    }

    return 0;
}
