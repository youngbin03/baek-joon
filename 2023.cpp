#include <iostream>
#include <cmath>
#include <vector>

int a[1000001];
std::vector<int> v;

void primeNumber(int number) {
    int endnum = pow(10,number)-1;
    a[0] = 0; a[1] = 0;
    for(int i=2; i<=endnum; i++){
        a[i] = 1;
    }
    for(int i=2; i<=endnum; i++){
        if(a[i]==0) continue;

        for(int j=i*2; j<=endnum; j+=i){
            a[j] = 0;
        }
    }
}

int main(){
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    // cout.tie(NULL);
    int number;
    std::cin >> number;
    primeNumber(number);

    int startnum = pow(10,number-1);
    int endnum = pow(10,number)-1;
    int d = 1;
    for(int j=startnum; j<=endnum; j++){
        d = 1;
        for(int i = number-1; i>=0; i--){
            int num = j/pow(10,i);
            if(a[num]==0){
                d = 0;
                continue;
            }
        }
        if(d==1) std::cout << j << '\n';
    }
    return 0;
}