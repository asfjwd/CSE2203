/*
Sample Input : +5V -5V +5V +5V -5V -5V -5V +5V
Expected Output : 01001110
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  // freopen("output.txt", "w", stdout);

  string input_s, output_s;
  string voltage_level[] = {"-5V", "+5V"};
  getline(cin, input_s);
  for(int i = 0; i < input_s.length(); i++){ 
    if(input_s[i] == ' ') continue;
    else if(input_s[i] == '+' or input_s[i] == '-'){
      int voltage = 0;
      char sign = input_s[i];
      for(i++; i < input_s.length(); i++){
        if( !(input_s[i] >= '0' and input_s[i] <= '9')) break;
        voltage = voltage * 10 + input_s[i] - '0';
      }
      if(voltage) output_s += (sign == '+' ? "0" : "1");
    }
    else {
      cout << "Error! Invalid Input.\n";
      return 0;
    }
  }
  cout << output_s << endl;
}
