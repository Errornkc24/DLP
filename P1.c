#include <stdio.h>
#include <string.h>

int main() {
    char input[50];

    while (1) {
        printf("Enter a string (or enter 0 to exit): ");
        scanf("%s", input);
        
        if (strcmp(input, "0") == 0) {
            break;
        }

        int len = strlen(input);
        if (len < 2 || input[len - 1] != 'b' || input[len - 2] != 'b' || input[len - 3] != 'a') {
            printf("The string is not valid.\n");
            continue;
        }

        int valid = 1;
        for (int i = 0; i < len - 2; i++) {
            if (input[i] != 'a') {
                valid = 0;
                break;
            }
        }

        if (valid) {
            printf("The string is valid.\n");
        } else {
            printf("The string is not valid.\n");
        }
    }

    return 0;
}