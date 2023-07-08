#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

#define MAX 2000000
#define INFTY (1<<30)

void maxHeapify(int A[], int H, int i) {
    int left;
    int right;
    int largest;

    left = 2 * i;
    right = 2 * i + 1;

    // 自分と子の中で最大のノードを選ぶ
    if (left <= H && A[left] > A[i]) {
        largest = left;
    } else {
        largest = i;
    }
    if (right <= H && A[right] > A[largest]) {
        largest = right;
    }

    // 入れ替え
    if (largest != i) {
        swap(A[i], A[largest]);
        maxHeapify(A, H, largest);
    }
}

void increaseKey(int A[], int i, int key) {
    if (key < A[i]) return;
    A[i] = key;
    while (i > 1 && A[i / 2] < A[i]) {
        // i / 2 = parent
        swap(A[i], A[i / 2]);
        i = i / 2;
    }
}

void insert(int A[], int H, int key) {
    H++;
    A[H] = -INFTY;
    increaseKey(A, H, key);
}

int extract(int A[], int H) {
    int maxv;
    if (H < 1) return -INFTY;
    maxv = A[1];
    A[1] = A[H];
    H--;
    maxHeapify(A, H, 1);
    
    return maxv;
}

int main() {
    cout << "a" << endl;
    int key;
    string command;

    int A[MAX + 1];
    int H;


    while(1) {
        cin >> command;
        if (command == "end") {
            break;
        } else if (command == "insert") {
            cin >> key;
            insert(A, H, key);
        } else {
            cout << extract(A, H) << endl;
        }
    }

    return 0;
}
