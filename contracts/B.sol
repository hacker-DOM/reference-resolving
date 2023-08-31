pragma solidity 0.8.0;

import "./A.sol";

contract B is A {
    function b_main() public pure {
        a_main();
    }
}

