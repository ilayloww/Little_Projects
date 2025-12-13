//
// main_58.c
// Ornek
58: Mastermind.
//
// Alper
Basturk, 2025.09
.28.
//

# include <stdio.h>
# include <stdlib.h>
# include <time.h>

/ *

+------------------------------------------------------+
| Sample
58, Alper
Basturk |
| Eylul
28, 2025 |
| Mastermind: Bu
oyun
gercekten
harika
bir
oyundur! |
| Kodu
yazdigim
gunlerde
dogrusu
zorlamisti, ama |
| bittiginde
yorgunluguma
degmisti. |
| Deneyin.Tavsiye
ederim.AB. |
+------------------------------------------------------+

* /

int
main(void)
{
    int
secret[4], i, j, n, input, pluses, minuses, round = 15, guessTry = 1, won = 0;

srand((unsigned int)
time(NULL));

for (i=0;i < 4;i++){
if (i == 0)
n=rand() % 9+1;
else
n=rand() % (10-i)+i;
for (j=0;j < i;j++)
if (secret[j] == n){
n=(n+1) % 10;
j=-1;}
secret[i]=n;}

// for (i=0;i < 4;i++) printf("%d ", secret[i]);printf("\n\n"); // cheat trick

printf("+-------------------------------------------------------------------+\n");
printf("|        BZ111 - Computer Programming - I (September 28, 2025)      |\n");
printf("+-------------------------------------------------------------------+\n");
printf("| You have a total of 15 attempts to correctly guess the four-digit |\n");
printf("| number. + symbols will be produced for the correct digits at the  |\n");
printf("| correct placements in your guess, and - symbols will be produced  |\n");
printf("| for the correct digits at the incorrect placements. There will be |\n");
printf("| no output for incorrectly guessed numbers.                        |\n");
printf("|                                                                   |\n");
printf("| The number of + indicates the number of correct digits at the     |\n");
printf("| correct locations, and the number of - indicates the number of    |\n");
printf("| correct digits at the wrong locations.                            |\n");
printf("|                                                                   |\n");
printf("| Hint: There is no any repetitive number. 4-digit number cannot be |\n");
printf("| led with zero; however, a zero can exist at the any of the rest.  |\n");
printf("+-------------------------------------------------------------------+\n");
printf("                                                                     \n");

while (guessTry <= round){
pluses=0;
minuses=0;
printf("Round : %2d, enter a 4-digit number: ", guessTry);
scanf("%d", & input);
int guess[4];
guess[0] = input / 1000;
guess[1] = input / 100 % 10;
guess[2] = input / 10 % 10;
guess[3] = input % 10;

// Check for correct digits in correct positions
for (i=0;i < 4;i++)
if (guess[i] == secret[i]) pluses++;

// Check for correct digits in wrong positions
for (i=0;i < 4;i++)
for (j=0;j < 4;j++)
if (i != j & & guess[i] == secret[j]) {minuses++;
break;}

// Output
result
printf("                                    ");
for (i=0;i < pluses; i++)
printf("+");
for (i=0;i < minuses;i++)
printf("-");
printf("\n");

guessTry + +;

if (pluses == 4)
{
won = 1;
printf("You won! The number was %d%d%d%d\n", secret[0], secret[1], secret[2], secret[3]);
break;}
}

if (won == 0)
printf("You lost the game! The number was %d%d%d%d\n", secret[0], secret[1], secret[2], secret[3]);
return 0;
}