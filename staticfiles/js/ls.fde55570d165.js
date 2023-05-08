function copyToClipboard() {
    var shortUrl = document.getElementById("short-url");
    shortUrl.select();
    shortUrl.setSelectionRange(0, 99999);
    document.execCommand("copy");
}
