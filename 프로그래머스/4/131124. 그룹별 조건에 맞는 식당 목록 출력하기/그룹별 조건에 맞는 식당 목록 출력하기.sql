-- MEMBER_ID 가 FK임.
-- MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
-- 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬

# 최대 맥스리뷰 구하는 쿼리 
# SELECT MAX(MAX_REVIEW) FROM
#     (SELECT COUNT(*) AS MAX_REVIEW
#     FROM MEMBER_PROFILE AS A
#     INNER JOIN REST_REVIEW AS B
#     ON A.MEMBER_ID = B.MEMBER_ID
#     GROUP BY A.MEMBER_NAME) AS SUBQUERY


SELECT A.MEMBER_NAME,
       B.REVIEW_TEXT,
       DATE_FORMAT(B.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE AS A
INNER JOIN REST_REVIEW AS B ON A.MEMBER_ID = B.MEMBER_ID
WHERE (SELECT COUNT(*) 
       FROM REST_REVIEW 
       WHERE MEMBER_ID = A.MEMBER_ID) = (SELECT MAX(MAX_REVIEW)
                                          FROM (SELECT COUNT(*) AS MAX_REVIEW
                                                FROM MEMBER_PROFILE AS A
                                                INNER JOIN REST_REVIEW AS B
                                                ON A.MEMBER_ID = B.MEMBER_ID
                                                GROUP BY A.MEMBER_NAME) AS SUBQUERY)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;

    