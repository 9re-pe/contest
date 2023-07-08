#include <iostream>
using namespace std;

#define MAX 2000000

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

int main() {
    int H;
    int A[MAX + 1];

    cin >> H;

    for (int i = 1; i <= H; i++) cin >> A[i];

    for (int i = H / 2; i >= 1; i--) maxHeapify(A, H, i);

    for (int i = 1; i <= H; i++) {
        cout << " " << A[i];
    }

    cout << endl;

    return 0;
}

