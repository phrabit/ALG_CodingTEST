class Solution {
    fun solution(my_string: String): String {
        
        // 문자열 역순 : str.reversed()
        
        var answer: String = ""
        
        for (i in my_string.reversed()){
            answer += i
        }
        
        return answer
    }
}