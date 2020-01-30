#include <iostream>
using namespace std;

int main()
{
    int t, i, n, s1, s2, f = -1, s = -1, temp, be = 0, m, e;
    cin >> t;
    cin >> n >> s1;
    int a[n];
    for (i = 0; i < n; i++)
    {
        cin >> temp;
        a[i] = temp;
    }
    e = n - 1;
    while (be <= e)
    {
        m = (be + e) / 2;
        if (a[m] == s1)
        {
            f = 1;
            break;
        }
        else if (a[m] < s1)
            be = m + 1;
        else
            e = m - 1;
    }
    cin >> n >> s1;
    int b[n];
    for (i = 0; i < n; i++)
    {
        cin >> temp;
        b[i] = temp;
    }
    be = 0;
    e = n - 1;
    while (be <= e)
    {
        m = (be + e) / 2;
        if (b[m] == s1)
        {
            f = 1;
            break;
        }
        else if (b[m] < s1)
            be = m + 1;
        else
            e = m - 1;
    }
    cout << f << "\n";
    cout << s << "\n";
    return 0;
}