const csrftoken = Cookies.get('csrftoken');

function initializeDataTable() {
    var table = $("#templates-table").DataTable({
        ajax: {
            url: "/api/templates",  // Replace with your API endpoint
            dataSrc: ""  // Since the data is directly an array
        },
        paging: true,
        lengthChange: true,
        searching: true,
        ordering: true,
        info: true,
        // dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'pdf'
        ],
        "columnDefs": [
            {
                "targets": -1,
                "data": null,
                "defaultContent": '<button class="btn btn-primary btn-sm edit-button">Edit</button>'
            }
        ],
        autoWidth: false,
        responsive: true,
        columns: [
            { data: "id" },
            { data: "name" },
            { data: "slug" },
            { data: "type" },
            { data: "created" },
            { data: "modified" },
            {
                data: null,
                className: "dt-center .edit-button",
                defaultContent: `
                <div>
                    <a class="nav-link  text-dark pr-0 pb-0" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="fa fa-ellipsis-v"></i>
                    </a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                        <a  class="dropdown-item manage" href=""> <i class="fa fa-edit mr-2"></i> Manage Template</a>
                        <a class="dropdown-item" href="#"> <i class="fa fa-trash mr-2"></i> Delete Template</a>
                        <a class="dropdown-item" href="#"> <i class="fa fa-copy mr-2"></i> Duplicate Template</a>
                    </div>
                </div>`,
                orderable: false
            },
        ]
    });

    // Add event listener for manage template button use the slug for the url
    // table.on('click', '.manage', function () {
    //     var data = table.row($(this).parents('tr')).data();
    //     window.location.href = `${data.type}.${data.name}.${window.location.hostname}:${window.location.port}`;
    // });

    // Add event listener for manage template button, using the slug for the URL
    table.on('click', '.manage', function (event) {
        event.preventDefault();  // Prevent the default anchor behavior
        var data = table.row($(this).parents('tr')).data();

        // Construct the URL and redirect
        var redirectUrl = `http://${data.slug}.${window.location.hostname}:${window.location.port}`;  // Adjust the URL path to your desired format
        // window.location.href = redirectUrl;

        // Open the URL in a new tab
        window.open(redirectUrl, '_blank');
    });


}

$(document).ready(function () {
    // Initialize DataTable
    initializeDataTable();
});

// trigger an event when name input is changed
$('#name').on('input', function () {
    $('#slug').val($(this).val().toLowerCase().replace(/[^a-z0-9]+/g, "-")
        .replace(/^-|-$/g, ""))
});

// create a function for creating a post request to /templates/create/
function createTemplate(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/admin/templates/create/',
        headers: {
            "X-CSRFToken": csrftoken
        },
        data: {
            name: $('#name').val(),
            slug: $('#slug').val(),
            description: $('#description').val()
        },
        // while request is being processed, display bootstrap spinner on top of the modal
        beforeSend: function () {
            $('#createTemplateModal').modal('hide');
            $('#loadingModal').modal('show');
        },
        success: function (response) {
            console.log(response);
            // if status is success display sweetalert and close modal
            $('#createTemplateModal').modal('hide');
            $('#loadingModal').modal('hide');
            $('#name').val('');
            $('#slug').val('');
            $('#description').val('');

            if (response.status === 'success') {
                Swal.fire({
                    icon: 'success',
                    title: 'Template Created Successfully',
                    showConfirmButton: false,
                    timer: 1500
                });

                // rerender table
                $('#templates-table').DataTable().ajax.reload();

                // close modal
            }
        },
        error: function (xhr, status, error) {
            console.log(error);
            //add error message on the modal
            $('#createTemplateModal .modal-body').append(error);
            $('#loadingModal').modal('hide');
            $('#createTemplateModal').modal('show');
        }
    });
}



// $(document).ready(function () {
//     $('#tenant-table').DataTable({
//         "columnDefs": [
//             {
//                 "targets": -1,
//                 "data": null,
//                 "defaultContent": '<button class="btn btn-primary btn-sm edit-button">Edit</button>'
//             }
//         ]
//     });
// });