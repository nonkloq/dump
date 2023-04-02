#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <string.h>
#include <sys/wait.h>
#include <stdlib.h>

#define MAX_ARG 10
#define MAX_LENGTH 1024


void type_prompt(){
    printf("6shell9>");
}

int read_command(char* cmd, char** parms){
    char input[MAX_LENGTH];
    
    fgets(input, MAX_LENGTH, stdin);

    input[strcspn(input, "\n")] = '\0'; 
    
    char *token = strtok(input, " ");
    strcpy(cmd, token);
    int i = 0;
    while (token != NULL) {
        parms[i++] = token;
        token = strtok(NULL, " ");
    }

    parms[i] = NULL; 

    return i;
}


int main(){
    char cmd[MAX_ARG];
    char *parms[MAX_ARG];
    int status = 0;


    int num_args;

    while (1){
        type_prompt();
        num_args = read_command(cmd,parms);
        if (strcmp(cmd, "exit") == 0) { break;} 

        if (strcmp(cmd, "cd") == 0) { 
            if (num_args > 1) { chdir(parms[1]);} 
            else {chdir(getenv("HOME"));}
            continue;
        }

        
        pid_t pid = fork();
        if (pid != 0) {
            /* Parent */ 
            printf("[%d]Parent->[%d]Child\n",getpid(),pid);
            waitpid(-1, &status, 0); // waits for its child process to complete

        } else{
            /* Child */
            printf("[%d]Child\n",getpid());
            execvp(cmd, parms); // execute and return.
            printf("%s: command not found\n", cmd); 
            exit(1);
        }
    }

    return status;

}