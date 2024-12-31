var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(tabname){
    for(lien of tablinks)
        lien.classList.remove("active-link")
    for(contenu of tabcontents){
        contenu.classList.remove('active-tab')
    }
    event.currentTarget.classList.add("active-link")
    document.getElementById(tabname).classList.add('active-tab')
}

var sidemenu = document.getElementById("sidemenu");

function openmenu(){
    sidemenu.style.right = "0";
}
function closemenu(){
    sidemenu.style.right = "-200px"
}
