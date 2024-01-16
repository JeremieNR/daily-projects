#include <stdio.h>

// sum_digits(x) returns the sum of all digits in integer x.
// requires: x must be a non-negative integer.
int sum_digits(int x) {
  if (x==0) {
    return 0;
  }
  if (!(x%10==0)) {
    return (1 + sum_digits(x - 1));
  }
  return sum_digits(x/10);
}

void test_sum_digits(void) {
  printf("%d",sum_digits(1410065407)); //expects 28
  printf("\n");
  printf("%d",sum_digits(136)); //expects 10
  printf("\n");
  printf("%d",sum_digits(5)); //expects 5
  printf("\n");
  printf("%d",sum_digits(10000001)); //expects 2
  printf("\n");
  printf("%d",sum_digits(99999999));  //expects 72
  printf("\n");
  printf("%d",sum_digits(5829332));  //expects 32
  printf("\n");
  printf("%d",sum_digits(5892975)); //expects 45
  printf("\n");
  printf("%d",sum_digits(472748447)); //expects 47
  printf("\n");
  printf("%d",sum_digits(27437284)); //expects 37
  printf("\n");
  printf("%d",sum_digits(19448772)); //expects 42
  printf("\n");
  printf("%d",sum_digits(58285722)); //expects 39
  printf("\n");
  printf("%d",sum_digits(959295820)); //expects 49
  printf("\n");
  printf("%d",sum_digits(582894294)); //expects 51
}

int main(void) {
  test_sum_digits();
}