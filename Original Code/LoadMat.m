s = what; %look in current directory
%s=what('dir') %change dir for your directory name 
matfiles=s.mat
for a=1:numel(matfiles)
load(char(matfiles(a)))
end