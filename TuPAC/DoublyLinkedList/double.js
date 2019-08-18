 /***********************NODO*************************/
function Node(value){
    //Atributos
    this.value = value;
    this.next = null;
    this.previous = null;

    //Metodos
    this.addNext = NodeAddNext;
    this.addPrevious = NodeAddPrevious;
}

function NodeAddNext(node){
    this.next = node;
}

function NodeAddPrevious(node){
    this.previous = node;
}

/********************Lista************************/
function DoublyLinkedList(){
    //Punteros de comienzo y final de la lista
    this.header = null;
    this.footer = null;

    //Metodos de la lista
    this.addToStart = DoublyLinkedListAddToStart;
    this.add = DoublyLinkedListAdd;
    this.addToEnd = DoublyLinkedListAddToEnd;
    this.search = DoublyLinkedListSearch;
    this.runForwards = DoublyLinkedListRunForwards;
    this.runBackwards = DoublyLinkedListRunBackwards;
}

function DoublyLinkedListAdd(node, referenceNode = null){
    if(!this.header){
        this.header = node;
        this.footer = node;

        printMessage(node);
    }

    //Si se da un nodo de referencia, se agrega el nodo nuevo como el siguiente de este nodo de referencia
    else if(referenceNode){
        temporalNode = this.search(referenceNode);
        if (temporalNode){
            nextNode = temporalNode.next;
            node.addNext(nextNode);
            node.addPrevious(temporalNode);
            nextNode.addPrevious(node);
            temporalNode.addNext(node);

            printMessage(node);
        }

        else{
            this.addToEnd(node);
            console.log("El nodo " + referenceNode + " no fue encontrado en la lista. " + node.value + " fue agregado al final de la lista.")
        }

    }

    //Si no se da un nodo de referencia, se asume que el nodo se desea agregar al final de la lista
    else{
        this.addToEnd(node);
    }

}

function DoublyLinkedListAddToEnd(node){
    previousNode = this.footer;
    this.footer = node;
    previousNode.addNext(node);
    node.addPrevious(previousNode);

    printMessage(node);
}

function DoublyLinkedListAddToStart(node){
    nextNode = this.header;
    node.addNext(nextNode);
    nextNode.addPrevious(node);
    this.header = node;

    printMessage(node);
}

function DoublyLinkedListSearch(searchValue){
    nodeWasFound = false;
    temporalNode = this.header;
    foundNode = null;

    while(temporalNode){
        if(temporalNode.value == searchValue){
            nodeWasFound = true;
            foundNode = temporalNode;
            break;

        }

        else{
            temporalNode = temporalNode.next;
        }
    }

    if(nodeWasFound){
        return foundNode;
    }
            
    else{
        return null;
    }
}

function DoublyLinkedListRunForwards(){
    trail = "NULL <=> ";
    temporalNode = this.header;
    while(temporalNode.next){
        trail = trail + temporalNode.value + " <=> ";
        temporalNode = temporalNode.next;
    }
            
    trail = trail + temporalNode.value + " <=> NULL";
    console.log(trail);
}

function DoublyLinkedListRunBackwards(){
    trail = "NULL <=> ";
    temporalNode = this.footer;
    while(temporalNode.previous){
        trail = trail + temporalNode.value + " <=> ";
        temporalNode = temporalNode.previous;
    }
            
    trail = trail + temporalNode.value + " <=> NULL";
    console.log(trail);
}

function printMessage(node){
    console.log("El nodo " + node.value + " fue agregado exitosamente.");
}