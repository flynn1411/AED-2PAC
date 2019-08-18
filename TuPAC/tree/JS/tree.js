/************************Nodo*************************/
function Node(value){
    this.value = value;
    this.next = null;

    this.children = new LinkedList();
}

/******************Lista Enlazada********************/
function LinkedList(){
    this.first = null;

    this._add = LinkedListAdd;
    this.isEmpty = LinkedListIsEmpty;
}

function LinkedListIsEmpty(){
    return this.first == null;
}

function LinkedListAdd(value, current = this.first){
    if(!this.first){
        this.first = new Node(value);
        return true;
    }
    else{
        if(current.next){
            current = current.next;
            this._add(value, current);
        }
        else{
            current.next = new Node(value);
            return true;
        }
    }
    return false;
}

/**********************Arbol***********************/
function Tree(){
    //atributos
    this.root = new Node("/");

    //metodos
    this.add = TreeAdd;
    this.search = TreeSearch;
    this.print = TreePrint;
}

function TreeAdd(value, parent = this.root){
    if((!this.search(parent)) && (parent != this.root)){
        console.log("El padre ", parent," no fue encontrado, el nodo ", value, " será agregado como hijo de la raíz." );
        parent = this.root;
        parent.children._add(value);
    }
    else if(parent == this.root){
        parent.children._add(value);
        console.log("El nodo ", value, " fue agregado con exito a la raíz.");
    }
    else{
        current = this.search(parent);
        current.children._add(value);
        console.log("El nodo ", value, " fue agregado exitosamente como hijo del nodo ", current.value, ".");
    }
}

function TreeSearch(value, current = this.root){
    if(current.next){
        if(current.value == value){
            return current;
        }else{
            if(current.children.first){
                if(this.search(value, current.children.first)){
                    return this.search(value, current.children.first);
                }
                else{
                    current = current.next;
                    return this.search(value, current);
                }
            }
            else{
                current = current.next;
                return this.search(value, current);
            }
        }
    }
    else{
        if(current.value == value){
            return current;
        }
        else{
            if(current.children.first){
                if(this.search(value, current.children.first)){
                    return this.search(value, current.children.first)
                }
                else{
                    return null;
                }
            }
            else{
                return null;
            }
        }
    }
}

function TreePrint(current = this.root){
    if(current.children.first){
        console.group(current.value);
        this.print(current.children.first);
        console.groupEnd();

        if(current.next){
            current = current.next;
            this.print(current);
        }
    }
    else{
        if(current.next){
            console.log(current.value);
            this.print(current.next);
        }
        else{
            console.log(current.value);
        }
    }
}