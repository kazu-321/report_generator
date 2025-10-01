# 実験の目的
C 言語を用いて文字列処理について学ぶ。


# prog2-01.c
## code
```c

#include <stdio.h>

int main(void) {
    char str[] = "abc";
    printf("%s\n", str);
    return 0;
}
```
## result
## 実行結果
### 出力:
```
abc
``` 

# prog2-02.c
## code
```c

#include <stdio.h>

int main(void) {
    char name[] = "橋本 千聡";
    printf("名前: %s\n", name);
    return 0;
}
```
## result
## 実行結果
### 出力:
```
名前: 橋本 千聡
``` 

# prog2-03.c
## code
```c

#include <stdio.h>

int main(void) {
    char str[1024];
    scanf("%s", str);
    printf("%s\n", str);
    return 0;
}
```
## result
## 実行 0
### 入力:
```
abcdefghijklmnopqrstuvwxyz
```
### 出力:
```
abcdefghijklmnopqrstuvwxyz
``` 

# prog2-04.c
## code
```c

#include <stdio.h>

int main(void) {
    char input;
    scanf("%c", &input);
    if(input == 'A') {
        printf("正解です\n");
    } else {
        printf("誤りです\n");
    }
    return 0;
}
```
## result
## 実行 0
### 入力:
```
A
```
### 出力:
```
正解です
```
## 実行 1
### 入力:
```
Z
```
### 出力:
```
誤りです
``` 

# prog2-05.c
## code
```c

#include <stdio.h>

int main(void) {
    char input;
    scanf("%c", &input);
    if('A' <= input && input <= 'C') {
        printf("正解です\n");
    } else {
        printf("誤りです\n");
    }
    return 0;
}
```
## result
## 実行 0
### 入力:
```
B
```
### 出力:
```
正解です
```
## 実行 1
### 入力:
```
C
```
### 出力:
```
正解です
```
## 実行 2
### 入力:
```
D
```
### 出力:
```
誤りです
``` 

# prog2-06.c
## code
```c

#include <stdio.h>

int main(void) {
    char name[]="HashimotoKazusa";
    for(int i=14; i>=0; i--){
        printf("%c", name[i]);
    }
    printf("\n");
    return 0;
}
```
## result
## 実行結果
### 出力:
```
asuzaKotomihsaH
``` 

# prog2-07.c
## code
```c

#include <stdio.h>

int main(void) {
    char name[]="HashimotoKazusa";
    int i=14;
    while(i>=0){
        printf("%c", name[i]);
        i--;
    }
    printf("\n");
    return 0;
}
```
## result
## 実行結果
### 出力:
```
asuzaKotomihsaH
``` 

# prog2-08.c
## code
```c

#include <stdio.h>

int main(void) {
    char name[]="Hashimoto Kazusa";
    printf("%s\n", name);
    return 0;
}
```
## result
## 実行結果
### 出力:
```
Hashimoto Kazusa
``` 

# prog2-09.c
## code
```c

#include <stdio.h>

int main(void) {
    char ibaraki[] = "ibaraki";
    for(int i=0; i<7; i++){
        printf("%c/", ibaraki[i]);
    }
    printf("\n");
    return 0;
}
```
## result
## 実行結果
### 出力:
```
i/b/a/r/a/k/i/
``` 

# prog2-10.c
## code
```c

#include <stdio.h>

int main(void) {
    char ibaraki[] = "ibaraki";
    int i = 0;
    while(i<7){
        printf("%c/", ibaraki[i]);
        i++;
    }
    printf("\n");
    return 0;
}
```
## result
## 実行結果
### 出力:
```
i/b/a/r/a/k/i/
``` 

# prog2-11.c
## code
```c

#include <stdio.h>

int main(void) {
    char arr[] = "oiibkayrrawkqiykpoasjebn";
    int i;
    int len = 0;
    while (arr[len] != '\0') {
        len++;
    }

    for (i = 1; i < len; i += 2) {
        putchar(arr[i]);
    }
    putchar('\n');

    return 0;
}
```
## result
## 実行結果
### 出力:
```
ibarakikosen
``` 

# prog2-12.c
## code
```c

#include <stdio.h>

int main(void) {
    printf("char型のバイト数: %zuバイト\n", sizeof(char));
    printf("char型のビット数: %zuビット\n", sizeof(char) * 8);
    return 0;
}
```
## result
## 実行結果
### 出力:
```
char型のバイト数: 1バイト
char型のビット数: 8ビット
``` 

# prog2-13.c
## code
```c

#include <stdio.h>

int main(void) {
    char data[3][1024] = {"Hello", "Goodbye", "Thankyou"};
    for(int i = 0; i < 3; i++) {
        printf("%s\n", data[i]);
    }
    return 0;
}
```
## result
## 実行結果
### 出力:
```
Hello
Goodbye
Thankyou
``` 

