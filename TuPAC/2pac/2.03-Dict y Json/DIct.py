from printDict import *
dct = { 
    "Root/":{ 
        "directorio1/":{
            "type":"folder",
            "date":"2019",
            "user":"myPc",
            "children":{
                "archive1":{
                    "type":"archive",
                    "extension":"mp3",
                    "date":"2019"},
                "dir1/":{
                    "type":"folder",
                    "date":"2019",
                    "user":"myPc",
                    "children":{
                        "archive1":{
                        "type":"archive",
                        "extension":"mp3",
                        "date":"2019"},
                        "archive2":{     
                        "type":"archive",
                        "extension":"mp4",
                        "date":"2019"}       
                    }   
                }
            }
        }, 
        "directorio2/":{
            "type":"folder",
            "date":"2019",
            "user":"myPc",
            "children":{}
        }, 
        "arvhivo1":{
            "type":"archive",
            "extension":"mp4",
            "date":"2019"
        }
    } 
}
dct2 = {"root/":{"Dir1/":{"Dir2/":{"Archive":{"size":200,"date":"2019"}},"Archive":{"size":200,"date":"2019"}}}}

printDict(dct2)