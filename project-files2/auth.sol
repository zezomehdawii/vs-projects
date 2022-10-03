pragma solidity ^0.5.1;

contract BlockChanger{
    enum State {ACTIVE , DOWN} //Define the device state on the network (defined by the admin)
    uint public deviceCount = 0;
    address [] public device_addresses;
   // bool isAuthenticated = false;
    struct Device_Info
    {
        string name;
        string hash_id;
        //bool isAuthenticated;
        State device_state;
    }


    mapping (address => Device_Info) public device;

    function add_device (address _addr, string memory _name, string memory _hash_id) public
    {
        device_addresses.push(_addr);
        device[_addr].name = _name;
        device[_addr].hash_id = _hash_id;
        device[_addr].device_state = State.ACTIVE;
        deviceCount += 1;
    }

    function authFunc (string memory _hash_id) public view returns (bool)  
    {
        for (uint i = 0; i < device_addresses.length ; i++)
        {
            if (keccak256(abi.encodePacked(_hash_id)) == keccak256(abi.encodePacked(device[device_addresses[i]].hash_id)))
            {
                if(device[device_addresses[i]].device_state == State.ACTIVE)
                {
                    return true;
                }
            }
        }
        return false;     
    }   
    function deActivate (string memory _hash_id) public returns (bool)
    {
        for (uint i = 0; i < device_addresses.length ; i++)
        {
            if (keccak256(abi.encodePacked(_hash_id)) == keccak256(abi.encodePacked(device[device_addresses[i]].hash_id)))
            {
                device[device_addresses[i]].device_state = State.DOWN;
                return true;
            }
        }
        return false;
    }

    function Activate (string memory _hash_id) public returns (bool)
    {
        for (uint i = 0; i < device_addresses.length ; i++)
        {
            if (keccak256(abi.encodePacked(_hash_id)) == keccak256(abi.encodePacked(device[device_addresses[i]].hash_id)))
            {
                device[device_addresses[i]].device_state = State.ACTIVE;
                return true;
            }
        }
        return false;
    }



}