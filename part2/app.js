const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')

function toggleSidebar(){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
}

const menuList = document.getElementById('menu-list')
menuList.style.maxHeight = '0px'

function toggleMenu(){
    if (menuList.style.maxHeight == '0px'){
        menuList.style.maxHeight = '300px';
        menuList.style.display = 'flex';
    } else {
        menuList.style.maxHeight = '0px'
    }
}

function adjustPageScale() {
    const mainDiv = document.querySelector('body');
    const screenWidth = window.innerWidth;

    if (screenWidth >= 992 && screenWidth <= 1600) {
        mainDiv.style.transform = 'scale(0.9)';
        mainDiv.style.transformOrigin = 'top center';
    } else if (screenWidth >= 700 && screenWidth <= 767) {
        mainDiv.style.transform = 'scale(0.8)';
        mainDiv.style.transformOrigin = 'top center';
    } else if (screenWidth >= 600 && screenWidth < 700) {
        mainDiv.style.transform = 'scale(0.75)';
        mainDiv.style.transformOrigin = 'top center';
    } else if (screenWidth <= 600) {
        mainDiv.style.transform = 'scale(0.5)';
        mainDiv.style.transformOrigin = 'top center';
    } else {
        mainDiv.style.transform = 'scale(1)';
    }
}

window.addEventListener('resize', adjustPageScale);
window.addEventListener('load', adjustPageScale);
