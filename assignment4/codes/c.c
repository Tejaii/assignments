#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double **P, **Q, **R, **M, **X;
    double N;  // Declare N as a scalar, since Matnorm likely returns a scalar

    // Create matrices
    P = createMat(2, 1);
    Q = createMat(2, 1);
    R = createMat(2, 1);
    M = createMat(2, 1);
    X = createMat(2, 1);

    // Assign values to matrices
    P[0][0] = 2;
    P[1][0] = 2;
    Q[0][0] = -4;
    Q[1][0] = -4;
    R[0][0] = 5;
    R[1][0] = -8;

    // Perform matrix operations
    M = Matadd(P, Q, 2, 1);
    M = Matscale(M, 2, 1, 0.5);
    X = Matsub(R, M, 2, 1);
    N = Matnorm(X, 2);  // Assuming Matnorm returns a scalar

    // Write the result to file
    FILE *file = fopen("output.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write matrix M and norm N to the file
    fprintf(file, "Norm of X: %.3lf\n", N);

    fclose(file);

    // Free matrices
    freeMat(P, 2);
    freeMat(Q, 2);
    freeMat(R, 2);
    freeMat(M, 2);
    freeMat(X, 2);

    return 0;
}

