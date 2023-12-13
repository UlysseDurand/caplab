#include "printlib.h"

int main(){
  bool x;
  int y;
  println_bool(x < y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 15: invalid type for relational operands: boolean and integer
