#include "printlib.h"

int main(){
  int x;
  string y;
  println_bool(x == y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 15: type mismatch for Equality operands: integer and string
