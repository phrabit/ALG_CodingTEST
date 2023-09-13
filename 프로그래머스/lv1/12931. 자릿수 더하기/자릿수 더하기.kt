class Solution {
    fun solution(n: Int): Int {
        var answer = 0

        val str_n : String = n.toString()
        
        for (i in str_n) {
            answer += (i.toInt()-48)
        }

        return answer
    }
}