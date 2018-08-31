/*
Copyright 2018 liuzhen .
*/

#include "Sort.h"

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


void BubbleSort(int *front, int num)
{
    for (int j = 0; j < num; j++) {
        for (int i = 0; i < num-j; i++) {
            if (front[i] > front[i+1]) {
                int temp = front[i];
                front[i] = front[i+1];
                front[i+1] = temp;
            }
        }
    }
}


void SelectSort(int *front, int num)
{
    for(int i = 0; i < num; i++) {
        for(int j = i; j < num; j++) {
            if (*(front+i) > *(front+j)) {
                int temp = *(front+i);
                *(front+i) = *(front+j);
                *(front+j) = temp;
            }
        }
    }
}


void SelectSort_opt(int *front, int num)
{
    for (int i = 0;i < num - 1;++i)
    {
        int k = i;
        for (int j = i + 1;j < num;++j)
        {
            if (front[k] > front[j])
            {
                k = j;
            }
        }
        if (i != k)
        {
            int temp = front[i];
            front[i] = front[k];
            front[k] = temp;
        }
    }
}

void InsertSort(int *front, int num)
{
    for(int i = 0; i < num; i++) {
        for (int j = 0; j < i; j++) {
            if (front[j] > front[i]) {
                int temp = front[i];
                for (int k = i; k > j; k--) {
                    front[k] = front[k-1];
                }
                front[j] = temp;
            }
            continue;
        }
    }
}


void BinaryInsertSort(int *front, int num)
{
    for(int i = 1; i < num; i++) {
        int start = 0;
        int end = i - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (front[mid] > front[i]) {
                end = mid-1;
            }
            else {
                start = mid+1;
            }
        }
        int temp = front[i];
        for (int k = i; k > start; k--) {
            front[k] = front[k-1];
        }
        front[start] = temp;
    }
}


void MergeSort(int *front, int *end)
{
    // 已经分到最后单个数据是一组
    if (front >= end) {
        return;
    }
    // 已经分到最后相邻 是一组,排一下序
    if (front == end - 1) {
        if (*front > *end) {
            int temp = *front;
            *front = *end;
            *end = temp;
        }
    }


    int num = 0;
    while((front + num) != end) {
        num++;
    }

    // 将beg到end分为2段A和B，并将A和B分别使用归并排序
    MergeSort(front, front+(num/2));
    MergeSort(front+(num/2)+1, end);

    // 将A 和 B 排序完毕后，合并A和B——使用插入排序
    for (int i = 0; i <= num; i++) {
        for (int j = 0; j < i; j++) {
            if(front[j] > front[i]) {
                int temp = front[i];
                for (int k = i; k > j; k--) {
                    front[k] = front[k-1];
                }
                front[j] = temp;
                continue;
            }
        }
    }

}




