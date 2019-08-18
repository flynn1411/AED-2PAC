function Node(value){
        this.value = value;
        this.next = null;
    }

    function LinkedList(){
        this.first = null;

        this.add = LinkedListAdd;
        this.print = LinkedListPrint;
    }

    function LinkedListAdd(newNode){

        if(!this.first){
            this.first = newNode;
        }

        else{
            current = this.first;
            previous = null;
            compare = new Compare();

            while(current){
                //Si el valor del actual es menor al valor del que deseo agregar
                if(compare.compare(current.value, newNode.value) < 0){
                    if(!current.next){
                        /*Si no hay siguiente del actual y se debe de seguir avanzando,
                          el nuevo nodo se agrega al final de la lista.*/
                        current.next = newNode;
                        return true;
                    }
                    else{
                        //Si tiene siguiente se sigue avanzando en la lista
                        previous = current;
                        current = current.next;
                    }
                }
                //Si el valor del actual es el mismo al que deseo agregar, reemplazo el nodo
                else if(compare.compare(current.value, newNode.value) == 0){
                    if(!previous){
                        //Si no tiene previo, esto me indica que el nodo a reemplazar es el primero de la lista
                        newNode.next = current.next;
                        this.first = newNode;
                        return true;
                    }
                    else{
                        //si el atual no tiene siguiente no hay necesidad de enlazar un nulo al nuevo nodo, ya lo tiene
                        if(!current.next){
                            previous.next = newNode;
                            return true;
                        }
                        //Si no se reemplaza normalmente
                        else{
                            previous.next = newNode;
                            previous.next.next = current.next;
                            return true;
                        }
                    }
                }
                //si el actual es mayor al que se desea agregar
                else{
                    //si no tiene previo, el nuevo será el primero en la lista
                    if(!previous){
                        this.first = newNode;
                        this.first.next = current;
                        return true;
                    }
                    else{
                        newNode.next = current;
                        previous.next = newNode;
                        return true;
                    }
                }
            }
            return false;
            
        }

    }

    function LinkedListPrint(){
        current = this.first;
        trail = " ";
        while(current.next){
            trail += current.value + " -> ";
            current = current.next;
        }

        trail += current.value;

        console.log(trail);
    }