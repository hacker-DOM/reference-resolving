pragma solidity 0.8.1;

import "./A.sol";

contract B is A {
    function b2_main() public pure {
        a_main();
    }
}
