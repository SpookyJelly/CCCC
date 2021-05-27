http://127.0.0.1:8000/

```
* http://127.0.0.1:8000/api/v1/accounts/ 
  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/registration/ 회원가입
  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/login/ 로그인
  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/logout/ 로그아웃
  POST http://127.0.0.1:8000/api/v1/accounts/delete/ 회원탈퇴 
  GET http://127.0.0.1:8000/api/v1/accounts/profile/ 현재 유저 정보
  GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/  해당 유저 프로필 
  GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/review/ 해당 유저 작성 리뷰 리스트 
  GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 폼 
  PUT http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 제출 
  POST http://127.0.0.1:8000/api/v1/accounts/follow/<str:username>/ 해당 유저 팔로우
  

* GET http://127.0.0.1:8000/api/v1/community/ 영화 전체 목록
  GET http://127.0.0.1:8000/api/v1/community/titles/ 영화 제목 목록
  GET http://127.0.0.1:8000/api/v1/community/review/ 리뷰 전체 목록
  POST http://127.0.0.1:8000/api/v1/community/review/  리뷰 생성
  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 디테일
  PUT http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 수정
  DELETE http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 삭제
  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 해당 리뷰 댓글 전체 목록
  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 댓글 생성
  PUT  http://127.0.0.1:8000/api/v1/community/
       review/<int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 수정
  DELETE  http://127.0.0.1:8000/api/v1/community/review/
       <int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 삭제
  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/review_like/ 해당 리뷰 좋아요
  GET  http://127.0.0.1:8000/api/v1/community/review/search/?q=%{태그1}%{태그2}/ 태그로 리뷰 검색xxxxxxxxxx * http://127.0.0.1:8000/api/v1/accounts/   POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/registration/ 회원가입  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/login/ 로그인  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/logout/ 로그아웃  POST http://127.0.0.1:8000/api/v1/accounts/delete/ 회원탈퇴   GET http://127.0.0.1:8000/api/v1/accounts/profile/ 현재 유저 정보  GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/  해당 유저 프로필   GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/review/ 해당 유저 작성 리뷰 리스트   GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 폼   PUT http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 제출   POST http://127.0.0.1:8000/api/v1/accounts/follow/<str:username>/ 해당 유저 팔로우  * GET http://127.0.0.1:8000/api/v1/community/ 영화 전체 목록  GET http://127.0.0.1:8000/api/v1/community/titles/ 영화 제목 목록  GET http://127.0.0.1:8000/api/v1/community/review/ 리뷰 전체 목록  POST http://127.0.0.1:8000/api/v1/community/review/  리뷰 생성  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 디테일  PUT http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 수정  DELETE http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 삭제  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 해당 리뷰 댓글 전체 목록  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 댓글 생성  PUT  http://127.0.0.1:8000/api/v1/community/       review/<int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 수정  DELETE  http://127.0.0.1:8000/api/v1/community/review/       <int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 삭제  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/review_like/ 해당 리뷰 좋아요  GET  http://127.0.0.1:8000/api/v1/community/review/search/?q=%{태그1}%{태그2}/ 태그로 리뷰 검색- http://127.0.0.1:8000/api/v1/accounts/   POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/registration/ 회원가입  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/login/ 로그인  POST http://127.0.0.1:8000/api/v1/accounts/rest-auth/logout/ 로그아웃  POST http://127.0.0.1:8000/api/v1/accounts/delete/ 회원탈퇴   GET http://127.0.0.1:8000/api/v1/accounts/profile/ 현재 유저 정보  GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/  해당 유저 프로필   GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/review/ 해당 유저 작성 리뷰 리스트   GET http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 폼   PUT http://127.0.0.1:8000/api/v1/accounts/<str:username>/update/ 해당 유저 프로필 수정 제출   POST http://127.0.0.1:8000/api/v1/accounts/follow/<str:username>/ 해당 유저 팔로우  - GET http://127.0.0.1:8000/api/v1/community/ 영화 전체 목록  GET http://127.0.0.1:8000/api/v1/community/titles/ 영화 제목 목록  GET http://127.0.0.1:8000/api/v1/community/review/ 리뷰 전체 목록  POST http://127.0.0.1:8000/api/v1/community/review/  리뷰 생성  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 디테일  PUT http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 수정  DELETE http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/detail/ 해당 리뷰 삭제  GET http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 해당 리뷰 댓글 전체 목록  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/comment/ 댓글 생성  PUT  http://127.0.0.1:8000/api/v1/community/       review/<int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 수정  DELETE  http://127.0.0.1:8000/api/v1/community/review/       <int:review_id>/comment/<int:comment_id>/detail/ 해당 댓글 삭제  POST http://127.0.0.1:8000/api/v1/community/review/<int:review_id>/review_like/ 해당 리뷰 좋아요  GET  http://127.0.0.1:8000/api/v1/community/review/search/?q=%{태그1}%{태그2}/ 태그로 리뷰 검색
```

