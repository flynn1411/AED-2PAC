/**********Node************/
function Node(value){
    this.value = value;
    this.next = null;
}

/***********Stack**********/
function Stack(){
    this.first = null;

    this.push = StackPush;
    this.pop = StackPop;
    this.printFirst = StackPrintFirst;
}

function StackPush(value){
    newNode = new Node(value);

    if(!this.first){
        this.first = newNode;
        return true;
    }
    else{
        newNode.next = this.first;
        this.first = newNode;
        return true;
    }
    return false;
}

function StackPop(){
    popped = null;
    if(!this.first){
        console.log("La pila esta vacia.")
    }
    else{
        popped = this.first;
        this.first = this.first.next;

        console.log(popped.value);
    }
}

function StackPrintFirst(){
    console.log(this.first.value);
}