#include "printlib.h"

int main(){
  bool x;
  int y;
  if (x) {
    println_int(y * x);
  }
  return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 7 col 16: invalid type for multiplicative operands: integer and boolean
