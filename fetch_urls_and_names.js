file_links = [];
file_names = [];

results = document.querySelectorAll('a[data-pats="resources_link"]:not([href="#"])')

$.each(results, function(_index, element){
    current_element = $(element);
    file_links.push(current_element.prop("href"));
    file_names.push(current_element.text());
});

file_links_output = file_links.join("\n");
file_names_output = file_names.join("\n");

console.log(file_links_output);
console.log(file_names_output);
