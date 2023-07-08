#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node *next;
    Node *prev;
};

Node *nill;

Node* listSearch(int key) {
    Node *cur = nill->next;
    while (cur != nill && cur->key != key)
    {
        cur = cur->next;
    }
    
    return cur;
}

void init() {
    nill = (Node *)malloc(sizeof(Node));
    nill->next = nill;
    nill->prev = nill;
}

void printList() {
    Node *cur = nill->next;
    int isfst = 0;
    while (1) {
        if (cur == nill) break;
        if (isfst++ > 0) printf(" ");
        printf("%d", cur->key);
        cur = cur->next;
    }
    printf("\n");
}

void deleteNode(Node *t) {
    if (t == nill) return;
    t->prev->next = t->next;
    t->next->prev = t->prev;
    free(t);
}

void deleteFirst() {
    deleteNode(nill->next);
}

void deleteLast() {
    deleteNode(nill->prev);
}

void deleteKey(int key) {
    deleteNode(listSearch(key));
}

void insert(int key) {
    Node *x = (Node *)malloc(sizeof(Node));
    x->key = key;

    x->next = nill->next;
    nill->next->prev = x;
    nill->next = x;
    x->prev = nill;
}

int main() {
    int n;
    scanf("%d", &n);
    init();

    char com[20];
    int key;
    for (int i = 0; i < n; i++) {
        scanf("%s%d", com, &key);
        if (com[0] == 'i') {
            // insert
            insert(key);
        } else if (com[0] == 'd') {
            if (strlen(com) > 6) {
                if (com[6] == 'F') {
                    // deleteFirst
                    deleteFirst();
                } else if (com[6] == 'L') {
                    // deleteLast
                    deleteLast();
                }
            } else {
                // delete
                deleteKey(key);
            }
        }
    }

    printList();

    return 0;
}
