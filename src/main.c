#define _POSIX_C_SOURCE 1

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <tgmath.h>
#include "fft-interp.h"

int main(int argc, char* argv[]){    
    int n, i;
    double spacing = NAN;
    char buff[100];

    n = atoi(argv[1]);
    spacing = atof(argv[2]);

    int n_ = 1;
    while(n_<n) n_ *= 2;

    double *x = (double *)malloc((n_+1)*sizeof(double));

    for(i=0; i<n; ++i){
      x[i]=atof(argv[i+3]);
    }

    trig_interpolate(x, x, n);

    double epsilon = 1e-9; 
    printf("f(x) = %g", fabs(x[0])>epsilon ? x[0] : 0);
    for(i=1; i<=n_/2; ++i){
      double cos = x[2*i-1];
      double sin = x[2*i];
      if(isnan(spacing)){ 
        if(fabs(cos)>epsilon)
          printf("%+g*cos(%g*x)", cos, ((float)i*n)/n_);
        if(fabs(sin)>epsilon)
          printf("%+g*sin(%g*x)", sin, ((float)i*n)/n_);
      }else{ 
        if(fabs(cos)>epsilon)
          printf("%+g*cos(%g*pi*x)", cos, 2*i/(n_*spacing));
        if(fabs(sin)>epsilon)
          printf("%+g*sin(%g*pi*x)", sin, 2*i/(n_*spacing));
      }
    }
    free(x);
    return 0;
}
