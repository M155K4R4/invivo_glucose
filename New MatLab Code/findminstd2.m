function [outMinStd] = findminstd2(data,num1)

out=data;
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
