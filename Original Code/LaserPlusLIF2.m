function [out,outMinStd,dev,wave] = LaserPlusLIF2(name,conc,num,num1)
%name=name;
concentration=conc;
run=1;
spect=1;
%%%%%

while run<=num
    %set(handles.run_num,'String',num2str(run));
    a=InitLaser();
    Zurich_asynch_SINGLE(a);
    tmp1=strcat(name,num2str(concentration),'_',num2str(spect));
    tmp2=strcat(name,num2str(concentration),'_',num2str(spect+1));
    action=strcat('[',tmp1,',',tmp2,',wave]=pfile1();');
    eval(action);
    run=run+1;
    spect=spect+2;
    %pause(1);
end

fclose(a);
%makeMats;
load 'REF.mat'
i=1;
dev=[];
while i<=length(concentration)
    j=1;
    mn=strcat(name,num2str(concentration(i)));
    eval(strcat(mn,'=[];'));
    out=[];
    while j<=spect-1      
        tmp=num2str(j);
        matname=strcat(mn,'_',tmp);
        %strev=[mn,'=[',mn,' ',matname,'./',matname,'REF];'];
        strev=['out=[out ',matname,'./REF];'];
        eval(strev);
        dev=[dev; mean(std(out,0,2))/mean(mean(out))];
        j=j+1;
    end
    i=i+1;
end

outMinStd=out;
minStd=mean(std(out,0,2))/mean(mean(out));
numToRemove=num1;
for j=1:numToRemove
    run=size(outMinStd,2);
    for i=1:run
        tempMinStd=[outMinStd(:,1:i-1) outMinStd(:,i+1:end)];
        newStd=mean(std(tempMinStd,0,2))/mean(mean(tempMinStd));
        if newStd<minStd
            minStd=newStd;   
            index=i;
        end
    end
    outMinStd=[outMinStd(:,1:index-1) outMinStd(:,index+1:end)];
end

%save 'Matlab090914';
end
