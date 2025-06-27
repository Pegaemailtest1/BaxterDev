const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");
const folderInput = document.getElementById("folderInput");
const browseFiles = document.getElementById("browseFiles");
const browseFolders = document.getElementById("browseFolders");
const fileList = document.getElementById("file-list");
const uploadBtn = document.getElementById("uploadBtn");
const notification = document.getElementById("notification");
 
let filesToUpload = [];
 
browseFiles.addEventListener("click", () => fileInput.click());
browseFolders.addEventListener("click", () => folderInput.click());
 
fileInput.addEventListener("change", handleFiles);
folderInput.addEventListener("change", handleFiles);
 
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("dragging");
});
 
dropArea.addEventListener("dragleave", () => dropArea.classList.remove("dragging"));
 
dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("dragging");
  handleDropItems(e.dataTransfer.items);
});
 
 
function handleDropItems(items) {
  const traverseFileTree = (item, path = "") => {
    return new Promise((resolve) => {
      if (item.isFile) {
        item.file(file => {
          file.fullPath = path + file.name;
          resolve([file]);
        });
      } else if (item.isDirectory) {
        const dirReader = item.createReader();
        dirReader.readEntries(entries => {
          Promise.all(entries.map(entry => traverseFileTree(entry, path + item.name + "/"))).then(filesArrays => {
            resolve(filesArrays.flat());
          });
        });
      }
    });
  };
 
  const promises = [];
  for (let i = 0; i < items.length; i++) {
    const item = items[i].webkitGetAsEntry();
    if (item) {
      promises.push(traverseFileTree(item));
    }
  }
 
  Promise.all(promises).then(filesArrays => {
    const allFiles = filesArrays.flat();
    allFiles.forEach(file => {
      addFile(file);
    });
    updateUploadButton();
  });
}
 
function handleFiles(e) {
  const selectedFiles = Array.from(e.target.files);
  selectedFiles.forEach(file => {
    addFile(file);
  });
  updateUploadButton();
 
  e.target.value = "";
}
 
function addFile(file) {
 
  if (filesToUpload.some(f => f.name === file.name && f.size === file.size)) {
    return;
  }
  filesToUpload.push(file);
 
  const listItem = document.createElement("div");
  listItem.className = "file-item";
 
  const fileName = document.createElement("span");
  fileName.textContent = file.fullPath || file.webkitRelativePath || file.name;
 
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "×";
  removeBtn.className = "remove-file-btn";
  removeBtn.title = "Remove file";
  removeBtn.onclick = () => {
    fileList.removeChild(listItem);
    filesToUpload = filesToUpload.filter(f => f !== file);
    updateUploadButton();
  };
 
  listItem.appendChild(fileName);
  listItem.appendChild(removeBtn);
  fileList.appendChild(listItem);
}
 
function updateUploadButton() {
  if (filesToUpload.length > 0) {
    uploadBtn.disabled = false;
    uploadBtn.classList.add("active");
    uploadBtn.textContent = "Upload";
  } else {
    uploadBtn.disabled = true;
    uploadBtn.classList.remove("active");
    uploadBtn.textContent = "Upload";
  }
}
 
uploadBtn.addEventListener("click", () => {
  if (uploadBtn.disabled) return;
 
  uploadBtn.disabled = true;
  uploadBtn.textContent = "Uploading...";
  uploadBtn.style.backgroundColor = "#ffc107";
  uploadBtn.style.cursor = "wait";
 
  const formData = new FormData();
  filesToUpload.forEach(file => {
    formData.append("files", file, file.fullPath || file.webkitRelativePath || file.name);
  });
 
  fetch("/upload", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    notification.textContent = data.message || "Upload successful!";
    fileList.innerHTML = "";
    filesToUpload = [];
    uploadBtn.disabled = true;
    uploadBtn.classList.remove("active");
    uploadBtn.textContent = "Uploaded";
    uploadBtn.style.backgroundColor = "#28a745";
    uploadBtn.style.cursor = "default";
 
   
    setTimeout(() => {
      updateUploadButton();
      uploadBtn.style.backgroundColor = "";
      uploadBtn.style.cursor = "";
    }, 3000);
  })
  .catch(err => {
    console.error(err);
    notification.textContent = "Upload failed. Please try again.";
    uploadBtn.disabled = false;
    uploadBtn.classList.add("active");
    uploadBtn.textContent = "Upload";
    uploadBtn.style.backgroundColor = "#28a745";
    uploadBtn.style.cursor = "pointer";
  });
});