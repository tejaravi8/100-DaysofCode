let send = document.getElementById("small")

function BoxArea(color) {
    // create a box
    let box = document.createElement("div")
    box.style.height = "100px"
    box.style.width = "100px"
    box.style.backgroundColor = color
    box.style.display = "inline-block"
    box.style.margin = "10px"
    box.style.position = "relative"

    // create a close (x) button
    let bt = document.createElement("button")
    bt.innerText = "x"
    bt.style.position = "absolute"
    bt.style.top = "5px"
    bt.style.right = "5px"
    bt.style.cursor = "pointer"

    // when button clicked → remove that particular box
    bt.addEventListener("click", function() {
        box.remove()
    })

    // add button inside box and box inside main container
    box.appendChild(bt)
    send.appendChild(box)
}

function Clearall() {
    send.innerHTML = ""  // ✅ clears all boxes, keeps container
}
