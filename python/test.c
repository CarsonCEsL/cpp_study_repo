#include <stdio.h>
#include <string.h>

int strStr(char* haystack, char* needle) {

    if (needle == NULL || haystack == NULL) {
        return -1;
    }

    if (strlen(needle) == 0) {
        return -1;
    }

    for (int i = 0; i <= strlen(haystack) - strlen(needle); i++) {
        char *p = haystack + i;
        char *q = needle;

        while (*q != '\0' && *p == *q) {
            p++;
            q++;
        }

        if (*q == '\0') {
            return i;
        }
    }

    return -1;
}

int main() {
    printf("%d.\n", strStr("lleet", "leeetertewrewr"));
}