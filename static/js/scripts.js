// sidebar toggle
let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");

btn.onclick = function(){
    sidebar.classList.toggle("active");
};


// sticky sidebar
const side_bar = document.querySelector('.sidebar');
const sidebarTop = sidebar.offsetTop;

window.addEventListener('scroll', () => {
if (window.pageYOffset >= sidebarTop) {
    side_bar.style.position = 'fixed';
    side_bar.style.top = 0;
} else {
    side_bar.style.position = 'relative';
}
});


// sticky top bar
const top_bar = document.querySelector('.top_bar');
const topbarTop = top_bar.offsetTop;

window.addEventListener('scroll', () => {
if (window.pageYOffset >= topbarTop) {
    top_bar.style.position = 'fixed';
    top_bar.style.top = 0;
} else {
    top_bar.style.position = 'sticky';
    top_bar.style.top = null;
}
});



const selectBtns = document.querySelectorAll('.select-btn');

selectBtns.forEach(selectBtn => {
selectBtn.addEventListener('click', () => {
    selectBtn.classList.toggle('open');
});

const items = selectBtn.parentNode.querySelector('.list-items').querySelectorAll('.item');

items.forEach(item => {
    item.addEventListener('click', () => {
    item.classList.toggle('checked');

    let checked = selectBtn.parentNode.querySelector('.list-items').querySelectorAll('.checked'),
        btnText = selectBtn.querySelector('.btn-text');

    if (checked && checked.length > 0) {
        btnText.innerText = `${checked.length} Selected`;
    } else {
        btnText.innerText = 'Select Language';
    }
    });
});
});