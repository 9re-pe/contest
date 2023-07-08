#include<iostream>
using namespace std;

struct Card {
    char suit;
    char value;
};

void bubble (struct Card A[], int N) {
    for (int i = 0; i < N; i ++) {
        for (int j = N - 1; j >= i + 1; j--) {
            if(A[j - 1].value > A[j].value) {
                swap(A[j], A[j - 1]);
            }
        }
    }
}

void selection (struct Card A[], int N) {
    for (int i = 0; i < N; i++) {
        int minj = i;
        for (int j = i; j < N; j++) {
            if (A[minj].value > A[j].value) minj = j;
        }
        swap(A[i], A[minj]);
    }
}

void print(struct Card A[], int N) {
    for (int i = 0; i < N; i++) {
        cout << A[i].suit << A[i].value;
        if (i < N - 1) cout << " ";
    }
    cout << endl;
}

// バブルソートと選択ソートの結果を比較
bool isStable(struct Card C1[], struct Card C2[], int N) {
    for (int i = 0; i < N; i++) {
        if (C1[i].suit != C2[i].suit) return false;
    }
    return true;
}

int main() {
    Card C1[100], C2[100];
    int N;
    char ch;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> C1[i].suit >> C1[i].value;
    }

    for (int i = 0; i < N; i++) C2[i] = C1[i];

    bubble(C1, N);
    selection(C2, N);

    print(C1, N);
    cout << "Stable" << endl;
    print(C2, N);
    if (isStable(C1, C2, N)) {
        cout << "Stable" << endl;
    } else {
        cout << "Not stable" << endl;
    }

    return 0;
}  
