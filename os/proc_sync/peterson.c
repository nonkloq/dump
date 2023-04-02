/* Peterson's Solution for Mutual Exclusion (Critical Section Problem)*/
#include <stdio.h>
#include <stdbool.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_PROCESSES 2


int turn = 0;
bool flag[NUM_PROCESSES] = {false};
int my_fav_num = -8;

void write_fav_num(int num){
    printf("\nPrevious Fav num: %d\n",my_fav_num);
    my_fav_num = num;
    printf("Current Fav num: %d\n\n",my_fav_num);
}


// Process 0
void *process_0() {
    while (true) {
        // Entry section
        flag[0] = true;
        turn = 1;
        while (flag[1] && turn == 1) {}
        printf("Process 0 is in the critical section.\n");
        
        write_fav_num(69);
        sleep(5);

        // Exit section
        flag[0] = false;
        printf("Process 0 is in the remainder section.\n");
    }
    return NULL;
}

// Process 1
void *process_1() {
    while (true) {
        // Entry section
        flag[1] = true;
        turn = 0;
        while (flag[0] && turn == 0) {}
        printf("Process 1 is in the critical section.\n");
                
        write_fav_num(420);
        sleep(2);        
        // Exit section
        flag[1] = false;
        printf("Process 1 is in the remainder section.\n");
    }
    return NULL;
}

int main() {
     pthread_t thread_0, thread_1;
    
    pthread_create(&thread_0, NULL, process_0, NULL);
    pthread_create(&thread_1, NULL, process_1, NULL);
    
    // wait main thread to join 0 & 1
    pthread_join(thread_0, NULL);
    pthread_join(thread_1, NULL);


    return 0;
}
