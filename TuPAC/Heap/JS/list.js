/*************************Nodo*************************/
function Node(value){
    this.value = value;
    this.next = null;
}

/***********************Lista*************************/
function LinkedList(){
    this.first = null;

    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
    this.getLength = LinkedListGetLength;
    this.atPosition = LinkedListAtPosition;
    this.getFirst = LinkedListGetFirst;
    this.getLast = LinkedListGetLast;
    this.addInPosition = LinkedListAddInPosition;
}

function LinkedListAdd(value){
    if(!this.first){
        this.first = new Node(value);
    }

    else{
        current = this.first;
        while(current.next){
            current = current.next;
        }

        current.next = new Node(value);
    }
}

function LinkedListGetLength(){
    current = this.first;
    length = 0;

    while(current.next){
        length++;
        current = current.next;
    }
    length++;

    return length;
}

function LinkedListAtPosition(position){
    currentNode = this.first;
    currentPosition = 0;
    
    if(position > this.getLength()){
        return null;
    }
    else{
        while(currentNode.next){
            if(currentPosition == position){
                return currentNode;
            }
            else{
                currentPosition++;
                currentNode = currentNode.next;
            }
        }
        if(currentPosition == position){
            return currentNode;
        }
    }

}

function LinkedListGetFirst(){
    return this.first;
}

function LinkedListGetLast(){
    current = this.first;

    while(current.next){
        current = current.next;
    }

    return current;
}

function LinkedListPrint(){
    trail = " ";

    current = this.first;

    while(current.next){
        trail = trail + current.value + " -> ";

        current = current.next;
    }

    trail = trail + current.value + " -> NULL";

    console.log(trail);
}

function LinkedListAddInPosition(value, n){
    count = 0;

    newNode = new Node(value);

    if (n == 0){
        queue = this.first;

        this.first = newNode;

        this.first.next = queue;
    }

    else if (n > 0){
        current = this.first;
        previous = null;

        while(current.next){
            previous = current;
            current = current.next;

            count ++;

            if(count == n){
                previous.next = newNode;
                newNode.next = current;

                return true;
            }

            return false;
        }
    }
}