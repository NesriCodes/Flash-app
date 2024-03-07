var clickFront = document.getElementsByClassName("click-front")[1]
var clickBack = document.getElementsByClassName("click-back")[0]

var front = document.getElementById("front")
var back = document.getElementById("back")



clickFront.addEventListener('click', frontCard);
clickBack.addEventListener('click', backCard);

function backCard() {
	front.style.display = 'none';
	back.style.display = 'block';
}

function frontCard() {
	back.style.display = 'none';
	front.style.display = 'block';
}