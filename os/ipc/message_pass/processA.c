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
    struct mq_attr attr;
    char buffer[MAX_MSG_SIZE];

    attr.mq_flags = 0;
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = MAX_MSG_SIZE;
    attr.mq_curmsgs = 0;

    mq = mq_open(QUEUE_NAME, O_CREAT | O_RDWR, S_IRWXU | S_IRWXG, &attr); // Creating MQueue

    if (mq == -1) {
        perror("mq_open");
        exit(1);
    }



    // read input and send it to process B
    while (strcmp(buffer, MSG_STOP)) {
        
        printf("Message to process B ('exit'): ");
        fgets(buffer, MAX_MSG_SIZE, stdin);
        int len = strlen(buffer);
        if (len > 0 && buffer[len - 1] == '\n') buffer[len - 1] = '\0';

        if (mq_send(mq, buffer, strlen(buffer) + 1, 0) == -1) {
            perror("mq_send");
            exit(1);
        }
    }

    if (mq_close(mq) == -1) { // Close MQueue
        perror("mq_close");
        exit(1);
    }

    if (mq_unlink(QUEUE_NAME) == -1) { // Delete Mqueue
        perror("mq_unlink");
        exit(1);
    }

    return 0;
}
