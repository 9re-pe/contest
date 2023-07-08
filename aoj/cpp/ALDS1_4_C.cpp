#include<stdio.h>
#include<string.h>
#include <iostream>
using namespace std;

const int M = 1046527;
const int NIL = -1;
const int L = 14;

// 最大L-2文字の文字列をM個格納できるハッシュテーブル
char H[M][L];

// 文字から数値に変換
int charToInt (char ch) {
    if (ch == 'A') return 1;
    else if (ch == 'B') return 2;
    else if (ch == 'C') return 3;
    else if (ch == 'D') return 4;
    else return 0;
}

// keyを生成
// 文字列から数値に変換
long long getKey (char str[]) {
    long long sum = 0;
    long long p = 1;

    for (long long i = 0; i < strlen(str); i++) {
        sum += p * (charToInt(str[i]));
        p *= 5;
    }

    return sum;
}

int h1 (int key) {
    return key % M;
}

int h2 (int key) {
    return 1 + (key % (M - 1));
}

int insert (char str[]) {
    long long key = getKey(str);

    long long h;
    for (long long i = 0; ; i++) {
        // 衝突しないハッシュ値が得られるまで繰り返す
        h = (h1(key) + i * h2(key)) % M;
        if (strcmp(H[h], str) == 0) {
            // すでにその文字列が辞書に登録されていた時
            return 1;
        } else if (strlen(H[h]) == 0) {
            // 衝突していないとき
            strcpy(H[h], str);
            return 0;
        }
    }

    return 0;
}

int find (char str[]) {
    long long key = getKey(str);
    long long h;
    for (int i = 0; ; i++) {
        h = (h1(key) + i * h2(key)) % M;
        if (strcmp(H[h], str) == 0) return 1;
        else if (strlen(H[h]) == 0) return 0;
        // 違う文字列が入っていたらハッシュ値を再計算
    }
    return 0;
}

int main() {
    for (int i = 0; i < M; i++) H[i][0] = '\0';

    int n;
    cin >> n;
    char str[L], com[9];
    for (int i = 0; i < n; i++) {
        scanf("%s %s", com, str);

        if (com[0] == 'i') {
            insert(str);
        } else {
            if (find(str)) {
                cout << "yes" << endl;
            }else {
                cout << "no" << endl;                
            }
        }
    }

    return 0;
}
