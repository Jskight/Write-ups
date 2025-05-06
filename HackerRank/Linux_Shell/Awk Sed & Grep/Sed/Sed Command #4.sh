# For each credit card number, print its masked version on a new line.
sed -r 's/[0-9]{4}[ ]/**** /g'