/****************************Node***************************/
function Node(value){
    this.value = value;
    this.lefttChild = null;
    this.rightChild = null;
}

/**************************Tree*****************************/
function BinarySearchTree(){
    this.root = null;

    this.add = BinarySearchTreeAdd;
    this.print = BinarySearchTreePrint;
    this.delete = BinarySearchTreeDelete;
}

function BinarySearchTreeAdd(value, current = this.root){
    if(!this.root){
        this.root = new Node(value);
        return true;
    }
    else{
        if(current.value > value){
            if(!current.lefttChild){
                current.lefttChild = new Node(value);
                return true;
            }
            else{
                current = current.lefttChild;
                return this.add(value, current);
            }
        }
        else{
            if(!current.rightChild){
                current.rightChild = new Node(value);
                return true;
            }
            else{
                current = current.rightChild;
                return this.add(value, current);
            }
        }
    }
    return false;
}

function BinarySearchTreePrint(current = this.root){
    if(!this.root){
        console.log("El arbol está vacio.");
    }

    else{
        if(current.lefttChild || current.rightChild){
            console.group(current.value);
            if(current.lefttChild){
                this.print(current.lefttChild);
            }

            if(current.rightChild){
                this.print(current.rightChild);
            }
            console.groupEnd();
        }

        else{
            console.log(current.value);
        }
    }
}


function BinarySearchTreeDelete(removeValue, current = this.root){
    if(!this.root){
        return false;
    }

    else{
        if(this.root.value == removeValue){
            leftChildren = this.root.lefttChild;
            rightChildren = this.root.rightChild;

            this.root = null;

            if(rightChildren){
                this.add(rightChildren);
            }

            if(leftChildren){
                this.add(leftChildren);
            }

            return true;
        }
        
    }
}