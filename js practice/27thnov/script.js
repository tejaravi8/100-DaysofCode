// ⭐ 1. Dark Mode Using localStorage
let themeBtn=document.getElementById("themeBtn")

if (localStorage.getItem("theme")==="dark"){
    document.body.classList.add("dark")
}

themeBtn.addEventListener("click",()=>{
    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.removeItem("theme");
    }
    // localStorage.removeItem("theme")
})

// let themeBtn = document.getElementById("themeBtn");

// // Apply saved theme on page load
// if (localStorage.getItem("theme") === "dark") {
//     document.body.classList.add("dark");
//     //document.body.setAttribute("class","dark")
// }

// // Toggle
// themeBtn.addEventListener("click", () => {
//     document.body.classList.toggle("dark");

//     if (document.body.classList.contains("dark")) {
//         localStorage.setItem("theme", "dark");
//     } else {
//         localStorage.removeItem("theme");
//     }
// });



// 2. OTP Verification Using sessionStorage

// let otpBtn = document.getElementById("otpBtn");
// let checkOtpBtn = document.getElementById("checkOtpBtn");

// otpBtn.addEventListener("click", () => {
//     let otp = document.getElementById("otpInput").value;
//     sessionStorage.setItem("otp", otp);
//     alert("OTP saved (sessionStorage)");
// });

// checkOtpBtn.addEventListener("click", () => {
//     let savedOtp = sessionStorage.getItem("otp");
//     let currentOtp = document.getElementById("otpInput").value;

//     if (savedOtp && savedOtp === currentOtp) {
//         alert("OTP Verified!");
//         sessionStorage.removeItem("otp");
//     } else {
//         alert("Wrong OTP");
//     }
// });

// // ⭐ 3. Login Token Using Cookies

// function setCookie(name, value, days) {
//     let date = new Date();
//     date.setTime(date.getTime() + (days*24*60*60*1000));
//     document.cookie = `${name}=${value}; expires=${date.toUTCString()}; path=/`;
// }

// function getCookie(name) {
//     let cookies = document.cookie.split("; ");
//     for (let c of cookies) {
//         let [key, value] = c.split("=");
//         if (key === name) return value;
//     }
//     return null;
// }

// let loginBtn = document.getElementById("loginBtn");
// let logoutBtn = document.getElementById("logoutBtn");
// let loginStatus = document.getElementById("loginStatus");

// // Update UI on load
// function updateStatus() {
//     let token = getCookie("token");
//     loginStatus.innerHTML = token ? "Logged In ✅" : "Logged Out ❌";
// }
// updateStatus();

// loginBtn.addEventListener("click", () => {
//     setCookie("token", "abc123xyz", 1); // 1 day
//     updateStatus();
// });

// logoutBtn.addEventListener("click", () => {
//     setCookie("token", "", -1); // delete cookie
//     updateStatus();
// });
