VALID PARENTHESES
-----------------------------------------------------------------------------------------
Runtime: 48 ms, faster than 74.79% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 98.20% of Python3 online submissions for Valid Parentheses.
-----------------------------------------------------------------------------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.