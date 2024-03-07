

//----------------------settings--------------------------




let setting = document.getElementById("setting")
let dropdownMenu = document.getElementsByClassName("dropdown-menu")[0]

setting.addEventListener('click', settingdropdown);
window.addEventListener('click', settingclose)



function settingdropdown(){
	dropdownMenu.style.display = 'block';
}

function settingclose(e){
	if (e.target == dropdownMenu){
		dropdownMenu.style.display = 'none';
	}
	
}




// -------------------cards modal--------------------------

let cards = document.getElementById('all-cards')


cards.addEventListener('click', cardOption)

function cardOption(e){
	let clickedItem = e.target.closest('.menuBtn');
	if (clickedItem){
		let clickedItemId = clickedItem.id;
		alert('hello' + clickedItemId)
	}
}

let cardsContainer = document.getElementById('all-cards');

cardsContainer.addEventListener('click', cardOption);
// window.addEventListener('click', closeModalWindow);


function cardOption(e) {
  let clickedItem = e.target;
  if (clickedItem.classList.contains('menuBtn')) {
    let menuModal = clickedItem.parentElement.querySelector('.modal')
    menuModal.style.display = 'block';
  }

	if (clickedItem.classList.contains('closeBtn')) {
	  let modal = clickedItem.closest('.modal');
    modal.style.display = 'none';	  }

    
	}

// ----------------------dark mode-----------------------------






