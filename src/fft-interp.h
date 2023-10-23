#ifndef FFT_INTERP_H
#define FFT_INTERP_H

int fft(double complex const *input, double complex *output, size_t n);
int trig_interpolate(double const *input, double *output, size_t n);

#endif
