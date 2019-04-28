url = "https://koreanjson.com/posts/1"

const getData = async function(){
    const response = await fetch(url);
    const data = await response.json();

    console.log(response);
    console.log(data);

    return "getData Return Value"
}

getData();