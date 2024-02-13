-- FIRST_HALF테이블의 SHIPMENT_ID는 JULY테이블의 SHIPMENT_ID의 외래 키입니다.
-- JULY테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키입니
-- 7월에는 아이스크림 주문량이 많아 같은 
-- 아이스크림에 대하여 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가 있습니다. 
-- 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 됩니다.

-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT A.FLAVOR
FROM (SELECT * FROM FIRST_HALF 
      UNION
      SELECT * FROM JULY) AS A
GROUP BY A.FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3

