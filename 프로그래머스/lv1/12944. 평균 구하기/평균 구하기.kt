class Solution {
    fun solution(arr: IntArray): Double {
        
        var sum = 0
        val len = arr.size // 배열(array)의 길이 : .size
        
        for (i in arr){
            sum += i
        }
        
        var answer:Double = sum.toDouble()/len.toDouble()
        
        return answer
    }
}