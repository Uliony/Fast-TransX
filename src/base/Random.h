#ifndef RANDOM_H
#define RANDOM_H

#include "Setting.h"
#include <algorithm>
#include <cstdlib>

// the random seeds for all threads.
uint64_t next_random[MAX_THREADS];

// reset the random seeds for all threads
extern "C" void setSeed(unsigned int seed) {
  unsigned int local_seed = seed;

  std::generate(next_random, next_random + MAX_THREADS,
                [&local_seed]() { return rand_r(&local_seed); });
}

// get a random integer for the threadIndex-th thread with the corresponding
// random seed.
uint64_t randd(INT threadIndex) {
  next_random[threadIndex] =
      next_random[threadIndex] * (uint64_t)(25214903917) + 11;
  return next_random[threadIndex];
}

// get a random integer from the range [0,x) for the threadIndex-th thread.
INT randMax(INT threadIndex, INT x) {
  INT res = static_cast<INT>(randd(threadIndex) % x);
  while (res < 0)
    res += x;
  return res;
}

#endif  // RANDOM_H
