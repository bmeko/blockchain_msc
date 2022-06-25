pragma solidity ^0.5.16;

contract file_auth {
    uint public taskcount=0;

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
    }
    function createtask(string memory _content,string memory _file_name, string memory _last_update,string memory location) public {
        taskcount ++;
        tasks[taskcount]= File_in(taskcount,_content,_file_name,_last_update,location,false);
        emit Fileadded(taskcount, _content,_file_name,_last_update,location, false);
    }
    function allow(uint _id, bool role) public{
       if (role){
            File_in memory _file = tasks[_id];
            _file.allowed = !_file.allowed;
            tasks[_id]= _file;
            emit Fileallowed(_id, _file.allowed);
       }
    }
    function check(string memory _content) public view returns(bool){
        uint i;
        
        for (i=0; i<taskcount; i++){
            File_in memory _file = tasks[i];
            if(keccak256(abi.encodePacked((_file.content))) == keccak256(abi.encodePacked((_content)))){
                return true;
            }
        }
    }
}
