#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAX 2000000
#define INFTY (1<<30)

int H, A[MAX + 1];

void maxHeapify(int i) {
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
        maxHeapify(largest);
    }
}

void increaseKey(int i, int key) {
    if (key < A[i]) return;
    A[i] = key;
    while (i > 1 && A[i / 2] < A[i]) {
        // i / 2 = parent
        swap(A[i], A[i / 2]);
        i = i / 2;
    }
}

void insert(int key) {
    H++;
    A[H] = -INFTY;
    increaseKey(H, key);
}

int extract() {
    int maxv;
    if (H < 1) return -INFTY;
    maxv = A[1];
    A[1] = A[H--];
    maxHeapify(1);
    
    return maxv;
}

int main() {
    int key;
    char command[10];

    int A[MAX + 1];
    int H;


    while(1) {
        scanf("%s", command);
        if (command[0] == 'e' && command[1] == 'n') {
            break;
        } else if (command[0] == 'i') {
            scanf("%d", &key);
            insert(key);
        } else {
            printf("%d\n", extract());
        }
    }

    return 0;
}
