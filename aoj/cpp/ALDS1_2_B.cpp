#include<iostream>
using namespace std;

// 選択ソート
int selectionSort (int A[], int N) {
    int sw = 0;
    for (int i = 0; i < N - 1; i++) {
        int minj = i;
        for (int j = i; j < N; j++) {
            if (A[minj] > A[j]) minj = j;
        }
        swap(A[i], A[minj]);
        if (i != minj) sw++;
    }

    return sw;
}

int main () {
    int A[100];
    int N;

    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];

    int sw = selectionSort(A, N);

    for (int i = 0; i < N; i++) {
        cout << A[i];
        if (i < N - 1) cout << " ";
    }
    cout << endl;
    cout << sw << endl;

    return 0;
}
