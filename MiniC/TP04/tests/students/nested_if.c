#include "printlib.h"

int main() {
    int x;
    int y;
    x = 2;
    y = 3;
    if (y > x) {
      if (y * x == 6) {
        println_int(42);
      }
    }
    return 0;
}
// EXPECTED
// 42
