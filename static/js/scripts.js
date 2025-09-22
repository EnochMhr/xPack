$(document).ready(function() {
    // Initialize sidebar toggle functionality
    const $hamburger = $(".toggle-btn");
    const $toggler = $("#icon");
    const $sidebar = $("#sidebar");

    if ($hamburger.length && $toggler.length && $sidebar.length) {
        $hamburger.on("click", function() {
            $sidebar.toggleClass("expand");
            $toggler.toggleClass("bx-chevrons-right bx-chevrons-left");
        });
    }
});