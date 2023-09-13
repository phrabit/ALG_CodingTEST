class Solution {
    fun solution(arr: IntArray): Double {
        
        // arr.average() 평균 바로 구하기
        // arr.sum() 합계 구하기
        
        var sum = 0
        val len = arr.size // 배열(array)의 길이 : .size
        
        for (i in arr){
            sum += i
        }
        
        var answer:Double = sum.toDouble()/len.toDouble()
        
        return answer
    }
}