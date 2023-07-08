#include <iostream>
using namespace std;

#define MAX 500000
#define SENTINEL 2000000000

int L[MAX/2 + 2];
int R[MAX/2 + 2];
int cnt;

void merge(int A[], int left, int mid, int right) {
    // 左右の配列の要素数を計算
    int n1 = mid - left;
    int n2 = right - mid;

    // 左右の配列に要素をコピー
    for (int i = 0; i < n1; i++) L[i] = A[left + i];
    for (int i = 0; i < n2; i++) R[i] = A[mid + i];

    // 番兵
    L[n1] = R[n2] = SENTINEL;

    int i = 0;
    int j = 0;
    for (int k = left; k < right; k++) {
        // 比較回数のカウント
        cnt++;

        // マージ
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
    }
}

void mergeSort(int A[], int left, int right) {
    // Aのleftからrightまでをソート
    if (left+1 < right) {
        // divideとsolve
        int mid = (left + right) / 2;
        mergeSort(A, left, mid);
        mergeSort(A, mid, right);
        // merge
        merge(A, left, mid, right);
    }
}

int main() {
    int A[MAX], n, i;
    cnt = 0;

    cin >> n;
    for (i = 0; i < n; i++) cin >> A[i];

    mergeSort(A, n, 0);

    for (i = 0; i < n; i++) {
        if (i != 0) cout << " ";
        cout << A[i];
    }
    cout << endl;

    cout << cnt << endl;

    return 0;
}
