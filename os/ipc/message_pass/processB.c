#include <stdio.h>
#include <stdlib.h>
#include <mqueue.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

#define QUEUE_NAME "/my_mq"
#define MAX_MSG_SIZE 1024
#define MSG_STOP "exit"

int main()
{
    mqd_t mq;
    char buffer[MAX_MSG_SIZE];
    int bytes_read;

    // open the message queue
    mq = mq_open(QUEUE_NAME, O_RDONLY);

    if (mq == -1) {
        perror("mq_open");
        exit(1);
    }

    printf("Waiting for messages from process A...\n");

    // process A read 
    while(1){
        bytes_read = mq_receive(mq, buffer, MAX_MSG_SIZE, NULL);

        if (bytes_read == -1) {
            perror("mq_receive");
            exit(1);
        }
        if(strcmp(buffer, MSG_STOP) == 0){
            printf("Exiting...\n");
            break;
        }

        printf("Message from process A: %s :)\n", buffer);

    } 

    if (mq_close(mq) == -1) {
        perror("mq_close");
        exit(1);
    }

    return 0;
}
