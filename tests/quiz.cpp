#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
void* thread_function(void *arg);

 int i,j;
 int main() {
 pthread_t a_thread;  //thread declaration 

 pthread_create(&a_thread, NULL, thread_function, NULL);
//thread is created
 pthread_join(a_thread, NULL); 
 printf("Inside Main Program: ");
 for(j=20;j<25;j++)
 {
 printf("%d ",j);
 sleep(1);
 }
 }
 
 void* thread_function(void *arg) {
// the work to be done by the thread is defined in this function
 printf("Inside Thread: "); for(i=0;i<5;i++)
 {
 printf("%d ",i);
 sleep(1);
 }
 }
