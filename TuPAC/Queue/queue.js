/***********Node***********/
function Node(value){
    this.value = value;
    this.next = null;
}

/***********Queue**********/
function Queue(){
    this.first = null;

    this.push = QueuePush;
    this.pop = QueuePop;
}

function QueuePush(value){
    if(!this.first){
        this.first = new Node(value);
    }

    else{
        current = this.first;
        while(current.next){
            current = current.next;
        }
        current.next = new Node(value)
    }
}

function QueuePop(){
    if(!this.first){
        console.log("La fila esta vacia.");
    }

    else{
        popped = this.first;
        this.first = this.first.next;

        console.log(popped.value);
    }
}

