// custom.js
function startCountdown(seconds) {
    function updateCountdown() {
        if (seconds === 0) {
            window.location.href = page1Url; // 跳轉到 page1
        } else {
            document.getElementById("countdown").innerHTML = seconds + " 秒後跳轉...";
            seconds--;
            setTimeout(updateCountdown, 1000); // 每秒更新倒數並呼叫自身
        }
    }

    var page1Url = "page1.html"; // 設定 page1 的相對路徑
    updateCountdown();
}
window.onload = function () {
    startCountdown(3);  // 開始倒數計時，3 秒後跳轉
};