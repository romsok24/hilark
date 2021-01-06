alias ll='ls -halF'
alias la='ls -A'
alias l='ls -CF'
alias rm='/bin/rm -iv'
alias dfr='df -h -x tmpfs -x devtmpfs | grep -v loop'
alias ip='ip --color'
alias gpg='gpg --pinentry loopback'

source <(microk8s.kubectl completion bash)
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;36m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
