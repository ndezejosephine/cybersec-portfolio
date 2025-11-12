# File System Forensics

## Goal
Practice file creation, permissions, timestamps — core forensic skills.

## Commands
```bash
#Attacker Actions (Hiding the Flag)
mkdir -p ~/lab/evidence && cd ~/lab/evidence
echo "SECRET: flag{linux_is_cool}" > flag.txt
chmod 600 flag.txt
touch -t 202001010000 oldfile.txt

#Pentester Actions (Finding the Flag)
find . -type f -exec ls -la {} \;
```

## Proof
Extracted flag: `flag{linux_is_cool}`