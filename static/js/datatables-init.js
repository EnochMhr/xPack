// Initialize DataTable with server-side rendered data
$(document).ready(function() {
    $('#example').DataTable({
        lengthMenu: [5, 10, 25, 50, -1],
        // Using server-side rendered HTML, no need for columns definition
        dom: 'lBfrtip' // Add length menu (l), buttons (B), filter (f), processing display (r), table (t), info (i), and pagination (p)
    });
});