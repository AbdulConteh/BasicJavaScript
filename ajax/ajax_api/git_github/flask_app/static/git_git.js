console.log("ello govena")

async function getGitData() {
    var response = await fetch("https://api.github.com/users/adion81");
    var gitData = await response.json();
    return gitData;
}
console.log(getGitData());