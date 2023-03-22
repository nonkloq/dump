#include<iostream>
#include<cstdlib>
using namespace std;


string ntor(int num);
int main(int argc,char* argv[]){

  if (argc == 1){
    cout << "Number Argument is Required!!"<<endl;
    return 1;
  }
  cout << ntor(atoi(argv[1]))<< endl;
  return 0;
}

string ntor(int num){
  string h[13] = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
  int n[13] = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
  string out = "";
  for (int i = 12;i>=0;i--){
    while (num >= n[i]){
      out += h[i];
      num -= n[i];
    }
  }
  return out;

}
