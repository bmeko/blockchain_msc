const file_auth = artifacts.require("file_auth");

module.exports = function (deployer) {
  deployer.deploy(file_auth);
};
