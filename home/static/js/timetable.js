
const scheduleList = document.querySelectorAll('.schedule-items');
const timetableSection = document.querySelector('.timetable-wrp');
const dayButtons = document.querySelectorAll('.day-button');
const scheduleItems = document.querySelector('.schedule-items');
const timetableUpButton = document.querySelector('.schedule-scroll-up');
const timetableDownButton = document.querySelector('.schedule-scroll-down');
const timetableDays = document.querySelector('.timetable-days');
const scheduleBtn = document.querySelector('.schedule-btn');
const scheduleTime = document.querySelectorAll('.schedule-time');

timetableUpButton.addEventListener('click', function (e) {
    const activeItem = document.querySelector('.schedule-items.active');
    activeItem.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    })
});

timetableDownButton.addEventListener('click', function () {
    const activeItem = document.querySelector('.schedule-items.active');
    activeItem.scrollTo({
        top: 500,
        left: 0,
        behavior: 'smooth'
    })
});

timetableSection.addEventListener('click', function (e) {
    const id = e.target.dataset.id;

    if (id) {
        e.target.classList.add("active");
        dayButtons.forEach(item => {
            item.classList.remove("active");
        })
        e.target.classList.add("active");
        scheduleList.forEach(item => {
            item.classList.remove("active");
        });
        const element = document.getElementById(id);
        element.classList.add("active");
    }

});


const mediaQuery = window.matchMedia('(max-width: 430px)');

mediaQuery.onchange = (e) => {
    if (e.matches) {
        timetableSection.classList.remove('center-block');
        timetableDays.classList.remove('center-block');
        scheduleBtn.classList.add('center-block');
    } else {
        timetableSection.classList.add('center-block');
        timetableDays.classList.add('center-block');
    }
}