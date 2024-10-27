#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <stdint.h>

#define BUFFER_SIZE 512

// Code used to recover files from a memory card

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Error: Invalid input.\n");
        return 1;
    }
    char *str = NULL;
    str = argv[1];
    FILE *card_file = fopen(str, "r");
    if (!card_file)
    {
        printf("Error: File doesn't exist.\n");
        return 1;
    }
    uint8_t buffer[BUFFER_SIZE];
    int counter = 0;
    int jpeg_check = 0;
    FILE *image_check = NULL;
    while (fread(buffer, 1, 512, card_file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpeg_check == 1)
            {
                fclose(image_check);
            }
            else
            {
                jpeg_check = 1;
            }
            char filename[8];
            sprintf(filename, "%03i.jpg", counter);
            image_check = fopen(filename, "w");
            counter++;
        }
        if (jpeg_check == 1)
        {
            fwrite(buffer, 1, 512, image_check);
        }
    }
    fclose(image_check);
    fclose(card_file);
    return 0;
}
