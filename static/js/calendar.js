document.addEventListener("DOMContentLoaded", function () {
  const calendarBody = document.querySelector(".calendar-body");
  const currentMonthYear = document.getElementById("current-month-year");
  const prevMonthButton = document.getElementById("prev-month");
  const nextMonthButton = document.getElementById("next-month");

  function generateCalendar(year, month) {
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();

    let calendarHTML =
      "<table><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>";
    calendarHTML += "<tr>";

    let day = 1;

    for (let i = 0; i < firstDay.getDay(); i++) {
      calendarHTML += "<td></td>";
    }

    for (let i = firstDay.getDay(); day <= daysInMonth; i++) {
      calendarHTML += `<td>${day}</td>`;
      if (i % 7 === 6) {
        calendarHTML += "</tr><tr>";
      }
      day++;
    }

    for (let i = lastDay.getDay(); i < 6; i++) {
      calendarHTML += "<td></td>";
    }

    calendarHTML += "</tr></table>";
    calendarBody.innerHTML = calendarHTML;
  }

  function updateCalendar() {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();

    generateCalendar(currentYear, currentMonth);

    const monthNames = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    currentMonthYear.textContent = `${monthNames[currentMonth]} ${currentYear}`;
  }

  updateCalendar();

  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  prevMonthButton.addEventListener("click", function () {
    const [currentMonth, currentYear] =
      currentMonthYear.textContent.split(" ");
    const monthIndex = monthNames.indexOf(currentMonth);
    const newMonthIndex = (monthIndex - 1 + 12) % 12;
    const newYear =
      newMonthIndex === 11 ? parseInt(currentYear) - 1 : currentYear;

    generateCalendar(newYear, newMonthIndex);
    currentMonthYear.textContent = `${monthNames[newMonthIndex]} ${newYear}`;
  });

  // Add a click event listener to all date cells
  document.querySelectorAll(".calendar-body td").forEach((cell) => {
    cell.addEventListener("click", function () {
      // Get the date from the cell
      const date = cell.textContent;

      // Convert the date string to a Date object, specifying the locale
      const dateObject = new Date(Date.parse(date, "en-US"));

      // Redirect to the desired page
      window.location.href = `/tasks/${dateObject.getFullYear()}-${dateObject.getMonth() + 1
        }-${dateObject.getDate()}`;
    });
  });

  nextMonthButton.addEventListener("click", function () {
    const [currentMonth, currentYear] =
      currentMonthYear.textContent.split(" ");
    const monthIndex = monthNames.indexOf(currentMonth);
    const newMonthIndex = (monthIndex + 1) % 12;
    const newYear =
      newMonthIndex === 0 ? parseInt(currentYear) + 1 : currentYear;

    generateCalendar(newYear, newMonthIndex);
    currentMonthYear.textContent = `${monthNames[newMonthIndex]} ${newYear}`;
  });
});