// whattotest.cpp
#include <math.h>
#include <string>
 
using namespace std;

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


string reverse(const string a){
    string temp = "";

    int length = a.length();

    for(int i = length-1; i>=0; --i)
    {
        temp += a[i];
    }

    return temp;

}
