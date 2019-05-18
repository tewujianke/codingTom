/*
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/  

#include <iostream>
#include <string>

using namespace std;

/*
Use c++ to solve as python is so damn easy
 */
class Solution {
public:
    string addBinary(string a, string b) {
      int i = a.size()-1;
      int j = b.size()-1;
      string newString("");

      int carry = 0;
      while (i>=0 || j>=0 || carry) {
	int cur = carry;
	carry=0;
	if(i>=0) cur+=a[i--]-'0';
	if(j>=0) cur+=b[j--]-'0';
	if(cur==2){carry=1;cur=0;}
	if(cur==3){carry=1;cur=1;}
	char tmp = char('0'+cur);
	newString = newString.insert(0,&tmp);
      }
      return newString;

    }
};




int main() {
  Solution s;
  string a = "11";
  string b = "1";
  string res = s.addBinary(a,b);
  cout<<res<<endl;
  return 0;
}
