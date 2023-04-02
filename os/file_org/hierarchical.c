#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#define MAX_LEN 100

int main() {
    char filename[MAX_LEN];
    char directory[MAX_LEN] = "root/"; // top-level directory (root)

    struct stat st = {0};
    if (stat(directory, &st) == -1) {
        mkdir(directory, 0700);
        printf("Top-level directory created.\n");
    } else printf("Top-level directory already exists.\n");

    while(1) {
        printf("\nEnter file name ('stop'): ");
        scanf("%s", filename);

        if(strcmp(filename, "stop") == 0) {
            printf("\nExiting...\n");
            break;
        }

        char subdirpath[MAX_LEN];
        printf("Enter subdirectory path (relative to '%s'): ", directory);
        scanf("%s", subdirpath);

        char filepath[MAX_LEN];
        strcpy(filepath, directory);
        strcat(filepath, subdirpath);


        char newpath[MAX_LEN] = "";
        char* token = strtok(filepath, "/");
        while(token != NULL) {
            strcat(newpath, token);
            strcat(newpath, "/");

            struct stat st = {0};
            if (stat(newpath, &st) == -1) {
                if(mkdir(newpath, 0700) == -1) {
                    printf("Error creating directory '%s'\n", newpath);
                    exit(1);
                }
                printf("New Directory '%s' created.\n", newpath);
            }
            token = strtok(NULL, "/");        
        }



        FILE* fp = fopen(strcat(newpath, "/"), "w");
        strcat(newpath, filename);
        fp = fopen(newpath, "w");
        if(fp == NULL) {
            printf("Error creating file.\n");
            exit(1);
        }

        printf("File '%s' created in subdirectory '%s'.\n", filename, subdirpath);

        fclose(fp);
    }

    printf("Removing the top-level directory and all its files...\n");
    char command[MAX_LEN];
    sprintf(command, "rm -r %s", directory);
    system(command);

    return 0;
}
