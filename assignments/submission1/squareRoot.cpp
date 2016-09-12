// whattotest.cpp
#include <math.h>
 
double squareRoot(const double a) {
    double b = sqrt(a);
    if(b != b) { // nan check
        return -1.0;
    }else{
        return sqrt(a);
    }
}


int addition(const int a, const int b){
	if(a == 0){
		return b;
	}else if (b==0){
		return a;
	}
	int sum = a+b;
	return sum;

}
