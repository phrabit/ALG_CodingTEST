class Solution {
    fun solution(money: Int): IntArray {
        
        // arrayListOf와는 다름 -> 얘는 동적이므로 추가 가능
        // 즉, arrayList와 배열간에 가장 큰 차이를 뽑자면 동적, 정적인 크기이다.

// IntArray는 그냥 Int 타입의 데이터를 저장하는 배열이므로 선언 시 size를 지정해주며 이후 원소를 추가하거나 제거가 불가능하다.

// ( index를 통하여 값에 접근하여 읽기/쓰기는 가능하다.)
        
        val cnt:Int = money/5500
        val rest:Int = money%5500
        
        var answer: IntArray = intArrayOf(cnt, rest)
        
        return answer
    }
}