/* Dining Philosopher Problem using mutex*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define N 5

pthread_t philosophers[N];
pthread_mutex_t chopsticks[N];

int tf=0;

void *philosopher(void *arg){
    int id = *(int*)arg;
    int left_chopstick = id;
    int right_chopstick = (id + 1) % N;

    int p_notate = 1;
    while(p_notate){  // for(int i=0;i<2;i++)// only 2 chance for each (not the original problem)
        // Pick up left chopstick
        pthread_mutex_lock(&chopsticks[left_chopstick]);
        printf("Philosopher %d picks up left chopstick %d\n", id, left_chopstick);

        // Pick up right chopstick
        if(pthread_mutex_trylock(&chopsticks[right_chopstick]) == 0){
            printf("Philosopher %d picks up right chopstick %d\n", id, right_chopstick);
            printf("Philosopher %d is eating\n", id);
            sleep(2);
            printf("Philosopher %d is done eating\n\n", id);
            tf++;
            p_notate=0;
            // Release right chopstick
            pthread_mutex_unlock(&chopsticks[right_chopstick]);
            printf("Philosopher %d puts down right chopstick %d\n", id, right_chopstick);
        } else printf("Philosopher %d can't get right chopstick %d\n\n", id, right_chopstick) ;

        // Release left chopstick
        pthread_mutex_unlock(&chopsticks[left_chopstick]);
        printf("Philosopher %d puts down left chopstick %d\n", id, left_chopstick);

        // Think (let'em use resource)
        printf("Philosopher %d is thinking\n\n", id);
        sleep(5);
    }

    pthread_exit(NULL);
}

int main(){
    int i, id[N];
    pthread_mutex_init(chopsticks, NULL);

    for(i=0; i<N; i++){
        id[i] = i;
        pthread_create(&philosophers[i], NULL, philosopher, &id[i]);
    }

    for(i=0; i<N; i++){
        pthread_join(philosophers[i], NULL);
    }

    pthread_mutex_destroy(chopsticks);
    printf("%d Philosophers Ate %d Food!\n",N,tf);
    return 0;
}
