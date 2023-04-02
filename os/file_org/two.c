#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#define MAX_LEN 100

int main() {
    char filename[MAX_LEN];
    char directory[MAX_LEN] = "master/"; // top-level directory (master)

    struct stat st = {0};
    if (stat(directory, &st) == -1) {
        mkdir(directory, 0700);
        printf("Top-level directory created.\n");
    } else printf("Top-level directory already exists.\n");

    while(1) {
        printf("Enter subdirectory/file name ('stop'): ");
        scanf("%s", filename);

        if(strcmp(filename, "stop") == 0) {
            printf("\nExiting...\n");
            break;
        }

        char subdir[MAX_LEN];
        char file[MAX_LEN];
        sscanf(filename, "%[^/]/%s", subdir, file);

        char subdirectory[MAX_LEN];
        strcpy(subdirectory, directory);
        strcat(subdirectory, subdir);

        if (stat(subdirectory, &st) == -1) {
            mkdir(subdirectory, 0700);
            printf("Subdirectory '%s' created in top-level directory '%s'.\n", subdir, directory);
        }

        char filepath[MAX_LEN];
        strcpy(filepath, subdirectory);
        strcat(filepath, "/");
        strcat(filepath, file);

        FILE* fp = fopen(filepath, "w");
        if(fp == NULL) {
            printf("Error creating file.\n");
            exit(1);
        }

        printf("File '%s' created in subdirectory '%s'.\n", file, subdir);

        fclose(fp);
    }
    
    printf("Removing the top-level directory and all its files...\n");
    char command[MAX_LEN];
    sprintf(command, "rm -r %s", directory);
    system(command);

    return 0;
}
