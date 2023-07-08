#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
    stack<int> stk1;
    stack<int> stk2;
    vector<int> vec;
    char ch;
    int ip;
    int totalArea = 0;
    for (int i = 0; cin >> ch; i++) {
        cout << 'a' << endl;
        if (ch == '\\') {
            // \ のとき
            stk1.push(i);
        } else if (ch == '/') {
            // / のとき
            if (!stk1.empty()) {
                ip = stk1.top(); stk1.pop();
                int s = i - ip - 1;
                // 総面積加算
                totalArea += s;
                // 個別面積計算用にpush
                stk2.push(s);
                // popした後にスタックが空なら水たまりが途切れている
                if (stk1.empty()) {
                    int s = 0;
                    while (!stk2.empty()) {
                        s += stk2.top(); stk2.pop();
                    }
                    vec.push_back(s);
                }
            }
        } // _ のときはなにもしない
        // 入力末尾処理 (stk1に余っていても水たまりが途切れたことになる)
        if (!stk1.empty()) {
            int s = 0;
            while (!stk2.empty()) {
                s += stk2.top(); stk2.pop();
            }
            vec.push_back(s);
        }
    }

    // 出力
    cout << totalArea << endl;
    int puddleNum = vec.size();
    cout << puddleNum;
    for (int i = 0; i < puddleNum; i++) {
        if (i < puddleNum - 1) {
            cout << " ";
        }
        cout << vec[i];
    }
    cout << endl;

    return 0;
}