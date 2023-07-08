#include<iostream>
#include <cstdlib>
using namespace std;

int top;
int S[1000];

void push(int x) {
    top++;
    S[top] = x;
}

int pop() {
    top--;
    return S[top + 1];
}

int main() {
    int a, b; // オペラントを扱うための変数
    top = 0; // initializeを直接行う
    char s[100]; // 入力受け取り用の配列

    while (cin >> s) {
        if (s[0] == '+') {
            b = pop();
            a = pop();
            push(a + b);
        } else if (s[0] == '-') {
            b = pop();
            a = pop();
            push(a - b);
        } else if (s[0] == '*') {
            b = pop();
            a = pop();
            push(a * b);
        } else {
            push(atoi(s));
        }
    }

    cout << pop() << endl;

    return 0;
}
