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