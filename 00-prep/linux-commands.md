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

# Process Hunting & Termination
### Scenario
Eliminate a persistent backdoor using only its saved PID — no process name.
### Commands
```bash
#Attacker Actions (Launch fake malware runs in background and hide the PID file)
sleep 9999 &
echo $! > rogue.pid

#Pentester Actions (Terminate it silently using only the attacker’s own PID file)
ps aux | grep sleep
kill $(cat rogue.pid)
```
