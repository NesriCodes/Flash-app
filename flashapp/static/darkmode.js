let darkMode = localStorage.getItem('darkMode');

const enableDarkMode = () =>{
	document.body.classList.add('dark-theme');
	localStorage.setItem('darkMode', 'enabled');
}

const disableDarkMode = () =>{
	document.body.classList.remove('dark-theme');
	localStorage.setItem('darkMode', 'disabled');
}

if (darkMode === 'enabled'){
	enableDarkMode();
}

const darkModeToggle = document.querySelector(".dark-mode")

darkModeToggle.addEventListener('click', () => {
	darkMode = localStorage.getItem('darkMode');
	if (darkMode !== 'enabled'){
		enableDarkMode();
	} else{
		disableDarkMode();
	}
});

