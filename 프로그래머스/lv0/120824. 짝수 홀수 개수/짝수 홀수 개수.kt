class Solution {
    fun solution(num_list: IntArray): IntArray {
               
        var even_cnt:Int = 0
        var odd_cnt:Int = 0
        
        for (i in num_list) {
            if (i%2==0){
                even_cnt++
            }else{
                odd_cnt++
            }
        }
        
        var answer: IntArray = intArrayOf(even_cnt, odd_cnt)

        return answer
    }
}