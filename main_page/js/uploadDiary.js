const uploadButton = document.querySelector(".upload_button"); // 업로드 버튼 가져오기
const diaryName = document.querySelector(".name input"); // 작성자 제목
const diaryTitle = document.querySelector(".title input"); // 일기장 제목
const Year = document.querySelector("#year"); // 연도
const Month = document.querySelector("#month"); // 월
const Dates = document.querySelector("#date"); // 일
const diaryContent = document.querySelector("#floatingTextarea2"); // 일기장 내용

// 공감 다이어리
function uploadDiary_gonggam(event_1) {
  event_1.preventDefault();
  let name = diaryName.value; // 일기장 제목
  let title = diaryTitle.value; // 일기장 제목
  // let diaryYear = Year.options[Year.selectedIndex].value; // 작성 연도
  // let diaryMonth = Month.options[Month.selectedIndex].value; // 작성 월
  // let diaryDate = Dates.options[Dates.selectedIndex].value; // 작성 일
  let content = diaryContent.value; // 일기장 내용

  let temp_html = `<div class="card">
                    <div class="card-header">
                      <h5 class="card-header-title">제목 : ${title} <br> <label style="font-size: 16px"> 작성자 : ${name} </label></h5>
                      
                      <!--공감 버튼-->
                      <button type="button" class="gongamBtn">
                        <i class="fa-regular fa-heart fa-xl"></i>
                      </button>
                    </div>
                    <div class="card-body au">
                      <p class="card-text">
                        ${content}
                      </p>
                    </div>
                  </div>`;

  $(".diary_lists_2").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary_gonggam);

//개인 다이어리
function uploadDiary_personal(event_2) {
  event_2.preventDefault();
  let title = diaryTitle.value; // 일기장 제목
  let diaryYear = Year.options[Year.selectedIndex].value; // 작성 연도
  let diaryMonth = Month.options[Month.selectedIndex].value; // 작성 월
  let diaryDate = Dates.options[Dates.selectedIndex].value; // 작성 일
  let content = diaryContent.value; // 일기장 내용

  let temp_html = `<div class="card">
                    <div class="card-header">
                      <h5 class="card-header-title">제목 : ${title}</h5>
                      <h5 class="card-header-title">날짜 : ${diaryYear}-${diaryMonth}-${diaryDate}</h5>
                    </div>
                    <div class="card-body au">
                      <p class="card-text">
                        ${content}
                      </p>
                    </div>
                  </div>`;

  $(".diary_lists_1").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary_personal);
