const canvas = document.querySelector("canvas")
const ctx = canvas.getContext("2d");

const colorBtns = document.querySelectorAll(".pallet button");
const eraserBtn = document.querySelectorAll("#eraser");
const downloadBtn = document.querySelector("#download");

//그리기 설정
let isDrawing = false;
let isErasing = false;

//초기 설정
ctx.livewidth = 5;
ctx.strokeStype = "red";

//이벤트 리스너
function startDrawing(e){
    isDrawing = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetx,e.offsetY);
}

function drawing(e){
    if (!isDrawing) return;
    if (isErasing){
        //지우개
        ctx.clearRect(e.offsetX,e.offsetY, 20, 20)
    }
    else{
       ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
    }
}

function stopDrawing(){
    isDrawing = false;
    ctx.closePath();
}

function startErasing(e){
    isErasing =true;
    colorBtns.forEach(button => button.classList.remove("selected"));
    e.currentTarget.classList.add("selected");
}

function downloadCanvas(){
    const image = canvas.toDataURL("image/jpg", 1.0);
    const linkEl = document.createElement('a');
    linkEl.href = image;
    linkEl.download = 'PaintApp';
    linkEl.click();
}

function changeColor(e){
    isErasing = false;
    ctx.strokeStyle = e.currentTarget.dataset.color;

    colorBtns.forEach(button => {
        if(button === e.currentTarget){
        button.classList.add("selected");
        } else{
        button.classList.remove("selected");
    }
    })
eraserBtn.classList.remove("selected");
}


//이벤트 연결
canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("mousemove", drawing);
canvas.addEventListener("mouseup", stopDrawing);
colorBtns.forEach(button => button.addEventListener("click", changeColor));
eraserBtn.forEach(button => button.addEventListener("click", startErasing));
downloadBtn.addEventListener("click", downloadCanvas);