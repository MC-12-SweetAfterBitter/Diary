const uploadButton = document.querySelector(
  ".upload_button .btn .btn-outline-secondary"
); // 업로드 버튼 가져오기
const diaryTitle = document.querySelector(".title input"); // 일기장 제목

function uploadDiary(event) {
  let title = diaryTitle.value;

  let temp_html = `<div class="card">
  <div class="card-header">
    <h5>${title}</h5>
    <h5>2022-03-25</h5>
  </div>
  <div class="card-body">
    <p class="card-text">
      오늘은 ~~ 했다. ~ 를 먹었고, ~와 함께 ~에 놀러갔다! 재밌었다.
    </p>
  </div>
</div>`;

  $(".diary_lists").append(temp_html);
}

uploadButton.addEventListener("click", uploadDiary);
/*
  const diaryInput = document.querySelector(".diary_content");
*/

/*
  event.preventDefault();
  const uploadedDiary = diaryInput.value;
  const uploadedTitle = diaryTitle.value;
  diaryInput.value = "";
  console.log(`${uploadedDiary}`);
  */
