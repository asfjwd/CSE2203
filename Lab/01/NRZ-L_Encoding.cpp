/*
Sample Input : 01001110
Expected Output : +5V, -5V, +5V, +5V, -5V, -5V, -5V, +5V
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  string input_s, output_s;
  string voltage_level[] = {"-5V", "+5V"};
  cin >> input_s;
  for(int i = 0; i < input_s.length(); i++){ 
    if(!(input_s[i] == '0' or input_s[i] == '1')){
      cout << "Error! Invalid Input!\n"; return 0;
    }
    output_s += (i ? ", " : "") + voltage_level[(input_s[i] - '0') ^  1];
  }
  cout << output_s << endl;
}
