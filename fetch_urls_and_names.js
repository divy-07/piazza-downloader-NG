let file_links = [];
let file_names = [];

results = document.querySelectorAll('a[id^="resourceLink"]:not([href="#"])')

results.forEach(function(element) {
    file_links.push(element.href);
    file_names.push(element.text);
});

file_links_output = file_links.join("\n");
file_names_output = file_names.join("\n");

console.log(file_links_output);
console.log(file_names_output);
