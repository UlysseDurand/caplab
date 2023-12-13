#include "printlib.h"

int main(){
  bool x;
  if (x) {

  } else {
    println_int(x);
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 8 col 4: invalid type for println_int statement: boolean
