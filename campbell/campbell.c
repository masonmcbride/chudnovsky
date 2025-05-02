/*-*- compile-command: gcc -o campbell -O3 -Wall -fno-strict-aliasing -fPIC -I"/Users/mason/w/cs/fun/chudnovsky/pari/GPDIR/include" campbell.c -L/Users/mason/w/cs/fun/chudnovsky/pari/GPDIR/lib -lpari -*-*/
#include <pari/pari.h>

/* Function Prototype */
void campbell_init(long prec);

/* Global Variables */
static GEN lambda1105;
static GEN boldJ3315;
static GEN x3315;
static GEN lambdaast3315;
static GEN lambdaast13260;
static GEN x13260;
static GEN z13260;
static GEN t3315;
static GEN alpha3315;
static GEN alpha13260;
static GEN b13260;
static GEN a13260;

/* Initialize Campbell Variables */
void campbell_init(long prec) {
  /* Initialize variables step-by-step */
  lambda1105 = gmul(gmul(gmul(gpowgs(gdivgs(gaddgs(gsqrt(stoi(5), prec), 1), 2), 12), gpowgs(gaddsg(4, gsqrt(stoi(17), prec)), 3)), gpowgs(gdivgs(gaddsg(15, gsqrt(stoi(221), prec)), 2), 3)), gpowgs(gaddsg(8, gsqrt(stoi(65), prec)), 3));
  boldJ3315 = gneg(gdiv(gmulsg(64, gsqr(lambda1105)), gmul(gsubgs(gsqr(lambda1105), 1), gpowgs(gsubgs(gmulsg(9, gsqr(lambda1105)), 1), 3))));
  x3315 = gmul(ginv(stoi(8)), gadd(gsubsg(2, gdiv(gmulsg(3, gpow(gneg(ginv(boldJ3315)), gdivgs(gen_2, 3), prec)), gpow(gaddsg(-1, gsqrt(gdiv(gaddsg(-1, boldJ3315), boldJ3315), prec)), ginv(stoi(3)), prec))), gmulsg(3, gpow(gdiv(gsubsg(1, gsqrt(gdiv(gaddsg(-1, boldJ3315), boldJ3315), prec)), boldJ3315), ginv(stoi(3)), prec))));
  lambdaast3315 = gdiv(gsqrt(gsubsg(1, gsqrt(gsubsg(1, x3315), prec)), prec), gsqrt(gen_2, prec));
  lambdaast13260 = gdiv(gsubsg(1, gsqrt(gsubsg(1, gsqr(lambdaast3315)), prec)), gaddsg(1, gsqrt(gsubsg(1, gsqr(lambdaast3315)), prec)));
  x13260 = gmulsg(4, gsub(gsqr(lambdaast13260), gpowgs(lambdaast13260, 4)));
  z13260 = gdiv(gmulsg(-27, x13260), gpowgs(gsubsg(1, gmulsg(4, x13260)), 3));
  t3315 = gadd(gadd(gadd(gadd(gsub(gadd(gadd(gdiv(readseq("1095255033002752301233099478037584"), readseq("2050242335692983321671746996556833")), gmul(gmul(gdiv(readseq("1006588064225996719872149534306400"), readseq("34854119706780716468419698941466161")), gsqrt(stoi(17), prec)), gsqrt(stoi(5), prec))), gmul(gdiv(readseq("692779168175128551453280427070000"), readseq("34854119706780716468419698941466161")), gsqrt(stoi(17), prec))), gmul(gdiv(readseq("136434536163779492503565618457696"), readseq("2050242335692983321671746996556833")), gsqrt(stoi(5), prec))), gmul(gdiv(readseq("400179322879781860521299209248000"), readseq("26653150364008783181732710955238829")), gsqrt(stoi(13), prec))), gmul(gmul(gmul(gdiv(readseq("1077564413015882021519209726762688"), readseq("453103556188149314089456086239060093")), gsqrt(stoi(13), prec)), gsqrt(stoi(17), prec)), gsqrt(stoi(5), prec))), gmul(gmul(gdiv(readseq("120226784218523863048087030809600"), readseq("64729079455449902012779440891294299")), gsqrt(stoi(17), prec)), gsqrt(stoi(13), prec))), gmul(gmul(gdiv(readseq("239369594240980944219359445009600"), readseq("26653150364008783181732710955238829")), gsqrt(stoi(13), prec)), gsqrt(stoi(5), prec)));
  alpha3315 = gdiv(gsub(gmul(gmulgs(gmul(gmul(gmul(ginv(gen_2), gsqrt(gdivgs(stoi(1105), 3), prec)), gsqrt(gsubsg(1, boldJ3315), prec)), gsubsg(1, t3315)), 2), gpow(gsubsg(1, gmulsg(4, x3315)), gdivgs(stoi(3), 2), prec)), gmul(gadd(gsubgs(gmulsg(4, x3315), 1), gsqrt(gsubsg(1, x3315), prec)), gsqrt(stoi(3315), prec))), gmulsg(2, gsubsg(1, gmulsg(4, x3315))));
  alpha13260 = gdiv(gsub(gmulsg(4, alpha3315), gmul(gmulsg(2, gsqrt(stoi(3315), prec)), gsqr(lambdaast3315))), gsqr(gaddsg(1, gsqrt(gsubsg(1, gsqr(lambdaast3315)), prec))));
  b13260 = gdiv(gmul(gmul(gaddgs(gmulsg(8, x13260), 1), gsqrt(gsubsg(1, x13260), prec)), gsqrt(stoi(13260), prec)), gpow(gsubsg(1, gmulsg(4, x13260)), gdivgs(stoi(3), 2), prec));
  a13260 = gdiv(gadd(gmul(gmulsg(2, gsubsg(1, gmulsg(4, x13260))), alpha13260), gmul(gadd(gsubgs(gmulsg(4, x13260), 1), gsqrt(gsubsg(1, x13260), prec)), gsqrt(stoi(13260), prec))), gmulsg(2, gpow(gsubsg(1, gmulsg(4, x13260)), gdivgs(stoi(3), 2), prec)));
}

