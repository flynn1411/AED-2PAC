function Node(value){
    this.value = value;

    this.left = null;
    this.right = null;
}

function BST(){
    //atributos
    this.root = null;

    //metodos
    this.add = BSTAdd;
    this.search = BSTSearch;
    this.print = BSTPrint;
    this.printGroup = BSTPrintGroup;
}

function BSTAdd(value, current = this.root){
    if(!this.root){
        this.root = new Node(value);
        return true;
    }
    else{
        if (current.value > value){
            if(!current.left){
                current.left = new Node(value);
                return true;
            }
            else{
                return this.add(value, current.left);
            }
        }
        else if(current.value < value){
            if(!current.right){
                current.right = new Node(value);
            }
            else{
                return this.add(value, current.right);
            }
        }
        return false;
    }
    return false;
}

function BSTSearch(value, current = this.root){
    if(current.value == value){
        return true;
    }
    else{
        if(current.value > value){
            if(current.left){
                return this.search(value, current.left);
            }
            else{
                return false;
            }
        }
        else{
            if(current.right){
                return this.search(value, current.right);
            }
            else{
                return false;
            }
        }
    }
}

function BSTPrint(current = this.root){
    if(current.left){
        this.print(current.left);
    }
    if(current){
        console.log(current.value);
    }

    if(current.right){
        this.print(current.right);
    }
}

function BSTPrintGroup(current = this.root){
    if(current.left || current.right){
        console.group(current.value);
        if(current.left){
            this.printGroup(current.left);
        }
        if(current.right){
            this.printGroup(current.right);
        }
        console.groupEnd();
    }
    else{
        console.log(current.value);
    }
}