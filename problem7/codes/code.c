#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<openssl/rand.h>

/* In this question, random variables X_1 and X_2 for events A and B respectively, are defined as indicator random variables.
 * i.e., they take value 1 if their respective event occurs, 0 if the event doesnt occur. We have to find the probability that at least one of the event occurs.
 */

int random_number(double p){
    unsigned char random_byte;
    if (RAND_bytes(&random_byte, 1) != 1) {
        fprintf(stderr, "Error generating random byte\n");
        exit(1);
    }
  /*
  * we generate a random number between 0 and 255, then scale it down to a number from   
  * 0 to 1 and we retun 0 only if the number is between 0 and p
  */ 
    double random_value = random_byte / 255.0;
    return random_value > p ? 0 : 1; 
}

//function to generate the probability of the union of the 2 events
float* union_probability(float p_a, float p_b, float p_a_p_b, int n){
	float* arr = malloc(sizeof(float) * 4);
	int count_X_1_or_X_2 = 0, count_X_1 = 0, count_X_2 = 0, count_X_3 = 0;

	//seeding the random number generator

	for(int i=0;i<n;i++){
		int X_1 = random_number(p_a);
		int X_2 = random_number(p_b);
		int X_3 = random_number(p_a_p_b);

		count_X_1 += X_1;
		count_X_2 += X_2;
		count_X_3 += X_3;
	}
	
	//using boolean algebra's property that P(A + B) = P(A) + P(B) - P(AB)
	arr[0] = (float)count_X_1 / n;
	arr[1] = (float)count_X_2 / n;
	arr[2] = (float)count_X_3 / n;
	arr[3] = (float)(count_X_1 + count_X_2 - count_X_3) / n;
	return arr;
}

void freeMemory(float* arr){
	free(arr);
}
