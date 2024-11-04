#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"
int main ()  {
	double **P,**Q,**M;
	P=createMat(2,1);
	Q=createMat(2,1);
	M=createMat(2,1);
	P[0][0]=0;	
	Q[1][0]=0;
	M[0][0]=2;
	M[1][0]=-5;
    
	P[1][0]=2*(M[1][0]);
	Q[0][0]=2*(M[0][0]);


	FILE *file=fopen("output.dat","w");
	if (file == NULL)  {
		printf("Error opening file!\n");
		return 1;
        }


	fprintf(file,"P Q\n");
        fprintf(file,"%.2f %.2f\n",P[1][0],Q[0][0]);
	fclose(file);
	freeMat(P,2);
        freeMat(Q,2);
	freeMat(M,2);


	return 0;
}
