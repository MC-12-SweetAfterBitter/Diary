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
                      <h5 class="card-header-title">작성자 : ${name} / 제목 : ${title}</h5>
                        <!--공감 버튼-->
                        <button type="button" class="btn btn-outline-danger">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart"
                                 viewBox="0 0 16 16">
                                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"></path>
                            </svg>
                        </button>
                    </div>
                    <div class="card-body">
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
                    <div class="card-body">
                      <p class="card-text">
                        ${content}
                      </p>
                    </div>
                  </div>`;

  $(".diary_lists_1").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary_personal);