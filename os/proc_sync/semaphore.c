/*Mutual exclusion using semaphore */
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
sem_t mutex;


int my_fav_num = -8;

void write_fav_num(int num){
    printf("\nPrevious Fav num: %d\n",my_fav_num);
    my_fav_num = num;
    printf("Current Fav num: %d\n\n",my_fav_num);
}


void *thread_function(void *arg){
    sem_wait(&mutex);

    // Critical section
    printf("Thread %d is in the critical section.\n", *(int*)arg);
    write_fav_num(*(int*)arg);
    sleep(3);

    
    sem_post(&mutex); // Release

    pthread_exit(NULL);
}

int main(){
    int i;
    pthread_t threads[5];
    int thread_args[5];

    sem_init(&mutex, 0, 1);

    for(i=0; i<5; i++){
        thread_args[i] = i+1;
        pthread_create(&threads[i], NULL, thread_function, &thread_args[i]);
    }

    for(i=0; i<5; i++){
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&mutex);

    return 0;
}
