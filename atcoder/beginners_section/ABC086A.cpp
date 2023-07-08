#include <iostream>
using namespace std;

string getOddOrEven (int i) {
    string re;
    
    if (i % 2 == 0) {
        re = "Even";
    } else {
        re = "Odd";
    }

    return re;
}

int main()
{
    int a, b;
    cin >> a >> b;

    int tmp;
    tmp = (a * b) % 2;
    string ans;
    ans = getOddOrEven(tmp);

    cout << ans << endl;

    return 0;
}