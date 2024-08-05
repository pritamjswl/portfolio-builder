// Function to open and close sidenav
function open_sidenav() {
    document.querySelector('#sideNav').style.left = '0';
    document.querySelector('#overlay').style.display = 'block';
}
function close_sidenav() {
    document.querySelector('#sideNav').style.left = '-100%';
    document.querySelector('#overlay').style.display = 'none';
}