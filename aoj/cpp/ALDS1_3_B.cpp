#include<iostream>
#include<algorithm>
using namespace std;

static const int p_max = 100005;

struct process {
    string name;
    int time;
};

class Queue {
    private:
        process prc[p_max];
        int head;
        int tail;

    public:
        Queue() {
            head = 0;
            tail = 0;
        }

        bool is_empty() {
            return head == tail;
        }

        void enqueue(process p) {
            prc[tail] = p;
            if (tail + 1 == p_max) {
                tail = 0;
            } else {
                tail++;
            }
        }

        process dequeue() {
            process p = prc[head];
            if (head + 1 == p_max) {
                head = 0;
            } else {
                head++;
            }
            return p;
        } 
};

int main() {
    int n;
    int q;
    int count = 0; // 開始からの経過時間を記録
    process p[100001]; // 入力受け取り用の配列

    cin >> n >> q;

    for (int i = 0; i < n; i++) {
        cin >> p[i].name >> p[i].time;
    }

    Queue que;
    for (int i = 0; i < n; i++) {
        que.enqueue(p[i]);
    }
    
    while(!que.is_empty()) {
        process tmp = que.dequeue();
        if (tmp.time > q) {
            que.enqueue({tmp.name, tmp.time - q});
            count += q;
        } else {
            count += tmp.time;
            cout << tmp.name << " " << count << endl;
        }
    }

    return 0;
}
