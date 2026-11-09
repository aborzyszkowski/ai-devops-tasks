const IPV4_REGEX = /^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(?![\s\S])/;

function isValidIPv4(address) {
  return typeof address === 'string' && IPV4_REGEX.test(address);
}

module.exports = isValidIPv4;
