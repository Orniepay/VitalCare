AOS.init({
    duration: 1000,
    offset: 100,
});

function showLogin() {
    document.getElementById('login-form').classList.add('active-form');
    document.getElementById('register-form').classList.remove('active-form');
    document.getElementById('login-btn').classList.add('active');
    document.getElementById('register-btn').classList.remove('active');
}

function showRegister() {
    document.getElementById('register-form').classList.add('active-form');
    document.getElementById('login-form').classList.remove('active-form');
    document.getElementById('register-btn').classList.add('active');
    document.getElementById('login-btn').classList.remove('active');
}
