/*
Copyright 2018 liuzhen .
*/

#include <iostream>
#include "Sort.h"
#include "StrRelate.h"

typedef unsigned int  uint;

using namespace std;


void SwapA( int &A, int &B );
void SwapB( unsigned int &A, unsigned int &B );

int main()
{
//    cout << "start!" << endl;
//    int list[10] = {2,3,5,9,1,6,7,4,8,10};
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;

//    int* front = list;
//    int* end = list + 9;
//    int len = sizeof(list)/sizeof(list[0]);

//    cout << "1. quick sort!" << endl;
//    quicksort(front, end);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;


//    cout << "2. Bubble sort!" << endl;
//    BubbleSort(front, len);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;

//    cout << "3. Select sort!" << endl;
//    SelectSort(front, len);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;


//    cout << "3. optimization Select sort!" << endl;
//    SelectSort_opt(front, len);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;


//    cout << "4. Insert sort!" << endl;
//    InsertSort(front, len);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;


//    cout << "4. Binary Insert sort!" << endl;
//    BinaryInsertSort(front, len);
//    for (int i = 0; i < 10; i++) {
//        cout << list[i] << " ";
//    }
//    cout << endl;

//    cout << "Strcpy !" << endl;
//    char str1[11] = "1111111111";
//    char str2[11] = "0123456789";
//    char* str = Strcpy(str1, str2);
//    cout << str << endl;

//    cout << "Strcat !" << endl;
//    char str1[11] = "1111111111";
//    char str2[11] = "0123456789";
//    char* str = Strcat(str1, str2);
//    cout << str << endl;


//    cout << "Swap without three arg!" << endl;
//    int a = -1;
//    int b = -2;
//    SwapA(a, b);
//    cout << a << b <<endl;
//    uint c = 1;
//    uint d = 2;
//    SwapB(c, d);
//    cout << c << d <<endl;

//    cout << "atoi!" << endl;
//    char* a = "1990";
//    int num = atoi(a);
//    cout << num << endl;

//    char s[]="abc";    //栈
//    char *p3="123456";    //123456\0在常量区，p3在栈上。
//    char *s="string"的内容是不可以改的
//    cout << "Inverted!" << endl;
//    char s[7] = "123456";
//    char* s1 = Inverted(s);
//    cout << s1 << endl;

//    cout << "Upper!" << endl;
//    char s[] = "abcDefg";
//    char* s1 = Upper(s);
//    cout << s1 << endl;

//    cout << "Strncpy !" << endl;
//    char str1[11] = "1111111111";
//    char str2[11] = "0123456789";
//    char* str = Strncpy(str1, str2, 5);
//    cout << str << endl;

    cout << "string reverse order!" << endl;
    char str[] = "abcdefg";
    char* str1 = reverse(str);
    cout << str1 << endl;

    return 0;
}

//4.不使用第三个变量交换两个数的值
void SwapA( int &A, int &B )
{
    if( A == B )
    {
        return;
    }
    A = A + B;
    B = A - B;
    A = A - B;
}


void SwapB( unsigned int &A, unsigned int &B )
{
    if( A == B )
    {
        return;
    }
    A = A ^ B;
    B = A ^ B;
    A = A ^ B;
}

