#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
void xx();
void delay(int time);
void banner();

int main()
{
	banner();
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int cards_balance = 1100;
    printf("## I promise you will love the sounds ##\n\n");
	printf("Note: I don't use money in my games, i use cards!\n");
    while(con == 0)
	{
        printf("\n[1] Want to know how many cards you got?\n");
        printf("\n[2] Ask for fireworks\n");
        printf("\n[3] Leave like nothing happened...\n");
        int menu;
        printf("\n Choose number: ");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n You got: %d \n\n\n", cards_balance);
        }
        else if(menu == 2){
            printf("Currently on stock\n");
            printf("[1] Outdated fireworks \n");
            printf("[2] fireworks that gives you the flag\n");
            printf("Enter your choice: ");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These knockoff fireworks will cost you 900 each, enter the quantity you want: ");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= cards_balance){
                        cards_balance = cards_balance - total_cost;
                        printf("\nNumber of left cards: %d\n\n", cards_balance);
                    }
                    else{
                        printf("Got no cards you genius!\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("The flag you looking for costs 100000 of cards, and we only have 1 in stock\n");
                printf("Enter 1 to have look at it: ");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(cards_balance > 100000){
                        //char buf[64];
                        //fgets(buf, 63, f);
                        xx();
                        
                        }
                    
                    else{
                        printf("\nNo cards? maybe later\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}

void xx ()
{	
	 delay(1000);
	//0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
	//D o Y 0 u _ R 3 m e M 8 3 R _ t H E _ J O K E R ?
	char ee[13];
	char oo [13];
	ee[0] = 'D'; oo[0] = 'o'; ee[1] = 'Y'; oo[1] = '0'; ee[2] = 'u'; oo[2] = '_'; ee[3] = 'R'; oo[3] = '3'; ee[4] = 'm';
	oo[4] = 'e'; ee[5] = 'M'; oo[5] = '8'; ee[6] = '3'; oo[6] = 'R'; ee[7] = '_'; oo[7] = 't'; ee[8] = 'H'; oo[8] = 'E';
	ee[9] = '_';oo[9] = 'J'; ee[10] = 'O'; oo[10] = 'K'; ee[11] = 'E'; oo[11] = 'R'; ee[12] = '?'; oo[12] = '?';
	int i;
	int j;
	int k;
	printf("CSCFLAG{");
	for(i=0 , j= 0 ; i<=25; i++)
	{
		
		if (i % 2 == 0)
    	{
			printf("%c", ee[j]);
			j++;
    		delay(100);
    	}
    	if (i % 2 != 0)
    	{
    		printf("%c", oo[k]);
    		k++;
    		delay(100);
    		
		}
	}
	printf("}");
}

void delay(int time)
{
    int milli_seconds = time;
    clock_t start_time = clock();
    while (clock() < start_time + milli_seconds);
}
 

void banner(){   
printf("______ _                             _         _____ _                 \n");
printf("|  ___(_)                           | |       /  ___| |                \n");
printf("| |_   _ _ __ _____      _____  _ __| | _____ \\ `--.| |__   ___  _ __  \n");
printf("|  _| | | '__/ _ \\ \\ /\\ / / _ \\| '__| |/ / __| `--. \\ '_ \\ / _ \\| '_ \\ \n");
printf("| |   | | | |  __/\\ V  V / (_) | |  |   <\\__ \\/\\__/ / | | | (_) | |_) |\n");
printf("|_|   |_|_|  \\___| \\_/\\_/ \\___/|_|  |_|\\_\\___/\\____/|_| |_|\\___/| .__/ \n");
printf("                                                                | |    \n");
printf("                                                                |_|    \n");
}


