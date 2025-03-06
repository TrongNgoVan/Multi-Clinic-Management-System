document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:5000/get_all_bacsi")  // Thay đổi nếu server chạy trên cổng khác
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("bacsi-table-body");
            tableBody.innerHTML = "";  // Xóa nội dung cũ trước khi thêm mới

            data.forEach(bacsi => {
                let row = `
                    <tr>
                        <td>${bacsi.ID}</td>
                        <td>${bacsi.ten}</td>
                        <td>${bacsi.dob}</td>
                        <td>${bacsi.chuyenmon}</td>
                        <td>${bacsi.hocvan}</td>
                        <td>${bacsi.kinhnghiem}</td>
                        <td><img src="${bacsi.img}" alt="Ảnh bác sĩ" width="50"></td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Lỗi khi lấy dữ liệu bác sĩ:", error));
});
