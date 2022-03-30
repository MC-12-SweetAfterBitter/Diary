const uploadButton = document.querySelector(".upload_button"); // 업로드 버튼 가져오기
const diaryTitle = document.querySelector(".title input"); // 일기장 제목
const diaryContent = document.querySelector("#floatingTextarea2"); // 일기장 내용

function uploadDiary(event) {
  event.preventDefault();
  let title = diaryTitle.value; // 일기장 제목
  let content = diaryContent.value; // 일기장 내용

  let temp_html = `<div class="card">
                    <div class="card-header">
                      <h5>${title}</h5>
                      <!-- 공감버튼리스트-->
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

  $(".diary_lists").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary);