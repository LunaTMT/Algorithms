
//Brute force method
unsigned int countBits(unsigned long long n){
  int count = 0;
  
    while (n > 0) {
        count += n & 1;
        n >>= 1;
    }

    return count;
}


//Kernighan's algorithm
unsigned int countBits(unsigned long long n){
  int count = 0;
  
  while (n > 0){
    n &= (n-1);
    count++;
  }
  return count;
}