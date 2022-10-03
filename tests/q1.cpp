#include <stdio.h>
int global = 100;
void* thread_function(void *arg);

void* print_id(void *argument) 
{
    int value = *((int*)(&argument));
    printf("value=%d; global=%d\n", value, global);
    return NULL;
}
 
int main() {
    pthread_t threads[2];
    ++global;
    for (int i = 0; i < 2; ++i) {
        pthread_create(&threads[i], NULL, print_id, (void) i);
    }
    for (int i = 0; i < 2; ++i) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
