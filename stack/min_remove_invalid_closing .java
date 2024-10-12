"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/

Time complexity : O(n), where n is the length of the input string.
Space complexity : O(n), where n is the length of the input string.

"""
class Solution {
    public String minRemoveToMakeValid(String s) {
        StringBuilder result = removeInvalidClosing(s, '(', ')');
        result = removeInvalidClosing(result.reverse().toString(), ')', '(');

        return result.reverse().toString();
    }

    private StringBuilder removeInvalidClosing(String input, char open, char close){
        StringBuilder sb = new StringBuilder();
        int balance = 0;

        for(int index = 0; index < input.length(); index++){
            char letter = input.charAt(index);

            if(letter == open){
                balance++;
            }
            
            if(letter == close){
                if(balance == 0) continue;
                balance--;
            }

            sb.append(letter);
        }

        return sb;
    }

    public String minRemoveToMakeValid1(String s) {
        if(s == null || s.length() == 0){
            return s;
        }

        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        Set<Integer> invalidIndexes = new HashSet<>();

        for(int index = 0; index < s.length(); index++){
            char letter = s.charAt(index);

            if(letter == '('){
                stack.push(index);
            }else if (letter == ')'){
                if(!stack.isEmpty()){
                    stack.pop();
                }else{
                    invalidIndexes.add(index);
                }
            }
        }

        while(!stack.isEmpty()){
            invalidIndexes.add(stack.pop());
        }

        for(int index = 0; index < s.length(); index++){
            if(!invalidIndexes.contains(index)){
                sb.append(s.charAt(index));
            }
        }

        return sb.toString();
    }
}