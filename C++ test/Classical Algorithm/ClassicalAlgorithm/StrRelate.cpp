/*
Copyright 2018 liuzhen .
*/

#include <stdio.h>
#include <iostream>
#include "StrRelate.h"
#include "string.h"
#include "assert.h"

using namespace std;

char* Strcpy(char *dest, char *src)
{
    if (dest == nullptr || src == nullptr) {
        return dest;
    }
    if (dest == src) {
        return dest;
    }

    char* temp = dest;
    while((*src) != '\0') {
        *temp = *src;
        temp++;
        src++;
    }
    *temp = '\0';
    return dest;
}


char *Strcat(char *dest, char *src)
{
    if (dest == nullptr || src == nullptr) {
        return dest;
    }
    int len = strlen(dest);
    char* temp = dest + len;
    while ((*temp = *src) != '\0') {
        temp++;
        src++;
    }
    return dest;
}


int atoi(char *src)
{
    assert(src != nullptr);
    int sum = 0;
    int time = 10;
    while(*src != '\0') {
        sum = sum*time +(*src - '0');
        src++;
    }
    return sum;
}


char *Inverted(char *src)
{
    if (src == nullptr) {
        return nullptr;
    }

    int lenth = strlen(src);
    for (int i = 0; i < lenth / 2; i++) {
        char temp = src[i];
        src[i] = src[lenth-1-i];
        src[lenth-1-i] = temp;
    }
    return src;
}


char *Upper(char *src)
{
    if (src == nullptr) {
        return nullptr;
    }
    char* temp = src;
    while(*temp != '\0') {
        if(*temp <= 'z' && *temp >= 'a') {
            *temp = *temp - 'a'+'A';
        }
        temp++;
    }
    return src;
}


char *Strncpy(char *dest, char *src, int count)
{
    assert(dest != nullptr && src != nullptr);
    if (dest == src || count <= 0) {
        return dest;
    }

    char* temp = dest;
    while(*src != '\0' && count > 0) {
        *temp = *src;
        temp++;
        src++;
        count--;
    }
    return dest;
}


char *reverse(char *input)
{
    if (input == nullptr) {
        return nullptr;
    }
    int len = strlen(input);
    char* output = new char[len+1];
    for (int i = 0; i < len; i++) {
        output[len-i-1] = input[i];
    }
    output[len] = '\0';
    return output;
}
