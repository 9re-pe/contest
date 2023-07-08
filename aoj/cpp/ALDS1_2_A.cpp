#include<iostream>
using namespace std;

// flgを用いたバブルソート
int bubbleSort (int A[], int N) {
    int sw = 0;
    int flg = 1;
    for (int i = 0; flg; i++) {
        flg = 0;
        for (int j = N - 1; j >= i + 1; j--) {
            if (A[j - 1] > A[j]) {
                swap(A[j], A[j - 1]);
                flg = 1;
                sw++;
            }
        }
    }
    return sw;
}

int main() {
    int A[100], N, sw;
    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];

    sw = bubbleSort(A, N);

    for (int i = 0; i < N; i++) {
        cout << A[i];
        if (i < N - 1) cout << " ";
    }
    cout << endl;
    cout << sw << endl;

    return 0;
}
