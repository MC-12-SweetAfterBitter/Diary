# Diary
회원가입
1. DB에 중복된 이름과 이메일 처리
2. 공백 처리
3. 패스워드 1차, 2차 동일한지 확인
4. 이메일 형식 확인
5. 회원정보 DB에 저장

로그인
1. DB에 있는 이메일과 비밀번호 확인
2. DB정보와 같으면 세션에 이메일과 이름정보를 저장하고 로그인


개인 다이어리
1. 로그인중이라면 개인 다이어리로, 아니라면 로그인 폼으로 이동
2. 업로드 시 다이어리와 세션 정보를 DB에 저장
3. 저장된 날짜순으로 정렬하며 로그인중인 세션값과 같은 DB만 불러옴

공유 다이어리
1. 업로드 시 다이어리 정보를 DB에 저장
2. 좋아요 버튼 클릭시 +1
3. 좋아요 버튼 기준으로 정렬 하여 DB를 불러옴



공통
1. 로그인 중일 떄는 모든 html에 세션정보가 할당된다
2. 로그인 시 특정폼이 변경되고 로그아웃 버튼이 활성화 된다

#22. 4. 1. 이동현
- 공감/개인 페이지 업로드, 목록 <a> 를 <div> 로 수정
- 일기장 쓰기 위치 오류 수정

#22. 4. 2. 이동현
- CSS > main_page > personal_page > write_button 코드 수정
- personal_page 내부 코드 정렬
- 코드 짜시면서 div 안닫혀 있는 부분 확인해주세요~

#22. 4. 2. 김명진
- 공유다이어리 기능 추가
- 좋아요 기능 추가

#22. 4. 3. 조수진
- 좋아요 버튼 수정했습니다!

#22. 4. 3. 김명진
- 회원가입 시 이메일 형식 확인하는 조건문 추가
  
#22. 4. 4. 조수진
- 다이어리 리스트 중앙 정렬
- 파일 첨부 폼 삭제
- 업로드한 다이어리 삭제 불가 안내 문구 추가
- 특정 box에 mouse hover over했을 경우, box-shadow 기능 추가

#22. 4. 5. 이동현
- gonggam_main.html : 글 리스트 제목, 작성자 부분 <div> 분류 후 위치 수정
- gonggam_main.css / personal_main.css : card, card_body 구분화 및 조정
- card, card_body 구분화에 따른 uploadDiary.js, gonggam_main.html, personal_main.html class 변경
- card_body : 높이 및 폰트 사이즈 수정
- 페이징 버튼 추가
- 로그인 / 회원가입 페이지 로고 이름 변경
- og 태그 추가

#22. 4. 5. 김명진
- 회원가입 성공 시 로그인 페이지로 바로 이동
- 유저 정보중 pw 암호화(예정)

#22. 4. 6. 조수진
- 공감 페이지 모달 기능 추가

#22. 4. 6. 이동현
- 로그인 / 회원가입 페이지 폼 상단 간격 조정
- 공감 / 개인 페이지 글 리스트 내용 규격 조정
- 개인 페이지 모달 기능 추가
- 모달 창 위치 수정 중