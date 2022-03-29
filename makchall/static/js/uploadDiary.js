const uploadButton = document.querySelector(".upload_button"); // 업로드 버튼 가져오기
const diaryTitle = document.querySelector(".title input"); // 일기장 제목
const Year = document.querySelector("#year"); // 연도
const Month = document.querySelector("#month"); // 월
const Dates = document.querySelector("#date"); // 일
const diaryContent = document.querySelector("#floatingTextarea2"); // 일기장 내용

function uploadDiary(event) {
  event.preventDefault();
  let title = diaryTitle.value; // 일기장 제목
  let diaryYear = Year.options[Year.selectedIndex].value; // 작성 연도
  let diaryMonth = Month.options[Month.selectedIndex].value; // 작성 월
  let diaryDate = Dates.options[Dates.selectedIndex].value; // 작성 일
  let content = diaryContent.value; // 일기장 내용

  let temp_html = `<div class="card">
                    <div class="card-header">
                      <h5>${title}</h5>
                      <h5>${diaryYear}-${diaryMonth}-${diaryDate}</h5>
                    </div>
                    <div class="card-body">
                      <p class="card-text">
                        ${content}
                      </p>
                    </div>
                  </div>`;

  $(".diary_lists").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary);