/* Reader Writers Problem using mutex*/
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_READERS 5
#define NUM_WRITERS 2

int data = 0;
int num_readers = 0;
pthread_mutex_t lock;
pthread_mutex_t write_lock;

void *reader(void *arg){
    int id = *(int*)arg;

    while(1){
        pthread_mutex_lock(&lock);
        num_readers++;
        if(num_readers == 1){
            pthread_mutex_lock(&write_lock);
        }
        pthread_mutex_unlock(&lock);

        printf("Reader %d reads data: %d\n", id, data);
        sleep(2);

        pthread_mutex_lock(&lock);
        num_readers--;
        if(num_readers == 0){
            pthread_mutex_unlock(&write_lock);
        }
        pthread_mutex_unlock(&lock);

        sleep(5);
    }

    pthread_exit(NULL);
}

void *writer(void *arg){
    int id = *(int*)arg;

    while(1){
        pthread_mutex_lock(&write_lock);

        data++;
        printf("Writer %d writes data: %d\n", id, data);
        sleep(5);

        pthread_mutex_unlock(&write_lock);
        usleep(10);
    }

    pthread_exit(NULL);
}

int main(){
    int i, id[NUM_READERS + NUM_WRITERS];
    pthread_t readers[NUM_READERS], writers[NUM_WRITERS];

    // init locks
    pthread_mutex_init(&lock, NULL);
    pthread_mutex_init(&write_lock, NULL);

    for(i=0; i<NUM_READERS; i++){
        id[i] = i;
        pthread_create(&readers[i], NULL, reader, &id[i]);
    }

    for(i=0; i<NUM_WRITERS; i++){
        id[i+NUM_READERS] = i;
        pthread_create(&writers[i], NULL, writer, &id[i+NUM_READERS]);
    }

    for(i=0; i<NUM_READERS; i++){
        pthread_join(readers[i], NULL);
    }

    for(i=0; i<NUM_WRITERS; i++){
        pthread_join(writers[i], NULL);
    }

    pthread_mutex_destroy(&lock);
    pthread_mutex_destroy(&write_lock);

    return 0;
}
