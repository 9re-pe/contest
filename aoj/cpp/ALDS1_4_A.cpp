#include <stdio.h>
#include <iostream>
using namespace std;


int search(int A[], int n, int key) {
    int i = 0;
    A[n] = key; // 番兵をセット
    while (A[i] != key) i++;
    return i != n;
}

int main() {
    int n;
    cin >> n;

    int A[10000 + 1];
    for (int i = 0; i < n; i++) cin >> A[i];

    int q;
    cin >> q;

    int key;
    int sum = 0;
    for (int i = 0; i < q; i++) {
        cin >> key;
        if (search(A, n, key)) sum++; 
    }

    cout << sum << endl;

    return 0;
}
