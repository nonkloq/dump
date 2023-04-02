/* Mutual Exclusion with test_and_set & compare_and_swap (Critical Section Problem)*/
#include <stdio.h>
#include <stdbool.h>
#include <stdatomic.h>
#include <pthread.h>
#include <unistd.h>

int my_fav_num = -8;
bool lock=false;


bool test_and_set(bool *target){
    // bool rv = *target;
    // *target = true;
    // return rv;
    return atomic_exchange(target, true);
}

int compare_and_swap(bool *val, bool expected, bool new_val){
    // int temp = *val;
    // if (*val == expected) *val = new_val;
    // return temp;
    return atomic_exchange(val, new_val) == expected;
}


void write_fav_num(int num){
    printf("\nPrevious Fav num: %d\n",my_fav_num);
    my_fav_num = num;
    printf("Current Fav num: %d\n\n",my_fav_num);
}


void* thread_func(void* arg) {
    int thread = *(int*)arg;
    for (int i = 0; i < 10; i++) {
        // while (compare_and_swap(&lock, false, true) != false) {}    
        
        while (test_and_set(&lock)) {}
        
        /* critical Section */
        printf("Thread %d entered critical section.\n", thread);
        write_fav_num(thread);
        sleep(1);
        
        /* remainder section */
        printf("Thread %d exited critical section.\n", thread);

        // Release lock
        lock = false;
        printf("Lock Release from: %d\n",thread);
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    int id1 = 69, id2 = 420;

    pthread_create(&thread1, NULL, thread_func, &id1);
    pthread_create(&thread2, NULL, thread_func, &id2);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    return 0;
}


