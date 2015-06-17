"""
Kathryn DiPippo
6/15/2015
LaserPlusLIF.py
- The main function. In matlab, this is the file that would be executed
- A main function is required to run the LaserPlusLIF function
- Eventually, every single function will be put into a single, fully commented file rather than having these
    all spread out like so
"""

def LaserPlusLIF(name, conc, total_runs, final_num_of_runs): #{		LIF2 features another variable num1
	name = strcat('A',name)#;	why does an A need to be appended?
	concentration = conc#;		what....form is concentration submitted as? why is this an array?
	run = 1#;
	spect = 1#;

	while (run <= total_runs): #{
		# # %set(handles.run_num,'String',num2str(run));
		# # a=InitLaser();
		Zurich_asynch_SINGLE(a)#;
		#-----there doesn't seem to be any purpose for the code below-----
		# # tmp1=strcat(name,num2str(concentration),'_',num2str(spect));
		# # tmp2=strcat(name,num2str(concentration),'_',num2str(spect+1));
		# # action=strcat('[',tmp1,',',tmp2,',wave]=pfile1();');
		pfile()					#eval(action);
		run++
		spect += 2
		time.sleep(1)			#pause(1)
	#}

	# # fclose(a);
	# # %makeMats;
	# # %load 'REF.mat'
	# # dev=[];
	for i in range (1,length(concentration)): #{	rewrote as for loop; retains same function; still don't know what length does here
		# # mn=strcat(name,num2str(concentration(i)));		this looks like we're creating the array for saving it
		# # eval(strcat(mn,'=[];'));						Michelle80=[];
		# # out=[];
		for j in range (1,spect) #{				rewrote as a for loop; it still retains the same function
			# # tmp=num2str(j);								tmp = '1'
			# # matname=strcat(mn,'_',tmp);
			# # %strev=[mn,'=[',mn,' ',matname,'./',matname,'REF];'];
			# # strev=['out=[out ',matname,'];'];
			# # eval(strev);
			# # dev=[dev; mean(std(out,0,2))/mean(mean(out))];
		#}
	#}
	return [out,dev,wave]#;
#}

# ---------------------------------------------------------------------------------------------------------------------
def remove_outliers(final_num_of_runs): #{
	# # % outMinStd=out;
	# # % minStd=mean(std(out,0,2))/mean(mean(out));
	# # % numToRemove = total_runs - final_num_of_runs;
	for j in range (1,numToRemove): #{
		##run=size(outMinStd,2);
		for i in range (1,run): #{
	# # %         tempMinStd=[outMinStd(:,1:i-1) outMinStd(:,i+1:end)];
	# # %         newStd=mean(std(tempMinStd,0,2))/mean(mean(tempMinStd));
	# # %         if newStd<minStd #{
	# # %             minStd=newStd;   
	# # %             index=i;
	# # %         end
	# # %     end
	# # %     outMinStd=[outMinStd(:,1:index-1) outMinStd(:,index+1:end)];
	# # % end

# # %save 'Matlab090914';
#}
