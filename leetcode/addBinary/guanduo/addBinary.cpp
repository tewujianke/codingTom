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
Use c++ to solve
 */
class Solution {
public:
    string addBinary(string a, string b) {
      int i = a.size()-1;  //reverse order. check LSB first
      int j = b.size()-1;
      string newString("");

      int carry = 0;
      while (i>=0 || j>=0 || carry) {  //while we are not finished looking at all bits (including the carry bits)
	int cur = carry;
	carry=0;
	if(i>=0) cur+=a[i--]-'0';
	if(j>=0) cur+=b[j--]-'0';
	if(cur==2){carry=1;cur=0;}  //we could get 2 or 3. Carry will always be 1 if cur is bigger than 1.
	if(cur==3){carry=1;cur=1;}
	char tmp = char('0'+cur);
	newString = newString.insert(0,&tmp); //add to new sring
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
