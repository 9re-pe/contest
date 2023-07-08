#include <iostream>
using namespace std;

int binarySearch (int A[], int n, int key) {
    int left = 0;
    int right = n;
    int mid;
    while (left < right) {
        mid = (left + right) / 2;
        if (A[mid] == key) return 1;
        if (A[mid] < key) left = mid + 1;
        if (key < A[mid]) right = mid;
    }
    return 0;
}

int main() {
    int n;
    cin >> n;

    int A[100000];
    for (int i = 0; i < n; i++) cin >> A[i];

    int q;
    cin >> q;

    int key;
    int sum = 0;
    for (int i =0; i < q; i++) {
        cin >> key;
        if (binarySearch(A, n, key)) sum++; 
    }

    cout << sum << endl;

    return 0;
}