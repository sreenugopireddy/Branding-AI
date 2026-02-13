async function call(url,data){
out.innerText = "Thinking..."
let r = await fetch(url,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})
let j = await r.json()
out.innerText = j.result
}

function brand(){
call("/api/brand",{idea:idea.value,tone:tone.value})
}

function content(){
call("/api/content",{desc:desc.value,tone:"professional"})
}

function colors(){
call("/api/colors",{industry:industry.value,tone:"modern"})
}

function chat(){
call("/api/chat",{msg:msg.value})
}

function copyOut(){
navigator.clipboard.writeText(out.innerText)
}
