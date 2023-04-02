#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#define MAX_LEN 100
int main() {
    char filename[MAX_LEN];
    char directory[MAX_LEN] = "files/"; // directory name

    struct stat st = {0};
    if (stat(directory, &st) == -1) {
        mkdir(directory, 0700);
        printf("Directory created.\n");
    } else printf("Directory already exists.\n");


    while(1) {
        printf("Enter file name ('stop'): ");
        scanf("%s", filename);

        if(strcmp(filename, "stop") == 0) {
            printf("\nExiting...\n");
            break;
        }

        char filepath[MAX_LEN];
        strcpy(filepath, directory);
        strcat(filepath, filename);

        FILE* fp = fopen(filepath, "w");
        if(fp == NULL) {
            printf("Error creating file.\n");
            exit(1);
        }

        printf("File '%s' created in single level directory '%s'.\n", filename, directory);

        fclose(fp);
    }
    
    printf("Removing The directory and the files...\n");
    char command[MAX_LEN];
    sprintf(command, "rm -r %s", directory);
    system(command);

    return 0;
}