/* Main Function */
int main() {
  pari_init(5000000, 2); /* Initialize PARI with default precision and stack size */
  long prec = 1000;      /* Precision in significant digits */

  /* Initialize Campbell variables */
  setrealprecision(1000, &prec);
  campbell_init(prec);

  /* Digits per iteration */
  pari_printf("Digits per iteration:\n");
  pari_printf("%Ps\n", gdiv(glog(gdivsg(-1, z13260), prec), glog(stoi(10), prec)));

  /* Digits from one iteration */
  GEN p1;
  {
    long n;
    p1 = gen_0;
    for (n = 0; n <= 1; ++n)
    {
      long l2;
      GEN p3;
      long l4;
      GEN p5;
      long l6;
      GEN p7;
      long l8;
      GEN p9;
      l2 = n - 1;
      {
        GEN i;	  /* int */
        p3 = gen_1;
        for (i = gen_0; cmpis(i, l2) <= 0; i = addis(i, 1))
          p3 = gmul(p3, gadd(ginv(gen_2), i));
      }
      l4 = n - 1;
      {
        GEN i;	  /* int */
        p5 = gen_1;
        for (i = gen_0; cmpis(i, l4) <= 0; i = addis(i, 1))
          p5 = gmul(p5, gadd(ginv(stoi(6)), i));
      }
      l6 = n - 1;
      {
        GEN i;	  /* int */
        p7 = gen_1;
        for (i = gen_0; cmpis(i, l6) <= 0; i = addis(i, 1))
          p7 = gmul(p7, gadd(gdivgs(stoi(5), 6), i));
      }
      l8 = n - 1;
      {
        GEN i;	  /* int */
        p9 = gen_1;
        for (i = gen_0; cmpis(i, l8) <= 0; i = addis(i, 1))
          p9 = gmul(p9, addsi(1, i));
      }
      p1 = gadd(p1, gmul(gmul(gdiv(gmul(gmul(p3, p5), p7), gpowgs(p9, 3)), gpowgs(z13260, n)), gadd(a13260, gmulgs(b13260, n))));
    }
  }

  pari_printf("Digits of first iteration:\n");
  pari_printf("%.1000Ps\n", p1);

  pari_close(); /* Clean up PARI */
  return 0;
}
