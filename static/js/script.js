const nav = document.querySelector(".nav");
const searchIcon = document.querySelector("#searchIcon");
const navOpenBtn = document.querySelector(".navOpenBtn");
const navCloseBtn = document.querySelector(".navCloseBtn");

searchIcon.addEventListener("click", () => {
  nav.classList.toggle("openSearch");
  nav.classList.remove("openNav");
  if (nav.classList.contains("openSearch")) {
    // Arama açıkken diğer menü öğelerini gizle
    document.querySelector(".nav-link").style.display = "none";
    return searchIcon.classList.replace("uil-search", "uil-times");
  } else {
    // Arama kapatıldığında diğer menü öğelerini tekrar göster
    document.querySelector(".nav-link").style.display = "flex";
    searchIcon.classList.replace("uil-times", "uil-search");
  }
});

navOpenBtn.addEventListener("click", () => {
  nav.classList.add("openNav");
  nav.classList.remove("openSearch");
  searchIcon.classList.replace("uil-times", "uil-search");
});

navCloseBtn.addEventListener("click", () => {
  nav.classList.remove("openNav");
  document.querySelector(".nav-link").style.display = "flex"; // Menüyü kapatırken diğer öğeleri tekrar göster
});


var modal = document.getElementById("myModal");
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];

img.onclick = function() {
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

span.onclick = function() {
  modal.style.display = "none";
}

// Document üzerine bir click event listener ekleyerek modal dışında bir yere tıklandığında modalı kapat
document.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}









