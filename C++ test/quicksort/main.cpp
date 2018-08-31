#include <iostream>
#include <list>

using namespace std;

void quicksort(int* front, int* end) {
    if (front >= end) {
        return;
    }
    int num = *front;
    int* fr = front;
    int* en = end;
    while (fr != en) {
        if (*fr >= *en) {
            int tmp = *fr;
            *fr = *en;
            *en = tmp;
        }
        if (num == *fr) {
            en--;
        }
        else {
            fr++;
        }
    }
    quicksort(front, fr-1);
    quicksort(fr+1, end);
}


int main()
{
    cout << "quick sort!" << endl;
    int list[10] = {2,3,5,9,1,6,7,4,8,10};
    for (int i = 0; i < 10; i++) {
        cout << list[i] << endl;
    }

    int* front = list;
    int* end = list + 9;
    quicksort(front, end);
    for (int i = 0; i < 10; i++) {
        cout << list[i] << endl;
    }

    return 0;
}

