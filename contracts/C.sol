pragma solidity 0.8.1;

import "./A.sol";

contract C is A {
    function c_main() public pure {
        a_main();
    }
}
