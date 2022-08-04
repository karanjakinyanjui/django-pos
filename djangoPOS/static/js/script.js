let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e) => {
    let arrowParent = e.target.parentElement.parentElement; //selecting main parent of arrow
    arrowParent.classList.toggle("showMenu");
  });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", () => {
  sidebar.classList.toggle("navclose");
});

$("#myModal").on("show", function () {
  var tit = $(".confirm-delete").data("title");

  $("#myModal .modal-body p").html(
    "Desea eliminar al usuario " + "<b>" + tit + "</b>" + " ?"
  );
  var id = $(this).data("id"),
    removeBtn = $(this).find(".danger");
});

$(".confirm-delete").on("click", function (e) {
  e.preventDefault();

  var id = $(this).data("id");
  $("#myModal").data("id", id).modal("show");
});

$("#btnYes").click(function () {
  // handle deletion here
  var id = $("#myModal").data("id");
  $("[data-id=" + id + "]")
    .parents("tr")
    .remove();
  $("#myModal").modal("hide");
});
