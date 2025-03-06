document.addEventListener("DOMContentLoaded", function () {
    // Load dữ liệu đã chọn trước đó
    let department = localStorage.getItem("selectedDepartment");
    if (department && document.getElementById("selected-department")) {
        document.getElementById("selected-department").innerText = department;
    }

    let selectedTime = localStorage.getItem("selectedTime");
    if (selectedTime && document.getElementById("selected-time")) {
        document.getElementById("selected-time").innerText = selectedTime;
    }

    // Chọn phòng chức năng
    window.selectDepartment = function (departmentName) {
        document.getElementById("selected-department").innerText = departmentName;
        localStorage.setItem("selectedDepartment", departmentName);
        window.location.href = "BenhNhanChonBacSi.html";
    };

    // Hiển thị Datepicker khi bấm vào nút chọn ngày
    $("#selectDateBtn").click(function () {
        $("#datePickerContainer").toggle();
    });

    // Khởi tạo Datepicker
    $('#datepicker').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true,
        todayHighlight: true
    }).on('changeDate', function (e) {
        let selectedDate = e.format();
        document.getElementById("selected-time").innerText = selectedDate;
        localStorage.setItem("selectedTime", selectedDate);
        $("#datePickerContainer").hide();
    });
});

function chonBacSi(tenBacSi) {
    localStorage.setItem("selectedDoctor", tenBacSi);
}

document.addEventListener("DOMContentLoaded", function () {
    let bacSi = localStorage.getItem("selectedDoctor");
    if (bacSi) {
        document.getElementById("selected-doctor").innerText = "Bác sĩ: " + bacSi;
    }
});

//nút Lên lịch
