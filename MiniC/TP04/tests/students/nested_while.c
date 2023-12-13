#include "printlib.h"

int main() {
    int i;
    int j;
    i = 0;
    j = 0;
    while (i < 2) {
      while (j < 2) {
        println_int(i);
        j = j+1;
      }
    i = i+1;
    }
    return 0;
}
// EXPECTED
// 0
// 0
