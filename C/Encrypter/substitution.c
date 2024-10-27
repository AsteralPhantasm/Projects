#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Program that encrypts messages using a substitution cypher. 

int repeat_check(string argv);
int char_check(string argv);

int main(int arglen, char *argv[])
{
    int x;
    char *str = NULL;
    char alphabet[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    if (arglen != 2 || arglen == 0)
    {
        printf("Error: Invalid input.\n");
        return 1;
    }
    else
    {
        str = argv[1];
    }
    if (strlen(str) != 26 || repeat_check(str) == 1 || char_check(str) == 1)
    {
        printf("Error: Invalid key.\n");
        return 1;
    }
    else
    {
        int k = 0;
        int j = 0;
        char key[26];
        strcpy(key, str);
        string plaintext = get_string("Plaintext: ");
        char plaintext2[50];
        strcpy(plaintext2, plaintext);
        while (k < strlen(plaintext2))
        {
            if (toupper(plaintext2[k]) == alphabet[j])
            {
                if (isupper(plaintext2[k]) > 0)
                {
                    plaintext2[k] = toupper(key[j]);
                    k++;
                    j = 0;
                }
                else if (islower(plaintext2[k]) > 0)
                {
                    plaintext2[k] = tolower(key[j]);
                    k++;
                    j = 0;
                }
                else
                {
                    continue;
                }
            }
            else if (isspace(plaintext2[k]) != 0 || isalpha(plaintext2[k]) == 0)
            {
                k++;
            }
            else
            {
                j++;
            }
        }
        printf("ciphertext: %s\n", plaintext2);
        return 0;
    }
}
int repeat_check(string argv)
{
    for (int i = 0; i < strlen(argv); i++)
    {
        for (int m = i + 1; m < strlen(argv); m++)
        {
            if (argv[i] == argv[m])
            {
                return 1;
            }
            else
            {
                continue;
            }
        }
    }
    return 0;
}
int char_check(string argv)
{
    for (int p = 0; p < strlen(argv); p++)
    {
        if (isalpha(argv[p]) == 0)
        {
            return 1;
        }
        else
        {
            continue;
        }
    }
    return 0;
}
