document.addEventListener("DOMContentLoaded", function () {
    const nameSearch = document.getElementById("name-search");
    const tags = document.querySelectorAll(".tag");
    const projects = document.querySelectorAll(".project");

    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase();
        console.log('Search query:', nameQuery); // Debugging

        projects.forEach((project) => {
            const name = project.getAttribute('data-name') ? project.getAttribute('data-name').toLowerCase() : '';
            const projectTags = project.getAttribute('data-tags') ? project.getAttribute('data-tags').toLowerCase() : '';
            const nameMatch = name.includes(nameQuery);
            const tagMatch = projectTags.includes(nameQuery); // Check if the search query matches any tag

            // Display project if it matches the search query or if it's selected by tag
            if (nameMatch || tagMatch) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        });
    }

    tags.forEach((tag) => {
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute("data-tag") ? this.getAttribute("data-tag").toLowerCase() : '';
            console.log('Selected tag:', selectedTag); // Debugging

            projects.forEach((project) => {
                const projectTags = project.getAttribute("data-tags") ? project.getAttribute("data-tags").toLowerCase() : '';
                if (projectTags.includes(selectedTag)) {
                    project.style.display = "";
                } else {
                    project.style.display = "none";
                }
            });
        });
    });

    nameSearch.addEventListener("keyup", filterProjects);
});
