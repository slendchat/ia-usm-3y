#include <unistd.h>

#include "../inc/utils.h"

void sleep_ms(int milliseconds) 
{
  usleep(milliseconds * 1000);
}