# prog2-14.c
## code
```c

#include <stdio.h>

int main(void) {
    char str[3][1024];
    for(int i = 0; i < 3; i++) {
        scanf("%s", str[i]);
    }
    for(int i = 0; i < 3; i++) {
        printf("%s\n", str[i]);
    }
    return 0;
}
```
## result
## 実行 0
### 入力:
```
ABCDE
fghijkl
nmopqrstuvwxyz
```
### 出力:
```
ABCDE
fghijkl
nmopqrstuvwxyz
``` 

# prog2-15.c
## code
```c

#include <stdio.h>

int main(void) {
    char day[7][10] = {
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    };
    int i;
    printf("0-月曜日 1-火曜日 2-水曜日 3-木曜日 4-金曜日 5-土曜日 6-日曜日\n");
    scanf("%d", &i);
    printf("%s\n", day[i]);
    return 0;
}
```
## result
## 実行 0
### 入力:
```
2
```
### 出力:
```
0-月曜日 1-火曜日 2-水曜日 3-木曜日 4-金曜日 5-土曜日 6-日曜日
Tuesday
``` 

# prog2-16.c
## code
```c

#include <stdio.h>
#include <string.h>


int main(void) {
    char str[1024];

    scanf("%s", str);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == 'a') {
            printf("%d番目\n", i + 1);
        }
    }

    return 0;
}
```
## result
## 実行 0
### 入力:
```
bcdfhiertkdjfga;sfisas;dlfkj;alwkej;alkjds;fsjdf
```
### 出力:
```
15番目
21番目
30番目
37番目
``` 

# prog2-17.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str[1024];
    int count = 0;

    scanf("%s", str);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == 'b') {
            count++;
        }
    }

    if (count > 0) {
        printf("文字 'b' は %d 個含まれています。\n", count);
    } else {
        printf("文字 'b' は含まれていません。\n");
    }

    return 0;
}
```
## result
## 実行 0
### 入力:
```
abcdefghijklnmbbbbabababab
```
### 出力:
```
文字 'b' は 9 個含まれています。
``` 

# prog2-18.c
## code
```c

#include <stdio.h>

int main(void) {
    char data[1024];
    char c;
    int count = 0;

    scanf("%s", data);
    getchar();
    scanf("%c", &c);

    // 文字列内のcの個数を数える
    for (int i = 0; data[i] != '\0'; i++) {
        if (data[i] == c) {
            count++;
        }
    }

    if (count > 0) {
        printf("'%c' は %d 回含まれています。\n", c, count);
    }
    else {
        printf("'%c' は含まれていません。\n", c);
    }

    return 0;
}
```
## result
## 実行 0
### 入力:
```
abcdeabcdabcaba
b
```
### 出力:
```
'b' は 4 回含まれています。
``` 

# prog2-19.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str[1024];
    int count[10] = {0};
    int i;

    scanf("%s", str);

    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            count[str[i] - '0']++;
        }
    }

    for (i = 0; i < 10; i++) {
        printf("%d: %d\n", i, count[i]);
    }

    return 0;
}
```
## result
## 実行 0
### 入力:
```
a0b1c2d3e45678901234907394587102339587104
```
### 出力:
```
0: 5
1: 4
2: 3
3: 5
4: 4
5: 3
6: 1
7: 4
8: 3
9: 4
``` 

# prog2-20.c
## code
```c

#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char str[1024];
    int i = 0;
    scanf("%s", str);

    while (str[i] != '\0' && str[i] != '\n')
    {
        if (!isdigit((unsigned char)str[i]))
        {
            printf("%c", str[i]);
        }
        i++;
    }
    printf("\n");

    return 0;
}

```
## result
## 実行 0
### 入力:
```
a1b2c3d4e5f6g7h8i9j0k
```
### 出力:
```
abcdefghijk
``` 

# prog3-1.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str[1024];
    scanf("%s", str);
    printf("文字列の長さは %zu です。\n", strlen(str));
    return 0;
}
```
## result
## 実行 0
### 入力:
```
abcde
```
### 出力:
```
文字列の長さは 5 です。
``` 

# prog3-2.c
## code
```c

#include <stdio.h>

int my_strlen(const char str[]) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

int main(void) {
    char str[1024];
    scanf("%s", str);
    printf("文字列の長さは %d です。\n", my_strlen(str));
    return 0;
}
```
## result
## 実行 0
### 入力:
```
abcde
```
### 出力:
```
文字列の長さは 5 です。
``` 

# prog3-3.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str1[1024] = "ibaraki";
    char str2[1024] = "kosen";

    strcpy(str1, str2);
    printf("%s\n", str1);

    return 0;
}
```
## result
## 実行結果
### 出力:
```
kosen
``` 

# prog3-4.c
## code
```c

#include <stdio.h>

void my_strcpy(char *dest, const char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0'; // Null-terminate the destination string
}

int main(void) {
    char str1[1024] = "ibaraki";
    char str2[1024] = "kosen";

    my_strcpy(str1, str2);
    printf("%s\n", str1);

    return 0;
}
```
## result
## 実行結果
### 出力:
```
kosen
``` 

