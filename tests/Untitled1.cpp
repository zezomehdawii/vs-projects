#include <stdio.h>

int x = 30; int y = 100; int z = 500;

void secondLevel() { printf("\n The secondLevel number is %i",y);}

void oneLevel() { printf("\n The oneLevel number is %i",x);
secondLevel(); }

void oneLevelAgain() {
printf("\n The oneLevelAgain number is %i",z);}

int main(){
oneLevel();
oneLevelAgain();
return 0;
}


