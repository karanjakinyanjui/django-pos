clear();
var count = 1;

fields = Array.from(document.querySelectorAll("form .form-group"), (i) => {
  try {
    const labelField = i.querySelector("label");
    const label = labelField.textContent;
    const input = i.querySelector("[name]");
    const type = input.type;
    const name = input.name;
    const placeholder = input.placeholder || `Enter ${input.name}`;
    return { name, label, type, placeholder };
  } catch (error) {
    console.log(`${i.textContent}${error}`);
  }
}).filter((i) => !!i);

types = new Set();

populate = ({ name, label, type, placeholder }) => {
  const is_textarea = type === "textarea";
  const inputTag = is_textarea ? "textarea" : "input";

  const is_Check = ["checkbox", "radio"].includes(type);

  const dontfloat = ["checkbox", "radio", "file"].includes(type);

  const fieldClass = is_Check ? "form-check-input" : "form-control";

  const divClass = dontfloat ? "mb-3" : "form-floating mb-3";

  const wrapper = `<div class="${divClass}">`;
  const label_ = `<label for="${name}" class="form-label">${label}</label>`;
  const input = `<${inputTag} type="${type}" class="${fieldClass}" id="${name}" placeholder="${placeholder}"></${inputTag}>`;
  if (type === "file") {
    return [wrapper, label_, input, "</div>"].join("\n");
  }
  return [wrapper, input, label_, "</div>"].join("\n");
};

str = "<div>";

for (const field of fields) {
  if (field.name.includes("[]")) {
    field.name = `${field.name.replace("[]", "")}_${count}`;
    count++;
  } else {
    count = 0;
  }
  str += populate(field) + "\n";
}
str += "</div>";

console.log(str);


