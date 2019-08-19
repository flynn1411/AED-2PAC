function Heap(){
    this.build = HeapBuild;
    this.printHeap = HeapPrintHeap;
}

function HeapBuild(list = new LinkedList()){
    var n = list.getLength(),
        h = Math.ceil(Math.log2(n+1)),
        mi = Math.pow(2, h-1)-1,
        mf = mi * 2,
        w = mf + 1,
        matrix = [];

        for (i = 0; i < h; i++){
            var row = [];
            for(j = 0; j < w; j++){
                row.push("&nbsp;");
            }
            matrix.push(row);
        }

        //Primera Fila
        matrix[0][Math.floor(w/2)] = list.atPosition(0).value;
        
        //Ultima fila
        for(count = 0; count < w; count += 2){
            for(j = mi; j < n; j++){
                matrix[h-1][count] = list.atPosition(j).value;
            }
        }

        //filas intermedias
        for(i = 1; i < h-1; i++){
            for(count = (Math.pow(2,h-1-i))-1; count < w; count += (Math.pow(2,h-i)-1)){
                for(j=1; j < mi; j++){
                    matrix[i][count] = list.atPosition(j).value;
                }
            }
        }
        this.printHeap(matrix);
}

function HeapPrintHeap(array){
    html = "<table border ='1'>";
    for (i = 0; i<array.length; i++){
        html += "<tr>";
            
        for(j = 0; j<array[i].length; j++){
            if((array[i].length == 2)&&(j == 1)){
                html += `<td colspan = "2"> ${array[i][j]} </td>`;
            }
            else{
                html += `<td> ${array[i][j]} </td>`;
            }
        }
        html += "</tr>";
    }
    
    document.write(html);
}