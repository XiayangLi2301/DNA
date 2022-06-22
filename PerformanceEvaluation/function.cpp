# include <iostream>
# include <cmath>
using namespace std;
int main(){
    double a,p;
    int N;
    a,N = cin>>('请输入a和N')
    p = func(a,N)
    cout<<"结果为:"<<p;
}
double func(double a,int N){
    s = power(a,N)
    t = 1;
    result = 0
    for(i=1;i++,i < N){
        t *= i;
        s += power(a,N)/ t;
    }
    result = power(a,N)/(power(a,N)+ t*(N-a)*s)
    return result
}