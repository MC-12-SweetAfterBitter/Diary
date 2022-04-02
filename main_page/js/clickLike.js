const gongamBtn = document.querySelector(".gongamBtn");
const Like = document.querySelector(".fa-heart");

function handleGongamBtnClick() {
  if (Like.className === "fa-regular fa-heart fa-xl") {
    Like.className = "fa-solid fa-heart fa-xl";
  } else {
    Like.className = "fa-regular fa-heart fa-xl";
  }
}

gongamBtn.addEventListener("click", handleGongamBtnClick);
