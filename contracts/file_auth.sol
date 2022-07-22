pragma solidity ^0.5.16;

contract file_auth {
    uint public taskcount=0;
    string public emptyarry;
    struct File_in{
        uint id;
        string content;
        string file_name;
        string last_update;
        string location;
        bool allowed;

    }

    mapping(uint => File_in) public tasks;
    
    event Fileadded(
        uint id,
        string content,
        string file_name,
        string last_update,
        string location,
        bool completed
    );
    event Fileallowed(
        uint id,
        bool allowed
    );
    constructor() public {
        //createtask("onefile");
        //string memory _file_name, string memory _last_update,string memory _location
    }

    // this part recievs and stores the data to the stract file type
    function createtask(string memory _content,string memory _file_name, string memory _last_update,string memory _location) public {
        taskcount ++;
        tasks[taskcount]= File_in(taskcount,_content,_file_name,_last_update,_location,false);
        emit Fileadded(taskcount, _content,_file_name,_last_update,_location, false);
    }
    /*function allow(uint _id, bool role) public{
       if (role){
            File_in memory _file = tasks[_id];
            _file.allowed = !_file.allowed;
            tasks[_id]= _file;
            emit Fileallowed(_id, _file.allowed);
       }
    }*/



    // this function gets the data that has been saved and compare it with the data from the user
    function check(string memory _content, string memory _file_name, string memory _last_update, string memory _path) public view returns(bool){
        uint i;
        
        for (i=0; i<taskcount; i++){
            
            File_in memory _file = tasks[i];
            //if(keccak256(abi.encodePacked((_file.content))) == keccak256(abi.encodePacked((_content)))){
              //  return (true,_file.histogram,_file.DCT);
            //}

            if(keccak256(abi.encodePacked(_file.file_name))==keccak256(abi.encodePacked(_file_name))){
                if(keccak256(abi.encodePacked(_file.location))==keccak256(abi.encodePacked(_path)) && keccak256(abi.encodePacked(_file.last_update))==keccak256(abi.encodePacked(_last_update)) && _file.allowed==true){
                    //this if statment compares the hash
                    if(keccak256(abi.encodePacked((_file.content))) == keccak256(abi.encodePacked((_content)))){
                        return _file.allowed;
                    }
                    else{
                        
                            return false;
                    }
                }
            }
            
            
        }
        return false;
    }
}