const writing = document.querySelector(".writing_place"); // 다이어리 쓰는 부분
const writingButton = document.querySelector(".write_button_anchor button"); // 일기장 쓰기 버튼

function OpenWriting() {
  const clickedButton = "active";
  if (writing.classList.contains(clickedButton)) {
    writing.classList.remove(clickedButton);
    writingButton.innerText = "일기장 쓰기";
  } else {
    writing.classList.add(clickedButton);
    writingButton.innerText = "일기장 닫기";
  }
}

writingButton.addEventListener("click", OpenWriting);