url = "https://koreanjson.com/posts/1"

const getData = async function(){
    const response = await fetch(url);
    console.log(response);
    const data = response.json();
    console.log(data);
    return "Return Value of getData"
}

console.log(getData());