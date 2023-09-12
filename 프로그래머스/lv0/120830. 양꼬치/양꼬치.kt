class Solution {
    fun solution(n: Int, k: Int): Int {
        
        val free : Int = n/10
        
        var pay : Int = n*12000 + (k-free)*2000
        
        return pay
        
        
        
    }
}