#include <stdio.h>
#include <iostream>
using namespace std;

// 入力値のMから選んだ要素を引いていく再帰関数
int solve(int i, int m, int A[], int n) {
    if (m == 0) return true;
    if (i >= n) return false;
    int res = solve(i + 1, m, A, n) || solve(i + 1, m - A[i], A, n);
    
    return res;
}

int main() {
    int n;
    cin >> n;
    int A[2001];
    for (int i = 0; i < n; i++) cin >> A[i];
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int m;
        cin >> m;
        if (solve(0, m, A, n)) cout << "yes" << endl;
        else cout << "no" << endl;
    }

    return 0;
} 
