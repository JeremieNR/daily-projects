#include "stdio.h"
#include "math.h"

// time_dilation(t, v) returns the dilated time from the given time and velocity
// Note: t is in seconds and v is in meters per second
float time_dilation(float t, float v) {
  float c = 299792458.00;
  return (t/sqrt(1-((v*v)/(c*c))));
}


void test_time_dilation(void) {
  printf("%f",time_dilation(50, 20000000));
}


int main(void) {
  test_time_dilation();
}
