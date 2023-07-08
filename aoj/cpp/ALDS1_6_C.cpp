#include <iostream>
using namespace std;

#define MAX 100000
#define SENTINEL 2000000000

struct Card {
    char suit;
    int value;
};

struct Card L[MAX/2 + 2];
struct Card R[MAX/2 + 2];

void merge(struct Card A[], int left, int mid, int right) {
    // 左右の配列の要素数を計算
    int n1 = mid - left;
    int n2 = right - mid;

    // 左右の配列に要素をコピー
    for (int i = 0; i < n1; i++) L[i] = A[left + i];
    for (int i = 0; i < n2; i++) R[i] = A[mid + i];

    // 番兵
    L[n1].value = R[n2].value = SENTINEL;

    int i = 0;
    int j = 0;
    for (int k = left; k < right; k++) {
        // マージ
        if (L[i].value <= R[j].value) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
    }
}

void mergeSort(struct Card A[], int left, int right) {
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

int partition(struct Card A[], int p, int r) {
    struct Card x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++) {
        if (A[j].value <= x.value) {
            i++;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[r]);

    return i + 1;
}

void quickSort(struct Card A[], int p, int r) {
    int q;
    if (p < r) {
        q = partition(A, p, r);
        quickSort(A, p, q - 1);
        quickSort(A, q + 1, r);
    }
}

int main() {
    int n;
    cin >> n;

    char s;
    int v;
    struct Card A[MAX], B[MAX];
    for (int i = 0; i < n; i++) {
        cin >> s >> v;
        A[i].suit = B[i].suit = s;
        A[i].value = B[i].value = v;
    }

    mergeSort(A, 0, n);
    quickSort(B, 0, n - 1);

    // 安定性の検証
    int isStable = 1;
    for (int i = 0; i < n; i++) {
        if (A[i].suit != B[i].suit) {
            isStable = 0;
            break;
        }
    }

    if (isStable) cout << "Stable" << endl;
    else cout << "Not stable" << endl;
    for (int i = 0; i < n; i++) {
        cout << B[i].suit << " " << B[i].value <<endl;
    }

    return 0;
}