# prog3-5.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str1[1024] = "ibaraki";
    char str2[1024] = "kosen";

    strcat(str1, str2);
    printf("%s\n", str1);

    return 0;
}
```
## result
## 実行結果
### 出力:
```
ibarakikosen
``` 

# prog3-6.c
## code
```c

#include <stdio.h>

void my_strcat(char *dest, const char *src) {
    while (*dest) {
        dest++;
    }
    while (*src) {
        *dest++ = *src++;
    }
    *dest = '\0';
}

int main(void) {
    char str1[1024] = "ibaraki";
    char str2[1024] = "kosen";

    my_strcat(str1, str2);
    printf("%s\n", str1);

    return 0;
}
```
## result
## 実行結果
### 出力:
```
ibarakikosen
``` 

# prog3-7.c
## code
```c

#include <stdio.h>
#include <string.h>

int main(void) {
    char str1[] = "ibaraki";
    char str2[] = "kosen";
    int result;

    result = strcmp(str1, str2);

    printf("str1: %s\n", str1);
    printf("str2: %s\n", str2);

    if (result < 0) {
        printf("str1 は str2 より小さいです。\n");
    } else if (result > 0) {
        printf("str1 は str2 より大きいです。\n");
    } else {
        printf("str1 と str2 は等しいです。\n");
    }

    return 0;
}
```
## result
## 実行結果
### 出力:
```
str1: ibaraki
str2: kosen
str1 は str2 より小さいです。
``` 

# prog4.c

## 説明
ibarakikousenkokusai kogakuka の 19 文字目に sozo を挿入するプログラム
strinsでは、19まではstr1をそのままコピーし、20からはstr2をコピーし、
その後にstr1の20文字目以降をコピーする。

## code
```c
#include <stdio.h>
#include <string.h>
char *strins(char *str1, char *str2, int start) {
    int c1, len1, len2;
    len1 = strlen(str1);
    len2 = strlen(str2);
    if (len1 < len2 || start >= len1)
        return (str1);
    for (c1 = len1; c1 >= start; c1--)
        str1[c1 + len2] = str1[c1];
    for (c1 = 0; c1 < len2; c1++)
        str1[start + c1] = str2[c1];
    return (str1);
}

int main(void) {
    char str1[128], str2[128];
    strcpy(str1, "ibarakikosenkokusaikogakuka");
    strcpy(str2, "sozo");
    printf("str1=%s\n", str1);
    printf("str2=%s\n", str2);
    printf("%s\n", strins(str1, str2, 19));
    return (0);
}
```
## result
## 実行結果
### 出力:
```
str1=ibarakikosenkokusaikogakuka
str2=sozo
ibarakikosenkokusaisozokogakuka
``` 

# prog5.c
## code
```c

#include <stdio.h>
#include <string.h>


int main() {
    char str[1024];
    int slide, i;
    scanf("%s", str);
    scanf("%d", &slide);

    int len = strlen(str);
    for (i = 0; i < len; i++) {
        if ('a' <= str[i] && str[i] <= 'z') {
            char shifted = ((str[i] - 'a' + slide) % 26) + 'a';
            printf("%c", shifted);
        } else {
            printf("%c", str[i]);
        }
    }
    printf("\n");
    return 0;
}
```
## result
## 実行 0
### 入力:
```
pazw
5
```
### 出力:
```
ufeb
``` 

# prog6.c
## code
```c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


int main() {
    char str[1024];
    int i, len;

    scanf("%s",str);
    
    len = strlen(str);

    srand((unsigned int)time(NULL));

    if (len > 0) {
        int rand_index = rand() % len;
        printf("入力された文字列: %s\n", str);
        printf("ランダムに選ばれた文字: %c (位置: %d)\n", str[rand_index], rand_index);
    } else {
        printf("文字列が入力されていません。\n");
    }

    return 0;
}

```

## 説明
このプログラムは、ユーザーから文字列を入力として受け取り、その中からランダムに1文字を選んで表示します。
- まず、標準入力から文字列を受け取ります。
- 乱数を初期化し、文字列の長さの範囲でランダムな位置を決めます。
- その位置の文字を表示します。
- 文字列が空の場合は、その旨を表示します。

## result
## 実行 0
### 入力:
```
abcdefghijklmnopqrstuvwxyz
```
### 出力:
```
入力された文字列: abcdefghijklmnopqrstuvwxyz
ランダムに選ばれた文字: v (位置: 21)
``` 


# 考察
基本的な文字列操作を復習することができた。

普段文字列操作はC++かアセンブラから行っているのでC言語でやると新鮮に感じた。

文字列操作や正規表現をマスターしてコマンドラインから何でもできるようになりたいと感じた。