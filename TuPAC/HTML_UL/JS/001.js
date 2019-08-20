function HTMLUl(){
    this.convert = HTMLUlConvert;
}

function HTMLUlConvert(array){
    let html = [];

    for(i in array){
        let element = array[i];

        if(typeof(element) != "object"){
            html.push(`<li>${element}</li>`);
        }
        else{
            html.push(`<li>${this.convert(element)}</li>`);
        }
    }

    return `<ul>${html.join("")}</ul>`;
}