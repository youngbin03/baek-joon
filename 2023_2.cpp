#include <iostream>
#include <cmath>

int N;

bool primeNumber(int num){
    for(int i=2; i<(num/2)+1; i++){
        if(num%i == 0) return false;
    }
    return true;
}

void DFS(int num, int k){
    if(k == N){
        if(primeNumber(num)){
            std::cout << num << '\n';
            return;
        }
    }
    for(int i=0; i<9; i++){
        if(i%2 != 0){
            if(primeNumber(num*10+i)){
                DFS(num*10+i,k+1);
            }
        }
    }
}

int main(){
    std::cin >> N;
    
    for(int j=2; j<=9; j++){
        if(j==2||j==3||j==5||j==7){
            DFS(j,1);
        }
    }

    return 0;
}