# Defined in - @ line 1
function config --wraps='git --git-dir=/home/halvard/Dotfiles --work-tree=/home/halvard' --description 'alias config git --git-dir=/home/halvard/Dotfiles --work-tree=/home/halvard'
  git --git-dir=/home/halvard/Dotfiles --work-tree=/home/halvard $argv;
end
