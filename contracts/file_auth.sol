pragma solidity ^0.5.16;

contract file_auth {
    uint public taskcount=0;

    struct File_in{
        uint id;
        string content;
        bool allowed;
    }

    mapping(uint => File_in) public tasks;
    constructor() public {
        createtask("onefile");
    }
    function createtask(string memory _content) public {
        taskcount ++;
        tasks[taskcount]= File_in(taskcount,_content, false);
        
    }

}