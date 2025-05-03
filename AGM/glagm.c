// From: https://forums.freebsd.org/threads/multiple-precision-variables-in-freebsd.78593/
// glagm.c — Compute π via Gauss–Legendre (AGM) at arbitrary precision
/*
 Usage:

    // Compile (requires GMP & MPFR):
    gcc \
        -I$(brew --prefix gmp)/include \
        -I$(brew --prefix mpfr)/include \
        -L$(brew --prefix gmp)/lib \
        -L$(brew --prefix mpfr)/lib \
        glagm.c -lmpfr -lgmp -o glagm

    // Run & count produced digits:
    ./glagm <iterations> <bit-precision> \
        | grep -Eo '[0-9]+\.[0-9]+' \
        | tr -d '\n' \
        | wc -m

    // Locate first mismatch position:
    cmp -b <(./glagm <iterations> <bit-precision> \
            | grep -Eo '[0-9]+\.[0-9]+'       \
            | tr -d '\n' )                    \
        pi_1mil.txt                          \
    | awk '/differ:/ {                           \
        byte=$5;                               \
        idx = byte > 2 ? byte-2 : byte;        \
        printf "First mismatch at digit %d\n", idx;
    }'

 Replace <iterations> and <bit-precision> as needed.

 Examples:

    // Computing one million digits of pi
    ./glagm 19 3321928 \
        | grep -Eo '[0-9]+\.[0-9]+' \
        | tr -d '\n' \
        | wc -m
    
    // Verify one million digits of pi computation 
    cmp -b <(./glagm 19 3321928 \
            | grep -Eo '[0-9]+\.[0-9]+' \
            | tr -d '\n') \
        pi_1mil.txt \
    | awk '/differ:/ {
        byte=$5;
        idx = byte>2 ? byte-2 : byte;
        printf "First mismatch at digit %d\n", idx
    }'

*/

#include <stdio.h>
#include <gmp.h>
#include <mpfr.h>
#include <stdlib.h>
#include <assert.h>


int pi(unsigned int *stop, unsigned int *bt){
    mpfr_t a, b, t, temp_A;
    mpfr_init2 (a, *bt);
    mpfr_init2 (b, *bt);
    mpfr_init2 (t, *bt);
    mpfr_init2 (temp_A, *bt);
    unsigned long p;

    //Initialize the values according to the Gauss–Legendre algorithm.
    mpfr_set_d (a, 1.0, MPFR_RNDD);

    mpfr_set_d (b, 2.0, MPFR_RNDD);
    mpfr_sqrt (b, b, MPFR_RNDD);
    mpfr_ui_div (b, 1, b, MPFR_RNDD);

    mpfr_set_d (t, 0.25, MPFR_RNDD);

    p = 1;

    //Perform iterations
    while (*stop>=1){
        (*stop)--;
    
        mpfr_add (temp_A, a, b, MPFR_RNDD);
        mpfr_div_ui (temp_A, temp_A, 2, MPFR_RNDD);
 
        mpfr_mul (b, a, b, MPFR_RNDU);
        mpfr_sqrt (b, b, MPFR_RNDD);
 
        mpfr_sub (a, a, temp_A, MPFR_RNDD);
        mpfr_sqr (a, a, MPFR_RNDD);
        mpfr_mul_ui (a, a, p, MPFR_RNDU);
        mpfr_sub (t, t, a, MPFR_RNDD);
 
        mpfr_swap  (a, temp_A);
 
        p = 2 * p;
    }

    //Perform final calculation
    mpfr_add (a, a, b, MPFR_RNDD);
    mpfr_sqr (a, a, MPFR_RNDD);

    mpfr_mul_ui (t, t, 4, MPFR_RNDU);

    mpfr_div (a, a, t, MPFR_RNDD);

    //Print Out Answer
    printf ("\n===================\nPI: ");
    mpfr_out_str (stdout, 10, 0, a, MPFR_RNDD);
    printf ("\n===================\n\n");

    mpfr_clear (a);
    mpfr_clear (b);
    mpfr_clear (t);
    mpfr_clear (temp_A);
    mpfr_free_cache ();
    return 0;
}


int main(int argc, char * argv[]){
  unsigned int i,b;

  if (argc <= 2){
    printf ("Usage: %s <number of iterations> <number of bits>\n", argv[0]);
    return 1;
  }

  i = atoi(argv[1]);
  b = atoi(argv[2]);

  assert( i >= 1);
  assert( b >= 1);
  pi(&i,&b);

  return 0;
}